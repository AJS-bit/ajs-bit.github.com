# -*- coding: utf-8 -*-
"""남은 화면 4종: 적립 모달 · 목적지 유형 5종 · 소비 과거 달 · 코칭 기록 없음."""
import pathlib
from gen_common import *

OUT = pathlib.Path(__file__).resolve().parent.parent


BODY_CSS = '-webkit-font-smoothing: antialiased; }'


def w(name, body, keep_all=False):
    html = doc(body)
    if keep_all:
        # 설명 문장이 많은 참고 시트는 한국어 낱말이 중간에서 끊기지 않게 한다.
        assert html.count(BODY_CSS) == 1
        html = html.replace(BODY_CSS, BODY_CSS[:-1] + 'word-break: keep-all; }')
    (OUT / f'{name}.dc.html').write_text(html, encoding='utf-8')
    print('wrote', name)


def kv(k, v, vcol=None, h=40, last=False):
    return (f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px; min-height: {h}px; '
            f'{"" if last else "border-bottom: 1px solid " + C["LINE_ROW"] + ";"}">'
            f'<span style="font-size: 13px; color: {C["INK2"]};">{k}</span>'
            f'<span style="font-size: 13.5px; font-weight: 600; color: {vcol or C["INK"]};">{v}</span></div>')


def chip(text, active=False):
    if active:
        return (f'<span style="display: inline-flex; align-items: center; height: 34px; padding: 0 12px; border-radius: 10px; '
                f'background: {C["BRAND_SOFT"]}; border: 1.5px solid {C["BRAND"]}; color: {C["BRAND"]}; font-size: 13px; font-weight: 600;">{text}</span>')
    return (f'<span style="display: inline-flex; align-items: center; height: 34px; padding: 0 12px; border-radius: 10px; '
            f'background: {C["SURF"]}; border: 1px solid {C["BORDER"]}; color: {C["INK2"]}; font-size: 13px; font-weight: 500;">{text}</span>')


def delta(before, after, note, tone="pos"):
    col = C["POS"] if tone == "pos" else C["INK"]
    return (f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px; min-height: 38px;">'
            f'<span style="font-size: 12.5px; color: {C["INK2"]};">{note}</span>'
            f'<span style="display: inline-flex; align-items: center; gap: 6px; flex-shrink: 0;">'
            f'<span style="font-size: 13px; color: {C["INK4"]}; text-decoration: line-through;">{before}</span>'
            f'{icon("arrowr", 13, C["INK4"], 2.2)}'
            f'<span style="font-size: 14px; font-weight: 700; letter-spacing: -0.02em; color: {col};">{after}</span></span></div>')


# ══════════════════════════════════════════════════════════════
# 1 · 적립액 추가 모달
# ══════════════════════════════════════════════════════════════
w('GoalContribute', sheet(
    '비상금 6개월 적립액 추가',
    '이 목적지의 적립 기록만 갱신합니다.',
    card(
        f'<div style="display: flex; align-items: center; gap: 13px;">'
        f'{ring(68, C["BRAND"], 52)}'
        f'<div style="flex: 1; min-width: 0;">'
        f'<div style="font-size: 15px; font-weight: 700; letter-spacing: -0.02em; color: {C["INK"]};">비상금 6개월</div>'
        f'<div style="font-size: 12.5px; color: {C["INK3"]}; margin-top: 3px;">'
        f'<b style=font-weight:600>1,020</b> / 1,500만원 · 남은 480만원</div>'
        f'<div style="font-size: 11.5px; color: {C["INK4"]}; margin-top: 2px;">월 35만원 배분 · 도착 예상 2027년 11월</div>'
        f'</div></div>', pad='14px 15px') +

    '<div>' +
    field('추가 적립액', '50', unit='만원', required=True,
          helper='이번에 실제로 넣은 금액을 적어 주세요') +
    f'<div style="display: flex; gap: 7px; margin-top: 10px; flex-wrap: wrap;">'
    f'{chip("월 배분 35만원")}{chip("50만원", True)}{chip("남은 480만원")}</div>'
    '</div>' +

    card(
        eyebrow_row('저장하면 이렇게 바뀝니다',
                    f'<span style="font-size: 11px; color: {C["INK4"]};">월 배분 유지 기준</span>') +
        f'<div style="margin-top: 4px;">'
        f'{delta("1,020만원", "1,070만원", "적립액")}'
        f'{delta("68%", "71%", "진행률")}'
        f'{delta("2027년 11월", "2027년 10월", "도착 예상")}'
        f'</div>',
        pad='13px 15px') +

    note('이 기록은 <b style=font-weight:600>목적지의 적립액만</b> 바꿉니다. 통장 잔액이나 소비 거래에 '
         '중복 반영되지 않아요.', 'mute') +

    card(
        section_head('최근 적립', '12회 · 1,020만원', link('전체'))
        + '<div style="margin-top: 6px;">'
        + ''.join(
            f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px; min-height: 38px; '
            f'{"" if last else "border-bottom: 1px solid " + C["LINE_ROW"] + ";"}">'
            f'<span style="font-size: 12.5px; color: {C["INK2"]};">{d}</span>'
            f'<span style="display: inline-flex; align-items: center; gap: 9px;">'
            f'<span style="font-size: 13px; font-weight: 600; color: {C["INK"]};">{a}</span>'
            f'{icon("more", 15, C["INK4"], 2.2)}</span></div>'
            for d, a, last in [('8월 15일', '35만원', False), ('7월 15일', '35만원', True)])
        + '</div>', pad='13px 15px'),

    sheet_footer('취소', '적립액 추가')), keep_all=True)


