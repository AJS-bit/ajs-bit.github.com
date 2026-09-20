# -*- coding: utf-8 -*-
"""v4 · 1단계 아트보드 — 첫 실행 소개 3장 · 홈 구성 1장 · 구성값을 반영한 홈 1장.

plan/v4-stocks.md §3(첫 실행 흐름)·§7(1단계)·§10. 라이트를 만들고 같은 자리에서 darken()으로
다크 짝까지 쓴다. 홈 아트보드의 헤더·히어로·다음 안내·이번 달 한도는 Main.dc.html에서 그대로
잘라 온다(v3 홈과 1px도 다르지 않아야 하므로 다시 그리지 않는다).

    python3 gen_v4.py            # 5 + 5장 → ../
"""
import pathlib
from gen_common import *
from darken import darken

OUT = pathlib.Path(__file__).resolve().parent.parent
V4 = ['IntroPosition', 'IntroRoute', 'IntroDestination', 'HomeSetup', 'HomeConfigured']

BRAND_GRAD = 'linear-gradient(140deg, #3556E6 0%, #7A3FE4 100%)'
ARROW = ('M20.28 2.32 2.88 9.62c-.9.4-.8 1.7.1 2l6.6 2.2c.3.1.5.3.6.6l2.2 6.6c.3.9 1.6 1 2 .1'
         'L21.68 3.72c.3-.8-.6-1.7-1.4-1.4Z')


KEEP_ALL_FROM = '-webkit-font-smoothing: antialiased; }'
KEEP_ALL_TO = '-webkit-font-smoothing: antialiased; word-break: keep-all; }'


def w(name, body, keep_all=True):
    """keep_all — 한국어가 단어 중간에서 줄바꿈되지 않게 body에 word-break: keep-all을 넣는다.
    HomeConfigured는 Main.dc.html을 그대로 잘라 쓰므로 Main과 같게 두려고 끈다."""
    light = doc(body)
    if keep_all:
        assert light.count(KEEP_ALL_FROM) == 1
        light = light.replace(KEEP_ALL_FROM, KEEP_ALL_TO)
    (OUT / f'{name}.dc.html').write_text(light, encoding='utf-8')
    (OUT / f'Dark{name}.dc.html').write_text(darken(light), encoding='utf-8')
    print('wrote', name, '+ Dark' + name)


def mark(size=28, radius=9, glyph=15):
    return (f'<div style="width: {size}px; height: {size}px; border-radius: {radius}px; background: {BRAND_GRAD}; '
            f'display: flex; align-items: center; justify-content: center; flex-shrink: 0;">'
            f'<svg width="{glyph}" height="{glyph}" viewBox="0 0 24 24" fill="#FFFFFF"><path d="{ARROW}"/></svg></div>')


# ══════════════ 공통 조각 ══════════════
def route_bar(cur=57.9, target=60):
    """홈 히어로의 항로 바. 채움 = 현재값, 깃발 = 목표. SPEC-COMPONENTS §26 식 그대로."""
    return (f'<div style="position: relative; height: 10px; border-radius: 99px; background: {C["TRACK"]}; overflow: visible;">'
            f'<div style="position: absolute; inset: 0 {100 - cur:.4g}% 0 0; border-radius: 99px; background: linear-gradient(90deg, #3556E6 0%, #6E6BEE 100%);"></div>'
            f'<div style="position: absolute; left: {target}%; top: -5px; width: 2px; height: 20px; border-radius: 2px; background: {C["INK"]};"></div></div>'
            f'<div style="position: relative; height: 15px; margin-top: 5px;">'
            f'<span style="position: absolute; left: 0; font-size: 11px; color: {C["INK3"]};">0%</span>'
            f'<span style="position: absolute; left: {target}%; transform: translateX(-50%); font-size: 11px; font-weight: 600; color: {C["INK"]}; white-space: nowrap;">내 목표 {target}%</span>'
            f'<span style="position: absolute; right: 0; font-size: 11px; color: {C["INK3"]};">100%</span></div>')


def dots(active, n=3):
    cells = []
    for i in range(n):
        if i == active:
            cells.append(f'<span style="width: 18px; height: 6px; border-radius: 99px; background: {C["BRAND"]};"></span>')
        else:
            cells.append(f'<span style="width: 6px; height: 6px; border-radius: 99px; background: {C["INPUT"]};"></span>')
    return f'<div style="display: flex; align-items: center; justify-content: center; gap: 6px;">{"".join(cells)}</div>'


