# -*- coding: utf-8 -*-
"""한도 · 히어로 · 하루 금액 — 앱 lib/navi-current.ts naviSpendingLimit(D1) · lib/navi-verdict.ts planCapInfo ·
lib/navi-limit-view.ts(오늘 포함 남은 날 · 10원 단위 하루 금액) · lib/navi-hero.ts targetLine을 그대로 옮긴 것(원 단위).

 - 판정 선(D1) = 직접 정한 한도, 아니면 월급 × 소비 목표 %. 월급이 없으면 판정하지 않는다(None).
 - 참고 정보 fromIncome = 월급 + 부수입 − min(목적지 필요액 합, (월급 + 부수입 − 대출상환) × 70%) − 대출상환.
   판정 선보다 작을 때만 「저축 · 상환 계획까지 지키려면 {N} 안에서 쓰면 돼요」로 보인다(planCapInfo).
 - 오늘 포함 남은 날 = max(1, 일수 − 지난 날 + 1) — 9월 8일 = 23일(예전 시안은 22일).
 - 하루 금액 = 남은 한도 ÷ 오늘 포함 남은 날, 10원 단위 반올림(roundDailyWon).
 - 히어로 오른쪽 줄 = 소비 목표 금액(월급 × 소비 목표 %) − 쓴 돈, 만 단위 원(「소비 목표까지 104만원 남음」).

    python3 limits.py
"""
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from sample import load, compact, js_round  # noqa: E402
import goal_alloc  # noqa: E402
import projection  # noqa: E402

DAYS, DONE = 30, 8          # 2026년 9월 · 8일


def verdict_total(S, manual=None):
    if manual and manual > 0:
        return manual
    return S['salary'] * S['target_pct'] / 100 if S['salary'] > 0 else None


def from_income(S, extra=None):
    inc = S['income']
    if not inc > 0:
        return None
    pay = projection.debt_pay(S, extra)
    need = min(goal_alloc.allocate(S, projection.capacity(S, extra))['totalRequired'], max(0, inc - pay) * 0.7)
    return max(0.0, inc - need - pay)


def plan_cap_info(S, extra=None):
    f, t = from_income(S, extra), verdict_total(S)
    return f if f is not None and t is not None and f < t else None


def days_left(days=DAYS, done=DONE):
    return max(1, min(days, days - done + 1))


def daily_won(remain, days=DAYS, done=DONE):
    return js_round(max(0, remain / days_left(days, done)) / 10) * 10 if remain > 0 else 0


def target_line(spent, salary, pct):
    shown, goal = js_round(spent), js_round(salary * pct / 100)
    if shown < goal:
        return f'소비 목표까지 {compact(goal - shown)}원 남음'
    if shown == goal:
        return '소비 목표에 딱 닿았어요'
    return f'소비 목표보다 {compact(shown - goal)}원 넘음'


def scene(S, spent):
    total = verdict_total(S)
    return dict(spent=spent, remain=total - spent, dailyWon=daily_won(total - spent), line=target_line(spent, S['salary'], S['target_pct']))


if __name__ == '__main__':
    S = load()
    t = verdict_total(S)
    print(f'판정 선(D1) {t:,.0f}원 = 월급 {S["salary"]:,}원 × 소비 목표 {S["target_pct"]}%')
    print(f'참고 정보 fromIncome {from_income(S):,.0f}원 → 「저축 · 상환 계획까지 지키려면 이번 달 {compact(plan_cap_info(S))}원 안에서 쓰면 돼요」')
    print(f'오늘 포함 {days_left()}일 남음')
    for tag, spent in (('9월 8일', S['spend']), ('완료 카드(+12,000)', S['spend'] + 12_000), ('이력 부족 히어로(5,000)', 5_000)):
        sc = scene(S, spent)
        print(f'  {tag:18} 남은 한도 {sc["remain"]:>9,}원 · 오늘 포함 하루 {sc["dailyWon"]:,}원 · {sc["line"]}')
