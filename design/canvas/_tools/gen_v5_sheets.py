# -*- coding: utf-8 -*-
"""v5 · 하루 시트 · 완료 카드 · 상태 줄의 빠진 장 — 2026-09-20 최신화 점검(rank 4 · 5 · 15 · 16 · 32).

앱 화면 2장(390 × 844)
  DaySheetNoSpend        하루 시트 · 소비 0건인 날(이체만 있는 오늘) — 맨 아래 `오늘은 안 썼어요`
  ReviewListSheet        `확인할 내용 2개 ›`를 누르면 열리는 목록 시트
구현 참고 장 4장(spec_frame · 앱 화면이 아님)
  DaySheetNoSpendStates  `오늘은 안 썼어요`의 경우들(누르기 전 · 누른 뒤 · 확인한 날을 다시 열었을 때 · 소비가 있는 날)
  DoneCardStates         완료 카드의 경우들(제목 3종 · 셋째 줄 우선순위 · 월급 미입력 · 취소 결과 · 취소 비활성)
  DaySheetStates         하루 시트의 조건부 문구와 입력 한계(둘째 줄 4종 · 빈 금액 · 저장 충돌 · 메모 카운터 · 전체 › 펼침 · 주 선택기 · 샘플 모드)
  CalendarStatusLines    달력 상태 줄의 경우들

앱 문구는 plan/v5-calendar.md(9판) 원문 그대로. gen_v5 의 조각과 w()(라이트 + 다크 짝)를 그대로 쓴다.
(import gen_v5 는 v5 장을 모두 다시 쓴다 — 멱등.)

    python3 gen_v5_sheets.py
"""
from gen_common import *
import gen_v5 as v5
from gen_v5 import (w, won, mark, spec_frame, case_cap, sample, memo_row, sheet_header, sheet_frame, amount_field, memo_field,
                    category_row, cat_chip, recent_row, recent_chip, RECENT, save_btn, links_row, day_done_btn, tx_row, field_label,
                    unsaved_line, neutral_notice, nowrap_btn, scrim_line, SCRIM_H, day_done, labeled, date_box, later_pill,
                    EFFECT_DONE_TODAY, EFFECT_DONE_PAST, EFFECT_ZERO_TODAY, EFFECT_ZERO_PAST, DONE_MAIN, DONE_CHIPS, done_chip,
                    CANON_SLOTS, DEMO_SLOTS, sheet_body, links_block)
from gen_calendar import (fmt_sum, WD, TODAY, WEEKS, SEP_TOTAL, cell, calendar_card, month_bar, month_grid, hint, status_line, today_tail, pill_row,
                          day_state, STATUS_FS, TODAY_TEXT, NO_RECORD, MARKS_ONLY, month_total_text, review_row as cal_review_row,
                          RECENT_TITLE, REVIEW_UNCAT, REVIEW_RECLOSE, REVIEW_PREV_UNCAT, legend)
# cal_review_row = 달력 카드의 `확인할 내용 N개 ›` 행. 이 파일의 review_row 는 확인할 내용 목록 시트(ReviewListSheet)의 행이라 다르다.

NEW = ['DaySheetNoSpend', 'DaySheetNoSpendStates', 'ReviewListSheet', 'DoneCardStates', 'DaySheetStates', 'CalendarStatusLines']

BRAND_LINK = f'font-weight: 600; color: {C["BRAND"]}; white-space: nowrap;'


def blink(text):
    return f'<span style="{BRAND_LINK}">{text}</span>'


# ══════════════ 공용 조각 ══════════════
def sheet_box(inner, cropped=False):
    """참고 장 안에 놓는 하루 시트(폭은 부모를 따른다). cropped = 머리줄만 잘라 보여 줄 때 — 아래 테두리 없이."""
    rad, bb = ('26px 26px 0 0', 'border-bottom: none;') if cropped else ('26px 26px 18px 18px', '')
    return (f'<div style="background: {C["SURF"]}; border: 1px solid {C["LINE"]}; {bb} border-radius: {rad}; overflow: hidden; '
            f'display: flex; flex-direction: column;">{inner}</div>')


def skip_band(text='금액 · 메모 · 카테고리 · 저장 — 기본 시트와 같아요'):
    """견본에서 입력 칸을 생략했다는 표시(앱에 없는 설명 띠)."""
    return (f'<div style="height: 32px; border-radius: 10px; border: 1px dashed {C["BORDER"]}; display: flex; align-items: center; justify-content: center; '
            f'font-size: 11px; color: {C["INK3"]}; flex-shrink: 0;">{text}</div>')


LIST_H = 44          # 카드 없는 `오늘 기록` 목록의 행 높이 — gen_v5.today_list 와 같다(카드 안 목록인 DaySheetList 만 46)


def transfer_row(cat, memo, amount, last=True, h=LIST_H):
    """하루 시트 목록의 이체 행 — 앱 b574373 (d): 메모 아래에 `소비율 제외` 배지(메모 · 배지가 한 열 · 사이 3), 메모는 낱말 단위로 두 줄까지.
    줄 높이는 내용을 따른다(최소 44 · 위아래 6 → 한 줄 메모면 52). 금액은 회색(ink-3). 카테고리 이름은 화면 글자 `저축·투자`(저장 키 `저축/투자`).
    ›를 누르면 자세한 `기록 수정` 창이 열린다. 분류 칸 96 · 메모 열이 소비 행과 같은 자리에서 시작한다(gen_v5.tx_row)."""
    bb = '' if last else f'border-bottom: 1px solid {C["LINE_ROW"]};'
    return (f'<div style="display: flex; align-items: center; gap: 10px; min-height: {h}px; padding: 6px 0; flex-shrink: 0; {bb}">'
            f'<span style="display: inline-flex; align-items: center; gap: 6px; width: 96px; flex-shrink: 0;"><span style="width: 8px; height: 8px; border-radius: 99px; background: {CAT[cat]};"></span>'
            f'<span style="font-size: 12.5px; font-weight: 500; color: {C["INK2"]}; white-space: nowrap;">{cat.replace("/", "·")}</span></span>'
            f'<span style="flex: 1; min-width: 0; display: flex; flex-direction: column; align-items: flex-start; gap: 3px;">'
            f'<span style="font-size: 14px; line-height: 18.9px; color: {C["INK"]}; word-break: keep-all;">{memo}</span>'
            f'<span style="font-size: 11px; font-weight: 600; line-height: 15.71px; color: {C["INK3"]}; background: {C["LINE_SOFT"]}; border-radius: 99px; padding: 1px 6px; white-space: nowrap;">소비율 제외</span></span>'
            f'<span style="font-size: 14.5px; font-weight: 600; letter-spacing: -0.02em; color: {C["INK3"]}; white-space: nowrap; flex-shrink: 0;">{won(amount)}</span>{icon("right", 15, C["INK4"], 2)}</div>')


def list_block(rows, label='오늘 기록'):
    """앱 section.day-sheet-list — 제목 17 · 8 아래 행."""
    return (f'<div style="display: flex; flex-direction: column; gap: 8px; flex-shrink: 0;">{field_label(label)}'
            f'<div style="display: flex; flex-direction: column;">{rows}</div></div>')


def hint_line(text):
    """금액 아래 한 줄(회색 11.5) — unsaved_line 과 같은 자리 · 같은 모양."""
    return f'<div style="font-size: 11.5px; line-height: 16.675px; color: {C["INK3"]}; padding: 0 2px; flex-shrink: 0;">{text}</div>'


EMPTY_AMOUNT = ''          # 빈 금액 칸은 `원`만(회색 0 없음 · 앱)
SAVE_OFF = btn('저장', 'disabled', h=52, radius=14, size=16)
NO_SPEND_HINT = '금액을 넣거나, 안 썼으면 「오늘은 안 썼어요」로 표시해요'                                   # 계획 §8 금액 0 · 빈 금액
SUB_TRANSFER = '오늘 소비는 아직 기록이 없어요 · 이체 300,000원(소비율 제외)'                            # 계획 §8 이체만 있는 날
SUB_MARKED = '오늘은 안 썼어요 · 0원 기록은 만들지 않아요'                                              # 앱 문구(record-11 · D4 기록)
CONFIRMED = f'안 썼다고 표시했어요 · {blink("표시 풀기")}'                                                 # 앱 문구
HINT_RECORD_DAY = '금액을 넣으면 저장할 수 있어요'                                                       # 기록이 있는 날 · 표시한 날의 빈 금액(a11y-1 · record-18)
# 소비 0건 · 적금 이체만 있는 오늘(W/tools/dz4/app/log-all.json DaySheetNoSpend) — 앱 recentEntries · 자주 쓴 카테고리 그대로
RECENT_NS = [('커피', 4500, None), ('버스', 4500, None), ('', 3000, None), ('택시', 45000, '교통'), ('점심', 9000, '식비')]
FREQ_NS = ('식비', '교통', '쇼핑')      # 앱 categorySlots — 캐논에서 9월 8일 소비를 빼고 적금 이체만 둔 날(하네스 2026-09-27 · 오늘 카페/간식 · 쇼핑이 빠져 교통이 둘째)


