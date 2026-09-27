# -*- coding: utf-8 -*-
"""원본 앱 lib/engine/finance.ts의 simulateDebt를 파이썬으로 그대로 옮긴 것.

이 파일이 정답입니다. amort.py는 여기에 맞춰야 하고, 어긋나면 amort.py가 틀린 것입니다.
crosscheck.py가 두 구현을 대조하고, 이 파일을 앱이 실제로 낸 값(app_ref.json)과도 대조합니다.

핵심 규칙 — 예산은 `모든 최소 상환의 합 + 추가분`으로 고정됩니다.
부채를 다 갚아도 그 최소 상환액은 사라지지 않고 다음 대상으로 굴러갑니다.

2026-09-26 앱 v5-stage1(a724aac)에 다시 맞춤:
 - 'current'(최소 상환만)는 순서를 정렬하지 않는다 — 풀린 최소 상환액이 목록 순서대로 굴러간다(예전 포팅은 고금리 순).
 - 멈춤 규칙: 어느 부채도 줄지 않으면(anyDebtShrinking) 멈춤. 눈덩이는 끝까지. continue_after=True면 멈추지 않는다(미래 경로).
 - 달마다 남은 잔액 · 실제로 쓰지 않은 예산(freed)을 기록한다 — 미래 경로(projection.py)가 쓴다.
 - 달 이름은 앱과 같게 「이번 달 + n」(payoffMonthText). 예전 시안은 이번 달을 1로 세어 한 달 이르게 적었다(2036년 4월 → 5월).
금액 단위는 unit(원/단위)로 정한다 — 기본 만원(unit=10000), 0.5원 문턱도 그 단위로 바꾼다.
"""


def simulate_debt(debts, extra=0.0, strategy='avalanche', max_months=600, continue_after=False, unit=10_000):
    eps = 0.5 / unit
    lst = [dict(name=d['name'], rate=d['apr'] / 100 / 12, balance=float(d['balance']),
                min=max(d['minimum'], 0.0), paid=None, interest=0.0)
           for d in debts if d['balance'] > 0]
    if not lst:
        return dict(months=0, interest=0.0, feasible=True, order=[], timeline=[], simulated=0)
    budget = sum(d['min'] for d in lst) + (0.0 if strategy == 'current' else extra)

    def ordered():
        c = list(lst)
        if strategy == 'snowball':
            c.sort(key=lambda d: d['balance'])          # 안정 정렬(JS Array.sort와 같음)
        elif strategy == 'avalanche':
            c.sort(key=lambda d: -d['rate'])
        return c                                         # 'current' — 목록 순서 그대로

    total, m, timeline = 0.0, 0, []
    while any(d['balance'] > eps for d in lst) and m < max_months:
        m += 1
        pool = budget
        before = [d['balance'] for d in lst]
        for d in lst:
            if d['balance'] <= 0:
                continue
            it = d['balance'] * d['rate']
            d['balance'] += it; d['interest'] += it; total += it
        for d in lst:
            if d['balance'] <= 0:
                continue
            pay = min(d['min'], d['balance'], pool)
            d['balance'] -= pay; pool -= pay
        for d in ordered():
            if pool <= 0:
                break
            if d['balance'] <= 0:
                continue
            pay = min(d['balance'], pool)
            d['balance'] -= pay; pool -= pay
        for d in lst:
            if d['balance'] <= eps and d['paid'] is None:
                d['paid'] = m; d['balance'] = 0.0
        timeline.append(dict(month=m, balance=sum(max(0.0, d['balance']) for d in lst), freed=max(0.0, pool)))
        shrinking = any(d['balance'] < b for d, b in zip(lst, before))
        if not continue_after and strategy != 'snowball' and m > 2 and not shrinking:
            break
    ok = all(d['balance'] <= eps for d in lst)
    return dict(months=m if ok else None, simulated=m, interest=total, feasible=ok, timeline=timeline,
                order=[(d['name'], d['paid'], d['interest']) for d in lst])


def ym(k, start=(2026, 9)):
    """payoffMonthText — 지금 달 + k."""
    t = start[0] * 12 + (start[1] - 1) + k
    return f'{t // 12}년 {t % 12 + 1}월'


if __name__ == '__main__':
    D = [dict(name='주택담보대출', balance=6200, apr=3.4,  minimum=32),
         dict(name='신용대출',     balance=2200, apr=6.8,  minimum=20),
         dict(name='학자금대출',   balance=280,  apr=2.5,  minimum=5),
         dict(name='카드 할부',    balance=180,  apr=14.5, minimum=20)]

    print('=== 원본 엔진(simulateDebt)을 그대로 돌린 결과 · 달 이름은 앱과 같게(이번 달 + n)')
    for tag, st, ex in (('고금리 우선 +15만', 'avalanche', 15), ('소액 우선 +15만', 'snowball', 15),
                        ('추가 없이(기준선)', 'avalanche', 0), ('최소 상환만(current)', 'current', 0)):
        r = simulate_debt(D, ex, st)
        print(f'  {tag:18} 다 갚는 달 {ym(r["months"]):11} ({r["months"]:3}개월) · 총이자 {r["interest"]:7,.0f}만원')
        if st == 'avalanche' and ex:
            for n_, p, i in sorted(r['order'], key=lambda x: x[1] or 999):
                print(f'      {n_:10} {ym(p):11} · 이자 {i:6,.0f}만원')
