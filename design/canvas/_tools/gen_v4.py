# -*- coding: utf-8 -*-
"""v4 · 1단계 아트보드 — 첫 실행 소개 3장 · 홈 구성(첫 실행 · 주식 켠 변형 · 설정에서 들어온 편집) · 설정 시트의 `홈 구성 ›` 행 · 구성값을 반영한 홈.

plan/v4-stocks.md §3(첫 실행 흐름)·§7(1단계)·§10. 라이트를 만들고 같은 자리에서 darken()으로
다크 짝까지 쓴다. 홈 아트보드의 헤더·히어로·다음 안내·이번 달 한도는 Main.dc.html에서 그대로
잘라 온다(v3 홈과 1px도 다르지 않아야 하므로 다시 그리지 않는다).

홈 구성 목록과 구성 반영 홈에는 v5 계획(§3-1 · §3-5 · §9-12)의 `이번 달 달력` 카드가 들어간다 — 달력 조각은 gen_calendar 에서 가져온다
(Main 에는 달력이 없어 잘라 올 마커가 없다. HomeCalendarStrip 과 같은 calendar_card(False) 를 쓴다).

    python3 gen_v4.py            # 8 + 8장 → ../
"""
import pathlib
from gen_common import *
from darken import darken
from gen_calendar import calendar_card, calendar_thumb

OUT = pathlib.Path(__file__).resolve().parent.parent
V4 = ['IntroPosition', 'IntroRoute', 'IntroDestination', 'HomeSetup', 'HomeSetupStocksOn', 'SettingsHomeEntry', 'HomeLayoutEdit', 'HomeConfigured']

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
    (OUT / f'Dark{name}.dc.html').write_text(darken(light, name), encoding='utf-8')
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

w('IntroRoute', intro(2, '항로', '목표까지 얼마나 남았는지,<br>지금 무엇을 하면 되는지 알려줍니다.', route_card + guide_card))


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


# 홈 구성 목록의 왼쪽 그림 — 카드 축소 미리보기(막대 몇 개)는 서로 구별이 안 돼 아이콘 하나로 바꿨다(2026-09-21 사용자 선택 · 전·후 비교 뒤).
CARD_ICON = {'calendar': 'cal', 'guide': 'arrowur', 'limit': 'sliders', 'goal': 'target', 'peer': 'users',
             'ratio': 'chart', 'networth': 'wallet', 'payoff': 'bank', 'stock': 'trend'}


def thumb(cid):
    """카드 아이콘 32 × 32(회색 바탕 · radius 10 · 아이콘 17px ink-2). 이름을 읽기 전에 무엇인지 보이게 한다."""
    return (f'<div style="width: 32px; height: 32px; border-radius: 10px; background: {C["INSET"]}; flex-shrink: 0; display: flex; '
            f'align-items: center; justify-content: center;">{icon(CARD_ICON[cid], 17, C["INK2"], 1.9)}</div>')


def pick_row(cid, name, desc, on, last=False):
    bb = '' if last else f'border-bottom: 1px solid {C["LINE_ROW"]};'
    return (f'<div style="display: flex; align-items: center; gap: 12px; height: 48px; {bb}">'
            f'{checkbox(on)}{thumb(cid)}'
            f'<div style="display: flex; flex-direction: column; gap: 2px; flex: 1; min-width: 0;">'
            f'<span style="font-size: 14px; font-weight: 600; letter-spacing: -0.01em; color: {C["INK"]};">{name}</span>'
            f'<span style="font-size: 11.5px; color: {C["INK3"]}; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">{desc}</span></div></div>')