# ══════════════ 1. DaySheetNoSpend — 소비 0건인 날(앱 화면) ══════════════
# 다른 장의 오늘(4건 37,000원)과 다른 사람의 오늘이다 — 소비 0건 · 적금 이체 300,000원만 있는 날. 키보드를 내린 상태(맨 아래 버튼이 보이게).
def no_spend_body(pad=18, sub=SUB_TRANSFER, button=True, marks=False):
    m = (lambda n: mark(n, pos='position: absolute; top: -6px; right: -6px;')) if marks else (lambda n: '')
    sub_html = sub + (mark(1, pos='margin-left: 6px; vertical-align: -3px;') if marks else '')
    bottom = (f'<div style="position: relative; flex-shrink: 0;">{day_done("오늘은 안 썼어요", EFFECT_ZERO_TODAY)}{m(3)}</div>' if button else '')
    return (sheet_header('9월 8일 소비 기록', sub_html)
            + sheet_body(amount_field(EMPTY_AMOUNT, focused=False)
                         + hint_line(NO_SPEND_HINT)
                         + memo_field('')
                         + category_row(None, frequent=FREQ_NS)
                         + recent_row([recent_chip(*r) for r in RECENT_NS], pad)
                         + f'<div style="margin-top: 2px; flex-shrink: 0;">{SAVE_OFF}</div>'
                         + links_block()
                         + f'<div style="position: relative; flex-shrink: 0;">{list_block(transfer_row("저축/투자", "적금", 300000))}{m(2)}</div>'
                         + bottom))


w('DaySheetNoSpend', sheet_frame(no_spend_body(), fit=True), keep_all=True)      # 시트는 내용 높이(앱)


# ══════════════ 2. DaySheetNoSpendStates — `오늘은 안 썼어요`의 경우들(구현 참고 장) ══════════════
def mini_sheet(sub, below, title='9월 8일 소비 기록'):
    return sheet_box(sheet_header(title, sub)
                     + f'<div style="padding: 12px 18px 16px; display: flex; flex-direction: column; gap: 10px;">{skip_band()}{below}</div>')


# 홈 달력의 오늘 칸(2026-09-24 — 기록 0건인 오늘은 `—`가 아니라 파란 `+`). 이체가 있으면 칸 아래에 `이체`가 붙는다.
PLUS, PLUS_TR = NO_RECORD, ('—', False, True, False)          # 오늘 · 소비 0건(표시 전) — 이체 없음 / 이체만 있음
ZERO_TR = ('0', False, True, True)                            # `오늘은 안 썼어요`로 표시한 뒤(이체만 있는 날)


def today_cell_note(states, label='홈 달력의 오늘 칸'):
    """달력의 오늘 칸 — 글로 설명하지 않고 칸 그대로 보여 준다. states 가 둘이면 전 → 뒤."""
    cells = f'<span style="display: inline-flex; flex-shrink: 0;">{icon("right", 14, C["INK4"], 2.2)}</span>'.join(
        cell(TODAY, '화', state=st_) for st_ in states)
    return (f'<div style="display: flex; align-items: center; gap: 10px; padding: 8px 12px; background: {C["INSET"]}; border-radius: 12px;">{cells}'
            f'<span style="font-size: 12px; line-height: 1.5; color: {C["INK2"]}; margin-left: 2px;">{label}</span></div>')


ns_left = (
    f'<div style="width: 362px; flex-shrink: 0; display: flex; flex-direction: column; gap: 8px;">'
    + sheet_box(no_spend_body(marks=True).replace('flex: 1; min-height: 0; overflow: hidden; padding: 12px 18px 21px;', 'padding: 12px 18px 16px;', 1))
    + f'<p style="margin: 2px 2px 0; font-size: 12px; line-height: 1.5; color: {C["INK3"]};">그림은 '
      f'<b style="font-weight: 600; color: {C["INK2"]};">소비는 없고 적금 이체만 있는 오늘</b>입니다. 바뀌는 자리는 둘째 줄 · 목록 · 맨 아래 버튼 세 곳입니다.</p></div>')
assert ns_left.count('padding: 12px 18px 16px;') == 1

NS_CASES = [
    (1, '소비도 이체도 없는 날', '목록 없이 맨 아래에 버튼과 효과 줄만 보입니다. 달력의 오늘 칸은 파란 +입니다.',
     mini_sheet('오늘 소비는 아직 기록이 없어요', day_done('오늘은 안 썼어요', EFFECT_ZERO_TODAY) + today_cell_note([PLUS]))),
    (3, '버튼을 누른 뒤', '저장 완료 카드도 토스트도 없습니다. 오늘 칸의 파란 +가 0으로 바뀌는 것이 확인입니다. 버튼은 사라지고 금액 아래 글은 「금액을 넣으면 저장할 수 있어요」입니다.',
     mini_sheet(SUB_MARKED + f'<span style="display: block; margin-top: 2px;">{CONFIRMED}</span>',
                list_block(transfer_row('저축/투자', '적금', 300000)) + today_cell_note([PLUS_TR, ZERO_TR], '누르기 전 → 누른 뒤'))),
    (1, '안 썼다고 표시한 날을 다시 열었을 때', '표시 풀기를 누르면 오늘 칸이 0에서 다시 파란 +로 돌아갑니다. 이체가 있으면 + 아래에 이체가 남습니다.',
     mini_sheet(SUB_MARKED + f'<span style="display: block; margin-top: 2px;">{CONFIRMED}</span>',
                list_block(transfer_row('저축/투자', '적금', 300000)) + today_cell_note([ZERO_TR, PLUS_TR], '표시 풀기를 누르면'))),
    (3, '소비가 한 건이라도 있는 날', '자동으로 기록된 고정비뿐이어도 이 버튼 대신 다 적었어요가 보입니다.',
     mini_sheet('오늘 1건 10,900원',
                list_block(tx_row('구독', '음악 구독', 10900, last=True, h=LIST_H)) + day_done('9월 8일 다 적었어요', EFFECT_DONE_TODAY))),
]
NS_MEMO = [
    (1, '둘째 줄은 그날 소비 합계 자리입니다. 소비가 0건이면 합계 대신 이 문장이 오고, 이체가 있으면 이체 금액을 (소비율 제외)와 함께 덧붙입니다. 지난 빈 날은 「9월 7일 소비는 아직 기록이 없어요」 · 버튼 「9월 7일은 안 썼어요」 · 효과 줄 「누르면 달력에 0으로 남아요 · 빈 날(—)과 구분돼요」입니다.'),
    (2, '이체 · 상환 행은 메모 아래 소비율 제외 배지(메모는 낱말 단위로 두 줄까지 · 줄은 내용만큼 높아짐)와 회색 금액으로 그립니다. 칸 숫자에도 소비 합계에도 들어가지 않습니다. ›를 누르면 자세한 기록 수정 창(기록 종류 · 계좌까지)이 열리고, 저장하면 홈에 「고쳤어요」가 뜹니다.'),
    (3, '오늘은 안 썼어요는 그 날짜 소비 기록이 0건일 때만 보입니다. 0원 기록을 만들지 않고 그 날짜에 표시만 남깁니다 — 달력 오늘 칸의 파란 +가 0이 되고, 표시를 풀면 다시 +입니다. '
        '표시한 뒤 소비를 저장하면 표시가 풀리고(상태 줄 9월 8일 표시가 풀렸어요 · 다시 표시), 마지막 소비를 지워 0건이 된 날은 자동으로 표시하지 않고 '
        '표시를 풀었어요 · 안 썼으면 「오늘은 안 썼어요」를 보여 줍니다.'),
]


MEMO_BLANK = '<span style="width: 17px; flex-shrink: 0;"></span>'          # 번호 표식(17px)과 같은 폭의 빈 칸


def memo_line(n, text, last=False):
    """구현 메모 한 줄. n 이 None 이면 앞 줄 번호의 이어지는 설명 — 표식 없이 같은 들여쓰기로."""
    if n is not None:
        return memo_row(n, text, last=last)
    row, badge = memo_row(0, text, last=last), mark(0, pos='margin-top: 1px; flex-shrink: 0;')
    assert row.count(badge) == 1
    return row.replace(badge, MEMO_BLANK)


def memo_card(rows):
    return (f'<div style="background: {C["SURF"]}; border: 1px solid {C["LINE"]}; border-radius: 18px; padding: 10px 18px 8px;">'
            f'<div style="font-size: 12px; font-weight: 700; color: {C["INK"]}; padding: 2px 0 4px;">구현 메모</div>'
            + ''.join(memo_line(n, t, last=(i == len(rows) - 1)) for i, (n, t) in enumerate(rows)) + '</div>')


def grid2(samples, cols=2):
    cells = ''.join(f'<div style="display: flex; flex-direction: column; gap: 8px; min-width: 0;">{cap}{pic}</div>' for cap, pic in samples)
    return f'<div style="flex: 1; min-width: 0; display: grid; grid-template-columns: repeat({cols}, 362px); gap: 24px 20px; align-items: start;">{cells}</div>'


w('DaySheetNoSpendStates', spec_frame(
    1200, 1252,      # 2026-09-27 fix-up 5 실제 웹폰트 자연 1228 + 24(예전 1234 는 여백 6) · fix-up 4 이체 줄 두 줄(메모 아래 소비율 제외)
    '안 쓴 날을 표시하는 경우',      # 2026-09-27 fix-up 시트 머리 ‹ › 28 칸 · 자연 1199 + 24      # 2026-09-26 1190 → 1221(효과 줄 · 칸 이름 위 · 자연 1197 + 24)      # 2026-09-24 후속 1160 → 1190(오늘 칸 + → 0 → + 견본 · 자연 높이 1164)
    '소비가 한 건도 없는 날에만 기록 창 맨 아래에 오늘은 안 썼어요가 보입니다. 누르면 달력의 오늘 칸이 파란 +에서 0으로 바뀝니다.',
    f'<div style="display: flex; gap: 32px; align-items: flex-start;">{ns_left}'
    f'{grid2([(case_cap(n, t, d), pic) for n, t, d, pic in NS_CASES])}</div>{memo_card(NS_MEMO)}', sub_w=760), keep_all=True)


