# -*- coding: utf-8 -*-
"""홈 달력 카드 공용 조각 — 자료 · 칸 · 접힘 카드(최근 7일 스트립) · 펼침 월 달력 · 상태 줄 · 홈 구성 행 축소 미리보기.

plan/v5-calendar.md(9판). gen_v5.py 에서 옮겨 왔다 — gen_v4.py · gen_v4_stocks.py · gen_v5.py 가 함께 쓴다.
이 모듈은 gen_common 만 import 한다(gen_v4 · gen_v5 를 import 하면 순환). 파일을 쓰지 않는다(import 부작용 없음).

    from gen_calendar import calendar_card, calendar_thumb

달력 · 하루 시트에는 의미색(주황 · 빨강 · 가정 보라)을 쓰지 않는다 — 오늘 칸 brand-soft, 나머지는 잉크 단계뿐.
2026년 9월: 1일 화요일 · 30일 · 5주. 오늘 8일(화). 2026년 8월: 1일 토요일 · 31일 · 6주.
칸 숫자 = 그날 소비 합계(고정비 포함 · 이체 제외). 표기는 앱 formatSum과 같다(1만 미만 원 단위 · 1만 이상 만 단위 한 자리).
"""
from gen_common import C, icon, card

WD = ['일', '월', '화', '수', '목', '금', '토']
TODAY = 8


def fmt_sum(n):
    """앱 lib/navi-quick-entry.ts formatSum과 같은 규칙(1억 미만만 다룬다 — 시안 자료의 최댓값은 712,000)."""
    if n < 10_000:
        return f'{n:,}'
    if n < 1_000_000:
        t = int(n / 1000 + 0.5)          # JS Math.round와 같게 0.5는 올림(58,500 → 5.9만)
        if t < 1000:
            return f'{t / 10:.1f}만'
    return f'{int(n / 10_000 + 0.5):,}만'


# day -> 원 단위 합계. None = 아직 기록 없음(—). 0 = 안 썼어요로 표시한 날.
SEP = {1: 12_000, 2: None, 3: 58_500, 4: 4_500, 5: 12_000, 6: 0, 7: None, 8: 37_000}
SEP_CHECK, SEP_TRANSFER = {1, 4, 5}, {6}
AUG = {1: 23_500, 2: 61_000, 3: 9_800, 4: 4_500, 5: 712_000, 6: 15_300, 7: 38_000, 8: 52_400, 9: 0, 10: 12_000,
       11: 6_700, 12: 89_000, 13: 4_500, 14: 27_600, 15: 118_000, 16: None, 17: 9_900, 18: 33_000, 19: 4_500,
       20: 64_500, 21: 17_800, 22: 72_000, 23: 41_200, 24: 5_600, 25: 13_000, 26: 8_900, 27: 29_500, 28: 96_000,
       29: 35_000, 30: None, 31: 55_000}
AUG_CHECK = {d for d, v in AUG.items() if v and d != 31}          # 0(안 썼어요)에는 ✓ 없음
AUG_TRANSFER = {25}
SEP_TOTAL = sum(v for v in SEP.values() if v)
AUG_TOTAL = sum(v for v in AUG.values() if v)
MONTHS = {'sep': (SEP, SEP_CHECK, SEP_TRANSFER), 'aug': (AUG, AUG_CHECK, AUG_TRANSFER)}


def day_state(month, day):
    """(합계 글자, 확인 ✓, 이체 배지, 0원 표시 여부)"""
    data, checks, transfers = MONTHS[month]
    v = data.get(day)
    text = '—' if v is None else fmt_sum(v)
    return text, day in checks, day in transfers, v == 0


def _mods(chk, tr, size=11, fs=10):
    mods = []
    if chk: mods.append(icon("check", size, C["INK2"], 2.8))
    if tr: mods.append(f'<span style="font-size: {fs}px; font-weight: 500; color: {C["INK2"]};">이체</span>')
    return f'<span style="display: inline-flex; align-items: center; gap: 3px; height: {size + 1}px; flex-shrink: 0;">{"".join(mods)}</span>'


