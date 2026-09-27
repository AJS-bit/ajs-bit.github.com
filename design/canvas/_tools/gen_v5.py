# -*- coding: utf-8 -*-
"""v5 · 1단계 아트보드 — 하루 시트(안전하고 쉬운 한 건의 기록).

plan/v5-calendar.md §3-4 · §4 · §5-4 · §10 1단계 검토물: 시트 기본(키보드 열림) · 목록 우선 · 수정 모드 ·
완료 카드 · 확인/겹침 · 분류하기 · 히어로 이력 부족 · 360px · 히어로 조건부 각주 조합. 라이트를 만들고
darken()으로 다크 짝을 쓴다. 홈은 Main.dc.html을 잘라 쓴다(히어로 1px 불변 원칙).

키보드는 그리지 않는다 — 시스템 숫자 키보드가 차지하는 자리를 빈 판으로만 표시한다(가짜 키 없음).

2026-09-20 최신화 점검 반영: 새 장 `DaySheetScrolled`(키보드를 내린 하루 시트 — 오늘 기록 · + 1건 더 보기 · 다 적었어요) ·
`HomeDefaultScroll`(기본 5카드 홈 전체 · 390 × 1330). `DaySheet360`은 360 × 640. `DoneCard` · `HeroInsufficient`에 달력 카드.
밖에서 불러 쓰는 조각: spec_frame · mark · case_cap · case_grid · sample · memo_row · sheet_frame · sheet_header · day_sheet_body ·
day_sheet_body_short · today_list · links_row · day_done_btn · more_row · tx_row · recent_chip · neutral_notice · DONE_CARD · limit_forward ·
goal_block · peer_block · calendar_after · calendar_first. (import 하면 v5 장을 모두 다시 쓴다 — 멱등.)

    python3 gen_v5.py
"""
import re
import gen_common
from gen_common import *
import gen_v4 as s1                     # cut · header · hero_block · guide_block · limit_block · OUT
from gen_v4_stocks import nav_v4        # (import 부작용: 2~5단계 파일도 다시 쓴다 — 멱등)
from darken import darken
from nobreak import nobreak          # 낱말 중간 꺾임 묶음(D14) — DZ4 장에만
from gen_calendar import (WD, TODAY, fmt_sum, SEP, SEP_CHECK, SEP_TRANSFER, AUG, AUG_CHECK, AUG_TRANSFER, SEP_TOTAL, AUG_TOTAL,
                          MONTHS, WEEKS, day_state, _mods, cell, gcell, nav_btn, month_bar, month_grid, list_link,
                          calendar_card, hint, status_line, today_tail, review_row, TODAY_TEXT, TODAY_RING,
                          legend, month_total_text, RECENT_TITLE, REVIEW_RECLOSE, REVIEW_UNCAT, REVIEW_PREV_UNCAT, NO_RECORD as CAL_NO_RECORD, pill_row)   # 달력 자료 · 칸 · 카드는 공용 모듈(gen_v4 계열도 함께 쓴다)

OUT = s1.OUT
V5 = ['HomeCalendarStrip', 'HomeDefaultScroll', 'HomeCalendar', 'HomeCalendar360', 'HomeCalendarPrev', 'DaySheet', 'DaySheetScrolled', 'DaySheetList', 'DaySheetEdit',
      'DoneCard', 'DaySheetConfirm', 'ClassifySheet', 'HeroInsufficient', 'DaySheet360', 'HeroFootnotes', 'CalendarCells', 'CalendarGridSizes']

KB_H = 280          # 시스템 숫자 키보드가 덮는 높이(자리만 표시)
SCRIM_H = 60


# DZ4 장(2026-09-26) — body keep-all 과 함께 낱말 중간 꺾임 묶음(nobreak · D14)을 넣는 장. 달력 홈 장(HomeCalendar*)은 DZ3 · gen_tour 가 잘라 쓰므로 뺀다.
DZ4_BOARDS = {'DaySheet', 'DaySheetScrolled', 'DaySheet360', 'DaySheetList', 'DaySheetEdit', 'DaySheetEditMoved', 'DaySheetDeleted', 'DaySheetPastEmpty',
              'DoneCard', 'DaySheetConfirm', 'ClassifySheet', 'ClassifySheetPicker', 'HeroInsufficient', 'HeroFootnotes', 'CalendarCells', 'CalendarGridSizes',
              'HomeDefaultScroll', 'HomeTargetEditor', 'HomeMonthStart', 'HomeSampleMode', 'DaySheetNoSpend', 'ReviewListSheet', 'DaySheetNoSpendStates',
              'DoneCardStates', 'DaySheetStates', 'CalendarStatusLines', 'InsufficientElsewhere', 'FutureProvisional', 'EtcSubline', 'LimitCardCases',
              'RecurringPrefill', 'ImportBackupNotes', 'PayoffStates', 'FutureStates', 'HomeGlanceRows', 'SampleModeTabs', 'DebtUnpayable',
              'HeroOverTarget', 'HomePrimaryGoal', 'HomeTargetSaved'}


def w(name, body, keep_all=False):
    if name in DZ4_BOARDS:
        keep_all = True
    light = doc(body, keep_all=keep_all)
    if name in DZ4_BOARDS:
        light = nobreak(light)
    (OUT / f'{name}.dc.html').write_text(light, encoding='utf-8')
    (OUT / f'Dark{name}.dc.html').write_text(darken(light, name), encoding='utf-8')
    print('wrote', name, '+ Dark' + name)


def won(n):
    return f'{n:,}원'


# ══════════════ 조각 ══════════════
def cat_chip(name, selected=False, size=12.5):
    col = CAT[name]
    if selected:
        return (f'<span style="display: inline-flex; align-items: center; gap: 6px; height: 32px; padding: 0 11px 0 9px; border-radius: 8px; '
                f'background: {C["BRAND_SOFT"]}; border: 1.5px solid {C["BRAND"]}; font-size: {size}px; font-weight: 600; color: {C["INK"]}; white-space: nowrap;">'
                f'<span style="width: 8px; height: 8px; border-radius: 99px; background: {col};"></span>{name}</span>')
    return (f'<span style="display: inline-flex; align-items: center; gap: 6px; height: 32px; padding: 0 11px 0 9px; border-radius: 8px; '
            f'background: {C["SURF"]}; border: 1px solid {C["BORDER"]}; font-size: {size}px; font-weight: 500; color: {C["INK"]}; white-space: nowrap;">'
            f'<span style="width: 8px; height: 8px; border-radius: 99px; background: {col};"></span>{name}</span>')


def recent_chip(memo, amount, cat=None):
    """최근 기록 칩 — 앱 recentEntries 모양 그대로:
    메모 + 카테고리 `커피 4,500 ● 카페/간식` · 메모 + 카테고리 없음 `편의점 6,500 카테고리 없음`(회색 · 점 없음) ·
    메모 없음 + 카테고리 `● 식비 4,500` · 메모도 카테고리도 없음 `카테고리 없음 3,000`. 색만으로 카테고리를 전하지 않게 점 뒤에 이름을 쓴다.
    메모는 8자 + … 로 줄인다. 가로 스크롤 · 최대 5개."""
    memo = memo if len(memo) <= 8 else memo[:8] + '…'
    amt = f'<span style="font-weight: 600;">{amount:,}</span>'
    dot = (lambda c: f'<span style="width: 7px; height: 7px; border-radius: 99px; background: {CAT[c]}; flex-shrink: 0;"></span>')
    none = f'<span style="font-size: 11px; font-weight: 500; color: {C["INK3"]};">카테고리 없음</span>'
    if memo and cat:
        inner = (f'{memo} {amt}<span style="display: inline-flex; align-items: center; gap: 4px; font-size: 11px; font-weight: 500; color: {C["INK2"]};">'
                 f'{dot(cat)}{cat}</span>')
    elif memo:
        inner = f'{memo} {amt}{none}'
    elif cat:
        inner = f'<span style="display: inline-flex; align-items: center; gap: 5px;">{dot(cat)}{cat}</span>{amt}'
    else:
        inner = f'<span style="font-weight: 500;">카테고리 없음</span>{amt}'
    return (f'<span style="display: inline-flex; align-items: center; gap: 7px; height: 32px; padding: 0 11px; border-radius: 8px; background: {C["INSET"]}; '
            f'font-size: 12px; font-weight: 500; color: {C["INK"]}; white-space: nowrap; flex-shrink: 0;">{inner}</span>')


def field_label(text):
    return f'<span style="font-size: 12px; font-weight: 600; line-height: 17px; color: {C["INK2"]};">{text}</span>'


def labeled(label, box, right=''):
    """앱 하루 시트 칸(2026-09-26 · 조각 C 뒤 앱 구조): 이름은 칸 위(12 / 600 · ink-2), 칸은 그 아래."""
    head = (f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px; min-height: 18px; margin-bottom: 6px;">{field_label(label)}{right}</div>'
            if right else f'<div style="display: flex; align-items: center; height: 18px; margin-bottom: 6px;">{field_label(label)}</div>')
    return f'<div style="display: flex; flex-direction: column; flex-shrink: 0;">{head}{box}</div>'


PH_MEMO = '예: 팀 점심'          # 앱 메모 칸의 빈 자리 글자


def amount_box(value, focused=True, selected=False):
    """금액 칸 — 48 · 값은 오른쪽 20 / 600 + 원. 비었으면 `원`만(회색 0 없음). selected = 수정 모드의 전체 선택."""
    ring = f'border: 1.5px solid {C["BRAND"]}; box-shadow: 0 0 0 3px rgba(53,86,230,.16);' if focused else f'border: 1px solid {C["INPUT"]};'
    val = (f'<span style="background: {C["BRAND_SOFT"]}; border-radius: 4px; padding: 1px 3px;">{value}</span>' if (selected and value) else value)
    v = (f'<span style="font-size: 20px; font-weight: 600; letter-spacing: -0.02em; color: {C["INK"]}; font-variant-numeric: tabular-nums;">{val}</span>' if value else '')
    return (f'<div style="display: flex; align-items: center; justify-content: flex-end; gap: 6px; height: 48px; margin: 1px 0; padding: 0 16px; border-radius: 12px; background: {C["SURF"]}; {ring}">'
            f'{v}<span style="font-size: 13px; font-weight: 500; color: {C["INK3"]};">원</span></div>')


def amount_field(value, focused=True, selected=False, w_=None):
    """금액 — 이름 `금액`은 칸 위(앱 구조)."""
    return labeled('금액', amount_box(value, focused, selected))


def memo_box(value='', counter=None, over=False):
    cnt = (f'<span style="font-size: 11px; font-weight: {600 if over else 400}; color: {C["INK2"] if over else C["INK3"]}; white-space: nowrap; flex-shrink: 0;">{counter}</span>'
           if counter else '')
    v = (f'<span style="flex: 1; min-width: 0; font-size: 15px; color: {C["INK"]}; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">{value}</span>' if value
         else f'<span style="flex: 1; font-size: 15px; color: {C["DIS"]};">{PH_MEMO}</span>')
    return (f'<div style="display: flex; align-items: center; gap: 10px; height: 44px; padding: 0 14px; border-radius: 12px; background: {C["SURF"]}; border: 1px solid {C["INPUT"]};">'
            f'{v}{cnt}</div>')


def memo_field(value='', counter=None, over=False):
    """메모 — 이름 `메모`는 칸 위, 빈 칸의 자리 글자 `예: 팀 점심`(앱)."""
    return labeled('메모', memo_box(value, counter, over))


def later_pill(pressed=True):
    """`나중에 고르기` — 카테고리를 안 고른 초안이면 눌린 알약(brand-soft · brand 600 · 1px brand), 골랐으면 안 눌린 외곽선 알약."""
    st = (f'background: {C["BRAND_SOFT"]}; color: {C["BRAND"]}; font-weight: 600; border: 1px solid {C["BRAND"]};' if pressed
          else f'background: {C["SURF"]}; color: {C["INK2"]}; font-weight: 500; border: 1px solid {C["BORDER"]};')
    return (f'<span style="display: inline-flex; align-items: center; height: 24px; padding: 0 8px; border-radius: 99px; {st} font-size: 12px; '
            f'white-space: nowrap; flex-shrink: 0;">나중에 고르기</span>')


# 자주 쓴 카테고리 세 칸 — 앱 categorySlots(시안 사용자 9월 8일 · W/design-state.json · 2026-09-27 fix-up 하네스): 식비 · 카페/간식 · 쇼핑.
# 하루 시트 · 완료 카드 · Components 가 같은 줄을 쓴다(예전 식비 · 카페/간식 · 교통 / 식비 · 쇼핑 · 교통은 지도 세계 · 데모 값).
CANON_SLOTS = ('식비', '카페/간식', '쇼핑')
DEMO_SLOTS = ('식비', '카페/간식', '교통')      # 앱 샘플 모드(데모 자료)의 세 칸 — 샘플 모드 시트만


def category_row(selected=None, frequent=CANON_SLOTS, later='auto', right=None, all_open=False):
    """카테고리 칸 — 이름 `카테고리` + 오른쪽 `나중에 고르기` 알약(later='auto' 면 고른 것이 없을 때 눌림) · 자주 쓴 3칸 + `전체 ›`.
    later=None 이면 알약 없음(샘플 모드 · 이체). right 인수는 옛 호출 호환(right='' → 알약 없음이 아니라 안 눌린 알약).
    고른 카테고리가 세 칸 밖이면 칩을 끼워 넣지 않고 아래 한 줄 `● 교통 선택됨`(앱 .day-sheet-picked · 11.5 ink-2 · 점 8).
    all_open = `전체 ›`를 펼친 상태 — 아래 전체 목록에서 켜져 보이므로 그 줄이 없다(앱 pickedOutside = !allOpen && …)."""
    chips = ''.join(cat_chip(n, selected == n) for n in frequent)
    pill = '' if later is None else later_pill(selected is None if later == 'auto' else bool(later))
    picked = ''
    if selected is not None and selected not in frequent and not all_open:
        picked = (f'<div style="display: flex; align-items: center; gap: 6px; font-size: 11.5px; line-height: 1.4; color: {C["INK2"]};">'
                  f'<span style="width: 8px; height: 8px; border-radius: 99px; background: {CAT[selected]}; flex-shrink: 0;"></span>{selected} 선택됨</div>')
    return (f'<div style="display: flex; flex-direction: column; gap: 8px; flex-shrink: 0;">'
            f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px; min-height: 24px;">{field_label("카테고리")}{pill}</div>'
            f'<div style="display: flex; align-items: center; gap: 6px; overflow: hidden;">{chips}'
            f'<span style="font-size: 12.5px; font-weight: 600; color: {C["BRAND"]}; white-space: nowrap; padding-left: 4px;">전체 &rsaquo;</span></div>{picked}</div>')


def recent_row(chips, pad=18):
    return (f'<div style="display: flex; flex-direction: column; gap: 8px;">{field_label("최근 기록")}'
            f'<div style="display: flex; gap: 6px; overflow: hidden; margin: 0 -{pad}px; padding: 0 {pad}px;">{"".join(chips)}</div></div>')


def unsaved_line(reading, fail=None):
    base = (f'<div style="font-size: 11.5px; line-height: 16.675px; color: {C["INK3"]}; padding: 0 2px; flex-shrink: 0;">'
            f'<span style="font-weight: 600; color: {C["INK2"]};">{reading}</span> · 저장을 눌러야 기록돼요</div>')
    if fail:      # 앱 .day-sheet-error.form-error — 분홍 칸 · 빨간 글 13 · 아이콘 없음 · 문장 끝에 파란 글 버튼 `다시 시도`(테두리 없음 · 600)
        base += (f'<div role="alert" style="display: flex; flex-wrap: wrap; align-items: center; gap: 6px 10px; padding: 9px 12px; background: {C["NEG_SOFT"]}; border-radius: 10px; margin-top: 6px; '
                 f'font-size: 13px; line-height: 1.45;"><span style="color: {C["NEG"]};">{fail}</span>'
                 f'<span style="font-weight: 600; color: {C["BRAND"]}; white-space: nowrap;">다시 시도</span></div>')
    return base


def kb_block(w_=390):
    """시스템 숫자 키보드 자리 — 가짜 키를 그리지 않고 높이만 표시한다."""
    return (f'<div style="position: absolute; left: 0; right: 0; bottom: 0; height: {KB_H}px; background: {C["TRACK"]}; border-top: 1px solid {C["BORDER"]}; '
            f'display: flex; align-items: center; justify-content: center; flex-direction: column; gap: 4px;">'
            f'<span style="font-size: 12px; font-weight: 600; color: {C["INK3"]};">시스템 숫자 키보드 자리</span>'
            f'<span style="font-size: 11px; color: {C["INK4"]};">기기가 그립니다 · 약 {KB_H}px · 이 위로 날짜·금액·저장이 보여야 해요</span></div>')


def scrim_line(text):
    return (f'<div style="height: {SCRIM_H}px; display: flex; align-items: flex-end; justify-content: center; padding: 0 20px 12px; flex-shrink: 0; text-align: center;">'
            f'<span style="font-size: 11px; line-height: 1.4; font-weight: 500; color: rgba(255,255,255,.62);">{text}</span></div>')


def sheet_header(title, sub, today=True, next_on=False, arrows=True, chip=None, weight=None):
    """새 기록 · 목록은 제목 양옆 ‹ › 로 날짜를 옮긴다. next_on = 다음 날로 갈 수 있을 때 진한 색.
    arrows=False = 기록 수정 · 카테고리 고르기(날짜는 본문 `날짜` 칸으로 옮긴다). chip = 제목 옆 회색 글(기본 today 면 `오늘` · 어제는 `어제`).
    앱 b574373 .day-sheet-header 상자 그대로(2026-09-27 fix-up 4): 위 20 · 좌우 18 · 아래 12 + 아래 선 · 손잡이(38 × 4)는 시트 윗변 8 아래에 겹쳐 그린다 ·
    제목 줄은 ‹ › 가 있으면 28(가운데 맞춤), 없으면 제목 줄 높이 21.6 · 둘째 줄(12.5 · 줄 높이 1.45)은 3 아래 · `닫기`는 위 4."""
    fw = weight or (700 if today else 600)      # 오늘 700 · 다른 날 600(앱 .day-sheet-title[data-today=false])
    t = f'<h2 style="margin: 0; font-size: 18px; font-weight: {fw}; line-height: 21.6px; letter-spacing: -0.025em; color: {C["INK"]}; white-space: nowrap;">{title}</h2>'
    chip = chip if chip is not None else ('오늘' if today else None)
    if chip:
        t += f'<span style="font-size: 12.5px; font-weight: 500; line-height: 17.86px; color: {C["INK3"]}; margin-left: 6px; white-space: nowrap;">{chip}</span>'
    # ‹ › = 앱 .day-sheet-nav — 28 × 28 가운데 맞춤 칸(제목은 x ≈ 50)
    nav = lambda ic, col: (f'<span style="width: 28px; height: 28px; display: inline-flex; align-items: center; justify-content: center; flex-shrink: 0;">'
                           f'{icon(ic, 18, col, 2)}</span>')
    left = nav("left", C["INK2"]) if arrows else ''
    right = nav("right", C["INK2"] if next_on else "#C4CCDA") if arrows else ''
    row_h = 'min-height: 28px; ' if arrows else ''
    return (f'<div style="position: relative; display: flex; align-items: flex-start; justify-content: space-between; gap: 10px; padding: 20px 18px 12px; border-bottom: 1px solid {C["LINE_SOFT"]}; flex-shrink: 0;">'
            f'<span style="position: absolute; top: 8px; left: 50%; margin-left: -19px; width: 38px; height: 4px; border-radius: 99px; background: {C["BORDER"]};"></span>'
            f'<div style="display: flex; flex-direction: column; gap: 3px; min-width: 0;">'
            f'<div style="display: flex; align-items: center; gap: 4px; {row_h}">{left}<div style="display: flex; align-items: center;">{t}</div>{right}</div>'
            f'<span style="font-size: 12.5px; line-height: 18.125px; color: {C["INK3"]};">{sub}</span></div>'
            f'<span style="font-size: 13px; font-weight: 600; line-height: 18.57px; color: {C["INK2"]}; padding-top: 4px; flex-shrink: 0; white-space: nowrap;">닫기</span></div>')