# ══════════════ 3. ReviewListSheet — `확인할 내용 2개 ›` 목록 시트(앱 화면) ══════════════
# 캐논(9월 8일)의 확인할 내용은 `카테고리 없는 기록 7건` 하나라 홈 달력 행이 그 이름이고 이 시트는 안 뜬다(2026-09-27 fix-up · 앱 하네스).
# 이 그림은 마감 뒤 8월에 기록을 더한 날(8월 30일 식비 55,000원 — SpendingPastChanged · 확인 창 G 와 같은 장면)의 두 항목이다(앱 문구 · D9 · D4 · 하네스로 확인):
# `8월에 새 기록이 있어요 · 8월 합계 고치기 ›` · `카테고리 없는 기록 7건 · 카테고리 고르기 ›`(→ ClassifySheet).
# 셋째 항목 `통신 반복 기록이 두 번 들어갔을 수 있어요 ›`는 자동 기록일(25일) 뒤에만 생기므로 9월 8일 화면에는 없다 — 주석으로 남긴다.
def review_row(text, last=False):
    # 앱 v5-integration.css — 모든 줄(첫 줄 포함) 위에 border-top 1px(목록 좌우 18 안쪽) · 머리에는 선이 없다(2026-09-27 fix-up 3 · 예전 머리 아래 온 폭 선 + 줄 아래 선)
    bb = f'border-top: 1px solid {C["LINE_SOFT"]};'
    return (f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 10px; min-height: 53px; {bb}">'
            f'<span style="font-size: 14.5px; font-weight: 600; color: {C["INK"]};">{text}</span>{icon("right", 16, C["INK4"], 2)}</div>')


def review_sheet(rows, n):
    # 앱 .review-sheet(c6b7de3 하네스 390 × 844 · 시트 윗변 644 · 높이 200): 1px 테두리 · 손잡이는 흐름 밖(위 8) · 머리 20 18 12 위 정렬 ·
    # 제목 18 / 700 / 23.4 · 「닫기」 = 높이 28 · 안쪽 0 4 글자 버튼(2026-09-27 fix-up 5 · 예전 손잡이 9 + 4 가 흐름 안 · 가운데 정렬 · 닫기 안쪽 없음)
    return (f'<span style="position: absolute; top: 8px; left: 50%; margin-left: -19px; width: 38px; height: 4px; border-radius: 99px; background: {C["BORDER"]};"></span>'
            f'<div style="display: flex; align-items: flex-start; justify-content: space-between; gap: 8px; padding: 20px 18px 12px; flex-shrink: 0;">'
            f'<h2 style="margin: 0; font-size: 18px; font-weight: 700; line-height: 23.4px; letter-spacing: -0.025em; color: {C["INK"]};">확인할 내용 {n}개</h2>'
            f'<span style="display: inline-flex; align-items: center; height: 28px; padding: 0 4px; font-size: 13px; font-weight: 600; color: {C["INK2"]}; flex-shrink: 0; white-space: nowrap;">닫기</span></div>'
            f'<div style="padding: 4px 18px 28px; display: flex; flex-direction: column;">'
            + ''.join(review_row(t, last=(i == len(rows) - 1)) for i, t in enumerate(rows)) + '</div>')


def note_line(label, text):
    return (f'<div style="display: flex; gap: 8px; font-size: 11.5px; line-height: 1.5;"><span style="width: 96px; flex-shrink: 0; color: rgba(255,255,255,.55);">{label}</span>'
            f'<span style="flex: 1; min-width: 0; color: rgba(255,255,255,.86);">{text}</span></div>')


review_note = (
    f'<div style="margin: 0 18px; padding: 12px 14px; border: 1px dashed rgba(255,255,255,.32); border-radius: 12px; display: flex; flex-direction: column; gap: 7px;">'
    f'<span style="font-size: 11px; font-weight: 600; letter-spacing: 0.02em; color: rgba(255,255,255,.62);">시안 주석 · 앱에는 보이지 않아요</span>'
    + note_line('항목은 셋뿐', '8월에 새 기록이 있어요 · 8월 합계 고치기 › · 통신 반복 기록이 두 번 들어갔을 수 있어요 › · 카테고리 없는 기록 7건 · 카테고리 고르기 ›')
    + note_line('이 화면', '마감한 8월에 기록을 더한 날(8월 30일 식비 55,000원 · 지난 달 소비 「마감 뒤 바뀜」과 같은 장면)의 두 항목. 기본 장면 9월 8일은 확인할 내용이 카테고리 없는 기록 7건 하나뿐이라 홈 행이 그 이름이고 이 시트는 안 떠요. 통신 항목은 자동 기록일(25일) 뒤에만 생겨요')
    + note_line('28일~다음 달 3일', '카테고리 없는 기록 7건 · 월말 전에 정리 ›')
    + note_line('달이 바뀌면', '9월 카테고리 없는 기록 7건 · 마감 전에 정리 ›(10월 2일 홈)')
    + note_line('누르면', '합계 고치기 → 한 단계 확인 「8월 소비 합계만 새 금액으로 고칠게요」(취소 · 합계 고치기 · 마감 창이 아님) · 반복 중복 → 그날 하루 시트 · 카테고리 → 카테고리 고르기 시트')
    + note_line('항목이 하나면', '홈 달력의 행이 그 항목 이름(예: 카테고리 없는 기록 7건 · 카테고리 고르기 ›)이 되고 누르면 바로 열려요 · 샘플 모드에는 항목이 없어요')
    + '</div>')

w('ReviewListSheet', (
    f'<div style="width: 390px; height: 844px; background: #2A3245; color: {C["INK"]}; display: flex; flex-direction: column; overflow: hidden; position: relative; font-variant-numeric: tabular-nums;">'
    f'<div style="flex: 1; min-height: 0; display: flex; flex-direction: column; justify-content: center;">{review_note}</div>'
    f'{scrim_line("배경을 눌러 닫기")}'
    f'<div style="position: relative; background: {C["SURF"]}; border: 1px solid {C["LINE"]}; border-radius: 26px 26px 0 0; display: flex; flex-direction: column; overflow: hidden; flex-shrink: 0;">'
    + review_sheet(['8월에 새 기록이 있어요 · 8월 합계 고치기', '카테고리 없는 기록 7건 · 카테고리 고르기'], 2) + '</div></div>'), keep_all=True)


# ══════════════ 4. DoneCardStates — 완료 카드의 경우들(구현 참고 장) ══════════════
CHECK = ('<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#3DD489" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg>')
ACT = {'main': 'padding: 0 14px; border: 1px solid rgba(255,255,255,.55); color: #FFFFFF; font-weight: 700;',
       'cancel': 'padding: 0 14px; border: 1px solid rgba(255,255,255,.28); color: #FFFFFF; font-weight: 600;',
       'off': 'padding: 0 12px; border: 1px solid rgba(255,255,255,.14); color: rgba(255,255,255,.42); font-weight: 600;'}
CHIP_ROW = ('<div style="display: flex; align-items: center; gap: 6px; margin-top: 9px;">' + ''.join(done_chip(n) for n in DONE_CHIPS)
            + '<span style="font-size: 13px; font-weight: 600; color: #FFFFFF; white-space: nowrap; padding-left: 4px;">전체 &rsaquo;</span></div>')


def done_card(title, main=None, third=None, actions=(), chips=False):
    """DoneCard 의 완료 카드와 같은 모양 — 자리만 고정(absolute)이 아니다. 라이트/다크가 같아야 해서 dc-keep.
    chips = 셋째 줄 아래 카테고리 칩 줄(카테고리 없이 저장했을 때)."""
    body = ''
    if main:
        body += f'<div style="font-size: 13.5px; line-height: 1.45; font-weight: 500; margin-top: 7px; color: #FFFFFF;">{main}</div>'
    if third:
        body += f'<div style="font-size: 12.5px; line-height: 1.45; margin-top: 3px; color: rgba(255,255,255,.72);">{third}</div>'
    if chips:
        body += CHIP_ROW
    if actions:
        body += '<div style="display: flex; gap: 8px; margin-top: 11px;">' + ''.join(
            f'<span style="display: inline-flex; align-items: center; justify-content: center; height: 36px; border-radius: 10px; font-size: 13px; white-space: nowrap; flex-shrink: 0; {ACT[k]}">{t}</span>'
            for t, k in actions) + '</div>'
    return ('<!--dc-keep--><div style="background: #101828; border-radius: 16px; padding: 13px 14px 12px; color: #FFFFFF; box-shadow: 0 8px 24px rgba(0,0,0,.28);">'
            '<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px;">'
            f'<span style="display: inline-flex; align-items: center; gap: 7px; font-size: 14px; font-weight: 700;">{CHECK}{title}</span>'
            '<span style="font-size: 12px; font-weight: 600; color: rgba(255,255,255,.72);">닫기</span></div>'
            f'{body}</div><!--/dc-keep-->')


def done_strip(text, undo=True):
    """6초 뒤 40px 띠 — `✓ {요약} · 되돌리기 · 닫기`. 저장 60초 뒤 사라지고 되돌리기도 그때 끝난다."""
    u = ('<span style="color: rgba(255,255,255,.4);">·</span><span style="font-weight: 700;">되돌리기</span>' if undo else '')
    return ('<!--dc-keep--><div style="display: flex; align-items: center; gap: 9px; height: 40px; padding: 0 14px; background: #101828; border-radius: 12px; color: #FFFFFF; '
            'font-size: 13px; box-shadow: 0 8px 24px rgba(0,0,0,.28);">'
            f'{CHECK}<span style="flex: 1; min-width: 0; font-weight: 600; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">{text}</span>{u}'
            '<span style="color: rgba(255,255,255,.4);">·</span><span style="font-weight: 600; color: rgba(255,255,255,.72);">닫기</span></div><!--/dc-keep-->')


