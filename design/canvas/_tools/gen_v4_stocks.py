# -*- coding: utf-8 -*-
"""v4 · 2~5단계 아트보드 — 내비 재편 · 주식탭 뼈대 · 카테고리 탐색 · 갱신·기준값 설정.

plan/v4-stocks.md §4·§5·§7. 1단계와 같은 방식(라이트를 만들고 darken()으로 다크 짝)이고,
`import gen_v4`가 1단계 5장도 함께 다시 쓴다(멱등). 목적지 탭의 본문은 Goals.dc.html·Future.dc.html에서
그대로 잘라 쓴다 — 내비만 바뀌고 화면은 v3 그대로라는 것이 2단계의 요점이기 때문.

    python3 gen_v4_stocks.py          # 16 + 16장 → ../ , 스냅숏 샘플 → ../../stocks-snapshot.sample.json

2026-09-26(사용성 140건): 앱 v5-stage1 a724aac 에는 주식 화면이 아직 없다(설정 › 홈 구성의 `주식 화면이 나오면 알려 드릴까요?`뿐) —
이 파일의 주식 장은 v4 3 ~ 5단계 계획 그림이고, D1 ~ D20 에 맞춰 말 · 모양만 고쳤다:
머리줄 = 앱 AppTopbar(gen_common · 제목 + `?` · 설정 · 코칭 · 알림 · 부제 없음) · 날짜는 `9월 4일 종가` · `보유 기록` → `보유 추가` ·
`평가액` → `지금 금액` · 맨 위 띠 = `목적지에 나누고 남은 돈`(앱 goal-tools leftoverCapacity · 시안 사용자는 0 → 앱의 0일 때 문구) ·
빈 화면은 카드 한 장 · 행동 하나 · 가정 카드 끝 버튼 `가정 종료` · 목적지 아이콘 = 과녁(앱).
"""
import json
import pathlib
import gen_common
from gen_common import *
import gen_v4 as s1                     # 1단계 조각(mark·topline·checkbox·line_card·cut·OUT)을 재사용
from darken import darken

OUT = s1.OUT
V4B = ['DestGoals', 'DestFuture', 'DestPayoff', 'HomeStocksOff',                                   # 2단계
       'StocksMine', 'HoldingAdd', 'StocksEmpty', 'HomeStocksCard',                  # 3단계
       'StocksHome', 'StockListGrowth', 'StockListDividend', 'StockDetail', 'StockThemes', 'StockStates',   # 4단계
       'StockSettings', 'SnapshotUpdate']                                            # 5단계

# 기준일은 직전 거래일이다. 2026-09-05 · 09-12 는 토요일이라 9/4(금) · 갱신 뒤 9/11(금)을 쓴다.
ASOF = '2026-09-04'                     # 스냅숏 JSON 의 기준일(ISO) — 화면에는 쓰지 않는다
ASOF_S = '9월 4일'                      # 가격 옆 기준일(D12 — ISO · `9/4` 대신 `M월 D일`)
ASOF_L = '2026년 9월 4일'
NEXT_ASOF = '2026-09-11'
NEXT_S = '9월 11일'
NEXT_L = '2026년 9월 11일'
# 맨 위 띠 — 앱 목적지 도구의 leftoverCapacity = max(0, 매달 모을 수 있는 돈 − 목적지에 나눠 넣는 돈)(D4 · D17 · goals-3 · goals-12).
# 시안 사용자(NUMBERS §1 · §7): 매달 모을 수 있는 돈 = 월급 + 부수입 390 − 월말 예상 소비 208 − 대출상환 92 = 90만원, 목적지에 90만원을 다 나눴고 57만원이 모자라 → 남은 돈 0.
CAPACITY = 90                           # 매달 모을 수 있는 돈(만원) — 예전 `이번 달 저축·투자 여력 27만원`(옛 모형)은 앱에 없다
SHORT = 57                              # 목적지에 매달 더 필요한 돈(만원)
NW = ' white-space: nowrap; flex-shrink: 0;'

# 주식 아이콘(캔들 두 개). 다른 탭 아이콘과 같은 24 그리드·1.9 획.
gen_common._P['candle'] = ('<path d="M8 3v3M8 15v6"/><rect x="5" y="6" width="6" height="9" rx="1"/>'
                           '<path d="M16 3v5M16 17v4"/><rect x="13" y="8" width="6" height="9" rx="1"/>')
gen_common._P['star'] = '<path d="m12 2 3.1 6.3 6.9 1-5 4.9 1.2 6.8-6.2-3.2-6.2 3.2 1.2-6.8-5-4.9 6.9-1Z"/>'
gen_common._P['list'] = '<path d="M8 6h13M8 12h13M8 18h13M3 6h.01M3 12h.01M3 18h.01"/>'
gen_common._P['tag'] = '<path d="M20.6 13.4 13.4 20.6a2 2 0 0 1-2.8 0L2 12V2h10l8.6 8.6a2 2 0 0 1 0 2.8Z"/><path d="M7 7h.01"/>'
gen_common._P['file'] = '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8Z"/><path d="M14 2v6h6"/>'


def w(name, body, keep_all=False):
    """keep_all — 한국어가 낱말 중간에서 꺾이지 않게 body 에 word-break: keep-all 을 넣는다."""
    light = doc(body, keep_all=keep_all)
    (OUT / f'{name}.dc.html').write_text(light, encoding='utf-8')
    (OUT / f'Dark{name}.dc.html').write_text(darken(light, name), encoding='utf-8')
    print('wrote', name, '+ Dark' + name)


# ══════════════ 새 바텀 내비 (계획 §4 권장안) ══════════════
NAV_ON = [("home", "홈"), ("wallet", "자산"), ("card", "소비"), ("candle", "주식"), ("target", "목적지")]      # 목적지 = 과녁(앱 · gen_common NAV 와 같은 그림 · a11y-10)
NAV_OFF = [("home", "홈"), ("wallet", "자산"), ("card", "소비"), ("target", "목적지")]


def nav_v4(active, stocks=True):
    items = NAV_ON if stocks else NAV_OFF
    cells = []
    for i, (ic, label) in enumerate(items):
        if i == active:
            cells.append(
                f'<div style="display: flex; flex-direction: column; align-items: center; gap: 3px; flex: 1; padding-top: 4px;">'
                f'<div style="width: 40px; height: 24px; border-radius: 99px; background: {C["BRAND_SOFT"]}; display: flex; align-items: center; justify-content: center;">{icon(ic, 18, C["BRAND"], 2)}</div>'
                f'<span style="font-size: 11px; font-weight: 600; color: {C["BRAND"]};">{label}</span></div>')
        else:
            cells.append(
                f'<div style="display: flex; flex-direction: column; align-items: center; gap: 3px; flex: 1; padding-top: 4px;">'
                f'<div style="width: 40px; height: 24px; display: flex; align-items: center; justify-content: center;">{icon(ic, 18, "#606B7D", 1.9)}</div>'
                f'<span style="font-size: 11px; font-weight: 500; color: #606B7D;">{label}</span></div>')
    return (f'<div style="display: flex; align-items: flex-start; justify-content: space-between; gap: 2px; height: 66px; '
            f'padding: 8px 10px 0; background: {C["SURF"]}; border-top: 1px solid {C["LINE"]}; flex-shrink: 0;">{"".join(cells)}</div>')


# ══════════════ 공통 조각 ══════════════
M_CONTENT = '<div style="flex: 1; min-height: 0; display: flex; flex-direction: column; gap: 10px; padding: 0 14px; overflow: hidden;">'
M_NAV = '<div style="display: flex; align-items: flex-start; justify-content: space-between; gap: 2px; height: 66px;'


def content_of(name):
    """v3 아트보드의 콘텐츠 컨테이너(헤더 아래 ~ 내비 위)를 통째로 가져온다."""
    src = (OUT / f'{name}.dc.html').read_text(encoding='utf-8')
    block = s1.cut(src, M_CONTENT, M_NAV).rstrip()
    assert block.endswith('</div>')
    return block


def asof_badge():
    return badge(f'{ASOF_S} 종가', 'mute').replace('padding: 4px 9px;">', 'padding: 4px 9px; white-space: nowrap; flex-shrink: 0;">', 1)


def back_header(title, sub=None, right=''):
    s = f'<span style="font-size: 12px; font-weight: 500; color: {C["INK3"]};">{sub}</span>' if sub else ''
    return (f'<div style="display: flex; align-items: center; gap: 6px; padding: 12px 12px 12px; flex-shrink: 0;">'
            f'<div style="width: 36px; height: 36px; border-radius: 11px; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">{icon("left", 20, C["INK2"], 2)}</div>'
            f'<div style="display: flex; align-items: baseline; gap: 8px; flex: 1; min-width: 0;">'
            f'<h1 style="margin: 0; font-size: 19px; font-weight: 700; letter-spacing: -0.03em; line-height: 1.2; color: {C["INK"]}; white-space: nowrap;">{title}</h1>{s}</div>{right}</div>')


# 앱 목적지 카드의 한 줄 식(goals-12) — 띠를 두 줄 줄이려고 「= 매달 모을 수 있는 돈 90만원」 대신 「= 90만원」(2026-09-27 fix-up · 주식 홈 아래 기준일 · 면책 줄이 탭 막대 위에 보이게)
# 2026-09-27 fix-up 2: 세 덩어리를 따로 nowrap 으로 묶고 보통 띄어쓰기로 이어 — 폰 장(띠 358)에서는 한 줄 그대로, StockStates 의 좁은 조각(띠 331)에서만 「−」 앞에서 꺾인다(띠 밖으로 넘치지 않게).
_FNW = '<span style="white-space: nowrap;">%s</span>'
# 2026-09-27 fix-up 3: 띠 제목(「목적지에 나누고 남은 돈」)과 같은 값을 말하는 식 — 예전 식은 끝이 「= 90만원」(매달 모을 수 있는 돈)이라 90만원이 남는 것처럼 읽혔다.
# 매달 모을 수 있는 돈 90만(월급 + 부수입 390만 − 월말 예상 소비 208만 − 대출상환 92만)을 목적지에 다 나눠 넣어 0원(앱 leftoverCapacity = max(0, 90만 − 146만)).
FORMULA = (f'<span style="letter-spacing: -0.03em;">{_FNW % f"매달 모을 수 있는 돈 {CAPACITY}만"} '
           f'{_FNW % f"− 목적지에 나눠 넣는 돈 {CAPACITY}만 = 0원"}</span>')


