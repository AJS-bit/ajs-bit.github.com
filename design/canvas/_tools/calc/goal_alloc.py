# -*- coding: utf-8 -*-
"""목적지 배분 — 앱 lib/navi-goals.ts naviGoalAllocation + lib/engine/finance.ts allocateGoals · requiredSaving ·
monthsToTarget + lib/navi-goal-tools.ts 도착 달(goalArrivalMonths · goalArrivalOffset · goalDeadline)을 그대로 옮긴 것(원 단위).

goals.py 는 옛 시안 모형(명목 월이율 apr/12 · 월 배분 35 + 28 = 63만원을 시안이 정함)이라 이제 숫자의 출처가 아니다. 앱은
 - 매달 나눠 넣을 돈(budget) = max(0, 매달 모을 수 있는 돈) — 저축 이체 63만원이 아니라 capacity(89.6만원)
 - 목적지마다 필요한 돈 = requiredSaving(목표액, 지금 모은 돈, round(목표일까지 남은 달), 유형 수익률) — 월 복리율은 (1 + 연)^(1/12) − 1
   유형 수익률: 비상금 · 일반 저축 0% · 투자 = 그 목적지의 수익률(없으면 투자 자산 기본 수익률) · 순자산 = 자산 가중 평균 수익률
 - 모자라면 가중치 (4 − 우선순위) × (1 + min(3, 24 ÷ 남은 달))로 나눈다 — 필요한 돈보다 몫이 크면 필요한 돈만 주고 남은 돈을 다시 나눈다
 - 부채 상환 목적지는 배분에 들지 않고 상환 계획(simulateDebt)의 다 갚는 달로, 순자산 목적지의 도착은 미래 경로(보통)로 본다
   (순자산 목적지도 목표일이 있으면 필요한 돈이 합계와 배분에 든다 — 그래서 시안의 순자산 2억원 목표일은 필요액이 0인 2058-10-08이다)

    python3 goal_alloc.py
"""
import math
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from sample import load, m_rate, months_until, month_index, add_months, month_label, months_text, compact, js_round  # noqa: E402
from engine_ref import simulate_debt  # noqa: E402
import projection  # noqa: E402

GOAL_ETA_CAP_MONTHS = 360
UNREACHABLE = '지금 배분으로는 도착하기 어려워요'


def clamp(v, lo, hi):
    return min(hi, max(lo, v))


def required_saving(target, current, months_n, annual):
    N = max(1, js_round(months_n))
    r = m_rate(annual)
    if r == 0:
        return max(0.0, (target - current) / N)
    g = (1 + r) ** N
    return max(0.0, (target - current * g) / ((g - 1) / r))


def months_to_target(target, current, pmt, annual):
    if current >= target:
        return 0
    r = m_rate(annual)
    if r <= 0:
        return (target - current) / pmt if pmt > 0 else None
    num, den = target * r + pmt, current * r + pmt
    if den <= 0 or num / den <= 0:
        return None
    mm = math.log(num / den) / math.log(1 + r)
    return mm if math.isfinite(mm) and 0 < mm < 1200 else None


def goal_type(g):
    return {'emergency': 'emergency', 'investment': 'investment', 'debt-payoff': 'debt-payoff', 'net-worth': 'net-worth'}.get(g['kind'], 'saving')


def net_worth(S):
    return sum(a['value'] for a in S['assets']) - sum(d['balance'] for d in S['debts'])


def goal_return(S, g):
    """naviGoalAnnualReturn"""
    t = goal_type(g)
    if t == 'investment':
        return g['annualReturn'] / 100 if 'annualReturn' in g else S['expected_return']
    if t != 'net-worth':
        return 0.0
    tot = sum(max(0, a['value']) for a in S['assets'])
    return sum(max(0, a['value']) * a['rate'] for a in S['assets']) / tot if tot > 0 else 0.0


def saving_row(S, g):
    now = S['now']
    saved = max(0, net_worth(S)) if goal_type(g) == 'net-worth' else g['saved']
    left = max(0.0, months_until(g.get('targetDate'), now) or 0.0)
    ret = goal_return(S, g)
    required = required_saving(g['target'], saved, left, ret) if left > 0 else max(0.0, g['target'] - saved)
    urgency = 1 + clamp(24 / max(left, 1), 0, 3) if left > 0 else 4
    needs_date = saved < g['target'] and (not g.get('targetDate') or g['targetDate'] < now.isoformat())
    row = dict(name=g['name'], type=goal_type(g), priority=g['priority'], targetDate=g.get('targetDate'), saved=saved, target=g['target'],
               monthsLeft=left, required=required, weight=(4 - clamp(g['priority'], 1, 3)) * urgency, ret=ret, needsTargetDate=needs_date,
               progress=clamp(saved / g['target'] * 100, 0, 100) if g['target'] > 0 else 0)
    if needs_date:
        row.update(required=0.0, weight=0.0)
    return row


def debt_row(S, g):
    now = S['now']
    linked = [d for d in S['debts'] if d['name'] in g['debts']]
    remaining = sum(max(0, d['balance']) for d in linked)
    extra = 0 if S['strategy'] == 'current' else max(0, S['extra'])
    run = simulate_debt(S['debts'], extra, S['strategy'], unit=1)
    paid = [next(p for n, p, _ in run['order'] if n == d['name']) for d in linked]
    eta = max(paid) if paid and all(p is not None for p in paid) else None
    target = max(g.get('originalPrincipal', 0), remaining)
    saved = min(target, max(0, target - remaining))
    left = max(0.0, months_until(g.get('targetDate'), now) or 0.0)
    return dict(name=g['name'], type='debt-payoff', priority=g['priority'], targetDate=g.get('targetDate'), saved=saved, target=target,
                monthsLeft=left, required=0.0, weight=0.0, allocated=0.0, gap=0.0, eta=eta, needsTargetDate=False,
                progress=clamp(saved / target * 100, 0, 100) if target > 0 else 0)