def b7(text):
    return f'<span style="font-weight: 700;">{text}</span>'


MAIN_BASE = DONE_MAIN
# 왼쪽 큰 카드 = DoneCard 장과 같은 저장(카테고리를 고르지 않은 편의점 12,000원) — 셋째 줄은 §4-4 의 4순위 문장 + 칩 줄
done_base = done_card('저장했어요', MAIN_BASE, v5.DONE_THIRD, [('한 건 더', 'main'), ('되돌리기', 'cancel')], chips=True)
assert v5.DONE_CARD.count(v5.DONE_THIRD) == 1 and v5.DONE_CARD.count('되돌리기') == 1      # DoneCard 장과 같은 문구
assert '월급의' not in v5.DONE_CARD      # 이 장의 저장은 4순위 문장이 먼저라 6순위 줄이 없다

THIRD = [('마감한 달에 저장', '8월 합계 고치기 ›'),
         ('지난달 날짜로 저장', '8월 합계와 최근 3개월 평균이 바뀌어 이번 달 예상도 달라질 수 있어요'),
         ('0~5시에 오늘로 저장', '어제로 옮기기 ›'),
         ('카테고리 없이 저장 · 칩 줄이 함께', '소비에는 이미 포함됐어요 · 지금 카테고리를 고를까요?'),
         ('반복 기록과 같은 돈을 「휴대폰 요금 맞아요」로 저장', '이번 달 휴대폰 요금 자동 기록은 건너뛰어요 · 되돌리면 다시 생겨요'),
         ('고정비 카테고리로 저장 · 맞는 반복 기록이 없을 때', '매달 반복으로 만들기 ›'),
         ('그 밖에 · 월급 있음 · 저장 전 기록 1건 이상', '월급의 31.1% → 31.4%')]      # 지금까지 쓴 돈 ÷ 월급, 저장 전 → 뒤(1,120,000 → 1,132,000 · 2026-09-24 — 예상 기준 조건 없음)
# 2026-09-24 최종 점검 후속: 마지막 줄은 저장 전 이번 달 기록이 0건이면(그달 첫 기록 — 0%를 보이지 않음) 없고, 전 · 후 글자가 같아도(31.1% → 31.1%) 없다(앱 navi-commit-policy)
PICTURED = 3      # 왼쪽 큰 카드(= DoneCard 장)가 걸린 순위 — 카테고리 없이 저장
assert THIRD[PICTURED][1] == v5.DONE_THIRD


def third_row(i, when, text, last=False, pictured=False):
    bb = '' if last else f'border-bottom: 1px solid {C["LINE_ROW"]};'
    if pictured:      # 제안 — 위 큰 카드가 이 순위의 경우임을 글로만 알린다(색 · 배지 없음)
        when += f'<span style="color: {C["INK3"]};"> · 위 그림</span>'
    strip = ('<!--dc-keep--><div style="background: #101828; border-radius: 8px; padding: 6px 10px; font-size: 12.5px; line-height: 1.45; color: rgba(255,255,255,.72);">'
             f'{text}</div><!--/dc-keep-->')
    return (f'<div style="display: flex; flex-direction: column; gap: 5px; padding: 9px 0; {bb}">'
            f'<div style="font-size: 12px; line-height: 1.4; color: {C["INK2"]};"><b style="font-weight: 600; color: {C["INK"]};">{i}순위</b>&nbsp;&nbsp;{when}</div>{strip}</div>')


third_table = card(
    f'<div style="display: flex; align-items: center; gap: 7px; padding-bottom: 2px;">{mark(2, pos="flex-shrink: 0;")}'
    f'<span style="font-size: 13.5px; font-weight: 700; color: {C["INK"]};">셋째 줄 · 한 줄만, 위에 있는 것이 먼저</span></div>'
    + ''.join(third_row(i + 1, a, b, last=(i == len(THIRD) - 1), pictured=(i == PICTURED)) for i, (a, b) in enumerate(THIRD)), pad='12px 16px 4px')

# 같은 반복 제안의 다른 입구 — 소비 › 내역 목록 맨 위 한 줄(spending-13 #4 · 앱 lib/navi-recurring-suggest.ts · 하네스 W/tools/fix1/cap_suggest.cjs).
# 캐논 9월 8일에는 조건에 맞는 기록이 없어 LedgerV5 에 없다(8월 보험료 메모가 「실손 보험료」) — 여기에만 그린다. 예: 8월 5일과 9월 1일의 「보험료」 120,000원.
SUGGEST_TEXT = '보험료 120,000원이 지난달에도 있었어요 · 매달 나가는 돈으로 등록할까요?'      # 앱 문구(recurringCandidates.text)
suggest_strip = (
    f'<div style="background: {C["BRAND_SOFT"]}; border-radius: 12px; padding: 11px 12px 10px; display: flex; flex-direction: column; gap: 8px;">'
    f'<span style="font-size: 12.5px; line-height: 1.5; color: #3B4E8F;">{SUGGEST_TEXT}</span>'
    f'<div style="display: flex; align-items: center; gap: 16px;"><span style="font-size: 12.5px; font-weight: 700; color: {C["BRAND"]}; white-space: nowrap;">등록하기 &rsaquo;</span>'
    f'<span style="display: inline-flex; align-items: center; gap: 4px; font-size: 12.5px; font-weight: 500; color: {C["INK2"]}; white-space: nowrap;">{icon("x", 13, C["INK2"], 2)}닫기</span></div></div>')
suggest_block = card(
    f'<div style="display: flex; align-items: center; gap: 7px; padding-bottom: 8px;">{mark(4, pos="flex-shrink: 0;")}'
    f'<span style="font-size: 13.5px; font-weight: 700; color: {C["INK"]};">같은 제안의 다른 입구 · 소비 › 내역 맨 위</span></div>'
    + suggest_strip
    + f'<p style="margin: 8px 2px 4px; font-size: 12px; line-height: 1.55; color: {C["INK3"]};">이번 달 기록 중 메모가 있고, 지난달에 같은 메모 · 같은 금액이 한 번씩 있고, 같은 반복 기록이 없을 때 목록 위에 한 줄(날짜가 이른 것 하나). '
      f'카테고리 없는 기록 · 반복이 만든 기록 · 한 달에 두 번 넘는 것은 빼요. 「등록하기 ›」 = 반복 기록 창을 이 기록으로 채워 엶(결제일 = 이 날 · 시작 = 다음 달 · 위 6순위와 같은 창 RecurringPrefill), '
      f'「닫기」 = 이번 실행 동안만 숨김(저장 안 함). 예: 8월 5일 · 9월 1일 보험료 120,000원 — 시안 사용자 9월 8일 내역(LedgerV5)에는 없어요.</p>', pad='12px 16px 10px')

done_left = (
    f'<div style="width: 362px; flex-shrink: 0; display: flex; flex-direction: column; gap: 12px;">'
    f'<div style="position: relative;">{done_base}'
    + mark(1, pos='position: absolute; left: -8px; top: 14px;') + mark(2, pos='position: absolute; left: -8px; top: 84px;')
    + mark(3, pos='position: absolute; left: -8px; top: 166px;') + '</div>'
    f'<p style="margin: 0 2px; font-size: 12px; line-height: 1.6; color: {C["INK3"]};">'
    f'<b style="font-weight: 600; color: {C["INK2"]};">1</b> 제목 · <b style="font-weight: 600; color: {C["INK2"]};">2</b> 셋째 줄(+ 칩 줄) · '
    f'<b style="font-weight: 600; color: {C["INK2"]};">3</b> 행동 두 칸(주 행동 + 되돌리기). 둘째 줄은 언제나 날짜 · 무엇을(메모 · 카테고리 · 없으면 카테고리 없음) 정확한 금액 · 그날 합계입니다. '
    f'그림은 홈 · 저장 뒤 완료 카드 장과 같습니다 — 카테고리를 고르지 않고 저장해서 셋째 줄이 아래 표의 4순위 문장이고 자주 쓴 카테고리 칩 줄이 붙습니다.</p>'
    f'{third_table}{suggest_block}</div>')