# 목록 순서 = 기본 배열(v5 §3-1): 이번 달 달력 · 다음 안내 · 이번 달 한도 · 대표 목적지 · 또래와 내 페이스 → 순자산 대비 소비(목록에 남고 기본 꺼짐)
# → 새 카드 둘 → (주식 켰을 때만) 주식 요약. 달력도 상한 5에 센다.
CARDS = [
    ('calendar', 'calendar', '이번 달 달력', '날마다 쓴 금액, 날짜를 눌러 바로 기록'),
    ('guide', 'guide', '다음 안내', '지금 할 일 한 가지'),
    ('limit', 'limit', '이번 달 한도', '하루 한도와 남은 한도'),
    ('goal', 'goal', '대표 목적지', '가장 앞선 목적지와 도착 예상'),
    ('peer', 'peer', '또래와 내 페이스', '내가 넣은 또래 기준과 내 소비율 비교'),
    # 홈 맨 아래 세 줄 카드(순자산 대비 소비 · 자산 종합 점수 · N년 뒤 순자산)를 한 카드로 묶어 켜고 끈다 — 이름 `자산 한눈에`(2026-09-21 사용자 결정)
    ('ratio', 'rows', '자산 한눈에', '순자산 대비 소비 · 자산 점수 · 10년 뒤 순자산'),
    ('networth', 'line', '순자산 한 줄', '지금 순자산과 다음 목표 금액'),
    ('payoff', 'line', '상환 계획 한 줄', '완제 예정일과 이번 달 상환액'),
]
STOCK_CARD = ('stock', 'stock', '주식 요약', '보유 평가액과 관심 종목 수, 기준일')
# 이 시안의 선택: 달력(기본 켜짐) · 다음 안내 · 이번 달 한도 + 새 카드 둘 → 5 / 5. HomeConfigured 가 이 구성의 결과.
ON_SETUP = {'calendar', 'guide', 'limit', 'networth', 'payoff'}
# 주식 켠 변형: HomeStocksCard(달력 · 다음 안내 · 주식 요약 · 이번 달 한도 · 순자산)와 같은 구성 → 5 / 5.
ON_STOCKS = {'calendar', 'guide', 'limit', 'networth', 'stock'}
# 설정에서 들어와 달력을 끈 상태 → 4 / 5.
ON_EDIT = ON_SETUP - {'calendar'}

fixed_row = card(
    f'<div style="display: flex; align-items: center; gap: 10px; height: 48px;">'
    f'{icon("lock", 16, C["INK4"], 1.9)}'
    f'<span style="font-size: 13.5px; font-weight: 600; color: {C["INK"]};">현재 위치 · 월급 대비 소비율</span>'
    f'<span style="margin-left: auto;">{badge("고정", "mute")}</span></div>', pad='0 14px')


def stock_card(on):
    return card(
        f'<div style="display: flex; align-items: flex-start; gap: 12px;">'
        f'<div style="display: flex; flex-direction: column; gap: 3px; flex: 1; min-width: 0;">'
        f'<span style="font-size: 14px; font-weight: 600; color: {C["INK"]};">주식도 볼까요?</span>'
        f'<span style="font-size: 12px; line-height: 1.45; color: {C["INK3"]};">보유·관심 종목을 내 항로에 연결해요. 켜면 주식 요약 카드와 주식 탭이 생겨요.</span></div>'
        f'{toggle(on)}</div>')


LEAD = (f'<p style="margin: 6px 0 0; font-size: 13.5px; line-height: 1.5; color: {C["INK2"]};">소비율은 늘 맨 위에 있어요.<br>'
        f'그 아래에 둘 카드를 5개까지 골라 주세요.</p>')


def setup_screen(top, head, on, stocks, footer, after_list='', scroll=0):
    """홈 구성 화면 세 장의 공통 틀 — 머리줄(고정) · 목록(스크롤 구역) · 아래 버튼(고정).
    scroll = 위로 밀어 올린 거리(px). 주식을 켜면 9행이라 844 안에 다 안 들어가 제목 · 안내 문장이 위로 넘어간 상태로 그린다."""
    cards = CARDS + ([STOCK_CARD] if stocks else [])
    picked = sum(1 for c in cards if c[0] in on)
    count_lbl = f'<span style="font-size: 12px; font-weight: 600; color: {C["INK3"]}; white-space: nowrap; flex-shrink: 0;">{picked} / 5 선택</span>'
    rows = ''.join(pick_row(cid, n, d, cid in on, last=(i == len(cards) - 1)) for i, (cid, k, n, d) in enumerate(cards))
    return frame(
        f'<div style="padding: 0 20px; flex-shrink: 0;">{top}</div>'
        f'<div style="flex: 1; min-height: 0; overflow: hidden; padding: 0 20px;">'
        f'<div style="display: flex; flex-direction: column; margin-top: {-scroll}px;">'
        f'{head}'
        f'<div style="margin-top: 12px;">{fixed_row}</div>'
        f'<div style="margin-top: 12px;">{section_head("홈 카드", right=count_lbl)}</div>'
        f'<div style="margin-top: 8px;">{card(rows, pad="0 14px")}</div>'
        f'{after_list}'
        f'<div style="margin-top: 10px;">{stock_card(stocks)}</div></div></div>'
        f'<div style="padding: 8px 20px 24px; display: flex; flex-direction: column; gap: 8px; flex-shrink: 0;">{footer}</div>')