SCRIM_TEXT = '배경을 눌러 닫기 · 앱이 다시 시작되면 저장하지 않은 내용은 사라져요'      # 계획 §4-2 원문


SHEET_TOP = 30          # 앱 시트가 화면 끝까지 올라올 때의 윗변(100dvh − 30 · 하네스 · 에뮬레이터 모두 30)
SHEET_BORDER = f'border: 1px solid {C["LINE"]}; border-bottom: 0;'      # 앱 .structured-dialog 1px 선(아래는 화면 끝)


def sheet_frame(inner, w_=390, keyboard=False, scrim_text=SCRIM_TEXT, h_=844, fit=False, footer=''):
    """fit=True = 시트가 내용 높이만큼만 아래에서 올라온다 — 위 어두운 배경의 안내는 시트 윗변 바로 위(아래 12)에 붙는다.
    fit=False = 시트가 화면 끝까지(윗변 30) 올라와 안내가 들어갈 자리가 없다 — 앱처럼 안내를 그리지 않는다(2026-09-27 fix-up 4 · 예전 60 띠 + 안내).
    keyboard=True = 키보드가 열린 모습: 앱 창이 키보드 위로 줄어(390 × 564 · 에뮬레이터 확인) 시트는 30 ~ 564, footer(저장 띠)가 그 바닥에 붙는다."""
    kb = kb_block(w_) if keyboard else ''
    if fit:
        return (f'<div style="width: {w_}px; height: {h_}px; background: #2A3245; color: {C["INK"]}; display: flex; flex-direction: column; overflow: hidden; position: relative; font-variant-numeric: tabular-nums;">'
                f'<div style="flex: 1; min-height: 0; display: flex; align-items: flex-end; justify-content: center; padding: 0 20px 12px; text-align: center;">'
                f'<span style="font-size: 11.5px; font-weight: 500; color: rgba(255,255,255,.62);">{scrim_text}</span></div>'
                f'<div style="flex-shrink: 0; background: {C["SURF"]}; {SHEET_BORDER} border-radius: 26px 26px 0 0; display: flex; flex-direction: column; overflow: hidden;">{inner}{footer}</div>{kb}</div>')
    sheet_h = h_ - SHEET_TOP - (KB_H if keyboard else 0)
    return (f'<div style="width: {w_}px; height: {h_}px; background: #2A3245; color: {C["INK"]}; display: flex; flex-direction: column; overflow: hidden; position: relative; font-variant-numeric: tabular-nums;">'
            f'<div style="height: {SHEET_TOP}px; flex-shrink: 0;"></div>'
            f'<div style="height: {sheet_h}px; flex-shrink: 0; background: {C["SURF"]}; {SHEET_BORDER} border-radius: 26px 26px 0 0; display: flex; flex-direction: column; overflow: hidden;">{inner}{footer}</div>{kb}</div>')


def sheet_body(inner, end=False, pad_top=12, pad_bottom=21):
    """앱 .dialog-body.day-sheet-body — 12 18 20(+ 시트 아래 선 1) · 칸 사이 10. end=True = 본문을 끝까지 내린 모습(아래에 맞추고 위가 머리줄 밑으로 가려진다)."""
    al = ' justify-content: flex-end;' if end else ''
    return (f'<div style="flex: 1; min-height: 0; overflow: hidden; padding: {pad_top}px 18px {pad_bottom}px; display: flex; flex-direction: column; gap: 10px;{al}">'
            f'{inner}</div>')


def save_footer(inner):
    """앱 .day-sheet-save-footer — 키보드가 열려 창이 700 아래로 줄면 저장이 본문 밖 바닥 띠로 간다(위 선 · 12 18 12 · 버튼 위 2)."""
    return (f'<div style="padding: 12px 18px 12px; border-top: 1px solid {C["LINE_SOFT"]}; background: {C["SURF"]}; flex-shrink: 0;">'
            f'<div style="margin-top: 2px;">{inner}</div></div>')


def save_btn(label='저장'):
    return btn(label, 'primary', h=52, radius=14, size=16)


LINKS_NOTE = '저축·투자와 대출상환은 계좌까지 고르는 기록 창에서 남겨요 · 소비율에는 안 들어가요'      # 앱 문구(record-7 B · D4 거래 → 기록)


def links_row(note=True):
    links = (f'<div style="display: flex; align-items: center; gap: 14px; height: 28px;">'
             f'<span style="font-size: 12.5px; font-weight: 600; color: {C["BRAND"]}; white-space: nowrap;">저축·투자로 기록 &rsaquo;</span>'
             f'<span style="font-size: 12.5px; font-weight: 600; color: {C["BRAND"]}; white-space: nowrap;">대출상환으로 기록 &rsaquo;</span></div>')
    if not note:
        return links
    return (f'<div style="display: flex; flex-direction: column; gap: 4px;">{links}'
            f'<span style="font-size: 11.5px; line-height: 17.25px; color: {C["INK3"]};">{LINKS_NOTE}</span></div>')


def links_block(note=True):
    """본문 안 링크 묶음(앱 .day-sheet-links 위 4)."""
    return f'<div style="padding-top: 4px; flex-shrink: 0;">{links_row(note)}</div>'


def day_done_btn(label):
    """시트 맨 아래 확인 버튼 — `9월 8일 다 적었어요`(소비 1건 이상 · 시간 무관). 채운 Primary 가 아니다(시트 안 채운 Primary 는 `저장` 하나)."""
    return btn(label, 'secondary', h=44, radius=12, size=12.5).replace('font-weight: 600;">', 'font-weight: 600; white-space: nowrap; flex-shrink: 0;">', 1)


# 버튼 아래 효과 줄(record-11 #1 · 앱 문구) — 누르면 무엇이 남는지
EFFECT_DONE_TODAY = '누르면 달력에 ✓가 남고 오늘 저녁엔 더 묻지 않아요'
EFFECT_DONE_PAST = '누르면 달력에 ✓가 남아요 · 안 눌러도 기록은 그대로예요'
EFFECT_ZERO_TODAY = '누르면 달력에 0으로 남고 오늘 기록 알림은 오지 않아요'
EFFECT_ZERO_PAST = '누르면 달력에 0으로 남아요 · 빈 날(—)과 구분돼요'


def effect_line(text):
    return f'<div style="font-size: 12px; line-height: 17.4px; color: {C["INK3"]}; padding: 0 2px;">{text}</div>'


def day_done(label, effect):
    """`다 적었어요` · `안 썼어요` 버튼 + 그 아래 효과 줄."""
    return f'<div style="padding-top: 4px; flex-shrink: 0; display: flex; flex-direction: column; gap: 4px;">{day_done_btn(label)}{effect_line(effect)}</div>'


def more_row(label='1건 더 보기'):
    return (f'<div style="display: flex; align-items: center; gap: 4px; height: 28px; padding: 0 2px; align-self: flex-start; flex-shrink: 0; font-size: 12.5px; font-weight: 600; color: {C["BRAND"]}; white-space: nowrap;">'
            f'{icon("plus", 13, C["BRAND"], 2.4)}{label}</div>')


def tx_row(cat, memo, amount, last=False, h=46, hl=False):
    """하루 기록 목록 행. cat=None = `카테고리 없음`. hl = 수정 중인 행(brand-soft 바탕 · 앱)."""
    bb = '' if last else f'border-bottom: 1px solid {C["LINE_ROW"]};'
    if hl:
        bb = f'background: {C["BRAND_SOFT"]}; border-radius: 8px;'
    if cat:
        left = (f'<span style="display: inline-flex; align-items: center; gap: 6px; width: 96px; flex-shrink: 0;"><span style="width: 8px; height: 8px; border-radius: 99px; background: {CAT[cat]};"></span>'
                f'<span style="font-size: 12.5px; font-weight: 500; color: {C["INK2"]}; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">{cat}</span></span>')
    else:
        left = f'<span style="width: 96px; flex-shrink: 0; font-size: 12.5px; font-weight: 500; color: {C["INK3"]}; white-space: nowrap;">카테고리 없음</span>'
    return (f'<div style="display: flex; align-items: center; gap: 10px; height: {h}px; flex-shrink: 0; {bb}">{left}'
            f'<span style="flex: 1; min-width: 0; font-size: 14px; color: {C["INK"]}; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">{memo}</span>'
            f'<span style="font-size: 14.5px; font-weight: 600; letter-spacing: -0.02em; color: {C["INK"]};">{won(amount)}</span>{icon("right", 15, C["INK4"], 2)}</div>')


def dashed_row(label):
    return (f'<div style="display: flex; align-items: center; justify-content: center; gap: 6px; height: 46px; border-radius: 14px; border: 1.5px dashed #B9C3D6; '
            f'background: rgba(255,255,255,.55); color: {C["BRAND"]}; font-size: 14px; font-weight: 600;">{icon("plus", 15, C["BRAND"], 2.4)}{label}</div>')


# ── 구현 참고 장(앱 화면이 아닌 설명 장)의 틀 — 번호 표시 · 알약 달린 넓은 장 ──
def mark(n, floating=False, pos=None):
    """번호 표시. floating = 달력 칸의 오른쪽 위에 얹는다. pos = 자리를 직접 줄 때."""
    if pos is None:
        pos = 'position: absolute; top: -4px; right: 0;' if floating else 'flex-shrink: 0; margin-top: 1px;'
    return (f'<span style="{pos} width: 17px; height: 17px; border-radius: 99px; background: {C["INK"]}; color: #FFFFFF; '
            f'font-size: 10.5px; font-weight: 700; display: inline-flex; align-items: center; justify-content: center; '
            f'box-shadow: 0 0 0 2px {C["SURF"]};">{n}</span>')


def spec_frame(w_, h_, title, sub, body, sub_w=640):
    chip = (f'<span style="align-self: flex-start; font-size: 11px; font-weight: 600; letter-spacing: 0.02em; color: {C["INK2"]}; '
            f'border: 1px solid {C["LINE"]}; background: {C["SURF"]}; border-radius: 99px; padding: 4px 10px;">구현 참고 · 앱 화면이 아닙니다</span>')
    return (f'<div style="width: {w_}px; height: {h_}px; background: {C["BG"]}; color: {C["INK"]}; padding: 28px 30px 30px; display: flex; '
            f'flex-direction: column; gap: 10px; overflow: hidden; font-variant-numeric: tabular-nums;">{chip}'
            f'<h2 style="margin: 2px 0 0; font-size: 20px; font-weight: 700; letter-spacing: -0.025em; color: {C["INK"]};">{title}</h2>'
            f'<p style="margin: 0 0 8px; font-size: 13px; line-height: 1.55; color: {C["INK3"]}; max-width: {sub_w}px;">{sub}</p>{body}</div>')


def case_cap(n, title, desc):
    """견본 위 설명 — 번호 + 상황을 말하는 제목 + 한 줄 설명."""
    return (f'<div><div style="display: flex; align-items: center; gap: 7px;">{mark(n, pos="flex-shrink: 0;")}'
            f'<span style="font-size: 14px; font-weight: 700; letter-spacing: -0.01em; color: {C["INK"]};">{title}</span></div>'
            f'<div style="font-size: 12px; line-height: 1.5; color: {C["INK3"]}; margin-top: 3px;">{desc}</div></div>')


def case_grid(samples):
    """왼쪽 온전한 그림 옆에 놓는 견본 2 × 2 — 견본은 앱의 카드 폭(362) 그대로."""
    cells = ''.join(f'<div style="display: flex; flex-direction: column; gap: 8px; min-width: 0;">{cap}{pic}</div>' for cap, pic in samples)
    return f'<div style="flex: 1; min-width: 0; display: grid; grid-template-columns: repeat(2, 362px); gap: 24px 20px; align-items: start;">{cells}</div>'


def sample(width, title, line, inner):
    """견본 하나 — 상황을 말하는 제목 + 한 줄 설명 + 그림."""
    return (f'<div style="width: {width}px; flex-shrink: 0; display: flex; flex-direction: column; gap: 8px;">'
            f'<div><div style="font-size: 14px; font-weight: 700; letter-spacing: -0.01em; color: {C["INK"]};">{title}</div>'
            f'<div style="font-size: 12px; line-height: 1.5; color: {C["INK3"]}; margin-top: 2px;">{line}</div></div>{inner}</div>')


# ══════════════ 1. 시트 기본 — 오늘 · 키보드 열림 ══════════════
# 최근 기록 칩 = 앱 recentEntries(30일 · 메모 + 금액 + 카테고리로 묶어 잦은 순 → 최근 날짜 · 최대 5 · record-17). 시안 사용자 9월 8일에 앱이 보이는 그대로(W/tools/dz4/app/log-all.json).
RECENT = [('커피', 4500, None), ('점심', 9000, '식비'), ('커피', 4500, '카페/간식'), ('생필품', 17000, '쇼핑'), ('편의점', 6500, None)]
TODAY_ROWS = [('카페/간식', '커피', 4500), ('식비', '점심', 9000), ('쇼핑', '생필품', 17000)]      # 오늘 4건 37,000원 중 앞 3건(dayTransactions 순서) — 넷째는 편의점 6,500원(카테고리 없음)
assert sum(a for _, _, a in TODAY_ROWS) + 6500 == 37_000


def today_list(h=44, rows=TODAY_ROWS, more='1건 더 보기', label='오늘 기록'):
    """키보드 경계 아래 — `오늘 기록` 라벨 + 3행 + `+ 1건 더 보기`(오늘 4건 37,000원 중 3건)."""
    body = ''.join(tx_row(c, m, a, last=(i == len(rows) - 1), h=h) for i, (c, m, a) in enumerate(rows))
    return (f'<div style="display: flex; flex-direction: column; gap: 8px; flex-shrink: 0;">{field_label(label)}'
            f'<div style="display: flex; flex-direction: column;">{body}</div>' + (more_row(more) if more else '') + '</div>')


def day_sheet_inputs(amount='12,000', memo='편의점', selected=None, keyboard=True, fail=None, pad=18):
    return (amount_field(amount, focused=keyboard)
            + unsaved_line('1.2만원', fail)
            + memo_field(memo)
            + category_row(selected)
            + recent_row([recent_chip(*r) for r in RECENT], pad))


def day_sheet_body(w_=390, fail=None, amount='12,000', memo='편의점', selected=None, keyboard=True):
    """하루 시트 본문(오늘). keyboard=True 는 키보드 열림(기본 아트보드) — 앱 창이 키보드 위로 줄어 저장은 바닥 띠(save_footer)로 가고 본문은 링크 줄에서 잘린다.
    False 는 키보드를 내리고 끝까지 내린 상태 — 위쪽 금액 칸이 머리줄 밑으로 밀려 올라가고 그 아래 `오늘 기록` · `+ 1건 더 보기` · `9월 8일 다 적었어요` + 효과 줄까지(저장은 본문 안)."""
    ins = day_sheet_inputs(amount, memo, selected, keyboard, fail)
    if keyboard:
        return (sheet_header('9월 8일 소비 기록', '오늘 4건 37,000원')
                + sheet_body(ins + links_block() + today_list()))
    return (sheet_header('9월 8일 소비 기록', '오늘 4건 37,000원')
            + sheet_body(ins + f'<div style="margin-top: 2px; flex-shrink: 0;">{save_btn()}</div>' + links_block() + today_list()
                         + day_done("9월 8일 다 적었어요", EFFECT_DONE_TODAY), end=True))


def day_sheet_body_short(w_=360):
    """360 × 640 — 키보드를 내리고 본문을 끝까지 민 상태. 창 높이가 700 아래라 `저장`은 바닥 띠에 고정되고(앱 max-height 700) 위 영역만 스크롤된다(계획 §8 좁은 화면).
    좌우 여백 = 앱 --day-sheet-x 18(본문 12 18 20 · 바닥 띠 12 18 12)."""
    return (sheet_header('9월 8일 소비 기록', '오늘 4건 37,000원')
            + sheet_body(day_sheet_inputs(keyboard=False) + links_block() + today_list() + day_done("9월 8일 다 적었어요", EFFECT_DONE_TODAY), end=True, pad_bottom=20))


w('DaySheet', sheet_frame(day_sheet_body(), keyboard=True, footer=save_footer(save_btn())))
# 같은 시트에서 키보드를 내리고 끝까지 내린 상태 — 오늘 기록 · + 1건 더 보기 · 다 적었어요 + 효과 줄이 보인다
w('DaySheetScrolled', sheet_frame(day_sheet_body(keyboard=False)))
# 가장 작은 화면 360 × 640 — 목록 3행 + `+ 1건 더 보기` + 다 적었어요 + `저장`까지 보이고 위 영역만 스크롤 · 푸터 고정
w('DaySheet360', sheet_frame(day_sheet_body_short(360), w_=360, h_=640, footer=save_footer(save_btn())))


# ══════════════ 2. 목록 우선 — 기록 있는 과거 날 ══════════════
# 행 순서 = 앱 dayTransactions(기록 순서) — 캐논 W/design-state.json 의 tx-10 택시 · tx-11 점심 · tx-12 간식(카테고리 없음) · LedgerV5 날짜 묶음과 같은 순서.
# 목록 위에는 늘 `9월 3일 기록` 이름(앱). 2026-09-27 fix-up 2 — 예전 점심 · 간식 · 택시는 옛 지도 세계의 순서였다.
DAY3_ROWS = [('교통', '택시', 45000), ('식비', '점심', 9000), (None, '간식', 4500)]


def day3_list(rows=DAY3_ROWS, hl=None, label='9월 3일 기록'):
    return (f'<div style="display: flex; flex-direction: column; gap: 8px; flex-shrink: 0;">{field_label(label)}'
            + card(''.join(tx_row(c, m, a, last=(i == len(rows) - 1), hl=(hl == m)) for i, (c, m, a) in enumerate(rows)), pad='2px 14px')
            + '</div>')      # 앱 목록 우선 · 수정 모드 — 카드(선 1 · 18 · 안쪽 2 14) 안 행 46


