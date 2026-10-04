# -*- coding: utf-8 -*-
"""첫 실행 안내(투어) — 화면에 처음 들어갈 때 저절로 뜨는 3단계 안내. 2026-09-22 사용자 요청 · 2026-09-26 앱(v5-stage1 a724aac)에 맞춤.

기존 탭 장(HomeDefaultScroll(앱 기본 카드 4개의 홈) · Assets · Debts · Strategy · Spending · LedgerV5 · Limits · Goals · GoalDesign · Future · Payoff)을 읽어
그 위에 어두운 막 + 강조 테두리 + 안내 카드를 얹는다. 문구 · 단계 · 버튼 · 배치 규칙은 앱 그대로다(lib/navi-tour.ts TOUR_STEPS ·
lib/navi-tour-policy.ts · components/navi/first-run-tour.tsx · app/first-run-tour.css).

규칙(design/CHANGES-2026-09-25.md):
  · 11화면(홈 · 자산 · 부채 · 상환 계획(자산) · 소비 · 내역 · 한도 · 목적지 · 새 목적지 설계 · 미래 · 상환 계획(미래))마다 처음 들어갈 때 저절로 뜬다.
    빈 화면이면 띄우지 않고 본 것으로도 기록하지 않는다(내용이 생긴 뒤 처음 들어갈 때 뜬다 · isEmptyScreen).
  · 카드 = 알약 「처음 안내」(제목 옆 ?로 다시 연 안내는 「화면 안내」) + 「{화면} n / N」 · 제목 16 / 700 · 본문 13 / 1.55 ·
    홈 3/3 만 각주 한 줄(12.5 · ink-3) · 버튼 줄 = 왼쪽 「건너뛰기」 · 「안내 모두 끄기」(13 / 600 · ink-3) + 오른쪽 「다음」/「알겠어요」(40 · 브랜드).
  · 막은 아래 탭 막대 위(y 778)까지 — 탭 막대는 밝게 남고 누를 수 있다. 강조도 탭 막대 위에서 잘린다.
  · 배치(placeTourCard): 카드 폭 min(420, 화면 − 28) = 362 · 대상 아래 12 → 안 되면 위 12 → 둘 다 안 되면 compact(탭 막대 위 14에 붙여
    대상 위로 겹침 · 꼬리 없음). 대상이 화면 밖(위 8 · 아래 탭 막대 − 8을 넘음)이거나 compact 이면 대상을 위로 스크롤(scrollIntoView start ·
    scroll-padding-top 20 · 문서 끝에서 막힘 — 끝 = 마지막 내용 아래가 y 716 · 탭 막대 위 62px 빈 자리 · 홈은 y 740 · 38px)한다. 그래도 compact 이고 대상 + 카드가 한 화면에 들면
    대상 아래를 화면 아래(scroll-padding-bottom 82)에 맞춘다. 홈 1(히어로)이 compact 면 큰 숫자가 위 여백 14에 닿을 때까지만 더 내린다(TOUR_KEEP).
    스크롤은 다음 단계로 이어진다. 꼬리 x = clamp(대상 왼쪽 + 30, 카드 왼쪽 + 24, 카드 오른쪽 − 24).
  · 다크: 카드 · 꼬리 #1E2739 · 선 #39455F · 막 rgba(4,7,14,.74) — darken 뒤에 이 파일이 덮어쓴다.
  · 저장 settings.onboarding.tourSeen 11키(보호 파일 · 백업 형식 불변).

좌표 표(PLACE)는 실제 웹폰트(IBM Plex Sans KR)를 띄운 Brave 헤드리스에서 바탕 장을 자연 높이로 펼쳐 대상 자리 · 카드 높이를 재고,
앱의 placeTourCard · 스크롤 순서를 그대로 흉내 내서 얻은 값이다(2026-09-26). 바탕 장을 고쳐 카드 자리가 바뀌면 다시 잰다.
2026-09-30: 홈의 달력이 펼친 월 달력이 기본이 되어(홈 문서 +314) 홈 · 시작 순서 · 샘플 홈의 표를 다시 쟀다 — 같은 흉내가 예전 장 9줄을
그대로 다시 만들어 내는 것을 먼저 확인했다. y 는 장에 그리는 정수 스크롤에서의 자리(대상 위 − 스크롤).
이 파일은 gen_v5 · gen_v5_sheets · gen_v5_screens · refresh_components_v5 뒤(탭 장이 다시 써진 뒤)에 돌린다. 처음 시작한 빈 홈(TourHomeChecklist)의 바탕은 HomeConfigured, 새 목적지 설계는 GoalDesignStates A 의 빈 폼으로 바꾼 GoalDesign, 내역은 ⋯ 메뉴를 닫은 LedgerV5. 다크 짝도 이 파일이 쓴다."""
import pathlib
import re
from gen_common import C, icon
from darken import darken

OUT = pathlib.Path(__file__).resolve().parent.parent
PHONE_H = 844
NAV_TOP = 778            # 아래 탭 막대 위쪽(66px) — 막 · 강조 · 카드 자리는 여기까지
CARD_W = 362             # min(420, 390 − 28)
CARD_LEFT = 14
GAP = 12

# 앱 lib/navi-tour.ts 그대로
BADGE_AUTO, BADGE_HELP = '처음 안내', '화면 안내'
SKIP, ALL_OFF, NEXT, DONE = '건너뛰기', '안내 모두 끄기', '다음', '알겠어요'
HOME_FOOTNOTE = f'다른 화면도 처음 들어갈 때 짧은 안내가 떠요. 필요 없으면 「{ALL_OFF}」를 누르세요.'

# 라이트 · 다크 값(카드 바탕 · 선 · 그림자 · 막). 다크는 darken 뒤에 채운다(first-run-21 · app/first-run-tour.css)
LIGHT = {'__TCBG__': C['SURF'], '__TCLN__': C['LINE'], '__TCSH__': '0 12px 32px -12px rgba(16,24,40,.45)', '__TDIM__': 'rgba(16,24,40,.62)'}
DARK = {'__TCBG__': '#1E2739', '__TCLN__': '#39455F', '__TCSH__': '0 12px 32px -12px rgba(0,0,0,.6)', '__TDIM__': 'rgba(4,7,14,.74)'}


def fill(html, vals):
    for k, v in vals.items():
        html = html.replace(k, v)
    assert '__T' not in html, 'placeholder left'
    return html


