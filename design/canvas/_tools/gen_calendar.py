# -*- coding: utf-8 -*-
"""홈 달력 카드 공용 조각 — 자료 · 칸 · 접힘 카드(최근 7일 스트립) · 펼침 월 달력 · 상태 줄 · 홈 구성 행 축소 미리보기.

plan/v5-calendar.md(9판). gen_v5.py 에서 옮겨 왔다 — gen_v4.py · gen_v4_stocks.py · gen_v5.py 가 함께 쓴다.
이 모듈은 gen_common 만 import 한다(gen_v4 · gen_v5 를 import 하면 순환). 파일을 쓰지 않는다(import 부작용 없음).

    from gen_calendar import calendar_card, calendar_thumb

달력 · 하루 시트에는 의미색(주황 · 빨강 · 가정 보라)을 쓰지 않는다 — 오늘 칸 brand-soft, 나머지는 잉크 단계뿐.
2026년 9월: 1일 화요일 · 30일 · 5주. 오늘 8일(화). 2026년 8월: 1일 토요일 · 31일 · 6주.
칸 숫자 = 그날 소비 합계(고정비 포함 · 이체 제외). 표기는 앱 formatSum과 같다(1만 미만 원 단위 · 1만 이상 만 단위 한 자리 ·
소수 첫 자리가 0이면 뗀다 — 3만 · 30만. 내역 날짜 머리글 `이체 30만`도 같은 함수).

2026-09-24(13판) — 이 카드가 「여기서 적는다」로 읽히게: 접힌 제목 `이번 달 소비 기록` + 안내 한 줄(접힘 · 펼침 둘 다) ·
오늘 칸은 늘 파란 안쪽 테두리 1.5px, 오늘 기록 0건(안 썼어요 아님)이면 `—` 대신 파란 원 `+` · 그때 상태 줄 자리에 가득 찬 폭 버튼
`+ 오늘 쓴 돈 적기`(40) · 기록이 있거나 안 썼어요 표시면 상태 문장 오른쪽에 알약 `+ 더 적기`/`+ 적기`, 그 줄 높이도 40(저장 전후 카드 높이 불변) ·
지난달을 보는 중이면 버튼 · 알약 없음. 9월 샘플은 9/1을 1,008,000원(관리비 · 공과금 · 보험 · 통신 등 — 월세 아님)으로 올려 9/1~9/8 합계가
히어로의 쓴 돈 1,120,000원(design/sample-data.json spendSoFar)과 같다.

2026-09-24 후속 — calendar_card(today_empty=True) = 오늘 기록 0건(states={TODAY: NO_RECORD}의 줄임) · 펼침도 states · since · review 를 따른다
(펼친 달력 · 오늘 0건 = 오늘을 뺀 합계 줄 + 버튼, 처음 쓰는 날 = since=TODAY 스트립 — 승인 그림에만 있던 두 상태 · CalendarStatusLines).
그 달 기록 0건의 합계 줄은 `9월 기록이 아직 없어요`(0원이라고 쓰지 않음), 안 썼어요 표시뿐이면 `안 썼어요 표시만 있어요`(앱 statusLine).
오늘 칸의 `+`에 이체 · ✓ 가 함께 있으면 `+`를 합계 자리에 겹쳐 놓는다(plus_slot · 앱과 같다).

2026-09-24 최종 점검 후속 — 접힌 스트립(보통 글자)의 수식어 줄 12 → 9(STRIP_MOD_H): 오늘 칸 안쪽 테두리와 요일 글자 사이 2px 이상 ·
이체 · ✓ 와 함께인 오늘 칸의 `+`는 지름 16 · 글자 10(큰 글자 20 · 12 — PLUS_WITH_MOD)이라 날짜 숫자와 `이체`에 닿지 않는다 ·
이체 · ✓ 가 없는 오늘 칸의 `+`(20 · 24)는 합계 + 수식어 자리 가운데에 두어 요일 · 날짜가 옆 칸과 같은 높이에 선다(원 위치는 그대로).
"""
from gen_common import C, icon, card

WD = ['일', '월', '화', '수', '목', '금', '토']
TODAY = 8


