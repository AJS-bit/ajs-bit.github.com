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
# 1 · 적립 모달 (goals-5 · goals-6 · goals-23 · D4 · D11 · components/navi/goal-contribute-dialog.tsx)
# 시안 사용자의 비상금 6개월(1,020 / 1,500만원 · 매달 70만원 · 도착 예상 2027년 4월)에 50만원을 넣을 때 — 값은 NUMBERS §7.
# ══════════════════════════════════════════════════════════════
def checkbox_row(text, on=False):
    box = (f'<span style="width: 20px; height: 20px; border-radius: 6px; border: 1.5px solid {C["INPUT"]}; background: {C["SURF"]}; flex-shrink: 0;"></span>'
           if not on else f'<span style="width: 20px; height: 20px; border-radius: 6px; background: {C["BRAND"]}; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">{icon("check", 13, "#FFFFFF", 3)}</span>')
    # 앱 .goal-contribution-asset-check — 줄 높이 46 · 상자 뒤 8 · 13.5 / 500 / 18.9 ink-2(2026-09-27 fix-up 5 · 예전 높이 20 · 사이 10)
    return (f'<div style="display: flex; align-items: center; gap: 8px; min-height: 46px; flex-shrink: 0;">{box}'
            f'<span style="font-size: 13.5px; font-weight: 500; line-height: 18.9px; color: {C["INK2"]};">{text}</span></div>')


CONTRIB_H = 892      # 자연 868 + 24 — gen_canvas TALL · screens.json 과 같아야 한다(2026-09-27 fix-up 5)


def same(value, note_text):
    return (f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px; min-height: 38px;">'
            f'<span style="font-size: 12.5px; color: {C["INK2"]};">{note_text}</span>'
            f'<span style="display: inline-flex; align-items: baseline; gap: 6px; flex-shrink: 0;">'
            f'<span style="font-size: 14px; font-weight: 700; letter-spacing: -0.02em; color: {C["INK"]};">{value}</span>'
            f'<span style="font-size: 12px; font-weight: 500; line-height: 18px; color: {C["INK3"]};">변화 없음</span></span></div>')      # 앱 .goal-contribution-unchanged 12 / 500


w('GoalContribute', sheet(
    '비상금 6개월에 적립',
    '이번에 넣은 돈을 목적지에 더해요.',
    card(
        f'<div style="display: flex; align-items: center; gap: 13px;">'
        f'{ring(68, C["BRAND"], 52, "68%")}'
        f'<div style="flex: 1; min-width: 0;">'
        f'<div style="font-size: 15px; font-weight: 700; letter-spacing: -0.02em; color: {C["INK"]};">비상금 6개월</div>'
        f'<div style="font-size: 12.5px; color: {C["INK3"]}; margin-top: 3px;">'
        f'<b style=font-weight:600>1,020 / 1,500만원</b> · 남은 480만원</div>'
        f'<div style="font-size: 11.5px; color: {C["INK4"]}; margin-top: 2px;">매달 70만원 · 도착 예상 2027년 4월</div>'
        f'</div></div>', pad='14px 15px') +

    '<div style="flex-shrink: 0;">' +
    field('이번에 넣은 돈', '50', unit='만원', required=True, readback='50만원',
          helper='실제로 넣은 금액을 적어 주세요') +
    f'<div style="display: flex; gap: 7px; margin-top: 10px; flex-wrap: wrap;">'
    f'{chip("매달 70만원")}{chip("50만원", True)}{chip("남은 480만원")}</div>'
    # 잔액도 늘리기 = 앱 .goal-contribution-entry 안 12 아래(따로 15 아래가 아님 · 2026-09-27 fix-up 5)
    f'<div style="margin-top: 12px;">{checkbox_row("생활비 통장 잔액도 50만원 늘리기")}</div>'
    '</div>' +

    card(
        eyebrow_row('저장하면 이렇게 바뀌어요',
                    f'<span style="font-size: 11px; color: {C["INK4"]};">지금 매달 모을 수 있는 돈 기준</span>') +
        f'<div style="margin-top: 4px;">'
        f'{delta("1,020만원", "1,070만원", "모은 돈")}'
        f'{delta("68%", "71%", "진행률")}'
        f'{delta("80만원", "72만원", "매달 필요한 돈")}'
        f'{same("2027년 4월", "도착 예상")}'
        f'</div>',
        pad='13px 15px') +

    note('이 기록은 목적지의 모은 돈만 바꿔요. 통장에 실제로 넣었다면 위에서 잔액도 함께 늘릴 수 있어요.', 'mute'),

    # 앱 하네스(390 × 844)는 시트 윗변 60 · 본문이 넘쳐 스크롤 — 시안은 본문을 다 펼쳐 그린다(2026-09-27 fix-up 5 · 예전 윗변 40 · 844 안에 눌러 담음)
    sheet_footer('취소', '적립하기'), scrim_h=60, body_pb=14, h=CONTRIB_H), keep_all=True)


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


