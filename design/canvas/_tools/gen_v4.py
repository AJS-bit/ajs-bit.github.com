# -*- coding: utf-8 -*-
"""v4 · 1단계 아트보드 — 첫 실행 소개 3장 · 홈 구성(첫 실행 · 주식 알림 켠 변형 · 설정에서 들어온 편집) · 설정 시트의 `홈 구성` 행 · 첫 실행 뒤 홈.

plan/v4-stocks.md §3(첫 실행 흐름)·§7(1단계)·§10. 라이트를 만들고 같은 자리에서 darken()으로
다크 짝까지 쓴다. 홈 아트보드의 머리줄·히어로·다음 안내·이번 달 한도는 Main.dc.html에서 그대로
잘라 온다(Main 과 1px도 다르지 않아야 하므로 다시 그리지 않는다).

홈 구성 목록과 홈에는 v5 계획(§3-1 · §3-5 · §9-12)의 달력 카드가 들어간다 — 달력 조각은 gen_calendar 에서 가져온다
(Main 에는 달력이 없어 잘라 올 마커가 없다). 2026-09-30부터 홈의 달력은 펼친 월 달력이 기본이라 HomeDefaultScroll 과 같은
calendar_card(HOME_EXPANDED) 를 쓴다(머리줄 `‹ 2026년 9월 ›` · 「접기 ▴」 — 접은 7일 줄 「이번 달 소비 기록」은 HomeCalendarStrip).

2026-09-26(사용성 140건 · 앱 v5-stage1 a724aac 이 기준):
- 소개 1 = 달력 예시 카드 + 간단한 위치 카드 두 장 · h1 `쓴 돈을 달력에 숫자만 적으면 / 월급의 몇 %를 썼는지 바로 보여요` · 자물쇠 한 줄(폰 문구) — first-run-13.
  소개 2 · 3 은 해요체 · `소비 목표` · `상환 계획 보기 ›` · `매달 35만원` · `신용대출 다 갚기`.
- 홈 구성 = 첫 실행에 남는다 · 버튼 `다음` · 처음 체크는 다음 안내 · 이번 달 한도 · 순자산 한 줄(부채 카드 미리 체크 안 함 · 3 / 4) ·
  고정 행 `이번 달 소비` / `이번 달 소비 기록` · 설명은 두 줄까지 줄바꿈(앱) · 4 / 4 이면 안 고른 행이 흐려짐 ·
  주식 카드는 `주식 화면이 나오면 알려 드릴까요?`(준비 중 · 목록에 주식 요약 행 없음).
- 설정 시트 = D5 의 `설정`(내 수치 · 화면 · 홈 화면 · 기기 알림 · 도움말 · 데이터 · 닫기).
- HomeConfigured = `내 데이터로 시작` 뒤 첫 홈(빈 히어로 · 시작 순서 · 한도 기준 없음 · 순자산 —) — 첫 체크 세 카드. 시안 사용자의 캐논 홈은 home_canon().

    python3 gen_v4.py            # 8 + 8장 → ../
"""
import pathlib
import brand_mark
from gen_common import *
from darken import darken
from gen_calendar import calendar_card, calendar_thumb, cell, day_state, NO_RECORD, TODAY, WD, HOME_EXPANDED

OUT = pathlib.Path(__file__).resolve().parent.parent
V4 = ['IntroPosition', 'IntroRoute', 'IntroDestination', 'HomeSetup', 'HomeSetupStocksOn', 'SettingsHomeEntry', 'HomeLayoutEdit', 'HomeConfigured']

BRAND_GRAD = 'linear-gradient(140deg, #3556E6 0%, #7A3FE4 100%)'
KA = ' word-break: keep-all;'


KEEP_ALL_FROM = '-webkit-font-smoothing: antialiased; }'
KEEP_ALL_TO = '-webkit-font-smoothing: antialiased; word-break: keep-all; }'


def w(name, body, keep_all=True):
    """keep_all — 한국어가 단어 중간에서 줄바꿈되지 않게 body에 word-break: keep-all을 넣는다."""
    light = doc(body)
    if keep_all:
        assert light.count(KEEP_ALL_FROM) == 1
        light = light.replace(KEEP_ALL_FROM, KEEP_ALL_TO)
    (OUT / f'{name}.dc.html').write_text(light, encoding='utf-8')
    (OUT / f'Dark{name}.dc.html').write_text(darken(light, name), encoding='utf-8')
    print('wrote', name, '+ Dark' + name)


def mark(size=32, radius=10):   # brand_mark.py 규격(2026-09-30) — 하루가 쌓인 길 · 네모의 54%(같은 날 둘째 결정 · 앱 아이콘과 같은 비율)
    return brand_mark.tile(size, radius, BRAND_GRAD)