# ══════════════════════════════════════════════════════════════
# 2 · 목적지 유형 5종
# ══════════════════════════════════════════════════════════════
def type_block(emoji, name, note_text, fields, calc, row_html, badge_html=''):
    return card(
        f'<div style="display: flex; align-items: flex-start; gap: 10px;">'
        f'<span style="font-size: 20px; line-height: 1; flex-shrink: 0; margin-top: 1px;">{emoji}</span>'
        f'<div style="flex: 1; min-width: 0;">'
        f'<div style="display: flex; align-items: center; gap: 7px;">'
        f'<span style="font-size: 15px; font-weight: 700; letter-spacing: -0.02em; color: {C["INK"]};">{name}</span>{badge_html}</div>'
        f'<div style="font-size: 12px; line-height: 1.45; color: {C["INK3"]}; margin-top: 3px;">{note_text}</div></div></div>'

        f'<div style="font-size: 10.5px; font-weight: 600; letter-spacing: 0.06em; color: {C["INK4"]}; margin-top: 12px;">입력하는 칸</div>'
        f'<div style="display: flex; gap: 6px; flex-wrap: wrap; margin-top: 6px;">{fields}</div>'

        f'<div style="display: flex; gap: 8px; padding: 9px 11px; background: {C["INSET"]}; border-radius: 11px; margin-top: 10px;">'
        f'<span style="flex-shrink: 0; margin-top: 1px;">{icon("chart", 13, C["INK3"], 1.9)}</span>'
        f'<span style="font-size: 11.5px; line-height: 1.5; color: {C["INK3"]};">{calc}</span></div>'

        f'<div style="margin-top: 11px; padding-top: 11px; border-top: 1px solid {C["LINE_ROW"]};">'
        f'<div style="font-size: 10.5px; font-weight: 600; letter-spacing: 0.06em; color: {C["INK4"]}; margin-bottom: 8px;">목록에서는 이렇게</div>'
        f'{row_html}</div>', pad='14px 15px')


def fieldchip(text, tone="mute"):
    m = {"mute": (C["INK2"], C["INSET"], C["BORDER"]),
         "brand": (C["BRAND"], C["BRAND_SOFT"], C["BRAND_SOFT"]),
         "vio": (C["VIO_STRONG"], C["VIO_SOFT"], C["VIO_SOFT"]),
         "off": (C["DIS"], C["SURF"], C["LINE"])}
    fg, bg, bd = m[tone]
    return (f'<span style="display: inline-flex; align-items: center; height: 27px; padding: 0 9px; border-radius: 8px; '
            f'background: {bg}; border: 1px solid {bd}; color: {fg}; font-size: 11.5px; font-weight: 600;">{text}</span>')


def goalrow(pct, color, title, meta1, meta2, action=None):
    act = action or ''
    return (f'<div style="display: flex; align-items: center; gap: 11px;">'
            f'{ring(pct, color, 40)}'
            f'<div style="flex: 1; min-width: 0;">'
            f'<div style="font-size: 13.5px; font-weight: 600; letter-spacing: -0.015em; color: {C["INK"]};">{title}</div>'
            f'<div style="font-size: 11.5px; color: {C["INK3"]}; margin-top: 2px;">{meta1}</div>'
            f'<div style="font-size: 11px; color: {C["INK4"]}; margin-top: 1px;">{meta2}</div></div>{act}</div>')