def fmt_sum(n):
    """앱 lib/navi-quick-entry.ts formatSum과 같은 규칙(시안 자료의 최댓값은 712,000 · 1억 이상은 Tokens 08의 견본용).
    소수 첫 자리가 0이면 `.0`을 뗀다 — 만 단위도 억 단위도(29,500 → `3만` · 300,000 → `30만` · 125,000 → `12.5만` 그대로 · 99,995,000 → `1억`)."""
    if n < 10_000:
        return f'{n:,}'
    if n < 1_000_000:
        t = int(n / 1000 + 0.5)          # JS Math.round와 같게 0.5는 올림(58,500 → 5.9만)
        if t < 1000:
            return f'{t // 10}만' if t % 10 == 0 else f'{t / 10:.1f}만'
    m = int(n / 10_000 + 0.5)            # 100만 이상은 정수 만 단위(5,000원에서 올림)
    if m < 10_000:
        return f'{m:,}만'
    e = int(n / 10_000_000 + 0.5)        # 1억 이상은 억 단위 소수 한 자리(500만원에서 올림) — 여기서도 `.0`은 뗀다(99,995,000 → `1억`)
    return f'{e // 10}억' if e % 10 == 0 else f'{e / 10:.1f}억'


# day -> 원 단위 합계. None = 아직 기록 없음(—). 0 = 안 썼어요로 표시한 날.
# 9월 1일 1,008,000 = 고정비(관리비 · 공과금 · 보험 · 통신 · 구독)와 한 달 장보기 등 — 행은 gen_screens.LEDGER_V5 의 9월 1일(카테고리 합이 소비 · 한도 장의 값과 같게).
# 월세는 없다 — 월세 700,000원은 9월 8일에 적는 장면(DaySheetConfirm · RecurringPrefill `결제일 8`)이다.
# 2026-09-24 전에는 12,000원이라 9월 합계가 124,000원이었고 히어로의 112만원과 두 샘플 세계로 갈라져 있었다.
SEP = {1: 1_008_000, 2: None, 3: 58_500, 4: 4_500, 5: 12_000, 6: 0, 7: None, 8: 37_000}
SEP_CHECK, SEP_TRANSFER = {1, 4, 5}, {6}
AUG = {1: 23_500, 2: 61_000, 3: 9_800, 4: 4_500, 5: 712_000, 6: 15_300, 7: 38_000, 8: 52_400, 9: 0, 10: 12_000,
       11: 6_700, 12: 89_000, 13: 4_500, 14: 27_600, 15: 118_000, 16: None, 17: 9_900, 18: 33_000, 19: 4_500,
       20: 64_500, 21: 17_800, 22: 72_000, 23: 41_200, 24: 5_600, 25: 68_000, 26: 8_900, 27: 29_500, 28: 96_000,
       29: 35_000, 30: None, 31: 55_000}
AUG_CHECK = {d for d, v in AUG.items() if v and d != 31}          # 0(안 썼어요)에는 ✓ 없음
AUG_TRANSFER = {6}                # 반복 거래 `ETF 자동이체` 매월 6일(RecurringPrefill · LedgerV5 9월 6일과 같은 날)
# 8월 25일 68,000 = 그날 쓴 13,000 + 자동 기록된 반복 거래 `휴대폰 요금` 55,000(매월 25일 · RecurringPrefill · DaySheetConfirm)
assert AUG[25] == 13_000 + 55_000
SEP_TOTAL = sum(v for v in SEP.values() if v)
assert SEP_TOTAL == 1_120_000      # = 히어로의 쓴 돈(sample-data.json spendSoFar) · 한도 `사용 112만원` · 소비 탭 `112만`
AUG_TOTAL = sum(v for v in AUG.values() if v)
assert AUG_TOTAL == 1_715_200      # 1,660,200 + 휴대폰 요금 55,000
MONTHS = {'sep': (SEP, SEP_CHECK, SEP_TRANSFER), 'aug': (AUG, AUG_CHECK, AUG_TRANSFER)}


def day_state(month, day):
    """(합계 글자, 확인 ✓, 이체 배지, 0원 표시 여부)"""
    data, checks, transfers = MONTHS[month]
    v = data.get(day)
    text = '—' if v is None else fmt_sum(v)
    return text, day in checks, day in transfers, v == 0