def card_inner(title, body, counter, last, badge=BADGE_AUTO, footnote=None):
    """카드 안쪽 — 배지 · 단계 · 제목 · 본문 · (각주) · 버튼 줄(TourCardContent)."""
    btn2 = ('display: inline-flex; align-items: center; min-height: 40px; padding: 8px 4px; font-size: 13px; font-weight: 600; '
            f'line-height: 1.4; color: {C["INK3"]}; white-space: nowrap;')
    foot = (f'<div style="margin-top: 6px; font-size: 12.5px; line-height: 1.5; color: {C["INK3"]}; word-break: keep-all; overflow-wrap: anywhere;">{footnote}</div>'
            if footnote else '')
    return (
        f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px; flex-wrap: wrap; '
        f'font-size: 11.5px; font-weight: 600; color: {C["INK3"]};">'
        f'<span style="display: inline-flex; align-items: center; gap: 5px; min-height: 22px; padding: 2px 9px; border-radius: 99px; '
        f'background: {C["BRAND_SOFT"]}; color: {C["BRAND"]}; font-weight: 700; letter-spacing: 0.02em; white-space: nowrap;">'
        f'{icon("help", 12, C["BRAND"], 2)}{badge}</span>'
        f'<span style="white-space: nowrap;">{counter}</span></div>'
        f'<div style="margin-top: 8px; font-size: 16px; font-weight: 700; letter-spacing: -0.02em; line-height: 1.35; color: {C["INK"]}; '
        f'word-break: keep-all; overflow-wrap: anywhere;">{title}</div>'
        f'<div style="margin-top: 8px; font-size: 13px; line-height: 1.55; color: {C["INK2"]}; word-break: keep-all; overflow-wrap: anywhere;">{body}</div>'
        f'{foot}'
        f'<div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 4px 8px; margin-top: 14px;">'
        f'<div style="display: flex; align-items: center; flex-wrap: wrap; gap: 0 12px; min-width: 0;">'
        f'<span style="{btn2}">{SKIP}</span><span style="{btn2}">{ALL_OFF}</span></div>'
        f'<span style="margin-left: auto; display: inline-flex; align-items: center; justify-content: center; min-height: 40px; padding: 8px 20px; '
        f'border-radius: 12px; background: {C["BRAND"]}; color: #FFFFFF; font-size: 14px; font-weight: 600; line-height: 1.4; white-space: nowrap; flex-shrink: 0;">'
        f'{DONE if last else NEXT}</span></div>')


def card_box(inner, pos):
    """카드 겉 — pos 는 위치 CSS(재기용은 'position: relative;')."""
    return (f'<div style="{pos} width: {CARD_W}px; background: __TCBG__; border: 1px solid __TCLN__; border-radius: 18px; padding: 16px; '
            f'box-shadow: __TCSH__; font-size: 13px; line-height: 1.55; color: {C["INK"]};">{inner}</div>')


def overlay(place, inner):
    """place = (스크롤, x, y, w, h, 모서리, 배치) — 스크롤 뒤 화면 좌표. 막 · 강조 · 꼬리 · 카드 — 탭 막대 위(778)까지만."""
    _, x, y, w_, h, radius, side = place
    ring = (f'<div style="position: absolute; left: {x}px; top: {y}px; width: {w_}px; height: {h}px; border-radius: {radius}px; '
            f'box-shadow: 0 0 0 2px rgba(255,255,255,.95), 0 0 0 4px {C["BRAND"]}, 0 0 0 9999px __TDIM__;"></div>')
    arrow = ''
    if side == 'below':
        pos = f'position: absolute; left: {CARD_LEFT}px; top: {y + h + GAP}px;'
        ay, rot = y + h + GAP - 6, 45
    elif side == 'above':
        pos = f'position: absolute; left: {CARD_LEFT}px; bottom: {NAV_TOP - (y - GAP)}px;'   # 막 상자(높이 778) 아래 기준
        ay, rot = y - GAP - 7, 225
    else:   # compact — 탭 막대 위 14에 붙이고 꼬리 없음
        assert side == 'compact', side
        pos = f'position: absolute; left: {CARD_LEFT}px; bottom: 14px;'
        ay = rot = None
    if ay is not None:
        ax = min(max(x + 30, CARD_LEFT + 24), CARD_LEFT + CARD_W - 24)
        arrow = (f'<div style="position: absolute; left: {ax}px; top: {ay}px; width: 13px; height: 13px; background: __TCBG__; '
                 f'border-left: 1px solid __TCLN__; border-top: 1px solid __TCLN__; transform: rotate({rot}deg);"></div>')
    return (f'<div style="position: absolute; left: 0; top: 0; width: 390px; height: {NAV_TOP}px; z-index: 5; overflow: hidden;">'
            f'{ring}{arrow}{card_box(inner, pos)}</div>')


# ── 바탕 장 ─────────────────────────────────────────────────────────────────────────────
ROOT = re.compile(r'<div style="width: 390px; height: (\d+)px; background: #EDF0F7;[^"]*">')


def div_span(html, start):
    """start 에서 여는 <div 의 짝 </div> 끝까지. 생성기가 쓴 잘 짜인 마크업을 전제한다."""
    assert html.startswith('<div', start), html[start:start + 40]
    depth, i = 0, start
    tag = re.compile(r'<div\b|</div>')
    for m in tag.finditer(html, start):
        depth += 1 if m.group(0) == '<div' else -1
        if depth == 0:
            return start, m.end()
    raise AssertionError('unbalanced div')


def strip_ledger_menu(html):
    """내역 장은 9월 8일 「점심」의 ⋯ 메뉴를 연 첫 화면이다 — 안내 장에는 열린 메뉴가 없어야 한다(맵 TourLedger1)."""
    key = '<div style="position: absolute; right: 0; top: calc(100% + 4px); z-index: 2; width: 156px;'      # gen_screens.row_menu(2026-09-27 fix-up 3 — 행 아래 4px · 156)
    assert html.count(key) == 1, 'ledger menu'
    a, b = div_span(html, html.index(key))
    s = html.rindex('<span style="flex-shrink: 0; display: inline-flex;">', 0, a)
    more = html[s:a].replace(C['INK2'], C['INK4'])          # 메뉴를 닫으면 ⋯ 아이콘도 다른 줄처럼 옅게
    return html[:s] + more + html[b:]