def list_body_of(sub, rows=DAY3_ROWS, notice=''):
    return (sheet_header('9월 3일 소비 기록', sub, today=False, next_on=True)      # 오늘(9월 8일)보다 앞선 날 — › 는 오늘에서만 멈춘다
            + notice
            + sheet_body(day3_list(rows) + dashed_row('추가') + links_block()
                         + day_done("9월 3일 다 적었어요", EFFECT_DONE_PAST)))      # 소비 1건 이상이면 시간과 무관하게 보인다


w('DaySheetList', sheet_frame(list_body_of('3건 58,500원'), fit=True))      # 시트는 내용 높이만큼(앱 · 짧은 날은 아래에서 올라온다)


# ══════════════ 3. 수정 모드 ══════════════
# record-15: 제목 양옆 ‹ › 없음 · 둘째 줄은 그날 합계만 · 첫 칸 `날짜 9월 3일 ▾`(기기 날짜 고르기 · 지난달 1일 ~ 오늘) · 읽기 줄에 `저장을 눌러야 기록돼요` ·
# 카테고리는 이미 골라서 `나중에 고르기`가 안 눌린 외곽선. 키보드 아래에는 그날 목록(고치는 행 강조) + 다 적었어요가 이어진다(키보드에 가림).
def date_box(text, focused=False):
    ring = f'border: 1.5px solid {C["BRAND"]}; box-shadow: 0 0 0 3px rgba(53,86,230,.16);' if focused else f'border: 1px solid {C["INPUT"]};'
    return (f'<div style="display: flex; align-items: center; height: 44px; padding: 0 14px; border-radius: 12px; background: {C["SURF"]}; {ring}">'
            f'<span style="display: inline-flex; align-items: center; gap: 6px; font-size: 15px; font-weight: 600; color: {C["INK"]}; white-space: nowrap;">{text}'
            f'<svg width="10" height="10" viewBox="0 0 10 10"><path d="M1 3h8L5 8Z" fill="{C["INK"]}"/></svg></span></div>')


def edit_buttons():
    return (f'<div style="display: flex; gap: 8px;">{btn("저장", "primary", h=52, radius=14, size=16).replace("width: 100%;", "flex: 3;")}'
            f'{btn("삭제", "secondary", h=52, radius=14, size=15).replace("width: 100%;", "flex: 2;")}</div>')      # 앱 206 : 138


def edit_body_of(date='9월 3일', moved=None, keyboard=False):
    """moved = 옮길 날 — `저장하면 9월 3일 → 9월 2일로 옮겨요` 한 줄이 날짜 칸 아래에(앱 .day-sheet-date-note). 옮기는 동안 다 적었어요 · 안 썼어요는 숨는다.
    keyboard=True = 금액 칸에 키보드가 열린 모습 — 저장 · 삭제는 바닥 띠(save_footer)로 가고 본문은 카테고리 아래에서 잘린다."""
    move_note = (f'<div style="font-size: 11.5px; font-weight: 500; line-height: 16.675px; color: {C["INK2"]}; margin-top: 6px;">저장하면 9월 3일 → {moved}로 옮겨요</div>'
                 if moved else '')
    date_field = labeled('날짜', date_box(moved or date, focused=bool(moved))).replace('</div></div>', '</div>' + move_note + '</div>', 1) if moved else labeled('날짜', date_box(date))
    ins = (date_field
           + amount_field('45,000', focused=not moved, selected=not moved)
           + unsaved_line('4.5만원')
           + memo_field('택시')
           + category_row('교통'))
    tail = day3_list(hl='택시') + ('' if moved else day_done("9월 3일 다 적었어요", EFFECT_DONE_PAST))
    actions = '' if keyboard else f'<div style="margin-top: 2px; flex-shrink: 0;">{edit_buttons()}</div>'
    return (sheet_header('9월 3일 기록 수정', '3건 58,500원', today=False, arrows=False)
            + sheet_body(ins + actions + tail))


w('DaySheetEdit', sheet_frame(edit_body_of(keyboard=True), keyboard=True, footer=save_footer(edit_buttons())))
# 새 장 — 날짜 칸에서 9월 2일을 골랐을 때(record-15 #2 · 앱 day-sheet moved). 기기 날짜 고르기를 닫은 직후라 날짜 칸에 포커스 · 숫자 키보드 없음 ·
# 시트는 내용 높이(앱) — 아래로 그날 목록(고치는 행 강조)까지 보이고 다 적었어요 · 안 썼어요는 숨는다.
w('DaySheetEditMoved', sheet_frame(edit_body_of(moved='9월 2일'), fit=True))

# 새 장 — 시트 안에서 지운 뒤(record-6 #3 · D10): 머리줄 아래 상태 띠 `지웠어요 · 택시 45,000원 · 되돌리기`, 남은 목록 · + 추가 · 링크 · 다 적었어요 + 효과 줄.
# 시트 뒤 아래 알림 카드는 없다(시트 안에서 알린다).
DELETED_STRIP = (f'<div role="status" style="padding: 8px 18px; border-bottom: 1px solid {C["LINE_SOFT"]}; background: {C["INSET"]}; font-size: 11.5px; font-weight: 500; '
                 f'line-height: 16.675px; color: {C["INK2"]}; flex-shrink: 0;">지웠어요 · 택시 45,000원 · <span style="font-weight: 600; color: {C["BRAND"]};">되돌리기</span></div>')      # 앱 .day-sheet-inline-notice — 머리줄 바로 아래 온 폭 띠 · 아이콘 없음
w('DaySheetDeleted', sheet_frame(list_body_of('2건 13,500원', rows=DAY3_ROWS[1:], notice=DELETED_STRIP), fit=True))      # 택시를 지운 뒤 = 점심 · 간식(앱)

# 새 장 — 기록 없는 지난 날(어제 · record-11 · record-18): 제목 옆 `어제` · 둘째 줄 `9월 7일 소비는 아직 기록이 없어요` · 빈 금액(원만) ·
# 읽기 줄 `금액을 넣거나, 안 썼으면 「9월 7일은 안 썼어요」로 표시해요` · 회색 저장 · 맨 아래 `9월 7일은 안 썼어요` + 효과 줄. 키보드를 내린 모습.
SAVE_OFF = btn('저장', 'disabled', h=52, radius=14, size=16)


def reason_line(text):
    """금액 아래 한 줄(회색 11.5) — unsaved_line 과 같은 자리 · 같은 모양(a11y-1 저장이 안 되는 까닭)."""
    return f'<div style="font-size: 11.5px; line-height: 16.675px; color: {C["INK3"]}; padding: 0 2px; flex-shrink: 0;">{text}</div>'


past_empty_body = (
    sheet_header('9월 7일 소비 기록', '9월 7일 소비는 아직 기록이 없어요', today=False, next_on=True, chip='어제')
    + sheet_body(amount_field('', focused=False)
                 + reason_line('금액을 넣거나, 안 썼으면 「9월 7일은 안 썼어요」로 표시해요')
                 + memo_field('')
                 + category_row(None)
                 + recent_row([recent_chip(*r) for r in RECENT], 18)
                 + f'<div style="margin-top: 2px; flex-shrink: 0;">{SAVE_OFF}</div>'
                 + links_block()
                 + day_done("9월 7일은 안 썼어요", EFFECT_ZERO_PAST)))
w('DaySheetPastEmpty', sheet_frame(past_empty_body, fit=True))


# ══════════════ 4. 완료 카드 — 홈 위 ══════════════
# 저장 뒤 홈: 히어로는 Main과 같은 자리·모양이고 값만 12,000원 저장 뒤로(2026-09-24 — 큰 숫자 · 게이지 · 설명 줄 = 지금까지 쓴 돈):
# 쓴 돈 1,120,000 → 1,132,000 · 31.1 → 31.4% · 112만 → 113만원 · 목표까지 28.9 → 28.6%p 남음 · 채움 inset 68.9 → 68.6%,
# 아래 칸(월말 예상 기준)은 208 → 210만원 · 여유 8 → 6만원(배지 `월말에도 목표 안` 그대로 · 210 ÷ 360 = 58.3%) · 순자산 대비 1.2% 그대로 · 하루 47,270 → 46,730원.
# 2026-09-26(DZ3 호환 · Main 이 앱 히어로로 바뀜): 오른쪽 줄은 돈(소비 목표까지 103만원 남음) · 캐논 각주의 카테고리 없는 금액 32,000 → 44,000원 ·
# 한도 `오늘 포함 하루 44,700원` · 둘째 줄 `216만원 중 113만원 썼어요` — NUMBERS §6. 완료 카드 문구 · 모양은 DZ4 몫.
hero_after = s1.hero_block
for a, b in [('>31.1<', '>31.4<'), ('104만원 남음', '103만원 남음'), ('inset: 0 68.9% 0 0', 'inset: 0 68.6% 0 0'),
             ('월급 360만원 중 112만원 썼어요', '월급 360만원 중 113만원 썼어요'),
             ('>208<span', '>210<span'), ('>8<span style="font-size: 13px; font-weight: 500; color: #0F7B47;">만원', '>6<span style="font-size: 13px; font-weight: 500; color: #0F7B47;">만원'),
             ('카테고리 없는 32,000원', '카테고리 없는 44,000원')]:
    assert hero_after.count(a) == 1, a
    hero_after = hero_after.replace(a, b)
limit_after = s1.limit_block
for a, b in [('남은 한도 104만원', '남은 한도 103만원'), ('inset: 0 48.1% 0 0', 'inset: 0 47.6% 0 0'),
             ('오늘 포함 하루 45,220원', '오늘 포함 하루 44,700원'), ('216만원 중 112만원 썼어요', '216만원 중 113만원 썼어요')]:
    assert limit_after.count(a) == 1, a
    limit_after = limit_after.replace(a, b)

# 셋째 줄 — 이 장의 저장은 DaySheet 에서 카테고리를 고르지 않은(`나중에 고르기`) 편의점 12,000원이라 계획 §4-4 우선순위의 4순위 문장 + 칩 줄이 온다(record-12 #1).
# 6순위 `월급의 31.1% → 31.4%`(지금까지 쓴 돈 ÷ 월급, 저장 전 → 뒤 · 2026-09-24)는 앞선 조건이 하나도 없고 월급이 있을 때만 — 히어로의 31.4% 등 값은 그대로다.
# 둘째 줄은 무엇을 저장했는지 말한다(record-20 #1): 날짜 · 메모 · 카테고리(없으면 `카테고리 없음`) 금액 저장 · 그날 합계. 버튼은 `한 건 더` · `되돌리기`(record-6 #2 · D10).
DONE_THIRD = '소비에는 이미 포함됐어요 · 지금 카테고리를 고를까요?'      # 앱 문구(record-12 #1 · D4)
DONE_MAIN = '9월 8일 · 편의점 · 카테고리 없음 <span style="font-weight: 700;">12,000원</span> 저장 · 오늘 5건 49,000원'
DONE_CHIPS = CANON_SLOTS      # 앱 categorySlots(before) — 시안 사용자 9월 8일(카테고리 없이 저장한 뒤 · 하네스 2026-09-27: 식비 · 카페/간식 · 쇼핑)


def done_chip(name):
    return (f'<span style="display: inline-flex; align-items: center; gap: 6px; height: 32px; padding: 0 12px 0 10px; border-radius: 99px; '
            f'border: 1px solid rgba(255,255,255,.34); background: rgba(255,255,255,.06); color: #FFFFFF; font-size: 13px; font-weight: 600; white-space: nowrap; flex-shrink: 0;">'
            f'<span style="width: 8px; height: 8px; border-radius: 99px; background: {CAT[name]};"></span>{name}</span>')


DONE_CHIP_ROW = ('<div style="display: flex; align-items: center; gap: 6px; margin-top: 9px;">' + ''.join(done_chip(n) for n in DONE_CHIPS)
                 + '<span style="font-size: 13px; font-weight: 600; color: #FFFFFF; white-space: nowrap; padding-left: 4px;">전체 &rsaquo;</span></div>')
DONE_BTN = {'main': 'padding: 0 14px; border: 1px solid rgba(255,255,255,.55); color: #FFFFFF; font-weight: 700;',
            'undo': 'padding: 0 14px; border: 1px solid rgba(255,255,255,.28); color: #FFFFFF; font-weight: 600;'}


def done_btn(label, kind):
    return (f'<span style="display: inline-flex; align-items: center; justify-content: center; height: 36px; border-radius: 10px; font-size: 13px; white-space: nowrap; flex-shrink: 0; {DONE_BTN[kind]}">{label}</span>')


DONE_CARD = ('<!--dc-keep--><div style="position: absolute; left: 14px; right: 14px; bottom: 78px; background: #101828; border-radius: 16px; padding: 13px 14px 12px; color: #FFFFFF; box-shadow: 0 8px 24px rgba(0,0,0,.28);">'
             '<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px;">'
             '<span style="display: inline-flex; align-items: center; gap: 7px; font-size: 14px; font-weight: 700;"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#3DD489" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg>저장했어요</span>'
             '<span style="font-size: 12px; font-weight: 600; color: rgba(255,255,255,.72);">닫기</span></div>'
             f'<div style="font-size: 13.5px; line-height: 1.45; font-weight: 500; margin-top: 7px; color: #FFFFFF;">{DONE_MAIN}</div>'
             f'<div style="font-size: 12.5px; margin-top: 3px; color: rgba(255,255,255,.72);">{DONE_THIRD}</div>'
             + DONE_CHIP_ROW
             + f'<div style="display: flex; gap: 8px; margin-top: 11px;">{done_btn("한 건 더", "main")}{done_btn("되돌리기", "undo")}</div>'
             '</div><!--/dc-keep-->')
assert '취소' not in DONE_CARD and '분류' not in DONE_CARD

# 달력은 저장 결과를 반영한다 — 오늘(8일) 칸 3.7만 → 4.9만, 상태 줄 `오늘 5건 49,000원`.
# 카테고리 없이 저장했으니 확인할 내용은 `카테고리 없는 기록 8건 · 카테고리 고르기`(7 + 1 · 앱) — 완료 카드 밑에 가려지지만 값은 맞춘다.
calendar_after = calendar_card(False, states={TODAY: (fmt_sum(49_000), False, False, False)}, status='오늘 5건 49,000원',
                               review='카테고리 없는 기록 8건 · 카테고리 고르기')
assert calendar_after.count('>4.9만<') == 1 and '3.7만' not in calendar_after
# 완료 카드 아래 끝(766)과 탭 바(778) 사이 12px 틈에 밑의 한도 카드 글자 윗절반이 비치지 않게, 본문을 한도 카드 시작 위에서 자른다.
# 실제 글꼴 실측(2026-09-24 · 달력 카드 172 → 222): 달력 아래 끝 617.7 · 다음 안내 626.6 ~ 743.0 · 한도 카드 시작 752.0 · 탭 바 위 끝 778
# → 본문 아래 끝을 751 로(778 − 27). 다음 안내는 완료 카드(624 ~ 766) 밑에 가려지고, 틈(766 ~ 778)에는 장 바탕만 보인다.
# 한도 카드 · 순자산 카드는 HTML 에 그대로 둔다(기준표 5번 46,730원 · 103만원 · 47.6%). 달력 · 다음 안내 높이가 바뀌면 이 값을 다시 잴 것.
DONE_BODY_CUT = 27
w('DoneCard', frame(
    f'\n  {s1.header}\n\n'
    f'  <div style="flex: 1; min-height: 0; display: flex; flex-direction: column; gap: 9px; padding: 0 14px; margin-bottom: {DONE_BODY_CUT}px; overflow: hidden; position: relative;">\n\n'
    f'    {hero_after}\n\n    {calendar_after}\n\n    {s1.guide_block}\n\n    {limit_after}\n\n    {s1.networth_card}\n\n  </div>\n\n'
    f'  {bottomnav(0)}\n  {DONE_CARD}\n').replace('overflow: hidden; font-variant-numeric: tabular-nums;">', 'overflow: hidden; position: relative; font-variant-numeric: tabular-nums;">', 1))


# ══════════════ 5. 저장 직전 확인 · 반복 겹침 — 구현 참고 장 ══════════════
# 앱 화면이 아니다. 왼쪽에 실제 하루 기록 창을 두어 안내가 뜨는 자리를 보여 주고, 오른쪽에 네 경우를 2 × 2로 놓는다
# (견본을 카드 폭 362보다 좁히면 ②의 버튼 두 개가 넘친다). 수치·조건은 견본 설명이 아니라 맨 아래 구현 메모에 모은다.
def nowrap_btn(html):
    """안내 상자 안 버튼 — 낱말 중간에서 꺾이거나 눌리지 않게."""
    return html.replace('font-weight: 600;">', 'font-weight: 600; white-space: nowrap; flex-shrink: 0;">', 1)


def neutral_notice(inner):
    """하루 시트 안 안내 상자 — 달력 · 시트 · 완료 카드에는 의미색(주황 · 빨강 · 가정 보라)을 쓰지 않는다(계획 §5-1 · §11). 중립 표면 + 잉크."""
    return f'<div style="padding: 11px 12px; background: {C["INSET"]}; border-radius: 12px; display: flex; flex-direction: column; gap: 9px;">{inner}</div>'


def confirm_block(inner):
    return (f'<div style="background: {C["SURF"]}; border: 1px solid {C["LINE"]}; border-radius: 18px; padding: 14px; display: flex; flex-direction: column; gap: 10px;">{inner}</div>')


def save_chip(name):
    """큰 금액 안내의 고정비 칩 — 누르면 그 카테고리로 바로 저장(앱 `주거/관리로 저장`)."""
    return (f'<span style="display: inline-flex; align-items: center; gap: 6px; height: 32px; padding: 0 11px 0 9px; border-radius: 8px; '
            f'background: {C["SURF"]}; border: 1px solid {C["BORDER"]}; font-size: 12.5px; font-weight: 500; color: {C["INK"]}; white-space: nowrap;">'
            f'<span style="width: 8px; height: 8px; border-radius: 99px; background: {CAT[name]};"></span>{name}으로 저장</span>'.replace('관리으로', '관리로').replace('보험으로', '보험으로'))


fixed_chips = ''.join(save_chip(n) for n in ['주거/관리', '통신', '보험', '구독'])
assert '주거/관리로 저장' in fixed_chips and '통신으로 저장' in fixed_chips and '구독으로 저장' in fixed_chips
notice_fixed = neutral_notice(
    f'<span style="font-size: 13.5px; font-weight: 600; color: {C["INK"]};">매달 나가는 돈인가요? 고르면 바로 저장돼요</span>'
    f'<div style="display: flex; gap: 6px; flex-wrap: wrap;">{fixed_chips}</div>'
    f'<div style="display: flex; align-items: center; gap: 12px;"><span style="font-size: 12.5px; font-weight: 600; color: {C["BRAND"]};">저축·투자 &rsaquo;</span><span style="font-size: 12.5px; font-weight: 600; color: {C["BRAND"]};">대출상환 &rsaquo;</span></div>')