BLOCKS = [
    ('A · 일반 저축', type_block(
        '💰', '일반 저축', '수익률을 반영하지 않고 넣은 돈만 더합니다.',
        fieldchip('목표액 *') + fieldchip('현재 적립액') + fieldchip('목표일') + fieldchip('연 수익률', 'off'),
        '남은 금액을 월 적립액으로 나눠 도착 예상일을 계산합니다.',
        goalrow(20, C["BRAND"], '결혼 자금 2,000만원', '400 / 2,000만원 · 월 30만원',
                '도착 예상 2031년 3월', smallbtn('적립')))),

    ('B · 투자', type_block(
        '🌱', '투자', '설정한 투자 기대수익률을 반영합니다.',
        fieldchip('목표액 *') + fieldchip('현재 평가액') + fieldchip('목표일') + fieldchip('연 기대수익률 5.0%', 'vio'),
        '복리로 계산합니다. 수익률은 가정값이라 도착 예상 옆에 “가정”이 붙습니다.',
        goalrow(42, '#6B85EC', '투자 계좌 5,000만원', '2,100 / 5,000만원 · 월 28만원',
                '2032년 6월 도착 · 연 5.0% 가정', smallbtn('적립')),
        badge('가정 포함', 'vio'))),

    ('C · 순자산', type_block(
        '💎', '순자산', '현재 순자산과 자산별 가중 기대수익률을 그대로 씁니다.',
        fieldchip('목표액 *') + fieldchip('현재 순자산 9,350만원 · 자동', 'brand') + fieldchip('현재 적립액', 'off'),
        '현재 순자산은 자산 화면에서 자동으로 가져옵니다. 직접 넣는 값이 아니어서 적립 버튼이 없습니다.',
        goalrow(47, C["VIO"], '순자산 2억원', '순자산 9,350 / 20,000만원 · 자동 계산',
                '도착 예상 2031년 10월 · 미래 경로 기준',      # DestGoals · Goals · 숫자 기준표와 같은 값(2032년 6월은 투자 계좌 5,000만원의 도착일)
                f'<span style="font-size: 11px; color: {C["INK4"]}; flex-shrink: 0;">적립 없음</span>'))),

    ('D · 부채 상환', type_block(
        '🏔️', '부채 상환', '실제 부채 잔액과 상환 설정에서 진행률·완제일을 계산합니다.',
        fieldchip('연결할 부채 *') + fieldchip('신용대출 ✓', 'brand') + fieldchip('목표액', 'off') + fieldchip('적립액', 'off'),
        '연결한 부채의 남은 원금이 목표가 됩니다. 완제 예상일은 상환 전략 화면의 계획을 그대로 씁니다.',
        goalrow(31, C["NEG"], '신용대출 완제', '남은 원금 2,200만원 · 연 6.8%',
                '완제 예상 2030년 10월 · 상환 계획 반영',
                f'<span style="font-size: 11px; color: {C["INK4"]}; flex-shrink: 0;">적립 없음</span>'))),

    ('E · 비상금', type_block(
        '🧯', '비상금', '언제든 쓸 수 있는 현금으로 보고 수익률은 0%로 계산합니다.',
        fieldchip('목표액 *') + fieldchip('현재 적립액') + fieldchip('목표 개월 수') + fieldchip('연 수익률 0% 고정', 'off'),
        '목표액은 월 고정비 × 개월 수로도 정할 수 있습니다. 수익률은 0%로 고정됩니다.',
        goalrow(68, C["BRAND"], '비상금 6개월', '월 고정비 250만원 × 6개월 = 1,500만원',
                '남은 480만원 · 월 35만원', smallbtn('적립')))),
]


REF_PILL = (f'<span style="display: inline-block; margin-bottom: 8px; font-size: 11px; font-weight: 600; '
            f'letter-spacing: 0.02em; color: {C["INK2"]}; border: 1px solid {C["LINE"]}; background: {C["SURF"]}; '
            f'border-radius: 99px; padding: 4px 10px; white-space: nowrap;">구현 참고 · 앱 화면이 아닙니다</span>')


def legend_item(tone, text):
    # 견본 색은 fieldchip 과 같은 토큰을 쓴다.
    # 연한 장 배경 위에서는 배경색만으로 구분이 안 돼서, 글자 '가'를 넣은 작은 칩으로 그리고 테두리로 색을 드러낸다.
    fg, bg, bd = {"mute": (C["INK2"], C["INSET"], f'1px solid {C["INPUT"]}'),
                  "brand": (C["BRAND"], C["BRAND_SOFT"], f'1px solid {C["BRAND"]}'),
                  "vio": (C["VIO_STRONG"], C["VIO_SOFT"], f'1px solid {C["VIO_LINE"]}'),
                  "off": (C["DIS"], C["SURF"], f'1px dashed {C["DIS"]}')}[tone]
    return (f'<span style="display: inline-flex; align-items: center; gap: 5px; white-space: nowrap;">'
            f'<span style="display: inline-flex; align-items: center; height: 16px; padding: 0 5px; border-radius: 5px; '
            f'background: {bg}; border: {bd}; color: {fg}; font-size: 10px; font-weight: 600; line-height: 1; '
            f'flex-shrink: 0;">가</span>{text}</span>')