DONE_CASES = [
    (1, '기록을 고쳐서 저장했을 때', '제목이 바뀌고 행동은 되돌리기 하나뿐입니다. 셋째 줄도 같은 순위를 따릅니다.',
     done_card('고쳤어요', f'9월 3일 · 택시 · 교통 {b7("42,000원")}으로 고침 · 3건 55,500원', '월급의 31.1% → 31.0%', [('되돌리기', 'cancel')])),
    (1, '날짜를 옮겨 저장했을 때', '제목이 옮겼어요로 바뀝니다.',
     done_card('옮겼어요', f'9월 3일 → 2일로 옮겼어요 · {b7("45,000원")}', None, [('되돌리기', 'cancel')])),
    (1, '카테고리 고르기에서 저장했을 때', '제목에 건수가 붙고 행동은 되돌리기 하나뿐입니다.',
     # 둘째 줄은 계획 §10 「9판 (b) 시안에서 정해 승인된 것」 표 원문 그대로 — ClassifySheet(gen_v5.CLS_*)의 7건을 다 정했을 때와 맞는다: 커피 3 + 메모 없는 3,000원 = 카페/간식 4건 · 간식 + 편의점 = 식비 2건 · 버스 = 교통 1건
     done_card('카테고리를 골랐어요 · 7건', '카페/간식 4건 · 식비 2건 · 교통 1건', None, [('되돌리기', 'cancel')])),
    (1, '저축·투자로 저장했을 때', '소비가 아니라 셋째 줄이 없고 그날 소비 합계도 말하지 않습니다.',
     done_card('저장했어요', f'9월 8일 · 적금 · 저축·투자 {b7("300,000원")} 저장 · 저축·투자라 소비율에는 안 들어가요', None, [('한 건 더', 'main'), ('되돌리기', 'cancel')])),
    # 9월 5일에 처음 연 사람(HeroInsufficient)이 커피 5,000원 뒤에 12,000원을 식비로 저장 — 이번 달 쓴 돈 5,000 → 17,000원 = 월급의 0.1% → 0.5%
    (2, '월말 예상 기준이 서기 전인 달', '월급의 몇 %인지는 지금까지 쓴 돈이라 이때도 나옵니다. 월말 예상은 말하지 않습니다.',
     done_card('저장했어요', f'9월 8일 · 식비 {b7("12,000원")} 저장 · 오늘 2건 17,000원', '월급의 0.1% → 0.5%', [('한 건 더', 'main'), ('되돌리기', 'cancel')])),
    (3, '월급을 아직 안 넣었을 때', '한 건 더 자리에 월급 입력하기가 옵니다(월급 입력 시트). 월급의 몇 % 줄은 없습니다.',
     done_card('저장했어요', f'9월 8일 · 식비 {b7("5,000원")} 저장 · 오늘 1건 5,000원', None, [('월급 입력하기 &rsaquo;', 'main'), ('되돌리기', 'cancel')])),
    (3, '6초가 지나면', '카드가 40px 띠로 줄어듭니다. 저장 60초 뒤 사라지고 되돌리기도 그때 끝납니다.', done_strip('12,000원 저장')),
    (3, '되돌리기를 눌렀을 때', '같은 자리 띠가 결과를 알립니다. 그 날짜의 확인 표시는 풀립니다.', done_strip('12,000원 기록을 되돌렸어요', undo=False)),
    (3, '그 기록이 이미 바뀌어 되돌릴 수 없을 때', '되돌리기 자리가 눌리지 않는 글로 바뀝니다. 연결된 기록이면 「연결된 기록은 되돌릴 수 없어요」.',
     done_card('저장했어요', MAIN_BASE, v5.DONE_THIRD, [('한 건 더', 'main'), ('이미 바뀌어 되돌릴 수 없어요', 'off')])),      # 왼쪽 큰 카드와 같은 저장
]
DONE_MEMO = [
    (1, '제목은 네 가지입니다 — 기록 창 저장은 저장했어요, 수정 저장은 고쳤어요(날짜를 옮기면 옮겼어요), 카테고리 고르기 저장은 카테고리를 골랐어요 · 7건. 뒤의 것들은 행동이 되돌리기 하나뿐입니다. 카드는 하나이고 새 저장이 생기면 자리를 바꿉니다.'),
    (2, '셋째 줄은 한 줄만 씁니다. 왼쪽 표에서 위에 있는 조건이 먼저입니다. 마지막 줄 월급의 N% → M%는 지금까지 쓴 돈 ÷ 월급(홈 큰 숫자와 같은 <span style="white-space: nowrap;">값)의</span> 저장 전 → 뒤이고, 앞선 조건이 하나도 없고 월급을 넣었을 때 나옵니다 — 월말 예상 기준이 서기 전인 달에도 나오고 월급 미입력에는 없습니다. '
        '저장 전 이번 달 기록이 0건이면(그달 첫 기록) 이 줄은 없습니다 — 0%를 보이지 않습니다. 전 · 후 글자가 같아도(31.1% → 31.1% · 0.1% 미만 → 0.1% 미만) 없습니다. 카테고리 없이 저장하면 4순위 문장과 칩 줄(자주 쓴 카테고리 셋 + 전체 ›)이 먼저입니다.'),
    (3, '되돌리기는 누르는 순간 방금 그 기록만 검사합니다. 금액 · 날짜 · 카테고리 · 계좌 연결이 저장 직후와 하나라도 다르면 되돌리지 않습니다. '
        '카드는 6초 동안 온전히 보이고 40px 띠 「✓ 12,000원 저장 · 되돌리기 · 닫기」로 줄었다가 저장 60초 뒤 사라집니다(되돌리기도 그때 끝남). 탭을 옮겨도 남고, 누르거나 마우스를 올리면 멈추고, 새 저장이 오면 자리를 바꿉니다. '
        '색으로 평가하지 않고 사실만 씁니다. 다 적었어요 · 안 썼어요는 카드 없이 달력 칸의 표시가 확인입니다.'),
]

DCS_H = 1534      # 2026-09-27 fix-up 3 자연 1510 + 24(점검 번호를 뗀 두 줄) · 예전 자연 1528 + 24
w('DoneCardStates', spec_frame(
    1200, DCS_H, '저장 완료 카드의 경우들',      # 2026-09-26 칩 줄 · 띠 · 옮겼어요 · 저축·투자 견본 · 7순위 표(자연 높이 + 24)
    '저장이 끝나면 홈 아래쪽에 뜨는 카드 하나가 제목 · 셋째 줄 · 행동만 바꿔 가며 모든 경우를 맡습니다. 6초 뒤에는 40px 띠로 줄어듭니다.',
    f'<div style="display: flex; gap: 32px; align-items: flex-start;">{done_left}'
    f'<div style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 22px;">'
    f'{grid2([(case_cap(n, t, d), pic) for n, t, d, pic in DONE_CASES])}{memo_card(DONE_MEMO)}</div></div>', sub_w=760), keep_all=True)


# ══════════════ 5. DaySheetStates — 하루 시트의 조건부 문구와 입력 한계(구현 참고 장) ══════════════
def rel(inner, n):
    return f'<div style="position: relative;">{inner}{mark(n, pos="position: absolute; top: -6px; right: -6px;")}</div>'


INLINE = 'margin-left: 6px; vertical-align: -3px;'
# 배지 5 는 `전체 ›`를 가리킨다. 묶음 모서리에 얹으면 첫 줄 오른쪽 끝의 `나중에 고르기`를 가리므로 `전체 ›` 바로 뒤 같은 줄에 놓는다
# (칩 줄이 align-items: center · gap 6px 라 세로 가운데 · 줄 높이는 그대로). category_row 는 다른 장도 쓰므로 여기서만 끼운다.
ALL_TAIL = '전체 &rsaquo;</span></div></div>'
_cat_row = category_row(None)
assert _cat_row.count(ALL_TAIL) == 1 and _cat_row.endswith(ALL_TAIL)
CAT_ROW_5 = _cat_row[:-len(ALL_TAIL)] + '전체 &rsaquo;</span>' + mark(5, pos='flex-shrink: 0;') + '</div></div>'
states_sheet = sheet_box(
    sheet_header('9월 8일 소비 기록' + mark(1, pos='margin-left: 6px; vertical-align: 3px;'), '오늘 4건 37,000원' + mark(2, pos=INLINE))
    + f'<div style="padding: 12px 18px 18px; display: flex; flex-direction: column; gap: 10px;">'
    + amount_field('12,000', focused=True)
    + rel(unsaved_line('1.2만원'), 3)
    + f'<div style="position: relative;">{memo_field("편의점")}{mark(4, pos="position: absolute; top: 18px; right: -6px;")}</div>'
    + CAT_ROW_5
    + recent_row([recent_chip(*r) for r in RECENT], 18)
    + f'<div style="margin-top: 2px;">{save_btn()}</div>'
    + links_block()
    + v5.today_list()      # 앱 — 키보드 아래로 오늘 기록 3행 + 1건 더 보기 · 다 적었어요 + 효과 줄(record-11 #1)
    + day_done('9월 8일 다 적었어요', EFFECT_DONE_TODAY) + '</div>')


def header_frag(title, sub, today=True, next_on=False):
    return sheet_box(sheet_header(title, sub, today=today, next_on=next_on), cropped=True)


def block(inner):
    return f'<div style="background: {C["SURF"]}; border: 1px solid {C["LINE"]}; border-radius: 18px; padding: 14px; display: flex; flex-direction: column; gap: 10px;">{inner}</div>'


def memo_long(value, counter, over=False):
    """긴 메모 — 이름은 칸 위 · 한 줄 · 끝 말줄임 · 칸 오른쪽 글자 수."""
    return memo_field(value, counter, over)


# 전체 › 펼침 — CATEGORIES 고정 순서 13개(저축/투자 · 대출상환 제외) 가운데 위에 이미 보이는 세 칸을 뺀 나머지(record-17 #2). 고정비 4개는 구분선 뒤.
FIXED4 = ['주거/관리', '통신', '보험', '구독']
ALL13 = [n for n in CAT if n not in ('저축/투자', '대출상환')]
assert len(ALL13) == 13 and all(n in ALL13 for n in FIXED4)
SHOWN3 = CANON_SLOTS      # 자주 쓴 세 칸 = 캐논(식비 · 카페/간식 · 쇼핑 — 같은 장의 기본 시트 · DoneCardStates 와 같게 · 2026-09-27 fix-up)
VAR9 = [n for n in ALL13 if n not in FIXED4 and n not in SHOWN3]
cat_open = (
    category_row('주거/관리', frequent=SHOWN3, later=False, all_open=True)
    + f'<div style="display: flex; flex-wrap: wrap; gap: 6px;">{"".join(cat_chip(n) for n in VAR9)}</div>'
    + f'<div style="height: 1px; background: {C["LINE"]};"></div>'
    + f'<div style="display: flex; flex-wrap: wrap; gap: 6px;">{"".join(cat_chip(n, n == "주거/관리") for n in FIXED4)}</div>'
    + hint_line('매달 나가는 돈이에요 · 실제 청구액으로 저장돼요'))
assert cat_open.count('1.5px solid') == 1          # 선택은 하나(주거/관리) — 위 자주 쓴 3칸에는 없는 이름이라 아래에서만 켜진다