def empty_goal_design(html):
    """새 목적지 설계는 처음 들어갈 때(안내가 뜨는 때) 빈 칸 — GoalDesignStates A 의 빈 폼 카드로 바꾼다(맵 TourGoalDesign1)."""
    states = (OUT / 'GoalDesignStates.dc.html').read_text(encoding='utf-8')
    k_empty = states.index('예: 결혼 자금')
    k_full = html.index('결혼 자금')
    hero_open = re.compile(r'<div style="background: #FFFFFF; border: 1px solid #E3E8F1; border-radius: 20px; padding: 15px;')
    s_empty = [m.start() for m in hero_open.finditer(states) if m.start() < k_empty][-1]
    s_full = [m.start() for m in hero_open.finditer(html) if m.start() < k_full][-1]
    a, b = div_span(states, s_empty)
    c, d = div_span(html, s_full)
    assert '목적지로 저장' in states[a:b] and '매달 넣어야 할 돈' in html[c:d]
    return html[:c] + states[a:b] + html[d:]


def base_html(board):
    html = (OUT / f'{board}.dc.html').read_text(encoding='utf-8')
    if board == 'LedgerV5':
        html = strip_ledger_menu(html)
    if board == 'GoalDesign':
        html = empty_goal_design(html)
    # 앱 body 와 같게 keep-all(D14) — 안내 카드 문구와 바탕이 같은 규칙으로 꺾이게
    html = html.replace('-webkit-font-smoothing: antialiased; }', '-webkit-font-smoothing: antialiased; word-break: keep-all; }', 1)
    return html


def phone(html, scroll):
    """폰 한 화면(844)으로 자르고 scroll 만큼 내린 모습 — 머리줄에 음의 위 여백을 주면 머리 · 본문이 함께 올라가고 탭 막대는 그대로다."""
    m = ROOT.search(html)
    assert m, 'root'
    html = html[:m.start()] + m.group(0).replace(f'height: {m.group(1)}px;', f'height: {PHONE_H}px;').replace('overflow: hidden;', 'overflow: hidden; position: relative;') + html[m.end():]
    if scroll:
        k = html.index('<div style="', m.start() + 10)
        html = html[:k + len('<div style="')] + f'margin-top: -{scroll}px; ' + html[k + len('<div style="'):]
    return html


def with_overlay(html, ov):
    k = html.rindex('</div>\n</x-dc>')
    return html[:k] + ov + html[k:]