LEGEND = (f'<div style="display: flex; flex-wrap: wrap; gap: 5px 12px; margin-top: 9px; font-size: 11px; color: {C["INK3"]};">'
          + legend_item('mute', '진한 칸 = 직접 입력') + legend_item('brand', '파란 칸 = 자동으로 채워짐')
          + legend_item('vio', '보라 칸 = 가정값') + legend_item('off', '흐린 칸 = 이 유형에는 없음') + '</div>')


def types_sheet(h):
    # 구현 참고용 시트: 제목 위에 알약, 용도 문장 아래에 칸 색 범례를 끼운다(state_sheet 는 공용이라 그대로 둔다).
    html = state_sheet(
        '목적지 유형 5종',
        '목적지 유형마다 입력하는 칸과 계산 방식이 어떻게 다른지 보여 줍니다.',
        BLOCKS, h=h)
    assert html.count('<h2 ') == 1 and html.count('</p></div>') >= 1
    html = html.replace('<h2 ', REF_PILL + '<h2 ', 1)
    return html.replace('</p></div>', '</p>' + LEGEND + '</div>', 1)


# ══════════════════════════════════════════════════════════════
# 3 · 소비 · 과거 달
# ══════════════════════════════════════════════════════════════
def past_month_stepper():
    return (f'<div style="display: flex; align-items: center; gap: 2px; height: 34px; padding: 0 4px; border-radius: 10px; '
            f'background: {C["SURF"]}; border: 1px solid {C["LINE"]};">{icon("left", 16, C["TAB_INK"], 2)}'
            f'<span style="font-size: 13px; font-weight: 600; color: {C["INK"]}; padding: 0 4px;">2026년 7월</span>'
            f'{icon("right", 16, C["TAB_INK"], 2)}</div>')


def closed_hero(month, pct, diff, networth, metrics, reclose=False):
    """마감한 달의 히어로(= 소비 탭의 월 마감 카드). reclose=True 면 v5(§9-9) — 달력 카드가 없을 때 `N월 다시 마감 필요 ›` 한 줄이 붙는다(주황 없이 굵기만)."""
    tail = ''
    if reclose:
        tail = (f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 10px; height: 40px; margin-top: 10px; '
                f'margin-bottom: -6px; border-top: 1px solid {C["LINE_SOFT"]};">'
                f'<span style="font-size: 12.5px; font-weight: 600; color: {C["INK"]}; white-space: nowrap;">{month} 다시 마감 필요 &rsaquo;</span></div>')
    return hero(
        f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 10px;">'
        f'<span style="font-size: 11.5px; font-weight: 600; letter-spacing: 0.07em; color: {C["INK3"]};">마감한 달</span>'
        f'{badge(month + " 마감 완료 · 확정", "pos", "check")}</div>'

        f'<div style="display: flex; align-items: flex-end; justify-content: space-between; gap: 10px; margin-top: 9px;">'
        f'{display_num(pct, "%", 54, 25)}'
        f'<div style="text-align: right; flex-shrink: 0; padding-bottom: 6px;">'
        f'<div style="font-size: 11.5px; color: {C["INK3"]};">이번 달보다</div>'
        f'<div style="font-size: 13px; font-weight: 600; color: {C["POS"]};">{diff}</div></div></div>'

        f'<div style="display: flex; align-items: baseline; justify-content: space-between; gap: 10px; margin-top: 5px;">'
        f'<span style="font-size: 13px; font-weight: 500; color: {C["INK2"]};">월급 대비 소비 <b style=font-weight:600>확정</b></span>'
        f'<span style="display: inline-flex; align-items: center; gap: 4px; flex-shrink: 0;">'
        f'<span style="font-size: 11px; font-weight: 500; color: {C["INK4"]};">순자산 대비</span>'
        f'<span style="font-size: 13px; font-weight: 600; letter-spacing: -0.02em; color: {C["INK2"]};">{networth}</span></span></div>'

        + metric3(metrics)

        + f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 10px; margin-top: 12px; '
          f'padding-top: 11px; border-top: 1px solid {C["LINE_SOFT"]};">'
          f'<span style="font-size: 11.5px; color: {C["INK3"]};">{month} 마감값 기준 · 예상치 아님</span>'
          f'{link("마감 내역")}</div>' + tail)


past_hero = closed_hero('7월', '54.3', '3.6%p 낮음', '2.0%', [
    ('마감 실수령', '352', '만원', None),
    ('월 소비 합계', '191', '만원', None),
    ('남은 여유', '+20', '만원', C["POS"]),
])