def allocate(S, cap=None):
    """naviGoalAllocation(state, capacity)"""
    if cap is None:
        cap = projection.capacity(S)
    budget = max(0.0, cap)
    rows = [saving_row(S, g) for g in S['goals'] if goal_type(g) != 'debt-payoff']
    active = [r for r in rows if r['required'] > 0 and r['saved'] < r['target']]
    total = sum(r['required'] for r in active)
    shares, remaining, pending = {}, min(budget, total), list(active)
    while pending and remaining > 0:
        W = sum(r['weight'] for r in pending) or 1
        capped = [r for r in pending if r['required'] <= remaining * r['weight'] / W]
        if not capped:
            for r in pending:
                shares[r['name']] = remaining * r['weight'] / W
            break
        for r in capped:
            shares[r['name']] = r['required']; remaining -= r['required']
        pending = [r for r in pending if r['name'] not in shares]
    for r in rows:
        complete = r['saved'] >= r['target']
        act = r['required'] > 0 and not complete
        r['allocated'] = shares.get(r['name'], 0.0) if act else 0.0
        r['gap'] = max(0.0, r['required'] - r['allocated']) if act else 0.0
        r['eta'] = 0 if complete else None if r['needsTargetDate'] else months_to_target(r['target'], r['saved'], r['allocated'], r['ret'])
        if r['type'] == 'net-worth':                          # 도착은 미래 경로(goalEtaMonths)
            r['eta_alloc'] = r['eta']
            r['eta'] = projection.net_worth_eta(S, r['target'])
    rows += [debt_row(S, g) for g in S['goals'] if goal_type(g) == 'debt-payoff']
    rows.sort(key=lambda r: (r['priority'], r['monthsLeft'], r['name']))
    for r in rows:
        saving = r['type'] not in ('debt-payoff', 'net-worth')
        r['arrival'] = arrival_label(S, r['eta'], GOAL_ETA_CAP_MONTHS if saving else math.inf, r['targetDate'] if saving else None)
        r['deadline'] = deadline(S, r['eta'], r['targetDate'], GOAL_ETA_CAP_MONTHS if saving else math.inf, saving)
    return dict(budget=budget, totalRequired=total, surplus=budget - total, rows=rows)


# ── 도착 달 · 목표일 대비(navi-goal-tools.ts) ─────────────────────────────
def arrival_months(eta):
    return max(0, math.ceil(eta - 0.1))


def reachable(eta, cap=GOAL_ETA_CAP_MONTHS):
    return isinstance(eta, (int, float)) and math.isfinite(eta) and arrival_months(eta) <= cap


def _target_index(iso):
    if not iso:
        return None
    y, m = int(iso[:4]), int(iso[5:7])
    return month_index(y, m) if 1 <= m <= 12 else None


def arrival_offset(S, eta, saving_target=None):
    now = S['now']
    months = arrival_months(eta)
    target = _target_index(saving_target) if saving_target else None
    left = months_until(saving_target, now) if saving_target else None
    if target is None or left is None or not left > 0:
        return months
    payments = max(1, js_round(left))
    return max(0, target - month_index(now.year, now.month) + months - payments)


def arrival_label(S, eta, cap=GOAL_ETA_CAP_MONTHS, saving_target=None):
    if not reachable(eta, cap):
        return None
    return month_label(S['now'].year, S['now'].month, arrival_offset(S, eta, saving_target))


def deadline(S, eta, target_date, cap=GOAL_ETA_CAP_MONTHS, saving=False):
    now = S['now']
    target = _target_index(target_date)
    gap = None
    if target is not None and reachable(eta, cap):
        gap = month_index(now.year, now.month) + arrival_offset(S, eta, target_date if saving else None) - target
    if target is not None and target_date[:10] < now.isoformat():
        return dict(kind='passed', gap=gap, text='목표일이 지났어요')
    if not reachable(eta, cap):
        return dict(kind='unreachable', gap=None, text=UNREACHABLE)
    if gap is None:
        return dict(kind='no-date', gap=None, text='목표일이 없어요')
    if gap < 0:
        return dict(kind='early', gap=gap, text=f'목표일보다 약 {months_text(-gap)} 빨라요')
    if gap > 0:
        return dict(kind='late', gap=gap, text=f'목표일보다 약 {months_text(gap)} 늦어요')
    return dict(kind='on-time', gap=gap, text='목표일에 맞춰 도착해요')


if __name__ == '__main__':
    S = load()
    a = allocate(S)
    print(f'매달 모을 수 있는 돈 {a["budget"]:,.0f}원 · 모두 도착하려면 {a["totalRequired"]:,.0f}원 · '
          f'{"남는 돈" if a["surplus"] >= 0 else "모자란 돈"} {abs(a["surplus"]):,.0f}원')
    for r in a['rows']:
        print(f'  {r["name"]:14} 우선 {r["priority"]} · 가중 {r["weight"]:.3f} · 필요 {r["required"]:>11,.0f} · 매달 {r["allocated"]:>11,.0f} '
              f'· {r["arrival"]} · {r["deadline"]["text"]}')