# 고리 · 적립 버튼 색 = 앱 목록(goals-view.tsx: 부채 상환 --warning · 투자 --violet · 비상금 현금성 색 · 그 밖 --primary)과
# 캔버스의 목적지 목록(Goals)과 같게. 순자산 · 부채 상환은 이름 옆에 유형 꼬리표(앱 `<small>{typeInfo.label}</small>` · 바탕 --goal-soft).
EMERGENCY_RING = '#38bdf8'


def kindtag(text, fg, bg):
    return (f'<span style="font-size: 10px; font-weight: 600; color: {fg}; background: {bg}; border-radius: 5px; padding: 2px 5px; '
            f'white-space: nowrap; flex-shrink: 0;">{text}</span>')


def goalrow(pct, color, title, meta1, meta2, action=None, tag=''):
    act = action or ''
    return (f'<div style="display: flex; align-items: center; gap: 11px;">'
            f'{ring(pct, color, 40, str(pct) + "%")}'
            f'<div style="flex: 1; min-width: 0;">'
            f'<div style="display: flex; align-items: center; gap: 6px; font-size: 13.5px; font-weight: 600; letter-spacing: -0.015em; color: {C["INK"]};">{title}{tag}</div>'
            f'<div style="font-size: 11.5px; color: {C["INK3"]}; margin-top: 2px;">{meta1}</div>'
            f'<div style="font-size: 11px; line-height: 1.45; color: {C["INK4"]}; margin-top: 1px;">{meta2}</div></div>{act}</div>')


def late(text):
    return f'<span style="color: {C["NEG"]};">{text}</span>'


def addbtn(tone='brand'):
    """「+ 적립」 — 바탕은 그 목적지 유형의 옅은 색(앱 --goal-soft · Goals 장과 같게)."""
    fg, bg = {'brand': (C["BRAND"], C["BRAND_SOFT"]), 'vio': (C["VIO_STRONG"], C["VIO_SOFT"]),
              'sky': (C["SKY"], C["SKY_SOFT"])}[tone]
    return (f'<div style="display: inline-flex; align-items: center; height: 30px; padding: 0 11px; border-radius: 9px; background: {bg}; '
            f'color: {fg}; font-size: 12.5px; font-weight: 600; white-space: nowrap; flex-shrink: 0;">+ 적립</div>')