past_chart = card(
    f'<div style="display: flex; align-items: baseline; justify-content: space-between; gap: 8px;">'
    f'<span style="font-size: 14px; font-weight: 600; color: {C["INK"]};">31일 동안 이렇게 썼어요</span>'
    f'<span style="font-size: 11.5px; color: {C["INK3"]};">확정 누적 191만원</span></div>'

    f'<div style="position: relative; height: 108px; margin-top: 12px;">'
    f'<span style="position: absolute; left: 0; top: 0; font-size: 10.5px; font-weight: 600; color: {C["INK3"]};">한도 211만</span>'
    f'<div style="position: absolute; left: 0; right: 0; top: 14px; border-top: 1px dashed {C["BORDER"]};"></div>'
    f'<svg width="100%" height="108" viewBox="0 0 330 108" preserveAspectRatio="none" style="position: absolute; inset: 0;">'
    f'<defs><linearGradient id="pg" x1="0" y1="0" x2="0" y2="1">'
    f'<stop offset="0" stop-color="{C["BRAND"]}" stop-opacity=".18"/>'
    f'<stop offset="1" stop-color="{C["BRAND"]}" stop-opacity="0"/></linearGradient></defs>'
    f'<path d="M2 100 L30 92 L58 88 L86 70 L114 64 L142 58 L170 50 L198 46 L226 38 L254 34 L282 30 L308 27 L322 26 L322 108 L2 108 Z" fill="url(#pg)"/>'
    f'<path d="M2 100 L30 92 L58 88 L86 70 L114 64 L142 58 L170 50 L198 46 L226 38 L254 34 L282 30 L308 27 L322 26" '
    f'fill="none" stroke="{C["BRAND"]}" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>'
    f'<circle cx="322" cy="26" r="4" fill="{C["BRAND"]}"/></svg>'
    f'<span style="position: absolute; right: 8px; top: 36px; font-size: 12px; font-weight: 700; color: {C["INK"]}; white-space: nowrap;">191만</span></div>'

    # 끝점은 점(r 4)이 카드 가장자리에 잘리지 않게 x 322 로 당겼다(오른쪽 여백 8). 나머지 날짜의 x 는 그대로다.
    # 눈금은 축 좌표에 맞춘다. 그림 영역 x 2~328이 1일~31일이므로
    # x(15) = 2 + 14/30 * 326 = 154.13 → viewBox 폭 330의 46.7%.
    # space-between으로 두면 가운데 라벨이 양끝 폭 차이만큼 밀려 여기서 3.5px 어긋났다.
    f'<div style="position: relative; height: 26px; border-top: 1px solid {C["LINE_SOFT"]}; padding-top: 8px; margin-top: 6px;">'
    f'<span style="position: absolute; left: 0; top: 8px; font-size: 11px; color: {C["INK4"]};">1일</span>'
    f'<span style="position: absolute; left: 46.7%; transform: translateX(-50%); top: 8px; font-size: 11px; color: {C["INK4"]}; white-space: nowrap;">15일</span>'
    f'<span style="position: absolute; right: 0; top: 8px; font-size: 11px; font-weight: 600; color: {C["INK"]};">31일 마감</span></div>')

past_cats = card(
    section_head('카테고리', '13개', link('내역 보기')) +
    f'<div style="margin-top: 11px; display: flex; flex-direction: column; gap: 10px;">'
    + ''.join(
        f'<div>'
        f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px; margin-bottom: 5px;">'
        f'<span style="display: inline-flex; align-items: center; gap: 7px;">{catdot(cat)}'
        f'<span style="font-size: 12.5px; color: {C["INK2"]};">{cat}</span></span>'
        f'<span style="font-size: 12.5px; font-weight: 600; color: {C["INK"]};">{amt}<span style="font-size: 11px; font-weight: 500; color: {C["INK3"]};">만원</span>'
        f'<span style="font-size: 11px; font-weight: 500; color: {C["INK4"]}; margin-left: 6px;">{pct}%</span></span></div>'
        f'{bar(pct, CAT[cat], 6)}</div>'
        for cat, amt, pct in [('주거/관리', '48', 25), ('식비', '41', 21), ('쇼핑', '26', 14)])
    + '</div>'
)

# 없는 탭은 없는 자리에서 설명한다 — 카드로 따로 두지 않는다.
tab_note = (f'<div style="display: flex; align-items: center; gap: 7px; padding: 0 16px 10px; flex-shrink: 0;">'
            f'{icon("info", 13, C["INK4"], 1.9)}'
            f'<span style="font-size: 11.5px; color: {C["INK3"]};">'
            f'마감한 달이라 <b style=font-weight:600>한도 탭이 없어요</b> · 기록은 내역에서 수정</span></div>')