# 위 여백 6px — 10px 이면 HomeSetup 맨 아래 `주식도 볼까요?` 카드의 아랫단 3px 이 고정 버튼 구역 위에서 잘린다(세로 예산).
SETUP_H1 = (f'<h1 style="margin: 6px 0 0; font-size: 22px; font-weight: 700; letter-spacing: -0.03em; line-height: 1.35; color: {C["INK"]};">홈에 무엇을 둘까요?</h1>')
SETUP_FOOT = (f'{btn("이 구성으로 시작", "primary", h=52, radius=14, size=16)}'
              f'<p style="margin: 0; text-align: center; font-size: 11.5px; line-height: 1.5; color: {C["INK3"]};">언제든 설정 › 홈 구성에서 바꿀 수 있어요.</p>')

# 첫 실행 · 주식 꺼짐(기본)
w('HomeSetup', setup_screen(topline("홈 구성"), SETUP_H1 + LEAD, ON_SETUP, False, SETUP_FOOT))

# 첫 실행 · `주식도 볼까요?`를 켠 순간 — 목록 끝에 `주식 요약` 행이 생긴다. 9행이라 제목 · 안내 문장이 위로 넘어간 스크롤 상태.
w('HomeSetupStocksOn', setup_screen(topline("홈 구성"), SETUP_H1 + LEAD, ON_STOCKS, True, SETUP_FOOT, scroll=83))

# 기존 사용자 · 설정 › 홈 구성으로 들어온 같은 목록 — 첫 실행이 아니라 `건너뛰기` · `이 구성으로 시작` 대신 닫기(×) · 저장.
edit_top = (f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px; height: 56px; margin-top: 8px;">'
            f'<h1 style="margin: 0; font-size: 20px; font-weight: 700; letter-spacing: -0.03em; color: {C["INK"]};">홈 구성</h1>'
            f'<div style="width: 36px; height: 36px; border-radius: 11px; background: {C["INSET"]}; display: flex; align-items: center; '
            f'justify-content: center; flex-shrink: 0;">{icon("x", 17, C["INK2"], 2.2)}</div></div>')
# 달력을 끈 상태에서만 목록 아래에 나오는 한 줄(v5 §7 '달력이 싫은 사용자'). 의미색 없이 잉크 단계만.
CAL_OFF_NOTE = (f'<p style="margin: 8px 2px 0; font-size: 11.5px; line-height: 1.5; color: {C["INK3"]};">'
                f'달력을 꺼도 소비 기록하기는 오늘 기록을 열어요. 확인할 내용은 소비 탭 알림에서 볼 수 있어요.</p>')
w('HomeLayoutEdit', setup_screen(edit_top, LEAD.replace('margin: 6px 0 0;', 'margin: 0;'), ON_EDIT, False,
                                 btn("저장", "primary", h=52, radius=14, size=16), after_list=CAL_OFF_NOTE))


# ══════════════ 설정 시트 · `홈 구성 ›` 행 ══════════════
# ProfileDialog(gen_modals.py)와 같은 시트 · 같은 구역을 맨 아래까지 내린 상태로 그린다 — `추가 설정`과 `데이터` 사이에 `홈 화면` 구역.
# 주식을 끈 사용자라 주식 행은 없다. gen_modals 는 import 하면 12장을 다시 쓰므로 구역 틀만 여기에 둔다.
def s_group(label, inner):
    return (f'<div style="flex-shrink: 0;"><div style="display: flex; align-items: baseline; justify-content: space-between; gap: 8px; margin-bottom: 9px;">'
            f'<span style="font-size: 11px; font-weight: 600; letter-spacing: 0.07em; color: {C["INK3"]};">{label}</span></div>{inner}</div>')


def nav_row(label, meta):
    return (f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px; height: 48px; '
            f'padding: 0 13px; border-radius: 12px; background: {C["INSET"]};">'
            f'<span style="font-size: 13.5px; font-weight: 600; color: {C["INK"]}; white-space: nowrap;">{label}</span>'
            f'<div style="display: flex; align-items: center; gap: 8px; flex-shrink: 0;">'
            f'<span style="font-size: 12px; color: {C["INK3"]}; white-space: nowrap;">{meta}</span>{icon("right", 16, C["INK4"], 2)}</div></div>')


