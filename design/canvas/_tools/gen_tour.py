# -*- coding: utf-8 -*-
"""첫 실행 안내(투어) 15장 — 탭에 처음 들어갈 때 한 번씩 뜨는 안내. 2026-09-22 사용자 요청 · 시안 승인 뒤 반영.

기존 탭 장(HomeCalendarStrip · Assets · Spending · Goals · Future)을 그대로 읽어 그 위에 어두운 막 + 강조 테두리 + 안내 카드를 얹는다.
강조할 요소의 좌표는 Brave 헤드리스에서 실제 웹폰트로 잰 값(아래 표). 탭 장을 고쳐 카드 위치가 바뀌면 다시 재서 표를 고친다.
규칙(plan/v5-calendar.md §10 11판 · CHANGES-2026-09-22.md):
  · 처음 설치해 첫 실행할 때만. 탭에 처음 들어가면 그 탭의 안내가 1단계부터. 홈 · 자산 · 소비 · 목적지 · 미래 각 3단계,
    탭 안의 세그먼트 화면(부채 · 상환 전략 · 내역 · 한도 · 새 목적지 설계 · 상환 계획)도 처음 들어갈 때 각 3단계 — 모두 11화면 × 3 = 33장.
  · 「건너뛰기」 = 그 탭의 남은 단계를 건너뜀. 다시 보려면 설정 › 도움말 › 「처음 안내 다시 보기」.
  · 저장 settings.onboarding.tourSeen = {home, assets, spending, goals, future} (보호 파일 · 백업 형식 불변).
  · 어두운 막 rgba(16,24,40,.62) · 강조 테두리 브랜드 파랑 4px + 흰 2px(요소의 모서리 그대로) · 카드는 요소 아래 12px, 아래에 자리가 없으면 위.
이 파일은 gen_v5.py 뒤(HomeCalendarStrip 이 다시 써진 뒤)에 돌린다. 다크 짝은 darken 으로 같이 쓴다."""
import pathlib
from gen_common import C, icon
from darken import darken

OUT = pathlib.Path(__file__).resolve().parent.parent
DIM = 'rgba(16,24,40,.62)'
ROOT_OPEN = ('<div style="width: 390px; height: 844px; background: #EDF0F7; color: #101828; display: flex; flex-direction: column; '
             'overflow: hidden; font-variant-numeric: tabular-nums;">')


def coach(target, title, body, step, last, above=False, radius=20):
    """target = (x, y, w, h) 강조할 요소. 카드는 그 아래(기본) 또는 위(above)에 12px 띄운다. 카드 높이를 몰라도 되게 위는 bottom 으로 앉힌다."""
    x, y, w_, h = target
    ring = (f'<div style="position: absolute; left: {x}px; top: {y}px; width: {w_}px; height: {h}px; border-radius: {radius}px; '
            f'box-shadow: 0 0 0 2px rgba(255,255,255,.95), 0 0 0 4px {C["BRAND"]}, 0 0 0 9999px {DIM};"></div>')
    counter = f'<span style="font-size: 11.5px; font-weight: 600; color: {C["INK3"]}; white-space: nowrap;">{step}</span>'
    primary = (f'<span style="display: inline-flex; align-items: center; justify-content: center; height: 40px; padding: 0 20px; border-radius: 12px; '
               f'background: {C["BRAND"]}; color: #FFFFFF; font-size: 14px; font-weight: 600; white-space: nowrap; flex-shrink: 0;">{"알겠어요" if last else "다음"}</span>')
    pos = f'bottom: {844 - y + 12}px;' if above else f'top: {y + h + 12}px;'
    caret_pos = 'bottom: -7px;' if above else 'top: -7px;'
    caret_border = (f'border-right: 1px solid {C["LINE"]}; border-bottom: 1px solid {C["LINE"]};' if above
                    else f'border-left: 1px solid {C["LINE"]}; border-top: 1px solid {C["LINE"]};')
    card_html = (
        f'<div style="position: absolute; left: 14px; width: 362px; {pos} background: {C["SURF"]}; border: 1px solid {C["LINE"]}; border-radius: 18px; '
        f'padding: 16px; display: flex; flex-direction: column; gap: 8px; box-shadow: 0 12px 32px -12px rgba(16,24,40,.45);">'
        f'<div style="position: absolute; {caret_pos} left: 30px; width: 13px; height: 13px; background: {C["SURF"]}; transform: rotate(45deg); {caret_border}"></div>'
        f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px;">'
        f'<span style="display: inline-flex; align-items: center; gap: 5px; height: 22px; padding: 0 9px; border-radius: 99px; background: {C["BRAND_SOFT"]}; '
        f'color: {C["BRAND"]}; font-size: 11.5px; font-weight: 700; letter-spacing: 0.02em;">{icon("help", 12, C["BRAND"], 2.2)}처음 안내</span>{counter}</div>'
        f'<span style="font-size: 16px; font-weight: 700; letter-spacing: -0.02em; line-height: 1.35; color: {C["INK"]};">{title}</span>'
        f'<span style="font-size: 13px; line-height: 1.55; color: {C["INK2"]}; word-break: keep-all;">{body}</span>'
        f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px; margin-top: 6px;">'
        f'<span style="font-size: 13px; font-weight: 600; color: {C["INK3"]}; padding: 8px 4px;">건너뛰기</span>{primary}</div></div>')
    return f'<div style="position: absolute; inset: 0; z-index: 5; overflow: hidden;">{ring}{card_html}</div>'