w('SpendingPast', frame(
    screen_header('소비', '7월 · 마감됨', tabs=['월 요약', '내역'], active=0,
                  trailing=past_month_stepper()) +
    tab_note +
    content([past_hero, past_chart, past_cats], gap=10) +
    f'<div style="height: 12px; flex-shrink: 0;"></div>' +
    bottomnav(2)))


# ══════════════════════════════════════════════════════════════
# 4 · 코칭 · 기록 없음
# ══════════════════════════════════════════════════════════════
def step(num, title, body, action=None, done=False):
    mark = (f'<span style="width: 24px; height: 24px; border-radius: 99px; background: {C["POS_SOFT"]}; display: flex; '
            f'align-items: center; justify-content: center; flex-shrink: 0;">{icon("check", 14, C["POS"], 3)}</span>'
            if done else
            f'<span style="width: 24px; height: 24px; border-radius: 99px; background: {C["BRAND"]}; color: #FFFFFF; '
            f'display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 700; flex-shrink: 0;">{num}</span>')
    act = action or ''
    return (f'<div style="display: flex; align-items: center; gap: 11px; min-height: 52px; '
            f'border-bottom: 1px solid {C["LINE_ROW"]};">{mark}'
            f'<div style="flex: 1; min-width: 0;">'
            f'<div style="font-size: 13.5px; font-weight: 600; color: {C["INK"] if not done else C["INK3"]};">{title}</div>'
            f'<div style="font-size: 11.5px; color: {C["INK4"]}; margin-top: 2px;">{body}</div></div>{act}</div>')


w('CoachEmpty', sheet(
    '코칭', '기록이 쌓이면 무엇부터 손댈지 순서대로 알려 드려요.',
    card(
        f'<div style="display: flex; align-items: center; gap: 13px;">'
        f'<div style="width: 46px; height: 46px; border-radius: 14px; background: {C["BRAND_SOFT"]}; display: flex; '
        f'align-items: center; justify-content: center; flex-shrink: 0;">{icon("spark", 23, C["BRAND"], 1.9)}</div>'
        f'<div style="min-width: 0;">'
        f'<div style="font-size: 16px; font-weight: 700; letter-spacing: -0.02em; color: {C["INK"]};">'
        f'아직 안내할 것이 없어요</div>'
        f'<div style="font-size: 12px; line-height: 1.5; color: {C["INK2"]}; margin-top: 4px;">'
        f'NAVI는 <b style=font-weight:600>기록에서만</b> 안내를 만듭니다. 일반적인 절약 조언을 지어내지 않아요.</div></div></div>',
        pad='14px 15px') +

    card(
        f'<div style="font-size: 12.5px; font-weight: 600; color: {C["INK2"]}; margin-bottom: 4px;">두 가지만 있으면 시작합니다</div>'
        + step('1', '월 실수령 급여', '소비율과 한도의 기준', smallbtn('입력하기', 'primary'))
        + step('2', '이번 달 소비 기록 3건', '카테고리별 비교가 가능해지는 최소치',
               f'<span style="font-size: 11.5px; font-weight: 600; color: {C["INK4"]}; flex-shrink: 0;">0 / 3건</span>')
        + f'<div style="display: flex; align-items: center; gap: 11px; min-height: 52px;">'
          f'<span style="width: 24px; height: 24px; border-radius: 99px; background: {C["TRACK"]}; color: {C["DIS"]}; '
          f'display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 700; flex-shrink: 0;">3</span>'
          f'<div style="flex: 1; min-width: 0;">'
          f'<div style="font-size: 13.5px; font-weight: 600; color: {C["DIS"]};">자산·부채 (선택)</div>'
          f'<div style="font-size: 11.5px; color: {C["DIS"]}; margin-top: 2px;">있으면 상환 순서와 미래 경로까지 안내합니다</div></div>'
          f'<span style="font-size: 11.5px; color: {C["DIS"]}; flex-shrink: 0;">나중에</span></div>',
        pad='14px 15px') +

    card(
        eyebrow_row('기록이 쌓이면 이런 안내를 받습니다',
                    f'<span style="font-size: 11px; color: {C["INK4"]};">예시</span>') +
        f'<div style="display: flex; flex-direction: column; gap: 8px; margin-top: 10px; opacity: .5;">'
        + ''.join(
            f'<div style="display: flex; gap: 10px; padding: 10px 11px; background: {C["INSET"]}; border-radius: 12px;">'
            f'<span style="flex-shrink: 0; margin-top: 1px;">{icon(ic, 15, C["INK4"], 2)}</span>'
            f'<div style="min-width: 0;">'
            f'<div style="font-size: 12.5px; font-weight: 600; color: {C["INK3"]};">{t}</div>'
            f'<div style="font-size: 11px; color: {C["INK4"]}; margin-top: 1px;">{b}</div></div></div>'
            for ic, t, b in [
                ('arrowur', '고금리 부채부터 줄이기', '연 14.5% 할부가 자산 증가를 가장 크게 낮춰요'),
                ('target', '목적지 도착일을 당기는 법', '카테고리를 10% 줄이면 몇 개월 빨라지는지'),
            ])
        + '</div>'
        + f'<div style="margin-top: 11px;">'
        + note('절감 효과 비교는 저장된 기록을 바꾸지 않는 <b style=font-weight:600>가정</b>입니다.', 'vio', 'info')
        + '</div>',
        pad='14px 15px'),

    f'{btn("소비 기록하기", "primary", ic="plus", h=48).replace("width: 100%;", "flex: 1.4;")}'
    f'{btn("닫기", "secondary", h=48).replace("width: 100%;", "flex: 1;")}'), keep_all=True)