def _mods(chk, tr, size=11, fs=10, h=None):
    """수식어 줄(✓ · 이체). h = 줄 높이(기본 size + 1 — 월 달력 12 · 큰 글자 13). 접힌 스트립의 보통 글자는 STRIP_MOD_H(9)."""
    mods = []
    if chk: mods.append(icon("check", size, C["INK2"], 2.8))
    if tr: mods.append(f'<span style="font-size: {fs}px; line-height: 12px; font-weight: 500; color: {C["INK2"]};">이체</span>')
    # 접힌 스트립의 9px 줄: `이체`(줄 12)가 줄보다 커서 가운데에 두면 위로 삐져나와 오늘 칸의 16px + 원에 닿는다 —
    # 줄 안 가운데를 1px 내린다(border-box 9 · padding-top 2 · 앱 v5-calendar.css와 같은 값).
    pad = ' box-sizing: border-box; padding-top: 2px;' if h == STRIP_MOD_H else ''
    return f'<span style="display: inline-flex; align-items: center; gap: 3px; height: {h or size + 1}px;{pad} flex-shrink: 0;">{"".join(mods)}</span>'


# 접힌 스트립(보통 글자)의 수식어 줄 높이 — 12 → 9(2026-09-24 최종 점검 후속). 칸 44 × 56 · 간격 2 그대로, 요일 · 날짜 · 합계 · 수식어가
# 10 + 2 + 11 + 2 + 13 + 2 + 9 = 49 로 들어가 위아래 3.5씩 남는다 → 오늘 칸 안쪽 테두리(1.5px)와 요일 글자 사이가 2px 넘게 빈다(전에는 52 · 0.75px).
# 모든 칸에 같은 높이를 예약하므로 줄 안의 요일 · 날짜가 같은 높이에 선다. 큰 글자(72)는 간격 3 · 줄 13 그대로.
STRIP_MOD_H = 9


CARD_TITLE = '이번 달 소비 기록'          # 접힌 카드 제목(2026-09-24 — 전에는 `이번 달 달력`). 펼치면 머리줄이 `‹ 2026년 9월 ›`
HINT = '날짜를 누르면 그날 쓴 돈을 적어요'    # 머리줄 아래 안내 한 줄(접힘 · 펼침 둘 다 · 12px ink-3)
TODAY_RING = f'box-shadow: inset 0 0 0 1.5px {C["BRAND"]};'      # 오늘 칸(이번 달을 볼 때) — 기록이 있어도 없어도


def plus_badge(size=20, glyph=None):
    """오늘 · 기록 0건(안 썼어요 아님) 칸의 파란 원 `+` — 지름 20(큰 글자 24) · brand 바탕 · 흰 +(원 − 8 = 12 · 16). 다른 빈 날은 그대로 `—`.
    이체 · ✓ 와 함께면 지름 16(큰 글자 20) · 글자 10(12) — PLUS_WITH_MOD."""
    return (f'<span style="width: {size}px; height: {size}px; border-radius: 99px; background: {C["BRAND"]}; display: inline-flex; '
            f'align-items: center; justify-content: center; flex-shrink: 0;">{icon("plus", glyph or size - 8, "#FFFFFF", 2.8)}</span>')


# 오늘 칸 `+`에 이체 · ✓ 가 함께 있을 때(2026-09-24 최종 점검 후속): 지름 20 → 16 · 글자 10(큰 글자 24 → 20 · 12).
# 합계 자리에 겹쳐 놓아도 날짜 숫자와 `이체`에 닿지 않는다. 이체 · ✓ 가 없는 오늘 칸의 `+`는 그대로 20(24).
PLUS_WITH_MOD = {False: (16, 10), True: (20, 12)}


def plus_slot(h, size=20, glyph=None):
    """자리(높이 h) 가운데에 겹쳐 놓은 `+`. 이체 · ✓ 가 함께 있는 오늘 칸은 합계 자리(13)에 — 원은 자리 위아래로 조금 넘친다(앱 `.calendar-cell-sum-add`와 같다).
    이체 · ✓ 가 없는 오늘 칸은 합계 + 간격 + 수식어 줄을 합친 자리에 — 요일 · 날짜가 옆 칸과 같은 높이에 선다."""
    return (f'<span style="height: {h}px; display: flex; align-items: center; justify-content: center; overflow: visible; flex-shrink: 0;">'
            f'{plus_badge(size, glyph)}</span>')


NO_RECORD = ('—', False, False, False)      # 오늘 기록 0건 · 안 썼어요 아님 — 오늘 칸 `+` · 버튼 `+ 오늘 쓴 돈 적기`
MARKS_ONLY = '안 썼어요 표시만 있어요'      # 그 달 소비 기록이 0건이고 안 썼어요 표시만 있을 때 상태 줄 끝에(앱 statusLine note)