def cell(day, wd=None, w_=44, pressed=False, prev=False, future=False, state=None, before=False, large=False):
    """스트립 칸(접힘 · 최근 7일). 44 × 56(큰 글자 72). 달 제목이 없는 자리라 지난달 날짜는 `8/31`처럼 달을 붙인다.
    state = (합계 글자, ✓, 이체, 0원 표시)를 직접 줄 때(저장 뒤 · 첫 기록처럼 기본 자료와 다른 장).
    before = 시작일(quickEntry.since) 이전 — `—` 없이 날짜만 옅게(누르면 열림).
    large = 큰 글자: 칸 높이 72 · 날짜 14.5 · 합계 12(스트립 칸 44는 47px에 못 미쳐 13이 아니라 12 — 계획 §3-2)."""
    is_today = day == TODAY and not prev
    label = f'8/{day}' if prev else str(day)
    h, fs_wd, fs_date, fs_sum, lh_sum, mod = (72, 12, 14.5, 12, 14, 12) if large else (56, 10, 11, 11, 13, 11)
    bg = C["BRAND_SOFT"] if is_today else 'transparent'
    ring = f'box-shadow: inset 0 0 0 2px {C["BRAND"]};' if pressed else ''
    blank = future or before
    date_col = C["INK4"] if blank else (C["INK"] if is_today else C["INK2"])
    parts = [f'<span style="font-size: {fs_date}px; line-height: 1; font-weight: {600 if is_today else 500}; color: {date_col};">{label}</span>']
    if not blank:
        s, chk, tr, zero = state if state is not None else day_state('aug' if prev else 'sep', day)
        col = C["INK3"] if s == '—' else (C["INK2"] if zero else C["INK"])
        parts.append(f'<span style="font-size: {fs_sum}px; line-height: {lh_sum}px; font-weight: 600; color: {col}; font-variant-numeric: tabular-nums;">{s}</span>')
        parts.append(_mods(chk, tr, size=mod, fs=mod - 1))
    else:
        parts.append(f'<span style="height: {lh_sum}px; flex-shrink: 0;"></span><span style="height: {mod + 1}px; flex-shrink: 0;"></span>')
    wdl = f'<span style="font-size: {fs_wd}px; line-height: 1; font-weight: 500; color: {C["INK3"]};">{wd}</span>' if wd else ''
    return (f'<div style="width: {w_}px; height: {h}px; border-radius: 10px; background: {bg}; {ring} display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 3px; flex-shrink: 0;">'
            f'{wdl}{"".join(parts)}</div>')


