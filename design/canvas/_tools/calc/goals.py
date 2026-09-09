# -*- coding: utf-8 -*-
"""목적지 도착 시점 계산. 만원·월 단위."""
def ym(k, start=(2026, 9)):
    t = start[0]*12 + (start[1]-1) + k
    return t//12, t%12+1

def months_to(target, cur, monthly, apr):
    """월말 납입 기준으로 target에 닿는 개월 수."""
    i = apr/100/12
    b, m = cur, 0
    while b < target and m < 1200:
        b = b*(1+i) + monthly
        m += 1
    return m

def required(target, cur, months, apr):
    """목표일까지 채우려면 필요한 월 납입."""
    i = apr/100/12
    if i == 0: return (target-cur)/months
    fv = cur*(1+i)**months
    af = ((1+i)**months - 1)/i
    return max(0.0, (target-fv)/af)

print('=== 목적지 도착 시점 (월 배분 기준)')
GOALS = [
    ('비상금 6개월',   1500, 1020, 35, 0.0),
    ('투자 계좌 5,000만원', 5000, 2100, 28, 5.0),
]
for name, tgt, cur, mo, r in GOALS:
    n = months_to(tgt, cur, mo, r)
    y, m = ym(n)
    print(f'  {name:18} {cur:,} → {tgt:,}만원 · 월 {mo}만원 · 연 {r}%  →  {n}개월 · {y}년 {m}월  ({cur/tgt*100:.0f}%)')

print('\n=== 목표일을 맞추려면 필요한 월 배분')
TARGETS = [('비상금 6개월', 1500, 1020, 6, 0.0, '2027년 3월'),
           ('투자 계좌 5,000만원', 5000, 2100, 36, 5.0, '2029년 9월')]
tot = 0
for name, tgt, cur, n, r, when in TARGETS:
    need = required(tgt, cur, n, r); tot += need
    print(f'  {name:18} {when}까지({n}개월) 필요 월 {need:.0f}만원')
print(f'  합계 필요 {tot:.0f}만원 · 현재 배분 63만원 → 월 {tot-63:.0f}만원 부족')

print('\n=== 순자산 2억 (미래 경로 기준)')
# 자산 구성별 기대수익 가중 → 자산 성장 + 월 저축 63만 + 부채 감소
assets = [('전세 보증금',9500,0.0),('ETF 계좌',4890,6.5),('퇴직연금 DC',1860,4.0),
          ('생활비 통장',1460,2.5),('청약저축',500,1.8)]
A = sum(a for _,a,_ in assets); wr = sum(a*r for _,a,r in assets)/A
print(f'  총자산 {A:,}만원 · 가중 기대수익 연 {wr:.2f}%')
import importlib.util, sys
spec = importlib.util.spec_from_file_location('am', '/tmp/claude-0/-home-user-ajs-bit-github-com/8f2afc13-0278-5882-ad06-7ee97dbbe248/scratchpad/amort.py')