def topline(left_text, right_text='건너뛰기'):
    return (f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px; height: 56px; margin-top: 8px; flex-shrink: 0;">'
            f'<div style="display: flex; align-items: center; gap: 8px;">{mark()}'
            f'<span style="font-size: 12px; font-weight: 500; color: {C["INK3"]};">{left_text}</span></div>'
            f'<span style="font-size: 13px; font-weight: 600; color: {C["BRAND"]};">{right_text}</span></div>')


def intro(step, eyebrow, sentence, art):
    return frame(
        f'<div style="flex: 1; min-height: 0; display: flex; flex-direction: column; padding: 0 20px; overflow: hidden;">'
        f'{topline(f"소개 {step} / 3")}'
        f'<div style="margin-top: 36px; display: flex; flex-direction: column; gap: 10px; flex-shrink: 0;">{art}</div>'
        f'<span style="display: block; margin-top: 30px; font-size: 11px; font-weight: 600; letter-spacing: 0.07em; color: {C["BRAND"]};">{eyebrow}</span>'
        f'<h1 style="margin: 8px 0 0; font-size: 23px; font-weight: 700; letter-spacing: -0.03em; line-height: 1.4; color: {C["INK"]}; text-wrap: pretty;">{sentence}</h1>'
        f'<div style="margin-top: auto; padding-bottom: 24px; display: flex; flex-direction: column; gap: 16px; flex-shrink: 0;">'
        f'{dots(step - 1)}{btn("다음", "primary", h=52, radius=14, size=16)}</div></div>')


# ══════════════ 소개 1 · 현재 위치 ══════════════
hero_excerpt = hero(
    eyebrow_row('현재 위치', badge('목표 안에서 순항 중', 'pos', 'check'))
    + f'<div style="display: flex; align-items: flex-end; justify-content: space-between; gap: 10px; margin-top: 8px;">'
    + display_num('57.9')
    + f'<div style="display: flex; flex-direction: column; align-items: flex-end; gap: 1px; padding-bottom: 4px;">'
    f'<span style="font-size: 11px; font-weight: 500; color: {C["INK3"]};">목표까지</span>'
    f'<span style="font-size: 14px; font-weight: 600; color: {C["POS"]};">2.1%p 여유</span></div></div>'
    + f'<div style="display: flex; align-items: baseline; justify-content: space-between; gap: 10px; margin-top: 5px;">'
    f'<span style="font-size: 13px; font-weight: 500; color: {C["INK2"]};">월급 대비 이번 달 예상 소비</span>'
    f'<span style="display: inline-flex; align-items: center; gap: 4px; flex-shrink: 0;">'
    f'<span style="font-size: 11px; font-weight: 500; color: {C["INK4"]};">순자산 대비</span>'
    f'<span style="font-size: 13px; font-weight: 600; letter-spacing: -0.02em; color: {C["INK2"]};">2.2%</span></span></div>'
    + f'<div style="margin-top: 15px;">{route_bar()}</div>')

w('IntroPosition', intro(1, '현재 위치', '이번 달 소비가 월급의 몇 %인지<br>숫자 하나로 봅니다.', hero_excerpt))


# ══════════════ 소개 2 · 항로 ══════════════
route_card = card(
    eyebrow_row('항로', f'<span style="font-size: 12px; font-weight: 600; color: {C["INK"]};">현재 57.9% · 목표 60%</span>')
    + f'<div style="margin-top: 16px;">{route_bar()}</div>')
guide_card = guidance('warn', '다음 안내', '카드 할부 금리 14.5%부터 줄여보세요',
                      '고금리 부채는 자산이 자라는 속도를 가장 크게 낮춰요.', '상환 전략 보기')

w('IntroRoute', intro(2, '항로', '목표까지 얼마나 남았는지,<br>지금 무엇을 할지 알려줍니다.', route_card + guide_card))