# 줄은 앱 목록(components/navi/goals-view.tsx)과 같게 — 고리 안 %, 「매달 N만원」, 도착 예상 · 늦으면 빨간 「목표일보다 약 … 늦어요」,
# 순자산 · 부채 상환은 적립 버튼 없음(D4 · D12 · goals-8 · goals-23). 값은 NUMBERS §7 · §13(A는 샘플 밖 예시 그대로).
BLOCKS = [
    ('A · 일반 저축', type_block(
        '💰', '일반 저축', '수익 없이 넣은 돈만 계산해요',
        fieldchip('이름 *') + fieldchip('표시 아이콘') + fieldchip('목표액 *') + fieldchip('지금 모은 돈') + fieldchip('우선순위') + fieldchip('목표일 *') + fieldchip('6개월 · 1년 · 2년'),
        '남은 금액을 매달 넣을 돈으로 나눠 도착 예상 달을 계산해요.',
        goalrow(20, C["BRAND"], '결혼 자금 2,000만원', '400 / 2,000만원 · 매달 30만원',
                '도착 예상 2031년 3월', addbtn()))),

    ('B · 투자', type_block(
        '🌱', '투자', '설정의 투자 자산 기본 수익률로 계산해요',
        fieldchip('이름 *') + fieldchip('표시 아이콘') + fieldchip('목표액 *') + fieldchip('지금 금액') + fieldchip('수익률 (연)') + fieldchip('우선순위') + fieldchip('목표일 *') + fieldchip('6개월 · 1년 · 2년'),
        '복리로 계산해요. 수익률을 비우면 설정의 투자 자산 기본 수익률(연 5.0%)을 써요.',
        goalrow(42, C["VIO"], '투자 계좌 5,000만원', '2,100 / 5,000만원 · 매달 19만원',
                '도착 예상 <span style="white-space: nowrap;">2033년 12월</span> · ' + late('목표일보다 <span style="white-space: nowrap;">약 4년 3개월</span> 늦어요') + ' · 수익률 연 5.0%', addbtn('vio')))),

    ('C · 순자산', type_block(
        '💎', '순자산', '지금 순자산과 가진 자산들의 평균 수익률로 계산해요',
        fieldchip('이름 *') + fieldchip('표시 아이콘') + fieldchip('목표액 *') + fieldchip('지금 순자산 · 자동 9,350만원', 'brand') + fieldchip('우선순위') + fieldchip('목표일 *') + fieldchip('지금 모은 돈', 'off'),
        '지금 순자산은 자산 탭에서 자동으로 가져와요 · 적립 버튼이 없어요',
        goalrow(47, C["BRAND"], '순자산 2억원', '9,350만 / 2억원 · 자산에서 자동으로 계산',
                '도착 예상 2031년 1월 · 미래 탭 계산', tag=kindtag('순자산', C["BRAND"], C["BRAND_SOFT"])))),

    ('D · 부채 상환', type_block(
        '🏔️', '부채 상환', '남은 빚과 상환 계획으로 다 갚는 달을 계산해요',
        fieldchip('이름 *') + fieldchip('표시 아이콘') + fieldchip('갚을 부채 · 1개 골랐어요 · 2,200만원', 'brand') + fieldchip('우선순위') + fieldchip('목표일 *') + fieldchip('목표액', 'off') + fieldchip('지금 모은 돈', 'off'),
        '목표액과 진행률은 실제 남은 원금에서 자동으로 계산해요. 매달 모으는 돈에서 따로 나눠 넣지 않아요.',
        goalrow(31, C["WARN"], '신용대출 다 갚기', '남은 원금 2,200만원 · 연 6.8%',
                '다 갚는 달 2030년 11월 · 상환 계획대로', tag=kindtag('부채 상환', C["WARN"], C["WARN_SOFT"])))),

    ('E · 비상금', type_block(
        '🧯', '비상금', '언제든 쓸 수 있는 현금이라 수익률 0%로 계산해요',
        fieldchip('이름 *') + fieldchip('표시 아이콘') + fieldchip('목표액 *') + fieldchip('지금 모은 돈') + fieldchip('지금 현금성 자산 1,460만원 넣기', 'brand') + fieldchip('우선순위') + fieldchip('목표일 *') + fieldchip('6개월 · 1년 · 2년'),
        '수익률은 0%로 계산해요. 지금 모은 돈 칸 아래 버튼으로 자산 탭의 현금성 자산 금액을 넣을 수 있어요.',
        goalrow(68, EMERGENCY_RING, '비상금 6개월', '1,020 / 1,500만원 · 매달 70만원',
                '도착 예상 2027년 4월 · ' + late('목표일보다 약 1개월 늦어요'), addbtn('sky')))),
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
          + legend_item('off', '흐린 칸 = 이 유형에는 없음') + '</div>')


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
# 3 · 소비 · 지난 달 월 요약 (spending-4 · spending-18 · spending-23 · record-1 · D9 · components/navi/spending-overview.tsx)
# 세 장: 마감한 7월(SpendingPast) · 아직 마감 안 한 8월(SpendingPastOpen · 6월만 마감한 날) · 마감 뒤 기록이 바뀐 8월(SpendingPastChanged).
# 값은 앱에 시안 사용자(W/design-state.json)를 넣은 화면 그대로(NUMBERS §5 · 2026-09-25 캡처).
# ══════════════════════════════════════════════════════════════
from gen_calendar import AUG