def capacity_band(case='zero'):
    """맨 위 띠 `목적지에 나누고 남은 돈`(앱 goal-tools leftoverCapacity · D4 낱말 · 총수입 · 여력 · 이번 달 · 저축 이체를 쓰지 않는다).
    case = 'zero'(시안 사용자 — 목적지에 이미 다 나눔 → 금액 대신 앱의 0일 때 문장) · 'amount'(남은 돈이 있을 때 — 견본 27만원) ·
    'provisional'(지난달 미마감) · 'nosalary'(월급 없음)."""
    right = ''
    if case == 'zero':
        line = f'목적지에 이미 매달 {CAPACITY}만원을 다 나눴어요 · 지금도 매달 {SHORT}만원이 모자라요'
        sub = FORMULA
    elif case == 'amount':
        line, sub = '목적지에 나눠 넣고 남은 돈이에요', '월급 + 부수입 − 월말 예상 소비 − 대출상환 = 매달 모을 수 있는 돈 · 목적지에 나눠 넣는 중'
        right = f'<span style="font-size: 17px; font-weight: 700; letter-spacing: -0.02em; color: {C["BRAND"]};{NW}">27<span style="font-size: 12.5px; font-weight: 600;">만원</span></span>'
    elif case == 'provisional':
        line, sub = '매달 모을 수 있는 돈은 지난달을 마감한 뒤 계산해요', '지난달들을 마감하면 확정돼요 · <span style="font-weight: 600; color: #3556E6; white-space: nowrap;">6월부터 마감하기 &rsaquo;</span>'
    else:
        line = '—'
        sub = '월급과 소비 기록을 넣으면 매달 모을 수 있는 돈을 계산해 드려요. <span style="font-weight: 600; color: #3556E6; white-space: nowrap;">월급 입력하기 &rsaquo;</span>'
    lcol = C["INK3"] if line == '—' else C["INK"]
    return (f'<div style="display: flex; align-items: flex-start; gap: 8px; padding: 9px 12px; background: {C["BRAND_SOFT"]}; border-radius: 14px; flex-shrink: 0;">'
            f'<span style="flex-shrink: 0; margin-top: 1px;">{icon("arrowu", 15, C["BRAND"], 2.2)}</span>'
            f'<div style="display: flex; flex-direction: column; gap: 2px; flex: 1; min-width: 0;">'
            f'<span style="font-size: 12px; font-weight: 600; color: {C["BRAND_BANNER"]};">목적지에 나누고 남은 돈</span>'
            f'<span style="font-size: 12.5px; font-weight: 600; line-height: 1.45; color: {lcol};">{line}</span>'
            f'<span style="font-size: 11px; line-height: 1.45; color: {C["BRAND_BANNER"]};">{sub}</span></div>{right}</div>')


def guardrail(text, link='목적지 보기'):
    """가드레일 한 줄 — 막지 않고 말만 한다. 아이콘 = 앱 알림 줄의 경고 삼각형(2026-09-27 fix-up · 깃발은 옛 목적지 글리프라 쓰지 않음)."""
    return (f'<div style="display: flex; align-items: center; gap: 8px; padding: 9px 12px; background: {C["WARN_SOFT"]}; border-radius: 12px; flex-shrink: 0;">'
            f'<span style="display: inline-flex; flex-shrink: 0;">{icon("warn", 14, C["WARN"], 2)}</span>'
            f'<span style="flex: 1; min-width: 0; font-size: 12px; line-height: 1.4; color: {C["WARN_INK"]};">{text}</span>'
            f'<span style="font-size: 12px; font-weight: 600; color: {C["WARN"]}; white-space: nowrap;">{link} &rsaquo;</span></div>')


# 사용자가 정한 선(비상금 목적지)을 이름으로 부르고 앱의 다음 안내 말투로(D1 · D16) — 비상금 목적지가 있고 100% 아래일 때만.
GUARD_EMERGENCY = '비상금 6개월 목적지가 68%예요 · 비상금을 먼저 채워 보세요'


def asof_footer(extra='', second='기준에 맞는 종목을 보여주는 것이지 투자 권유가 아니에요.'):
    """second = 둘째 줄(면책). 테마는 기준으로 거른 목록이 아니라 업종 이름표라 따로 준다(2026-09-27 fix-up 2)."""
    return (f'<p style="margin: 2px 2px 0; font-size: 11px; line-height: 1.5; color: {C["INK3"]};">'
            f'데이터 기준일 {ASOF_L} 종가 · 설정 › 주식에서 새로 받기{extra}<br>{second}</p>')


def won(n):
    return f'{n:,}원'


# ══════════════ 표본 — 보유·관심 (3단계, 사용자 입력만) ══════════════
# 종가는 사용자가 직접 넣은 값. 평가액 = 수량 × 종가. 합계 1,244만원 · 매입 대비 +36만원.
HOLD = [('삼성전자', 'KOSPI', 60, 68400, 71200, 'ETF 계좌'),
        ('SK하이닉스', 'KOSPI', 20, 178000, 182500, 'ETF 계좌'),
        ('KODEX 200', 'KOSPI', 120, 36800, 37650, 'ETF 계좌')]
HOLD_TOTAL = sum(q * p for _, _, q, _, p, _ in HOLD)
HOLD_COST = sum(q * a for _, _, q, a, _, _ in HOLD)
assert HOLD_TOTAL == 12_440_000 and HOLD_TOTAL - HOLD_COST == 360_000
WATCH = [('현대차', 'KOSPI', 242000, '배당 · 4분기 확인'), ('삼성전기', 'KOSPI', 156500, ''),
         ('NAVER', 'KOSPI', None, ''), ('카카오', 'KOSPI', None, '관심만'), ('LG에너지솔루션', 'KOSPI', None, '')]


def stock_row(name, market, right, sub, last=False, pad='11px 0'):
    bt = '' if last else f'border-bottom: 1px solid {C["LINE_ROW"]};'
    return (f'<div style="display: flex; align-items: center; gap: 10px; padding: {pad}; {bt}">'
            f'<div style="display: flex; flex-direction: column; gap: 2px; flex: 1; min-width: 0;">'
            f'<div style="display: flex; align-items: baseline; gap: 6px;"><span style="font-size: 14px; font-weight: 600; color: {C["INK"]};">{name}</span>'
            f'<span style="font-size: 11px; color: {C["INK4"]};">{market}</span></div>'
            f'<span style="font-size: 12px; line-height: 1.4; color: {C["INK2"]};">{sub}</span></div>{right}</div>')


def price_col(price, sub, dim=False):
    if price is None:
        return (f'<div style="display: flex; flex-direction: column; align-items: flex-end; gap: 2px; flex-shrink: 0;">'
                f'<span style="font-size: 15px; font-weight: 600; color: {C["DIS"]};">—</span>'
                f'<span style="font-size: 11px; color: {C["INK4"]};">{sub}</span></div>')
    return (f'<div style="display: flex; flex-direction: column; align-items: flex-end; gap: 2px; flex-shrink: 0;">'
            f'<span style="font-size: 15px; font-weight: 600; letter-spacing: -0.02em; color: {C["INK"]};">{won(price)}</span>'
            f'<span style="font-size: 11px; color: {C["INK4"]};">{sub}</span></div>')


# ══════════════ 2단계 · 내비 재편 ══════════════
def dest_header(active):
    return screen_header('목적지', '4개 진행 중 · 앞으로의 항로', tabs=['내 목적지', '자산 경로', '상환 계획'], active=active)


# 목록 끝 점선 버튼 = 앱과 같은 「+ 목적지 추가」(2026-09-27 사용자 결정 2 — 예전 제안 「+ 새 목적지 설계 ›」를 거둠). 새 목적지 설계는 추가 창과 같은 길.
goals_content = content_of('Goals')
assert goals_content.count('</svg>\n      목적지 추가\n    </div>') == 1
w('DestGoals', frame(dest_header(0) + '\n' + goals_content + '\n' + nav_v4(4)), keep_all=True)      # Goals 원본도 keep_all(D14)
w('DestFuture', frame(dest_header(1) + '\n' + content_of('Future') + '\n' + nav_v4(4)), keep_all=True)      # Future 원본도 keep_all — 없으면 아래 안내문이 「금액/은」으로 꺾임
# 상환 계획 — Payoff 본문(저장된 계획 · 2026-09-26)을 그대로, 머리와 내비만 새 것.
payoff_content = content_of('Payoff')
assert '저장된 계획' in payoff_content      # 2026-09-26(DZ2) Payoff = 저장된 계획(D6) — 초안(보라 점선)은 PayoffStates
# Payoff 원본이 keep_all=True 로 쓰이므로(gen_screens) 여기도 같게 — 안내문이 낱말 중간에서 꺾이지 않는다.
w('DestPayoff', frame(dest_header(2) + '\n' + payoff_content + '\n' + nav_v4(4)), keep_all=True)