# ── 안내 단계(앱 TOUR_STEPS 그대로) · 대상 = 바탕 장 루트에서 자식 번호 경로(0 머리줄 · 1 본문 · 2 탭 막대) ───────────────
TOUR = {
    # 홈 바탕 = 앱 기본 카드 4개(DEFAULT_HOME_CARDS)의 전체 홈 — 3단계에서 내린 모습에 대표 목적지가 아니라 한도 · 순자산 · 상환 계획 줄이 보이게(goals-14)
    'Home': ('HomeDefaultScroll', '홈', [
        ((1, 0), '이번 달 소비는 여기서 봐요', '이번 달 월급에서 지금까지 쓴 비율이에요. 막대가 소비 목표 선을 넘지 않게 써 보세요. 월말 예상은 아래 칸에 있어요.', None),
        ((1, 1), '날짜를 누르면 바로 기록', '날짜를 누르거나 아래 + 버튼을 누르고 숫자만 넣으면 끝이에요. 카테고리는 나중에 소비 탭에서 골라도 돼요.', None),
        ((1, 2), '지금 할 일 한 가지', '기록이 쌓이면 가장 효과가 큰 일 하나를 골라 알려 줘요. 누르면 그 화면으로 바로 가요.', HOME_FOOTNOTE)]),
    'Assets': ('Assets', '자산', [
        ((0, 1), '가진 것과 갚을 것', '자산 구성 · 부채 · 상환 계획 세 탭이에요. 부채가 있으면 상환 계획에서 언제 다 갚는지 봐요.', None),
        ((1, 0), '순자산 = 자산 − 부채', '여섯 달 흐름을 그래프로 봐요. 자산이나 부채를 고치면 바로 다시 계산돼요.', None),
        ((1, 1, 0), '생활비 몇 달치가 있나요', '현금과 바로 뺄 수 있는 돈으로 생활비를 몇 달 버틸 수 있는지예요. 비상금 목적지와 이어져요.', None)]),
    'Spending': ('Spending', '소비', [
        ((0, 2), '이번 달 · 내역 · 한도', '이번 달은 쓰는 속도, 내역은 기록 정리, 한도는 카테고리별 상한이에요. 카테고리 없이 저장한 기록은 내역에서 카테고리를 골라요.', None),
        ((1, 0), '계획한 속도로 쓰고 있나요', '실선은 지금까지 쓴 돈, 점선은 월말 예상이에요. 점선 끝이 한도 안이면 이번 달은 괜찮아요.', None),
        ((1, 1), '카테고리마다 얼마 썼는지', '한도의 몇 %를 썼는지예요. 100%를 넘으면 빨갛게 보이고, 누르면 그 카테고리 내역이 열려요.', None)]),
    'Goals': ('Goals', '목적지', [
        ((1, 0), '저축을 목적지에 나눠요', '월급에서 소비와 상환을 빼고 남는 돈을 앱이 우선순위와 목표일에 따라 목적지마다 나눠요. 모자라면 여기서 먼저 알려 줘요.', None),
        ((1, 1, 1), '도착 예상일이 보여요', '지금 속도로 언제 도착하는지 계산해요. 적립을 누르면 그 목적지에 넣은 돈을 기록해요.', None),
        ((1, 2), '목적지를 정해 보세요', '비상금 · 여행 · 전세금처럼 돈을 모으는 목적지예요. 새 목적지 설계 탭에서는 매달 필요한 돈을 먼저 계산해 볼 수 있어요.', None)]),
    'Future': ('Future', '미래', [
        ((1, 0), '앞으로의 자산 경로', '기간과 투자 환경을 고르면 지금 속도로 자산이 어떻게 자라는지 그려요. 실제 기록은 바뀌지 않아요.', None),
        ((1, 1), '다음 지점까지 얼마나', '1억원처럼 다음 지점까지 얼마나 남았는지 보여 줘요. 저축을 늘리면 앞당겨져요.', None),
        ((1, 2), '보라 점선은 저장되지 않는 가정', '밀어 보면 위의 큰 숫자와 그래프도 보라 점선으로 바뀌어요. 저장 기록과는 따로예요.', None)]),
    # ── 탭 안의 세그먼트 화면 — 그 화면에 처음 들어갈 때 따로(2026-09-22 사용자: "그 항목으로 이동하면 그 밑의 요소도 설명이 들어가야")
    'Debts': ('Debts', '부채', [
        ((1, 0), '갚을 것 전체', '총부채와 평균 금리, 월 최소 상환액이에요. 주택담보 · 전세대출 비중이 크면 금리가 낮고 오래 갚는 빚이 많다는 뜻이에요.', None),
        ((1, 1), '금리 높은 것부터', '잔액은 작아도 금리가 높으면 이자가 빨리 불어요. 먼저 갚을 것을 여기서 알려 줘요.', None),
        ((1, 2), '부채 한 건씩', '건마다 종류 · 금리 · 월 최소 상환액이에요. 새 부채도 추가하고, 누르면 고칠 수 있어요.', None)]),
    'Strategy': ('Strategy', '상환 계획', [
        ((1, 0), '저장된 상환 계획', '상환 방식과 월 추가 상환액이에요. 바꾸려면 아래 버튼으로 미래 › 상환 계획에 가서 시험하고 저장해요.', None),
        ((1, 1), '언제 다 갚나요', '저장된 계획대로면 다 갚는 달과 총이자예요.', None),
        ((1, 2), '이 순서로 갚아요', '먼저 끝나는 빚부터 다 갚는 달을 순서대로 보여 줘요. 다 갚은 빚에 내던 돈은 다음 빚으로 넘어가요.', None)]),
    'Ledger': ('LedgerV5', '내역', [
        ((1, 0), '기록을 찾고 거르기', '메모나 카테고리로 찾고, 칩으로 걸러요. 카테고리 없는 기록은 위의 카테고리 고르기 ›로 한꺼번에 정해요.', None),
        ((1, 1), '날짜별로 묶여요', '날마다 소비 합계와 이체가 머리글에 있어요. 달력에서 저장한 기록도 여기 같이 쌓이고, 누르면 고칠 수 있어요.', None),
        ((0, 1, 0, 1), '기록 추가', '+ 기록은 홈 달력과 같은 기록 창을 열어요. 저축 · 상환 이체와 계좌 연결은 그 창의 저축·투자로 기록 › · 대출상환으로 기록 ›에서 남겨요.', None)]),
    'Limits': ('Limits', '한도', [
        ((1, 0), '이번 달 쓸 수 있는 돈', '월급 × 소비 목표로 정한 이번 달 한도예요. 소비 목표를 바꾸면 바로 따라 바뀌고, 직접 정할 수도 있어요.', None),
        ((1, 2), '카테고리마다 얼마씩', '총한도를 카테고리에 나눠요. 배분 편집을 누르면 하나씩 고치고, 넘은 곳은 빨갛게 보여요.', None),
        ((1, 3), '계산 근거는 여기', '한도를 어떻게 정했는지 식으로 보여 줘요. 숫자가 이해되지 않으면 여기부터 열어 보세요.', None)]),
    'GoalDesign': ('GoalDesign', '새 목적지 설계', [
        ((0, 1), '내 목적지 ↔ 새 목적지 설계', '여기서 만든 목적지는 내 목적지 탭에 쌓여요. 우선순위를 바꾸면 목적지마다 매달 넣을 돈이 따라 바뀌어요.', None),
        ((1, 0), '추천에서 시작해도 돼요', '추천 카드를 누르면 이름 · 목표액 · 목표일이 채워져요. 골라서 고치기만 하면 돼요.', None),
        ((1, 1), '이름 · 목표액 · 기간', '*는 꼭 넣어야 해요. 지금 모은 돈과 수익률은 비워도 돼요. 넣으면 매달 넣어야 할 돈이 그만큼 정확해져요.', None)]),
    'Payoff': ('Payoff', '상환 계획', [
        ((1, 0), '추가 상환을 시험해 보세요', '월 추가 상환액을 움직이면 다 갚는 달과 총이자가 바뀌어요. 움직이는 동안은 보라 점선 — 저장되지 않는 가정이에요.', None),
        ((1, 1), '얼마나 빨라지나요', '고금리 우선 · 소액 우선 방식별로 다 갚는 달과 총이자를 비교해요. 지금 방식과의 차이도 함께요.', None),
        ((1, 2), '마음에 들면 저장', '저장해야 홈 · 자산 경로 · 목적지 계산에 반영돼요. 저장하지 않은 가정은 앱을 닫으면 사라져요.', None)]),
    # ── 변형 — 샘플로 둘러보기로 시작한 홈의 1단계(2026-09-27 fix-up 2 · D8 샘플 띠는 모든 탭에 · 안내 막 아래 흐리게 · 머리줄 · 히어로가 띠 높이만큼 아래).
    # 바탕 = HomeSampleMode(자식 0 = 샘플 띠 · 1 머리줄 · 2 본문 · 3 탭 막대). 1단계만 장으로 쓴다 — 2 · 3단계는 TourHome2 · 3 과 같은 카드가 띠만큼 아래.
    'HomeSample': ('HomeSampleMode', '홈', [
        ((2, 0), '이번 달 소비는 여기서 봐요', '이번 달 월급에서 지금까지 쓴 비율이에요. 막대가 소비 목표 선을 넘지 않게 써 보세요. 월말 예상은 아래 칸에 있어요.', None),
        ((2, 1), '날짜를 누르면 바로 기록', '날짜를 누르거나 아래 + 버튼을 누르고 숫자만 넣으면 끝이에요. 카테고리는 나중에 소비 탭에서 골라도 돼요.', None),
        ((2, 2), '지금 할 일 한 가지', '기록이 쌓이면 가장 효과가 큰 일 하나를 골라 알려 줘요. 누르면 그 화면으로 바로 가요.', HOME_FOOTNOTE)]),
    # ── 변형 — 처음 시작한 빈 홈의 3단계(시작 순서 카드 · TOUR_HOME_CHECKLIST_STEP · first-run-5). 3단계만 장으로 쓴다
    'HomeChecklist': ('HomeConfigured', '홈', [
        ((1, 0), '이번 달 소비는 여기서 봐요', '이번 달 월급에서 지금까지 쓴 비율이에요. 막대가 소비 목표 선을 넘지 않게 써 보세요. 월말 예상은 아래 칸에 있어요.', None),
        ((1, 1), '날짜를 누르면 바로 기록', '날짜를 누르거나 아래 + 버튼을 누르고 숫자만 넣으면 끝이에요. 카테고리는 나중에 소비 탭에서 골라도 돼요.', None),
        ((1, 2), '시작 순서', '월급 → 첫 소비 기록 순서로 채우면 홈이 계산을 시작해요. 자산 · 부채는 있으면 넣어요.', HOME_FOOTNOTE)]),
}
# 실측 · 배치 표 — (스크롤, x, y, w, h, 모서리, 배치). 모서리 = 대상 요소의 border-radius(강조 테두리가 따른다). y 는 스크롤한 뒤 화면 좌표. 2026-09-26 앱 placeTourCard 흉내(위 설명)
# 스크롤 끝 = 마지막 내용 아래가 y 716 에 오는 자리(앱 a724aac 실측: app-shell 아래 여백 104 + 탭 내용 끝 24 → 탭 막대 위 62px 빈 자리).
#   2026-09-27 fix-up 2: 이 규칙은 세그먼트가 있는 화면에만 맞다(안쪽 탭 내용이 .tab-content 보다 24 먼저 끝남). 홈은 문서 = 마지막 내용 아래 + 104 라
#   끝에서 마지막 내용 아래가 y 740(탭 막대 위 38px) — 홈 · 시작 순서 · 샘플 홈은 − 740 으로 잰다(tools/fix2/measure_tour.cjs).
#   2026-09-26 검토에서 고침 — 처음 표는 끝을 「자연 높이 + 16 − 844」(탭 막대 위 16px)로 잡아 끝에 닿는 단계(홈 3 · 소비 3 · 목적지 3 · 미래 3 · 한도 2 · 3 · 상환 계획 3 · 시작 순서)가 앱보다 46px(홈 32px) 아래였고, 미래 3 카드는 앱과 달리 위로 갔다.
PLACE = {
    'Home': [   # 자연 높이 1531 · 마지막 내용 아래 1451 · 스크롤 끝 711(2026-09-30 다시 잼 — 홈의 달력이 펼친 월 달력(556.8) · 홈 끝 = 마지막 내용 아래 − 740)
        (0, 14, 103, 362, 363, 20, 'below'),   # 카드 188 · 이번 달 소비 월말에도 목표 — 그대로(히어로가 달력 위)
        (455, 14, 20, 362, 557, 18, 'compact'),   # 카드 188 · 2026년 9월 접기 날짜를 누르면 — 화면 밖(아래 1032)이라 위 20 으로 스크롤 · 아래(776.8 > 764) · 위 모두 안 돼 compact(꼬리 없음 · 탭 막대 위 14) · 끝 맞춤은 557 + 188 + 40 > 778 이라 건너뜀
        (455, 14, 587, 362, 155, 18, 'above'),   # 카드 231 · 다음 안내 투자 계좌 5,00 — 스크롤 455 를 이어받아 화면 안(587 ~ 742) · 아래(985 > 764)는 안 되고 위(344 ≥ 14)
    ],
    'Assets': [   # 자연 높이 953 · 스크롤 끝 171
        (0, 16, 73, 358, 42, 12, 'below'),   # 카드 188 · 자산 구성 부채 상환 계획
        (0, 14, 127, 362, 277, 20, 'below'),   # 카드 188 · 순자산 전월 대비 2.5% 9
        (0, 14, 414, 177, 88, 14, 'below'),   # 카드 188 · 현금성 비상금 7.0개월 치 
    ],
    'Spending': [   # 자연 높이 933 · 스크롤 끝 151
        (0, 16, 117, 358, 42, 12, 'below'),   # 카드 208 · 이번 달 내역 한도
        (0, 14, 171, 362, 342, 20, 'below'),   # 카드 188 · 31.1 % 월급 대비 지금까
        (151, 14, 371, 362, 289, 18, 'above'),   # 카드 188 · 카테고리별 소비 112만원 /
    ],
    'Goals': [   # 자연 높이 968 · 스크롤 끝 186
        (0, 14, 127, 362, 300, 20, 'below'),   # 카드 208 · 매달 모으는 돈 매달 모으는 
        (0, 29, 477, 332, 98, 0, 'above'),   # 카드 188 · 68 % 비상금 6개월 1,0
        (186, 14, 670, 362, 46, 14, 'above'),   # 카드 188 · 목적지 추가
    ],
    'Future': [   # 자연 높이 1180 · 마지막 내용 아래 1114 · 스크롤 끝 398(2026-09-27 fix-up 다시 잼 — 바탕 Future 를 앱 실측으로: 경로 430 · 지점 165 · 접힘 70 + 86 · 어림 안내 위 33)
        (0, 14, 127, 362, 430, 20, 'below'),   # 카드 188 · 기간 5년 10년 20년 30
        (0, 14, 567, 362, 165, 18, 'above'),   # 카드 188 · 다음 자산 지점 1억원 4개월
        (398, 14, 344, 362, 127, 18, 'below'),   # 카드 188 · 저장되지 않는 가정 10년 뒤 — 앱(스크롤 396 · y 343)과 같이 아래 · 아래 어림 안내가 보임
    ],
    'Debts': [   # 자연 높이 885 · 스크롤 끝 103
        (0, 14, 127, 362, 181, 20, 'below'),   # 카드 188 · 총부채 평균 금리 연 4.4%
        (0, 14, 318, 362, 135, 18, 'below'),   # 카드 188 · 상환 안내 카드 할부 · 연 
        (0, 14, 462, 362, 274, 18, 'above'),   # 카드 188 · 부채 4건 8,860만원 추가
    ],
    'Strategy': [   # 자연 높이 744 · 스크롤 끝 0
        (0, 14, 127, 362, 175, 20, 'below'),   # 카드 188 · 저장된 상환 계획 저장된 계획
        (0, 14, 312, 362, 116, 18, 'below'),   # 카드 168 · 다 갚는 달 2036년 5월 
        (0, 14, 437, 362, 241, 18, 'above'),   # 카드 188 · 갚는 순서 고금리 우선 1 카
    ],
    'Ledger': [   # 자연 높이 2041 · 스크롤 끝 1259
        (0, 14, 171, 362, 204, 18, 'below'),   # 카드 188 · 메모·카테고리 검색 반복 기록
        (365, 14, 20, 362, 1534, 18, 'compact'),   # 카드 188 · 9월 8일 화요일 · 오늘 소
        (53, 312, 20, 62, 34, 10, 'below'),   # 카드 208 · 기록
    ],
    'Limits': [   # 자연 높이 1082 · 마지막 내용 아래 1016 · 스크롤 끝 300(2026-09-27 fix-up 다시 잼 — 기타 부줄이 이름 칸 안 두 줄)
        (0, 14, 171, 362, 240, 20, 'below'),   # 카드 188 · 이번 달 총한도 자동 216 
        (300, 14, 261, 362, 395, 18, 'above'),   # 카드 188 · 카테고리 배분 13개 · 직접
        (300, 14, 666, 362, 50, 14, 'above'),   # 카드 188 · 이 한도는 어떻게 계산했나요?
    ],
    'GoalDesign': [   # 자연 높이 780 · 스크롤 끝 0
        (0, 16, 73, 358, 42, 12, 'below'),   # 카드 188 · 내 목적지 새 목적지 설계
        (0, 14, 127, 362, 180, 18, 'below'),   # 카드 188 · 추천 목적지에서 시작 부채 다
        (0, 14, 317, 362, 334, 20, 'above'),   # 카드 188 · 이름 예: 결혼 자금 목표액 
    ],
    'Payoff': [   # 자연 높이 900 · 스크롤 끝 118
        (0, 14, 127, 362, 317, 18, 'below'),   # 카드 188 · 저장된 계획  월 추가 상환을
        (0, 14, 454, 362, 282, 18, 'above'),   # 카드 188 · 고금리 우선 추천 다 갚는 달
        (118, 14, 628, 362, 89, 18, 'above'),   # 카드 188 · 저장된 상환 계획이에요 슬라이
    ],
    'HomeChecklist': [   # 자연 높이 1468 · 마지막 내용 아래 1402 · 스크롤 끝 662(2026-09-30 다시 잼 — 펼친 빈 9월 518.8 · 홈 끝 규칙 − 740)
        (0, 14, 103, 362, 359, 20, 'below'),   # 카드 188 · 이번 달 소비 소비 목표 조정
        (452, 14, 20, 362, 519, 18, 'below'),   # 카드 188 · 2026년 9월 접기 날짜를 누르면 — 위 20 으로 스크롤 · 20 + 519 + 12 + 188 = 739 ≤ 764 라 아래(장으로는 안 씀 · 3단계 스크롤의 출발점)
        (662, 14, 339, 362, 238, 18, 'above'),   # 카드 231 · 다음 안내 시작 순서 1 월급 — 화면 밖(아래 787)이라 스크롤, 문서 끝 662 에서 막힘 · 대상 y 339 · 카드 위는 그대로
    ],
    'HomeSample': [   # 자연 높이 1513 · 마지막 내용 아래 1433 · 스크롤 끝 693(2026-09-30 다시 잼 — 펼친 샘플 9월 537.6 · 합계 줄 없이 샘플 문장 · 1단계만 장으로 씀)
        (0, 14, 135, 362, 370, 20, 'below'),   # 카드 188 · 이번 달 소비 소비 목표 조정 — 그대로
        (495, 14, 20, 362, 538, 18, 'below'),   # 카드 188 · 2026년 9월 접기 날짜를 누르면 — 위 20 으로 스크롤 · 20 + 538 + 12 + 188 = 758 ≤ 764 라 아래
        (495, 14, 567, 362, 116, 18, 'above'),   # 카드 231 · 다음 안내 카드 할부 금리 1 — 스크롤 495 를 이어받아 화면 안 · 아래(927 > 764)는 안 되고 위
    ],
}