# 7월 날짜별 소비(시안 사용자 기록 · 저축/투자 이체 제외) — 합 191만원 = 7월 마감의 소비 합계
JUL = {3: 110_000, 5: 720_000, 9: 90_000, 10: 45_000, 12: 410_000, 15: 60_000, 18: 260_000, 21: 120_000, 26: 50_000, 28: 45_000}
assert sum(JUL.values()) == 1_910_000
AUG_DAYS = {d: (v or 0) for d, v in AUG.items()}
assert sum(AUG_DAYS.values()) == 1_715_200
LATE = 55_000      # 마감 뒤 8월 30일에 더 적은 식비(SpendingPastChanged) — 마감 때 1,715,200원 → 지금 기록 1,770,200원


def cum_path(daily, days=31):
    """누적 소비 선 — x 2~328(1일~31일) · y 100(0원) ~ 10(그 달 합계)."""
    tot = sum(daily.values())
    c, pts = 0, []
    for d in range(1, days + 1):
        c += daily.get(d, 0)
        x = 2 + (d - 1) * 326 / (days - 1)
        y = 100 - 90 * c / tot
        pts.append(f'{x:.1f} {y:.1f}')
    return 'M' + ' L'.join(pts)


def past_chart(daily, total_label):
    path = cum_path(daily)
    ticks = ''.join(
        f'<span style="position: absolute; left: {pct}%; transform: translateX({tx}); top: 8px; font-size: 11px; color: {C["INK4"]}; white-space: nowrap;">{d}일</span>'
        for d, pct, tx in [(1, 0.6, '0'), (8, 22.5, '-50%'), (15, 46.7, '-50%'), (22, 70.9, '-50%'), (31, 99.4, '-100%')])
    return card(
        f'<div style="display: flex; align-items: baseline; justify-content: space-between; gap: 8px;">'
        f'<span style="font-size: 14px; font-weight: 600; color: {C["INK"]};">31일 동안 이렇게 썼어요</span>'
        f'<span style="font-size: 12px; color: {C["INK3"]};">기록 합계 {total_label}</span></div>'
        f'<div style="position: relative; height: 108px; margin-top: 12px;">'
        f'<svg width="100%" height="108" viewBox="0 0 330 108" preserveAspectRatio="none" style="position: absolute; inset: 0;">'
        f'<defs><linearGradient id="pg" x1="0" y1="0" x2="0" y2="1">'
        f'<stop offset="0" stop-color="{C["BRAND"]}" stop-opacity=".16"/>'
        f'<stop offset="1" stop-color="{C["BRAND"]}" stop-opacity="0"/></linearGradient></defs>'
        f'<path d="{path} L328 108 L2 108 Z" fill="url(#pg)"/>'
        f'<path d="{path}" fill="none" stroke="{C["BRAND"]}" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg></div>'
        # 눈금 x = 2 + (일 − 1)/30 × 326 → viewBox 330 의 %(1일 · 8일 · 15일 · 22일 · 31일)
        f'<div style="position: relative; height: 26px; border-top: 1px solid {C["LINE_SOFT"]}; padding-top: 8px; margin-top: 6px;">{ticks}</div>')


CAT_IC = {'주거/관리': 'house', '식비': 'rice', '쇼핑': 'bag', '보험': 'shield', '문화/여가': 'leaf', '교통': 'bus', '통신': 'phone'}