# 주식 꺼짐 = 4탭. 홈은 시안 사용자의 기본 홈(gen_v4.home_canon — 앱 DEFAULT_HOME_CARDS) 그대로, 내비만 다르다(v4 §4 · 2단계 계획).
# 달력 · 각주가 들어와 홈이 844 를 넘는다. 이 장이 보여 주려는 아래 카드(한도 · 순자산 · 상환 계획)가 보이게 '아래로 스크롤한 상태'로 그린다 —
# 머리는 밀려 올라가고, 본문은 아래 맞춤(flex-end)이라 넘치는 만큼 히어로 윗단이 잘린다. 아래 여백 14 = 카드 사이 간격과 같게.
HOME_SCROLL_PAD = 14
w('HomeStocksOff', frame(s1.home_canon(scrolled_pad=HOME_SCROLL_PAD) + nav_v4(0, stocks=False)), keep_all=True)      # HomeStocksCard 와 같게(D14)


# ══════════════ 3단계 · 주식탭 뼈대 (사용자 입력만) ══════════════
def mine_content(empty=False):
    if empty:
        # 빈 화면 = 카드 한 장 · 행동 하나 · 안내 · `?` 없음(D7 · AMEND 2 · first-run-4) — 앱의 빈 자산 카드와 같은 모양(제안 문구).
        # `이 화면에 없는 것`(실시간 시세 · 주문 …) 한 줄은 페이지 노트로 옮겼다(v4 §5-6).
        empty_card = card(
            f'<div style="display: flex; flex-direction: column; align-items: center; text-align: center; padding: 22px 8px 18px;">'
            # 앱 빈 화면 카드 · EmptyStates D 와 같은 모양(2026-09-27 fix-up): 파란 옅은 칸 + 브랜드 아이콘 · 가운데 작은 버튼 하나
            f'<div style="width: 52px; height: 52px; border-radius: 16px; background: {C["BRAND_SOFT"]}; display: flex; align-items: center; justify-content: center;">{icon("candle", 24, C["BRAND"], 1.8)}</div>'
            f'<span style="margin-top: 14px; font-size: 16px; font-weight: 700; letter-spacing: -0.02em; color: {C["INK"]};">등록된 종목이 없어요</span>'
            f'<span style="margin-top: 6px; font-size: 12.5px; line-height: 1.5; color: {C["INK2"]};">보유 종목을 추가하면 지금 금액이 보여요.</span>'
            f'<div style="margin-top: 16px;">{btn("보유 추가", "primary", "plus", h=40, full=False, size=14).replace("gap: 6px;", "gap: 6px; padding: 0 16px;")}</div></div>', pad='4px 14px')
        return content([empty_card])

    hold_rows = ''.join(
        stock_row(n, m, price_col(q * p, f'{q}주 · 평단 {won(a)}'), f'{ASOF_S} 종가 {won(p)}', last=(i == len(HOLD) - 1), pad='9px 0')
        for i, (n, m, q, a, p, acc) in enumerate(HOLD))
    hold_card = card(
        # '직접 입력' · 계좌 이름은 행마다 되풀이하지 않고 머리말 · 합계 행에 한 번만 쓴다.
        section_head('보유', f'{len(HOLD)}종목 · 종가는 직접 넣은 값이에요', link('보유 추가'))
        .replace(f'font-size: 12px; color: {C["INK3"]};">', f'font-size: 12px; color: {C["INK3"]}; white-space: nowrap;">', 1)
        .replace(f'font-weight: 600; color: {C["BRAND"]};">', f'font-weight: 600; color: {C["BRAND"]};{NW}">', 1)
        + f'<div style="margin-top: 2px;">{hold_rows}</div>'
        + f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px; padding: 10px 0 4px; border-top: 1px solid {C["LINE_SOFT"]};">'
        f'<div style="display: flex; flex-direction: column; gap: 1px;"><span style="font-size: 12.5px; font-weight: 600; color: {C["INK"]};">지금 금액 합계</span>'
        f'<span style="font-size: 11px; color: {C["INK3"]};">{HOLD[0][5]} · 매입 대비 +36만원 · {ASOF_S} 종가 기준</span></div>'
        f'<span style="font-size: 17px; font-weight: 700; letter-spacing: -0.02em; color: {C["INK"]};">1,244<span style="font-size: 12.5px; font-weight: 600; color: {C["INK2"]};">만원</span></span></div>'
        + f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px; padding: 8px 0 2px;">'
        f'<div style="display: flex; flex-direction: column; gap: 1px;"><span style="font-size: 12.5px; font-weight: 500; color: {C["INK2"]};">ETF 계좌 지금 금액에도 반영하기</span>'
        f'<span style="font-size: 11px; color: {C["INK3"]};">꺼 두면 자산·순자산은 계좌에 적은 4,890만원 그대로예요</span></div>{toggle(False)}</div>',
        pad='12px 14px 8px')
    watch_rows = ''.join(
        stock_row(n, m, price_col(p, f'{ASOF_S} · 직접 입력' if p else '종가 미입력'), memo or '&nbsp;', last=(i == len(WATCH) - 1), pad='6px 0')
        for i, (n, m, p, memo) in enumerate(WATCH))
    watch_card = card(section_head('관심', f'{len(WATCH)}종목', link('관심 추가')) + f'<div style="margin-top: 2px;">{watch_rows}</div>', pad='12px 14px 6px')
    return content([capacity_band(), hold_card, watch_card])


# 머리줄 = 앱 AppTopbar(제목 + `?` · 설정 · 코칭 · 알림 · 배지 = 중요 알림 수 · 부제 없음 — D14). 3단계는 `내 종목` 한 화면이라 세그먼트가 없다(4단계부터 `둘러보기 | 내 종목`).
# 탭 장처럼 본문을 다 보여 주는 높이(관심 5종목 끝까지 · 자연 888 + 24 · gen_canvas TALL · screens.json · 2026-09-27 fix-up)
STOCKS_MINE_H = 912
w('StocksMine', frame(screen_header('주식') + mine_content() + nav_v4(3), h=STOCKS_MINE_H), keep_all=True)
w('StocksEmpty', frame(screen_header('주식', help=False) + mine_content(empty=True) + nav_v4(3)), keep_all=True)      # 빈 화면 — `?` 없음(D7)

# 모달 · 보유 기록
# 기준일 칸 = 앱 날짜 입력 모양(달력 아이콘 + `2026. 09. 04.` · 기록 추가의 `날짜`와 같다 · D12)
# 앱 날짜 입력처럼 달력 아이콘이 앞(왼쪽) · 8px 뒤 날짜 · 왼쪽 맞춤(2026-09-27 fix-up · 예전엔 아이콘이 오른쪽 끝)
_df = field("기준일", "2026. 09. 04.", optional=True)
_DATE_SPAN = 'overflow: hidden; white-space: nowrap;">2026. 09. 04.</span>'
assert _df.count(_DATE_SPAN) == 1
_i = _df.index(_DATE_SPAN); _s = _df.rindex('<span', 0, _i)
date_field = _df[:_s] + f'<span style="display: inline-flex; flex-shrink: 0; margin-right: 8px;">{icon("cal", 16, C["INK3"], 1.9)}</span>' + _df[_s:]
assert date_field.count('<rect x="3" y="4"') == 1
w('HoldingAdd', sheet(
    '보유 추가', '종목 · 수량 · 평단만 있으면 저장돼요.<br>종가는 비워 두면 —로 남아요.',
    f'{solo(field("종목", "삼성전자 · 005930 · KOSPI", required=True))}'
    f'<div style="display: flex; gap: 10px;">{field("수량", "60", "주", required=True)}{field("평단", "68,400", "원", required=True)}</div>'
    f'<div style="display: flex; gap: 10px;">{field("종가", "71,200", "원", optional=True)}{date_field}</div>'
    f'{note("종가는 직접 넣는 값이라 실시간 시세가 아니에요. 가격 옆에는 늘 이 기준일이 붙어요.", "mute")}'
    f'{solo(select_field("연결 계좌", "ETF 계좌 · 4,890만원", optional=True))}'
    f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 10px; padding: 12px 13px; background: {C["INSET"]}; border-radius: 14px;">'
    f'<div style="display: flex; flex-direction: column; gap: 2px;"><span style="font-size: 13.5px; font-weight: 600; color: {C["INK"]};">계좌 지금 금액에도 반영하기</span>'
    f'<span style="font-size: 11.5px; line-height: 1.45; color: {C["INK3"]};">켜면 수량 × 종가가 ETF 계좌 지금 금액에 더해져<br>자산 · 순자산 · 자산 경로에 반영돼요. 기본은 꺼짐이에요.</span></div>{toggle(False)}</div>',
    sheet_footer('취소', '보유 추가'), body_pb=14), keep_all=True)

# 홈 · 주식 요약 카드 (구성에서 주식을 켠 사용자)
stock_summary_card = card(
    f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 10px; height: 46px;">'
    f'<div style="display: flex; flex-direction: column; gap: 2px; min-width: 0;">'
    f'<span style="font-size: 13.5px; font-weight: 600; color: {C["INK"]};">주식 요약</span>'
    f'<span style="font-size: 11.5px; color: {C["INK3"]}; white-space: nowrap;">보유 3 · 관심 5 · {ASOF_S} 종가 · 직접 입력</span></div>'
    f'<div style="display: flex; align-items: center; gap: 8px; flex-shrink: 0;">'
    f'<span style="font-size: 15px; font-weight: 600; letter-spacing: -0.02em; color: {C["INK"]};">1,244만원</span>'
    f'{icon("right", 16, C["INK4"], 2)}</div></div>', pad='4px 14px')
