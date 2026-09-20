# -*- coding: utf-8 -*-
"""v4 · 2~5단계 아트보드 — 내비 재편 · 주식탭 뼈대 · 카테고리 탐색 · 갱신·기준값 설정.

plan/v4-stocks.md §4·§5·§7. 1단계와 같은 방식(라이트를 만들고 darken()으로 다크 짝)이고,
`import gen_v4`가 1단계 5장도 함께 다시 쓴다(멱등). 목적지 탭의 본문은 Goals.dc.html·Future.dc.html에서
그대로 잘라 쓴다 — 내비만 바뀌고 화면은 v3 그대로라는 것이 2단계의 요점이기 때문.

    python3 gen_v4_stocks.py          # 16 + 16장 → ../ , 스냅숏 샘플 → ../../stocks-snapshot.sample.json
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
ASOF = '2026-09-04'
ASOF_S = '9/4'
NEXT_ASOF = '2026-09-11'
NEXT_S = '9/11'
CAPACITY = 27                           # 이번 달 저축·투자 여력(만원) = 총수입 390 − 소비 예상 208 − 저축 이체 63 − 대출상환 92
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
    (OUT / f'Dark{name}.dc.html').write_text(darken(light), encoding='utf-8')
    print('wrote', name, '+ Dark' + name)


# ══════════════ 새 바텀 내비 (계획 §4 권장안) ══════════════
NAV_ON = [("home", "홈"), ("wallet", "자산"), ("card", "소비"), ("candle", "주식"), ("flag", "목적지")]
NAV_OFF = [("home", "홈"), ("wallet", "자산"), ("card", "소비"), ("flag", "목적지")]


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
    return badge(f'{ASOF_S} 종가', 'mute')


def back_header(title, sub=None, right=''):
    s = f'<span style="font-size: 12px; font-weight: 500; color: {C["INK3"]};">{sub}</span>' if sub else ''
    return (f'<div style="display: flex; align-items: center; gap: 6px; padding: 12px 12px 12px; flex-shrink: 0;">'
            f'<div style="width: 36px; height: 36px; border-radius: 11px; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">{icon("left", 20, C["INK2"], 2)}</div>'
            f'<div style="display: flex; align-items: baseline; gap: 8px; flex: 1; min-width: 0;">'
            f'<h1 style="margin: 0; font-size: 19px; font-weight: 700; letter-spacing: -0.03em; line-height: 1.2; color: {C["INK"]}; white-space: nowrap;">{title}</h1>{s}</div>{right}</div>')


def capacity_band():
    """투자 여력 띠 — sample-data 의 month.leftover(27만원)를 그대로 가져온다. 새 계산 없음.
    증가분이 아니라 금액이라 '+'를 붙이지 않는다."""
    return (f'<div style="display: flex; align-items: center; gap: 10px; padding: 10px 14px; background: {C["BRAND_SOFT"]}; border-radius: 14px; flex-shrink: 0;">'
            f'{icon("arrowu", 16, C["BRAND"], 2.2)}'
            f'<div style="display: flex; flex-direction: column; gap: 1px; flex: 1; min-width: 0;">'
            f'<span style="font-size: 12px; font-weight: 500; color: {C["BRAND_BANNER"]};">이번 달 저축·투자 여력</span>'
            f'<span style="font-size: 11px; color: {C["BRAND_BANNER"]};">총수입 390만원 − 소비 예상·저축·상환</span></div>'
            f'<span style="font-size: 17px; font-weight: 700; letter-spacing: -0.02em; color: {C["BRAND"]};{NW}">{CAPACITY}<span style="font-size: 12.5px; font-weight: 600;">만원</span></span></div>')


def guardrail(text, link='목적지 보기'):
    """가드레일 한 줄 — 막지 않고 말만 한다."""
    return (f'<div style="display: flex; align-items: center; gap: 8px; padding: 9px 12px; background: {C["WARN_SOFT"]}; border-radius: 12px; flex-shrink: 0;">'
            f'{icon("flag", 14, C["WARN"], 2)}'
            f'<span style="flex: 1; min-width: 0; font-size: 12px; line-height: 1.4; color: {C["WARN_INK"]};">{text}</span>'
            f'<span style="font-size: 12px; font-weight: 600; color: {C["WARN"]}; white-space: nowrap;">{link} &rsaquo;</span></div>')


GUARD_EMERGENCY = '비상금이 68%예요. 투자보다 비상금을 먼저 채우는 걸 권해요.'


def asof_footer(extra=''):
    return (f'<p style="margin: 2px 2px 0; font-size: 11px; line-height: 1.5; color: {C["INK3"]};">'
            f'데이터 기준일 {ASOF} 종가 · 설정에서 새로 받기{extra}<br>기준에 맞는 종목을 보여주는 것이지 투자 권유가 아니에요.</p>')


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


# 세그먼트에서 '새 목적지 설계'가 빠졌으므로 목록 끝 점선 버튼이 그 화면으로 가는 길이다 — 문구를 바꾸고 오른쪽 화살표를 붙인다.
goals_content = content_of('Goals')
ADD_OLD = '</svg>\n      목적지 추가\n    </div>'
assert goals_content.count(ADD_OLD) == 1
goals_content = goals_content.replace(
    ADD_OLD, '</svg>\n      <span style="white-space: nowrap; flex-shrink: 0;">새 목적지 설계</span>\n      '
    + icon("right", 16, C["BRAND"], 2) + '\n    </div>')
w('DestGoals', frame(dest_header(0) + '\n' + goals_content + '\n' + nav_v4(4)))
w('DestFuture', frame(dest_header(1) + '\n' + content_of('Future') + '\n' + nav_v4(4)))
# 상환 계획 — Payoff 본문(가정 카드 보라 점선 · 저장 띠 포함)을 그대로, 머리와 내비만 새 것.
payoff_content = content_of('Payoff')
assert '저장되지 않는 가정' in payoff_content and 'dashed' in payoff_content
# Payoff 원본이 keep_all=True 로 쓰이므로(gen_screens) 여기도 같게 — 안내문이 낱말 중간에서 꺾이지 않는다.
w('DestPayoff', frame(dest_header(2) + '\n' + payoff_content + '\n' + nav_v4(4)), keep_all=True)

# 주식 꺼짐 = 4탭. 홈은 1단계 '구성 반영' 그대로, 내비만 다르다.
hc = (OUT / 'HomeConfigured.dc.html').read_text(encoding='utf-8')
hc_body = s1.cut(hc, '<div style="width: 390px; height: 844px;', M_NAV)
hc_inner = hc_body[hc_body.index('>') + 1:]
# 달력이 들어오면서 홈이 844 를 넘는다. 위에서부터 그리면 이 장이 보여 주려는 아래 카드(한도 · 순자산 · 상환 계획)가 잘리므로
# HomeCalendar 처럼 '아래로 스크롤한 상태'로 그린다 — 머리는 밀려 올라가고, 본문은 아래 맞춤(flex-end)이라 넘치는 만큼 히어로 윗단이 잘린다.
HC_CONTENT = '<div style="flex: 1; min-height: 0; display: flex; flex-direction: column; gap: 8px; padding: 0 14px; overflow: hidden;">'
# 아래 패딩 27px(허용 20~35) — 절단선이 히어로 큰 숫자 줄(57.9% · 여유)과 그다음 줄 사이의 빈 띠에 와서, 프레임 맨 위에 글자 아랫부분이 남지 않는다.
# 12px 이면 절단선이 54px 숫자 줄을 지나 글자 밑동 약 8px 이 남는다. 본문 높이가 바뀌면 이 값을 다시 잰다.
assert HC_CONTENT.count('padding: 0 14px;') == 1
HOME_SCROLLED = HC_CONTENT.replace('padding: 0 14px;', 'justify-content: flex-end; padding: 0 14px 27px;')
assert hc_inner.count(HC_CONTENT) == 1 and '이번 달 달력' in hc_inner
hc_scrolled = '\n  ' + hc_inner[hc_inner.index(HC_CONTENT):].replace(HC_CONTENT, HOME_SCROLLED)
w('HomeStocksOff', frame(hc_scrolled + nav_v4(0, stocks=False)))


# ══════════════ 3단계 · 주식탭 뼈대 (사용자 입력만) ══════════════
def mine_content(empty=False):
    if empty:
        empty_card = card(
            f'<div style="display: flex; flex-direction: column; align-items: center; text-align: center; padding: 22px 8px 18px;">'
            f'<div style="width: 52px; height: 52px; border-radius: 16px; background: {C["INSET"]}; display: flex; align-items: center; justify-content: center;">{icon("candle", 24, C["INK3"], 1.8)}</div>'
            f'<span style="margin-top: 14px; font-size: 16px; font-weight: 700; letter-spacing: -0.02em; color: {C["INK"]};">아직 기록한 종목이 없어요</span>'
            f'<span style="margin-top: 6px; font-size: 12.5px; line-height: 1.5; color: {C["INK2"]};">보유 종목은 수량과 평단을, 관심 종목은 이름만 적으면 돼요.<br>종가는 직접 넣고, 비워 두면 —로 남아요.</span>'
            f'<div style="display: flex; gap: 8px; width: 100%; margin-top: 18px;">'
            f'{btn("보유 기록", "primary", "plus", h=46).replace("width: 100%;", "flex: 1;")}'
            f'{btn("관심 추가", "secondary", "star", h=46).replace("width: 100%;", "flex: 1;")}</div></div>', pad='4px 14px')
        quiet = card(
            f'<span style="font-size: 11px; font-weight: 600; letter-spacing: 0.07em; color: {C["INK3"]};">이 화면에 없는 것</span>'
            f'<p style="margin: 6px 0 0; font-size: 12.5px; line-height: 1.55; color: {C["INK2"]};">실시간 시세 · 주문 · 호가 · 뉴스 · 커뮤니티 · 시세 알림은 없어요.<br>'
            f'내 기록을 정리해 보는 화면이라, 주문은 쓰시는 증권 앱에서 하시면 돼요.</p>')
        return content([capacity_band(), empty_card, quiet])

    hold_rows = ''.join(
        stock_row(n, m, price_col(q * p, f'{q}주 · 평단 {won(a)}'), f'{ASOF_S} 종가 {won(p)}', last=(i == len(HOLD) - 1), pad='9px 0')
        for i, (n, m, q, a, p, acc) in enumerate(HOLD))
    hold_card = card(
        # '직접 입력' · 계좌 이름은 행마다 되풀이하지 않고 머리말 · 합계 행에 한 번만 쓴다.
        section_head('보유', f'{len(HOLD)}종목 · 종가는 직접 넣은 값이에요', link('보유 기록'))
        .replace(f'font-size: 12px; color: {C["INK3"]};">', f'font-size: 12px; color: {C["INK3"]}; white-space: nowrap;">', 1)
        .replace(f'font-weight: 600; color: {C["BRAND"]};">', f'font-weight: 600; color: {C["BRAND"]};{NW}">', 1)
        + f'<div style="margin-top: 2px;">{hold_rows}</div>'
        + f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px; padding: 10px 0 4px; border-top: 1px solid {C["LINE_SOFT"]};">'
        f'<div style="display: flex; flex-direction: column; gap: 1px;"><span style="font-size: 12.5px; font-weight: 600; color: {C["INK"]};">평가액 합계</span>'
        f'<span style="font-size: 11px; color: {C["INK3"]};">{HOLD[0][5]} · 매입 대비 +36만원 · {ASOF_S} 종가 기준</span></div>'
        f'<span style="font-size: 17px; font-weight: 700; letter-spacing: -0.02em; color: {C["INK"]};">1,244<span style="font-size: 12.5px; font-weight: 600; color: {C["INK2"]};">만원</span></span></div>'
        + f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px; padding: 8px 0 2px;">'
        f'<div style="display: flex; flex-direction: column; gap: 1px;"><span style="font-size: 12.5px; font-weight: 500; color: {C["INK2"]};">ETF 계좌 평가액에 반영</span>'
        f'<span style="font-size: 11px; color: {C["INK3"]};">꺼 두면 자산·순자산은 계좌에 적은 4,890만원 그대로예요</span></div>{toggle(False)}</div>',
        pad='12px 14px 8px')
    watch_rows = ''.join(
        stock_row(n, m, price_col(p, f'{ASOF_S} 직접 입력' if p else '종가 미입력'), memo or '&nbsp;', last=(i == len(WATCH) - 1), pad='6px 0')
        for i, (n, m, p, memo) in enumerate(WATCH))
    watch_card = card(section_head('관심', f'{len(WATCH)}종목', link('관심 추가')) + f'<div style="margin-top: 2px;">{watch_rows}</div>', pad='12px 14px 6px')
    return content([capacity_band(), hold_card, watch_card])


w('StocksMine', frame(screen_header('주식', '보유 3 · 관심 5', trailing=topicons()) + mine_content() + nav_v4(3)), keep_all=True)
w('StocksEmpty', frame(screen_header('주식', '아직 기록 없음', trailing=topicons()) + mine_content(empty=True) + nav_v4(3)), keep_all=True)

# 모달 · 보유 기록
w('HoldingAdd', sheet(
    '보유 기록', '수량과 평단만 적으면 저장돼요.<br>종가는 비워 두면 —로 남아요.',
    f'{solo(field("종목", "삼성전자 · 005930 · KOSPI", required=True))}'
    f'<div style="display: flex; gap: 10px;">{field("수량", "60", "주", required=True)}{field("평단", "68,400", "원", required=True)}</div>'
    f'<div style="display: flex; gap: 10px;">{field("종가", "71,200", "원", optional=True)}{field("기준일", ASOF, optional=True)}</div>'
    f'{note("종가는 직접 넣는 값이라 실시간 시세가 아니에요. 가격 옆에는 늘 이 기준일이 붙습니다.", "mute")}'
    f'{solo(select_field("연결 계좌", "ETF 계좌 · 4,890만원", optional=True))}'
    f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 10px; padding: 12px 13px; background: {C["INSET"]}; border-radius: 14px;">'
    f'<div style="display: flex; flex-direction: column; gap: 2px;"><span style="font-size: 13.5px; font-weight: 600; color: {C["INK"]};">계좌 평가액에 반영</span>'
    f'<span style="font-size: 11.5px; line-height: 1.45; color: {C["INK3"]};">켜면 수량 × 종가가 ETF 계좌 평가액에 더해져<br>자산·순자산·미래 경로에 반영돼요. 기본은 꺼짐이에요.</span></div>{toggle(False)}</div>',
    sheet_footer('취소', '저장'), body_pb=14), keep_all=True)

# 홈 · 주식 요약 카드 (구성에서 주식을 켠 사용자)
stock_summary_card = card(
    f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 10px; height: 46px;">'
    f'<div style="display: flex; flex-direction: column; gap: 2px; min-width: 0;">'
    f'<span style="font-size: 13.5px; font-weight: 600; color: {C["INK"]};">주식 요약</span>'
    f'<span style="font-size: 11.5px; color: {C["INK3"]}; white-space: nowrap;">보유 3 · 관심 5 · {ASOF_S} 종가 · 직접 입력</span></div>'
    f'<div style="display: flex; align-items: center; gap: 8px; flex-shrink: 0;">'
    f'<span style="font-size: 15px; font-weight: 600; letter-spacing: -0.02em; color: {C["INK"]};">1,244만원</span>'
    f'{icon("right", 16, C["INK4"], 2)}</div></div>', pad='4px 14px')
# v4-3 은 v5-3 뒤라 한도 라벨이 '앞으로 하루 …'(gen_v5 home_expanded 와 같은 치환 · 첫 줄은 한 줄 고정).
LIM_LEFT = '<span style="font-size: 13.5px; font-weight: 600; color: #101828;">이번 달 한도 '
assert s1.limit_block.count(LIM_LEFT) == 1 and s1.limit_block.count('하루 47,270원') == 1
limit_v53 = (s1.limit_block.replace(LIM_LEFT, LIM_LEFT.replace('color: #101828;', 'color: #101828; white-space: nowrap;'))
             .replace('하루 47,270원', '앞으로 하루 47,270원'))
w('HomeStocksCard', frame(
    f'\n  {HOME_SCROLLED}\n\n'
    f'    {s1.hero_block}\n\n    {s1.calendar_block}\n\n    {s1.guide_block}\n\n    {stock_summary_card}\n\n    {limit_v53}\n\n    {s1.networth_card}\n\n  </div>\n\n'
    f'  {nav_v4(0)}\n'), keep_all=True)


# ══════════════ 4단계 · 카테고리 탐색 (내장 스냅숏) ══════════════
# 스냅숏 표본. 이름은 실재 종목이지만 수치는 전부 디자인 검증용 가상값이다 (샘플 JSON의 _ 참고).
GROWTH = [  # (이름, 시장, 종가, 이유 한 줄, 충족, 분모)
    ('삼성전자', 'KOSPI', 71200, '영업이익 3년간 연 18% 증가', 3, 3),
    ('SK하이닉스', 'KOSPI', 182500, '매출 3년간 연 24% 증가', 3, 3),
    ('삼양식품', 'KOSPI', 1020000, '매출 3년간 연 32% 증가', 3, 3),
    ('알테오젠', 'KOSDAQ', 312000, '영업이익 3년간 연 41% 증가 · 3년 중 2년만 증가', 2, 3),
    ('리노공업', 'KOSDAQ', 198000, '3년 내내 이익 증가 · 매출 성장은 연 8%', 2, 3),
    ('레인보우로보틱스', 'KOSDAQ', 148000, '매출 연 33% 증가 · 이익 기록 2년뿐', 1, 1),
]
DIVIDEND = [
    ('KT&amp;G', 'KOSPI', 118500, '배당수익률 5.1% · 12년 연속', 3, 3),
    ('하나금융지주', 'KOSPI', 68900, '배당수익률 4.8% · 9년 연속', 3, 3),
    ('삼성화재', 'KOSPI', 372000, '배당수익률 3.9% · 배당성향 44%', 3, 3),
    ('맥쿼리인프라', 'KOSPI', 12850, '배당수익률 5.6% · 배당성향 —', 2, 2),
    ('현대차', 'KOSPI', 242000, '배당수익률 4.2% · 3년 연속', 2, 3),
    ('신한지주', 'KOSPI', 61400, '배당수익률 3.4% · 배당성향 26%', 3, 3),
]


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
    return frame(
        back_header(title, sub, asof_badge())
        + content([f'<div style="display: flex; flex-direction: column; gap: 9px;">{chips}{sort_row(count)}</div>',
                   card(list_rows(rows) + more_row(count - len(rows)), pad='2px 14px 0'),
                   asof_footer()], gap=10))


w('StockListGrowth', list_screen('성장주', '기준 3개',
                                 crit_chips(['매출 성장', '이익 성장 속도', '꾸준한 이익 증가']), GROWTH, 12), keep_all=True)
w('StockListDividend', list_screen('배당주', '기준 3개',
                                   crit_chips(['높은 배당수익률', '연속 배당', '무리 없는 배당'], (True, True, False)), DIVIDEND, 27), keep_all=True)


# 주식 홈 (S1)
def cat_card(ic, name, count, chips, col):
    ch = ''.join(f'<span style="font-size: 11px; font-weight: 500; color: {C["INK2"]}; background: {C["INSET"]}; border-radius: 99px; padding: 3px 8px; white-space: nowrap;">{c}</span>' for c in chips)
    return (f'<div style="background: {C["SURF"]}; border: 1px solid {C["LINE"]}; border-radius: 18px; padding: 13px 13px 12px; display: flex; flex-direction: column; gap: 9px; min-width: 0;">'
            f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 6px;">'
            f'<div style="width: 30px; height: 30px; border-radius: 10px; background: {col}18; display: flex; align-items: center; justify-content: center;">{icon(ic, 16, col, 2)}</div>'
            f'{icon("right", 15, C["INK4"], 2)}</div>'
            f'<div style="display: flex; flex-direction: column; gap: 2px;"><span style="font-size: 15px; font-weight: 700; letter-spacing: -0.02em; color: {C["INK"]};">{name}</span>'
            f'<span style="font-size: 11.5px; color: {C["INK3"]};">{count}</span></div>'
            f'<div style="display: flex; flex-wrap: wrap; gap: 4px;">{ch}</div></div>')


cats = (f'<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 10px;">'
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
    screen_header('주식', f'기준일 {ASOF_S}', tabs=['둘러보기', '내 종목'], active=0)
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


base_m = months_to(5000, 2100, 28, 5.0)
sim_m = months_to(5000, 2100, 28 + 15, 5.0)
assert ym(base_m) == (2032, 6), ym(base_m)
SIM_Y, SIM_M = ym(sim_m)
AHEAD = base_m - sim_m
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
    f'<div style="margin-top: 4px;">{slider(75, C["VIO"])}</div>'
    # 결과는 두 행으로 — 한 줄에 네 덩어리를 넣으면 전부 두 줄로 꺾인다.
    f'<div style="margin-top: 8px; font-size: 12px; color: {C["INK3"]}; white-space: nowrap;">투자 계좌 5,000만원 도착</div>'
    f'<div style="display: flex; align-items: center; gap: 6px; margin-top: 5px; font-size: 13px; color: {C["INK2"]}; white-space: nowrap;">'
    f'<span style="font-weight: 500; color: {C["INK4"]}; text-decoration: line-through; flex-shrink: 0;">2032년 6월</span>{icon("arrowr", 13, C["VIO_STRONG"], 2.4)}'
    f'<span style="font-size: 14px; font-weight: 700; color: {C["VIO_STRONG"]}; flex-shrink: 0;">{SIM_Y}년 {SIM_M}월</span>'
    f'<span style="margin-left: auto; display: inline-flex; align-items: center; background: {C["VIO_SOFT"]}; color: {C["VIO_STRONG"]}; font-size: 11.5px; font-weight: 600; '
    f'border-radius: 99px; padding: 4px 9px; white-space: nowrap; flex-shrink: 0;">{AHEAD // 12}년 {AHEAD % 12}개월 빨라져요</span></div>'
    f'<p style="margin: 8px 0 0; font-size: 11px; line-height: 1.45; color: {C["INK3"]};">이번 달 여력 {CAPACITY}만원 안에서 넣어 본 가정이에요.<br>'
    f'수익률은 이 종목이 아니라 투자 계좌 목표의 연 5.0%로 봤어요.</p></div>')
detail_actions = (f'<div style="display: flex; gap: 8px; padding: 10px 14px 20px; background: {C["SURF"]}; border-top: 1px solid {C["LINE"]}; flex-shrink: 0;">'
                  f'{btn("관심 추가", "secondary", "star", h=48).replace("width: 100%;", "flex: 1;")}'
                  f'{btn("보유 기록", "primary", "plus", h=48).replace("width: 100%;", "flex: 1.3;")}</div>')
w('StockDetail', frame(
    back_header('삼성전자', '005930 · KOSPI')
    + content([price_card, reason_card, metrics_card, sim_card], gap=8).replace('padding: 0 14px;', 'padding: 0 14px 12px;', 1)
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
               theme_grid, asof_footer()], gap=10)
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
band_over = guardrail('이번 달 소비율이 63.2%예요. 목표 60%를 넘었어요.', '한도 보기')
row_short = card(list_rows([GROWTH[5]]), pad='2px 14px')
row_nodiv = card(list_rows([DIVIDEND[3]]), pad='2px 14px')
list_badges = (f'<div style="display: flex; align-items: center; gap: 6px; margin-top: 8px;">'
               + (badge("성장", "brand") + badge("배당", "pos")).replace('padding: 4px 9px;">', 'padding: 4px 9px;' + NW + '">') + '</div>')
detail_top = hero(price_head.replace('padding: 4px 9px;">', 'padding: 4px 9px;' + NW + '">') + list_badges, pad='12px 14')
home_head = screen_header('주식', f'기준일 {ASOF_S}', tabs=['둘러보기', '내 종목'], active=0).replace('padding: 14px 16px 12px;', 'padding: 14px 14px 12px;', 1)
home_frag = (f'<div style="{FRAG}">{home_head}<div style="display: flex; flex-direction: column; gap: 10px; padding: 0 14px 14px;">'
             f'{capacity_band()}{marked(1, band_emergency)}{mine_summary}</div></div>')
name_bar = (f'<div style="display: flex; align-items: baseline; gap: 8px; padding: 0 2px 8px;">'
            f'<span style="font-size: 19px; font-weight: 700; letter-spacing: -0.03em; line-height: 1.2; color: {C["INK"]}; white-space: nowrap;">삼성전자</span>'
            f'<span style="font-size: 12px; font-weight: 500; color: {C["INK3"]};">005930 · KOSPI</span></div>')
states_left = (cap('주식 홈 · 위쪽') + home_frag + SPACER
               + cap('종목 목록 · 한 줄') + marked(2, card(list_rows(GROWTH[:2]), pad='2px 14px')) + SPACER
               + cap('종목 상세 · 맨 위') + name_bar + marked(3, detail_top))
states_cells = [
    spec_cell(1, '비상금이 모자랄 때', '비상금을 다 채우기 전까지 주식 홈 위쪽에 보여요. 누르면 목적지로 가요.', band_emergency),
    spec_cell(1, '이번 달 소비가 목표를 넘었을 때', '소비율이 목표를 넘은 달에 보여요. 누르면 소비 한도로 가요.', band_over),
    spec_cell(1, '둘 다 괜찮을 때 — 띠가 나타나지 않아요', '띠 자리에 다른 안내를 넣지 않아요. 아래 카드가 그대로 올라와요.',
              f'<div style="display: flex; flex-direction: column; gap: 10px;">{capacity_band()}{mine_summary}</div>'),
    spec_cell(2, '상장한 지 얼마 안 돼 기록이 짧을 때', '자료가 없는 기준은 충족 수에서 빼고, 몇 개가 빠졌는지 배지 아래에 적어요. 0으로 세지 않아요.', row_short),
    spec_cell(2, '배당 기록이 없을 때', '배당성향을 알 수 없으면 —로 두고, 자료가 있는 기준 2개로만 세요.', row_nodiv),
    spec_cell(3, '한 종목이 두 목록에 있을 때', '흔한 일이라 경고 없이 배지로만 알려요. 배지는 줄이 바뀌어도 쪼개지지 않아요.', detail_top),
]
w('StockStates', spec_frame(
    1180, 880, '주식 탭 · 특수한 상황 6가지',
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
                  f'<p style="margin: 7px 0 0; font-size: 11.5px; line-height: 1.5; color: {C["INK3"]};">탭·홈 카드·설정 항목이 사라지고 보유·관심 기록은 남아요.</p>'),
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
toast = ('<!--dc-keep--><div style="display: flex; align-items: center; gap: 9px; padding: 11px 14px; background: #101828; border-radius: 14px; color: #FFFFFF; font-size: 13px; font-weight: 500;">'
         '<svg style="flex-shrink: 0;" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#3DD489" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg>'
         f'<span style="flex: 1; min-width: 0; line-height: 1.4;">{NEXT_S} 종가로 바꿨어요 · 내 종목 금액도 다시 계산했어요</span></div><!--/dc-keep-->')
update_left = (cap('시작 · 주식 설정에서 [새로 받기]를 누르면') + sheet_frag + '<div style="height: 22px;"></div>'
               + spec_cell(4, '시트를 닫은 뒤 알림', '다 받은 뒤 설정을 닫으면 화면 아래에 잠깐 떴다 사라져요.', toast))
update_cells = [
    spec_cell(1, '물어보기', '왼쪽 1번 카드가 그 자리에서 이렇게 바뀌어요. 새 창은 뜨지 않아요.', data_panel(
        upd_card('종목 데이터를 새로 받을까요?', f'파일 하나(수백 KB)를 한 번 받아서 {ASOF} 기준 데이터를 새것으로 바꿔요.', 'file', C["BRAND"], C["BRAND_SOFT"],
                 f'<div style="display: flex; gap: 8px; margin-top: 10px;">{sbtn("취소", "secondary", h=34)}{sbtn("받기", "primary", "download", h=34)}</div>'))),
    spec_cell(2, '받는 중', '얼마나 받았는지 막대와 숫자로 보여줘요.', data_panel(
        upd_card('받는 중 · 312 / 640 KB', '받는 동안에도 지금 데이터로 그대로 쓸 수 있어요.', 'loader', C["INK3"], C["INSET"],
                 f'<div style="margin-top: 10px;">{bar(48.75, C["BRAND"], 6)}</div>'))),
    spec_cell(3, '다 받았을 때', '새 기준일과 종목 수를 알려줘요. 내가 적은 것은 바뀌지 않아요.', data_panel(
        upd_card(f'다 받았어요 · 기준일 {NEXT_ASOF}', f'2,631종목 · 가격 옆 날짜가 모두 {NEXT_S}로 바뀌어요. 내 보유·관심 종목과 기준값은 그대로예요.', 'check', C["POS"], C["POS_SOFT"]))),
    spec_cell(3, '못 받았을 때', '인터넷이 끊겼거나 파일이 없을 때. 지금 데이터는 그대로 남아요.', data_panel(
        upd_card('받지 못했어요', f'인터넷이 끊겼거나 파일을 찾지 못했어요. <span style="white-space: nowrap;">{ASOF}</span> 기준 데이터를 그대로 쓰고, 아무것도 지워지지 않았어요.', 'warn', C["NEG"], C["NEG_SOFT"],
                 f'<div style="display: flex; gap: 8px; margin-top: 10px;">{sbtn("나중에", "secondary", h=34)}{sbtn("다시 시도", "soft", "refresh", h=34)}</div>'))),
]
w('SnapshotUpdate', spec_frame(
    1180, 762, '종목 데이터 새로 받기 · 순서대로',
    '주식 설정에서 [새로 받기]를 누르면 이 순서로 바뀌어요. 받다가 실패해도 지금 데이터로 그대로 쓸 수 있어요.',
    spec_cols(update_left, update_cells,
              f'어느 단계에서도 실시간 시세는 받지 않아요. 받는 것은 {strong("기준일 종가가 담긴 파일")} 하나뿐이고, 가격 옆에는 늘 기준일을 함께 보여줘요.')),
  keep_all=True)