# ── 참고 장 — 규칙 한 장(TourRules · AMEND 2 · first-run-3 · first-run-4 · first-run-21 · D7 · D8 · D14) ───────────────────
RULES_W, RULES_H = 1200, 1760   # 2026-09-27 fix-up 한도 빈 카드 버튼 줄 · 데스크톱 배치 줄 · 자연 1736 + 24 · 자연 1658 + 24(2026-09-26 검토 — 배치 줄 하나 · 상환 계획 빈 카드 「부채 보기」)


def _sample_card(title, body, counter, badge=BADGE_AUTO, last=False, footnote=None):
    return fill(card_box(card_inner(title, body, counter, last, badge, footnote), 'position: relative;'), LIGHT)


def _dark_sample():
    """다크 카드 견본 — 다크 짝에서도 그대로 보이게 dc-keep 로 감싼다(한 번만 다크로 바꾼 값)."""
    inner = card_inner('이번 달 소비는 여기서 봐요', '이번 달 월급에서 지금까지 쓴 비율이에요. 막대가 소비 목표 선을 넘지 않게 써 보세요. 월말 예상은 아래 칸에 있어요.',
                       '홈 1 / 3', False)
    card = fill(darken(card_box(inner, 'position: relative;'), 'TourRules-dark'), DARK).replace(f'width: {CARD_W}px;', 'width: 330px;', 1)
    return (f'<!--dc-keep--><div style="background: #080C16; border-radius: 18px; padding: 16px;">{card}</div><!--/dc-keep-->')