# 앱에는 아직 주식 요약 카드가 없다(준비 중 · 홈 구성에서도 세지 않음) — 이 장은 v4 3단계 뒤의 계획 그림이다(캔버스 제목 · 노트에 적음).
# 한도 라벨은 단계 라벨이 사라져 늘 `오늘 포함 하루 45,220원`(D3 · tasks-2) + 둘째 줄(home-3) — Main 의 한도 카드 그대로.
assert s1.limit_block.count('오늘 포함 하루 45,220원') == 1 and '앞으로 하루' not in s1.limit_block and '216만원 중 112만원 썼어요' in s1.limit_block
HOME_SCROLLED = s1.M_CONTENT.replace('padding: 0 14px;', f'justify-content: flex-end; padding: 0 14px {HOME_SCROLL_PAD}px;')
w('HomeStocksCard', frame(
    f'\n  {HOME_SCROLLED}\n\n'
    f'    {s1.hero_block}\n\n    {s1.calendar_block}\n\n    {s1.guide_block}\n\n    {stock_summary_card}\n\n    {s1.limit_block}\n\n    {s1.networth_card}\n\n  </div>\n\n'
    f'  {nav_v4(0)}\n'), keep_all=True)


# ══════════════ 4단계 · 카테고리 탐색 (내장 스냅숏) ══════════════
# 스냅숏 표본. 이름은 실재 종목이지만 수치는 전부 디자인 검증용 가상값이다 (샘플 JSON의 _ 참고).
GROWTH = [  # (이름, 시장, 종가, 이유 한 줄, 충족, 분모)
    ('삼성전자', 'KOSPI', 71200, '영업이익 3년간 연 18% 증가', 3, 3),
    ('SK하이닉스', 'KOSPI', 182500, '매출 3년간 연 24% 증가', 3, 3),
    ('삼양식품', 'KOSPI', 1020000, '매출 3년간 연 32% 증가', 3, 3),
    ('알테오젠', 'KOSDAQ', 312000, '영업이익 3년간 연 41% 증가 · 3년 중 2년만 증가', 2, 3),
    ('리노공업', 'KOSDAQ', 198000, '3년 내내 이익 증가 · 매출 성장은 연 8%', 2, 3),
    ('레인보우로보틱스', 'KOSDAQ', 148000, '매출 연 33% 증가 · 이익 자료 2년뿐', 1, 1),      # 「기록」은 돈 기록만(D4) — 회사 자료는 「자료」
]
DIVIDEND = [
    ('KT&amp;G', 'KOSPI', 118500, '배당수익률 5.1% · 12년 연속', 3, 3),
    ('하나금융지주', 'KOSPI', 68900, '배당수익률 4.8% · 9년 연속', 3, 3),
    ('삼성화재', 'KOSPI', 372000, '배당수익률 3.9% · 배당성향 44%', 3, 3),
    ('신한지주', 'KOSPI', 61400, '배당수익률 3.4% · 배당성향 26%', 3, 3),      # 머리 「충족 기준 수 ▾」 순서대로 3/3 넷 → 2개 충족(2026-09-27 fix-up 2)
    ('맥쿼리인프라', 'KOSPI', 12850, '배당수익률 5.6% · 배당성향 —', 2, 2),
    ('현대차', 'KOSPI', 242000, '배당수익률 4.2% · 3년 연속', 2, 3),
]
assert [r[4] for r in DIVIDEND] == sorted((r[4] for r in DIVIDEND), reverse=True)


def met_chip(k, n):
    full = k == n
    col, bg = (C["INK"], C["INSET"]) if full else (C["INK3"], C["INSET"])
    return (f'<span style="display: inline-flex; align-items: center; gap: 4px; padding: 3px 8px; border-radius: 99px; background: {bg}; '
            f'font-size: 11px; font-weight: 600; color: {col}; white-space: nowrap;">{k}/{n} 충족</span>')


def list_rows(rows, total=3):
    """total = 그 목록의 기준 수. 분모가 total 보다 작으면(자료 없는 기준이 있으면) 배지 아래에 몇 개가 빠졌는지 적는다 —
    '1/1 충족'이 '3/3 충족'과 똑같이 읽히지 않게."""
    out = []
    for i, (n, m, p, why, k, d) in enumerate(rows):
        missing = (f'<span style="font-size: 11px; color: {C["INK4"]}; white-space: nowrap;">{total - d}개 자료 없음</span>'
                   if d < total else '')
        right = (f'<div style="display: flex; flex-direction: column; align-items: flex-end; gap: 4px; flex-shrink: 0;">'
                 f'<span style="font-size: 15px; font-weight: 600; letter-spacing: -0.02em; color: {C["INK"]};">{won(p)}</span>{met_chip(k, d)}{missing}</div>')
        out.append(stock_row(n, m, right, why, last=(i == len(rows) - 1)))
    return ''.join(out)


def crit_chips(labels, on=(True, True, True)):
    cells = []
    for lab, o in zip(labels, on):
        if o:
            cells.append(f'<span style="display: inline-flex; align-items: center; gap: 5px; height: 30px; padding: 0 10px 0 8px; border-radius: 99px; background: {C["BRAND"]}; color: #FFFFFF; font-size: 12px; font-weight: 600; white-space: nowrap;">{icon("check", 12, "#FFFFFF", 3)}{lab}</span>')
        else:
            cells.append(f'<span style="display: inline-flex; align-items: center; height: 30px; padding: 0 11px; border-radius: 99px; background: {C["SURF"]}; border: 1px solid {C["BORDER"]}; color: {C["INK2"]}; font-size: 12px; font-weight: 500; white-space: nowrap;">{lab}</span>')
    return f'<div style="display: flex; flex-wrap: wrap; gap: 6px;">{"".join(cells)}</div>'


def sort_row(count):
    return (f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px; padding: 0 2px;">'
            f'<span style="font-size: 12px; color: {C["INK3"]};">{count}종목 · 기준을 끄면 목록이 달라져요</span>'
            f'<span style="display: inline-flex; align-items: center; gap: 3px; font-size: 12px; font-weight: 600; color: {C["INK2"]};">충족 기준 수 {icon("down", 13, C["INK2"], 2.2)}</span></div>')


def more_row(n):
    return (f'<div style="display: flex; align-items: center; justify-content: center; gap: 4px; height: 42px; border-top: 1px solid {C["LINE_ROW"]}; font-size: 12.5px; font-weight: 600; color: {C["BRAND"]};">아래로 {n}종목 더{icon("down", 14, C["BRAND"], 2.2)}</div>')


def list_screen(title, sub, chips, rows, count):
    """카테고리 목록 — 시트가 아닌 화면이라 앱처럼 아래 탭(주식 켬)을 둔다(StockThemes 와 같게)."""
    return frame(
        back_header(title, sub, asof_badge())
        + content([f'<div style="display: flex; flex-direction: column; gap: 9px;">{chips}{sort_row(count)}</div>',
                   card(list_rows(rows) + more_row(count - len(rows)), pad='2px 14px 0'),
                   asof_footer()], gap=10)
        + nav_v4(3))


w('StockListGrowth', list_screen('성장주', '기준 3개',
                                 crit_chips(['매출 성장', '이익 성장 속도', '꾸준한 이익 증가']), GROWTH, 12), keep_all=True)
w('StockListDividend', list_screen('배당주', '기준 3개',
                                   crit_chips(['높은 배당수익률', '연속 배당', '무리 없는 배당']), DIVIDEND, 27), keep_all=True)      # 기준 셋 다 켬 — 머리 「기준 3개」 · 3/3 충족과 맞게(2026-09-27 fix-up)


# 주식 홈 (S1)
def cat_card(ic, name, count, chips, col):
    ch = ''.join(f'<span style="font-size: 11px; font-weight: 500; color: {C["INK2"]}; background: {C["INSET"]}; border-radius: 99px; padding: 3px 8px; white-space: nowrap;">{c}</span>' for c in chips)
    # 머리 한 줄 = 아이콘 · 이름 + 개수 · › (2026-09-27 fix-up — 예전 아이콘 줄을 따로 두어 격자가 396 이라 기준일 · 면책 줄이 탭 막대 밑에 가렸다)
    return (f'<div style="background: {C["SURF"]}; border: 1px solid {C["LINE"]}; border-radius: 18px; padding: 12px 12px 12px; display: flex; flex-direction: column; gap: 9px; min-width: 0;">'
            f'<div style="display: flex; align-items: center; gap: 8px;">'
            f'<div style="width: 30px; height: 30px; border-radius: 10px; background: {col}18; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">{icon(ic, 16, col, 2)}</div>'
            f'<div style="display: flex; flex-direction: column; gap: 1px; flex: 1; min-width: 0;"><span style="font-size: 15px; font-weight: 700; letter-spacing: -0.02em; line-height: 1.25; color: {C["INK"]};">{name}</span>'
            f'<span style="font-size: 11px; color: {C["INK3"]}; white-space: nowrap;">{count}</span></div>'
            f'{icon("right", 15, C["INK4"], 2)}</div>'
            f'<div style="display: flex; flex-wrap: wrap; gap: 4px;">{ch}</div></div>')


cats = (f'<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 10px; align-items: start;">'
        + cat_card('arrowur', '성장', '12종목 · 기준 3개', ['매출 성장', '이익 성장 속도', '꾸준한 이익 증가'], C["BRAND"])
        + cat_card('search', '저평가', '19종목 · 기준 4개', ['순자산 대비 저평가', '자본 대비 이익 높음', '주가 회복 중', '매출 대비 이익 높음'], C["SKY"])
        + cat_card('leaf', '배당', '27종목 · 기준 3개', ['높은 배당수익률', '연속 배당', '무리 없는 배당'], C["POS"])
        + cat_card('tag', '테마', '14개 테마', ['반도체', '2차전지', '바이오', 'AI'], C["VIO"])
        + '</div>')