def gcell(day, month='sep', kind='in', today=False, future=False, pressed=False, large=False, tight=False):
    """월 달력 칸. 폭은 7등분(1fr) · 높이 56(큰 글자 72). 위에서부터 날짜 · 합계 · 수식어.
    kind: 'in' 이번에 보는 달 · 'adj' 이웃 달(옅은 숫자, 기록은 옅게 보이고 누르면 그 날짜 시트) · 'out' 홈 범위 밖이나 미래(숫자만, 누를 수 없음)."""
    h = 72 if large else 56
    # tight = 칸 폭이 47px에 못 미치는 곳(360 · 320 펼침): 큰 글자 합계를 13 → 12로 한 단계 낮춰 `71.2만`이 잘리지 않게 한다
    fs_date, fs_sum, mod = ((14.5, 12 if tight else 13, 12 if tight else 13) if large else (12, 11, 11))
    blank = future or kind == 'out'
    bg = C["BRAND_SOFT"] if today else 'transparent'
    ring = f'box-shadow: inset 0 0 0 2px {C["BRAND"]};' if pressed else ''
    if blank or kind == 'adj':
        date_col, weight = C["INK4"], 500
    else:
        date_col, weight = (C["INK"], 700) if today else (C["INK2"], 500)
    parts = [f'<span style="font-size: {fs_date}px; font-weight: {weight}; color: {date_col}; line-height: 1.2;">{day}</span>']
    if blank:
        parts.append(f'<span style="height: {fs_sum + 2}px;"></span><span style="height: {mod + 1}px;"></span>')
    else:
        s, chk, tr, zero = day_state(month, day)
        if kind == 'adj':
            col = C["INK4"]
        else:
            col = C["INK3"] if s == '—' else (C["INK2"] if zero else C["INK"])
        parts.append(f'<span style="font-size: {fs_sum}px; font-weight: 600; color: {col}; font-variant-numeric: tabular-nums; line-height: 1.2; white-space: nowrap;">{s}</span>')
        parts.append(_mods(chk, tr, size=mod, fs=mod - 1) if kind == 'in' else f'<span style="height: {mod + 1}px;"></span>')
    fade = ' opacity: .45;' if kind == 'out' else (' opacity: .7;' if kind == 'adj' else '')   # 이번 달 미래 100% > 지난달 이웃 칸 70% > 범위 밖 45%
    return (f'<div style="min-width: 0; height: {h}px; border-radius: 10px; background: {bg}; {ring}{fade} display: flex; flex-direction: column; '
            f'align-items: center; justify-content: center; gap: {3 if large else 2}px;">{"".join(parts)}</div>')


def nav_btn(name, enabled=True, size=32):
    col = C["INK2"] if enabled else C["INK4"]
    arrow = icon(name, 16 if size <= 32 else 19, col, 2.2)
    if not enabled:
        arrow = f'<span style="display: inline-flex; opacity: .5;">{arrow}</span>'
    return (f'<span style="width: {size}px; height: {size}px; border-radius: 10px; border: 1px solid {C["LINE"]}; display: inline-flex; '
            f'align-items: center; justify-content: center; flex-shrink: 0;">{arrow}</span>')


def month_bar(label, prev_on, next_on, back_pill=False, large=False, pill_below=False, label_w=None):
    """펼친 달력의 머리줄 — ‹ 2026년 9월 › · (지난달을 볼 때) 이번 달로 · 접기. 이동 범위는 이번 달 + 지난달(하루 시트 범위와 같다)."""
    size = 40 if large else 32
    fs, tfs = (19, 15.5) if large else (15, 12)
    pill = (f'<span style="font-size: {tfs}px; font-weight: 600; color: {C["BRAND"]}; background: {C["BRAND_SOFT"]}; border-radius: 99px; '
            f'padding: 5px 10px; white-space: nowrap;">이번 달로</span>') if back_pill else ''
    below = ''
    if back_pill and (pill_below or large):      # 334px 안에 머리줄 + 알약이 들어가지 않는 경우
        below = f'<div style="display: flex; justify-content: flex-end; margin-top: 6px;">{pill}</div>'
        pill = ''
    return (f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 6px; min-height: {size}px;">'
            f'<div style="display: flex; align-items: center; gap: 4px;">{nav_btn("left", prev_on, size)}'
            f'<span style="min-width: {label_w or (118 if large else 94)}px; text-align: center; font-size: {fs}px; font-weight: 700; letter-spacing: -0.015em; color: {C["INK"]}; white-space: nowrap;">{label}</span>'
            f'{nav_btn("right", next_on, size)}</div>'
            f'<div style="display: flex; align-items: center; gap: 8px;">{pill}'
            f'<span style="display: inline-flex; align-items: center; gap: 2px; font-size: {tfs}px; font-weight: 600; color: {C["INK2"]}; white-space: nowrap;">접기{icon("up", 14 if not large else 17, C["INK2"], 2.2)}</span></div></div>{below}')


