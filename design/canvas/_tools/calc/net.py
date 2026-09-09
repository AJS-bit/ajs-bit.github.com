# -*- coding: utf-8 -*-
"""순자산 경로: 자산 성장 + 월 저축 − 부채 잔액."""
import sys
sys.path.insert(0, '/tmp/claude-0/-home-user-ajs-bit-github-com/8f2afc13-0278-5882-ad06-7ee97dbbe248/scratchpad')
from amort import Debt

DEBTS = [Debt('주택담보대출', 6200, 3.4, 32), Debt('신용대출', 2200, 6.8, 20),
         Debt('학자금대출', 280, 2.5, 5), Debt('카드 할부', 180, 14.5, 20, fixed_term=9)]
ASSETS0, WR, SAVE, EXTRA = 18210, 2.40, 63, 15

def ym(k, start=(2026, 9)):
    t = start[0]*12 + (start[1]-1) + k
    return t//12, t%12+1

def path(months):
    ds = [Debt(d.name, d.bal, d.apr, d.minimum, d.fixed_term) for d in DEBTS]
    a, ia = ASSETS0, WR/100/12
    out = []
    for m in range(1, months+1):
        a = a*(1+ia) + SAVE
        for d in ds:
            if d.bal > 0 and not d.fixed_term: d.bal += d.bal*d.i
        pool = EXTRA
        for d in ds:
            if d.bal <= 0: continue
            p = min(d.minimum, d.bal); d.bal -= p; pool += d.minimum - p
        while pool > 1e-9:
            live = sorted([d for d in ds if d.bal > 1e-9], key=lambda d: -d.apr)
            if not live: break
            t = live[0]; p = min(pool, t.bal); t.bal -= p; pool -= p
        out.append((m, a, sum(d.bal for d in ds), a - sum(d.bal for d in ds)))
    return out

p = path(300)
print(f'시작  자산 {ASSETS0:,}만 · 부채 {sum(d.bal for d in DEBTS):,.0f}만 · 순자산 {ASSETS0-sum(d.bal for d in DEBTS):,.0f}만\n')
print('=== 순자산 이정표')
for tgt in (10000, 15000, 20000):
    hit = next((r for r in p if r[3] >= tgt), None)
    if hit:
        y, mo = ym(hit[0])
        print(f'  {tgt/10000:.1f}억원  {y}년 {mo:2}월  ({hit[0]}개월 = {hit[0]//12}년 {hit[0]%12}개월)  자산 {hit[1]:,.0f} − 부채 {hit[2]:,.0f}')
print('\n=== 연도별')
for m in (12, 60, 120, 180):
    r = p[m-1]; y, mo = ym(m)
    print(f'  {m//12:2}년 뒤 ({y}.{mo:02}) 자산 {r[1]:9,.0f} · 부채 {r[2]:8,.0f} · 순자산 {r[3]:9,.0f}만원')

print('\n=== 투자 환경별 10년 뒤 순자산 (저축 63만원 계속 반영)')
def at(months, wr):
    ds = [Debt(d.name, d.bal, d.apr, d.minimum, d.fixed_term) for d in DEBTS]
    a, ia = ASSETS0, wr/100/12
    for m in range(months):
        a = a*(1+ia) + SAVE
        for d in ds:
            if d.bal > 0 and not d.fixed_term: d.bal += d.bal*d.i
        pool = EXTRA
        for d in ds:
            if d.bal <= 0: continue
            p = min(d.minimum, d.bal); d.bal -= p; pool += d.minimum - p
        while pool > 1e-9:
            live = sorted([d for d in ds if d.bal > 1e-9], key=lambda d: -d.apr)
            if not live: break
            t = live[0]; p = min(pool, t.bal); t.bal -= p; pool -= p
    return a - sum(d.bal for d in ds)
for lab, wr in (('보수', 1.0), ('기준', 2.4), ('낙관', 5.0)):
    v = at(120, wr)
    print(f'  {lab} {wr}%  →  {v:,.0f}만원 = {v/10000:.2f}억  (현재 대비 +{v-9350:,.0f}만원)')

print('\n=== 다음 자산 지점 (기준 2.4%)')
p2 = path(300)
for tgt in (10000, 15000, 20000, 25000):
    hit = next((r for r in p2 if r[3] >= tgt), None)
    if hit:
        y, mo = ym(hit[0]); n = hit[0]
        print(f'  {tgt:,}만원  {n//12}년 {n%12}개월 뒤  {y}년 {mo}월')

print('\n=== 소비를 월 15만원 줄이면 (저축 63 → 78만원)')
SAVE = 78
v = at(120, 2.4)
print(f'  10년 뒤 순자산 {v:,.0f}만원  (+{v-at.__globals__["ASSETS0"]*0:.0f}) → 기준 대비 +{v-28174:,.0f}만원')