def month_total_text(m, total):
    """펼친 달력의 그 달 합계 한 줄 — 기록이 0건이면 `0원`이라고 쓰지 않는다(미입력은 0원이 아니다 · 앱 statusLine)."""
    return f'{m}월 기록이 아직 없어요' if total == 0 else f'{m}월 기록한 소비 {total:,}원'


def hint(large=False, mt=2):
    """머리줄 아래 안내 한 줄 — `날짜를 누르면 그날 쓴 돈을 적어요`(12px · ink-3 · 큰 글자 15)."""
    return f'<div style="font-size: {15 if large else 12}px; line-height: 1.45; color: {C["INK3"]}; margin-top: {mt}px;">{HINT}</div>'


def cell(day, wd=None, w_=44, pressed=False, prev=False, future=False, state=None, before=False, large=False):
    """스트립 칸(접힘 · 최근 7일). 44 × 56(큰 글자 72). 달 제목이 없는 자리라 지난달 날짜는 `8/31`처럼 달을 붙인다.
    state = (합계 글자, ✓, 이체, 0원 표시)를 직접 줄 때(저장 뒤 · 첫 기록처럼 기본 자료와 다른 장).
    before = 시작일(quickEntry.since) 이전 — `—` 없이 날짜만 옅게(누르면 열림).
    large = 큰 글자: 칸 높이 72 · 날짜 14.5 · 합계 12(스트립 칸 44는 47px에 못 미쳐 13이 아니라 12 — 계획 §3-2).
    오늘 칸은 늘 파란 안쪽 테두리 1.5px(누른 순간은 2px), 기록 0건 · 안 썼어요 아님이면 `—` 대신 파란 원 `+`(칸 크기 불변)."""
    is_today = day == TODAY and not prev
    label = f'8/{day}' if prev else str(day)
    h, fs_wd, fs_date, fs_sum, lh_sum, mod = (72, 12, 14.5, 12, 14, 12) if large else (56, 10, 11, 11, 13, 11)
    gap = 3 if large else 2
    mod_h = mod + 1 if large else STRIP_MOD_H          # 수식어 줄 — 보통 9 · 큰 글자 13
    bg = C["BRAND_SOFT"] if is_today else 'transparent'
    ring = f'box-shadow: inset 0 0 0 2px {C["BRAND"]};' if pressed else (TODAY_RING if is_today else '')
    blank = future or before
    date_col = C["INK4"] if blank else (C["INK"] if is_today else C["INK2"])
    parts = [f'<span style="font-size: {fs_date}px; line-height: 1; font-weight: {600 if is_today else 500}; color: {date_col};">{label}</span>']
    if not blank:
        s, chk, tr, zero = state if state is not None else day_state('aug' if prev else 'sep', day)
        if is_today and s == '—' and not zero:
            if chk or tr:       # 이체 · ✓ 가 붙으면 + 를 합계 자리(13px)에 겹쳐 놓는다 — 앱과 같다. 원은 16(큰 글자 20)이라 날짜 · `이체`에 닿지 않는다
                parts.append(plus_slot(lh_sum, *PLUS_WITH_MOD[large]))
                parts.append(_mods(chk, tr, size=mod, fs=mod - 1, h=mod_h))
            else:               # 합계 + 간격 + 수식어 줄 자리 가운데 — 칸 안 높이가 옆 칸과 같아 요일 · 날짜가 같은 높이에 선다(원 위치는 전과 같다)
                parts.append(plus_slot(lh_sum + gap + mod_h, 24 if large else 20))
        else:
            col = C["INK3"] if s == '—' else (C["INK2"] if zero else C["INK"])
            parts.append(f'<span style="font-size: {fs_sum}px; line-height: {lh_sum}px; font-weight: 600; color: {col}; font-variant-numeric: tabular-nums;">{s}</span>')
            parts.append(_mods(chk, tr, size=mod, fs=mod - 1, h=mod_h))
    else:
        parts.append(f'<span style="height: {lh_sum}px; flex-shrink: 0;"></span><span style="height: {mod_h}px; flex-shrink: 0;"></span>')
    wdl = f'<span style="font-size: {fs_wd}px; line-height: 1; font-weight: 500; color: {C["INK3"]};">{wd}</span>' if wd else ''
    # 칸 사이 간격 2(큰 글자 3) · 수식어 줄 9(큰 글자 13) — 요일 · 날짜 · 합계 · 수식어가 56 안에 49 로 들어가 오늘 칸의 안쪽 테두리(1.5px)와
    # 요일 글자 사이가 2px 넘게 빈다(2026-09-24 최종 점검 후속 · 그 전 52 → 0.75px · 처음 55)
    return (f'<div style="width: {w_}px; height: {h}px; border-radius: 10px; background: {bg}; {ring} display: flex; flex-direction: column; align-items: center; justify-content: center; gap: {gap}px; flex-shrink: 0;">'
            f'{wdl}{"".join(parts)}</div>')