# ══════════════ 공통 조각 ══════════════
def route_bar(cur=31.1, target=60, fill=True):
    """홈 히어로의 항로 바. 채움 = 지금까지 쓴 돈 ÷ 월급(2026-09-24 — 전에는 월말 예상), 깃발 = 소비 목표. SPEC-COMPONENTS §26 식 그대로.
    fill=False = 기록이 없는 빈 히어로(채움 없음)."""
    fl = (f'<div style="position: absolute; inset: 0 {100 - cur:.4g}% 0 0; border-radius: 99px; background: linear-gradient(90deg, #3556E6 0%, #6E6BEE 100%);"></div>'
          if fill else '')
    return (f'<div style="position: relative; height: 10px; border-radius: 99px; background: {C["TRACK"]}; overflow: visible;">{fl}'
            f'<div style="position: absolute; left: {target}%; top: -5px; width: 2px; height: 20px; border-radius: 2px; background: {C["INK"]};"></div></div>'
            f'<div style="position: relative; height: 15px; margin-top: 5px;">'
            f'<span style="position: absolute; left: 0; font-size: 11px; color: {C["INK3"]};">0%</span>'
            f'<span style="position: absolute; left: {target}%; transform: translateX(-50%); font-size: 11px; font-weight: 600; color: {C["INK"]}; white-space: nowrap;">소비 목표 {target}%</span>'
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
    right = f'<span style="font-size: 13px; font-weight: 600; color: {C["BRAND"]};">{right_text}</span>' if right_text else ''
    return (f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px; height: 56px; margin-top: 8px; flex-shrink: 0;">'
            f'<div style="display: flex; align-items: center; gap: 8px;">{mark()}'
            f'<span style="font-size: 12px; font-weight: 500; color: {C["INK3"]};">{left_text}</span></div>{right}</div>')


def intro(step, eyebrow, sentence, art, note_html=''):
    return frame(
        f'<div style="flex: 1; min-height: 0; display: flex; flex-direction: column; padding: 0 20px; overflow: hidden;">'
        f'{topline(f"소개 {step} / 3")}'
        f'<div style="margin-top: 36px; display: flex; flex-direction: column; gap: 10px; flex-shrink: 0;">{art}</div>'
        f'<span style="display: block; margin-top: 30px; font-size: 11px; font-weight: 600; letter-spacing: 0.07em; color: {C["BRAND"]};">{eyebrow}</span>'
        f'<h1 style="margin: 8px 0 0; font-size: 23px; font-weight: 700; letter-spacing: -0.03em; line-height: 1.4; color: {C["INK"]}; text-wrap: pretty;">{sentence}</h1>'
        f'{note_html}'
        f'<div style="margin-top: auto; padding-bottom: 24px; display: flex; flex-direction: column; gap: 16px; flex-shrink: 0;">'
        f'{dots(step - 1)}{btn("다음", "primary", h=52, radius=14, size=16)}</div></div>')


# ══════════════ 소개 1 · 현재 위치 ══════════════
# 앱 components/navi/intro-flow.tsx step 0(first-run-13): 달력 예시(제목만 · 칸 7개 · ✓ 없음 · 오늘 칸 파란 테두리) + 간단한 위치 카드
# (머리 `이번 달 소비` + 배지 · 큰 숫자 44 · 설명 줄 · 항로 바). 오른쪽 `소비 목표까지` 줄과 `순자산 대비`는 뺐다. 값은 시안 9월 2 ~ 8일 그대로(데이터와 잇지 않는 예시).
def intro_strip_cell(d):
    s, _, tr, zero = day_state('sep', d)
    return cell(d, WD[(1 + d) % 7], state=(s, False, tr, zero), flex=True, w_=46)


intro_calendar = card(
    f'<span style="display: block; font-size: 14px; font-weight: 600; line-height: 1.4; color: {C["INK"]};">이번 달 소비 기록</span>'
    f'<div style="display: flex; justify-content: space-between; margin-top: 8px;">{"".join(intro_strip_cell(d) for d in range(2, 9))}</div>',
    pad='12px 14px 10px')
intro_position = hero(
    eyebrow_row('이번 달 소비', badge('월말에도 목표 안', 'pos', 'check'))
    + f'<div style="margin-top: 8px;">{display_num("31.1", size=44, unit_size=21)}</div>'
    + f'<div style="font-size: 13px; font-weight: 500; color: {C["INK2"]}; margin-top: 5px;">월급 360만원 중 112만원 썼어요</div>'
    + f'<div style="margin-top: 12px;">{route_bar()}</div>', pad=14).replace('padding: 14px;', 'padding: 14px 16px;', 1)
LOCK_NOTE = (f'<p style="display: flex; align-items: flex-start; gap: 6px; margin: 12px 0 0; font-size: 13.5px; line-height: 1.5; color: {C["INK2"]};">'
             f'<span style="flex-shrink: 0; margin-top: 2px;">{icon("lock", 14, C["INK3"], 1.9)}</span>'
             f'<span>은행 · 카드 연결 없이 직접 적고, 이 폰에만 저장돼요.</span></p>')      # 앱 폰(native) 문구 — 웹은 `이 브라우저에만`(첫 실행 페이지 노트)
w('IntroPosition', intro(1, '현재 위치',
                         f'쓴 돈을 달력에 숫자만 적으면<br>월급의 <span style="white-space: nowrap;">몇 %를</span> 썼는지 바로 보여요',
                         intro_calendar + intro_position, LOCK_NOTE))


# ══════════════ 소개 2 · 항로 ══════════════
route_card = card(
    eyebrow_row('항로', f'<span style="font-size: 12px; font-weight: 600; color: {C["INK"]}; white-space: nowrap;">현재 31.1% · 소비 목표 60%</span>')
    + f'<div style="margin-top: 16px;">{route_bar()}</div>')
guide_card = guidance('warn', '다음 안내', '카드 할부 금리 14.5%부터 줄여 보세요',
                      '고금리 부채는 자산이 자라는 속도를 가장 크게 낮춰요.', '상환 계획 보기')

w('IntroRoute', intro(2, '항로', '소비 목표까지 얼마나 남았는지,<br>지금 무엇을 하면 되는지 알려 줘요.', route_card + guide_card))


# ══════════════ 소개 3 · 목적지 ══════════════
def dest_row(name, eta, pct, color, last=False):
    bb = '' if last else f'border-bottom: 1px solid {C["LINE_ROW"]};'
    return (f'<div style="display: flex; align-items: center; gap: 12px; height: 62px; {bb}">'
            f'{ring(pct, color, 44, f"{pct}%")}'
            f'<div style="display: flex; flex-direction: column; gap: 3px; flex: 1; min-width: 0;">'
            f'<span style="font-size: 14px; font-weight: 600; letter-spacing: -0.015em; color: {C["INK"]};">{name}</span>'
            f'<span style="font-size: 12px; color: {C["INK3"]};">{eta}</span></div>'
            f'{icon("right", 16, C["INK4"], 2)}</div>')


# 수치 = 시안 사용자 목적지(NUMBERS §7 · D17 · 같은 값은 모든 장에서 같게 — 2026-09-27 fix-up). 앱 intro-flow.tsx 의 고정 예시(2027년 11월 · 35만원 ·
# 2032년 6월 · 2030년 10월)는 옛 값이라 앱 쪽을 고칠 것(CHANGED 앱 후속).
dest_card = card(
    eyebrow_row('목적지', f'<span style="font-size: 12px; font-weight: 500; color: {C["INK3"]};">도착 예상</span>')
    + f'<div style="margin-top: 4px;">'
    + dest_row('비상금 6개월', '2027년 4월 · 매달 70만원', 68, ASSET['현금성'])
    + dest_row('투자 계좌 5,000만원', '2033년 12월 · 수익률 연 5.0% 가정', 42, C['VIO'])
    + dest_row('신용대출 다 갚기', '2030년 11월 · 상환 계획대로', 31, C['WARN'], last=True)
    + '</div>', pad='12px 14px 2px')

w('IntroDestination', intro(3, '목적지', '비상금 · 투자 · 상환,<br>언제 도착할지 날짜로 알려 줘요.', dest_card))


# ══════════════ 구성 · 홈에 무엇을 둘까요? ══════════════
def checkbox(on):
    if on:
        return (f'<div style="width: 22px; height: 22px; border-radius: 7px; background: {C["BRAND"]}; display: flex; '
                f'align-items: center; justify-content: center; flex-shrink: 0;"><!--dc-keep-->{icon("check", 14, "#FFFFFF", 3)}<!--/dc-keep--></div>')      # 다크도 흰 체크(앱 · darken 이 surface 로 바꾸지 않게)
    return (f'<div style="width: 22px; height: 22px; border-radius: 7px; background: {C["SURF"]}; '
            f'border: 1.5px solid {C["INPUT"]}; flex-shrink: 0;"></div>')


# 홈 구성 목록의 왼쪽 그림 — 카드 축소 미리보기(막대 몇 개)는 서로 구별이 안 돼 아이콘 하나로 바꿨다(2026-09-21 사용자 선택 · 전·후 비교 뒤).
CARD_ICON = {'calendar': 'cal', 'guide': 'arrowur', 'limit': 'sliders_h', 'goal': 'target', 'peer': 'users',      # 한도 = 앱 SlidersHorizontal(2026-09-27 fix-up)
             'ratio': 'chart', 'networth': 'wallet', 'payoff': 'bank', 'stock': 'trend'}


def thumb(cid):
    """카드 아이콘 32 × 32(회색 바탕 · radius 10 · 아이콘 17px ink-2). 이름을 읽기 전에 무엇인지 보이게 한다."""
    return (f'<div style="width: 32px; height: 32px; border-radius: 10px; background: {C["INSET"]}; flex-shrink: 0; display: flex; '
            f'align-items: center; justify-content: center;">{icon(CARD_ICON[cid], 17, C["INK2"], 1.9)}</div>')


def pick_row(cid, name, desc, on, last=False, dim=False):
    """홈 카드 한 행 — 앱 .v4-setup-pick(최소 48 · 위아래 6 · 설명은 줄바꿈 · 11.5 / 1.4). dim = 4 / 4 일 때 안 고른 행(체크 · 아이콘 · 글자 45% · 바탕 그대로)."""
    bb = '' if last else f'border-bottom: 1px solid {C["LINE_ROW"]};'
    op = ' opacity: .45;' if dim else ''
    return (f'<div style="display: flex; align-items: center; gap: 12px; min-height: 48px; padding: 6px 0; {bb}">'
            f'<div style="display: flex; align-items: center; gap: 12px; flex-shrink: 0;{op}">{checkbox(on)}{thumb(cid)}</div>'
            f'<div style="display: flex; flex-direction: column; gap: 2px; flex: 1; min-width: 0;{op}">'
            f'<span style="font-size: 14px; font-weight: 600; letter-spacing: -0.01em; color: {C["INK"]};">{name}</span>'
            f'<span style="font-size: 11.5px; line-height: 1.4; color: {C["INK3"]};">{desc}</span></div></div>')


# 목록 순서 = 앱 HOME_CARD_KEYS: 다음 안내 · 이번 달 한도 · 대표 목적지 · 또래와 내 페이스 · 자산 한눈에 · 순자산 한 줄 · 상환 계획 한 줄.
# 달력은 2026-09-22 사용자 결정으로 선택지에서 빠져 소비율처럼 고정 행(늘 켜짐) — 상한은 4. 주식 요약은 준비 중이라 목록에 없다(first-run-16).
# 설명은 앱 문구 그대로(AMEND 1 · home-13 · home-20 · D4).
CARDS = [
    ('guide', 'guide', '다음 안내', '지금 할 일 한 가지'),
    ('limit', 'limit', '이번 달 한도', '이번 달 남은 한도와 하루에 쓸 수 있는 돈'),
    ('goal', 'goal', '대표 목적지', '가장 앞선 목적지와 도착 예상'),
    ('peer', 'peer', '또래와 내 페이스', '나이와 또래 기준을 직접 넣으면 내 월말 예상과 비교해요 · 나중에 넣어도 돼요'),
    # 홈 맨 아래 세 줄 카드(순자산 대비 월말 예상 · 자산 종합 점수 · 10년 뒤 순자산)를 한 카드로 묶어 켜고 끈다 — 이름 `자산 한눈에`(2026-09-21 사용자 결정)
    ('ratio', 'rows', '자산 한눈에', '순자산 대비 월말 예상 · 자산 종합 점수 · 10년 뒤 순자산을 세 줄로'),
    ('networth', 'line', '순자산 한 줄', '지금 순자산 금액과 다음 지점까지 남은 돈'),
    ('payoff', 'line', '상환 계획 한 줄', '다 갚는 달과 매달 갚는 돈'),
]
# 첫 실행의 처음 체크(AMEND 1 · 앱 firstRunHomeCards(false)) — 부채 카드는 미리 체크하지 않는다: 다음 안내 · 이번 달 한도 · 순자산 한 줄 = 3 / 4.
ON_SETUP = {'guide', 'limit', 'networth'}
# 설정에서 들어온 편집 = 샘플(홈 구성을 저장하지 않은 사람)의 기본 카드 DEFAULT_HOME_CARDS 4 / 4 — 나머지 행은 흐려진다.
ON_EDIT = {'guide', 'limit', 'networth', 'payoff'}


def lock_row(label, sub=None, last=False):
    """고정 행 — 자물쇠 · 이름 · 한 줄 설명 · `고정` 배지(앱 .v4-setup-fixed-row · 최소 48 · 위아래 6)."""
    bb = '' if last else f'border-bottom: 1px solid {C["LINE_ROW"]};'
    sub_html = f'<span style="font-size: 11.5px; line-height: 1.4; color: {C["INK3"]};">{sub}</span>' if sub else ''
    return (f'<div style="display: flex; align-items: center; gap: 10px; min-height: 48px; padding: 6px 0; {bb}">'
            f'{icon("lock", 16, C["INK4"], 1.9)}'
            f'<div style="display: flex; flex-direction: column; gap: 2px; flex: 1; min-width: 0;">'
            f'<span style="font-size: 13.5px; font-weight: 600; color: {C["INK"]};">{label}</span>{sub_html}</div>'
            f'<span style="flex-shrink: 0;">{badge("고정", "mute")}</span></div>')


# 이번 달 소비(히어로)와 달력은 늘 켜져 있다(달력은 2026-09-22 결정 — 기록의 기본 입구라서 끌 수 없음). `현재 위치`는 머리말에서 물러났다(D18 · 앱 문구).
fixed_row = card(lock_row('이번 달 소비', '월급 대비 지금까지 쓴 비율')
                 + lock_row('이번 달 소비 기록', '날짜를 눌러 바로 기록 · 늘 이번 달 소비 아래', last=True), pad='0 14px')


def stock_card(on):
    """주식은 준비 중 — 켜 두면 settings.features.stocks 만 저장하고 화면에는 아무것도 생기지 않는다. 켜도 끄도 같은 설명."""
    return card(
        f'<div style="display: flex; align-items: flex-start; gap: 12px;">'
        f'<div style="display: flex; flex-direction: column; gap: 3px; flex: 1; min-width: 0;">'
        f'<span style="font-size: 14px; font-weight: 600; color: {C["INK"]};">주식 화면이 나오면 알려 드릴까요?</span>'
        f'<span style="font-size: 12px; line-height: 1.45; color: {C["INK3"]};">지금은 준비 중이에요. 켜 두면 주식 화면이 생길 때 알려 드려요.</span></div>'
        f'{toggle(on)}</div>')


LEAD = (f'<p style="margin: 6px 0 0; font-size: 13.5px; line-height: 1.5; color: {C["INK2"]};">이번 달 소비와 소비 기록 달력은 늘 맨 위에 있어요.<br>'
        f'그 아래에 둘 카드를 4개까지 골라 주세요.</p>')


def setup_screen(top, head, on, stocks, footer, to_end=False, dim_rest=False, dialog=False):
    """홈 구성 화면의 공통 틀 — 머리줄(고정) · 목록(스크롤 구역) · 아래 버튼(고정). 앱처럼 844 한 화면으로 그린다:
    처음 모습은 맨 아래 주식 카드가 아래 버튼 구역에 가려 잘리고(앱 캡처와 같다), to_end=True 면 끝까지 내린 모습(아래 맞춤 — 넘친 윗부분이 잘린다).
    dim_rest = 4 / 4 일 때 안 고른 행을 흐리게.
    dialog = 설정 › 홈 구성 — 앱은 화면을 꽉 채운 페이지가 아니라 가운데 뜬 창(390 × 820 · 위 12 · 모서리 없음 · 1px 테두리 그림자)이고
    위아래 12px 틈으로 뒤의 홈(샘플 띠 · 탭 바)이 검정 10% + 흐림 4px 으로 비친다(2026-09-27 fix-up 4 · 하네스 b574373)."""
    picked = sum(1 for c in CARDS if c[0] in on)
    dim = dim_rest and picked >= 4
    count_lbl = f'<span style="font-size: 12px; font-weight: 600; color: {C["INK3"]}; white-space: nowrap; flex-shrink: 0;">{picked} / 4 선택</span>'
    rows = ''.join(pick_row(cid, n, d, cid in on, last=(i == len(CARDS) - 1), dim=(dim and cid not in on))
                   for i, (cid, k, n, d) in enumerate(CARDS))
    inner_align = 'justify-content: flex-end; ' if to_end else ''
    body = (
        f'<div style="padding: 0 20px; flex-shrink: 0;">{top}</div>'
        f'<div style="flex: 1; min-height: 0; overflow: hidden; padding: 0 20px; display: flex; flex-direction: column; {inner_align}">'
        f'<div style="display: flex; flex-direction: column; flex-shrink: 0; padding-bottom: 16px;">'
        f'{head}'
        f'<div style="margin-top: 12px;">{fixed_row}</div>'
        f'<div style="margin-top: 12px;">{section_head("홈 카드", right=count_lbl)}</div>'
        f'<div style="margin-top: 8px;">{card(rows, pad="0 14px")}</div>'
        f'<div style="margin-top: 10px;">{stock_card(stocks)}</div></div></div>'
        f'<div style="padding: 8px 20px 24px; display: flex; flex-direction: column; gap: 8px; flex-shrink: 0; background: {C["BG"]};">{footer}</div>')
    if not dialog:
        return frame(body)
    # 뒤의 홈 — 흐림 4px 이라 글자는 안 보이고 색만 남는다: 위 12 = 샘플 띠(brand-soft), 아래 12 = 탭 바 윗부분(surface · 위 선). 그 위에 검정 10% 막.
    return (f'<div style="width: 390px; height: 844px; position: relative; overflow: hidden; background: {C["BRAND_SOFT"]}; color: {C["INK"]}; font-variant-numeric: tabular-nums;">'
            f'<div style="position: absolute; left: 0; right: 0; bottom: 0; height: 12px; background: {C["SURF"]}; border-top: 1px solid {C["LINE"]};"></div>'
            f'<div style="position: absolute; inset: 0; background: rgba(0,0,0,.1);"></div>'
            f'<div style="position: absolute; left: 0; top: 12px; width: 390px; height: 820px; background: {C["BG"]}; box-shadow: 0 0 0 1px rgba(16,24,40,.1); '
            f'display: flex; flex-direction: column; overflow: hidden;">{body}</div></div>')


SETUP_H1 = (f'<h1 style="margin: 6px 0 0; font-size: 22px; font-weight: 700; letter-spacing: -0.03em; line-height: 1.35; color: {C["INK"]};">홈에 무엇을 둘까요?</h1>')
SETUP_FOOT = (f'{btn("다음", "primary", h=52, radius=14, size=16)}'
              f'<p style="margin: 0; text-align: center; font-size: 11.5px; line-height: 1.5; color: {C["INK3"]};">언제든 설정 › 홈 구성에서 바꿀 수 있어요.</p>')

# 첫 실행 · 소개 3장 → 홈 구성(AMEND 1 · 버튼 `다음` → 시작 방법 고르기). 처음 화면 — 주식 카드가 아래 버튼 구역에 가린다(앱과 같다).
w('HomeSetup', setup_screen(topline("홈 구성"), SETUP_H1 + LEAD, ON_SETUP, False, SETUP_FOOT))

# 첫 실행 · `주식 화면이 나오면 알려 드릴까요?`를 켠 모습 — 목록은 그대로(주식 요약 행 없음), 끝까지 내린 상태.
w('HomeSetupStocksOn', setup_screen(topline("홈 구성"), SETUP_H1 + LEAD, ON_SETUP, True, SETUP_FOOT, to_end=True))

# 기존 사용자 · 설정 › 홈 구성으로 들어온 같은 목록 — 첫 실행이 아니라 `건너뛰기` · `다음` 대신 닫기(×) · 저장(앱 대화상자 · 아래 안내 줄 없음).
edit_top = (f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px; height: 56px; margin-top: 8px;">'
            f'<h1 style="margin: 0; font-size: 20px; font-weight: 700; letter-spacing: -0.03em; color: {C["INK"]};">홈 구성</h1>'
            f'<div style="width: 36px; height: 36px; border-radius: 11px; background: {C["INSET"]}; display: flex; align-items: center; '
            f'justify-content: center; flex-shrink: 0;">{icon("x", 17, C["INK2"], 2.2)}</div></div>')
w('HomeLayoutEdit', setup_screen(edit_top, LEAD.replace('margin: 6px 0 0;', 'margin: 0;'), ON_EDIT, False,
                                 btn("저장", "primary", h=52, radius=14, size=16), dim_rest=True, dialog=True))


# ══════════════ 설정 시트 · `홈 구성` 행 (D5 · home-9 · language-ia-5) ══════════════
# 앱 components/navi/settings-sheet.tsx — 내 수치 · 화면(바로 적용돼요) · 홈 화면 · 기기 알림 · 도움말 · 데이터 · 닫기. 내 수치의 입력 칸은 ProfileDialog(`내 수치`).
# 샘플 사용자(홈 구성을 저장하지 않음 → 기본 카드 4개) · 테마 `시스템` · 폰(앱) 저장 문구.
def s_group(label, inner, tag=None):
    t = (f'<span style="font-size: 12px; font-weight: 500; color: {C["INK3"]}; white-space: nowrap;">{tag}</span>') if tag else ''
    return (f'<div style="flex-shrink: 0;"><div style="display: flex; align-items: baseline; justify-content: space-between; gap: 8px; margin-bottom: 9px;">'
            f'<span style="font-size: 11px; font-weight: 600; letter-spacing: 0.07em; color: {C["INK3"]};">{label}</span>{t}</div>{inner}</div>')


def nav_row(label, meta=''):
    m = f'<span style="font-size: 12px; color: {C["INK3"]}; white-space: nowrap;">{meta}</span>' if meta else ''
    return (f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px; min-height: 48px; '
            f'padding: 0 13px; border-radius: 12px; background: {C["INSET"]};">'
            f'<span style="font-size: 13.5px; font-weight: 600; color: {C["INK"]}; white-space: nowrap;">{label}</span>'
            f'<div style="display: flex; align-items: center; gap: 8px; flex-shrink: 0;">{m}{icon("right", 16, C["INK3"], 2)}</div></div>')


numbers_row = (f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px; min-height: 56px; '
               f'padding: 10px 13px; border-radius: 12px; background: {C["INSET"]}; flex-shrink: 0;">'
               f'<div style="display: flex; flex-direction: column; gap: 2px; min-width: 0;">'
               f'<span style="font-size: 13.5px; font-weight: 600; color: {C["INK"]};">내 수치</span>'
               f'<span style="font-size: 12px; color: {C["INK3"]};">월급 360만원 · 소비 목표 60%</span></div>{icon("right", 16, C["INK3"], 2)}</div>')
settings_body = (
    numbers_row
    + s_group('화면', segmented(['시스템', '라이트', '다크'], 0), tag='바로 적용돼요')
    + s_group('홈 화면', nav_row('홈 구성', '카드 4개'))
    + s_group('기기 알림', nav_row('알림', '끔'))
    + s_group('도움말', nav_row('처음 안내 다시 보기'))
    + s_group('데이터', f'<p style="margin: 0 0 8px; font-size: 11.5px; line-height: 1.5; color: {C["INK3"]};">이 기기에 암호화해 저장해요</p>'
                       f'<div style="display: flex; gap: 8px;">'
                       f'{btn("백업 내보내기", "secondary", "download", h=44).replace("width: 100%;", "flex: 1;")}'
                       f'{btn("백업 불러오기", "secondary", "upload", h=44).replace("width: 100%;", "flex: 1;")}</div>'
                       f'<div style="margin-top: 8px;">{btn("모든 데이터 지우기", "danger", "refresh", h=44)}</div>'))
settings_sheet = sheet('설정', '화면 · 알림 · 백업을 여기서 바꿔요.', settings_body,
                       btn('닫기', 'secondary', h=48), body_pb=14)
w('SettingsHomeEntry', settings_sheet)


# ══════════════ 홈 ══════════════
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
M_CONTENT = '<div style="flex: 1; min-height: 0; display: flex; flex-direction: column; gap: 10px; padding: 0 14px; overflow: hidden;">'
M_NAV = '<div style="display: flex; align-items: flex-start; justify-content: space-between; gap: 2px; height: 66px;'
NOTES_OPEN, NOTES_CLOSE = '<!--hero-notes-->', '<!--/hero-notes-->'

header = cut(main_src, M_HEADER, M_CONTENT).rstrip()
hero_block = cut(main_src, M_HERO, M_GUIDE).rstrip()
guide_block = cut(main_src, M_GUIDE, M_GOAL).rstrip()
limit_block = cut(main_src, M_LIMIT, M_NAV).rstrip()
assert limit_block.endswith('</div>')
limit_block = limit_block[:limit_block.rfind('</div>')].rstrip()   # 콘텐츠 컨테이너의 닫는 태그는 뺀다
assert hero_block.count('>31.1<') == 1 and '소비 기록하기' not in hero_block   # 히어로 버튼은 2026-09-22에 뺐다 — 기록은 달력 날짜로
# 큰 숫자 · 게이지 = 지금까지 쓴 돈 ÷ 월급(1,120,000 ÷ 3,600,000 = 31.1% · 채움 inset 68.9%), 배지 · 아래 칸 = 월말 예상(57.9% · 208만원) — 2026-09-24
# 오른쪽 줄 = 돈(2026-09-26 · 소비 목표 216만 − 쓴 돈 112만 = 104만원 · D4 · D17 · NUMBERS §2)
assert all(hero_block.count(x) == 1 for x in ('이번 달 소비', '월말에도 목표 안', '소비 목표 조정', '104만원 남음', '월급 360만원 중 112만원 썼어요',
                                                  '>1.2%<', 'inset: 0 68.9% 0 0', '>208<span', '월급 · 부수입 고치기', NOTES_OPEN, NOTES_CLOSE))
assert '현재 위치' not in hero_block and '28.9%p' not in hero_block and '내 목표' not in hero_block
# 히어로 각주(캐논 · W/design-state.json · 2026-09-27 fix-up): 카테고리 없는 32,000원 · 고정비 이력 두 줄(8월 마감값 = 기록 합이라 합계 고치기 줄 없음).
# 다른 장면을 그리는 장은 hero_bare 에 각주를 새로 붙인다.
hero_bare = hero_block[:hero_block.index(NOTES_OPEN)].rstrip() + '\n\n' + hero_block[hero_block.index(NOTES_CLOSE) + len(NOTES_CLOSE):].lstrip()
assert '8월 합계 고치기' not in hero_bare and hero_bare.count('<div') == hero_bare.count('</div>')
_b = header.index('<span style="position: absolute; top: 4px; right: 4px;')
header_nobadge = header[:_b] + header[header.index('</span>', _b) + len('</span>'):]      # 알림 0건 — 종 배지 없음
assert header.count('>1</span>') == 1 and '>1</span>' not in header_nobadge
# 달력 카드 — Main 에는 달력이 없어 잘라 올 마커(M_CAL)가 없다. HomeDefaultScroll 과 같은 펼친 월 달력(홈의 기본 · 2026-09-30)을 공용 조각으로 만든다.
# 이 조각을 HomeStocksOff(home_canon) · HomeStocksCard(gen_v4_stocks)가 받아 쓴다 — 접은 7일 줄은 HomeCalendarStrip 에만.
calendar_block = calendar_card(HOME_EXPANDED)
assert (calendar_block.count('2026년 9월') == 1 and '접기' in calendar_block and '펼치기' not in calendar_block and '이번 달 소비 기록' not in calendar_block
        and '더 적기' in calendar_block and '기록 없음' in calendar_block and '9월 기록한 소비 1,120,000원' in calendar_block)


def line_card(label, sub, value, value_label=None, missing=False):
    """홈 한 줄 카드(앱 .home-line-card · 높이 56 · 위아래 4). value_label = 값 앞 작은 이름(`매달 갚는 돈`).
    missing = 값이 없을 때 회색 `—`."""
    vl = (f'<span style="font-size: 11.5px; font-weight: 500; color: {C["INK3"]}; white-space: nowrap;">{value_label}</span>') if value_label else ''
    vcol, vw = (C["INK4"], 500) if missing else (C["INK"], 600)
    return card(
        f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 10px; min-height: 46px;">'
        f'<div style="display: flex; flex-direction: column; gap: 2px; min-width: 0;">'
        f'<span style="font-size: 13.5px; font-weight: 600; color: {C["INK"]};">{label}</span>'
        f'<span style="font-size: 11.5px; color: {C["INK3"]};">{sub}</span></div>'
        f'<div style="display: flex; align-items: center; gap: 8px; flex-shrink: 0;">'
        f'<span style="display: inline-flex; align-items: baseline; gap: 4.5px; white-space: nowrap;">{vl}'
        f'<span style="font-size: 15px; font-weight: {vw}; letter-spacing: -0.02em; color: {vcol};">{value}</span></span>'
        f'{icon("right", 16, C["INK4"], 2)}</div></div>', pad='4px 14px')


# 순자산 9,350만원 · 1억 도착 2027년 1월(미래 경로의 1억 지점 · home-2) · 다 갚는 달 2036년 5월(앱 달 셈 · D17) · 매달 갚는 돈 92만원 — NUMBERS §3.
networth_card = line_card('순자산', '1억원까지 650만원 · <span style="white-space: nowrap;">2027년 1월</span> 도착 예상', '9,350만원')
payoff_card = line_card('상환 계획', '다 갚는 달 <span style="white-space: nowrap;">2036년 5월</span> · 고금리 우선', '92만원', value_label='매달 갚는 돈')


def home_canon(scrolled_pad=None):
    """시안 사용자(9월 8일)의 기본 홈 — 앱 DEFAULT_HOME_CARDS: 히어로 · 달력 · 다음 안내 · 이번 달 한도 · 순자산 한 줄 · 상환 계획 한 줄.
    scrolled_pad = 아래로 스크롤한 모습(본문 아래 맞춤 · 넘친 윗부분이 잘림 · 아래 여백 px). None 이면 위에서부터."""
    content = M_CONTENT if scrolled_pad is None else M_CONTENT.replace('padding: 0 14px;', f'justify-content: flex-end; padding: 0 14px {scrolled_pad}px;')
    head = f'\n  {header}\n' if scrolled_pad is None else ''      # 아래로 내린 모습이면 머리줄은 밀려 올라가 안 보인다
    return (f'{head}\n  {content}\n\n    {hero_block}\n\n    {calendar_block}\n\n    {guide_block}\n\n    {limit_block}\n\n'
            f'    {networth_card}\n\n    {payoff_card}\n\n  </div>\n\n')


# ══════════════ 홈 · 첫 실행 뒤(내 데이터로 시작 · 아무것도 넣지 않은 날) ══════════════
# 앱: 소개 → 홈 구성(처음 체크 그대로 `다음`) → 시작 방법 고르기 `내 데이터로 시작` → 홈 안내 `건너뛰기`. 9월 8일 · 월급 · 기록 · 자산 · 부채 0.
# 카드 = 처음 체크 셋(다음 안내 · 이번 달 한도 · 순자산 한 줄 · AMEND 1 · first-run-14). 다음 안내 자리는 `시작 순서`(first-run-5). 알림 0건이라 종 배지 없음.
DASH18 = f'<span style="font-size: 18px; font-weight: 600; letter-spacing: -0.02em; color: {C["INK4"]};">—</span>'


def tile3(labels, values):
    cells = []
    for i, (lab, val) in enumerate(zip(labels, values)):
        pad = 'padding-right: 10px;' if i == 0 else ('padding: 0 10px; border-left: 1px solid #EFF2F8;' if i == 1 else 'padding-left: 10px; border-left: 1px solid #EFF2F8;')
        cells.append(f'<div style="display: flex; flex-direction: column; gap: 3px; {pad}">'
                     f'<span style="font-size: 11.5px; font-weight: 500; color: {C["INK3"]}; white-space: nowrap;">{lab}</span>{val}</div>')
    return (f'<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 0; margin-top: 14px; padding-top: 13px; border-top: 1px solid #EFF2F8;">'
            + ''.join(cells) + '</div>')


PILL = (f'<span style="display: inline-flex; align-items: center; height: 28px; padding: 0 11px; border-radius: 99px; border: 1px solid #C9D3F5; background: {C["SURF"]}; '
        f'font-size: 12px; font-weight: 600; color: {C["BRAND"]}; white-space: nowrap; flex-shrink: 0;">소비 목표 조정</span>')
HERO_FOOT = (f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 10px; margin-top: 12px;">'
             f'<span style="font-size: 11px; line-height: 1.4; color: {C["INK3"]};{KA}">월급(실수령) 기준 · 저축 이체와 대출 갚은 돈은 쓴 돈에 넣지 않아요</span>'
             f'<span style="display: inline-flex; align-items: center; font-size: 11.5px; font-weight: 600; color: {C["BRAND"]}; white-space: nowrap; flex-shrink: 0;">'
             f'월급 · 부수입 고치기{icon("right", 13, C["BRAND"], 2.2)}</span></div>')


def hero_empty(second='9월을 마감하면 10월부터 월말 예상을 보여 드려요', caption='월급을 넣으면 월급의 몇 %를 썼는지 보여요', cta=True):
    """기록 · 월급이 없는 히어로: 배지 없음 · 회색 `아직 기록이 없어요` · 빈 게이지 · 아래 칸 모두 — ·
    기준 줄 + `월급 · 부수입 고치기 ›` · 가득 찬 폭 `+ 월급 입력하고 시작`(월급이 있으면 cta=False)."""
    body = (f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px; min-height: 28px;">'
            f'<span style="font-size: 11px; font-weight: 600; letter-spacing: 0.07em; color: {C["INK3"]}; white-space: nowrap;">이번 달 소비</span>{PILL}</div>'
            f'<div style="margin-top: 8px; font-size: 21px; font-weight: 700; letter-spacing: -0.045em; line-height: 1.2; color: {C["INK3"]};">아직 기록이 없어요</div>'
            f'<div style="margin-top: 5px; font-size: 13px; font-weight: 500; line-height: 1.5; color: {C["INK2"]};{KA}">{caption}</div>'
            f'<div style="margin-top: 3px; font-size: 12px; line-height: 1.45; color: {C["INK3"]};{KA}">{second}</div>'
            f'<div style="margin-top: 15px;">{route_bar(0, fill=False)}</div>'
            + tile3(['월급', '월말 예상', '월말 예상 여유'], [DASH18] * 3)
            + HERO_FOOT
            + (f'<div style="margin-top: 10px;">{btn("월급 입력하고 시작", "primary", "plus", h=46)}</div>' if cta else ''))
    return hero(body)


def start_checklist():
    """다음 안내 자리의 `시작 순서`(앱 .start-checklist): 1 월급 (실수령) [입력하기](지금 할 줄 · 파란 바탕) ·
    2 첫 소비 기록 [오늘 쓴 돈 적기] · 3 자산 · 부채 + `선택 사항` [추가]. 월급과 기록 한 건이 생기면 카드가 사라진다."""
    def step(n, title, desc, action, current=False, optional=False, muted=False):
        num_bg, num_fg = (C["TRACK"], C["INK3"]) if muted else (C["BRAND"], '#FFFFFF')
        tag = (f' <span style="font-size: 11px; font-weight: 500; color: {C["INK3"]}; background: {C["INSET"]}; border-radius: 99px; padding: 1px 6px; margin-left: 2px; white-space: nowrap;">선택 사항</span>'
               if optional else '')
        act = (f'<span style="display: inline-flex; align-items: center; height: 30px; padding: 0 11px; border-radius: 13px; font-size: 12.5px; font-weight: 600; white-space: nowrap; flex-shrink: 0; '
               + (f'background: {C["BRAND"]}; color: #FFFFFF; border: 1px solid {C["BRAND"]};' if current else f'background: {C["SURF"]}; color: {C["BRAND"]}; border: 1px solid {C["LINE"]};')
               + f'">{action}</span>')
        bg = f'background: {C["BRAND_SOFT"]};' if current else ''
        return (f'<div style="display: flex; align-items: center; gap: 10px; min-height: 52px; padding: 6px 8px; margin: 0 -8px; border-radius: 14px; {bg}">'
                f'<span style="width: 24px; height: 24px; border-radius: 99px; background: {num_bg}; color: {num_fg}; font-size: 12px; font-weight: 700; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">{n}</span>'
                f'<div style="display: flex; flex-direction: column; gap: 2px; flex: 1; min-width: 0;">'
                f'<span style="font-size: 13.5px; font-weight: 600; color: {C["INK"]};">{title}{tag}</span>'
                f'<span style="font-size: 11px; line-height: 1.45; color: {C["INK3"]};">{desc}</span></div>{act}</div>')
    return (f'<div style="background: {C["SURF"]}; border: 1px solid {C["LINE"]}; border-radius: 18px; padding: 14px 16px 10px; flex-shrink: 0;">'
            f'<span style="display: block; font-size: 11px; font-weight: 600; letter-spacing: 0.06em; color: {C["BRAND"]};">다음 안내</span>'
            f'<span style="display: block; margin: 4px 0 6px; font-size: 16px; font-weight: 600; letter-spacing: -0.035em; line-height: 1.4; color: {C["INK"]};">시작 순서</span>'
            f'<div style="display: flex; flex-direction: column; gap: 2px;">'
            + step(1, '월급 (실수령)', '월급의 몇 %를 썼는지 계산하는 기준', '입력하기', current=True)
            + step(2, '첫 소비 기록', '날짜를 누르고 숫자만 넣으면 돼요', '오늘 쓴 돈 적기')
            + f'<div style="height: 1px; background: {C["LINE_SOFT"]};"></div>'
            + step(3, '자산 · 부채', '있으면 순자산과 갚는 순서까지 보여요', '추가', optional=True, muted=True)
            + '</div></div>')


def limit_empty():
    """판정 선이 없는 이번 달 한도: `이번 달 한도 오늘 포함 하루 —` · 오른쪽 `— ›` · `한도를 아직 안 정했어요` · 빈 막대."""
    return (f'<div style="background: {C["SURF"]}; border: 1px solid {C["LINE"]}; border-radius: 18px; padding: 12px 14px; flex-shrink: 0;">'
            f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px;">'
            f'<span style="font-size: 13.5px; font-weight: 600; color: {C["INK"]}; white-space: nowrap;">이번 달 한도 <span style="font-weight: 500; color: {C["INK3"]};">오늘 포함 하루 —</span></span>'
            f'<div style="display: flex; align-items: center; gap: 4px;"><span style="font-size: 13.5px; font-weight: 600; color: {C["INK4"]};">—</span>{icon("right", 16, C["INK4"], 2)}</div></div>'
            f'<div style="font-size: 13px; line-height: 1.45; color: {C["INK2"]}; margin-top: 4px;">한도를 아직 안 정했어요</div>'
            f'<div style="height: 8px; border-radius: 99px; background: {C["TRACK"]}; margin-top: 9px;"></div></div>')


# 첫 홈 달력 — 펼친 9월(홈의 기본 · 2026-09-30): 첫 줄 8/30 · 8/31(이웃 달) · 1 ~ 7일 `—`, 오늘(8) 기록 0건 → 파란 `+` ·
# 합계 줄 `9월 기록이 아직 없어요`(0원이라고 쓰지 않음) · 가득 찬 폭 `+ 오늘 쓴 돈 적기` · 확인할 내용 없음(home-4 · record-11).
# 시작일 = 오늘(9월 8일에 「내 데이터로 시작」) — 그 전 날 · 앞 이웃 달 칸도 기록이 없으면 `—`(since).
calendar_empty = calendar_card(HOME_EXPANDED, states={d: NO_RECORD for d in range(1, 9)}, since=TODAY, review=0)
assert '9월 기록이 아직 없어요' in calendar_empty and '오늘 쓴 돈 적기' in calendar_empty and '확인할 내용' not in calendar_empty and '5.5만' not in calendar_empty
networth_empty = line_card('순자산', '자산을 입력하면 현재 위치를 알 수 있어요', '—', missing=True)
payoff_empty = line_card('상환 계획', '부채 입력 전', '—', missing=True)
HOME_EMPTY_H = 1492      # 자연 높이 1468 + 24(2026-09-30 펼친 빈 9월 · 예전 접힌 줄 1154 + 24 = 1178). gen_canvas TALL · screens.json 과 같아야 한다
w('HomeConfigured', frame(
    f'\n  {header_nobadge}\n\n  {M_CONTENT}\n\n    {hero_empty()}\n\n    {calendar_empty}\n\n    {start_checklist()}\n\n'
    f'    {limit_empty()}\n\n    {networth_empty}\n\n  </div>\n\n'
    f'  {bottomnav(0)}\n', h=HOME_EMPTY_H))