def status_rows(review=2, text='오늘 4건 37,000원', large=False):
    fs, rfs, rh = (14.5, 16, 44) if large else (11, 12.5, 32)
    rows = f'<div style="font-size: {fs}px; line-height: 1.5; color: {C["INK2"]}; margin-top: 8px;">{text}</div>'
    if review:
        rows += (f'<div style="display: flex; align-items: center; justify-content: space-between; height: {rh}px; margin-top: 2px; border-top: 1px solid {C["LINE_SOFT"]};">'
                 f'<span style="font-size: {rfs}px; font-weight: 600; color: {C["INK"]};">확인할 내용 {review}개</span>{icon("right", 15, C["INK4"], 2)}</div>')
    return rows


# 주 배열: ('in'|'adj'|'out', day, 그 칸의 자료가 속한 달)
WEEKS = {
    'sep': [[('adj', 30, 'aug'), ('adj', 31, 'aug')] + [('in', d, 'sep') for d in range(1, 6)],
            [('in', d, 'sep') for d in range(6, 13)], [('in', d, 'sep') for d in range(13, 20)],
            [('in', d, 'sep') for d in range(20, 27)],
            [('in', d, 'sep') for d in range(27, 31)] + [('out', d, 'oct') for d in range(1, 4)]],
    'aug': [[('out', d, 'jul') for d in range(26, 32)] + [('in', 1, 'aug')],
            [('in', d, 'aug') for d in range(2, 9)], [('in', d, 'aug') for d in range(9, 16)],
            [('in', d, 'aug') for d in range(16, 23)], [('in', d, 'aug') for d in range(23, 30)],
            [('in', 30, 'aug'), ('in', 31, 'aug')] + [('adj', d, 'sep') for d in range(1, 6)]],
}


def month_grid(month='sep', pressed=None, large=False, tight=False, weeks=None):
    head = ''.join(f'<span style="text-align: center; font-size: {14 if large else 11}px; font-weight: 500; color: {C["INK3"]};">{d}</span>' for d in WD)
    rows = []
    for wk in (WEEKS[month] if weeks is None else WEEKS[month][weeks]):
        cs = []
        for kind, d, m in wk:
            is_sep = m == 'sep'
            cs.append(gcell(d, month=m if m in MONTHS else 'sep', kind=kind,
                            today=(is_sep and d == TODAY and kind != 'out'),
                            future=(is_sep and d > TODAY), pressed=(kind == 'in' and pressed == d), large=large, tight=tight))
        rows.append(f'<div style="display: grid; grid-template-columns: repeat(7, minmax(0, 1fr)); border-top: 1px solid {C["LINE_SOFT"]}; padding: 2px 0;">{"".join(cs)}</div>')
    return (f'<div style="display: grid; grid-template-columns: repeat(7, minmax(0, 1fr)); margin-top: {10 if large else 8}px; padding-bottom: 5px;">{head}</div>'
            f'<div style="display: flex; flex-direction: column; border-bottom: 1px solid {C["LINE_SOFT"]};">{"".join(rows)}</div>')


def list_link(large=True):
    return (f'<div style="display: flex; align-items: center; justify-content: space-between; height: 44px; margin-top: 2px; border-top: 1px solid {C["LINE_SOFT"]};">'
            f'<span style="font-size: {16 if large else 12.5}px; font-weight: 600; color: {C["BRAND"]};">목록으로 보기</span>{icon("right", 15, C["BRAND"], 2)}</div>')