def _week_picker_retired():      # 2026-09-26 record-15 — 주 단위 선택기는 앱에 없다(제목은 글자 · 새 기록은 ‹ › · 고칠 때는 날짜 칸). 옛 그림 기록용
    """헤더 날짜를 누르면 열리는 주 단위 선택기 — 이번 달 + 지난달. 합계 없이 날짜만, 아직 오지 않은 날은 옅게(누를 수 없음)."""
    def day(d, kind, month):
        if kind != 'in':
            return '<span></span>'
        future = month == 'sep' and d > TODAY
        today = month == 'sep' and d == TODAY
        col = C["DIS"] if future else C["INK"]
        bg = f'background: {C["BRAND_SOFT"]}; font-weight: 700;' if today else 'font-weight: 500;'
        return (f'<span style="height: 32px; border-radius: 9px; display: flex; align-items: center; justify-content: center; font-size: 13px; color: {col}; {bg}">{d}</span>')

    def month_rows(month, label, n=None):
        rows = ''.join(f'<div style="display: grid; grid-template-columns: repeat(7, minmax(0, 1fr)); border-top: 1px solid {C["LINE_SOFT"]};">'
                       + ''.join(day(d, k, month) for k, d, m in wk) + '</div>' for wk in WEEKS[month][:n])
        return f'<div style="font-size: 12px; font-weight: 600; color: {C["INK2"]}; padding: 10px 2px 6px;">{label}</div>{rows}'

    wd = ''.join(f'<span style="text-align: center; font-size: 11px; font-weight: 500; color: {C["INK3"]};">{d}</span>' for d in WD)
    return (f'<div style="padding: 10px 18px 0; min-height: 300px;">'
            f'<div style="display: grid; grid-template-columns: repeat(7, minmax(0, 1fr));">{wd}</div>'
            + month_rows('sep', '9월') + month_rows('aug', '8월', 3) + '</div>')


# 날짜를 바꾸는 두 길(record-15): 새 기록은 제목 옆 ‹ › 로 하루씩(지난달 1일 ~ 오늘 · ›는 오늘에서 멈춤), 기록을 고칠 때는 제목에 ‹ › 가 없고 첫 칸 `날짜 9월 3일 ▾`(기기 날짜 고르기).
picker = block(labeled('날짜', date_box('9월 5일'))
               + f'<div style="font-size: 11.5px; font-weight: 500; line-height: 16.675px; color: {C["INK2"]}; margin-top: -4px; padding: 0;">저장하면 9월 3일 → 9월 5일로 옮겨요</div>'
               + f'<div style="font-size: 11.5px; line-height: 1.45; color: {C["INK3"]}; padding: 0 2px;">옮기는 동안 다 적었어요 · 안 썼어요 버튼은 숨어요</div>')

sample_mode = sheet_box(
    sheet_header('9월 8일 소비 기록', f'오늘 4건 37,000원<span style="display: block; margin-top: 2px;">샘플 데이터에 저장돼요 · 내 데이터로 시작하면 사라져요 · {blink("내 데이터로 시작 &rsaquo;")}</span>')
    + f'<div style="padding: 12px 18px 18px; display: flex; flex-direction: column; gap: 10px;">'
    + amount_field('12,000', focused=True) + unsaved_line('1.2만원') + memo_field('편의점')
    + category_row('식비', frequent=DEMO_SLOTS, later=None)      # 샘플 모드 = 앱 데모 자료의 세 칸
    + recent_row([recent_chip(*r) for r in RECENT], 18)      # 샘플에서도 최근 기록 칩은 있다(앱)
    + f'<div style="margin-top: 2px;">{save_btn()}</div>'
    + links_block()      # 그 아래 오늘 기록 목록은 평소와 같고 다 적었어요 버튼만 없다(샘플) — 그림은 여기까지
    + '</div>')

conflict = neutral_notice(
    f'<span style="font-size: 13px; line-height: 1.45; color: {C["INK"]};">다른 변경이 먼저 저장됐어요 · {blink("다시 저장")}</span>')


def col(items, width=362):
    return f'<div style="width: {width}px; flex-shrink: 0; display: flex; flex-direction: column; gap: 22px;">{"".join(items)}</div>'


def case(n, title, desc, pic):
    return f'<div style="display: flex; flex-direction: column; gap: 8px;">{case_cap(n, title, desc)}{pic}</div>'


states_col1 = col([
    f'<div style="display: flex; flex-direction: column; gap: 8px;">{states_sheet}'
    f'<p style="margin: 2px 2px 0; font-size: 12px; line-height: 1.5; color: {C["INK3"]};">번호는 글이 바뀌는 자리입니다. 그림은 '
    f'<b style="font-weight: 600; color: {C["INK2"]};">오늘 · 평소</b>의 기록 창입니다.</p></div>',
    case(1, '기록을 고칠 때 날짜를 옮기려면', '제목은 글자일 뿐 누르지 않습니다. 새 기록은 ‹ ›로 하루씩 옮기고, 고칠 때는 날짜 칸이 기기의 날짜 고르기를 엽니다.', picker),
])
states_col2 = col([
    case(2, '새벽 0~5시에 열었을 때', '날짜를 앱이 바꾸지 않고 안내만 합니다.',
         header_frag('9월 8일 소비 기록', '어젯밤 소비면 ‹ 로 어제로 바꿔요')),
    case(2, '지난달 날짜를 열었을 때', '그 기록이 어느 달 소비에 들어가는지 말합니다.',
         header_frag('8월 30일 소비 기록', '8월 기록이에요 · 8월 소비에 들어가요', today=False, next_on=True)),
    case(2, '이미 마감한 달의 날짜를 열었을 때', '저장을 막지 않고, 저장하면 그 달 합계만 한 번 더 확인한다고 알립니다(합계 고치기).',
         header_frag('8월 20일 소비 기록', f'마감한 달이에요 · 저장하면 8월 합계만 한 번 더 확인해요<span style="display: block; margin-top: 2px;">✓ 다 적었다고 표시했어요 · {blink("표시 풀기")}</span>', today=False, next_on=True)),
    case(2, '월급을 아직 안 넣었을 때', '기록은 막지 않습니다.',
         header_frag('9월 8일 소비 기록', '월급을 아직 안 넣었어요 · 기록만 쌓여요')),
    case(3, '금액이 비었을 때', '저장은 회색이고 까닭을 한 줄로 말합니다. 0원 기록은 만들지 않습니다.',
         block(amount_field(EMPTY_AMOUNT, focused=True) + hint_line(HINT_RECORD_DAY) + SAVE_OFF
               + f'<div style="font-size: 11.5px; line-height: 1.5; color: {C["INK3"]}; border-top: 1px solid {C["LINE_ROW"]}; padding-top: 8px;">그날 기록이 0건이면 「{NO_SPEND_HINT}」 · 지난 날은 「8월 30일은 안 썼어요」</div>')),
    case(3, '원 단위가 아닌 숫자를 넣었을 때', '소수점은 받지 않습니다 — 빨간 글 한 줄 · 저장은 회색.',
         block(amount_field('12.5', focused=True) + f'<div style="font-size: 11.5px; line-height: 1.45; color: {C["NEG"]}; padding: 0 2px;">원 단위 숫자로 넣어 주세요</div>' + SAVE_OFF)),
    case(3, '저장하는 사이 다른 기록이 먼저 저장됐을 때', '적은 내용은 그대로 두고 다시 저장하게 합니다.',
         block(amount_field('12,000', focused=False) + conflict)),
])
# 메모 본보기 — 카운터(52/60 · 64/60)와 실제 글자 수가 같아야 한다(*.dc.html 이 값의 기준 · 그림에서는 말줄임에 가려도).
MEMO_52 = '회사 앞 편의점에서 야근하면서 먹을 도시락이랑 음료수 두 개, 내일 아침에 먹을 샌드위치 하나'
MEMO_64 = '예전에 길게 적어 둔 메모는 그대로 열리고 저장도 되지만 여기서 글자를 더 넣을 수는 없어요, 지난겨울에 적은 메모'
assert len(MEMO_52) == 52 and len(MEMO_64) == 64
states_col3 = col([
    case(4, '메모가 50자를 넘겼을 때', '50자부터 글자 수가 보이고 60자에서 더 들어가지 않습니다.',
         block(memo_long(MEMO_52, '52/60') + memo_long(MEMO_64, '64/60 · 더 못 넣어요', over=True))),
    case(5, '전체 ›를 눌렀을 때', '위에 보이는 세 칸을 뺀 나머지가 늘 같은 순서로 펼쳐집니다. 매달 나가는 돈 네 가지는 선 아래에 모여 있습니다.', block(cat_open)),
    case(3, '카테고리 고르기에서 아무것도 정하지 않았을 때', '회색 「0건 저장」과 까닭 한 줄 — 추천 칩도 눌러야 정해집니다.',
         block(btn('0건 저장', 'disabled', h=52, radius=14, size=16)
               + f'<p style="margin: 0; text-align: center; font-size: 11.5px; line-height: 1.5; color: {C["INK3"]};">카테고리를 골라 주세요 · 추천도 눌러야 정해져요</p>')),
    f'<div style="display: flex; flex-direction: column; gap: 8px;">'
    f'<div><div style="font-size: 14px; font-weight: 700; letter-spacing: -0.01em; color: {C["INK"]};">샘플 데이터로 둘러보는 중일 때</div>'
    f'<div style="font-size: 12px; line-height: 1.5; color: {C["INK3"]}; margin-top: 3px;">둘째 줄 아래 샘플 안내가 한 줄 더 붙고, 나중에 고르기와 다 적었어요 · 안 썼어요가 없습니다. 카테고리는 식비가 미리 골라져 있습니다.</div></div>{sample_mode}</div>',
])
STATES_MEMO = [
    (1, '새 기록의 ‹ ›는 하루씩 움직이고 지난달 1일부터 오늘까지입니다(›는 오늘에서 멈춤). 그보다 앞선 달은 소비 탭의 기록 추가에서 남깁니다. 고칠 때는 ‹ › 대신 날짜 칸으로 옮겨요.'),
    (2, '둘째 줄은 평소에 그날 합계(오늘 4건 37,000원)입니다. 위 네 경우에는 그 자리에 안내 문장이 옵니다. 마감한 달 안내는 8월 기록 안내보다 먼저이고, 저장 뒤 완료 카드의 셋째 줄이 「8월 합계 고치기 ›」입니다.'),
    (3, '금액 아래 한 줄은 저장을 한 번 더 물어보는 경우 장의 네 안내와 같은 자리입니다. 기록이 있는 날은 금액을 넣고 저장을 눌러요 · 지난 빈 날은 「9월 21일은 안 썼어요」처럼 날짜를 넣은 버튼입니다.'),
    (4, '예전에 60자를 넘겨 적은 메모는 그대로 열리고 저장도 됩니다. 글자를 더 넣는 것만 막습니다.'),
    (5, '위에 보이는 세 가지를 뺀 나머지가 늘 같은 순서로 펼쳐집니다 — 식비 · 카페/간식 · 교통 · 쇼핑 · 문화/여가 · 의료/건강 · 교육 · 경조사 · 기타, 선 아래 주거/관리 · 통신 · 보험 · 구독. 저축·투자와 대출상환은 여기에 없습니다. 창이 열려 있는 동안 칩 순서는 바뀌지 않습니다.'),
]