def confirm_save(label):
    return f'<div style="margin-top: 2px;">{btn(label, "primary", h=48, radius=14, size=15)}</div>'


block_fixed = confirm_block(amount_field('700,000', focused=False) + unsaved_line('70만원') + notice_fixed + confirm_save('카테고리 없이 저장'))
block_rule = confirm_block(
    amount_field('55,000', focused=False) + unsaved_line('5.5만원')
    + neutral_notice(
        f'<span style="font-size: 13px; line-height: 1.45; color: {C["INK"]};">이번 달 휴대폰 요금 55,000원은 <b style="font-weight: 600;">25일에 자동으로 기록돼요</b> · 방금 적은 게 휴대폰 요금인가요?</span>'
        f'<div style="display: flex; gap: 8px;">{nowrap_btn(smallbtn("다른 소비예요", "soft", h=34))}{nowrap_btn(smallbtn("휴대폰 요금 맞아요", "secondary", h=34))}</div>')
    + confirm_save('다른 소비로 저장'))
block_dup = confirm_block(
    amount_field('55,000', focused=False) + unsaved_line('5.5만원')
    + neutral_notice(
        f'<span style="font-size: 13px; line-height: 1.45; color: {C["INK"]};">같은 날 통신 55,000원(반복)이 <b style="font-weight: 600;">이미 있어요</b></span>'
        f'<div style="display: flex; gap: 8px;">{nowrap_btn(smallbtn("그래도 저장", "secondary", h=34))}{nowrap_btn(smallbtn("취소", "secondary", h=34))}</div>')
    + confirm_save('그래도 저장'))
block_fail = confirm_block(
    amount_field('12,000', focused=True)
    + unsaved_line('1.2만원', fail='저장하지 못했어요. 적은 내용은 그대로 있어요.')
    )
# 왼쪽 — DaySheet와 같은 창(머리줄 · 금액 · 읽기 줄 · 안내 · 메모 · 카테고리 · 최근 기록 · 저장)에 ①의 안내를 넣고 그 자리에 번호를 얹는다. 이체 링크 · 키보드 자리는 뺀다.
# 최근 기록 줄은 안내가 떠 있어도 앱처럼 카테고리와 저장 사이에 남는다(2026-09-27 fix-up 3).
confirm_sheet = (
    f'<div style="background: {C["SURF"]}; border: 1px solid {C["LINE"]}; border-radius: 26px 26px 18px 18px; overflow: hidden; display: flex; flex-direction: column;">'
    + sheet_header('9월 8일 소비 기록', '오늘 4건 37,000원')
    + f'<div style="padding: 12px 18px 18px; display: flex; flex-direction: column; gap: 10px;">'
    + amount_field('700,000', focused=False) + unsaved_line('70만원')
    + f'<div style="position: relative;">{notice_fixed}{mark(1, pos="position: absolute; top: -6px; right: -6px; flex-shrink: 0;")}</div>'
    + memo_field('월세') + category_row(None) + recent_row([recent_chip(*r) for r in RECENT], 18)
    + f'<div style="margin-top: 2px;">{save_btn("카테고리 없이 저장")}</div></div></div>')
confirm_left = (
    f'<div style="width: 362px; flex-shrink: 0; display: flex; flex-direction: column; gap: 8px;">{confirm_sheet}'
    f'<p style="margin: 2px 2px 0; font-size: 12px; line-height: 1.5; color: {C["INK3"]};">네 안내 모두 '
    f'<b style="font-weight: 600; color: {C["INK2"]};">금액 칸 바로 아래</b> 이 자리에 뜨고, 저장 버튼의 글이 그때의 기본 행동으로 바뀝니다. 그림은 1번의 경우입니다.</p></div>')
CONFIRM_CASES = [
    (1, '큰 금액을 적었을 때', '월급의 10%가 넘으면 매달 나가는 돈인지 물어봅니다. 칩을 누르면 그 카테고리로 바로 저장됩니다.', block_fixed),
    (2, '곧 자동으로 기록될 돈을 미리 적었을 때', '휴대폰 요금이 맞다고 하면 이번 달 자동 기록은 건너뜁니다.', block_rule),
    (3, '같은 날 같은 돈이 이미 있을 때', '알려만 주고 막지 않습니다.', block_dup),
    (4, '저장이 안 됐을 때', '창은 그대로 열려 있고 적은 값도 남아 있습니다.', block_fail)]
CONFIRM_MEMO = [
    (1, '적은 금액이 월급(실수령)의 10% 이상이고 카테고리를 고르지 않았을 때 뜹니다. 그림은 월급 360만원이라 36만원부터입니다. 카테고리를 이미 골랐으면 묻지 않아요 · '
        '저장을 한 번 더 누르면(「카테고리 없이 저장」) 카테고리 없이 저장되고, 예상 소비에는 적은 금액 그대로 더해집니다.'),
    (2, '메모가 반복 기록 이름과 같거나, 금액 차이가 5% 안이고 카테고리가 같을 때(카테고리도 메모도 비었으면 금액만 봅니다) · 아직 결제일 전일 때 뜹니다. '
        '「휴대폰 요금 맞아요」로 저장하면 완료 카드가 「이번 달 휴대폰 요금 자동 기록은 건너뛰어요 · 되돌리면 다시 생겨요」라고 알립니다.'),
    (3, '같은 날 자동으로 기록된 반복 기록이 이미 있을 때 뜹니다. 금액이 비슷하다는 이유만으로 지우거나 자동 기록을 건너뛰지 않습니다.'),
    (4, '안내는 금액 칸 아래에 그대로 남습니다. 저장 완료 카드는 뜨지 않습니다.')]


def memo_row(n, text, last=False):
    bb = '' if last else f' border-bottom: 1px solid {C["LINE_ROW"]};'
    return (f'<div style="display: flex; gap: 10px; padding: 7px 0;{bb}">{mark(n, pos="margin-top: 1px; flex-shrink: 0;")}'
            f'<div style="font-size: 12px; line-height: 1.55; color: {C["INK2"]};">{text}</div></div>')


CONFIRM_H = 1221      # 2026-09-27 fix-up 4 자연 1197 + 24(하루 시트 상자 모형) ·     # 자연 1195 + 24 — 최근 기록 줄을 더해도 오른쪽 견본 열이 더 길어 그대로(gen_canvas WIDE · screens.json 과 같게 · 2026-09-27 fix-up 3)
confirm_memo = (f'<div style="background: {C["SURF"]}; border: 1px solid {C["LINE"]}; border-radius: 18px; padding: 10px 18px 8px;">'
                f'<div style="font-size: 12px; font-weight: 700; color: {C["INK"]}; padding: 2px 0 4px;">구현 메모</div>'
                + ''.join(memo_row(n, t, last=(n == 4)) for n, t in CONFIRM_MEMO) + '</div>')
w('DaySheetConfirm', spec_frame(
    1200, CONFIRM_H, '저장을 눌렀는데 한 번 더 물어보는 경우',      # 2026-09-26 900 → 1219(칸 이름 위 · 읽기 줄 · 견본마다 기본 행동 저장 버튼 · 자연 1195 + 24)
    '아래 네 경우에는 바로 저장하지 않고 금액 칸 아래에 안내가 뜹니다. 저장 버튼의 글이 그때의 기본 행동(카테고리 없이 저장 · 다른 소비로 저장 · 그래도 저장)으로 바뀝니다.',
    f'<div style="display: flex; gap: 32px; align-items: flex-start;">{confirm_left}'
    f'{case_grid([(case_cap(n, t, d), blk) for n, t, d, blk in CONFIRM_CASES])}</div>{confirm_memo}', sub_w=760), keep_all=True)


# ══════════════ 6. 분류하기 시트 ══════════════
def check(on):
    if on:
        return f'<span style="width: 22px; height: 22px; border-radius: 7px; background: {C["BRAND"]}; display: inline-flex; align-items: center; justify-content: center; flex-shrink: 0;">{icon("check", 14, "#FFFFFF", 3)}</span>'
    return f'<span style="width: 22px; height: 22px; border-radius: 7px; background: {C["SURF"]}; border: 1.5px solid {C["INPUT"]}; flex-shrink: 0;"></span>'


def cls_chip(reco, chosen):
    """추천 칩 — 누르기 전 `● 기타 추천`(외곽선), 누른 뒤 `● 카페/간식`(brand-soft · brand 테두리)."""
    return (f'<span style="display: inline-flex; align-items: center; gap: 5px; height: 30px; padding: 0 10px; border-radius: 8px; '
            f'{"background: " + C["BRAND_SOFT"] + "; border: 1.5px solid " + C["BRAND"] + ";" if chosen else "background: " + C["SURF"] + "; border: 1px solid " + C["BORDER"] + ";"} '
            f'font-size: 12px; font-weight: 600; color: {C["INK"]}; white-space: nowrap; flex-shrink: 0;"><span style="width: 8px; height: 8px; border-radius: 99px; background: {CAT[reco]};"></span>{reco}'
            + ('' if chosen else f'<span style="font-size: 10.5px; font-weight: 500; color: {C["INK3"]};">추천</span>') + '</span>')


PICK = f'<span style="font-size: 12.5px; font-weight: 600; color: {C["BRAND"]}; white-space: nowrap; flex-shrink: 0;">카테고리 고르기 &rsaquo;</span>'


def cls_row(title, amount, reco=None, chosen=False, group=None, last=False, extra=''):
    """카테고리 고르기 시트의 한 묶음 — 앱 .classify-group(아래 선 · 마지막은 없음) 안에 .classify-row(최소 52 · 위아래 6) + extra(펼친 고르기 · 날짜별 줄).
    모든 줄에 `카테고리 고르기 ›`(추천 칩이 있어도). group = (건수, 펼침) 이면 묶음 줄(×N · ▲/▼).
    금액은 묶음 전체 합계(제외해도 그대로 — 바닥의 건수만 바뀐다 · DZ0 규칙). 이름 14 / 600 · 금액 12 ink-2(앱)."""
    bb = '' if last else f'border-bottom: 1px solid {C["LINE_ROW"]};'
    cnt = f' <span style="font-weight: 500; color: {C["INK3"]};">×{group[0]}</span>' if group else ''
    chev = (f'<span style="width: 28px; height: 28px; display: inline-flex; align-items: center; justify-content: center; flex-shrink: 0;">{icon("up" if group[1] else "down", 16, C["INK4"], 2)}</span>'
            if group else '')
    return (f'<div style="flex-shrink: 0; {bb}">'
            f'<div style="display: flex; align-items: center; gap: 10px; min-height: 52px; padding: 6px 0;">'
            f'<div style="display: flex; flex-direction: column; gap: 2px; flex: 1; min-width: 0;">'
            f'<span style="font-size: 14px; font-weight: 600; line-height: 19.6px; color: {C["INK"]}; white-space: nowrap;">{title}{cnt}</span>'
            f'<span style="font-size: 12px; line-height: 17.14px; color: {C["INK2"]};">{won(amount)}</span></div>'
            + (cls_chip(reco, chosen) if reco else '') + PICK + chev + '</div>' + extra + '</div>')


def no_memo_title(date_text):
    """메모 없는 기록은 묶지 않고 한 건씩 — 굵은 날짜 + 작은 회색 `메모 없음`."""
    return f'{date_text} <span style="font-size: 11px; font-weight: 500; color: {C["INK3"]};">메모 없음</span>'


def sub_row(date, amount, on, last=False):
    bb = '' if last else f'border-bottom: 1px solid {C["LINE_ROW"]};'
    return (f'<div style="display: flex; align-items: center; gap: 10px; height: 40px; padding-left: 8px; {bb}">{check(on)}'
            f'<span style="flex: 1; font-size: 13px; color: {C["INK2"]};">{date}</span>'
            f'<span style="font-size: 13px; font-weight: 600; color: {C["INK"] if on else C["INK3"]};">{won(amount)}</span></div>')


# 카테고리 없는 7건 = 내역 장 LedgerV5(gen_screens.LEDGER_V5)의 카테고리 없는 행과 같은 자료다 — 합 32,000원(히어로 각주 · EtcSubline · 한도 기타 줄과 같은 값).
# 줄 순서 = 최근 기록부터(앱 classify-sheet · DZ0 규칙): 9/8 편의점 · 9/5 버스 · 9/5 메모 없음 · 커피 ×3(9/5 · 9/4 · 9/1 — 묶음 안도 최근부터) · 9/3 간식.
# gen_screens 는 import 하면 장을 다시 쓰므로 글자로 둔다 — 그쪽 카테고리 없는 행이 바뀌면 여기도 맞춘다(아래 assert 가 건수 · 합계를 지킨다).
CLS_COFFEE = [(5, 4500, False), (4, 4500, True), (1, 4500, True)]            # (날짜, 금액, 고름) — 같은 메모 `커피` 묶음 · 5일은 `제외` 본보기
# 추천 = 앱 classifyGroups: 최근 30일 같은 메모의 확정 카테고리 중 최신. 캐논은 8월 14일 편의점 · 8월 26일 간식을 마감 뒤 기타로 골라서 둘 다 `기타 추천`,
# 커피는 9월 8일 커피(카페/간식)라 `카페/간식 추천`(하네스 2026-09-27 · NUMBERS §1). 예전 간식 `식비 추천`은 캐논에 없는 8월 28일 식비 간식(데모 기반 지도 자료)에서 나왔다.
CLS_SINGLE = [('편의점', 6500, '기타'), ('버스', 4500, None), ('', 3000, None), ('간식', 4500, '기타')]      # (메모 · 없으면 날짜 + `메모 없음`, 금액, 추천)
CLS_COUNT = len(CLS_COFFEE) + len(CLS_SINGLE)
CLS_PICKED = sum(1 for _, _, on in CLS_COFFEE if on)                         # 추천을 눌러 정한 것은 커피 묶음뿐(편의점 · 간식의 `기타 추천`은 아직 안 누름)
CLS_COFFEE_SUM = sum(a for _, a, _ in CLS_COFFEE)
assert CLS_COUNT == 7 and CLS_COFFEE_SUM + sum(a for _, a, _ in CLS_SINGLE) == 32_000 and CLS_COFFEE_SUM == 13_500      # `카테고리 없는 기록 7건` · 32,000원


def cls_head():
    """앱 .classify-sheet-header = 하루 시트 머리(위 20 · 아래 12 + 선 · 손잡이 8) — 제목 줄에 ‹ › 가 없어 제목 22 · 설명 두 줄은 3 아래."""
    return sheet_header(f'카테고리 고르기 · {CLS_COUNT}건', '같은 메모끼리 묶고, 메모 없는 기록은 한 건씩 보여요. 추천은 눌러야 정해지고, 정한 것만 저장돼요.',
                        today=True, arrows=False, chip='', weight=700).replace('white-space: nowrap;">카테고리 고르기', 'white-space: nowrap;">카테고리 고르기', 1)


def cls_foot(n, reason):
    """앱 .classify-sheet-footer — 위 선 · 12 18 20(+ 시트 아래 선 1) · 버튼과 까닭 줄 사이 8."""
    b = btn(f'{n}건 저장', 'primary' if n else 'disabled', h=52, radius=14, size=16)
    return (f'<div style="padding: 12px 18px 21px; border-top: 1px solid {C["LINE_SOFT"]}; flex-shrink: 0; display: flex; flex-direction: column; gap: 8px;">{b}'
            f'<p style="margin: 0; text-align: center; font-size: 11.5px; line-height: 17.25px; color: {C["INK3"]};">{reason}</p></div>')


def cls_body(picker=False):
    """picker=False = 커피 추천을 눌러 고르고 묶음을 펼쳐 9월 5일을 뺀 모습(2건 저장). picker=True = 버스 줄의 `카테고리 고르기 ›`를 누른 모습(새 장 · 아직 0건).
    본문 = 앱 .classify-sheet-body 6 18 20 · 묶음 사이 간격 없음(선으로 나눔)."""
    picker_block = ''
    if picker:      # 앱 .day-sheet-expanded — 위 8 · 아래 10 · 칩 사이 6(줄 바꿈) · 나눔 선(위아래 4) · 고정비 넷 · 안내 11
        var9 = [n for n in CAT if n not in ('저축/투자', '대출상환', '주거/관리', '통신', '보험', '구독')]
        picker_block = (f'<div style="display: flex; flex-wrap: wrap; gap: 6px; padding: 8px 0 10px;">{"".join(cat_chip(n) for n in var9)}'
                        f'<div style="flex-basis: 100%; height: 1px; background: {C["LINE"]}; margin: 4px 0;"></div>'
                        f'{"".join(cat_chip(n) for n in ("주거/관리", "통신", "보험", "구독"))}'
                        f'<span style="flex-basis: 100%; font-size: 11px; line-height: 16.5px; color: {C["INK3"]};">매달 나가는 돈이에요 · 실제 청구액으로 저장돼요</span></div>')
    rows = cls_row('편의점', 6500, '기타') + cls_row('버스', 4500, extra=picker_block)
    rows += cls_row(no_memo_title('9월 5일 토'), 3000)
    if picker:
        rows += cls_row('커피', CLS_COFFEE_SUM, '카페/간식', chosen=False, group=(3, False))
    else:
        subs = (f'<div style="background: {C["INSET"]}; border-radius: 0 0 12px 12px; padding: 0 10px 2px; margin-bottom: 2px;">'
                + ''.join(sub_row(f'9월 {d}일' + ('' if on else ' · 제외'), a, on, last=(i == len(CLS_COFFEE) - 1)) for i, (d, a, on) in enumerate(CLS_COFFEE))
                + '</div>')
        rows += cls_row('커피', CLS_COFFEE_SUM, '카페/간식', chosen=True, group=(3, True), extra=subs)
    rows += cls_row('간식', 4500, '기타', chosen=False, last=True)
    foot = (cls_foot(0, '카테고리를 골라 주세요 · 추천도 눌러야 정해져요') if picker
            else cls_foot(CLS_PICKED, f'나머지 {CLS_COUNT - CLS_PICKED}건은 카테고리 없음으로 남아요'))
    return (cls_head() + f'<div style="padding: 6px 18px 20px; display: flex; flex-direction: column;">'
            + rows + '</div>' + foot)


w('ClassifySheet', sheet_frame(cls_body(), scrim_text='배경을 눌러 닫기', fit=True), keep_all=True)
# 새 장 — 줄의 `카테고리 고르기 ›`를 누르면 그 줄 아래에 전체 고르기가 펼쳐진다(spending-3 #2 · 앱 classify-sheet). 아직 정한 것이 없어 회색 `0건 저장` + 까닭 줄(a11y-1).
w('ClassifySheetPicker', sheet_frame(cls_body(picker=True), scrim_text='배경을 눌러 닫기', fit=True), keep_all=True)


