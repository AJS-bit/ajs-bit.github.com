import sys; sys.path.insert(0, '/tmp/claude-0/-home-user-ajs-bit-github-com/8f2afc13-0278-5882-ad06-7ee97dbbe248/scratchpad')
from amort import Debt
DEBTS=[Debt('주택담보대출',6200,3.4,32),Debt('신용대출',2200,6.8,20),Debt('학자금대출',280,2.5,5),Debt('카드 할부',180,14.5,20,fixed_term=9)]
def nw(months, save, wr=2.40, extra=15):
    ds=[Debt(d.name,d.bal,d.apr,d.minimum,d.fixed_term) for d in DEBTS]; a=18210; ia=wr/100/12
    for _ in range(months):
        a=a*(1+ia)+save
        for d in ds:
            if d.bal>0 and not d.fixed_term: d.bal+=d.bal*d.i
        pool=extra
        for d in ds:
            if d.bal<=0: continue
            p=min(d.minimum,d.bal); d.bal-=p; pool+=d.minimum-p
        while pool>1e-9:
            live=sorted([d for d in ds if d.bal>1e-9],key=lambda d:-d.apr)
            if not live: break
            t=live[0]; p=min(pool,t.bal); t.bal-=p; pool-=p
    return a-sum(d.bal for d in ds)

SPEND=208
print('=== 소비 절감 가정 (코칭 슬라이더)')
for cut in (5,10,15,20):
    saved = SPEND*cut/100
    base, better = nw(120,63), nw(120,63+saved)
    em = 480/(35+saved)          # 비상금 남은 480만
    print(f'  −{cut:2}%  월 {saved:5.1f}만원 절감 → 10년 뒤 +{better-base:,.0f}만원 · 비상금 도착 {14-round(em):+d}개월 (14 → {round(em)}개월)')

print('\n=== 카드 할부 경고 문구 근거')
print(f'  카드 할부 180만 @14.5%  → 월 수수료 상당 {180*0.145/12:.1f}만원 (잔액 비중 2.0%)')
print(f'  신용대출 2,200만 @6.8%  → 월 이자 {2200*0.068/12:.1f}만원 (잔액 비중 24.8%)')
print(f'  금리 배수 {14.5/6.8:.1f}배')

print('\n=== 예산 (총수입 390만)')
save, repay = 63, 92
print(f'  소비 {SPEND} + 저축·투자 이체 {save} + 대출상환 {repay} = {SPEND+save+repay}만  →  남음 {390-SPEND-save-repay}만 ({(390-SPEND-save-repay)/390*100:.1f}%)')
print(f'  소비율 제외 합계 {save+repay}만원')
print(f'  월급 대비 소비 {SPEND/360*100:.1f}%  ·  총수입 대비 {SPEND/390*100:.1f}%')