# ══════════════ 소개 3 · 목적지 ══════════════
def dest_row(name, eta, pct, color, last=False):
    bb = '' if last else f'border-bottom: 1px solid {C["LINE_ROW"]};'
    return (f'<div style="display: flex; align-items: center; gap: 12px; height: 62px; {bb}">'
            f'{ring(pct, color, 44, f"{pct}%")}'
            f'<div style="display: flex; flex-direction: column; gap: 3px; flex: 1; min-width: 0;">'
            f'<span style="font-size: 14px; font-weight: 600; letter-spacing: -0.015em; color: {C["INK"]};">{name}</span>'
            f'<span style="font-size: 12px; color: {C["INK3"]};">{eta}</span></div>'
            f'{icon("right", 16, C["INK4"], 2)}</div>')


# 수치는 v3 샘플(sample-data.json derived.goalEta)과 Goals.dc.html의 링 값 그대로.
dest_card = card(
    eyebrow_row('목적지', f'<span style="font-size: 12px; font-weight: 500; color: {C["INK3"]};">도착 예상</span>')
    + f'<div style="margin-top: 4px;">'
    + dest_row('비상금 6개월', '2027년 11월 · 월 35만원 적립', 68, ASSET['현금성'])
    + dest_row('투자 계좌 5,000만원', '2032년 6월 · 연 5.0% 가정', 42, C['VIO'])
    + dest_row('신용대출 완제', '2030년 10월 · 상환 계획 반영', 31, C['WARN'], last=True)
    + '</div>', pad='12px 14px 2px')

w('IntroDestination', intro(3, '목적지', '비상금 · 투자 · 상환,<br>언제 도착할지 날짜로 알려줍니다.', dest_card))


# ══════════════ 구성 · 홈에 무엇을 둘까요? ══════════════
def checkbox(on):
    if on:
        return (f'<div style="width: 22px; height: 22px; border-radius: 7px; background: {C["BRAND"]}; display: flex; '
                f'align-items: center; justify-content: center; flex-shrink: 0;">{icon("check", 14, "#FFFFFF", 3)}</div>')
    return (f'<div style="width: 22px; height: 22px; border-radius: 7px; background: {C["SURF"]}; '
            f'border: 1.5px solid {C["INPUT"]}; flex-shrink: 0;"></div>')


def _ln(w_, top, col=None, left=8, h=3):
    col = col or C["INPUT"]
    return (f'<span style="position: absolute; left: {left}px; top: {top}px; width: {w_}px; height: {h}px; '
            f'border-radius: 99px; background: {col};"></span>')


def thumb(kind):
    """카드 축소 미리보기 44×30. 글자 없이 형태만 — 무엇인지 알아보게 하는 용도."""
    if kind == 'guide':
        inner = (f'<span style="position: absolute; left: 0; top: 0; bottom: 0; width: 3px; background: {C["WARN_RULE"]};"></span>'
                 + _ln(22, 9, C["INK4"], 10) + _ln(14, 17, None, 10))
    elif kind == 'goal':
        inner = (f'<span style="position: absolute; left: 7px; top: 8px; width: 14px; height: 14px; border-radius: 99px; '
                 f'background: conic-gradient({C["VIO"]} 0% 68%, {C["INPUT"]} 68% 100%);"></span>'
                 f'<span style="position: absolute; left: 10.5px; top: 11.5px; width: 7px; height: 7px; border-radius: 99px; background: {C["INSET"]};"></span>'
                 + _ln(12, 10, C["INK4"], 26) + _ln(9, 17, None, 26))
    elif kind == 'limit':
        inner = _ln(16, 7, C["INK4"]) + _ln(28, 17, C["TRACK"], 8, 5) + _ln(15, 17, C["VIO"], 8, 5)
    elif kind == 'peer':
        inner = (_ln(28, 8, C["TRACK"], 8, 5) + _ln(17, 8, C["BRAND"], 8, 5)
                 + _ln(28, 17, C["TRACK"], 8, 5) + _ln(19, 17, C["VIO_LINE"], 8, 5))
    elif kind == 'rows':
        inner = (_ln(12, 6, C["INK4"]) + _ln(8, 6, C["INK4"], 28) + _ln(12, 13.5) + _ln(8, 13.5, None, 28)
                 + _ln(12, 21) + _ln(8, 21, None, 28))
    elif kind == 'line':
        inner = _ln(14, 13.5, C["INK4"]) + _ln(12, 13.5, C["INK"], 24)
    else:
        raise KeyError(kind)
    return (f'<div style="width: 44px; height: 30px; border-radius: 7px; background: {C["INSET"]}; border: 1px solid {C["LINE_SOFT"]}; '
            f'flex-shrink: 0; overflow: hidden; position: relative;">{inner}</div>')