def past_cats(total_label, n, rows):
    items = []
    for cat, man, pct in rows:
        items.append(
            f'<div style="display: flex; align-items: center; gap: 11px;">{caticon(cat, CAT_IC[cat], 34)}'
            f'<div style="flex: 1; min-width: 0;">'
            f'<div style="display: flex; align-items: baseline; justify-content: space-between; gap: 8px;">'
            f'<span style="font-size: 14px; font-weight: 600; color: {C["INK"]};">{cat}</span>'
            f'<span style="font-size: 13.5px; font-weight: 700; color: {C["INK"]};">{man}만원</span></div>'
            f'<div style="margin-top: 6px;">{bar(pct, CAT[cat], 6)}</div></div>'
            f'<span style="font-size: 12.5px; font-weight: 600; color: {C["INK3"]}; white-space: nowrap; flex-shrink: 0; width: 76px; text-align: right;">전체의 {pct}% &rsaquo;</span></div>')
    return card(
        f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px;">'
        f'<div style="display: flex; align-items: baseline; gap: 7px;"><span style="font-size: 15px; font-weight: 700; color: {C["INK"]};">카테고리</span>'
        f'<span style="font-size: 12.5px; color: {C["INK3"]};">{total_label} · {n}개</span></div>{link("내역 보기")}</div>'
        f'<div style="margin-top: 12px; display: flex; flex-direction: column; gap: 12px;">{"".join(items)}</div>')


TREND_FOLD = card(f'<div style="display: flex; align-items: center; gap: 8px; font-size: 14px; font-weight: 600; color: {C["INK"]};">'
                  f'<svg width="9" height="9" viewBox="0 0 9 9"><path d="M1.5 0 7.5 4.5 1.5 9Z" fill="{C["INK"]}"/></svg>소비 추이·절감 기회</div>', pad='14px 16px')

# 없는 탭은 없는 자리에서 설명한다 — 카드로 따로 두지 않는다.
tab_note = (f'<div style="display: flex; align-items: center; gap: 7px; padding: 0 16px 10px; flex-shrink: 0;">'
            f'{icon("info", 13, C["INK4"], 1.9)}'
            f'<span style="font-size: 12px; color: {C["INK3"]};">지난 달에는 한도 탭이 없어요 · 기록은 내역에서 고쳐요</span></div>')


def close_card(title, body, right, tone=None):
    """월 마감 카드 — 월 요약 맨 위. tone='warn' 이면 주황 테두리."""
    bd = f'1px solid {C["WARN_RULE"]}' if tone == 'warn' else f'1px solid {C["LINE"]}'
    return (f'<div style="background: {C["SURF"]}; border: {bd}; border-radius: 18px; padding: 13px 15px; flex-shrink: 0;">'
            f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 10px;">'
            f'<div style="min-width: 0;"><div style="font-size: 12.5px; font-weight: 600; color: {C["INK"]};">{title}</div>'      # 앱 월 마감 카드 제목 12.5 / 600(2026-09-27 fix-up 2)
            f'<div style="font-size: 11.5px; line-height: 1.45; color: {C["INK3"]}; margin-top: 3px;">{body}</div></div>{right}</div></div>')


def past_hero(eyebrow, badge_html, value, caption, burn, metrics, foot):
    big = (display_num(value, "%", 54, 25) if value else
           f'<div style="height: 54px; display: flex; align-items: center;"><span style="width: 32px; height: 5px; border-radius: 3px; background: {C["INK3"]};"></span></div>')
    return hero(
        f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 10px;">'
        f'<span style="font-size: 12px; font-weight: 600; letter-spacing: 0.04em; color: {C["INK3"]};">{eyebrow}</span>{badge_html}</div>'
        f'<div style="margin-top: 12px;">{big}</div>'
        # 앱 .spending-fidelity-top p — 12px · 500 · ink-3 · 줄이 좁으면 오른쪽 줄이 아래로 내려간다(2026-09-27 fix-up · 예전 12.5 ink-2 nowrap 은 오른쪽 줄이 4px 넘침)
        f'<div style="display: flex; flex-wrap: wrap; align-items: baseline; justify-content: space-between; gap: 4px 10px; margin-top: 8px;">'
        f'<span style="font-size: 12px; font-weight: 500; color: {C["INK3"]};">{caption}</span>'
        f'<span style="font-size: 12px; color: {C["INK2"]}; white-space: nowrap;">한 달에 순자산의 <b style="font-weight: 700; color: {C["INK"]};">{burn}</b>를 썼어요</span></div>'
        + metric3(metrics)
        + f'<div style="margin-top: 12px; padding-top: 11px; border-top: 1px solid {C["LINE_SOFT"]}; font-size: 12px; color: {C["INK3"]};">{foot}</div>')