# ══════════════════════════════════════════════════════════════
# 5 · 달력이 없을 때 `확인할 내용`이 옮겨 가는 자리 (AlertsReview · 구현 참고 장)
# ══════════════════════════════════════════════════════════════
# plan/v5-calendar.md §3-3 · §8 · §9-9 · §9-19 · §12-36: 달력 카드를 껐거나 달력이 나오기 전 단계에서는 같은 목록 · 같은 문구를
# 소비 탭 알림 줄(AlertsPanel)이 보여 주고, `8월 다시 마감 필요 ›`는 월 마감 카드에도, `분류하기 ›`는 내역 필터 칩으로도 나온다.
# 표현은 굵기 600 · 주황 없음. 틀과 알림 행은 gen_modals 의 것을 그대로 쓴다(import 하면 모달 장도 다시 써지지만 같은 내용이다).
from gen_modals import alert, group, ALERTS_DESC, STALE_NOTE, spec_frame, mark, guide_row, case_cap

REVIEW_ITEMS = ['8월 다시 마감 필요', '통신 반복 건이 두 번 잡혔을 수 있어요', '분류 안 함 7건 · 분류하기']


def review_row(text, last=False):
    bb = '' if last else f'border-bottom: 1px solid {C["LINE_ROW"]};'
    return (f'<div style="display: flex; align-items: center; min-height: 44px; {bb}">'
            f'<span style="font-size: 13.5px; font-weight: 600; color: {C["INK"]};">{text} &rsaquo;</span></div>')


review_group = (
    f'<div style="position: relative; flex-shrink: 0;">'
    + group('확인할 내용', f'<div style="padding: 0 13px; background: {C["INSET"]}; border-radius: 14px;">'
            + ''.join(review_row(t, last=(i == len(REVIEW_ITEMS) - 1)) for i, t in enumerate(REVIEW_ITEMS)) + '</div>', mb=7)
    + mark(1, pos='position: absolute; top: -5px; right: -5px;') + '</div>')

alerts_review_sheet = sheet(
    '알림 3건', ALERTS_DESC,
    review_group +
    f'<div style="display: flex; flex-direction: column;">'
    f'{alert("warn", "warn", "주거/관리 한도의 94%를 썼어요", "47만원 / 50만원 · 이번 달 22일 남음", "카테고리 한도")}'
    f'{alert("neg", "bank", "카드 할부 금리가 14.5%예요", "보유 부채 중 가장 높습니다", "상환 전략")}'
    f'{alert("sky", "shield", "비상금이 목표의 68%예요", "1,020 / 1,500만원 · 480만원 남음", "목적지 배분")}</div>'
    f'{STALE_NOTE}',
    btn('닫기', 'secondary', h=48), scrim_h=40, body_gap=13)

# 8월 마감 카드 — 값은 MonthlyClose 의 8월(급여 360만 · 소비 2,043,800 · 소비율 56.8% · 월말 순자산 9,120만)에서 계산.
# `남은 여유`는 SpendingPast(7월: 한도 211 − 소비 191 = +20)와 같은 정의 = 소비 한도 − 월 소비 합계 → 360 × 60% = 216 − 204.4 = 11.6 → +12.
# (저축·투자 여력 식 390 − 204.4 − 92 − 63 = +31 은 다른 이름의 값이라 이 라벨에 쓰지 않는다 · 숫자 기준표 #3 · #11)
aug_hero = closed_hero('8월', '56.8', '1.1%p 낮음', '2.2%', [
    ('마감 실수령', '360', '만원', None),
    ('월 소비 합계', '204', '만원', None),
    ('남은 여유', '+12', '만원', C["POS"]),
], reclose=True)