def gcell(day, month='sep', kind='in', today=False, future=False, pressed=False, large=False, tight=False, state=None):
    """월 달력 칸. 폭은 7등분(1fr) · 높이 56(큰 글자 72). 위에서부터 날짜 · 합계 · 수식어.
    kind: 'in' 이번에 보는 달 · 'adj' 이웃 달(옅은 숫자, 기록은 옅게 보이고 누르면 그 날짜 시트) · 'out' 홈 범위 밖이나 미래(숫자만, 누를 수 없음).
    today = 오늘 칸(이번 달을 볼 때) — 파란 안쪽 테두리 1.5px, 기록 0건 · 안 썼어요 아님이면 `—` 대신 파란 원 `+`. state = 자료를 덮어쓸 때."""
    h = 72 if large else 56
    # tight = 칸 폭이 47px에 못 미치는 곳(360 · 320 펼침): 큰 글자 합계를 13 → 12로 한 단계 낮춰 `71.2만`이 잘리지 않게 한다
    fs_date, fs_sum, mod = ((14.5, 12 if tight else 13, 12 if tight else 13) if large else (12, 11, 11))
    blank = future or kind == 'out'
    bg = C["BRAND_SOFT"] if today else 'transparent'
    ring = f'box-shadow: inset 0 0 0 2px {C["BRAND"]};' if pressed else (TODAY_RING if today else '')
    if blank or kind == 'adj':
        date_col, weight = C["INK4"], 500
    else:
        date_col, weight = (C["INK"], 700) if today else (C["INK2"], 500)
    parts = [f'<span style="font-size: {fs_date}px; font-weight: {weight}; color: {date_col}; line-height: 1.2;">{day}</span>']
    if blank:
        parts.append(f'<span style="height: {fs_sum + 2}px;"></span><span style="height: {mod + 1}px;"></span>')
    else:
        s, chk, tr, zero = state if state is not None else day_state(month, day)
        if today and kind == 'in' and s == '—' and not zero:
            sum_h = round(fs_sum * 1.2, 1)      # 합계 줄 높이(line-height 1.2) — 옆 칸과 같은 자리
            if chk or tr:       # 이체 · ✓ 와 함께 — 원 16(큰 글자 20)을 합계 자리에 겹쳐 놓고 수식어 줄은 그대로(스트립 · 앱과 같다)
                parts.append(plus_slot(sum_h, *PLUS_WITH_MOD[large]))
                parts.append(_mods(chk, tr, size=mod, fs=mod - 1))
            else:               # 합계 + 간격 + 수식어 줄 자리 가운데 — 날짜가 옆 칸과 같은 높이(원 위치는 전과 같다)
                parts.append(plus_slot(round(sum_h + (3 if large else 2) + mod + 1, 1), 24 if large else 20))
        else:
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


def month_bar(label, prev_on, next_on, back_pill=False, large=False, pill_below=False, label_w=None, fold=True):
    """펼친 달력의 머리줄 — ‹ 2026년 9월 › · (지난달을 볼 때) 이번 달로 · 접기. 이동 범위는 이번 달 + 지난달(하루 시트 범위와 같다).
    fold=False = `접기`가 없는 머리줄(늘 펼쳐 두는 데스크톱 홈 — DesktopHomeV5). 오른쪽에 둘 것이 없으면 오른쪽 묶음도 그리지 않는다."""
    size = 40 if large else 32
    fs, tfs = (19, 15.5) if large else (15, 12)
    pill = (f'<span style="font-size: {tfs}px; font-weight: 600; color: {C["BRAND"]}; background: {C["BRAND_SOFT"]}; border-radius: 99px; '
            f'padding: 5px 10px; white-space: nowrap;">이번 달로</span>') if back_pill else ''
    below = ''
    if back_pill and (pill_below or large):      # 334px 안에 머리줄 + 알약이 들어가지 않는 경우
        below = f'<div style="display: flex; justify-content: flex-end; margin-top: 6px;">{pill}</div>'
        pill = ''
    toggle = (f'<span style="display: inline-flex; align-items: center; gap: 2px; font-size: {tfs}px; font-weight: 600; color: {C["INK2"]}; white-space: nowrap;">'
              f'접기{icon("up", 14 if not large else 17, C["INK2"], 2.2)}</span>') if fold else ''
    right = f'<div style="display: flex; align-items: center; gap: 8px;">{pill}{toggle}</div>' if (pill or toggle) else ''
    return (f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 6px; min-height: {size}px;">'
            f'<div style="display: flex; align-items: center; gap: 4px;">{nav_btn("left", prev_on, size)}'
            f'<span style="min-width: {label_w or (118 if large else 94)}px; text-align: center; font-size: {fs}px; font-weight: 700; letter-spacing: -0.015em; color: {C["INK"]}; white-space: nowrap;">{label}</span>'
            f'{nav_btn("right", next_on, size)}</div>'
            f'{right}</div>{below}')