settings_body = (
    s_group('소비 목표',
            f'<div style="padding: 13px; background: {C["INSET"]}; border-radius: 14px;">'
            f'<div style="display: flex; align-items: baseline; justify-content: space-between; gap: 8px;">'
            f'<span style="font-size: 13px; color: {C["INK2"]};">급여의 얼마까지 쓸까요?</span>'
            f'<span style="font-size: 22px; font-weight: 700; letter-spacing: -0.03em; color: {C["INK"]};">60<span style="font-size: 14px; font-weight: 600; color: {C["INK2"]};">%</span></span></div>'
            f'<div style="margin-top: 9px;">{slider(60)}</div>'
            f'<div style="display: flex; align-items: center; margin-top: 4px;">'
            f'<span style="flex: 1; font-size: 11px; color: {C["INK4"]};">0%</span>'
            f'<span style="font-size: 11.5px; font-weight: 600; color: {C["INK"]}; white-space: nowrap;">월 216만원까지</span>'
            f'<span style="flex: 1; text-align: right; font-size: 11px; color: {C["INK4"]};">100%</span></div>'
            # ProfileDialog(gen_modals.py)의 같은 카드와 글자 그대로 — 아래 맞춤이라 시트 머리 아래 잘린 띠에는 이 상자의 빈 바탕만 보인다.
            f'<div style="margin-top: 11px;">{note("60%는 통계 평균이나 정답이 아니라 <b style=font-weight:600>바꿔도 되는 계획 시작값</b>입니다. 0%로 두어도 그대로 유지돼요.", "mute")}</div></div>')
    + s_group('추가 설정',
              f'<div style="display: flex; gap: 10px;">{field("부수입", "30", "만원", optional=True)}'
              f'{field("총자산", "1억 8,210", "만원", state="readonly")}</div>'
              f'<div style="display: flex; gap: 10px; margin-top: 12px;">{field("총부채", "8,860", "만원", state="readonly")}'
              f'{field("기대수익률", "2.4", "%", optional=True, w=124)}</div>'
              f'<div style="margin-top: 9px;">{note("자산 5건·부채 4건을 따로 입력해 두어서 총자산과 총부채는 그 합계로 표시됩니다. 자산·부채 화면에서 고칠 수 있어요.", "mute", "lock")}</div>'
              f'<div style="margin-top: 12px;"><div style="font-size: 12px; font-weight: 600; color: {C["INK2"]}; margin-bottom: 7px;">테마</div>'
              f'{segmented(["시스템", "라이트", "다크"], 0)}</div>')
    + s_group('홈 화면', nav_row('홈 구성', '카드 5개'))
    + s_group('데이터', f'<div style="display: flex; gap: 8px;">'
                        f'{btn("백업 내보내기", "secondary", "download", h=44).replace("width: 100%;", "flex: 1;")}'
                        f'{btn("불러오기", "secondary", "upload", h=44).replace("width: 100%;", "flex: 1;")}</div>'
                        f'<div style="margin-top: 8px;">{btn("모두 지우고 새로 시작", "danger", h=44)}</div>'))
settings_sheet = sheet('내 수치 입력', '급여와 소비 목표만 있으면 홈이 계산됩니다. 나머지는 언제든 채워도 돼요.',
                       settings_body, sheet_footer('취소', '저장'), body_pb=14)
# 맨 아래까지 스크롤한 상태: 본문을 아래 맞춤으로 두면 넘친 윗부분(소비 목표 구역)이 시트 머리 아래로 잘린다.
BODY_FROM = 'padding: 14px 18px 14px; display: flex; flex-direction: column; gap: 15px;">'
assert settings_sheet.count(BODY_FROM) == 1
settings_sheet = settings_sheet.replace(BODY_FROM, BODY_FROM.replace('flex-direction: column;', 'flex-direction: column; justify-content: flex-end;'))
w('SettingsHomeEntry', settings_sheet)


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
# 달력 카드 — Main 에는 아직 달력이 없어 잘라 올 마커(M_CAL)가 없다. HomeCalendarStrip 과 같은 접힘 카드를 공용 조각으로 만든다.
# gen_v4_stocks · gen_v5 가 s1.calendar_block 으로 같은 카드를 가져다 쓸 수 있다.
calendar_block = calendar_card(False)
assert calendar_block.count('이번 달 달력') == 1 and '펼치기' in calendar_block


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
    f'    {hero_block}\n\n    {calendar_block}\n\n    {guide_block}\n\n    {limit_block}\n\n    {networth_card}\n\n    {payoff_card}\n\n  </div>\n\n'
    f'  {bottomnav(0)}\n'), keep_all=False)