# 높이 = 본문을 다 보여 주는 자연 높이 + 24(다른 탭 장과 같게 · 실제 웹폰트로 잼 · gen_canvas TALL · screens.json 과 같게 · 2026-09-27 fix-up · 예전 844 는 카테고리 카드가 탭 막대 밑에 가렸다)
PAST_H = {'SpendingPast': 1212, 'SpendingPastOpen': 1264, 'SpendingPastChanged': 1212}      # 자연 1188 · 1240 · 1188 + 24(2026-09-27 fix-up 2 월 마감 카드 글자 크기를 앱대로)


def past_screen(month_label, close, hero_html, chart_html, cats_html, h=844):
    return (frame(
        screen_header('소비', tabs=['월 요약', '내역'], active=0, subrow=month_row(month_label, next_on=True)) +
        tab_note +
        content([close, hero_html, chart_html, cats_html, TREND_FOLD], gap=10) +
        f'<div style="height: 12px; flex-shrink: 0;"></div>' +
        bottomnav(2), h=h), True)


def link_btn(text, col=None):
    return f'<span style="font-size: 11.5px; font-weight: 600; color: {col or C["BRAND"]}; white-space: nowrap; flex-shrink: 0;">{text} &rsaquo;</span>'


# 7월 — 8월 2일에 마감(당시 월급 352만원 · 월급 + 부수입 382만원 · 대출상환 92만원). 소비·상환 후 = 382 − 191 − 92 = 99만원(부호 없음 · 기본 글자색)
w('SpendingPast', *past_screen(
    '2026년 7월',
    close_card('7월 마감 · 8월 2일에 마감했어요', '당시 월급 + 부수입 382만원 · 대출상환 92만원', link_btn('마감값 보기·고치기')),
    past_hero('마감한 달', badge('7월 마감값 기준', 'pos'), '54.3', '월급 대비 소비 · 마감 기준', '2.0%',
              [('월급', '352', '만원', None), ('월 소비 합계', '191', '만원', None), ('소비·상환 후', '99', '만원', None)], '7월 마감값 기준'),
    past_chart(JUL, '191만원'),
    past_cats('191만원', 13, [('주거/관리', 48, 25), ('식비', 41, 21), ('쇼핑', 26, 14), ('보험', 12, 6), ('문화/여가', 12, 6)]), h=PAST_H['SpendingPast']))


def month_chips():
    # 앱 월 마감 카드의 마감할 달 줄 — 11.5px · 이름표 600(2026-09-27 fix-up 2)
    return (f'<div style="display: flex; align-items: center; gap: 12px; margin-top: 10px; padding-top: 10px; border-top: 1px solid {C["LINE_SOFT"]}; font-size: 11.5px; line-height: 1.45;">'
            f'<span style="font-weight: 600; color: {C["INK3"]};">마감할 달</span>'
            f'<span style="display: inline-flex; align-items: center; gap: 3px; color: {C["INK3"]};">{icon("check", 13, C["INK3"], 2.4)}6월</span>'
            f'<span style="font-weight: 600; color: {C["BRAND"]};">7월</span>'
            f'<span style="font-weight: 700; color: {C["INK"]};">8월</span></div>')


