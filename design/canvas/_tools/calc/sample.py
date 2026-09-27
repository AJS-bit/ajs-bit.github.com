# -*- coding: utf-8 -*-
"""design/sample-data.json 을 계산기 입력으로 읽는다(원 단위). goal_alloc · limits · projection 이 함께 쓴다.

앱의 시각 규칙을 그대로 옮긴 작은 도우미도 여기 둔다 — 달 더하기(addMonths) · 남은 달(monthsUntil) · JS Math.round.
기준일은 sample-data.json 의 asOf(2026-09-08, 서울 정오).
"""
import json
import math
import pathlib
from datetime import date

SAMPLE = pathlib.Path(__file__).resolve().parents[3] / 'sample-data.json'

TYPE_OF = {'부동산': 'realestate', '투자': 'investment', '연금': 'pension', '현금성': 'cash', '기타': 'other'}


def js_round(x):
    """JS Math.round — .5는 +∞ 쪽으로."""
    return math.floor(x + 0.5)


def load(path=SAMPLE):
    d = json.loads(pathlib.Path(path).read_text(encoding='utf-8'))
    p, m = d['profile'], d['month']
    y, mo, dd = map(int, d['asOf'].split('-'))
    return {
        'now': date(y, mo, dd),
        'salary': p['netSalary'], 'side': p['sideIncome'], 'income': p['netSalary'] + p['sideIncome'],
        'target_pct': p['spendTargetPct'], 'expected_return': p['expectedReturn'] / 100, 'risk': 'balanced',
        'spend': m['spendSoFar'], 'projected': m['spendProjected'],
        'assets': [dict(name=a['name'], type=TYPE_OF[a['type']], value=a['value'], rate=a['rate'] / 100) for a in d['assets']],
        'debts': [dict(name=x['name'], type=x['type'], balance=x['balance'], apr=x['apr'], minimum=x['minimum']) for x in d['debts']],
        'strategy': d['repayment']['strategy'], 'extra': d['repayment']['extraMonthly'],
        'goals': d['goals'],
        'raw': d,
    }


# ── 달 · 날짜 (앱 engine/format.ts · navi-goal-tools.ts) ─────────────────────────────
def month_index(y, m):
    return y * 12 + (m - 1)


def add_months(y, m, k):
    """addMonths('YYYY-MM', k) — 앱의 달 셈: 이번 달 + k(이번 달을 1로 세지 않는다)."""
    t = month_index(y, m) + k
    return t // 12, t % 12 + 1


def month_label(y, m, k=0):
    yy, mm = add_months(y, m, k)
    return f'{yy}년 {mm}월'


def months_until(iso, now):
    """monthsUntil — (연 차 × 12) + 달 차 + 날짜 차 ÷ 30. 목표일이 없으면 None."""
    if not iso:
        return None
    y, m, d = map(int, iso.split('-'))
    return (y - now.year) * 12 + (m - now.month) + (d - now.day) / 30


def months_text(m):
    """engine months() — 「3년 2개월」."""
    if m is None:
        return '—'
    if m >= 12 * 80:
        return '80년+'
    t = max(0, js_round(m))
    yy, r = divmod(t, 12)
    if yy == 0:
        return f'{r}개월'
    if r == 0:
        return f'{yy}년'
    return f'{yy}년 {r}개월'


def compact(v):
    """engine compact() — 123456789 → '1억 2,346만' · 12340000 → '1,234만'."""
    raw = js_round(v)
    neg = '-' if raw < 0 else ''
    x = abs(raw)
    if x >= 100_000_000:
        eok, man = x // 100_000_000, js_round((x % 100_000_000) / 10_000)
        if man == 0:
            return f'{neg}{eok:,}억'
        if man == 10_000:
            return f'{neg}{eok + 1:,}억'
        return f'{neg}{eok:,}억 {man:,}만'
    if x >= 10_000:
        return f'{neg}{js_round(x / 10_000):,}만'
    return f'{neg}{x:,}'


def m_rate(annual):
    """engine mRate — 연 수익률(소수) → 월 복리율."""
    return (1 + annual) ** (1 / 12) - 1