mine_summary = card(
    f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 10px; height: 46px;">'
    f'<div style="display: flex; flex-direction: column; gap: 2px; min-width: 0;">'
    f'<span style="font-size: 13.5px; font-weight: 600; color: {C["INK"]};">내 종목</span>'
    f'<span style="font-size: 11.5px; color: {C["INK3"]}; white-space: nowrap;">보유 3 · 관심 5 · {ASOF_S} 종가</span></div>'
    f'<div style="display: flex; align-items: center; gap: 8px; flex-shrink: 0;">'
    f'<span style="font-size: 15px; font-weight: 600; letter-spacing: -0.02em; color: {C["INK"]};">1,244만원</span>{icon("right", 16, C["INK4"], 2)}</div></div>', pad='4px 14px')
w('StocksHome', frame(
    screen_header('주식', tabs=['둘러보기', '내 종목'], active=0)
    + content([capacity_band(),
               guardrail(GUARD_EMERGENCY),
               mine_summary, cats, asof_footer()], gap=10)
    + nav_v4(3)), keep_all=True)


# 종목 상세 (S3) — 내 항로에 넣어보기는 calc/goals.py의 months_to와 같은 식 (연이율/12).
def months_to(target, cur, monthly, apr):
    i = apr / 100 / 12
    b, m = cur, 0
    while b < target and m < 1200:
        b = b * (1 + i) + monthly
        m += 1
    return m


def ym(k, start=(2026, 9)):
    t = start[0] * 12 + (start[1] - 1) + k
    return t // 12, t % 12 + 1


# 내 항로에 넣어보기 — 기준은 그 목적지의 `이 목적지에 매달 넣을 돈`(naviGoalAllocation · 시안 사용자 매달 19만원 → 도착 2033년 12월)이고,
# 15만원을 더하면 2031년 9월 · 2년 3개월 빨라진다(NUMBERS §7 · §14 — 앱 엔진 값 · goalArrivalMonths). 옛 고정 28만원 · months_to 셈은 쓰지 않는다(D17).
BASE_Y, BASE_M = 2033, 12
SIM_Y, SIM_M = 2031, 9
AHEAD = (BASE_Y * 12 + BASE_M) - (SIM_Y * 12 + SIM_M)
assert AHEAD == 27
LOW, HIGH, CUR = 52100, 88800, 71200
POS_PCT = round((CUR - LOW) / (HIGH - LOW) * 100, 1)


def reason_row(ok, label, rule, val, last=False, pad='9px 0'):
    bt = '' if last else f'border-bottom: 1px solid {C["LINE_ROW"]};'
    mark_ = (f'<span style="width: 22px; height: 22px; border-radius: 99px; background: {C["POS_SOFT"]}; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">{icon("check", 13, C["POS"], 3)}</span>'
             if ok else f'<span style="width: 22px; height: 22px; border-radius: 99px; background: {C["INSET"]}; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">{icon("x", 12, C["INK3"], 2.6)}</span>')
    return (f'<div style="display: flex; align-items: center; gap: 10px; padding: {pad}; {bt}">{mark_}'
            f'<div style="display: flex; flex-direction: column; gap: 1px; flex: 1; min-width: 0;">'
            f'<span style="font-size: 13.5px; font-weight: 600; color: {C["INK"]};">{label}</span>'
            f'<span style="font-size: 11.5px; color: {C["INK3"]};">{rule}</span></div>'
            f'<span style="font-size: 14px; font-weight: 600; letter-spacing: -0.02em; color: {C["INK"]}; white-space: nowrap;">{val}</span></div>')


price_head = (
    f'<div style="display: flex; align-items: flex-end; justify-content: space-between; gap: 10px;">'
    f'<div style="display: flex; align-items: baseline; gap: 3px;"><span style="font-size: 34px; font-weight: 700; letter-spacing: -0.04em; line-height: 1; color: {C["INK"]};">71,200</span>'
    f'<span style="font-size: 16px; font-weight: 600; color: {C["INK2"]};">원</span></div>{asof_badge()}</div>')
price_card = hero(
    price_head
    + f'<div style="display: flex; align-items: center; gap: 6px; margin-top: 8px;">{badge("성장", "brand")}{badge("배당", "pos")}'
    f'<span style="font-size: 11.5px; color: {C["INK3"]};">성장·배당 두 목록에 있어요</span></div>'
    f'<div style="margin-top: 10px;"><div style="display: flex; justify-content: space-between; font-size: 11px; color: {C["INK3"]};"><span>52주 저 {won(LOW)}</span><span>52주 고 {won(HIGH)}</span></div>'
    f'<div style="position: relative; height: 8px; border-radius: 99px; background: {C["TRACK"]}; margin-top: 5px;">'
    f'<div style="position: absolute; left: {POS_PCT}%; top: -4px; width: 16px; height: 16px; margin-left: -8px; border-radius: 99px; background: {C["SURF"]}; border: 2.5px solid {C["INK"]};"></div></div>'
    f'<div style="font-size: 11px; color: {C["INK3"]}; margin-top: 7px; text-align: center;">52주 저점과 고점 사이 {POS_PCT:.0f}% 지점</div></div>', pad='12px 14')
reason_card = card(
    section_head('성장주 목록에 있는 이유', '3 / 3 충족')
    + f'<div style="margin-top: 2px;">'
    + reason_row(True, '매출 성장', '매출 3년 연평균 증가율 10% 이상', '연 12%', pad='7px 0')
    + reason_row(True, '이익 성장 속도', '영업이익 3년 연평균 증가율 15% 이상', '연 18%', pad='7px 0')
    + reason_row(True, '꾸준한 이익 증가', '최근 3년 동안 해마다 영업이익 증가', '3년 중 3년', last=True, pad='7px 0') + '</div>',
    pad='12px 14px 4px')
metrics_card = card(
    f'<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 0;">'
    + ''.join(f'<div style="display: flex; flex-direction: column; gap: 3px; {"padding-left: 10px; border-left: 1px solid " + C["LINE_SOFT"] + ";" if i else "padding-right: 10px;"}">'
              f'<span style="font-size: 11.5px; font-weight: 500; color: {C["INK3"]};">{k}</span>'
              f'<span style="font-size: 16px; font-weight: 600; letter-spacing: -0.02em; color: {C["INK"]};">{v}</span></div>'
              for i, (k, v) in enumerate([('연 매출', '300.9조'), ('영업이익', '32.7조'), ('이익 증가율', '연 18%')]))   # 성장 = 매출 · 영업이익 · 증가율(계획 §5-2 S3). 값은 이유 카드 '이익 성장 속도 연 18%'와 같다.
    + '</div>', pad='11px 14px')
sim_card = (
    f'<div style="background: {C["SURF"]}; border: 1px dashed {C["VIO_LINE"]}; border-radius: 18px; padding: 12px 14px; flex-shrink: 0;">'
    f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px;">{badge("저장되지 않는 가정", "vio", "spark")}'
    f'<span style="font-size: 12px; font-weight: 600; color: {C["INK3"]};">가정 종료</span></div>'
    f'<p style="margin: 10px 0 0; font-size: 15px; font-weight: 600; letter-spacing: -0.015em; color: {C["INK"]};">내 항로에 넣어보기</p>'
    f'<div style="display: flex; align-items: baseline; justify-content: space-between; gap: 8px; margin-top: 6px;">'
    f'<span style="font-size: 12.5px; color: {C["INK2"]};">이 종목에 매달</span>'
    f'<span style="font-size: 22px; font-weight: 700; letter-spacing: -0.03em; color: {C["VIO_STRONG"]};">15<span style="font-size: 13px; font-weight: 600;">만원</span></span></div>'
    f'<div style="margin-top: 4px;">{slider(round(15 / CAPACITY * 100, 1), C["VIO"])}</div>'
    # 결과는 두 행으로 — 한 줄에 네 덩어리를 넣으면 전부 두 줄로 꺾인다.
    f'<div style="margin-top: 8px; font-size: 12px; color: {C["INK3"]}; white-space: nowrap;">투자 계좌 5,000만원 도착</div>'
    f'<div style="display: flex; align-items: center; gap: 6px; margin-top: 5px; font-size: 13px; color: {C["INK2"]}; white-space: nowrap;">'
    f'<span style="font-weight: 500; color: {C["INK4"]}; text-decoration: line-through; flex-shrink: 0;">{BASE_Y}년 {BASE_M}월</span>{icon("arrowr", 13, C["VIO_STRONG"], 2.4)}'
    f'<span style="font-size: 14px; font-weight: 700; color: {C["VIO_STRONG"]}; flex-shrink: 0;">{SIM_Y}년 {SIM_M}월</span>'
    f'<span style="margin-left: auto; display: inline-flex; align-items: center; background: {C["VIO_SOFT"]}; color: {C["VIO_STRONG"]}; font-size: 11.5px; font-weight: 600; '
    f'border-radius: 99px; padding: 4px 9px; white-space: nowrap; flex-shrink: 0;">{AHEAD // 12}년 {AHEAD % 12}개월 빨라져요</span></div>'
    # 슬라이더 끝 = 매달 모을 수 있는 돈 90만원(제안) — 시안 사용자는 이미 목적지에 다 나눠서 이 금액은 그 위에 더 넣는 가정이다(goals-3 · D17).
    # 두 줄로(2026-09-27 fix-up · 세 줄이면 가정 카드 아래가 버튼 줄에 가림). 「연 5.0%로」는 % 뒤에서 꺾이지 않게 nowrap(D14 · D4 수익률 연 N%).
    f'<p style="margin: 8px 0 0; font-size: 11px; line-height: 1.45; color: {C["INK3"]};">이미 목적지에 다 나눈 {CAPACITY}만원 위에 15만원을 더 넣는 가정이에요. '
    f'수익률은 투자 계좌 5,000만원 목적지의 <span style="white-space: nowrap;">연 5.0%로</span> 계산했어요.</p></div>')