def pick_row(kind, name, desc, on, last=False):
    bb = '' if last else f'border-bottom: 1px solid {C["LINE_ROW"]};'
    return (f'<div style="display: flex; align-items: center; gap: 12px; height: 52px; {bb}">'
            f'{checkbox(on)}{thumb(kind)}'
            f'<div style="display: flex; flex-direction: column; gap: 2px; flex: 1; min-width: 0;">'
            f'<span style="font-size: 14px; font-weight: 600; letter-spacing: -0.01em; color: {C["INK"]};">{name}</span>'
            f'<span style="font-size: 11.5px; color: {C["INK3"]}; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">{desc}</span></div></div>')


# 이 시안의 선택: 기본값(v3 홈)에서 대표 목적지·또래·순자산 대비를 빼고 새 카드 둘을 넣은 상태 → 4 / 5.
PICKS = [
    ('guide', '다음 안내', '지금 할 일 한 가지', True),
    ('goal', '대표 목적지', '가장 앞선 목적지와 도착 예상', False),
    ('limit', '이번 달 한도', '하루 한도와 남은 금액', True),
    ('peer', '또래와 내 페이스', '내가 넣은 또래 기준과 내 소비율 비교', False),
    ('rows', '순자산 대비 소비', '가진 자산에 비해 얼마나 쓰는지', False),
    ('line', '순자산 한 줄', '지금 순자산과 다음 목표 금액', True),
    ('line', '상환 계획 한 줄', '완제 예정일과 이번 달 상환액', True),
]
picked = sum(1 for p in PICKS if p[3])
count_lbl = (f'<span style="font-size: 12px; font-weight: 600; color: {C["INK3"]};">{picked} / 5 선택</span>')
pick_rows = ''.join(pick_row(k, n, d, o, last=(i == len(PICKS) - 1)) for i, (k, n, d, o) in enumerate(PICKS))

fixed_row = card(
    f'<div style="display: flex; align-items: center; gap: 10px; height: 48px;">'
    f'{icon("lock", 16, C["INK4"], 1.9)}'
    f'<span style="font-size: 13.5px; font-weight: 600; color: {C["INK"]};">현재 위치 · 월급 대비 소비율</span>'
    f'<span style="margin-left: auto;">{badge("고정", "mute")}</span></div>', pad='0 14px')

stock_card = card(
    f'<div style="display: flex; align-items: flex-start; gap: 12px;">'
    f'<div style="display: flex; flex-direction: column; gap: 3px; flex: 1; min-width: 0;">'
    f'<span style="font-size: 14px; font-weight: 600; color: {C["INK"]};">주식도 볼까요?</span>'
    f'<span style="font-size: 12px; line-height: 1.45; color: {C["INK3"]};">보유·관심 종목을 내 항로에 연결해요. 켜면 주식 요약 카드와 주식 탭이 생겨요.</span></div>'
    f'{toggle(False)}</div>')

w('HomeSetup', frame(
    f'<div style="flex: 1; min-height: 0; display: flex; flex-direction: column; padding: 0 20px; overflow: hidden;">'
    f'{topline("홈 구성")}'
    f'<h1 style="margin: 10px 0 0; font-size: 22px; font-weight: 700; letter-spacing: -0.03em; line-height: 1.35; color: {C["INK"]};">홈에 무엇을 둘까요?</h1>'
    f'<p style="margin: 6px 0 0; font-size: 13.5px; line-height: 1.5; color: {C["INK2"]};">소비율은 늘 맨 위에 있어요.<br>그 아래에 둘 카드를 5개까지 골라 주세요.</p>'
    f'<div style="margin-top: 12px;">{fixed_row}</div>'
    f'<div style="margin-top: 12px;">{section_head("홈 카드", right=count_lbl)}</div>'
    f'<div style="margin-top: 8px;">{card(pick_rows, pad="0 14px")}</div>'
    f'<div style="margin-top: 10px;">{stock_card}</div>'
    f'<div style="margin-top: auto; padding-bottom: 24px; display: flex; flex-direction: column; gap: 8px; flex-shrink: 0;">'
    f'{btn("이 구성으로 시작", "primary", h=52, radius=14, size=16)}'
    f'<p style="margin: 0; text-align: center; font-size: 11.5px; line-height: 1.5; color: {C["INK3"]};">언제든 설정 › 홈 구성에서 바꿀 수 있어요.</p></div></div>'))