_chip = lambda inner, on=False, strong=False: (
    f'<span style="display: inline-flex; align-items: center; gap: 4px; height: 32px; padding: 0 10px; border-radius: 99px; '
    + (f'background: {C["BRAND_SOFT"]}; color: {C["BRAND"]}; font-weight: 600;' if on else
       f'border: 1px solid {C["LINE"]}; color: {C["INK"] if strong else C["INK2"]}; font-weight: {600 if strong else 500};')
    + f' font-size: 12.5px; white-space: nowrap; flex-shrink: 0;">{inner}</span>')
chips_sample = card(
    f'<div style="display: flex; gap: 5px; overflow: hidden;">'
    + _chip(f'전체 14건{icon("down", 13, C["BRAND"], 2)}', on=True) + _chip('분류 안 함 7건', strong=True)
    + _chip(f'{catdot("식비", 8)}식비') + '</div>', pad='12px 14px')      # 폭 340 안에 들어가게 앞의 세 칩만
# `전체 14건` = LedgerV5 의 칩과 같은 수(gen_screens.V5_COUNT · 소비 13 + 이체 1). gen_screens 는 import 하면 장을 다시 쓰므로 글자로 둔다 — 그쪽 행 수가 바뀌면 여기도 맞춘다.

REVIEW_GUIDE = [
    (1, '확인할 내용', '달력 카드의 「확인할 내용 N개 ›」 목록과 같은 세 항목 · 같은 문구입니다.',
     '달력 카드를 끈 사용자와 달력이 나오기 전 단계에서만 알림 맨 위에 보입니다. 굵기로만 구분하고 주황은 쓰지 않습니다. 항목이 없으면 이 묶음도 없습니다. '
     '그림은 세 항목이 모두 있을 때입니다 — 9월 8일 시안의 홈에는 그중 둘만 있습니다(확인할 내용 목록 시트 장).'),
    (None, '8월 다시 마감 필요 ›', '8월 월 마감 창을 엽니다.', '마감한 뒤 그 달의 소비 합계가 바뀌었을 때 생깁니다(조건은 지금과 같음).'),
    (None, '통신 반복 건이 두 번 잡혔을 수 있어요 ›', '그 날짜의 하루 시트를 열어 두 행을 보여 줍니다.', '손으로 적은 건과 자동 기록이 겹친 것 같을 때. 반복 겹침 확인이 들어가는 2단계부터 나옵니다.'),
    (None, '분류 안 함 7건 · 분류하기 ›', '분류하기 시트를 엽니다.', '분류 안 함이 1건 이상이면 항상 들어갑니다.'),
]
review_guide = card(''.join(guide_row(*r, last=(i == len(REVIEW_GUIDE) - 1)) for i, r in enumerate(REVIEW_GUIDE)), pad='4px 16px')
review_foot = (f'<p style="margin: 0 2px; font-size: 12px; line-height: 1.6; color: {C["INK3"]};">달력을 끈 홈에서도 히어로의 '
               f'<b style="font-weight: 600; color: {C["INK2"]};">소비 기록하기</b>는 그대로 오늘 하루 시트를 엽니다. 홈에는 이 목록을 따로 두지 않습니다.</p>')

w('AlertsReview', spec_frame(
    1200, 1040, '달력이 없을 때 「확인할 내용」이 보이는 곳',
    '홈에 달력 카드가 없으면(껐거나 달력이 나오기 전 단계) 같은 목록을 소비 탭의 알림이 보여 줍니다. 왼쪽이 알림 창, 오른쪽 아래가 같은 문구가 붙는 다른 두 자리입니다.',
    f'<div style="display: flex; gap: 28px; align-items: flex-start;">'
    f'<div style="width: 390px; flex-shrink: 0; border-radius: 18px; overflow: hidden;">{alerts_review_sheet}</div>'
    f'<div style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 18px;">{review_guide}'
    f'<div style="display: flex; gap: 20px; align-items: flex-start;">'
    f'<div style="width: 362px; flex-shrink: 0; display: flex; flex-direction: column; gap: 8px;">'
    f'{case_cap(2, "소비 탭의 월 마감 카드", "다시 마감해야 하는 달의 카드 맨 아래에 같은 문구가 한 줄 붙습니다. 누르면 그 달의 월 마감 창이 열립니다.")}{aug_hero}</div>'
    f'<div style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 8px;">'
    f'{case_cap(3, "내역 탭의 필터 칩", "분류하기 시트는 이 칩으로도 열립니다(소비 · 내역 v5 장).")}{chips_sample}</div></div>'
    f'{review_foot}</div></div>', sub_w=1000), keep_all=True)

if __name__ == '__main__':
    import sys
    h = int(sys.argv[1]) if len(sys.argv) > 1 else 1920
    w('GoalTypes', types_sheet(h), keep_all=True)
