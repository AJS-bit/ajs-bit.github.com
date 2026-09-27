# -*- coding: utf-8 -*-
"""미래 경로 — 앱 lib/engine/finance.ts project() + lib/navi-current.ts naviProject()를 그대로 옮긴 것(원 단위).

net.py 는 옛 시안 모형(월 저축 63만원 · 자산 전체에 가중 2.4%)이라 이제 숫자의 출처가 아니다. 앱은
 - 매달 모으는 돈 = 매달 모을 수 있는 돈(capacity = 월급 + 부수입 − 월말 예상 소비 − 대출상환)
 - 지금 자산은 자산마다 넣은 수익률(현금성 · 기타를 뺀 자산은 투자 환경에 따라 보정), 새로 모은 돈은 투자 자산 기본 수익률(투자 환경 보정)
 - 부채를 다 갚고 풀린 상환액(freed)도 그달 모으는 돈에 더한다
로 경로를 그린다. 투자 환경 = RISK[balanced]: 조심스럽게 = r × 2/6 − 2%p · 보통 = r · 좋을 때 = r × 9/6 + 3%p.

    python3 projection.py
"""
import math
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from sample import load, m_rate, add_months, month_label, months_text, compact, js_round  # noqa: E402
from engine_ref import simulate_debt  # noqa: E402

RISK = {'conservative': (0.04, 0.01, 0.06), 'balanced': (0.06, 0.02, 0.09), 'aggressive': (0.08, 0.00, 0.13)}
NET_WORTH_MILESTONES = [10_000_000, 30_000_000, 50_000_000, 100_000_000, 150_000_000, 200_000_000,
                        300_000_000, 400_000_000, 500_000_000, 700_000_000, 1_000_000_000]


def scenario_rate(annual, scenario, risk='balanced'):
    """investmentScenarioRate"""
    exp, bad, good = RISK[risk]
    mult = bad / (exp or 1) if scenario == 'bad' else good / (exp or 1) if scenario == 'good' else 1
    shift = -0.02 if scenario == 'bad' else 0.03 if scenario == 'good' else 0
    return max(-0.5, annual * mult + shift)


def debt_pay(S, extra=None):
    ex = S['extra'] if extra is None else extra
    active = [d for d in S['debts'] if d['balance'] > 0]
    mins = sum(max(0, d['minimum']) for d in active)
    return mins + (max(0, ex) if active and S['strategy'] != 'current' else 0)


def capacity(S, extra=None, projected=None):
    """매달 모을 수 있는 돈 = 월급 + 부수입 − 월말 예상 소비 − 대출상환(naviMetrics.capacity)."""
    return S['income'] - (S['projected'] if projected is None else projected) - debt_pay(S, extra)


def project(S, months=120, scenario='base', spend_delta=0.0, extra=None, monthly_save=None):
    ex = S['extra'] if extra is None else extra
    assets = []
    for a in S['assets']:
        base = a['rate']
        rate = base if a['type'] in ('cash', 'other') else scenario_rate(base, scenario, S['risk'])
        assets.append([float(a['value']), m_rate(rate)])
    saving_rate = m_rate(scenario_rate(S['expected_return'], scenario, S['risk']))
    active = [d for d in S['debts'] if d['balance'] > 0]
    strategy = S['strategy'] or 'avalanche'
    ex = max(0, ex) if active and strategy != 'current' else 0
    total_pay = sum(max(0, d['minimum']) for d in active) + ex
    run = simulate_debt(active, ex, strategy, months + 12, continue_after=True, unit=1)
    base_save = (capacity(S, extra) if monthly_save is None else monthly_save) + spend_delta
    saved, series = 0.0, []
    start_net = sum(a['value'] for a in S['assets']) - sum(d['balance'] for d in S['debts'])
    for i in range(1, months + 1):
        for a in assets:
            a[0] *= 1 + a[1]
        if saved > 0:
            saved *= 1 + saving_rate
        step = run['timeline'][i - 1] if i - 1 < len(run['timeline']) else None
        bal = max(0.0, step['balance']) if step else 0.0
        freed = step['freed'] if step else (total_pay if run['feasible'] else 0)
        save = base_save + freed
        saved += save
        asum = sum(a[0] for a in assets) + saved
        series.append(dict(i=i, net=asum - bal, assets=asum, debts=bal, save=save))
    return dict(series=series, monthly_save=base_save, start_net=start_net, debt=run)


def estimate_text(v):
    """estimateText — 100만원 단위 반올림, 1억 이상은 소수 둘째 자리까지 「약 3.82억원」."""
    r = js_round(v / 1_000_000) * 1_000_000
    if abs(r) >= 100_000_000:
        s = f'{r / 100_000_000:.2f}'.rstrip('0').rstrip('.')
        return f'약 {s}억원'
    return f'약 {compact(r)}원'


def short_estimate(v):
    """shortEstimate — 옆 메뉴의 「3.8억」."""
    r = js_round(v / 1_000_000) * 1_000_000
    if abs(r) >= 100_000_000:
        s = f'{js_round(r / 10_000_000) / 10:.1f}'.rstrip('0').rstrip('.')
        return f'{s}억'
    return compact(r)


def milestones(S, count=3, months=600):
    """다음 자산 지점 — 사다리에서 지금 순자산보다 큰 가까운 count개, 경로(보통)가 처음 닿는 달."""
    p = project(S, months, 'base')
    net0 = p['start_net']
    now = S['now']
    out = []
    for t in [x for x in NET_WORTH_MILESTONES if x > net0][:count]:
        hit = next((pt for pt in p['series'] if pt['net'] >= t), None)
        if hit is None:
            out.append(dict(target=t, months=None, when=None, date=None))
        else:
            out.append(dict(target=t, months=hit['i'], when=f'{months_text(hit["i"])} 뒤', date=month_label(now.year, now.month, hit['i'])))
    return out


def net_worth_eta(S, target):
    """netWorthGoalEta — 보통 경로가 목표액에 처음 닿는 달까지 개월 수(600개월 안)."""
    p = project(S, 600, 'base')
    if p['start_net'] >= target:
        return 0
    hit = next((pt for pt in p['series'] if pt['net'] >= target), None)
    return None if hit is None else hit['i']


if __name__ == '__main__':
    S = load()
    print(f'매달 모을 수 있는 돈 {capacity(S):,.0f}원 · 새로 모은 돈 수익률 보통 {S["expected_return"]:.1%}')
    for sc, name in (('bad', '조심스럽게'), ('base', '보통'), ('good', '좋을 때')):
        p = project(S, 120, sc)
        fin = p['series'][-1]['net']
        print(f'  {name:6} 연 {scenario_rate(S["expected_return"], sc) * 100:5.1f}% → 10년 뒤 {estimate_text(fin)} ({fin:,.0f}원)')
    for m in milestones(S):
        print(f'  {compact(m["target"])}원 · {m["when"]} · {m["date"]}')