DSS_H = 1919      # 2026-09-27 fix-up 시트 머리 ‹ › 28 칸 · 자연 1895 + 24 · 자연 1891 + 24(2026-09-26 · 날짜 칸 · 소수점 · 0건 저장 견본 · DZ4 검토: 기본 시트 오늘 기록 · 다 적었어요 · 샘플 시트 최근 기록 · 링크)
w('DaySheetStates', spec_frame(
    1210, DSS_H, '기록 창의 글이 바뀌는 경우', '기록 창은 하나이고, 날짜 · 시간 · 입력한 값에 따라 아래 다섯 자리의 글과 모양만 바뀝니다.',
    f'<div style="display: flex; gap: 32px; align-items: flex-start;">{states_col1}{states_col2}{states_col3}</div>{memo_card(STATES_MEMO)}', sub_w=760), keep_all=True)


# ══════════════ 6. CalendarStatusLines — 달력 상태 줄의 경우들(구현 참고 장) ══════════════
def st(text, link=None):
    return text + (f' · {blink(link)}' if link else '')


_base = calendar_card(False)
STATUS_OPEN = f'<span style="flex: 1; min-width: 0; font-size: {STATUS_FS}px; line-height: 1.5; color: {C["INK2"]};">{TODAY_TEXT}</span>'
assert _base.count(STATUS_OPEN) == 1
status_left_card = _base.replace(STATUS_OPEN, STATUS_OPEN.replace(f'{TODAY_TEXT}</span>', f'{TODAY_TEXT}{mark(1, pos="margin-left: 6px; vertical-align: -3px;")}</span>'))

# 펼친 달력에서 아직 오지 않은 날을 눌렀을 때 — 그 달 합계 줄은 그대로, 오늘 합계 자리에 3초 안내(알약은 그대로) · 확인할 내용 행(캐논 = 항목 하나의 이름)도 그대로
# (2026-09-24 최종 점검 후속 — 안내가 떠 있는 동안 행이 사라지는 것처럼 보이지 않게. 행이 없는 견본은 샘플 · 처음 쓰는 날뿐)
future_card = card(month_bar('2026년 9월', prev_on=True, next_on=False) + hint(mt=6) + month_grid('sep', weeks=slice(1, 3)) + legend()      # 범례 줄은 어느 견본에나(record-11 #3)
                   + status_line(f'9월 기록한 소비 {SEP_TOTAL:,}원') + today_tail(day_state('sep', TODAY), '아직 오지 않은 날은 적을 수 없어요', mt=8)
                   + cal_review_row(REVIEW_UNCAT),
                   pad='13px 14px 13px')
assert REVIEW_UNCAT in future_card

# 샘플 문장은 늘 위 줄(버튼일 때도 알약일 때도) — 샘플에서 그날 첫 기록을 저장해 버튼이 알약으로 바뀌어도 카드 높이가 같다
# (2026-09-24 통합 점검 — 알약 옆에 두면 첫 저장에 카드가 한 줄 줄어든다). 알약 옆은 오늘 합계. 샘플에는 ✓ · 안 썼어요 표시가 없다.
SAMPLE_TEXT = '샘플에서는 「다 적었어요」 표시를 쓰지 않아요 · 카테고리는 저장할 때 골라요'      # 앱 문구(record-11 · D4)
_sample_base = calendar_card(False, review=0, states={3: ('5.9만', False, False, False), 4: ('4,500', False, False, False),
                                                       5: ('1.2만', False, False, False), 6: ('—', False, True, False)})
_pill = pill_row(TODAY_TEXT, mt=10)
assert _sample_base.count(_pill) == 1
sample_card = _sample_base.replace(_pill, status_line(SAMPLE_TEXT, mt=8) + pill_row(TODAY_TEXT, mt=6))

# 1 ~ 6일 — 스트립에 지난달 날이 들어가 제목이 `최근 7일 소비 기록`(home-17 #2). 9월 3일에 본 모습(8/28 ~ 9/3).
MONTH_START_STRIP = [('8/28', '금', (fmt_sum(96_000), True, False, False), False), ('8/29', '토', (fmt_sum(35_000), True, False, False), False),
                     ('8/30', '일', NO_RECORD, False), ('8/31', '월', (fmt_sum(55_000), False, False, False), False),
                     ('1', '화', (fmt_sum(1_008_000), True, False, False), False), ('2', '수', NO_RECORD, False),
                     ('3', '목', (fmt_sum(58_500), False, False, False), True)]
# 9월 3일의 확인할 내용 = 9월 카테고리 없는 기록 2건(1일 커피 · 3일 간식) 하나 — 8월은 9월 2일에 마감했고 그 달 카테고리 없는 3건은 마감 뒤 골랐다(캐논).
# 28일 ~ 다음 달 3일에는 행 끝이 「월말 전에 정리」(앱 navi-quick-entry reviewItems monthEndFrom 28 · monthEndTo 3 · D4 · 2026-09-27 fix-up 2 하네스 9월 3일).
month_start_card = calendar_card(False, title=RECENT_TITLE, strip=MONTH_START_STRIP, status='오늘 3건 58,500원',
                                 review='카테고리 없는 기록 2건 · 월말 전에 정리')
assert '최근 7일 소비 기록' in month_start_card and '8/28' in month_start_card

# 막힌 ‹ — 8월을 보는 중 ‹ 를 누르면 3초 동안 그 달 합계 자리에 `더 이전 달은 소비 › 내역에서 볼 수 있어요 · 내역 보기 ›`(home-18 #1).
_aug = calendar_card(True, month='aug')      # 확인할 내용 행(캐논 7건)은 8월을 보는 동안에도 그대로(앱 · 막힌 ‹ 앞뒤 모두 · 2026-09-27 fix-up 2)
_aug_total = status_line(month_total_text(8, 1_715_200), False, mt=8)
assert _aug.count(_aug_total) == 1
blocked_card = _aug.replace(_aug_total, status_line(st('더 이전 달은 소비 › 내역에서 볼 수 있어요', '내역 보기 &rsaquo;'), mt=8))

# 그 달 기록 0건 · 안 썼어요 표시만(D7) — 펼친 9월: 칸은 모두 —, 6일만 0, 오늘 +. 합계 줄 `9월 기록이 아직 없어요 · 안 썼어요 표시만 있어요` + 버튼.
ZERO_MONTH = {d: NO_RECORD for d in range(1, 9)}
ZERO_MONTH[6] = ('0', False, False, True)
zero_month_card = calendar_card(True, states=ZERO_MONTH, review=0)      # 캐논 8월 마감값 = 기록 합이라 합계 고치기 항목이 없다 · 9월이 비면 카테고리 없는 기록도 없다(앱 · 2026-09-27 fix-up 2)
assert '9월 기록이 아직 없어요 · 안 썼어요 표시만 있어요' in zero_month_card