STATUS_FS, STATUS_FS_L = 12.5, 16          # 상태 문장 글자(큰 글자) — 2026-09-24 에 11 → 12.5 (버튼 · 알약과 나란히 읽히게 · 승인 그림 그대로)
ROW_H, ROW_H_L = 40, 48                    # 버튼 높이 = 알약 줄 높이(큰 글자 48) — 저장 전후 카드 높이가 변하지 않는다


def status_line(text, large=False, mt=8):
    """상태 문장 한 줄 — 펼친 달력의 그 달 합계(`9월 기록한 소비 N원`), 버튼 위 안내(저녁 · 샘플 · 풀림 · 미래)."""
    return f'<div style="font-size: {STATUS_FS_L if large else STATUS_FS}px; line-height: 1.5; color: {C["INK2"]}; margin-top: {mt}px;">{text}</div>'


def add_button(large=False, mt=10):
    """오늘 기록 0건(안 썼어요 아님) — 가득 찬 폭 버튼 `+ 오늘 쓴 돈 적기`(누르면 오늘 하루 시트). 높이 40 · 반경 12 · brand-soft · brand 14/700
    (큰 글자 48 · 14 · 16.5). 앱은 button 요소."""
    h, r, fs, isz = (ROW_H_L, 14, 16.5, 18) if large else (ROW_H, 12, 14, 16)
    return (f'<div style="display: flex; align-items: center; justify-content: center; gap: 6px; height: {h}px; margin-top: {mt}px; border-radius: {r}px; '
            f'background: {C["BRAND_SOFT"]}; color: {C["BRAND"]}; font-size: {fs}px; font-weight: 700; white-space: nowrap;">{icon("plus", isz, C["BRAND"], 2.6)}오늘 쓴 돈 적기</div>')


def more_pill(label='더 적기', large=False):
    """오늘 기록이 있으면 `+ 더 적기`, 안 썼어요 표시면 `+ 적기` — 높이 32 · brand-soft · brand 13/700(큰 글자 38 · 15)."""
    h, fs, isz, px = (38, 15, 16, 14) if large else (32, 13, 14, 12)
    return (f'<span style="display: inline-flex; align-items: center; gap: 4px; height: {h}px; padding: 0 {px}px; border-radius: 99px; background: {C["BRAND_SOFT"]}; '
            f'color: {C["BRAND"]}; font-size: {fs}px; font-weight: 700; white-space: nowrap; flex-shrink: 0;">{icon("plus", isz, C["BRAND"], 2.6)}{label}</span>')


def pill_row(text, large=False, label='더 적기', mt=10):
    """상태 문장 + 오른쪽 알약. 줄 높이를 버튼과 같은 40(큰 글자 48)으로 둔다 — 문장이 두 줄이 되어도 그 안에 든다."""
    return (f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 10px; min-height: {ROW_H_L if large else ROW_H}px; margin-top: {mt}px;">'
            f'<span style="flex: 1; min-width: 0; font-size: {STATUS_FS_L if large else STATUS_FS}px; line-height: 1.5; color: {C["INK2"]};">{text}</span>'
            f'{more_pill(label, large)}</div>')


def today_tail(today_state, text=None, large=False, mt=10):
    """상태 줄 자리. today_state = 오늘 칸 (글자, ✓, 이체, 0원 표시).
    기록 0건 · 안 썼어요 아님 → 가득 찬 폭 버튼(안내 문장이 있으면 버튼 위에 그대로 — `오늘 아직 기록이 없어요`는 버튼이 대신한다).
    그 밖 → 문장 + 알약(`+ 더 적기` · 안 썼어요 표시면 `+ 적기`)."""
    s, _, _, zero = today_state
    if s == '—' and not zero:
        if text:
            return status_line(text, large, mt=mt - 2) + add_button(large, mt=6)
        return add_button(large, mt=mt)
    return pill_row(text or '', large, label='적기' if zero else '더 적기', mt=mt)