# ══════════════ 7. 히어로 이력 부족 — 홈 ══════════════
# 2026-09-24(13판): 이력 부족도 평소(A1)와 같은 틀이다 — 머리말 `현재 위치` · 큰 숫자 = 지금까지 쓴 돈 ÷ 월급 · 설명 줄 · 오른쪽 `목표까지 N%p 남음` ·
# 게이지 채움 · 순자산 대비는 A1 과 같은 규칙(쓴 돈 기준이라 예상 기준을 통과하지 않아도 보인다). 다른 점: 배지 없음 · 아래 칸 `월말 예상 —` · `월말 예상 여유 —` ·
# 설명 줄 바로 아래 각주 두 줄. 틀이 같아야 기록 부족 → 통과로 넘어가도 카드가 흔들리지 않으므로 Main 의 히어로를 잘라 값만 바꾼다(다시 그리지 않는다).
BADGE_RE = re.compile(r'\s*<span style="display: inline-flex; align-items: center; gap: 4px; background: #E4F4EA;.*?</span>', re.S)
HERO_RIGHT = '<span style="font-size: 14px; font-weight: 600; color: #101828; white-space: nowrap;">104만원 남음</span>'
HERO_CAPTION_ROW = '<div style="display: flex; align-items: baseline; justify-content: space-between; gap: 10px; margin-top: 5px;">'
TILE2 = '>208<span style="font-size: 13px; font-weight: 500; color: #475467;">만원</span></span>'
TILE3 = '>8<span style="font-size: 13px; font-weight: 500; color: #0F7B47;">만원</span></span>'
DASH = f'<span style="font-size: 18px; font-weight: 600; letter-spacing: -0.02em; color: {C["INK4"]};">—</span>'
FOOT_FIRST = '아직 기록하지 않은 소비는 포함되지 않았어요'           # 계획 §3-4 원문
FOOT_NO_HISTORY = '9월을 마감하면 10월부터 월말 예상을 보여 드려요'   # D9 · first-run-11 — 지난 기록이 하나도 없는 사람(링크 없음 · 앱 basisWhen)
for _m in (HERO_RIGHT, HERO_CAPTION_ROW, TILE2, TILE3, '>31.1</span>', '월급 360만원 중 112만원 썼어요', '>1.2%</span>', 'inset: 0 68.9% 0 0'):
    assert s1.hero_bare.count(_m) == 1, _m
assert len(BADGE_RE.findall(s1.hero_bare)) == 1


def foot_line(text):
    return f'<div style="font-size: 12px; line-height: 1.45; color: {C["INK3"]}; margin-top: 3px;">{text}</div>'


def hero_insufficient(second=FOOT_NO_HISTORY, big='0.1', caption='월급 360만원 중 5,000원 썼어요', gap='216만원 남음', burn='0.1% 미만', fill=0.1):
    """이력 부족 히어로(A2) — 기본값은 9월 5일에 처음 연 사람(오늘 커피 5,000원 한 건): 5,000 ÷ 3,600,000 = 0.14% → 0.1% · 목표까지 59.9%p 남음 ·
    순자산 대비 5,000 ÷ 9,350만 = 0.005% → `0.1% 미만`(0 < x < 0.05 · 0.0% 로 보이지 않게). 채움은 0.1%라 막대에는 거의 보이지 않는다."""
    h = BADGE_RE.sub('', s1.hero_bare, count=1)      # 캐논 각주(8월 · 32,000원 · 고정비)가 없는 히어로 — 이 사람의 각주는 아래에서 붙인다
    h = h.replace('>31.1</span>', f'>{big}</span>')
    h = h.replace(HERO_RIGHT, HERO_RIGHT.replace('104만원 남음', gap))
    h = h.replace('월급 360만원 중 112만원 썼어요', caption)
    h = h.replace('>1.2%</span>', f'>{burn}</span>')
    h = h.replace('inset: 0 68.9% 0 0', f'inset: 0 {100 - fill:.4g}% 0 0')
    # 아래 칸 둘 — 월말 예상 · 월말 예상 여유 = —(회색). 칸의 글자 span 을 통째로 바꾼다
    i2 = h.index(TILE2); j2 = h.rindex('<span style="font-size: 18px;', 0, i2)
    h = h[:j2] + DASH + h[i2 + len(TILE2):]
    i3 = h.index(TILE3); j3 = h.rindex('<span style="font-size: 18px;', 0, i3)
    h = h[:j3] + DASH + h[i3 + len(TILE3):]
    # 설명 줄 바로 아래 각주 두 줄
    c0 = h.index(HERO_CAPTION_ROW)
    depth, k = 0, c0
    for m in re.finditer(r'<div\b|</div>', h[c0:]):
        depth += 1 if m.group(0) == '<div' else -1
        if depth == 0:
            k = c0 + m.end(); break
    h = h[:k] + '\n      ' + foot_line(FOOT_FIRST) + foot_line(second) + h[k:]
    assert h.count('—</span>') == 2 and '월말에도 목표 안' not in h and h.count('<div') == h.count('</div>')
    return h


# 다음 안내(first-run-5 #2 · 앱 nextBestAction): 이 사람은 캐논 부채(카드 할부 14.5%)가 있어 늘 있는 안내 `카드 할부 금리 14.5%부터 줄여보세요`가 먼저 온다
# (앱 그대로 · 종 배지 중요 1 과 같은 까닭). 연 10% 이상 부채가 없는 사람은 빠진 날 안내 `어제 쓴 돈도 적어 볼까요?`(info) — InsufficientElsewhere ⑤ 에 둘 다 그린다.
# 예전 사실 카드(`기록한 소비 5,000원 · …`)는 앱에 없다.
GUIDE_TITLE = '투자 계좌 5,000만원에 매달 47만원이 더 필요해요'
assert s1.guide_block.count(GUIDE_TITLE) == 1 and s1.guide_block.count('목적지 보기 &rsaquo;') == 1
first_guide = (s1.guide_block.replace(GUIDE_TITLE, '카드 할부 금리 14.5%부터 줄여보세요')
               .replace('지금 매달 모으는 돈으로는 목표일에 닿기 어려워요. 목표일이나 순서를 바꿔 보세요.', '고금리 부채는 자산이 자라는 속도를 가장 크게 낮춰요.')
               .replace('목적지 보기 &rsaquo;', '상환 계획 보기 &rsaquo;'))
guide_missing_day = guidance('info', '다음 안내', '어제 쓴 돈도 적어 볼까요?', '빠진 날을 채울수록 이번 달 쓴 돈이 정확해져요.', '7일 적기')
# 달력 — 앱을 9월 5일에 처음 연 사람: 2~4일은 시작일 이전(— 없는 옅은 빈 칸), 5~7일은 회색 —, 오늘 칸 5,000. 확인할 내용 없음.
FIRST_SINCE = 5
NO_RECORD = ('—', False, False, False)
calendar_first = calendar_card(False, since=FIRST_SINCE, review=0, status='오늘 1건 5,000원',
                               states={5: NO_RECORD, 6: NO_RECORD, 7: NO_RECORD, TODAY: (fmt_sum(5_000), False, False, False)})
# 2026-09-26(DZ3 · home-18): 시작일(9/5) 전의 2 ~ 4일도 기록이 없으면 `—` + 범례 줄의 `—` 하나 = 3 + 3 + 1
assert calendar_first.count('>—<') == 7 and calendar_first.count('>5,000<') == 1 and '확인할 내용' not in calendar_first
# 한도 `오늘 포함 하루 93,700원`(D3 · NUMBERS §6) · 둘째 줄 `216만원 중 5,000원 썼어요`(home-3) · 달 중간에 시작한 사람은 남은 한도를 초록 대신 기본 글자색 +
# `9월 5일부터 기록 · 그 전 소비는 빠져 있어요`(tasks-1 · D3 · 앱 homeLimitView).
SINCE_LINE = '9월 5일부터 기록 · 그 전 소비는 빠져 있어요'
limit_first = s1.limit_block
for a, b in [('남은 한도 104만원', '남은 한도 216만원'), ('inset: 0 48.1% 0 0', 'inset: 0 99.8% 0 0'),
             ('오늘 포함 하루 45,220원', '오늘 포함 하루 93,700원'),
             ('216만원 중 112만원 썼어요</div>', f'216만원 중 5,000원 썼어요</div><div style="font-size: 12px; line-height: 1.45; color: {C["INK3"]}; margin-top: 2px;">{SINCE_LINE}</div>'),
             ('color: #0F7B47; white-space: nowrap; flex-shrink: 0;">남은 한도 216만원', f'color: {C["INK"]}; white-space: nowrap; flex-shrink: 0;">남은 한도 216만원')]:
    assert limit_first.count(a) == 1, a
    limit_first = limit_first.replace(a, b)
# 머리줄 종 배지 = 중요 알림 수(D14 · home-10) — 이 사람도 중요 1(카드 할부 금리 · 앱 1). 예전 2 는 옛 규칙.
header_first = s1.header
w('HeroInsufficient', frame(
    f'\n  {header_first}\n\n'
    f'  <div style="flex: 1; min-height: 0; display: flex; flex-direction: column; gap: 9px; padding: 0 14px; overflow: hidden;">\n\n'
    f'    {hero_insufficient()}\n\n    {calendar_first}\n\n    {first_guide}\n\n    {limit_first}\n\n  </div>\n\n'
    f'  {bottomnav(0)}\n'))


# ══════════════ 8. 홈 맨 위 카드에 붙는 작은 안내 줄 — 구현 참고 장 ══════════════
# 앱 화면이 아니다. 왼쪽에 온전한 카드 한 장(캐논 = 시안 사용자 9월 8일 · 안내 줄 두 줄)을 두어 안내 줄 자리를 표시하고, 오른쪽에는 카드의 아랫부분
# (월급 · 부수입 고치기 줄 + 안내 줄)만 다섯 경우로 놓는다. 안내 줄은 카드의 마지막 줄들이다(앱 hero-notes · 11px · 줄 사이 10).
HERO_BASIS = '<div style="display: flex; align-items: center; justify-content: space-between; gap: 10px; margin-top: 12px;">'
assert s1.hero_bare.count(HERO_BASIS) == 1 and '소비 기록하기' not in s1.hero_bare and s1.hero_bare.endswith('</div>')
hero_top = s1.hero_bare[:s1.hero_bare.index(HERO_BASIS)]                        # 카드 여는 태그 ~ 세 칸 요약(캐논 각주 없는 히어로)
_tail = s1.hero_bare[s1.hero_bare.index(HERO_BASIS):]
hero_tail = _tail[:_tail.rstrip().rindex('</div>')].rstrip()                     # 월급 · 부수입 고치기 줄(카드 닫는 태그 앞까지)
assert '월급 · 부수입 고치기' in hero_tail
NOTE_STYLE = f'font-size: 11px; line-height: 1.4; color: {C["INK3"]};'
LINKY = f'<span style="font-weight: 600; color: {C["BRAND"]}; white-space: nowrap;">%s &rsaquo;</span>'


def hero_tail_with(notes, marked=False):
    """월급 · 부수입 고치기 줄 아래에 안내 줄을 붙인다(앱처럼 줄마다 위 10). marked = 안내 줄 자리를 옅은 파란 테두리와 알약으로 표시(왼쪽 온전한 카드용)."""
    lines = ''.join(f'<p style="{NOTE_STYLE} margin: {10 if i else 0}px 0 0;">{n}</p>' for i, n in enumerate(notes))
    if marked:
        pill = (f'<span style="position: absolute; bottom: -9px; right: 4px; height: 17px; padding: 0 7px; border-radius: 99px; '
                f'background: {C["INK"]}; color: #FFFFFF; font-size: 10.5px; font-weight: 700; display: inline-flex; align-items: center; white-space: nowrap;">안내 줄</span>')
        # 2026-09-27 fix-up 2: 테두리 안쪽 여백(6 · 8 · 아래 12) — 글이 테두리에 닿지 않고 알약은 둘째 줄 아래 여백 위에 걸친다(겉 여백 −8 로 글 자리는 그대로)
        return hero_tail + (f'<div style="position: relative; margin: 4px -8px 0; padding: 6px 8px 12px; border-radius: 8px; box-shadow: 0 0 0 3px rgba(53,86,230,.16);">{lines}{pill}</div>')
    return hero_tail + (f'<div style="margin-top: 10px;">{lines}</div>' if notes else '')


def hero_fragment(notes):
    """카드의 아랫부분만 — 위 테두리 없이 아래 모서리만 둥글게 해서 잘라 낸 조각으로 보이게."""
    return (f'<div style="background: {C["SURF"]}; border: 1px solid {C["LINE"]}; border-top: none; border-radius: 0 0 20px 20px; padding: 4px 16px 16px; '
            f'box-shadow: 0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24);">{hero_tail_with(notes)}</div>')


NOTE_R = '8월에 새 기록이 있어요 · ' + LINKY % '8월 합계 고치기'                    # D9 · record-1 — 마감한 달의 기록이 마감 뒤 바뀌었을 때(링크 줄)
NOTE_R2 = '지난 기록에 새 기록이 있어요 · ' + LINKY % '합계 고치기'
NOTE_A = '카테고리 없는 32,000원은 적은 금액 그대로 예상에 더했어요'
NOTE_B = '카테고리 없는 지난 기록도 평균에 넣었어요. 카테고리를 고르면 다시 계산해요.'
NOTE_C = '지난 고정비 기록을 보고 앞으로 나갈 돈도 예상했어요'
NOTE_D = '기록이 한 달치뿐이라 예상이 달라질 수 있어요'
# 시안 사용자 9월 8일(홈 장 전부 · Main hero-notes)과 같다 — 2026-09-27 fix-up: 두 줄(8월 마감값 = 기록 합이라 합계 고치기 줄 없음 · 8월 카테고리 없는 3건은
# 마감 뒤 기타로 골라 「지난 기록도」 줄 없음 · 앱 하네스 W/design-state.json).
CANON_NOTES = [NOTE_A, NOTE_C]
assert s1.hero_block.count(NOTE_A) == 1 and s1.hero_block.count(NOTE_C) == 1 and '8월 합계 고치기' not in s1.hero_block and NOTE_B not in s1.hero_block
FOOTNOTE_CASES = [
    (1, '덧붙일 말이 없을 때', '월급 · 부수입 고치기 줄로 카드가 끝납니다.', []),
    (2, '마감한 달에 새 기록이 있을 때', '첫 줄은 링크 줄입니다. 배지 · 월말 예상 · 여유는 그대로입니다. 두 달 이상이면 「지난 기록에 새 기록이 있어요 · 합계 고치기 ›」.', [NOTE_R]),
    (3, '이번 달에 카테고리 없는 기록이 있을 때', '안내가 한 줄 붙습니다.', [NOTE_A]),
    (4, '지난달 기록으로 예상을 계산한 날', '카테고리 없는 지난 기록이 평균에 들어갔거나 고정비를 지난 기록으로 예상했을 때. 이번 달 기록만으로 계산한 날에는 나오지 않습니다.', [NOTE_B, NOTE_C]),
    (5, '기록이 한 달치뿐일 때', '안내가 한 줄 붙습니다.', [NOTE_D])]
footnote_left = (
    f'<div style="width: 362px; flex-shrink: 0; display: flex; flex-direction: column; gap: 8px;">{hero_top}{hero_tail_with(CANON_NOTES, marked=True)}</div>'
    f'<p style="margin: 2px 2px 0; font-size: 12px; line-height: 1.5; color: {C["INK3"]};">안내 줄은 '
    f'<b style="font-weight: 600; color: {C["INK2"]};">월급 · 부수입 고치기 줄 아래, 카드의 맨 끝</b>에 붙습니다. 그림은 홈 장들과 같은 9월 8일 — 3번 줄과 4번의 고정비 줄이 함께 나온 날입니다(마감한 8월에 새 기록이 없어 2번 줄은 없어요).</p>'
    f'<p style="margin: 0 2px; font-size: 12px; line-height: 1.5; color: {C["INK3"]};">순서는 늘 합계 고치기 줄 → 카테고리 없는 이번 달 금액 → 카테고리 없는 지난 기록 → 고정비 이력 → 한 달치뿐입니다.</p></div>')
footnote_foot = (f'<p style="margin: 10px 2px 0; font-size: 12px; line-height: 1.6; color: {C["INK3"]}; max-width: 900px;">오른쪽 견본은 카드의 '
                 f'<b style="font-weight: 600; color: {C["INK2"]};">아랫부분</b>만 잘라 보여 줍니다. 카드의 나머지는 모든 경우에 같고, 안내 줄이 붙은 만큼만 카드가 길어집니다. '
                 f'합계 고치기 줄을 누르면 마감 창이 아니라 한 단계 확인 「8월 소비 합계만 새 금액으로 고칠게요」가 바로 열립니다(확인 창 G).</p>')
HF_H = 800      # 자연 높이 776 + 24(다섯 경우 · 2026-09-26)
w('HeroFootnotes', spec_frame(
    1200, HF_H, '홈 맨 위 카드에 붙는 작은 안내 줄',
    '월말 예상을 계산한 방식에 덧붙일 말이 있을 때만 월급 · 부수입 고치기 줄 아래에 회색 글이 한두 줄 붙습니다.',
    f'<div style="display: flex; gap: 32px; align-items: flex-start;">{footnote_left}'
    f'{case_grid([(case_cap(n, t, d), hero_fragment(notes)) for n, t, d, notes in FOOTNOTE_CASES])}</div>{footnote_foot}', sub_w=760), keep_all=True)


# ══════════════ 8-2. 홈 맨 위 카드 — 소비 목표를 넘을 때(구현 참고 장 · 2026-09-27 fix-up 2) ══════════════
# 앱 a724aac 하네스(W/design-state.json + 한 가지씩 바꿈 · shots/verify2/app/home-page/hero-target50 · hero-over · hero-equal) 그대로 · NUMBERS §2.
# D4: 배지는 세 가지 그대로(월말에도 목표 안 · 월말엔 목표 초과 · 월말엔 월급 초과) · 오른쪽 줄은 돈 — 「소비 목표까지 / N 남음」 · 「소비 목표에 / 딱 닿았어요」 ·
# 「소비 목표보다 / N 넘음」(주황) · 셋째 칸은 월말 예상이 목표를 넘으면 「월말 예상 초과」(빨강). 큰 숫자 · 게이지 = 지금까지 쓴 돈 ÷ 월급.
HERO_BADGE_OVER = ('<span style="display: inline-flex; align-items: center; gap: 4px; background: #FDF1E0; color: #B45309; font-size: 11.5px; font-weight: 600; '
                   'border-radius: 99px; padding: 4px 9px; white-space: nowrap;">월말엔 목표 초과</span>')
HERO_RIGHT_LABEL = '<span style="font-size: 11px; font-weight: 500; color: #626D88; white-space: nowrap;">소비 목표까지</span>'
TICK60 = '<div style="position: absolute; left: 60%; top: -5px;'
TICK60_LABEL = '<span style="position: absolute; left: 60%; transform: translateX(-50%); font-size: 11px; font-weight: 600; color: #101828; white-space: nowrap;">소비 목표 60%</span>'
TILE3_LABEL = '<span style="font-size: 11.5px; font-weight: 500; color: #626D88; white-space: nowrap;">월말 예상 여유</span>'
TILE3_OVER = '<span style="font-size: 18px; font-weight: 600; letter-spacing: -0.02em; color: #0F7B47;">8<span style="font-size: 13px; font-weight: 500; color: #0F7B47;">만원</span></span>'
for _m in (HERO_RIGHT_LABEL, TICK60, TICK60_LABEL, TILE3_LABEL, TILE3_OVER):
    assert s1.hero_block.count(_m) == 1, _m