def with_coach(html, overlay):
    assert html.count(ROOT_OPEN) == 1, 'root'
    html = html.replace(ROOT_OPEN, ROOT_OPEN.replace('overflow: hidden;', 'overflow: hidden; position: relative;'), 1)
    k = html.rindex('</div>\n</x-dc>')
    return html[:k] + overlay + html[k:]


# 실측 좌표(x, y, w, h) — 2026-09-22 · 히어로 버튼을 뺀 뒤. 홈은 2026-09-24 다시 잼(달력 카드에 안내 한 줄 · 적기 알약 줄 40): 히어로 296 · 달력 222 · 다음 안내 116(627).
# 세그먼트는 모서리 14, 버튼 13, 카드 20(내역 묶음 · 한도 배분 18 · 한도 근거 14 · 머리 「거래」 10).
# 내역 2단계는 994px 목록 카드를 탭 바 위까지(490)만 강조한다.
TOUR = {
    'Home': ('HomeCalendarStrip', '홈', [
        ((14, 90, 362, 296), '여기가 현재 위치예요', '이번 달 월급에서 지금까지 쓴 비율이에요. 막대가 내 목표 선을 넘지 않게 써 보세요. 월말 예상은 아래 칸에 있어요.', False, 20),
        # 달력이 222 로 길어져 카드를 아래에 두면 탭 바(778~)를 덮는다(629 + 186 = 815) — 규칙대로 위(히어로 쪽)로 올린다(2026-09-24)
        ((14, 395, 362, 222), '날짜를 누르면 바로 기록', '날짜를 누르거나 아래 + 버튼을 누르고 숫자만 넣으면 끝이에요. 분류는 나중에 소비 탭에서 해도 돼요.', True, 20),
        ((14, 627, 362, 116), '지금 할 일 한 가지', '기록이 쌓이면 가장 효과가 큰 일 하나를 골라 알려 줘요. 누르면 그 화면으로 바로 가요.', True, 20)]),
    'Assets': ('Assets', '자산', [
        ((16, 60, 358, 42), '가진 것과 갚을 것', '자산 구성 · 부채 · 상환 전략 세 탭이에요. 부채가 있으면 상환 전략에서 갚는 순서를 정해요.', False, 14),
        ((14, 114, 362, 275), '순자산 = 자산 − 부채', '여섯 달 흐름을 그래프로 봐요. 자산이나 부채를 고치면 바로 다시 계산돼요.', False, 20),
        ((14, 399, 362, 69), '생활비 몇 달치가 있나요', '현금과 바로 뺄 수 있는 돈으로 생활비를 몇 달 버틸 수 있는지예요. 비상금 목적지와 이어져요.', False, 20)]),
    'Spending': ('Spending', '소비', [
        ((16, 58, 358, 42), '이번 달 · 내역 · 한도', '이번 달은 쓰는 속도, 내역은 기록 정리, 한도는 카테고리별 상한이에요. 달력에서 저장한 기록은 내역에서 분류해요.', False, 14),
        ((14, 112, 362, 342), '계획한 속도로 쓰고 있나요', '실선은 지금까지 쓴 돈, 점선은 월말 예상이에요. 회색 계획선보다 위에 있으면 빠르게 쓰는 중이에요.', False, 20),
        ((14, 464, 362, 289), '카테고리마다 얼마 썼는지', '한도 대비 비율이 100%를 넘으면 빨갛게 표시돼요. 전체 보기에서 한도를 조정해요.', True, 20)]),
    'Goals': ('Goals', '목적지', [
        ((14, 114, 362, 178), '저축을 목적지에 나눠요', '월 저축 여력을 목적지마다 얼마씩 넣을지 정해요. 모자라면 여기서 먼저 알려 줘요.', False, 20),
        ((14, 302, 362, 380), '도착 예상일이 보여요', '지금 속도로 언제 도착하는지 계산해요. 적립을 누르면 그 목적지에 넣은 돈을 기록해요.', True, 20),
        ((14, 692, 362, 46), '목적지를 정해 보세요', '비상금 · 여행 · 전세금처럼 모을 목표예요. 새 목적지 설계 탭에서 한 걸음씩 만들 수도 있어요.', True, 13)]),
    'Future': ('Future', '미래', [
        ((14, 114, 362, 386), '앞으로의 자산 경로', '기간과 투자 환경을 고르면 지금 속도로 자산이 어떻게 자라는지 그려요. 실제 기록은 바뀌지 않아요.', False, 20),
        ((14, 510, 362, 151), '다음 지점까지 얼마나', '1억원처럼 다음 고비까지 몇 달 남았는지 보여 줘요. 저축을 늘리면 앞당겨져요.', True, 20),
        ((14, 671, 362, 103), '보라 점선은 저장되지 않는 가정', '월 소비를 줄이면 10년 뒤 얼마가 달라지는지 시험해 보는 자리예요. 저장 기록과는 따로예요.', True, 20)]),
    # ── 탭 안의 세그먼트 화면 — 그 화면에 처음 들어갈 때 따로(2026-09-22 사용자: "그 항목으로 이동하면 그 밑의 요소도 설명이 들어가야")
    'Debts': ('Debts', '부채', [
        ((14, 114, 362, 160), '갚을 것 전체', '총부채와 가중 평균 금리, 월 최소 상환액이에요. 담보 비중이 크면 급하지 않은 빚이 많다는 뜻이에요.', False, 20),
        ((14, 284, 362, 116), '금리 높은 것부터', '잔액은 작아도 금리가 높으면 이자가 빨리 불어요. 먼저 갚을 것을 여기서 알려 줘요.', False, 20),
        ((14, 410, 362, 274), '부채 한 건씩', '건마다 종류 · 금리 · 월 최소 상환액이에요. 추가로 새 부채를 넣고, 누르면 고칠 수 있어요.', True, 20)]),
    'Strategy': ('Strategy', '상환 전략', [
        ((14, 114, 362, 292), '갚는 순서를 고르세요', '고금리 우선은 이자를 가장 적게, 소액 우선은 건수를 빨리 줄여요. 고르면 바로 저장돼요.', False, 20),
        ((14, 416, 362, 101), '언제 다 갚나', '지금 방식대로면 완제 시점과 총이자예요. 다른 방식과 얼마나 차이 나는지도 함께 보여요.', False, 20),
        ((14, 527, 362, 241), '이 순서로 갚아요', '먼저 끝나는 빚부터 완제 시점을 순서대로 보여 줘요. 다 갚은 돈은 다음 빚으로 넘어가요.', True, 20)]),
    'Ledger': ('LedgerV5', '내역', [
        ((14, 112, 362, 152), '기록을 찾고 거르기', '메모나 카테고리로 찾고, 칩으로 걸러요. 분류 안 함 칩을 누르면 분류하기 시트가 열려요.', False, 20),
        ((14, 274, 362, 490), '날짜별로 묶여요', '날마다 소비 합계와 이체가 머리글에 있어요. 달력에서 저장한 기록도 여기 같이 쌓이고, 누르면 고칠 수 있어요.', True, 18),
        ((312, 14, 62, 34), '자세히 넣을 땐 거래', '달력은 숫자만, 여기서는 종류 · 카테고리 · 계좌까지 넣어요. 저축 · 상환 이체도 여기서 기록해요.', False, 10)]),
    'Limits': ('Limits', '한도', [
        ((14, 112, 362, 215), '이번 달 쓸 수 있는 돈', '월급에서 저축 · 상환을 뺀 총한도예요. 자동 계산이지만 직접 정할 수도 있어요.', False, 20),
        ((14, 337, 362, 374), '카테고리마다 얼마씩', '총한도를 카테고리에 나눠요. 편집을 누르면 하나씩 고치고, 넘긴 곳은 빨갛게 보여요.', True, 18),
        ((14, 721, 362, 50), '계산 근거는 여기', '무엇을 빼고 어떻게 나눴는지 식을 보여 줘요. 숫자가 이해되지 않으면 여기부터 열어 보세요.', True, 14)]),
    'GoalDesign': ('GoalDesign', '새 목적지 설계', [
        ((16, 60, 358, 42), '내 목적지 ↔ 새 목적지 설계', '여기서 만든 목적지는 내 목적지 탭에 쌓여요. 우선순위를 바꾸면 월 저축 배분이 따라와요.', False, 14),
        ((14, 114, 362, 147), '추천에서 시작해도 돼요', '비상금 6개월 · 전세 보증금처럼 흔한 목적지는 값이 채워져요. 골라서 고치기만 하면 돼요.', False, 20),
        ((14, 271, 362, 509), '이름 · 목표액 · 기간', '*는 꼭 넣어야 해요. 시작 적립액과 연 수익률은 비워도 되고, 넣으면 도착 예상이 정확해져요.', True, 20)]),
    'Payoff': ('Payoff', '상환 계획', [
        ((14, 114, 362, 242), '추가 상환을 시험해 보세요', '월 추가 상환액을 움직이면 완제 시점과 총이자가 바뀌어요. 보라 점선은 저장되지 않는 가정이에요.', False, 20),
        ((14, 366, 362, 259), '얼마나 빨라지나', '고금리 우선 · 소액 우선 방식별로 완제 예상과 총이자를 비교해요. 지금 방식과의 차이도 함께요.', True, 20),
        ((14, 635, 362, 126), '마음에 들면 저장', '저장해야 자산 경로와 목적지 계산에 반영돼요. 저장 전까지는 어디에도 영향이 없어요.', True, 20)]),
}
NAMES = [f'Tour{k}{i}' for k, (_, _, steps) in TOUR.items() for i in range(1, len(steps) + 1)]

if __name__ == '__main__':
    for key, (base, label, steps) in TOUR.items():
        html = (OUT / f'{base}.dc.html').read_text(encoding='utf-8')
        n = len(steps)
        for i, (target, title, body, above, radius) in enumerate(steps, 1):
            name = f'Tour{key}{i}'
            light = with_coach(html, coach(target, title, body, f'{label} {i} / {n}', last=(i == n), above=above, radius=radius))
            (OUT / f'{name}.dc.html').write_text(light, encoding='utf-8')
            (OUT / f'Dark{name}.dc.html').write_text(darken(light, name), encoding='utf-8')
            print('wrote', name, '+ Dark' + name)