def review_row(review, large=False):
    """`확인할 내용 N개 ›` 행(0이면 없음) — 버튼 · 알약 줄 아래."""
    if not review:
        return ''
    rfs, rh = (16, 44) if large else (12.5, 32)
    return (f'<div style="display: flex; align-items: center; justify-content: space-between; height: {rh}px; margin-top: 6px; border-top: 1px solid {C["LINE_SOFT"]};">'
            f'<span style="font-size: {rfs}px; font-weight: 600; color: {C["INK"]};">확인할 내용 {review}개</span>{icon("right", 15, C["INK4"], 2)}</div>')


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


def month_grid(month='sep', pressed=None, large=False, tight=False, weeks=None, today_state=None, states=None, since=None):
    """states = {날짜: (합계 글자, ✓, 이체, 0원 표시)} 이번 달(9월) 칸을 덮어쓸 때(today_state 는 오늘 칸만 — 예전 인수).
    since = 시작일(quickEntry.since) — 9월 그 날짜 전 칸과 앞 이웃 달(8월) 칸은 합계 없이 날짜만 옅게(스트립의 before 와 같은 모양)."""
    states = dict(states or {})
    if today_state is not None:
        states.setdefault(TODAY, today_state)
    head = ''.join(f'<span style="text-align: center; font-size: {14 if large else 11}px; font-weight: 500; color: {C["INK3"]};">{d}</span>' for d in WD)
    rows = []
    for wk in (WEEKS[month] if weeks is None else WEEKS[month][weeks]):
        cs = []
        for kind, d, m in wk:
            is_sep = m == 'sep'
            before = since is not None and month == 'sep' and (m == 'aug' or (is_sep and d < since))
            cs.append(gcell(d, month=m if m in MONTHS else 'sep', kind=kind,
                            today=(is_sep and d == TODAY and kind != 'out'),
                            future=(is_sep and d > TODAY) or before, pressed=(kind == 'in' and pressed == d), large=large, tight=tight,
                            state=(states.get(d) if (is_sep and kind == 'in') else None)))
        rows.append(f'<div style="display: grid; grid-template-columns: repeat(7, minmax(0, 1fr)); border-top: 1px solid {C["LINE_SOFT"]}; padding: 2px 0;">{"".join(cs)}</div>')
    return (f'<div style="display: grid; grid-template-columns: repeat(7, minmax(0, 1fr)); margin-top: {10 if large else 8}px; padding-bottom: 5px;">{head}</div>'
            f'<div style="display: flex; flex-direction: column; border-bottom: 1px solid {C["LINE_SOFT"]};">{"".join(rows)}</div>')


def list_link(large=True):
    return (f'<div style="display: flex; align-items: center; justify-content: space-between; height: 44px; margin-top: 2px; border-top: 1px solid {C["LINE_SOFT"]};">'
            f'<span style="font-size: {16 if large else 12.5}px; font-weight: 600; color: {C["BRAND"]};">목록으로 보기</span>{icon("right", 15, C["BRAND"], 2)}</div>')


TODAY_TEXT = '오늘 4건 37,000원'          # 기본 자료의 오늘(9/8) — 하루 시트 둘째 줄 · LedgerV5 9월 8일과 같다