def _cap(t, sub=''):
    s = f'<div style="font-size: 12px; line-height: 1.5; color: {C["INK3"]}; margin-top: 2px;">{sub}</div>' if sub else ''
    return f'<div><div style="font-size: 13.5px; font-weight: 700; color: {C["INK"]};">{t}</div>{s}</div>'


def _table(head, rows, widths):
    cols = ' '.join(widths)
    th = ''.join(f'<div style="padding: 8px 10px; font-size: 11.5px; font-weight: 700; color: {C["INK3"]}; background: {C["INSET"]};">{h}</div>' for h in head)
    tr = ''.join(''.join(f'<div style="padding: 8px 10px; font-size: 12px; line-height: 1.5; color: {C["INK2"] if j else C["INK"]}; '
                         f'font-weight: {600 if j == 0 else 400}; border-top: 1px solid {C["LINE_ROW"]};">{c}</div>' for j, c in enumerate(r)) for r in rows)
    return (f'<div style="display: grid; grid-template-columns: {cols}; background: {C["SURF"]}; border: 1px solid {C["LINE"]}; border-radius: 14px; overflow: hidden;">'
            f'{th}{tr}</div>')


def _block(title, inner):
    return (f'<div style="display: flex; flex-direction: column; gap: 8px;">'
            f'<div style="font-size: 14px; font-weight: 700; letter-spacing: -0.01em; color: {C["INK"]};">{title}</div>{inner}</div>')


def _lines(items):
    li = ''.join(f'<li style="margin: 0 0 4px;">{t}</li>' for t in items)
    return f'<ul style="margin: 0; padding-left: 18px; font-size: 12.5px; line-height: 1.55; color: {C["INK2"]};">{li}</ul>'