def hero_over(big, right_label, right_text, right_color, caption, burn, fill, tick, tile2, tile3):
    """캐논 히어로(각주 두 줄 그대로)에서 값만 바꾼다 — 배지 「월말엔 목표 초과」 · 셋째 칸 「월말 예상 초과」 빨강."""
    h = BADGE_RE.sub('\n          ' + HERO_BADGE_OVER, s1.hero_block, count=1)
    h = h.replace('>31.1</span>', f'>{big}</span>')
    h = h.replace(HERO_RIGHT_LABEL, HERO_RIGHT_LABEL.replace('소비 목표까지', right_label))
    h = h.replace(HERO_RIGHT, HERO_RIGHT.replace('color: #101828;', f'color: {right_color};').replace('104만원 남음', right_text))
    h = h.replace('월급 360만원 중 112만원 썼어요', caption)
    h = h.replace('>1.2%</span>', f'>{burn}</span>')
    h = h.replace('inset: 0 68.9% 0 0', f'inset: 0 {round(100 - fill, 1):g}% 0 0')
    h = h.replace(TICK60, TICK60.replace('60%', f'{tick}%')).replace(TICK60_LABEL, TICK60_LABEL.replace('60%', f'{tick}%'))
    h = h.replace(TILE2, TILE2.replace('>208<', f'>{tile2}<'))
    h = h.replace(TILE3_LABEL, TILE3_LABEL.replace('월말 예상 여유', '월말 예상 초과'))
    h = h.replace(TILE3_OVER, f'<span style="font-size: 18px; font-weight: 600; letter-spacing: -0.02em; color: {C["NEG"]};">{tile3}'
                              f'<span style="font-size: 13px; font-weight: 500; color: {C["NEG"]};">만원</span></span>')
    assert h.count('월말엔 목표 초과') == 1 and '월말에도 목표 안' not in h and h.count('월말 예상 초과') == 1 and h.count('<div') == h.count('</div>')
    assert h.count(NOTE_A) == 1 and h.count(NOTE_C) == 1
    return h


OVER_CASES = [
    (1, '소비 목표를 50%로 낮춰 저장한 뒤',
     '소비 목표 조정(HomeTargetEditor)에서 50%로 저장하면 선 · 오른쪽 줄 · 배지 · 셋째 칸이 새 소비 목표 180만원으로 바로 바뀝니다. 쓴 돈 31.1%와 월말 예상 208만원은 그대로입니다. '
     '같은 순간 아래 알림 「소비 목표 50%로 저장했어요 · 한도 180만원」 + 되돌리기가 뜨고 종 배지(1 → 3) · 다음 안내 · 한도 카드도 함께 바뀝니다(홈 페이지 HomeTargetSaved).',
     hero_over('31.1', '소비 목표까지', '68만원 남음', C['INK'], '월급 360만원 중 112만원 썼어요', '1.2%', 31.1, 50, '208', '28')),
    (2, '쓴 돈이 소비 목표를 넘었을 때',
     '이번 달 쓴 돈이 219만원(소비 목표 216만원 + 32,000원)이 된 날. 오른쪽 줄은 「소비 목표보다 3만원 넘음」 주황, 이번 달 한도 카드는 「3만원 넘음」 빨강(LimitCardCases).',
     hero_over('60.9', '소비 목표보다', '3만원 넘음', C['WARN'], '월급 360만원 중 219만원 썼어요', '2.3%', 60.9, 60, '316', '100')),
    (3, '소비 목표에 딱 닿았을 때',
     '쓴 돈이 216만원 = 소비 목표인 날. 오른쪽 줄 「소비 목표에 딱 닿았어요」 주황 · 한도 카드는 「남은 한도 0원」 · 「오늘 포함 하루 0원」.',
     hero_over('60.0', '소비 목표에', '딱 닿았어요', C['WARN'], '월급 360만원 중 216만원 썼어요', '2.3%', 60.0, 60, '312', '96'))]
over_foot = (f'<p style="margin: 14px 2px 0; font-size: 12px; line-height: 1.6; color: {C["INK3"]}; max-width: 1100px;">'
             f'배지는 월말 예상으로만 판정합니다 — 월말 예상 ≤ 소비 목표면 「월말에도 목표 안」(초록 · 시안 사용자 홈), 넘으면 「월말엔 목표 초과」(주황), 월급마저 넘으면 「월말엔 월급 초과」(빨강 · Components 02). '
             f'오른쪽 줄은 지금까지 쓴 돈과 소비 목표의 차이를 돈으로 말하고, 넘거나 딱 닿으면 주황 글자입니다. 셋째 칸은 월말 예상이 소비 목표 안이면 「월말 예상 여유」 초록, 넘으면 「월말 예상 초과」 빨강입니다. '
             f'직접 정한 한도가 있어도 이 카드는 늘 월급 × 소비 목표 %로 판단합니다 — 「한도」라는 이름이 붙은 곳만 직접 정한 한도를 씁니다.</p>')
OVER_H = 765      # 자연 741 + 24(2026-09-27 fix-up 5 — 실제 웹폰트로 다시 재니 729 에서 12px 잘려 있었다 · 예전 자연 705) — gen_canvas WIDE · screens.json 과 같아야 한다
w('HeroOverTarget', spec_frame(
    1230, OVER_H, '홈 맨 위 카드 · 소비 목표를 넘을 때',
    '같은 시안 사용자(9월 8일 · 각주 두 줄)에서 소비 목표나 쓴 돈만 바꾼 세 경우입니다. 카드의 틀은 그대로이고 글과 색만 바뀝니다.',
    f'<div style="display: grid; grid-template-columns: repeat(3, 362px); gap: 24px 28px; align-items: start;">'
    + ''.join(f'<div style="display: flex; flex-direction: column; gap: 8px; min-width: 0;">{case_cap(n, t, d)}{h}</div>' for n, t, d, h in OVER_CASES)
    + f'</div>{over_foot}', sub_w=760), keep_all=True)


# ══════════════ 9. 홈 달력 — 접힘(최근 7일 스트립) · 펼침(월 달력) · 칸 상태 · 폭/글자 크기 ══════════════
# 펼침은 어느 폭·어느 글자 크기에서도 **월 달력(7열 그리드)** 이다 — 날짜를 세로로 늘어놓은 목록으로 자동 대체하지 않는다(7판).
# 2026년 9월: 1일 화요일 · 30일 · 5주. 오늘 8일(화). 2026년 8월: 1일 토요일 · 31일 · 6주.
# 칸 숫자 = 그날 소비 합계(고정비 포함 · 이체 제외). 표기는 앱 formatSum과 같다(1만 미만 원 단위 · 1만 이상 만 단위 한 자리 · 소수 첫 자리 0은 뗀다).
# 자료 · 칸 · 접힘/펼침 카드 · 상태 줄은 gen_calendar.py 로 옮겼다(gen_v4 · gen_v4_stocks 도 쓰도록). 여기는 홈에 얹는 틀과 장만 남는다.


def limit_card(forward=False, two_lines=False):
    """홈 한도 카드 = Main 의 한도 카드 그대로(2026-09-26 · DZ3 호환). 단계 라벨 `하루 …` · `앞으로 하루 …`는 없어졌다 —
    늘 `오늘 포함 하루 45,220원` + 둘째 줄 `216만원 중 112만원 썼어요`, 좁으면 `남은 한도`가 둘째 줄 오른쪽으로(앱 flex-wrap).
    forward · two_lines 인수는 옛 호출 호환용(무시)."""
    html = s1.limit_block
    assert html.count('오늘 포함 하루 45,220원') == 1 and '앞으로 하루' not in html and html.count('216만원 중 112만원 썼어요') == 1
    return html


def limit_forward(two_lines=False):
    """LimitCardCases(gen_v5_screens)가 쓰는 평소 한도 카드 — 이제 1 · 2단계와 같은 카드(라벨 `오늘 포함 하루`)."""
    return limit_card(True, two_lines)


def limit_stage12():
    """홈의 한도 카드(HomeCalendarStrip · HomeDefaultScroll · 펼침 · InsufficientElsewhere 와 같다)."""
    return limit_card(False)


def home_expanded(width=390, pad=14, month='sep', pressed=None, limit=True):
    peek = f'<div style="height: 22px; background: {C["SURF"]}; border: 1px solid {C["LINE"]}; border-top: none; border-radius: 0 0 20px 20px; flex-shrink: 0; opacity: .55;"></div>'
    lim = ('\n\n    ' + limit_stage12()) if limit else ''
    return frame(
        f'\n  <div style="flex: 1; min-height: 0; display: flex; flex-direction: column; gap: 9px; padding: 0 14px; overflow: hidden;">\n\n'
        f'    {peek}\n\n    {calendar_card(True, pressed=pressed, pad=pad, month=month)}\n\n    {s1.guide_block}{lim}\n\n  </div>\n\n'
        f'  {bottomnav(0)}\n', w=width)


# 홈 구성에서 켜는 카드 두 장은 v3 시안에서 그대로 잘라 온다 — 대표 목적지(Main) · 또래와 내 페이스(HomeScroll). 기본 홈(HomeCalendarStrip · HomeDefaultScroll)에는 없다.
goal_block = s1.cut(s1.main_src, s1.M_GOAL, s1.M_LIMIT).rstrip()
assert goal_block.count('대표 목적지') == 1 and goal_block.count('<div') == goal_block.count('</div>')
_scroll_src = (OUT / 'HomeScroll.dc.html').read_text(encoding='utf-8')
P_PEER = '<div style="background: #FFFFFF; border: 1px solid #E3E8F1; border-radius: 18px; padding: 14px; flex-shrink: 0;">'
P_ROWS = '<div style="background: #FFFFFF; border: 1px solid #E3E8F1; border-radius: 18px; padding: 4px 14px; flex-shrink: 0;">'
assert _scroll_src.count(P_PEER) == 1 and _scroll_src.count(P_ROWS) == 1
peer_block = s1.cut(_scroll_src, P_PEER, P_ROWS).rstrip()
assert peer_block.count('또래와 내 페이스') == 1 and peer_block.count('<div') == peer_block.count('</div>') and '순자산 대비 월말 예상' not in peer_block
assert peer_block.count('내 월말 예상') == 1 and '내 소비율' not in peer_block      # 또래 카드는 월말 예상으로 비교(2026-09-24 이름)

# 홈 · 접힘 — 히어로 그대로, 첫 카드가 달력(최근 7일). 그 아래로 다음 안내 · 이번 달 한도 · 순자산 한 줄 · 상환 계획 한 줄이 이어진다(앱 DEFAULT_HOME_CARDS ·
# 화면 아래에서 잘림 · HomeDefaultScroll 과 같은 순서 — 2026-09-27 fix-up 2: 예전 대표 목적지는 기본 카드가 아니다).
w('HomeCalendarStrip', frame(
    f'\n  {s1.header}\n\n'
    f'  <div style="flex: 1; min-height: 0; display: flex; flex-direction: column; gap: 9px; padding: 0 14px; overflow: hidden;">\n\n'
    f'    {s1.hero_block}\n\n    {calendar_card(False)}\n\n    {s1.guide_block}\n\n    {limit_stage12()}\n\n    {s1.networth_card}\n\n    {s1.payoff_card}\n\n  </div>\n\n'
    f'  {bottomnav(0)}\n'))

# 홈 · 기본 카드 전체 스크롤 — 앱 DEFAULT_HOME_CARDS(홈 구성을 저장하지 않은 사람): 히어로 · 달력(고정) · 다음 안내 · 이번 달 한도 · 순자산 한 줄 · 상환 계획 한 줄.
# 대표 목적지 · 또래는 기본이 아니다(goals-14 · first-run-14). 스크롤 전체 길이를 한 장에(앱 문서 높이 1241 · 390 · 캐논 각주 두 줄).
HOME_DEFAULT_H = 1241      # 자연 높이 1217 + 24 — gen_canvas TALL · screens.json 과 같아야 한다(2026-09-27 fix-up · 캐논 각주 두 줄)
w('HomeDefaultScroll', frame(
    f'\n  {s1.header}\n\n'
    f'  <div style="flex: 1; min-height: 0; display: flex; flex-direction: column; gap: 10px; padding: 0 14px 14px; overflow: hidden;">\n\n'
    f'    {s1.hero_block}\n\n    {calendar_card(False)}\n\n    {s1.guide_block}\n\n    {limit_stage12()}\n\n    {s1.networth_card}\n\n    {s1.payoff_card}\n\n  </div>\n\n'
    f'  {bottomnav(0)}\n', h=HOME_DEFAULT_H))

# 홈 · 펼침 — 월 달력. 아래로 조금 스크롤한 상태(히어로 아랫단이 위에 남음). 날짜 칸을 누르면 → 다음 장 하루 시트.
# 2026-09-24 최종 점검 후속 — 3일 칸 누름(2px 링)을 그리지 않는다. 오늘 칸도 1.5px 링이라 정지 그림에서 둘째 오늘처럼 읽혔다.
# 누름 모양은 SPEC-COMPONENTS §27-1 표(inset 2px)와 CalendarCells 끝 문단 · Components 08 설명 1 에 글로 남는다.
w('HomeCalendar', home_expanded())
# 같은 화면 360px — 가장 흔한 안드로이드 폭. 카드 좌우 패딩 10, 칸 폭 44.6. 목록으로 바뀌지 않는다.
w('HomeCalendar360', home_expanded(width=360, pad=10))
# ‹ 로 지난달(8월)을 보는 상태 — 6주. › 와 `이번 달로`가 살아나고, 칸을 누르면 그 날짜 하루 시트.
# 아래는 HomeCalendar 와 같이 다음 안내 → 이번 달 한도(맨 윗부분이 탭 막대 위에 보임 · 앱 같은 스크롤 · 2026-09-27 fix-up).
w('HomeCalendarPrev', home_expanded(month='aug'))


# ══════════════ 10. 구현 참고 장 — 달력 칸 읽는 법 · 폭과 글자 크기 ══════════════
# 앱 화면이 아니라 구현하는 사람이 보는 설명 장이다. 폰 프레임을 쓰지 않고 가로로 넓게 펴서, 실제 달력 옆에 짧은 설명을 둔다.
# 틀(mark · spec_frame)은 위 조각 구역에 있다. 맨 위 알약 `구현 참고 · 앱 화면이 아닙니다`로 앱 화면과 구분한다. 설명은 "무엇을 뜻하는지" 한 줄 + "누르면 어떻게 되는지(또는 알아 둘 점)" 한 줄.
# 달력 위에 찍는 번호: (자료가 속한 달, 날짜) → 번호
MARKS = {('sep', 7): 1, ('sep', 3): 2, ('sep', 4): 3, ('sep', 6): 4, ('sep', 8): 5, ('sep', 12): 6, ('aug', 31): 7, ('oct', 2): 8}
CELL_GUIDE = [   # (번호, 이름, 무엇을 뜻하는지, 누르면 어떻게 되는지 또는 알아 둘 점)
    (1, '—', '아직 기록이 없는 날', '누르면 그 날짜 기록 창이 열려요'),
    (2, '금액', '그날 쓴 돈의 합계 · 쓰는 법은 오른쪽 표에 있어요', '누르면 그날 기록 목록이 먼저 보여요'),
    (3, '금액 아래 ✓', '다 적었어요로 표시한 날', '그날 기록을 고치면 ✓가 풀려요'),
    (4, '0', '안 쓴 날이라고 표시한 날', ('이체', '저축·대출상환이 있던 날 · 소비 합계에는 넣지 않아요')),      # 한 번호 안에서 같은 굵기의 두 줄
    (5, '오늘', '옅은 파란 칸 · 파란 테두리 · 굵은 날짜 · 아직 안 적었으면 — 대신 파란 +', '누르면 금액 입력부터 시작해요 · 카드 아래 적기 버튼 · 알약과 같은 곳'),
    (6, '아직 오지 않은 날', '날짜만 옅게 보여요', '눌러도 열리지 않고, 오늘 합계 자리에 3초 동안 「아직 오지 않은 날은 적을 수 없어요」가 떠요'),
    (7, '지난달 날짜', '첫 주의 8월 30·31일 · 기록이 옅게 보여요', '누르면 그 날짜 기록 창이 열려요'),
    (8, '다음 달 날짜', '10월 1~3일 · 아직 오지 않은 날은 날짜만 옅게', '누를 수 없어요 · 이미 지난 날이면 7번처럼 기록이 옅게 보여요'),
    (9, '시작일 전 날', '앱을 쓰기 시작한 날보다 앞선 날도 기록이 없으면 —', '따로 모양을 두지 않아요 · 누르면 그 날짜 기록 창이 열려요'),      # home-18 · D7 — 예전 `빈 칸`(날짜만 옅게)은 없앴다
]


def marked_calendar():
    """HomeCalendar와 같은 9월 달력 — 설명할 칸에 번호만 얹는다."""
    wd = ''.join(f'<span style="text-align: center; font-size: 11px; font-weight: 500; color: {C["INK3"]};">{d}</span>' for d in WD)
    rows = []
    for wk in WEEKS['sep']:
        cs = []
        for kind, d, m in wk:
            is_sep = m == 'sep'
            c_ = gcell(d, month=m if m in MONTHS else 'sep', kind=kind,
                       today=(is_sep and d == TODAY and kind != 'out'), future=(is_sep and d > TODAY))      # 오늘 칸 테두리 · + 규칙은 gcell 이 그린다
            n = MARKS.get((m, d))
            cs.append(f'<div style="position: relative; min-width: 0;">{c_}{mark(n, True) if n else ""}</div>')
        rows.append(f'<div style="display: grid; grid-template-columns: repeat(7, minmax(0, 1fr)); border-top: 1px solid {C["LINE_SOFT"]}; padding: 2px 0;">{"".join(cs)}</div>')
    grid = (f'<div style="display: grid; grid-template-columns: repeat(7, minmax(0, 1fr)); margin-top: 8px; padding-bottom: 5px;">{wd}</div>'
            f'<div style="display: flex; flex-direction: column; border-bottom: 1px solid {C["LINE_SOFT"]};">{"".join(rows)}</div>')
    return card(month_bar('2026년 9월', prev_on=True, next_on=False) + hint(mt=6) + grid + legend()
                + status_line(f'9월 기록한 소비 {SEP_TOTAL:,}원') + today_tail(day_state('sep', TODAY), TODAY_TEXT, mt=8)
                + review_row(REVIEW_UNCAT), pad='13px 14px 13px')      # 캐논 = 항목 하나의 이름(2026-09-27 fix-up)