def calendar_card(expanded=False, pressed=None, pad=14, month='sep', large=False, with_list_link=False,
                  states=None, since=None, status=None, review=2, scroll=False, fold=True, today_empty=False, month_total=None):
    """접힘(최근 7일 스트립) · 펼침(월 달력) 카드. 기본값이면 예전과 똑같은 결과.
    states = {날짜: (합계 글자, ✓, 이체, 0원 표시)} 기본 자료를 덮어쓸 칸 · since = 시작일(이전 칸은 옅은 빈 칸) ·
    status = 상태 문장(접힘) · review = `확인할 내용 N개`(0이면 행 없음) · scroll = 320px(칸 44 고정 · 카드 안 가로 스크롤 · 오늘이 오른쪽 끝) ·
    large = 큰 글자(칸 높이 72). fold=False(펼침에만) = 머리줄에 `접기`를 두지 않는다 — 늘 펼쳐 두는 데스크톱 홈.
    today_empty = 오늘 기록 0건(안 썼어요 아님) — states={TODAY: NO_RECORD}의 줄임. 오늘 칸 `+` · 버튼 `+ 오늘 쓴 돈 적기`.
    펼침(9월)도 states · since · review 를 따른다(2026-09-24 보강) — 그 달 합계 줄은 덮어쓴 칸을 빼고 다시 센다
    (`—` · 0 칸은 0원, 금액을 덮어쓴 칸이 있으면 month_total 로 합계를 준다). 합계가 0이면 `9월 기록이 아직 없어요`,
    그 달이 안 썼어요 표시뿐이면 `안 썼어요 표시만 있어요`를 붙인다(버튼일 때는 합계 줄 끝 · 알약일 때는 오늘 줄 끝 — 앱 calendar-card).
    상태 줄 자리(2026-09-24): 오늘 기록 0건(안 썼어요 아님)이면 버튼 `+ 오늘 쓴 돈 적기`, 아니면 문장 + 알약 `+ 더 적기` — 둘 다 높이 40."""
    if today_empty:
        states = {**(states or {}), TODAY: NO_RECORD}
    if not expanded:
        tfs, sfs, isz = (18, 15.5, 17) if large else (14, 12, 14)
        title = (f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px;">'
                 f'<span style="font-size: {tfs}px; font-weight: 600; color: {C["INK"]};">{CARD_TITLE}</span>'
                 f'<span style="display: inline-flex; align-items: center; gap: 2px; font-size: {sfs}px; font-weight: 600; color: {C["INK2"]};">펼치기{icon("down", isz, C["INK2"], 2.2)}</span></div>')
        # 최근 7일 — 오늘이 오른쪽 끝 (9/2 ~ 9/8)
        cells = ''.join(cell(d, WD[(1 + d) % 7], pressed=(pressed == d), state=(states or {}).get(d),
                             before=(since is not None and d < since), large=large) for d in range(2, 9))
        if scroll:      # 칸 7개(308)가 안 들어가는 폭 — 칸을 줄이지 않고 오른쪽(오늘)부터 보이게 두고 왼쪽이 잘린다
            body = f'<div style="display: flex; justify-content: flex-end; overflow: hidden; margin-top: 10px;">{cells}</div>'
        else:
            body = f'<div style="display: flex; justify-content: space-between; margin-top: 10px;">{cells}</div>'
        today = (states or {}).get(TODAY) or day_state('sep', TODAY)
        text = status if status is not None else (TODAY_TEXT if TODAY not in (states or {}) else None)
        tail = today_tail(today, text, large=large) + review_row(review, large)
        return card(title + hint(large) + body + tail, pad=f'13px {pad}px 13px')
    over = dict(states or {}) if month == 'sep' else {}
    if month == 'sep':
        bar = month_bar('2026년 9월', prev_on=True, next_on=False, large=large, fold=fold)
        kept = {d: v for d, v in SEP.items() if d not in over and not (since is not None and d < since)}
        if month_total is None:
            assert all(t in ('—', '0') for t, _, _, _ in over.values()), '금액을 덮어쓴 칸이 있으면 month_total 을 준다'
            month_total = sum(v for v in kept.values() if v)
        marks_only = month_total == 0 and (any(v == 0 for v in kept.values()) or any(z for _, _, _, z in over.values()))
        today = over.get(TODAY) or day_state('sep', TODAY)
        add = today[0] == '—' and not today[3]
        head = month_total_text(9, month_total) + (f' · {MARKS_ONLY}' if marks_only and add else '')
        text = None if add else (status if status is not None else (TODAY_TEXT if TODAY not in over else
                                                                     ('오늘은 안 썼다고 표시했어요' if today[3] else None)))
        if marks_only and not add:
            text = f'{text} · {MARKS_ONLY}' if text else MARKS_ONLY
        tail = status_line(head, large, mt=8) + today_tail(today, text, large=large, mt=8)
    else:           # 지난달을 보는 중 — 버튼 · 알약 없음
        bar = month_bar('2026년 8월', prev_on=False, next_on=True, back_pill=True, large=large, fold=fold)
        tail = status_line(month_total_text(8, AUG_TOTAL), large, mt=8)
    tail += review_row(review, large) + (list_link(large) if with_list_link else '')
    return card(bar + hint(large, mt=6) + month_grid(month, pressed, large, states=over, since=since) + tail,
                pad=f'13px {pad}px {4 if with_list_link else 13}px')


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