def rules_board():
    from gen_common import doc
    from nobreak import nobreak
    empty = (f'<div style="background: {C["SURF"]}; border: 1px solid {C["LINE"]}; border-radius: 18px; padding: 22px 16px; text-align: center;">'
             f'<div style="width: 48px; height: 48px; margin: 0 auto; border-radius: 14px; background: {C["BRAND_SOFT"]}; display: flex; align-items: center; justify-content: center;">{icon("wallet", 22, C["BRAND"], 1.9)}</div>'
             f'<div style="font-size: 17px; font-weight: 700; letter-spacing: -0.02em; color: {C["INK"]}; margin-top: 12px;">등록된 자산이 없어요</div>'
             f'<div style="font-size: 13.5px; color: {C["INK3"]}; margin-top: 6px;">첫 자산을 추가하면 순자산이 보여요.</div>'
             f'<div style="display: inline-flex; gap: 6px; margin-top: 16px; height: 44px; padding: 0 20px; border-radius: 13px; background: {C["BRAND"]}; color: #FFFFFF; font-size: 14px; font-weight: 600; align-items: center;">{icon("plus", 16, "#FFFFFF", 2.2)}자산 추가</div></div>')
    left = (f'<div style="width: {CARD_W}px; flex-shrink: 0; display: flex; flex-direction: column; gap: 10px;">'
            + _cap('처음 안내 · 홈 3 / 3', '저절로 뜬 안내. 홈 마지막 단계만 각주 한 줄이 붙는다.')
            + _sample_card('지금 할 일 한 가지', '기록이 쌓이면 가장 효과가 큰 일 하나를 골라 알려 줘요. 누르면 그 화면으로 바로 가요.', '홈 3 / 3', last=True, footnote=HOME_FOOTNOTE)
            + '<div style="height: 6px;"></div>'
            + _cap('화면 안내 · 제목 옆 ?로 다시 연 안내', '단계 · 문구 · 버튼은 같고 알약만 「화면 안내」.')
            + _sample_card('가진 것과 갚을 것', '자산 구성 · 부채 · 상환 계획 세 탭이에요. 부채가 있으면 상환 계획에서 언제 다 갚는지 봐요.', '자산 1 / 3', badge=BADGE_HELP)
            + '<div style="height: 6px;"></div>'
            + _cap('다크', '카드 · 꼬리 #1E2739 · 선 #39455F · 막 rgba(4,7,14,.74).')
            + _dark_sample()
            + '<div style="height: 6px;"></div>'
            + _cap('빈 화면 — 안내도 ?도 없음', '빈 카드 한 장 + 버튼 하나. 본 것으로 기록하지 않아 내용이 생긴 뒤 처음 들어갈 때 안내가 뜬다.')
            + empty + '</div>')
    t_empty = _table(['화면', '빈 화면 = 안내를 미룸', '빈 카드의 버튼'], [
        ('홈', '비지 않음 — 늘 뜬다', '—'),
        ('자산', '자산 0 · 부채 0', '+ 자산 추가'),
        ('부채 · 상환 계획(자산)', '부채 0', '+ 부채 추가'),
        ('상환 계획(미래)', '잔액이 남은 부채 0 — 넣은 부채를 다 갚았으면 버튼은 「부채 보기」', '부채 추가'),
        ('소비', '이번 달 소비 기록 0건', '+ 오늘 쓴 돈 적기'),
        ('내역', '고른 달 기록 0건(이체 포함)', '+ 오늘 쓴 돈 적기'),
        ('한도', '판정할 한도 없음(월급도 직접 정한 한도도 없음 · 소비 목표 0%)', '월급 입력하기(소비 목표 0%면 「소비 목표 바꾸기」 → 내 수치) · 글 링크 「직접 정하기 ›」'),
        ('목적지', '목적지 0', '+ 목적지 추가'),
        ('새 목적지 설계', '비지 않음 — 늘 뜬다', '—'),
        ('미래', '월급 · 부수입 · 자산 · 부채가 하나도 없음', '월급 입력하기 · 자산 추가'),
    ], ['150px', '1fr', '170px'])
    t_close = _table(['누르면', '본 것으로 기록'], [
        ('건너뛰기', '이 화면만'),
        ('안내 모두 끄기', '11화면 모두 — 다른 화면에서도 더 뜨지 않음'),
        ('다음', '기록 안 함 — 다음 단계로'),
        ('알겠어요(마지막 단계)', '이 화면만'),
        ('아래 탭으로 다른 화면', '이 화면만 — 탭 막대는 안내 중에도 밝고 누를 수 있다'),
        ('Esc', '건너뛰기와 같다'),
    ], ['190px', '1fr'])
    right = (f'<div style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 22px;">'
             + _block('언제 뜨나 — 11화면 모두 처음 들어갈 때 저절로', _lines([
                 '홈 · 자산 · 부채 · 상환 계획(자산) · 소비 · 내역 · 한도 · 목적지 · 새 목적지 설계 · 미래 · 상환 계획(미래)마다 3단계.',
                 '빈 화면이면 띄우지 않고 본 것으로도 기록하지 않는다 — 내용이 생긴 뒤 처음 들어갈 때 뜬다. 빈 화면 표는 앱 한 곳(isEmptyScreen)이다.',
                 '다른 창(하루 시트 · 설정 등)이 열려 있으면 그 창이 닫힌 뒤에 뜬다.']) + t_empty)
             + _block('닫는 방법 — 버튼 줄 = 왼쪽 「건너뛰기」 · 「안내 모두 끄기」 + 오른쪽 「다음」/「알겠어요」', t_close + _lines([
                 '저장 중에는 버튼이 흐려지고 오른쪽 버튼이 「저장 중…」. 저장하지 못하면 카드 안 빨간 줄 「안내 상태를 저장하지 못했어요. 다시 눌러 주세요.」(role=alert) — 그 단계에 머문다.']))
             + _block('다시 보기', _lines([
                 '홈이 아닌 화면 = 제목 바로 뒤 「?」(보이는 크기 28 · 누르는 영역 44 · aria 「{화면} 안내 보기」 · 안내 막 아래에선 흐리게) → 같은 3단계, 알약만 「화면 안내」(TourHelpReplay).',
                 '홈에는 「?」가 없다 — 설정 › 도움말 「처음 안내 다시 보기」가 11화면을 모두 되살리고 홈으로 간다.',
                 '빈 화면에는 「?」도 없다.']))
             + _block('단계 수 — 대상이 있는 단계만 센다', _lines([
                 '대상이 화면에 없는 단계는 설명만 보여 주지 않고 건너뛰고, 「{화면} n / N」은 남은 단계만 센다. 홈 구성에서 다음 안내를 끄면 「홈 1 / 2」 · 「홈 2 / 2」.',
                 '각주가 달린 단계(홈 3 / 3)가 빠지면 남은 마지막 단계가 각주를 이어받는다.',
                 '처음 시작한 빈 홈은 다음 안내 자리에 「시작 순서」 카드가 있어 3단계가 그 카드를 설명한다(TourHomeChecklist).']))
             + _block('배치 — 앱 placeTourCard 그대로(좌표를 저장하지 않고 그 자리에서 잰다)', _lines([
                 '카드 폭 min(420, 화면 − 28) · 왼쪽 14. 대상 아래 12에 두고, 안 되면 위 12, 둘 다 안 되면 compact — 탭 막대 위 14에 붙여 대상 위로 겹치고 꼬리 없음.',
                 '대상이 화면 밖(위 8 · 탭 막대 − 8을 넘음)이거나 compact 이면 대상을 위로 스크롤(위 여백 20 · 문서 끝에서 멈춤 — 끝에서는 마지막 내용 아래가 탭 막대 위 62px, 홈은 38px). 스크롤은 다음 단계로 이어진다.',
                 '끝에 막혀 그래도 compact 이고 대상 + 카드가 한 화면에 들어가면 대상 아래를 화면 아래(탭 막대 위 16)에 맞춘다. 홈 1(히어로)이 compact 면 큰 숫자가 위 여백 14에 닿을 때까지만 더 내린다(TOUR_KEEP).',
                 '막 · 강조 · 카드 자리는 아래 탭 막대 위(390 × 844 에서 778)까지 — 탭 막대는 밝게 남는다. 강조 = 흰 2px + 브랜드 4px, 대상의 모서리 그대로.',
                 '꼬리 x = clamp(대상 왼쪽 + 30, 카드 왼쪽 + 24, 카드 오른쪽 − 24) — 오른쪽 끝 버튼(「+ 기록」)을 가리키면 꼬리도 오른쪽.',
                 '데스크톱(1440 등)도 같은 11화면 안내 — 카드 폭 420 · 왼쪽 = 대상 왼쪽(화면 안으로 가둠) · 탭 막대가 없어 막은 화면 끝까지.']))
             + _block('색 · 저장', _lines([
                 '라이트 막 rgba(16,24,40,.62) · 다크 막 rgba(4,7,14,.74) · 다크 카드 · 꼬리 #1E2739 · 선 #39455F.',
                 '저장 = settings.onboarding.tourSeen 11키(home · assets · debts · strategy · spending · ledger · limits · goals · goalDesign · future · payoff). 보호 파일 · 백업 형식 그대로. 키가 없는 옛 사용자는 본 것으로 읽는다.']))
             + '</div>')
    sub = ('앱 v5-stage1 a724aac 의 lib/navi-tour.ts · lib/navi-tour-policy.ts · components/navi/first-run-tour.tsx 그대로. '
           '화면마다의 안내 장(33장)은 이 규칙을 시안 사용자(9월 8일) 화면에 적용한 결과다.')
    body = (f'<div style="display: flex; gap: 32px; align-items: flex-start;">{left}{right}</div>')
    chip = (f'<span style="align-self: flex-start; font-size: 11px; font-weight: 600; letter-spacing: 0.02em; color: {C["INK2"]}; '
            f'border: 1px solid {C["LINE"]}; background: {C["SURF"]}; border-radius: 99px; padding: 4px 10px; white-space: nowrap;">구현 참고 · 앱 화면이 아닙니다</span>')
    frame_ = (f'<div style="width: {RULES_W}px; height: {RULES_H}px; background: {C["BG"]}; color: {C["INK"]}; padding: 28px 30px 30px; display: flex; '
              f'flex-direction: column; gap: 10px; overflow: hidden; font-variant-numeric: tabular-nums;">{chip}'
              f'<h2 style="margin: 2px 0 0; font-size: 20px; font-weight: 700; letter-spacing: -0.025em; color: {C["INK"]};">첫 실행 안내 — 규칙</h2>'
              f'<p style="margin: 0 0 8px; font-size: 13px; line-height: 1.55; color: {C["INK3"]}; max-width: 760px;">{sub}</p>{body}</div>')
    light = nobreak(doc(frame_, keep_all=True))
    return light, darken(light, 'TourRules')


