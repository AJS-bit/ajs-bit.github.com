# -*- coding: utf-8 -*-
"""원본 앱 engine/finance.ts의 simulateDebt를 파이썬으로 그대로 옮긴 것 (만원 단위).

이 파일이 정답입니다. amort.py는 여기에 맞춰야 하고, 어긋나면 amort.py가 틀린 것입니다.
crosscheck.py가 두 구현을 대조합니다.

핵심 규칙 — 예산은 `모든 최소 상환의 합 + 추가분`으로 고정됩니다.
부채를 다 갚아도 그 최소 상환액은 사라지지 않고 다음 대상으로 굴러갑니다.
"""
def simulate_debt(debts, extra=0.0, strategy='avalanche', max_months=600):
    lst = [dict(name=d['name'], rate=d['apr']/100/12, balance=float(d['balance']),
                min=max(d['minimum'], 0.0), paid=None, interest=0.0)
           for d in debts if d['balance'] > 0]
    budget = sum(d['min'] for d in lst) + (0.0 if strategy == 'current' else extra)
    total, m, feasible = 0.0, 0, True
    timeline = []
    while any(d['balance'] > 0.00005 for d in lst) and m < max_months:   # 0.5원 = 0.00005만원
        m += 1
        pool = budget
        for d in lst:
            if d['balance'] <= 0: continue
            it = d['balance'] * d['rate']
            d['balance'] += it; d['interest'] += it; total += it
        for d in lst:
            if d['balance'] <= 0: continue
            pay = min(d['min'], d['balance'], pool)
            d['balance'] -= pay; pool -= pay
        order = sorted(lst, key=(lambda d: d['balance']) if strategy == 'snowball' else (lambda d: -d['rate']))
        for d in order:
            if pool <= 0: break
            if d['balance'] <= 0: continue
            pay = min(d['balance'], pool)
            d['balance'] -= pay; pool -= pay
        for d in lst:
            if d['balance'] <= 0.00005 and d['paid'] is None:
                d['paid'] = m; d['balance'] = 0.0
        rem = sum(max(0.0, d['balance']) for d in lst)
        timeline.append(rem)
        if m > 2 and rem >= timeline[m-3]: feasible = False; break
    return dict(months=m, interest=total, feasible=feasible and m < max_months,
                order=[(d['name'], d['paid'], d['interest']) for d in lst])

def ym(k, start=(2026, 9)):
    t = start[0]*12 + (start[1]-1) + k
    return f'{t//12}년 {t%12+1}월'

if __name__ == '__main__':
    D = [dict(name='주택담보대출', balance=6200, apr=3.4,  minimum=32),
         dict(name='신용대출',     balance=2200, apr=6.8,  minimum=20),
         dict(name='학자금대출',   balance=280,  apr=2.5,  minimum=5),
         dict(name='카드 할부',    balance=180,  apr=14.5, minimum=20)]

    print('=== 원본 엔진(simulateDebt)을 그대로 돌린 결과')
    for tag, st, ex in (('고금리 우선 +15만','avalanche',15), ('소액 우선 +15만','snowball',15), ('최소만','current',0)):
        r = simulate_debt(D, ex, st)
        print(f'  {tag:16} 완제 {ym(r["months"]):11} ({r["months"]:3}개월) · 총이자 {r["interest"]:7,.0f}만원')
        if st == 'avalanche':
            for n_, p, i in sorted(r['order'], key=lambda x: x[1] or 999):
                print(f'      {n_:10} {ym(p):11} · 이자 {i:6,.0f}만원')