def guide_row(n, name, meaning, tap, last=False):
    """tap 이 (이름, 뜻) 짝이면 둘째 줄도 첫 줄과 같은 굵기의 제목 줄로 쓴다(④의 0 / 이체)."""
    border = '' if last else f'border-bottom: 1px solid {C["LINE_ROW"]};'
    if isinstance(tap, tuple):
        second = (f'<div style="font-size: 13.5px; line-height: 1.4; color: {C["INK2"]};"><b style="font-weight: 600; color: {C["INK"]};">{tap[0]}</b>&nbsp;&nbsp;{tap[1]}</div>')
    else:
        second = f'<div style="font-size: 12px; line-height: 1.4; color: {C["INK3"]};">{tap}</div>'
    return (f'<div style="display: flex; gap: 11px; padding: 10px 0; {border}">{mark(n)}'
            f'<div style="display: flex; flex-direction: column; gap: 2px; min-width: 0;">'
            f'<div style="font-size: 13.5px; line-height: 1.4; color: {C["INK2"]};"><b style="font-weight: 600; color: {C["INK"]};">{name}</b>&nbsp;&nbsp;{meaning}</div>'
            f'{second}</div></div>')


cell_guide = card(''.join(guide_row(*r, last=(i == len(CELL_GUIDE) - 1)) for i, r in enumerate(CELL_GUIDE)), pad='4px 16px')
cell_foot = (f'<p style="margin: 10px 2px 0; font-size: 12px; line-height: 1.6; color: {C["INK3"]};">'
             f'접힌 최근 7일 줄에는 달 제목이 없어서 지난달 날짜를 <b style="font-weight: 600; color: {C["INK2"]};">8/31</b>처럼 달을 붙여 씁니다. '
             f'6일 칸은 안 쓴 날로 표시했고 이체도 있어서 0과 이체가 같이 보입니다. 표시 없이 이체만 있는 날은 숫자 없이 이체만 보입니다. '
             f'오늘 칸의 가는 파란 테두리(1.5px)는 늘 있고, 칸을 누르는 순간에는 더 굵은 테두리(2px)가 생깁니다(그림에는 그리지 않음 · SPEC-COMPONENTS §27-1). 오늘 칸의 +가 금액으로 바뀌어도 칸 크기는 같습니다. '
             f'칸 아래 범례 줄 「— 기록 없음 · 0 안 썼어요 · ✓ 다 적었어요」는 접힘 · 펼침 · 목록 어디서나 늘 있어서 저장 전후 카드 높이가 같습니다.</p>')

# 9번(시작일 전 날)은 왼쪽 9월 달력에 없는 상태라(그 사람은 8월에도 기록이 있다) 다른 사람의 접힌 줄을 따로 보여 준다 — HeroInsufficient 와 같은 달력.
# 2026-09-26(home-18): 시작일 전 날도 기록이 없으면 — (따로 옅은 빈 칸을 두지 않는다).
# 번호 자리: 카드 안쪽 332를 7칸(44)이 space-between 으로 나눠 칸 간격 4 → 3일 칸(둘째)의 오른쪽 끝 = 1 + 14 + 48 + 44 = 107.
# 세로: 제목 줄 아래 안내 한 줄(2 + 17.4)과 칸 위 간격 10(전 8)이 생겨 칸이 21px 내려갔다(2026-09-24) — 38 → 59.
since_strip = (f'<div style="position: relative;">{calendar_first}'
               + mark(9, pos="position: absolute; top: 57px; left: 93px;") + '</div>')


def fmt_row(examples, rule, last=False):
    bb = '' if last else f' border-bottom: 1px solid {C["LINE_ROW"]};'
    ex = ''.join(f'<span style="font-size: 13px; font-weight: 600; color: {C["INK"]}; font-variant-numeric: tabular-nums; white-space: nowrap;">{e}</span>' for e in examples)
    return (f'<div style="display: flex; align-items: center; gap: 12px; padding: 9px 0;{bb}">'
            f'<div style="width: 112px; flex-shrink: 0; display: flex; gap: 10px;">{ex}</div>'
            f'<div style="flex: 1; min-width: 0; font-size: 12px; line-height: 1.5; color: {C["INK2"]};">{rule}</div></div>')


# 계획 §3-3 칸 숫자 형식(§12-22) — 본보기 숫자는 계획 원문 그대로
fmt_card = card(
    f'<div style="font-size: 13.5px; font-weight: 700; color: {C["INK"]}; padding-bottom: 4px;">칸에 금액을 쓰는 법</div>'
    + fmt_row(['4,500', '900'], '1만 미만은 원 단위 그대로')
    + fmt_row(['1.2만', '12.5만'], '1만 이상은 만 단위 소수 한 자리 · 500원에서 올려요(11,500 → 1.2만)')
    + fmt_row(['3만', '30만'], '소수 첫 자리가 0이면 떼요<br>(29,500 → 3만 · 300,000 → 30만)')      # 제안 — 계획 §3-3의 예시 `이체 30만`에 맞춘 규칙
    + fmt_row(['120만', '1,200만'], '100만 이상은 소수 없이')
    + fmt_row(['1.2억'], '1억 이상', last=True)
    + f'<div style="font-size: 12px; line-height: 1.5; color: {C["INK3"]}; padding-top: 8px; border-top: 1px solid {C["LINE_ROW"]};">'
      f'상태 줄 · 기록 창 · 저장 완료 카드의 합계는 줄이지 않고 원 단위 그대로 씁니다(오늘 4건 37,000원).</div>', pad='12px 16px')

w('CalendarCells', spec_frame(
    1330, 880, '달력 칸 읽는 법',      # 2026-09-26 830 → 880(범례 줄 · 자연 856 + 24)      # 2026-09-24 820 → 830(달력 카드에 안내 줄 · 적기 줄 · 자연 높이 801)
    '칸의 숫자는 그날 소비 합계입니다(고정비 포함 · 이체 제외). 왼쪽 달력의 번호를 가운데에서 찾으세요.',
    f'<div style="display: flex; gap: 28px; align-items: flex-start;">'
    f'<div style="width: 362px; flex-shrink: 0;">{marked_calendar()}</div>'
    f'<div style="width: 490px; flex-shrink: 0;">{cell_guide}{cell_foot}</div>'
    f'<div style="width: 362px; flex-shrink: 0; display: flex; flex-direction: column; gap: 22px;">'
    + sample(362, '앱을 9월 5일에 처음 연 사람의 달력', '접힌 최근 7일 줄 · 2~4일은 쓰기 시작한 날보다 앞이지만 기록이 없으면 다른 빈 날처럼 —예요', since_strip)
    + fmt_card + '</div></div>', sub_w=760), keep_all=True)


# 폭과 글자 크기 — 어디서나 월 달력. 320px은 칸 39.4 × 56, 큰 글자는 칸 높이 72. 날짜 목록은 자동 대체가 아니라 큰 글자에서 고르는 보기.
# 앱처럼 이번 달 오늘까지 여덟 줄 모두(9월 8일 → 1일 · 2026-09-27 fix-up 3 · 예전엔 4일에서 끊고 표시가 없었다) — 값은 달력 칸과 같은 SEP 자료
_WD1 = '화수목금토일월'
LIST_ROWS = [(f'9월 {d}일 {_WD1[(d - 1) % 7]}' + (' · 오늘' if d == TODAY else ''),
              '—' if SEP[d] is None else ('0원 · 이체' if d in SEP_TRANSFER and not SEP[d] else f'{SEP[d]:,}원'), d in SEP_CHECK)
             for d in range(TODAY, 0, -1)]
assert [r[1] for r in LIST_ROWS] == ['37,000원', '—', '0원 · 이체', '12,000원', '4,500원', '58,500원', '—', '1,008,000원']
EMPTY13 = '<span style="width: 13px;"></span>'


def list_amount(a):
    if a == '—':
        return f'<span style="font-size: 16px; font-weight: 500; color: {C["INK3"]};">{a}</span>'
    col = C["INK2"] if a.startswith('0원') else C["INK"]
    return f'<span style="font-size: 16px; font-weight: 600; color: {col};">{a}</span>'


# 목록의 오늘 행(2026-09-24 최종 점검 후속) — 칸과 같이 brand-soft 바탕 · 안쪽 테두리 1.5px brand · 반경 10. 오늘 기록이 0건이면 `—` 대신 파란 원 `+`(24 — 큰 글자 칸과 같다).
# 이 견본의 오늘은 4건 37,000원이라 금액 그대로. 행 좌우 안쪽 6px(오늘 행 바탕이 글자에 닿지 않게 모든 행에).
LIST_TODAY = f'background: {C["BRAND_SOFT"]}; border-radius: 10px; {TODAY_RING}'


def list_row(d, a, c, today=False):
    line = f'border-top: 1px solid {"transparent" if today else C["LINE_ROW"]};'
    return (f'<div style="display: flex; align-items: center; gap: 10px; min-height: 48px; padding: 0 6px; {line}{" " + LIST_TODAY if today else ""}">'
            f'<span style="flex: 1; font-size: 16px; color: {C["INK"]};{" font-weight: 600;" if today else ""}">{d}</span>{list_amount(a)}{icon("check", 14, C["INK2"], 2.8) if c else EMPTY13}</div>')


list_view = card(
    month_bar('2026년 9월', prev_on=True, next_on=False, large=True) + hint(True, mt=6)
    + f'<div style="margin-top: 8px;">'
    + ''.join(list_row(d, a, c, today=(i == 0)) for i, (d, a, c) in enumerate(LIST_ROWS))
    + '</div>'
    # 목록 아래에도 달력 카드의 나머지가 그대로 남는다(앱): 범례 줄 · 그 달 합계 · 오늘 합계 + 알약 · 확인할 내용 · 달력으로 보기
    + legend(True) + status_line(month_total_text(9, SEP_TOTAL), True, mt=8) + today_tail(day_state('sep', TODAY), TODAY_TEXT, large=True, mt=10)
    + review_row(REVIEW_UNCAT, True)      # 캐논 = 항목 하나의 이름(2026-09-27 fix-up)
    + list_link(True).replace('목록으로 보기', '달력으로 보기'),
    pad='13px 14px 4px')


cal320 = calendar_card(True, pad=8).replace('2026년 9월', '9월').replace('min-width: 94px', 'min-width: 44px')
cal_large = calendar_card(True, large=True, with_list_link=True)
bar_prev320 = card(month_bar('8월', prev_on=False, next_on=True, back_pill=True, pill_below=True, label_w=44) + hint(mt=6)
                   + month_grid('aug', weeks=slice(0, 1)), pad='13px 8px 13px')          # 머리 부분만 떠 있지 않게 요일 줄과 첫 주를 붙인다
cal_large320 = card(month_bar('8월', prev_on=False, next_on=True, back_pill=True, large=True, label_w=52) + hint(True, mt=6)
                    + month_grid('aug', large=True, tight=True, weeks=slice(0, 3)), pad='13px 8px 13px')

# 접힌 최근 7일 줄 — 320px: 칸은 카드 안쪽 7등분(최대 44 · 320에서 약 39 × 56) · 옆으로 밀지 않고 7일이 다 보인다(home-17 · gen_calendar).
strip320 = calendar_card(False, pad=8, scroll=True)
# 큰 글자: 접힌 줄도 칸 그대로 — 칸 높이 72 · 날짜 14.5 · 합계는 칸 폭 44(47 미만)라 12 · 금액을 숨기지 않는다 · 상태 줄 14.5.
strip_large = calendar_card(False, large=True)

# 구현 수치는 견본 설명에 흩지 않고 맨 아래 한 단락으로 모은다.
sizes_memo = (f'<div style="margin-top: 24px; display: flex; flex-direction: column; gap: 4px;">'
              f'<div style="font-size: 12px; font-weight: 600; color: {C["INK2"]};">구현 메모</div>'
              f'<p style="margin: 0; font-size: 12px; line-height: 1.6; color: {C["INK3"]}; word-break: keep-all;">가장 좁은 폰은 화면 너비 320px, 달력 칸은 39 × 56입니다. '
              f'큰 글자에서는 칸 높이가 72가 됩니다. 좁은 폰 + 큰 글자에서는 금액 글자 크기를 12로 줄입니다. '
              f'지난달을 볼 때 &lsquo;이번 달로&rsquo; 버튼은 제목 줄 바로 아래 줄 오른쪽에 둡니다. '
              f'접힌 최근 7일 줄도 칸은 카드 안쪽 7등분(최대 44)이라 가장 좁은 폰에서 약 39 × 56이 되고, 옆으로 밀지 않고 7일이 다 보입니다. '
              f'큰 글자에서는 접힌 줄도 칸 높이 72 · 날짜 14.5이고, 칸 폭이 44 이하라 금액 글자는 12입니다. 칸 아래 범례 줄은 접힘 · 펼침 · 목록 모두에 늘 있습니다. '
              f'카드 아래 버튼 「+ 오늘 쓴 돈 적기」와 알약 줄(오늘 합계 + 「+ 더 적기」)은 어느 폭에서나 높이 40, 큰 글자에서는 48이고 제목 아래 안내 한 줄은 15px입니다. '
              f'목록으로 보기의 오늘 행도 칸처럼 파란 안쪽 테두리이고, 오늘 기록이 없으면 「—」 대신 파란 +(24)가 옵니다.</p></div>')

sizes_row1 = ('<div style="display: flex; gap: 36px; align-items: flex-start;">'
              + sample(292, '가장 좁은 폰', '달력 그대로. 제목은 9월만 적어요', cal320)
              + sample(362, '글자를 크게 쓰는 사람', '달력 그대로. 칸이 높아지고 글자가 커져요', cal_large)
              + sample(362, '목록으로 보기를 고르면', '스스로 고른 사람에게만. 저절로 바뀌지 않아요', list_view)
              + '</div>')
sizes_row2 = ('<div style="display: flex; gap: 36px; align-items: flex-start; margin-top: 26px;">'
              + '<div style="width: 292px; flex-shrink: 0; display: flex; flex-direction: column; gap: 24px;">'
              + sample(292, '가장 좁은 폰에서 지난달을 볼 때', '&lsquo;이번 달로&rsquo; 버튼은 제목 아랫줄로 내려가요 · 그림은 첫 주까지만 잘랐어요', bar_prev320)
              + sample(292, '가장 좁은 폰 · 접어 둔 달력', '칸을 카드 안쪽 7등분으로 줄여 7일이 다 보여요. 옆으로 밀지 않아요', strip320)
              + '</div>'
              + sample(292, '좁은 폰 + 큰 글자', '금액 글자를 조금 줄여 71.2만도 잘리지 않아요 · 그림은 셋째 주까지만 잘랐어요', cal_large320)
              + sample(362, '글자를 크게 쓰는 사람 · 접어 둔 달력', '칸이 높아지고 글자가 커져요. 금액은 숨기지 않아요', strip_large)
              + '</div>')

w('CalendarGridSizes', spec_frame(
    1150, 1745, '달력을 펼치면 어디서나 월 달력',      # 2026-09-27 fix-up 3 자연 1721 + 24(목록 여덟 줄 · 「이번 달로」 11px)      # 2026-09-26 1714 → 1750(목록 보기 아래 범례 · 합계 · 알약 · 확인할 내용 · 자연 1726 + 24)      # 2026-09-24 1490 → 1670(카드마다 안내 줄 · 적기 버튼/알약 줄) → 2026-09-26 DZ3 1714(칸 아래 범례 줄 · 자연 1690 + 24)
    '화면이 좁아도, 글자를 크게 써도 날짜를 세로로 늘어놓은 목록으로 바뀌지 않습니다. 접어 둔 최근 7일 줄도 칸 그대로입니다.',
    sizes_row1 + sizes_row2 + sizes_memo))


# ══════════════ 11. 새 홈 장 — 소비 목표 조정 · 달이 바뀐 첫 주 · 샘플 모드 (DZ4 · 2026-09-26) ══════════════
PILL_ADJ = ('<span style="display: inline-flex; align-items: center; height: 28px; padding: 0 11px; border-radius: 99px; border: 1px solid #C9D3F5; background: #FFFFFF; '
            'font-size: 12px; font-weight: 600; color: #3556E6; white-space: nowrap; flex-shrink: 0;">소비 목표 조정</span>')
TILES_OPEN = '<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 0; margin-top: 14px;'
DATE_LINE = '9월 8일 · 오늘 포함 23일 남음'
assert s1.hero_bare.count(PILL_ADJ) == 1 and s1.hero_bare.count(TILES_OPEN) == 1 and s1.header.count(DATE_LINE) == 1


def hero_with_notes(hero, notes):
    """각주 없는 히어로(hero_bare 모양) 끝에 안내 줄을 붙인다 — Main hero-notes 와 같은 모양(11px · 위 10)."""
    assert hero.rstrip().endswith('</div>')
    k = hero.rstrip().rindex('</div>')
    lines = ''.join(f'<p style="font-size: 11px; line-height: 1.4; color: {C["INK3"]}; margin: 10px 0 0;">{n}</p>' for n in notes)
    return hero[:k] + lines + hero[k:]


# ── HomeTargetEditor · 히어로 안의 소비 목표 조정(home-1 · D1 · D4) ──
# 알약 `소비 목표 조정`을 누르면 게이지 아래에 편집기가 열리고 알약은 `닫기`. 값을 아직 움직이지 않아 저장 버튼은 회색 `소비 목표 60%로 저장`.
# 참고 줄(ink-3 12 · 빨강 없음)은 planCapInfo 가 있을 때만 — 시안 사용자 152만원(NUMBERS §5 · 앱 캡처의 147만원은 지도 세계의 목적지 값).
# 그림은 캐논 9월 8일 그대로(2026-09-27 fix-up · 앱 하네스): 각주 두 줄(카테고리 없는 32,000원 · 고정비) · 달력의 `카테고리 없는 기록 7건` 행.
PILL_CLOSE = (f'<span style="display: inline-flex; align-items: center; justify-content: center; height: 28px; min-width: 64px; padding: 0 14px; border-radius: 99px; '
              f'background: {C["BRAND_SOFT"]}; font-size: 12px; font-weight: 600; color: {C["BRAND"]}; white-space: nowrap; flex-shrink: 0;">닫기</span>')


def round_btn(glyph):
    g = (f'<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="{C["INK2"]}" stroke-width="2" stroke-linecap="round"><path d="M5 12h14"/></svg>'
         if glyph == 'minus' else icon(glyph, 15, C["INK2"], 2))
    return (f'<span style="width: 30px; height: 30px; border-radius: 99px; background: {C["SURF"]}; border: 1px solid {C["BORDER"]}; display: inline-flex; '
            f'align-items: center; justify-content: center; flex-shrink: 0;">{g}</span>')


