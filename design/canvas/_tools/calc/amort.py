# -*- coding: utf-8 -*-
"""부채 상각 시뮬레이터. 만원 단위, 월 단위."""
from dataclasses import dataclass

@dataclass
class Debt:
    name: str
    bal: float
    apr: float        # 연 %
    minimum: float    # 월 최소 상환 (만원)
    fixed_term: int = 0   # >0이면 무이자성 할부: 남은 회차

    @property
    def i(self): return self.apr / 100 / 12


def simulate(debts, extra=0.0, order='avalanche', start=(2026, 9), cap_months=600):
    """상환 시뮬레이션. 완제 순서/월/총이자를 돌려준다."""
    ds = [Debt(d.name, d.bal, d.apr, d.minimum, d.fixed_term) for d in debts]
    key = (lambda d: -d.apr) if order == 'avalanche' else (lambda d: d.bal)
    interest = 0.0
    payoff = {}
    m = 0
    while any(d.bal > 1e-9 for d in ds) and m < cap_months:
        m += 1
        # 1) 이자 발생 (할부는 수수료가 회차에 포함된 것으로 보고 이자 미발생)
        for d in ds:
            if d.bal > 0 and not d.fixed_term:
                it = d.bal * d.i
                d.bal += it
                interest += it
        # 2) 최소 상환
        pool = extra
        for d in ds:
            if d.bal <= 0: continue
            pay = min(d.minimum, d.bal)
            d.bal -= pay
            pool += d.minimum - pay          # 다 갚고 남은 최소분은 눈덩이로
        # 3) 눈덩이 + 추가분을 우선순위 1위에 몰아준다
        while pool > 1e-9:
            live = sorted([d for d in ds if d.bal > 1e-9], key=key)
            if not live: break
            t = live[0]
            pay = min(pool, t.bal)
            t.bal -= pay
            pool -= pay
        for d in ds:
            if d.bal <= 1e-9 and d.name not in payoff:
                payoff[d.name] = m
    y, mo = start
    def ym(k):
        t = (y * 12 + (mo - 1)) + (k - 1)
        return t // 12, t % 12 + 1
    return {'months': m, 'interest': interest,
            'payoff': {k: ym(v) for k, v in sorted(payoff.items(), key=lambda x: x[1])},
            'payoff_m': dict(sorted(payoff.items(), key=lambda x: x[1])),
            'end': ym(m)}


def show(tag, r):
    y, mo = r['end']
    print(f'{tag:16} 완제 {y}년 {mo}월 ({r["months"]}개월 = {r["months"]//12}년 {r["months"]%12}개월) · 총이자 {r["interest"]:,.0f}만원')
    for n, (yy, mm) in r['payoff'].items():
        print(f'                 {n:10} {yy}년 {mm:2}월 완제 ({r["payoff_m"][n]}개월)')


# ── 지금 시안의 수치 ─────────────────────────────────────────
NOW = [Debt('주택담보대출', 6200, 3.4, 32),
       Debt('신용대출', 2480, 6.8, 21),
       Debt('카드 할부', 180, 14.5, 20, fixed_term=9)]
print('=== 현재 시안 수치로 실제 계산하면')
show('최소만', simulate(NOW))
show('추가 20만', simulate(NOW, 20))
show('소액 우선 20만', simulate(NOW, 20, order='snowball'))
print('\n  → 고금리 우선과 소액 우선이 완전히 같습니다.')
print('     카드 할부가 잔액도 가장 작고 금리도 가장 높아 두 전략의 순서가 동일하기 때문입니다.')
print('     "고금리 우선이 120만원 절약"은 이 데이터에서 성립할 수 없습니다.')

# ── 새 구성: 총부채 8,860만 유지, 학자금(작지만 저금리)을 넣어 두 전략을 가른다 ──
NEW = [Debt('주택담보대출', 6200, 3.4, 32),
       Debt('신용대출',   2200, 6.8, 20),
       Debt('학자금대출',   280, 2.5, 5),
       Debt('카드 할부',    180, 14.5, 20, fixed_term=9)]
print('\n=== 새 구성 (총부채 %d만 · 월 최소 %d만)' % (sum(d.bal for d in NEW), sum(d.minimum for d in NEW)))
w = sum(d.bal*d.apr for d in NEW)/sum(d.bal for d in NEW)
print(f'    가중 평균 연 {w:.2f}%  ·  구성: ' + ' · '.join(f'{d.name[:2]} {d.bal/sum(x.bal for x in NEW)*100:.0f}%' for d in NEW))
for ex in (0, 15):
    print()
    show(f'최소만' if ex == 0 else f'고금리+추가{ex}만', simulate(NEW, ex))
    if ex:
        show(f'소액+추가{ex}만', simulate(NEW, ex, order='snowball'))
        a = simulate(NEW, ex); b = simulate(NEW, ex, order='snowball')
        print(f'                 → 고금리 우선이 이자 {b["interest"]-a["interest"]:,.0f}만원 적고, '
              f'완제가 {b["months"]-a["months"]}개월 빠릅니다')