# 장 이름 — 탭 다섯 · 세그먼트 여섯(33장) + 변형 둘 + 참고 장
REGULAR = ['Home', 'Assets', 'Spending', 'Goals', 'Future', 'Debts', 'Strategy', 'Ledger', 'Limits', 'GoalDesign', 'Payoff']
NAMES = [f'Tour{k}{i}' for k in REGULAR for i in range(1, len(TOUR[k][2]) + 1)] + ['TourHomeChecklist', 'TourHelpReplay', 'TourRules', 'TourHomeSample1']


def tour_board(key, i, badge=BADGE_AUTO):
    """key 의 i 번째(0부터) 단계 장 — (라이트, 다크)."""
    board, label, steps = TOUR[key]
    path, title, body, foot = steps[i]
    place = PLACE[key][i]
    n = len(steps)
    inner = card_inner(title, body, f'{label} {i + 1} / {n}', last=(i == n - 1), badge=badge, footnote=foot)
    html = with_overlay(phone(base_html(board), place[0]), overlay(place, inner))
    return fill(html, LIGHT), fill(darken(html, f'Tour{key}{i + 1}'), DARK)


def write(name, pair):
    light, dark = pair
    (OUT / f'{name}.dc.html').write_text(light, encoding='utf-8')
    (OUT / f'Dark{name}.dc.html').write_text(dark, encoding='utf-8')
    print('wrote', name, '+ Dark' + name)


if __name__ == '__main__':
    for key in REGULAR:
        for i in range(len(TOUR[key][2])):
            write(f'Tour{key}{i + 1}', tour_board(key, i))
    write('TourHomeChecklist', tour_board('HomeChecklist', 2))
    write('TourHomeSample1', tour_board('HomeSample', 0))      # 2026-09-27 fix-up 2 — 샘플로 둘러보기로 시작한 홈(흐려진 샘플 띠 아래)
    write('TourHelpReplay', tour_board('Assets', 0, badge=BADGE_HELP))
    write('TourRules', rules_board())