# 8월 — 아직 마감 전(6월만 마감한 날). 월급은 채우지 않는다(—) · 순자산 비율 = 172만 ÷ 8월 순자산 9,120만 = 1.9%
# 2026-09-27 fix-up 2: 앱 실측 글자 크기 — 제목 12.5 / 600 · 설명 11.5 / 16.7(두 줄) · 버튼 12.5 / 600 · 88 × 44 · 여백 0 10 → 카드 119(예전 13.5 / 700 · 12 / 1.5 · 14px 42 는 설명이 세 줄 · 149)
OPEN_CARD = (f'<div style="background: {C["SURF"]}; border: 1.5px solid {C["WARN_RULE"]}; border-radius: 18px; padding: 13px 14px; flex-shrink: 0;">'
             f'<div style="display: flex; align-items: center; gap: 12px;">'
             f'<div style="flex: 1; min-width: 0;"><div style="font-size: 12.5px; font-weight: 600; line-height: 1.45; color: {C["INK"]};">8월은 아직 마감하지 않았어요</div>'
             f'<div style="font-size: 11.5px; line-height: 1.45; color: {C["INK3"]}; margin-top: 2px;">마감하면 그 달 수입 · 상환으로 소비율을 확정해요 · 모두 마감하면 홈에서 월말 예상을 볼 수 있어요</div></div>'
             f'{btn("8월 마감하기", "primary", h=44, full=False, size=12.5).replace("gap: 6px;", "gap: 6px; padding: 0 10px; flex-shrink: 0;")}</div>'
             f'{month_chips()}</div>')
w('SpendingPastOpen', *past_screen(
    '2026년 8월', OPEN_CARD,
    past_hero('지난 달 기록', badge('마감 전', 'mute'), None, '월급 대비 소비 · 마감하면 보여요', '1.9%',
              [('월급', '—', '', C["INK3"]), ('월 소비 합계', '172', '만원', None), ('소비·상환 후', '—', '', C["INK3"])], '지금 월급으로 지난달을 채우지 않아요'),
    past_chart(AUG_DAYS, '172만원'),
    past_cats('172만원', 13, [('주거/관리', 50, 29), ('식비', 30, 17), ('쇼핑', 18, 10), ('문화/여가', 13, 7), ('보험', 12, 7)]), h=PAST_H['SpendingPastOpen']))