detail_actions = (f'<div style="display: flex; gap: 8px; padding: 10px 14px 20px; background: {C["SURF"]}; border-top: 1px solid {C["LINE"]}; flex-shrink: 0;">'
                  f'{btn("관심 추가", "secondary", "star", h=48).replace("width: 100%;", "flex: 1;")}'
                  f'{btn("보유 추가", "primary", "plus", h=48).replace("width: 100%;", "flex: 1.3;")}</div>')
w('StockDetail', frame(
    back_header('삼성전자', '005930 · KOSPI')
    + content([price_card, reason_card, metrics_card, sim_card], gap=6).replace('padding: 0 14px;', 'padding: 0 14px 12px;', 1)      # 카드 사이 6 — 가정 카드 아래가 버튼 줄 위 12px 넘게 떨어지게(2026-09-27 fix-up)
    + detail_actions), keep_all=True)


# 테마 (S4)
THEMES = [('반도체', 24), ('2차전지', 18), ('바이오', 31), ('AI', 15), ('방산', 9), ('조선', 7), ('로봇', 11),
          ('자동차', 12), ('금융', 20), ('엔터', 8), ('건설', 10), ('유틸리티', 6), ('화장품', 9), ('게임', 7)]
theme_cells = ''.join(
    f'<div style="display: flex; align-items: center; gap: 8px; height: 46px; padding: 0 12px; background: {C["SURF"]}; border: 1px solid {C["LINE"]}; border-radius: 14px; min-width: 0;">'
    f'{icon("tag", 14, C["VIO"], 2)}<span style="flex: 1; min-width: 0; font-size: 13.5px; font-weight: 600; color: {C["INK"]}; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">{n}</span>'
    f'<span style="font-size: 11.5px; color: {C["INK3"]}; white-space: nowrap;">{c}</span></div>'
    for n, c in THEMES)
theme_grid = f'<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 8px;">{theme_cells}</div>'
w('StockThemes', frame(
    back_header('테마', f'{len(THEMES)}개 테마', asof_badge())
    + content([note('테마는 기준으로 거른 목록이 아니라 <b style="font-weight: 600;">업종별로 묶어 둔 이름표</b>예요. 한 종목이 여러 테마에 들어갈 수 있어요.', 'mute', 'tag'),
               theme_grid, asof_footer(second='업종별로 묶어 보여주는 것이지 투자 권유가 아니에요.')], gap=10)
    + nav_v4(3)), keep_all=True)


# ══════════════ 설명 장 틀 (gen_v5.py 의 spec_frame · mark 와 같은 틀) ══════════════
def spec_frame(w_, h_, title, sub, body, sub_w=720):
    chip = (f'<span style="align-self: flex-start; font-size: 11px; font-weight: 600; letter-spacing: 0.02em; color: {C["INK2"]}; '
            f'border: 1px solid {C["LINE"]}; background: {C["SURF"]}; border-radius: 99px; padding: 4px 10px;">구현 참고 · 앱 화면이 아닙니다</span>')
    return (f'<div style="width: {w_}px; height: {h_}px; background: {C["BG"]}; color: {C["INK"]}; padding: 28px 30px 30px; display: flex; '
            f'flex-direction: column; gap: 10px; overflow: hidden; font-variant-numeric: tabular-nums;">{chip}'
            f'<h2 style="margin: 2px 0 0; font-size: 20px; font-weight: 700; letter-spacing: -0.025em; color: {C["INK"]};">{title}</h2>'
            f'<p style="margin: 0 0 8px; font-size: 13px; line-height: 1.55; color: {C["INK3"]}; max-width: {sub_w}px;">{sub}</p>{body}</div>')


def num(n, pos=''):
    """번호 표시. pos = 화면 조각 위에 얹을 때의 위치 스타일."""
    return (f'<span style="{pos}flex-shrink: 0; width: 17px; height: 17px; border-radius: 99px; background: {C["INK"]}; color: #FFFFFF; '
            f'font-size: 10.5px; font-weight: 700; display: inline-flex; align-items: center; justify-content: center; '
            f'box-shadow: 0 0 0 2px {C["SURF"]};">{n}</span>')


def marked(n, html):
    return f'<div style="position: relative;">{html}{num(n, "position: absolute; top: -6px; right: -6px; ")}</div>'


def cap(t):
    return f'<div style="font-size: 11px; font-weight: 600; letter-spacing: 0.06em; color: #606B7D; padding: 0 2px 6px;">{t}</div>'


def spec_cell(n, title, desc, spec):
    return (f'<div style="display: flex; flex-direction: column; gap: 9px; min-width: 0;">'
            f'<div style="display: flex; gap: 9px; align-items: flex-start;"><span style="display: inline-flex; margin-top: 2px;">{num(n)}</span>'
            f'<div style="display: flex; flex-direction: column; gap: 2px; min-width: 0;">'
            f'<span style="font-size: 13.5px; font-weight: 600; line-height: 1.4; color: {C["INK"]};">{title}</span>'
            f'<span style="font-size: 12px; line-height: 1.4; color: {C["INK3"]};">{desc}</span></div></div>{spec}</div>')


def spec_cols(left, cells, foot):
    grid = f'<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 22px 24px; align-items: start;">{"".join(cells)}</div>'
    note_ = f'<p style="margin: 18px 2px 0; font-size: 12px; line-height: 1.6; color: {C["INK3"]};">{foot}</p>'
    return (f'<div style="display: flex; gap: 28px; align-items: flex-start;">'
            f'<div style="width: 362px; flex-shrink: 0; display: flex; flex-direction: column;">{left}</div>'
            f'<div style="flex: 1; min-width: 0;">{grid}{note_}</div></div>')


def strong(t):
    return f'<b style="font-weight: 600; color: {C["INK2"]};">{t}</b>'


SPACER = '<div style="height: 16px;"></div>'
FRAG = f'border: 1px solid {C["INPUT"]}; border-radius: 22px; overflow: hidden; background: {C["BG"]};'

# 특수한 상황 (4단계) — 경고 띠 3종 · 자료 없음 2종 · 여러 목록. 왼쪽은 실제 화면 조각, 오른쪽은 번호별 견본.
band_emergency = guardrail(GUARD_EMERGENCY)
# 월말 예상이 소비 목표를 넘을 때 — 앱 알림 문구(D1 · D4 · home-8). 판정은 소비 목표로만 · 누르면 이번 달 소비로(한도가 아니라).
# 값은 앱 하네스(캐논 + 9월 2일 쇼핑 300,000원 → 월말 예상 66.2% · NUMBERS §14 · 2026-09-27 fix-up 2 — 63.2%는 옛 장의 값)
band_over = guardrail('월말엔 소비 목표 60%를 넘어요 · 월말 예상 월급의 66.2%예요. 월 22만원 줄이면 소비 목표 안이에요.', '이번 달 소비')      # 앱 알림 둘째 문장까지(2026-09-27 fix-up 3)
row_short = card(list_rows([GROWTH[5]]), pad='2px 14px')
row_nodiv = card(list_rows([next(r for r in DIVIDEND if r[0] == '맥쿼리인프라')]), pad='2px 14px')
list_badges = (f'<div style="display: flex; align-items: center; gap: 6px; margin-top: 8px;">'
               + (badge("성장", "brand") + badge("배당", "pos")).replace('padding: 4px 9px;">', 'padding: 4px 9px;' + NW + '">') + '</div>')
detail_top = hero(price_head.replace('padding: 4px 9px;">', 'padding: 4px 9px;' + NW + '">') + list_badges, pad='12px 14')
_home_head = screen_header('주식', tabs=['둘러보기', '내 종목'], active=0)
assert _home_head.count('padding: 14px 16px 12px;') == 1      # gen_common screen_header 의 바깥 여백 — 바뀌면 여기서 멈춘다
home_head = _home_head.replace('padding: 14px 16px 12px;', 'padding: 14px 14px 12px;', 1)
home_frag = (f'<div style="{FRAG}">{home_head}<div style="display: flex; flex-direction: column; gap: 10px; padding: 0 14px 14px;">'
             f'{capacity_band()}{marked(1, band_emergency)}{mine_summary}</div></div>')
name_bar = (f'<div style="display: flex; align-items: baseline; gap: 8px; padding: 0 2px 8px;">'
            f'<span style="font-size: 19px; font-weight: 700; letter-spacing: -0.03em; line-height: 1.2; color: {C["INK"]}; white-space: nowrap;">삼성전자</span>'
            f'<span style="font-size: 12px; font-weight: 500; color: {C["INK3"]};">005930 · KOSPI</span></div>')
states_left = (cap('주식 홈 · 위쪽') + home_frag + SPACER
               + cap('종목 목록 · 한 줄') + marked(2, card(list_rows(GROWTH[:2]), pad='2px 14px')) + SPACER
               + cap('종목 상세 · 맨 위') + name_bar + marked(3, detail_top))