target_editor = (
    f'<div style="margin-top: 14px; background: {C["INSET"]}; border-radius: 16px; padding: 14px 12px 12px; display: flex; flex-direction: column; gap: 10px;">'
    f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px;">'
    f'<span style="font-size: 13px; color: {C["INK2"]};">월급의 얼마까지 쓸까요?</span>'
    f'<div style="display: flex; align-items: center; gap: 10px;">{round_btn("minus")}'
    f'<span style="font-size: 20px; font-weight: 700; letter-spacing: -0.03em; color: {C["INK"]};">60<span style="font-size: 13px; font-weight: 600; color: {C["INK2"]};">%</span></span>'
    f'{round_btn("plus")}</div></div>'
    f'<div style="position: relative; height: 22px; margin: 0 2px;">'
    f'<div style="position: absolute; left: 0; right: 0; top: 9px; height: 4px; border-radius: 99px; background: {C["TRACK"]};"></div>'
    f'<div style="position: absolute; left: 0; width: 60%; top: 9px; height: 4px; border-radius: 99px; background: {C["BRAND"]};"></div>'
    f'<span style="position: absolute; left: calc(60% - 11px); top: 0; width: 22px; height: 22px; border-radius: 99px; background: {C["SURF"]}; border: 2.5px solid {C["BRAND"]}; box-shadow: 0 1px 3px rgba(16,24,40,.18);"></span></div>'
    f'<div style="display: flex; align-items: center; justify-content: space-between; font-size: 11px; color: {C["INK3"]}; margin-top: -2px;">'
    f'<span>0%</span><span style="font-size: 12px; font-weight: 600; color: {C["INK"]};">월 216만원까지</span><span>100%</span></div>'
    f'<div style="background: {C["SURF"]}; border: 1px solid {C["LINE"]}; border-radius: 12px; padding: 11px 12px; min-height: 100px; display: flex; flex-direction: column; gap: 6px;">'      # 앱처럼 미리 보기 줄이 나타나도 흔들리지 않게 자리를 잡아 둔다(≈100 · 2026-09-27 fix-up 2)
    f'<span style="font-size: 12.5px; line-height: 1.5; color: {C["INK2"]};">소비 목표를 움직이면 저장했을 때 바뀌는 것이 여기에 보여요.</span>'
    f'<span style="font-size: 12px; line-height: 1.45; color: {C["INK3"]};">저축 · 상환 계획까지 지키려면 152만원 안에서 쓰면 돼요</span></div>'
    f'<div style="display: flex; gap: 6px; font-size: 11.5px; line-height: 1.5; color: {C["INK3"]};"><span style="flex-shrink: 0; margin-top: 2px;">{icon("lock", 12, C["INK3"], 2)}</span>'
    f'<span>쓴 돈 112만원(31.1%)과 월말 예상 208만원은 소비 목표를 바꿔도 그대로예요</span></div>'
    f'<div style="display: flex; gap: 8px;">{btn("취소", "secondary", h=40, radius=12, size=14).replace("width: 100%;", "flex: 1;")}'
    # 저장 버튼 비활성 = 앱 home-target.css(:disabled → 바탕 · 테두리 var(--disabled) #B4BECD · 글자 primary-foreground 흰색 · 다크 #5D6B85) — 하루 시트의 옅은 비활성과 다르다(2026-09-27 fix-up 3)
    f'{btn("소비 목표 60%로 저장", "primary", h=40, radius=12, size=14).replace("width: 100%;", "flex: 1.6;").replace("background: " + C["BRAND"] + ";", "background: " + C["DIS"] + ";")}</div></div>')
hero_edit = hero_with_notes(s1.hero_bare, CANON_NOTES).replace(PILL_ADJ, PILL_CLOSE).replace(TILES_OPEN, target_editor + TILES_OPEN)
assert hero_edit.count('소비 목표 60%로 저장') == 1 and '소비 목표 조정' not in hero_edit and hero_edit.count('<div') == hero_edit.count('</div>')
w('HomeTargetEditor', frame(
    f'\n  {s1.header}\n\n'
    f'  <div style="flex: 1; min-height: 0; display: flex; flex-direction: column; gap: 10px; padding: 0 14px; overflow: hidden;">\n\n'
    f'    {hero_edit}\n\n    {calendar_card(False)}\n\n  </div>\n\n'
    f'  {bottomnav(0)}\n'), keep_all=True)


# ── HomeMonthStart · 달이 바뀐 첫 주(10월 2일 · 9월 마감 전 · 10월 기록 0건) ──
# home-17 #2: 1 ~ 6일에는 스트립에 지난달 날이 들어가 제목이 `최근 7일 소비 기록` · 지난달 날은 `9/26`처럼 달을 붙인다.
# home-6 · D9: 0건인 달의 히어로 = 회색 `아직 기록이 없어요` · `달력에서 날짜를 눌러 쓴 돈을 적어 보세요` · `9월을 마감하면 월말 예상을 볼 수 있어요 · 9월 마감하기 ›` · 배지 없음.
# first-run-5 #3: 첫 기록 전 한도 `총 216만원` + `소비를 기록하면 남은 한도가 보여요`. 9월 마감 전이라 다음 안내는 늘 있는 카드 할부 안내 · 순자산 줄은 도착 시점 대신 D9 문장.
# 상환 계획 다 갚는 달은 10월 기준으로 한 달 밀린 2036년 6월(앱 캡처 · 116개월 뒤). 9월 끝 칸이 —인 것은 캐논 자료가 9월 8일에서 끝나서다.
LINK = f'<span style="font-weight: 600; color: {C["BRAND"]}; white-space: nowrap;">%s &rsaquo;</span>'
VAL_360 = (f'<span style="font-size: 18px; font-weight: 600; letter-spacing: -0.02em; color: {C["INK"]};">360'
           f'<span style="font-size: 13px; font-weight: 500; color: #475467;">만원</span></span>')
DASH18_V4 = s1.DASH18


def hero_zero(second, caption):
    """이번 달 기록 0건 · 월급 있음 — 빈 히어로에 월급 칸만 채운다."""
    h = s1.hero_empty(second=second, caption=caption, cta=False)
    assert h.count(DASH18_V4) == 3
    return h.replace(DASH18_V4, VAL_360, 1)


def limit_before():
    """첫 기록 전 이번 달 한도(앱): `이번 달 한도` · 오른쪽 `총 216만원 ›` · `소비를 기록하면 남은 한도가 보여요` · 빈 막대."""
    return (f'<div style="background: {C["SURF"]}; border: 1px solid {C["LINE"]}; border-radius: 18px; padding: 12px 14px; flex-shrink: 0;">'
            f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px;">'
            f'<span style="font-size: 13.5px; font-weight: 600; color: {C["INK"]}; white-space: nowrap;">이번 달 한도</span>'
            f'<div style="display: flex; align-items: center; gap: 4px;"><span style="font-size: 13.5px; font-weight: 600; color: {C["INK"]}; white-space: nowrap;">총 216만원</span>{icon("right", 16, C["INK4"], 2)}</div></div>'
            f'<div style="font-size: 13px; line-height: 1.45; color: {C["INK2"]}; margin-top: 4px;">소비를 기록하면 남은 한도가 보여요</div>'
            f'<div style="height: 8px; border-radius: 99px; background: {C["TRACK"]}; margin-top: 9px;"></div></div>')


OCT_STRIP = [('9/26', '토', CAL_NO_RECORD, False), ('9/27', '일', CAL_NO_RECORD, False), ('9/28', '월', CAL_NO_RECORD, False), ('9/29', '화', CAL_NO_RECORD, False),
             ('9/30', '수', CAL_NO_RECORD, False), ('1', '목', CAL_NO_RECORD, False), ('2', '금', CAL_NO_RECORD, True)]
# 확인할 내용 = `9월 카테고리 없는 기록 7건 · 마감 전에 정리` 하나(앱 10월 2일 · 캐논 · 2026-09-27 fix-up — 예전 합계 고치기 항목은 캐논에 없다).
cal_oct = calendar_card(False, title=RECENT_TITLE, strip=OCT_STRIP, review=REVIEW_PREV_UNCAT)
assert '최근 7일 소비 기록' in cal_oct and '오늘 쓴 돈 적기' in cal_oct and REVIEW_PREV_UNCAT in cal_oct and '합계 고치기' not in cal_oct
MONTH_START_H = 1118      # 자연 높이 1094 + 24
w('HomeMonthStart', frame(
    f'\n  {s1.header.replace(DATE_LINE, "10월 2일 · 오늘 포함 30일 남음")}\n\n'
    f'  <div style="flex: 1; min-height: 0; display: flex; flex-direction: column; gap: 10px; padding: 0 14px 14px; overflow: hidden;">\n\n'
    f'    {hero_zero("9월을 마감하면 월말 예상을 볼 수 있어요 · " + LINK % "9월 마감하기", "달력에서 날짜를 눌러 쓴 돈을 적어 보세요")}\n\n'
    f'    {cal_oct}\n\n    {first_guide}\n\n    {limit_before()}\n\n'
    f'    {s1.line_card("순자산", "9월을 마감하면 도착 시점을 볼 수 있어요", "9,350만원")}\n\n'
    f'    {s1.line_card("상환 계획", "다 갚는 달 <span style=" + chr(34) + "white-space: nowrap;" + chr(34) + ">2036년 6월</span> · 고금리 우선", "92만원", value_label="매달 갚는 돈")}\n\n  </div>\n\n'
    f'  {bottomnav(0)}\n', h=MONTH_START_H), keep_all=True)


# ── HomeSampleMode · 샘플 데이터로 둘러보는 중 ──
# D8 · language-ia-21 · first-run-17: 머리줄 위 띠 `샘플 데이터로 둘러보는 중 · 내 데이터로 시작 ›` 하나(다른 샘플 안내 없음).
# 샘플은 지난달들을 마감하지 않아 히어로가 `아직 기록하지 않은 소비는 포함되지 않았어요` + `월말 예상을 보려면 6월 · 7월 · 8월을 마감해 주세요 · 6월부터 마감하기 ›` ·
# 배지 없음 · 월말 예상 · 여유 — (D9). 달력은 `다 적었어요` 표시를 쓰지 않아 ✓ · 안 썼어요 0이 없고, 샘플 문장이 위 줄 · 확인할 내용 행 없음.
# 숫자는 시안 캐논(9월 8일 · 31.1% · 112만원 …)으로 그렸다 — 앱 샘플의 숫자(31.0% · 오늘 2건 112,500원 …)는 앱 자체 예시라 이 표에 없다.
def sample_strip():
    # 앱 .app-sample-strip — 높이 32(2rem) · 좌우 14 · brand-soft · 글자 12 / 500 brand-ink-on-soft #3B4E8F(다크 #A8BCF5) · 버튼 12 / 600 brand(2026-09-27 fix-up 3 · 예전 36 · ink-2)
    return (f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px; height: 32px; padding: 0 14px; background: {C["BRAND_SOFT"]}; flex-shrink: 0;">'
            f'<span style="font-size: 12px; font-weight: 500; line-height: 1.35; color: {C["BRAND_BANNER"]}; white-space: nowrap;">샘플 데이터로 둘러보는 중</span>'
            f'<span style="display: inline-flex; align-items: center; font-size: 12px; font-weight: 600; color: {C["BRAND"]}; white-space: nowrap;">내 데이터로 시작{icon("right", 13, C["BRAND"], 2.2)}</span></div>')


SAMPLE_CAL_TEXT = '샘플에서는 「다 적었어요」 표시를 쓰지 않아요 · 카테고리는 저장할 때 골라요'      # 앱 문구(record-11 · D4)
TILE3_RE = re.compile(r'(<span style="font-size: 18px; font-weight: 600; letter-spacing: -0.02em; color: #(?:101828|0F7B47);">(?:208|8)<span style="font-size: 13px; font-weight: 500; color: #(?:475467|0F7B47);">만원</span></span>)')


def hero_provisional(second_line):
    """월말 예상 기준이 서기 전(지난달 미마감) — 배지 없음 · 월말 예상 · 여유 — · 설명 줄 아래 각주 두 줄. 큰 숫자 · 오른쪽 줄 · 순자산 줄은 그대로."""
    h = BADGE_RE.sub('', s1.hero_bare, count=1)
    h, n = TILE3_RE.subn(DASH, h)
    assert n == 2, n
    c0 = h.index(HERO_CAPTION_ROW)
    depth, k = 0, c0
    for m in re.finditer(r'<div\b|</div>', h[c0:]):
        depth += 1 if m.group(0) == '<div' else -1
        if depth == 0:
            k = c0 + m.end(); break
    return h[:k] + foot_line(FOOT_FIRST) + foot_line(second_line) + h[k:]


_sample_base = calendar_card(False, review=0, states={d: (v[0], False, v[2], False) for d, v in
                                                       {3: ('5.9만', 0, False), 4: ('4,500', 0, False), 5: ('1.2만', 0, False), 6: ('—', 0, True)}.items()})
_sample_pill = pill_row(TODAY_TEXT, mt=10)
assert _sample_base.count(_sample_pill) == 1
cal_sample = _sample_base.replace(_sample_pill, status_line(SAMPLE_CAL_TEXT, mt=8) + pill_row(TODAY_TEXT, mt=6))
SAMPLE_H = 1246      # 자연 높이 1222 + 24(2026-09-27 fix-up 3 · 샘플 띠 36 → 32) · 예전 1226 + 24
w('HomeSampleMode', frame(
    f'\n  {sample_strip()}\n  {s1.header}\n\n'
    f'  <div style="flex: 1; min-height: 0; display: flex; flex-direction: column; gap: 10px; padding: 0 14px 14px; overflow: hidden;">\n\n'
    f'    {hero_provisional("월말 예상을 보려면 6월 · 7월 · 8월을 마감해 주세요 · " + LINK % "6월부터 마감하기")}\n\n'
    f'    {cal_sample}\n\n    {first_guide}\n\n    {limit_stage12()}\n\n'
    f'    {s1.line_card("순자산", "지난달들을 마감하면 도착 시점을 볼 수 있어요", "9,350만원")}\n\n    {s1.payoff_card}\n\n  </div>\n\n'
    f'  {bottomnav(0)}\n', h=SAMPLE_H), keep_all=True)


# ══════════════ 12. 새 홈 장(2026-09-27 fix-up 3) — 대표 목적지 카드 · 소비 목표를 저장한 직후 ══════════════
# ── HomePrimaryGoal · 홈 구성에서 「대표 목적지」를 고른 사람(앱 HOME_CARD_KEYS primaryGoal · 하네스 homeLayout = 대표 목적지 · 한도 · 순자산 · 상환 계획) ──
# 카드는 Main 의 대표 목적지 조각 그대로(68% 고리 · 「대표 목적지 ⌄」 목적지 고르기 · 비상금 6개월 · 1,020 / 1,500만원 · 도착까지 7개월 · 매달 70만원 · ›).
# 기본 홈(HomeDefaultScroll)에는 없다 — 다음 안내 자리를 이 카드가 대신한 구성. 스크롤 전체를 한 장에.
PRIMARY_H = 1195      # 자연 1171 + 24 —(gen_canvas TALL · screens.json 과 같게)
w('HomePrimaryGoal', frame(
    f'\n  {s1.header}\n\n'
    f'  <div style="flex: 1; min-height: 0; display: flex; flex-direction: column; gap: 10px; padding: 0 14px 14px; overflow: hidden;">\n\n'
    f'    {s1.hero_block}\n\n    {calendar_card(False)}\n\n    {goal_block}\n\n    {limit_stage12()}\n\n    {s1.networth_card}\n\n    {s1.payoff_card}\n\n  </div>\n\n'
    f'  {bottomnav(0)}\n', h=PRIMARY_H))


# ── HomeTargetSaved · 소비 목표 조정에서 50%로 저장한 직후(앱 하네스 target50 · D1 · D4 · D10) ──
# 아래 어두운 알림 「소비 목표 50%로 저장했어요 · 한도 180만원」 + 닫기 · 되돌리기(6초 뒤 40px 띠) · 같은 순간 종 배지 1 → 3(한도 · 월말 예상 알림이 새 선으로) ·
# 다음 안내 「월말엔 소비 목표 50%를 넘어요」 · 한도 카드 「오늘 포함 하루 29,570원 · 남은 한도 68만원 · 180만원 중 112만원 썼어요」. 히어로는 HeroOverTarget ①과 같다.
_bell = 'border: 2px solid #EDF0F7;">1</span>'
assert s1.header.count(_bell) == 1
header_bell3 = s1.header.replace(_bell, _bell.replace('>1<', '>3<'))
GUIDE_T = '투자 계좌 5,000만원에 매달 47만원이 더 필요해요'
GUIDE_B = '지금 매달 모으는 돈으로는 목표일에 닿기 어려워요. 목표일이나 순서를 바꿔 보세요.'
assert s1.guide_block.count(GUIDE_T) == 1 and s1.guide_block.count(GUIDE_B) == 1 and s1.guide_block.count('목적지 보기 &rsaquo;') == 1
guide_over = (s1.guide_block.replace(GUIDE_T, '월말엔 소비 목표 50%를 넘어요')
              .replace(GUIDE_B, '월말 예상 월급의 57.9%예요. 월 28만원 줄이면 소비 목표 안이에요.').replace('목적지 보기 &rsaquo;', '줄일 소비 찾기 &rsaquo;'))
limit_50 = limit_stage12()
for _a, _b in [('오늘 포함 하루 45,220원', '오늘 포함 하루 29,570원'), ('남은 한도 104만원', '남은 한도 68만원'), ('216만원 중 112만원 썼어요', '180만원 중 112만원 썼어요'),
               ('inset: 0 48.1% 0 0', 'inset: 0 37.8% 0 0')]:
    assert limit_50.count(_a) == 1, _a
    limit_50 = limit_50.replace(_a, _b)
TARGET_NOTICE = ('<!--dc-keep--><div style="position: absolute; left: 14px; right: 14px; bottom: 78px; background: #101828; border-radius: 16px; padding: 13px 14px 12px; color: #FFFFFF; box-shadow: 0 8px 24px rgba(0,0,0,.28);">'
                 '<div style="display: flex; align-items: flex-start; justify-content: space-between; gap: 8px;">'
                 '<span style="display: inline-flex; align-items: flex-start; gap: 7px; font-size: 14px; line-height: 1.45; font-weight: 500;"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#3DD489" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink: 0; margin-top: 3px;"><path d="M20 6 9 17l-5-5"/></svg>'
                 '<span><b style="font-weight: 700;">소비 목표 50%로 저장했어요</b> · 한도 180만원</span></span>'
                 '<span style="font-size: 12px; font-weight: 600; color: rgba(255,255,255,.72); white-space: nowrap; flex-shrink: 0;">닫기</span></div>'
                 f'<div style="display: flex; gap: 8px; margin-top: 11px;">{done_btn("되돌리기", "main")}</div>'
                 '</div><!--/dc-keep-->')
w('HomeTargetSaved', frame(
    f'\n  {header_bell3}\n\n'
    f'  <div style="flex: 1; min-height: 0; display: flex; flex-direction: column; gap: 9px; padding: 0 14px; overflow: hidden; position: relative;">\n\n'
    f'    {OVER_CASES[0][3]}\n\n    {calendar_card(False)}\n\n    {guide_over}\n\n    {limit_50}\n\n  </div>\n\n'
    f'  {bottomnav(0)}\n  {TARGET_NOTICE}\n').replace('overflow: hidden; font-variant-numeric: tabular-nums;">', 'overflow: hidden; position: relative; font-variant-numeric: tabular-nums;">', 1))