# 8월 — 9월 2일에 마감한 뒤 8월 30일 식비 55,000원을 더 적은 경우(record-1 · D9). 히어로 · 그래프 · 카테고리는 지금 기록으로,
# 배지는 「마감 뒤 바뀜」. 49.2% = 1,770,200 ÷ 3,600,000 · 소비·상환 후 = 390 − 177 − 92 = 121만원
CHANGED_DAYS = dict(AUG_DAYS); CHANGED_DAYS[30] += LATE
w('SpendingPastChanged', *past_screen(
    '2026년 8월',
    close_card('8월 마감 뒤 기록이 바뀌었어요', '마감 때 1,715,200원 → 지금 기록 1,770,200원', link_btn('8월 합계 고치기', C["WARN"]), tone='warn'),
    past_hero('마감한 달', badge('마감 뒤 바뀜', 'warn'), '49.2', '월급 대비 소비 · 마감 기준', '1.9%',
              [('월급', '360', '만원', None), ('월 소비 합계', '177', '만원', None), ('소비·상환 후', '121', '만원', None)], '8월 마감값 기준'),
    past_chart(CHANGED_DAYS, '177만원'),
    past_cats('177만원', 13, [('주거/관리', 50, 28), ('식비', 36, 20), ('쇼핑', 18, 10), ('문화/여가', 13, 7), ('보험', 12, 7)]), h=PAST_H['SpendingPastChanged']))


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
        f'아직 알려 드릴 것이 없어요</div>'
        f'<div style="font-size: 12px; line-height: 1.5; color: {C["INK2"]}; margin-top: 4px;">'
        f'NAVI는 <b style=font-weight:600>내 기록에서만</b> 안내를 만들어요. 흔한 절약 조언을 지어내지 않아요.</div></div></div>',
        pad='14px 15px') +

    card(
        f'<div style="font-size: 12.5px; font-weight: 600; color: {C["INK2"]}; margin-bottom: 4px;">이렇게 시작해 보세요</div>'
        + step('1', '월급 (실수령)', '월급의 몇 %를 썼는지 보는 기준', smallbtn('입력하기', 'primary'))
        + step('2', '첫 소비 기록', '날짜를 누르고 숫자만 넣으면 돼요',
               f'<span style="font-size: 12px; font-weight: 600; color: {C["INK3"]}; flex-shrink: 0;">0건</span>')
        + f'<div style="display: flex; align-items: center; gap: 11px; min-height: 52px;">'
          f'<span style="width: 24px; height: 24px; border-radius: 99px; background: {C["TRACK"]}; color: {C["DIS"]}; '
          f'display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 700; flex-shrink: 0;">3</span>'
          f'<div style="flex: 1; min-width: 0;">'
          f'<div style="font-size: 13.5px; font-weight: 600; color: {C["DIS"]};">자산 · 부채 (선택 사항)</div>'
          f'<div style="font-size: 11.5px; color: {C["DIS"]}; margin-top: 2px;">있으면 순자산과 갚는 순서까지 알려 드려요</div></div>'
          f'<span style="font-size: 11.5px; color: {C["DIS"]}; flex-shrink: 0;">나중에</span></div>',
        pad='14px 15px') +

    card(
        eyebrow_row('기록이 쌓이면 이런 안내를 받아요',
                    f'<span style="font-size: 11px; color: {C["INK4"]};">예시</span>') +
        f'<div style="display: flex; flex-direction: column; gap: 8px; margin-top: 10px; opacity: .5;">'
        + ''.join(
            f'<div style="display: flex; gap: 10px; padding: 10px 11px; background: {C["INSET"]}; border-radius: 12px;">'
            f'<span style="flex-shrink: 0; margin-top: 1px;">{icon(ic, 15, C["INK4"], 2)}</span>'
            f'<div style="min-width: 0;">'
            f'<div style="font-size: 12.5px; font-weight: 600; color: {C["INK3"]};">{t}</div>'
            f'<div style="font-size: 11px; color: {C["INK4"]}; margin-top: 1px;">{b}</div></div></div>'
            for ic, t, b in [
                ('arrowur', '고금리 부채부터 줄이기', '넣은 금리를 보고 먼저 갚을 부채를 알려 드려요'),
                ('target', '목적지 도착을 당기는 법', '카테고리를 줄이면 몇 개월 빨라지는지'),
            ])
        + '</div>'
        + f'<div style="margin-top: 11px;">'
        + note('절감 효과 비교는 저장된 기록을 바꾸지 않는 <b style=font-weight:600>가정</b>이에요.', 'vio', 'info')
        + '</div>',
        pad='14px 15px'),

    f'{btn("오늘 쓴 돈 적기", "primary", ic="plus", h=48).replace("width: 100%;", "flex: 1.4;")}'
    f'{btn("닫기", "secondary", h=48).replace("width: 100%;", "flex: 1;")}'), keep_all=True)



# (5 · AlertsReview 「달력이 없을 때 확인할 내용이 보이는 곳」은 2026-09-22에 지웠다 — 달력이 늘 켜져 있어 그 상태가 없다.)


if __name__ == '__main__':
    import sys
    # 목적지 유형 시트 높이 = 실제 웹폰트로 잰 자연 높이 + 24(2026-09-25 · gen_canvas TALL · screens.json 과 같게).
    # 예전 호출(`gen_rest.py 1920`)의 숫자는 이 값보다 작으면 무시한다 — 소리 없이 잘리지 않게.
    H = 2170      # 2026-09-27 fix-up 칸 칩 「표시 아이콘」(유형마다) · 자연 2146 + 24
    h = max(int(sys.argv[1]), H) if len(sys.argv) > 1 else H
    w('GoalTypes', types_sheet(h), keep_all=True)