states_cells = [
    spec_cell(1, '비상금이 모자랄 때', '비상금 목적지가 있고 100% 아래일 때만 주식 홈 위쪽에 보여요. 누르면 목적지로 가요.', band_emergency),
    spec_cell(1, '월말 예상이 소비 목표를 넘을 때', '월급이 있고 지난달을 마감해 월말 예상이 확정된 달에만 보여요 · 임시 계산 중엔 판정하지 않아요. 누르면 이번 달 소비로 가요.', band_over),
    spec_cell(1, '경고 띠가 둘 다 없을 때', '비상금 · 월말 예상 경고 띠만 빠지고, 맨 위 <span style="white-space: nowrap;">「목적지에 나누고 남은 돈」</span> 띠와 내 종목 카드는 그대로예요.',
              f'<div style="display: flex; flex-direction: column; gap: 10px;">{capacity_band()}{mine_summary}</div>'),
    spec_cell(1, '지난달을 아직 마감하지 않았을 때', '금액을 보이지 않아요. 누르면 가장 앞선 달의 마감 창이 열려요.', capacity_band('provisional')),
    spec_cell(1, '월급이 없을 때', '0원으로 치지 않고 —로 둬요. 누르면 월급 입력 시트가 열려요.', capacity_band('nosalary')),
    spec_cell(2, '상장한 지 얼마 안 돼 자료가 짧을 때', '자료가 없는 기준은 충족 수에서 빼고, 몇 개가 빠졌는지 배지 아래에 적어요. 0으로 세지 않아요.', row_short),
    spec_cell(2, '배당 자료가 없을 때', '배당성향을 알 수 없으면 —로 두고, 자료가 있는 기준 2개로만 세요.', row_nodiv),
    spec_cell(3, '한 종목이 두 목록에 있을 때', '흔한 일이라 경고 없이 배지로만 알려요. 배지는 줄이 바뀌어도 쪼개지지 않아요.', detail_top),
]
STATES_H = 975      # 2026-09-27 fix-up 3 자연 951 + 24(과소비 띠 둘째 문장 · 식 줄) · 2026-09-27 fix-up 2 자연 950 + 24(주식 홈 조각의 식 줄이 「−」 앞에서 두 줄) · 2026-09-27 fix-up 셀 제목 · 경고 아이콘 · 자연 934 + 24 · 자연 높이 + 24(8가지 · 2026-09-26 잼). gen_canvas WIDE · screens.json 과 같아야 한다
w('StockStates', spec_frame(
    1180, STATES_H, '주식 탭 · 특수한 상황 8가지',
    '경고 띠는 알려주기만 하고 아무것도 막지 않아요. 자료가 없는 기준은 —로 두고 충족 수에서 빼요. 왼쪽 화면의 번호를 오른쪽에서 찾으세요.',
    spec_cols(states_left, states_cells,
              f'—는 0점이 아니라 {strong("자료 없음")}이라는 뜻이에요. 레인보우로보틱스는 성장 기준 3개 중 자료가 있는 1개만 세어 {strong("1/1 충족")}으로 보여요.')),
  keep_all=True)