def calendar_card(expanded=False, pressed=None, pad=14, month='sep', large=False, with_list_link=False,
                  states=None, since=None, status=None, review=2, scroll=False):
    """접힘(최근 7일 스트립) · 펼침(월 달력) 카드. 아래 인수는 접힘에만 쓴다(기본값이면 예전과 똑같은 결과).
    states = {날짜: (합계 글자, ✓, 이체, 0원 표시)} 기본 자료를 덮어쓸 칸 · since = 시작일(이전 칸은 옅은 빈 칸) ·
    status = 상태 줄 문장 · review = `확인할 내용 N개`(0이면 행 없음) · scroll = 320px(칸 44 고정 · 카드 안 가로 스크롤 · 오늘이 오른쪽 끝) ·
    large = 큰 글자(칸 높이 72)."""
    if not expanded:
        tfs, sfs, isz = (18, 15.5, 17) if large else (14, 12, 14)
        title = (f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px;">'
                 f'<span style="font-size: {tfs}px; font-weight: 600; color: {C["INK"]};">이번 달 달력</span>'
                 f'<span style="display: inline-flex; align-items: center; gap: 2px; font-size: {sfs}px; font-weight: 600; color: {C["INK2"]};">펼치기{icon("down", isz, C["INK2"], 2.2)}</span></div>')
        # 최근 7일 — 오늘이 오른쪽 끝 (9/2 ~ 9/8)
        cells = ''.join(cell(d, WD[(1 + d) % 7], pressed=(pressed == d), state=(states or {}).get(d),
                             before=(since is not None and d < since), large=large) for d in range(2, 9))
        if scroll:      # 칸 7개(308)가 안 들어가는 폭 — 칸을 줄이지 않고 오른쪽(오늘)부터 보이게 두고 왼쪽이 잘린다
            body = f'<div style="display: flex; justify-content: flex-end; overflow: hidden; margin-top: 8px;">{cells}</div>'
        else:
            body = f'<div style="display: flex; justify-content: space-between; margin-top: 8px;">{cells}</div>'
        tail = status_rows(review=review, large=large) if status is None else status_rows(review=review, text=status, large=large)
        return card(title + body + tail, pad=f'13px {pad}px 13px')
    if month == 'sep':
        bar = month_bar('2026년 9월', prev_on=True, next_on=False, large=large)
        status = f'9월 기록한 소비 {SEP_TOTAL:,}원 · 오늘 4건 37,000원'
    else:
        bar = month_bar('2026년 8월', prev_on=False, next_on=True, back_pill=True, large=large)
        status = f'8월 기록한 소비 {AUG_TOTAL:,}원'
    tail = status_rows(text=status, large=large) + (list_link(large) if with_list_link else '')
    return card(bar + month_grid(month, pressed, large) + tail, pad=f'13px {pad}px {4 if with_list_link else 13}px')


def calendar_thumb():
    """홈 구성(HomeSetup) 행의 축소 미리보기 — gen_v4.thumb() 과 같은 44 × 30 틀(INSET 바탕 · LINE_SOFT 테두리 · 반경 7).
    글자 없이 형태만: 최근 7일 스트립 7칸, 오늘이 오른쪽 끝이고 오늘 칸만 brand-soft 바탕. 칸마다 날짜 점 + 합계 막대
    (기록 없는 날 = 옅은 막대 — 자료 SEP 의 9/2 · 9/7 과 같은 자리)."""
    cells = []
    for i, d in enumerate(range(TODAY - 6, TODAY + 1)):
        today = d == TODAY
        empty = SEP.get(d) is None
        left = 3.2 + i * 5.2             # 안쪽 폭 42 에 7칸(4.4) + 간격 0.8 = 35.6 을 가운데로
        bar = C["INK"] if today else (C["INPUT"] if empty else C["INK4"])
        if today:
            cells.append(f'<span style="position: absolute; left: {left:.1f}px; top: 5px; width: 4.4px; height: 18px; border-radius: 2px; background: {C["BRAND_SOFT"]};"></span>')
        cells.append(
            f'<span style="position: absolute; left: {left + 1.2:.1f}px; top: 9px; width: 2px; height: 2px; border-radius: 99px; background: {C["INK4"]};"></span>'
            f'<span style="position: absolute; left: {left + 0.7:.1f}px; top: 16px; width: 3px; height: 3px; border-radius: 99px; background: {bar};"></span>')
    return (f'<div style="width: 44px; height: 30px; border-radius: 7px; background: {C["INSET"]}; border: 1px solid {C["LINE_SOFT"]}; '
            f'flex-shrink: 0; overflow: hidden; position: relative;">{"".join(cells)}</div>')