# ══════════════ 홈 · 구성 반영 ══════════════
def cut(text, start, end):
    """Main.dc.html에서 start로 시작해 end 직전까지를 잘라 온다. 마커는 정확히 한 번 있어야 한다."""
    assert text.count(start) == 1, f'start marker ×{text.count(start)}: {start[:60]}'
    i = text.index(start)
    j = text.index(end, i)
    return text[i:j]


main_src = (OUT / 'Main.dc.html').read_text(encoding='utf-8')
M_HEADER = '<div style="display: flex; flex-direction: column; gap: 6px; padding: 12px 16px 10px; flex-shrink: 0;">'
M_HERO = '<div style="background: #FFFFFF; border: 1px solid #E3E8F1; border-radius: 20px; padding: 16px;'
M_GUIDE = '<div style="display: flex; gap: 12px; background: #FFFFFF; border: 1px solid #E3E8F1; border-left: 3px solid #DE8A2A;'
M_GOAL = '<div style="display: flex; align-items: center; gap: 12px; background: #FFFFFF; border: 1px solid #E3E8F1; border-radius: 18px; padding: 13px;'
M_LIMIT = '<div style="background: #FFFFFF; border: 1px solid #E3E8F1; border-radius: 18px; padding: 12px 14px; flex-shrink: 0;">'
M_CONTENT = '<div style="flex: 1; min-height: 0; display: flex; flex-direction: column; gap: 9px; padding: 0 14px; overflow: hidden;">'
M_NAV = '<div style="display: flex; align-items: flex-start; justify-content: space-between; gap: 2px; height: 66px;'

header = cut(main_src, M_HEADER, M_CONTENT).rstrip()
hero_block = cut(main_src, M_HERO, M_GUIDE).rstrip()
guide_block = cut(main_src, M_GUIDE, M_GOAL).rstrip()
limit_block = cut(main_src, M_LIMIT, M_NAV).rstrip()
assert limit_block.endswith('</div>')
limit_block = limit_block[:limit_block.rfind('</div>')].rstrip()   # 콘텐츠 컨테이너의 닫는 태그는 뺀다
assert hero_block.count('57.9') == 1 and '소비 기록하기' in hero_block


def line_card(label, sub, value):
    return card(
        f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 10px; height: 46px;">'
        f'<div style="display: flex; flex-direction: column; gap: 2px; min-width: 0;">'
        f'<span style="font-size: 13.5px; font-weight: 600; color: {C["INK"]};">{label}</span>'
        f'<span style="font-size: 11.5px; color: {C["INK3"]}; white-space: nowrap;">{sub}</span></div>'
        f'<div style="display: flex; align-items: center; gap: 8px; flex-shrink: 0;">'
        f'<span style="font-size: 15px; font-weight: 600; letter-spacing: -0.02em; color: {C["INK"]};">{value}</span>'
        f'{icon("right", 16, C["INK4"], 2)}</div></div>', pad='4px 14px')


# 순자산 9,350만원 · 1억 도착 2027-02 · 완제 2036-04 · 월 상환 92만원 — 전부 sample-data.json derived 값.
networth_card = line_card('순자산', '1억까지 650만원 · 2027년 2월 도착 예상', '9,350만원')
payoff_card = line_card('상환 계획', '완제 예상 2036년 4월 · 고금리 우선', '이번 달 92만원')

w('HomeConfigured', frame(
    f'\n  {header}\n\n'
    f'  <div style="flex: 1; min-height: 0; display: flex; flex-direction: column; gap: 8px; padding: 0 14px; overflow: hidden;">\n\n'
    f'    {hero_block}\n\n    {guide_block}\n\n    {limit_block}\n\n    {networth_card}\n\n    {payoff_card}\n\n  </div>\n\n'
    f'  {bottomnav(0)}\n'), keep_all=False)