# 오늘(9월 8일) 기록 4건이 없는 견본 — 그 가운데 편의점 6,500원이 카테고리 없는 7건 중 하나라 행은 6건(앱 하네스 · 9월 8일 기록을 지운 캐논 · 2026-09-27 fix-up 2)
REVIEW_TODAY_GONE = '카테고리 없는 기록 6건 · 카테고리 고르기'
STATUS_CASES = [
    ('오늘 소비 기록이 아직 없을 때', '오늘 칸에 파란 +가 생기고, 문장 대신 「+ 오늘 쓴 돈 적기」 버튼이 옵니다.',
     calendar_card(False, today_empty=True, review=REVIEW_TODAY_GONE)),
    ('오늘을 안 쓴 날로 표시했을 때', '오늘 칸은 0이고 알약은 「+ 적기」입니다.',
     calendar_card(False, states={TODAY: ('0', False, False, True)}, status='오늘은 안 썼다고 표시했어요', review=REVIEW_TODAY_GONE)),
    ('저녁 6시가 지났고 오늘 기록이 있을 때', '합계 뒤에 링크 「오늘 다 적었어요 ›」가 붙습니다. 누르면 바로 표시됩니다.',
     calendar_card(False, status=st('오늘 4건 37,000원', '오늘 다 적었어요 &rsaquo;'))),
    ('저녁 링크를 누른 뒤', '오늘 칸에 ✓가 남고 줄은 「· 다 적었어요 ✓」가 됩니다.',
     calendar_card(False, states={TODAY: ('3.7만', True, False, False)}, status='오늘 4건 37,000원 · 다 적었어요 ✓')),
    ('표시한 날의 기록이 바뀌었을 때', '안 쓴 날로 표시한 뒤 4,500원을 적은 경우입니다.',
     calendar_card(False, states={TODAY: ('4,500', False, False, False)}, status=st('9월 8일 표시가 풀렸어요', '다시 표시'))),
    # 적금 300,000원(저축/투자)은 ETF 자동이체 반복 기록(매월 6일 · 300,000원 · 9월 6일 자동 기록)과 같은 달 · 카테고리 · 금액이라 앱이 반복 중복 후보로 묻는다 —
    # 행은 「확인할 내용 2개」(반복 중복 · 카테고리 없는 기록 6건 · 앱 c6b7de3 하네스 · 2026-09-27 fix-up 5 · 예전 「카테고리 없는 기록 6건」 한 항목)
    ('오늘 이체만 있을 때', '오늘 칸은 + 아래 이체. 버튼 위에 「오늘 소비 없음 · 이체 30만」 한 줄이 옵니다. 적금 30만원은 ETF 자동이체 반복 기록과 같은 달 · 카테고리 · 금액이라 반복 중복 후보가 더해져 확인할 내용이 둘입니다.',
     calendar_card(False, states={TODAY: ('—', False, True, False)}, status='오늘 소비 없음 · 이체 30만', review=2)),
    ('확인할 내용이 둘 이상일 때', '행이 「확인할 내용 N개 ›」가 되고 누르면 목록 시트가 열립니다(예: 마감 뒤 8월에 기록을 더한 날). 하나뿐이면 다른 견본처럼 그 항목 이름이고 바로 엽니다.',
     calendar_card(False, review=2)),
    ('아직 오지 않은 날을 눌렀을 때', '기록 창은 열리지 않고 3초 동안 오늘 합계 자리에 이 문장이 옵니다.', future_card),
    ('샘플 데이터로 둘러보는 중일 때', '언제나 이 문장이 위 줄에 있고, 알약 옆은 오늘 합계입니다. ✓ · 0 표시가 없고 확인할 내용 행도 없습니다.', sample_card),
    ('처음 쓰는 날 · 시작일이 오늘일 때', '시작일 전 날도 기록이 없으면 다른 빈 날처럼 —입니다. 오늘 칸의 +와 버튼으로 시작하고, 확인할 내용 행은 없습니다.',
     calendar_card(False, today_empty=True, since=TODAY, review=0)),
    ('달이 바뀐 첫 주(1 ~ 6일)', '스트립에 지난달 날이 들어가 제목이 「최근 7일 소비 기록」이고, 지난달 날은 8/28처럼 달을 붙입니다.', month_start_card),
    ('지난달(8월)을 보다가 ‹를 눌렀을 때', '더 앞선 달은 달력에서 열지 않습니다. 3초 동안 이 문장이 그 달 합계 자리에 옵니다.', blocked_card),
]
# 펼친 달력 · 오늘 기록이 아직 없을 때 — 왼쪽 열 맨 아래(카드가 길어 오른쪽 격자에 두면 한 줄이 통째로 늘어난다)
FIRST_OPEN = calendar_card(True, today_empty=True, review=REVIEW_TODAY_GONE)
assert month_total_text(9, SEP_TOTAL - 37_000) in FIRST_OPEN and '오늘 쓴 돈 적기' in FIRST_OPEN and '더 적기' not in FIRST_OPEN
assert month_total_text(9, 0) == '9월 기록이 아직 없어요'
# 그림의 표식은 1 하나뿐이다 — 첫 줄에만 1 을 달고 나머지 두 줄은 같은 1번의 이어지는 설명(번호 없이 같은 들여쓰기).
STATUS_MEMO = [
    (1, '상태 줄은 언제나 한 문장입니다. 회색 12.5px이고 평가하는 말이나 느낌표를 쓰지 않습니다. 오늘 기록이 0건이면(안 썼어요 표시가 아니면) 문장 대신 '
        '「+ 오늘 쓴 돈 적기」 <span style="white-space: nowrap;">버튼(40)이</span> 오고, 기록이 있으면 문장 오른쪽에 「+ 더 적기」(안 썼어요 표시면 「+ 적기」) 알약이 붙습니다. 알약 줄도 높이 40이라 저장해도 카드 높이가 그대로입니다.'),
    (None, f'달력을 펼치면 그 위에 그 달 합계 한 줄(9월 기록한 소비 {SEP_TOTAL:,}원)이 더 있고, 오늘 합계와 알약(또는 버튼)은 그 아래 줄입니다. 지난달을 볼 때는 8월 합계만 말하고 버튼 · 알약이 없습니다. '
        f'그 달 소비 기록이 0건이면 합계 줄은 0원이 아니라 「{month_total_text(9, 0)}」이고, 안 썼어요 표시만 있으면 「{MARKS_ONLY}」를 붙입니다(버튼일 때는 합계 줄 끝, 알약일 때는 오늘 줄 끝).'),
    (None, '표시가 풀렸어요 · 3초 안내는 어느 달을 보든 오늘 합계 자리를 대신합니다 — 알약 옆 같은 줄이라 줄 높이 40이 그대로이고, 펼친 달력의 그 달 합계 줄과 확인할 내용 행도 그대로입니다. '
        '버튼이 있을 때(오늘 0건)는 버튼 위 한 줄입니다. 샘플 문장은 늘 위 줄이고 알약 옆은 오늘 합계라, 샘플에서 첫 기록을 저장해도 카드 높이가 같습니다. 저장 실패는 여기가 아니라 기록 창 안에 남습니다. '
        '지난달을 보다가 흐린 ‹를 누르면 3초 동안 그 달 합계 자리에 「더 이전 달은 소비 › 내역에서 볼 수 있어요 · 내역 보기 ›」가 옵니다. 칸 아래 범례 줄은 어느 상태에서나 늘 있습니다.'),
]


def cap(title, desc):
    return (f'<div><div style="font-size: 14px; font-weight: 700; letter-spacing: -0.01em; color: {C["INK"]};">{title}</div>'
            f'<div style="font-size: 12px; line-height: 1.5; color: {C["INK3"]}; margin-top: 3px;">{desc}</div></div>')


status_left = (
    f'<div style="width: 362px; flex-shrink: 0; display: flex; flex-direction: column; gap: 8px;">{status_left_card}'
    f'<p style="margin: 2px 2px 8px; font-size: 12px; line-height: 1.5; color: {C["INK3"]};">상태 줄은 '
    f'<b style="font-weight: 600; color: {C["INK2"]};">날짜 칸 아래 한 줄</b>입니다. 그림은 평소(오늘 기록이 있고 저녁 6시 전)입니다.</p>'
    f'{memo_card(STATUS_MEMO)}'
    f'<div style="display: flex; flex-direction: column; gap: 8px; margin-top: 16px;">'
    + cap('펼친 달력 · 오늘 기록이 아직 없을 때', '그 달 합계 한 줄 아래에 버튼이 옵니다. 오늘 칸에는 파란 +. 합계는 오늘을 뺀 그 달 기록입니다.')
    + f'{FIRST_OPEN}</div>'
    f'<div style="display: flex; flex-direction: column; gap: 8px; margin-top: 16px;">'
    + cap('그 달 기록이 0건이고 안 썼어요 표시만 있을 때', '합계 줄이 0원이 아니라 「9월 기록이 아직 없어요 · 안 썼어요 표시만 있어요」입니다. 접어 두면 버튼 위에 「안 썼어요 표시만 있어요」.')
    + f'{zero_month_card}</div></div>')

CSL_H = 2629      # 2026-09-27 fix-up 5 자연 2605 + 24(이체만 견본 설명 · 확인할 내용 2개) · fix-up 2 자연 2587 + 24(오늘 기록이 없는 견본 · 막힌 ‹ 에 확인할 내용 행) · DZ4 검토 — 자연 2549 + 24(아직 오지 않은 날 견본에 범례 줄 · 낱말 묶음) · 이전 자연 2527 + 24(2026-09-26 · 저녁 링크 뒤 · 이체만 · 항목 하나 · 첫 주 · 막힌 ‹ · 그 달 0건)
w('CalendarStatusLines', spec_frame(
    1200, CSL_H, '달력 아래 한 줄이 바뀌는 경우',      # 2026-09-26 DZ3 1570 → 1613(칸 아래 범례 줄 · 자연 1589 + 24)
         # 2026-09-24 1050 → 1160(견본 카드마다 안내 줄 · 적기 줄 40) → 1500(처음 쓰는 날 · 펼친 달력 오늘 0건 견본) → 1540(최종 점검 후속 · 미래 견본의 확인할 내용 행 · 메모) → 1570(통합 점검 · 샘플 문장 위 줄 · 자연 높이 1543.5)
    '접어 둔 달력의 날짜 칸 아래에는 오늘 합계를 말하는 한 문장과 적기 알약(오늘 기록이 없으면 버튼)이 있습니다. 아래 경우에는 그 줄이 바뀝니다.',
    f'<div style="display: flex; gap: 32px; align-items: flex-start;">{status_left}'
    f'{grid2([(cap(t, d), pic) for t, d, pic in STATUS_CASES])}</div>', sub_w=760), keep_all=True)