# 스냅숏 표본 JSON — 종목당 20필드. 수치는 전부 가상.
snap = {
    '_': '디자인 검증용 스냅숏 표본. 종목명은 실재하지만 수치는 전부 가상값이며 어떤 공시·시세도 인용하지 않았다. '
         '실제 스냅숏은 앱을 빌드할 때 공개 자료로 만든다(plan/v4-stocks.md §5-4). 사용자 데이터가 아니고 백업에 들어가지 않는다.',
    'asOf': ASOF, 'currency': 'KRW', 'count': 8,
    'thresholdsDefault': {'growth': {'revenueCagr3y': 10, 'opIncomeCagr3y': 15, 'steadyYears': 3},
                          'value': {'pbrMax': 1.0, 'roeMin': 10, 'perMax': 10, 'reboundFromLow': 20, 'opMarginMin': 15},
                          'dividend': {'yieldMin': 3, 'streakMin': 5, 'payoutRange': [20, 70]}},
    'fields': ['code', 'name', 'market', 'close', 'high52', 'low52', 'marketCap', 'netAssets', 'revenue4y', 'opIncome4y',
               'netIncome', 'roe', 'per', 'pbr', 'dps', 'dividendStreak', 'payoutRatio', 'themes'],
    'items': [
        {'code': '005930', 'name': '삼성전자', 'market': 'KOSPI', 'close': 71200, 'high52': 88800, 'low52': 52100,
         'marketCap': 425.0e12, 'netAssets': 380.0e12, 'revenue4y': [211.0e12, 232.0e12, 268.0e12, 300.9e12],
         'opIncome4y': [19.8e12, 23.9e12, 27.6e12, 32.7e12], 'netIncome': 26.1e12, 'roe': 8.9, 'per': 16.3, 'pbr': 1.12,
         'dps': 1444, 'dividendStreak': 8, 'payoutRatio': 32, 'themes': ['반도체', 'AI']},
        {'code': '000660', 'name': 'SK하이닉스', 'market': 'KOSPI', 'close': 182500, 'high52': 214000, 'low52': 118000,
         'marketCap': 132.0e12, 'netAssets': 72.0e12, 'revenue4y': [26.1e12, 33.4e12, 42.0e12, 49.8e12],
         'opIncome4y': [3.1e12, 5.9e12, 9.7e12, 13.4e12], 'netIncome': 9.9e12, 'roe': 14.2, 'per': 13.3, 'pbr': 1.83,
         'dps': 1200, 'dividendStreak': 5, 'payoutRatio': 9, 'themes': ['반도체', 'AI']},
        {'code': '003230', 'name': '삼양식품', 'market': 'KOSPI', 'close': 1020000, 'high52': 1150000, 'low52': 610000,
         'marketCap': 7.7e12, 'netAssets': 1.1e12, 'revenue4y': [0.91e12, 1.19e12, 1.73e12, 2.10e12],
         'opIncome4y': [0.09e12, 0.15e12, 0.34e12, 0.47e12], 'netIncome': 0.36e12, 'roe': 33.0, 'per': 21.4, 'pbr': 7.0,
         'dps': 4000, 'dividendStreak': 6, 'payoutRatio': 8, 'themes': ['식품']},
        {'code': '196170', 'name': '알테오젠', 'market': 'KOSDAQ', 'close': 312000, 'high52': 452000, 'low52': 198000,
         'marketCap': 16.6e12, 'netAssets': 0.6e12, 'revenue4y': [0.04e12, 0.09e12, 0.10e12, 0.21e12],
         'opIncome4y': [-0.01e12, 0.02e12, 0.01e12, 0.08e12], 'netIncome': 0.07e12, 'roe': 12.1, 'per': 237, 'pbr': 27.7,
         'dps': 0, 'dividendStreak': 0, 'payoutRatio': None, 'themes': ['바이오']},
        {'code': '058470', 'name': '리노공업', 'market': 'KOSDAQ', 'close': 198000, 'high52': 226000, 'low52': 152000,
         'marketCap': 3.0e12, 'netAssets': 0.55e12, 'revenue4y': [0.28e12, 0.26e12, 0.27e12, 0.31e12],
         'opIncome4y': [0.11e12, 0.12e12, 0.13e12, 0.14e12], 'netIncome': 0.12e12, 'roe': 22.0, 'per': 25.0, 'pbr': 5.5,
         'dps': 3000, 'dividendStreak': 10, 'payoutRatio': 38, 'themes': ['반도체']},
        {'code': '277810', 'name': '레인보우로보틱스', 'market': 'KOSDAQ', 'close': 148000, 'high52': 205000, 'low52': 96000,
         'marketCap': 2.9e12, 'netAssets': 0.2e12, 'revenue4y': [None, None, 0.015e12, 0.02e12],
         'opIncome4y': [None, None, -0.001e12, 0.001e12], 'netIncome': 0.001e12, 'roe': 0.5, 'per': None, 'pbr': 14.5,
         'dps': 0, 'dividendStreak': 0, 'payoutRatio': None, 'themes': ['로봇', 'AI']},
        {'code': '033780', 'name': 'KT&G', 'market': 'KOSPI', 'close': 118500, 'high52': 126000, 'low52': 84000,
         'marketCap': 14.5e12, 'netAssets': 9.2e12, 'revenue4y': [5.2e12, 5.6e12, 5.8e12, 5.9e12],
         'opIncome4y': [1.3e12, 1.2e12, 1.2e12, 1.25e12], 'netIncome': 0.95e12, 'roe': 10.3, 'per': 15.3, 'pbr': 1.58,
         'dps': 6000, 'dividendStreak': 12, 'payoutRatio': 64, 'themes': ['소비재']},
        {'code': '088980', 'name': '맥쿼리인프라', 'market': 'KOSPI', 'close': 12850, 'high52': 13900, 'low52': 11200,
         'marketCap': 6.4e12, 'netAssets': 5.9e12, 'revenue4y': [0.30e12, 0.33e12, 0.36e12, 0.38e12],
         'opIncome4y': [0.25e12, 0.27e12, 0.29e12, 0.31e12], 'netIncome': 0.29e12, 'roe': 4.9, 'per': 22.1, 'pbr': 1.08,
         'dps': 720, 'dividendStreak': 18, 'payoutRatio': None, 'themes': ['인프라', '유틸리티']},
    ],
}
(OUT.parent / 'stocks-snapshot.sample.json').write_text(json.dumps(snap, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print('wrote stocks-snapshot.sample.json')


# ══════════════ 5단계 · 설정 › 주식 · 스냅숏 갱신 ══════════════
def group(label, inner, meta=None):
    m = f'<span style="font-size: 11.5px; color: {C["INK3"]};">{meta}</span>' if meta else ''
    return (f'<div><div style="display: flex; align-items: baseline; justify-content: space-between; gap: 8px; margin-bottom: 9px;">'
            f'<span style="font-size: 11px; font-weight: 600; letter-spacing: 0.07em; color: {C["INK3"]};">{label}</span>{m}</div>{inner}</div>')


def foldrow(label, meta=None, open_=False):
    m = f'<span style="font-size: 12px; color: {C["INK3"]};">{meta}</span>' if meta else ''
    return (f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px; height: 48px; '
            f'padding: 0 13px; border-radius: 12px; background: {C["INSET"]};">'
            f'<span style="font-size: 13.5px; font-weight: 600; color: {C["INK"]};">{label}</span>'
            f'<div style="display: flex; align-items: center; gap: 8px;">{m}{icon("up" if open_ else "down", 16, C["INK4"], 2)}</div></div>')


def thr_row(word, rule, val, last=False):
    bt = '' if last else f'border-bottom: 1px solid {C["LINE_ROW"]};'
    stepper = (f'<div style="display: flex; align-items: center; height: 32px; border: 1px solid {C["INPUT"]}; border-radius: 9px; overflow: hidden; flex-shrink: 0;">'
               f'<span style="width: 30px; height: 100%; display: flex; align-items: center; justify-content: center; color: {C["INK2"]}; font-size: 15px;">−</span>'
               f'<span style="min-width: 72px; padding: 0 6px; white-space: nowrap; text-align: center; font-size: 13.5px; font-weight: 600; color: {C["INK"]}; border-left: 1px solid {C["INPUT"]}; border-right: 1px solid {C["INPUT"]}; height: 100%; display: flex; align-items: center; justify-content: center;">{val}</span>'
               f'<span style="width: 30px; height: 100%; display: flex; align-items: center; justify-content: center; color: {C["INK2"]}; font-size: 15px;">+</span></div>')
    return (f'<div style="display: flex; align-items: center; gap: 10px; padding: 9px 0; {bt}">'
            f'<div style="display: flex; flex-direction: column; gap: 1px; flex: 1; min-width: 0;">'
            f'<span style="font-size: 13.5px; font-weight: 600; color: {C["INK"]};">{word}</span>'
            f'<span style="font-size: 11.5px; color: {C["INK3"]};">{rule}</span></div>{stepper}</div>')


growth_open = (f'<div style="padding: 0 13px 4px; background: {C["INSET"]}; border-radius: 0 0 12px 12px; margin-top: -8px; padding-top: 4px;">'
               + thr_row('매출 성장', '매출 3년 연평균 증가율', '10% 이상')
               + thr_row('이익 성장 속도', '영업이익 3년 연평균 증가율', '15% 이상')
               + thr_row('꾸준한 이익 증가', '최근 3년 중 영업이익이 늘어난 해', '3년 중 3년', last=True) + '</div>')
def sbtn(label, kind="soft", ic=None, h=30):
    """좁은 자리에서 글자가 세로로 쪼개지지 않는 작은 버튼."""
    return smallbtn(label, kind, ic, h).replace('font-weight: 600;">', 'font-weight: 600;' + NW + '">', 1)


# '스냅숏 · 갱신'은 내부 용어라 화면에서는 '종목 데이터 · 새로 받기'로 쓴다.
DATA_LABEL = '종목 데이터'
data_card = (
    f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 10px; padding: 12px 13px; background: {C["INSET"]}; border-radius: 14px;">'
    f'<div style="display: flex; flex-direction: column; gap: 2px; flex: 1; min-width: 0;"><span style="font-size: 13.5px; font-weight: 600; color: {C["INK"]};">{ASOF_S} 종가 기준 · 2,614종목</span>'
    f'<span style="font-size: 11.5px; line-height: 1.45; color: {C["INK3"]};">못 받아도 지금 데이터로 쓸 수 있어요.</span></div>{sbtn("새로 받기", "soft", "refresh", h=32)}</div>')
THR_META = '숫자는 여기서만 바꿀 수 있어요'
settings_html = sheet(
    '주식', '기준값은 처음에 넣어 둔 값일 뿐이에요. 바꿔도 앱이 좋다 나쁘다를 말하지 않아요.',
    group(DATA_LABEL, data_card) +
    group('기준값', foldrow('성장주', '3개 · 기본값', open_=True) + growth_open
          + f'<div style="margin-top: 8px;">{foldrow("저평가주", "4개 · 기본값")}</div>'
          + f'<div style="margin-top: 8px;">{foldrow("배당주", "3개 · 하나 바꿈")}</div>', THR_META) +
    group('기능', f'{btn("주식 기능 끄기", "danger", h=44)}'
                  f'<p style="margin: 7px 0 0; font-size: 11.5px; line-height: 1.5; color: {C["INK3"]};">탭 · 홈 카드 · 설정 항목이 사라지고 보유 · 관심 종목은 남아요.</p>'),
    sheet_footer('취소', '저장'))
w('StockSettings', settings_html, keep_all=True)


def upd_card(title, body, ic, icol, ibg, right=''):
    return card(
        f'<div style="display: flex; gap: 12px; align-items: flex-start;">'
        f'<div style="width: 34px; height: 34px; border-radius: 11px; background: {ibg}; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">{icon(ic, 18, icol, 2)}</div>'
        f'<div style="display: flex; flex-direction: column; gap: 3px; flex: 1; min-width: 0;">'
        f'<span style="font-size: 14.5px; font-weight: 600; letter-spacing: -0.015em; color: {C["INK"]};">{title}</span>'
        f'<span style="font-size: 12.5px; line-height: 1.45; color: {C["INK2"]};">{body}</span>{right}</div></div>')


# 새로 받기 순서 (5단계) — 왼쪽은 주식 설정 시트 조각(누르기 전), 오른쪽 ①②③은 같은 '종목 데이터' 자리에서 바뀌는 모습.
def data_panel(inner):
    return (f'<div style="background: {C["SURF"]}; border: 1px solid {C["LINE"]}; border-radius: 18px; padding: 12px;">'
            f'<div style="font-size: 11px; font-weight: 600; letter-spacing: 0.07em; color: {C["INK3"]}; padding: 0 2px 9px;">{DATA_LABEL}</div>{inner}</div>')


# 시트 머리(손잡이 · 제목 · 닫기)는 StockSettings 와 1px 도 다르지 않게 그 장에서 잘라 쓴다.
_sheet_top = s1.cut(settings_html, '<div style="display: flex; justify-content: center; padding: 9px 0 0; flex-shrink: 0;">',
                    '<div style="flex: 1; min-height: 0; overflow: hidden; padding: 14px 18px')
sheet_frag = (
    f'<div style="border-radius: 22px; overflow: hidden; background: #2A3245;">'
    f'<div style="height: 40px; display: flex; align-items: flex-end; justify-content: center; padding-bottom: 10px;">'
    f'<span style="font-size: 11.5px; font-weight: 500; color: rgba(255,255,255,.62);">배경을 눌러 닫기</span></div>'
    f'<div style="background: {C["SURF"]}; border-radius: 26px 26px 0 0; color: {C["INK"]};">{_sheet_top}'
    f'<div style="padding: 14px 18px 18px; display: flex; flex-direction: column; gap: 15px;">'
    + group(DATA_LABEL, marked(1, data_card))
    + group('기준값', foldrow('성장주', '3개 · 기본값') + f'<div style="margin-top: 8px;">{foldrow("저평가주", "4개 · 기본값")}</div>', THR_META)
    + '</div></div></div>')
# 설정 안의 동작은 결과를 시트 안에 보여 주고(③) 설정을 닫은 뒤에는 아래 알림을 띄우지 않는다(D10 · tasks-10) — 예전 ④ 알림은 뺐다.
update_left = cap('시작 · 설정 › 주식에서 「새로 받기」를 누르면') + sheet_frag
update_cells = [
    spec_cell(1, '물어보기', '왼쪽 1번 카드가 그 자리에서 이렇게 바뀌어요. 새 창은 뜨지 않아요.', data_panel(
        upd_card('종목 데이터를 새로 받을까요?', f'파일 하나(수백 KB)를 한 번 받아서 <span style="white-space: nowrap;">{ASOF_L}</span> 기준 데이터를 새것으로 바꿔요.', 'file', C["BRAND"], C["BRAND_SOFT"],
                 f'<div style="display: flex; gap: 8px; margin-top: 10px;">{sbtn("취소", "secondary", h=34)}{sbtn("받기", "primary", "download", h=34)}</div>'))),
    spec_cell(2, '받는 중', '얼마나 받았는지 막대와 숫자로 보여줘요.', data_panel(
        upd_card('받는 중 · 312 / 640 KB', '받는 동안에도 지금 데이터로 그대로 쓸 수 있어요.', 'loader', C["INK3"], C["INSET"],
                 f'<div style="margin-top: 10px;">{bar(48.75, C["BRAND"], 6)}</div>'))),
    spec_cell(3, '다 받았을 때', '새 기준일과 종목 수를 알려줘요. 내가 적은 것은 바뀌지 않아요.', data_panel(
        upd_card(f'다 받았어요 · 기준일 {NEXT_L}', f'2,631종목 · 가격 옆 날짜가 모두 {NEXT_S}로 바뀌어요. 내 보유·관심 종목과 기준값은 그대로예요. 설정 시트 안에 이렇게 남아요.', 'check', C["POS"], C["POS_SOFT"]))),
    spec_cell(3, '못 받았을 때', '인터넷이 끊겼거나 파일이 없을 때. 지금 데이터는 그대로 남아요.', data_panel(
        upd_card('받지 못했어요', f'인터넷이 끊겼거나 파일을 찾지 못했어요. <span style="white-space: nowrap;">{ASOF_L}</span> 기준 데이터를 그대로 쓰고, 아무것도 지워지지 않았어요.', 'warn', C["NEG"], C["NEG_SOFT"],
                 f'<div style="display: flex; gap: 8px; margin-top: 10px;">{sbtn("나중에", "secondary", h=34)}{sbtn("다시 시도", "soft", "refresh", h=34)}</div>'))),
]
w('SnapshotUpdate', spec_frame(
    1180, 750, '종목 데이터 새로 받기 · 순서대로',
    '설정 › 주식에서 「새로 받기」를 누르면 이 순서로 바뀌어요. 받다가 실패해도 지금 데이터로 그대로 쓸 수 있어요.',
    spec_cols(update_left, update_cells,
              f'어느 단계에서도 실시간 시세는 받지 않아요. 받는 것은 {strong("기준일 종가가 담긴 파일")} 하나뿐이고, 가격 옆에는 늘 기준일을 함께 보여줘요.')),
  keep_all=True)
