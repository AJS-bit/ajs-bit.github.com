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
from gen_calendar import (WD, TODAY, fmt_sum, SEP, SEP_CHECK, SEP_TRANSFER, AUG, AUG_CHECK, AUG_TRANSFER, SEP_TOTAL, AUG_TOTAL,
                          MONTHS, WEEKS, day_state, _mods, cell, gcell, nav_btn, month_bar, status_rows, month_grid, list_link,
                          calendar_card)   # 달력 자료 · 칸 · 카드는 공용 모듈(gen_v4 계열도 함께 쓴다)

OUT = s1.OUT
V5 = ['HomeCalendarStrip', 'HomeDefaultScroll', 'HomeCalendar', 'HomeCalendar360', 'HomeCalendarPrev', 'DaySheet', 'DaySheetScrolled', 'DaySheetList', 'DaySheetEdit',
      'DoneCard', 'DaySheetConfirm', 'ClassifySheet', 'HeroInsufficient', 'DaySheet360', 'HeroFootnotes', 'CalendarCells', 'CalendarGridSizes']

KB_H = 280          # 시스템 숫자 키보드가 덮는 높이(자리만 표시)
SCRIM_H = 60


def w(name, body, keep_all=False):
    light = doc(body, keep_all=keep_all)
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
    """최근 기록 칩 — `커피 4,500 ·카페/간식` · `편의점 6,500 ·분류 안 함`(계획 §4-2). 색만으로 분류를 전하지 않게 점 뒤에 이름을 쓴다.
    메모는 8자 + … 로 줄인다. 가로 스크롤 · 최대 5개."""
    memo = memo if len(memo) <= 8 else memo[:8] + '…'
    if cat:
        tail = (f'<span style="display: inline-flex; align-items: center; gap: 4px; font-size: 11px; font-weight: 500; color: {C["INK2"]};">'
                f'<span style="width: 7px; height: 7px; border-radius: 99px; background: {CAT[cat]}; flex-shrink: 0;"></span>{cat}</span>')
    else:
        tail = f'<span style="font-size: 11px; font-weight: 500; color: {C["INK3"]};">분류 안 함</span>'
    return (f'<span style="display: inline-flex; align-items: center; gap: 7px; height: 32px; padding: 0 11px; border-radius: 8px; background: {C["INSET"]}; '
            f'font-size: 12px; font-weight: 500; color: {C["INK"]}; white-space: nowrap; flex-shrink: 0;">{memo} <span style="font-weight: 600;">{amount:,}</span>{tail}</span>')


def field_label(text):
    return f'<span style="font-size: 12px; font-weight: 600; color: {C["INK2"]};">{text}</span>'


def amount_field(value, focused=True, selected=False, w_=None):
    """금액 입력 — 17px 우측 정렬, 단위 원. selected = 수정 모드의 전체 선택."""
    ring = f'border: 1.5px solid {C["BRAND"]}; box-shadow: 0 0 0 3px rgba(53,86,230,.16);' if focused else f'border: 1px solid {C["INPUT"]};'
    val = (f'<span style="background: {C["BRAND_SOFT"]}; border-radius: 4px; padding: 1px 3px;">{value}</span>' if selected else value)
    return (f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 10px; height: 48px; padding: 0 14px; border-radius: 12px; background: {C["SURF"]}; {ring}">'
            f'{field_label("금액")}<span style="display: inline-flex; align-items: baseline; gap: 4px;">'
            f'<span style="font-size: 20px; font-weight: 600; letter-spacing: -0.02em; color: {C["INK"]}; font-variant-numeric: tabular-nums;">{val}</span>'
            f'<span style="font-size: 13px; font-weight: 500; color: {C["INK3"]};">원</span></span></div>')


def memo_field(value='', counter=None):
    cnt = f'<span style="font-size: 11px; color: {C["INK3"]};">{counter}</span>' if counter else ''
    v = f'<span style="font-size: 15px; color: {C["INK"]};">{value}</span>' if value else f'<span style="font-size: 15px; color: {C["DIS"]};">메모</span>'
    return (f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 10px; height: 44px; padding: 0 14px; border-radius: 12px; background: {C["SURF"]}; border: 1px solid {C["INPUT"]};">'
            f'<span style="display: inline-flex; align-items: center; gap: 12px;">{field_label("메모")}{v}</span>{cnt}</div>')


def category_row(selected=None, frequent=('식비', '카페/간식', '교통'), right='나중에 분류'):
    chips = ''.join(cat_chip(n, selected == n) for n in frequent)
    r = f'<span style="margin-left: auto; font-size: 12px; font-weight: 500; color: {C["INK3"]}; white-space: nowrap;">{right}</span>' if right else ''
    return (f'<div style="display: flex; flex-direction: column; gap: 8px;">'
            f'<div style="display: flex; align-items: center; gap: 8px;">{field_label("분류")}{r}</div>'
            f'<div style="display: flex; align-items: center; gap: 6px; overflow: hidden;">{chips}'
            f'<span style="font-size: 12.5px; font-weight: 600; color: {C["BRAND"]}; white-space: nowrap; padding-left: 4px;">전체 &rsaquo;</span></div></div>')


def recent_row(chips, pad=18):
    return (f'<div style="display: flex; flex-direction: column; gap: 8px;">{field_label("최근 기록")}'
            f'<div style="display: flex; gap: 6px; overflow: hidden; margin: 0 -{pad}px; padding: 0 {pad}px;">{"".join(chips)}</div></div>')


def unsaved_line(reading, fail=None):
    base = (f'<div style="font-size: 11.5px; line-height: 1.45; color: {C["INK3"]}; padding: 0 2px;">'
            f'<span style="font-weight: 600; color: {C["INK2"]};">{reading}</span> · 저장을 눌러야 기록돼요</div>')
    if fail:      # 오류 문장은 한 문장, `다시 시도`는 따로 떨어진 버튼
        warn = icon("warn", 14, C["NEG"], 2).replace('<svg ', '<svg style="flex-shrink: 0; margin-top: 2px;" ', 1)
        retry = smallbtn("다시 시도", "secondary", h=30).replace('display: inline-flex;', 'align-self: center; display: inline-flex;', 1).replace('font-weight: 600;">', 'font-weight: 600; white-space: nowrap; flex-shrink: 0;">', 1)
        base += (f'<div style="display: flex; gap: 8px; padding: 9px 11px; background: {C["NEG_SOFT"]}; border-radius: 10px; margin-top: 6px;">'
                 f'{warn}<span style="flex: 1; min-width: 0; font-size: 11.5px; line-height: 1.45; color: #7C221E;">{fail}</span>{retry}</div>')
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


def sheet_header(title, sub, today=True, next_on=False):
    """제목 양옆 ‹ › 로 날짜를 옮긴다(기록 · 목록 · 수정 모두 같은 모양). next_on = 다음 날로 갈 수 있을 때 진한 색."""
    t = f'<h2 style="margin: 0; font-size: 18px; font-weight: 700; letter-spacing: -0.025em; color: {C["INK"]}; white-space: nowrap;">{title}</h2>'
    if today:
        t += f'<span style="font-size: 12.5px; font-weight: 500; color: {C["INK3"]}; margin-left: 6px;">오늘</span>'
    return (f'<div style="display: flex; justify-content: center; padding: 9px 0 0; flex-shrink: 0;"><span style="width: 38px; height: 4px; border-radius: 99px; background: {C["BORDER"]};"></span></div>'
            f'<div style="display: flex; align-items: flex-start; justify-content: space-between; gap: 10px; padding: 12px 18px 12px; border-bottom: 1px solid {C["LINE_SOFT"]}; flex-shrink: 0;">'
            f'<div style="display: flex; flex-direction: column; gap: 3px; min-width: 0;">'
            f'<div style="display: flex; align-items: center; gap: 4px;">'
            f'{icon("left", 18, C["INK2"], 2)}'
            f'<div style="display: flex; align-items: baseline;">{t}</div>'
            f'{icon("right", 18, C["INK2"] if next_on else "#C4CCDA", 2)}'
            f'</div><span style="font-size: 12.5px; color: {C["INK3"]};">{sub}</span></div>'
            f'<span style="font-size: 13px; font-weight: 600; color: {C["INK2"]}; padding-top: 4px; flex-shrink: 0;">닫기</span></div>')


SCRIM_TEXT = '배경을 눌러 닫기 · 앱이 다시 시작되면 저장하지 않은 내용은 사라져요'      # 계획 §4-2 원문


def sheet_frame(inner, w_=390, keyboard=False, scrim_text=SCRIM_TEXT, h_=844):
    kb = kb_block(w_) if keyboard else ''
    return (f'<div style="width: {w_}px; height: {h_}px; background: #2A3245; color: {C["INK"]}; display: flex; flex-direction: column; overflow: hidden; position: relative; font-variant-numeric: tabular-nums;">'
            f'{scrim_line(scrim_text)}'
            f'<div style="flex: 1; min-height: 0; background: {C["SURF"]}; border-radius: 26px 26px 0 0; display: flex; flex-direction: column; overflow: hidden;">{inner}</div>{kb}</div>')


def save_btn(label='저장'):
    return btn(label, 'primary', h=52, radius=14, size=16)


LINKS_NOTE = '저축·투자와 대출상환은 거래 추가에서 남겨요 · 소비율에는 안 들어가요'      # 계획 §8 원문


def links_row(note=True):
    links = (f'<div style="display: flex; align-items: center; gap: 14px;">'
             f'<span style="font-size: 12.5px; font-weight: 600; color: {C["BRAND"]}; white-space: nowrap;">저축·투자로 기록 &rsaquo;</span>'
             f'<span style="font-size: 12.5px; font-weight: 600; color: {C["BRAND"]}; white-space: nowrap;">대출상환으로 기록 &rsaquo;</span></div>')
    if not note:
        return links
    return (f'<div style="display: flex; flex-direction: column; gap: 5px;">{links}'
            f'<span style="font-size: 11.5px; line-height: 17px; color: {C["INK3"]};">{LINKS_NOTE}</span></div>')


def day_done_btn(label):
    """시트 맨 아래 확인 버튼 — `9월 8일 다 적었어요`(소비 1건 이상 · 시간 무관). 채운 Primary 가 아니다(시트 안 채운 Primary 는 `저장` 하나)."""
    return btn(label, 'secondary', h=44, radius=12, size=14.5).replace('font-weight: 600;">', 'font-weight: 600; white-space: nowrap; flex-shrink: 0;">', 1)


def more_row(label='1건 더 보기'):
    return (f'<div style="display: flex; align-items: center; gap: 5px; height: 32px; flex-shrink: 0; font-size: 12.5px; font-weight: 600; color: {C["BRAND"]}; white-space: nowrap;">'
            f'{icon("plus", 13, C["BRAND"], 2.4)}{label}</div>')


def tx_row(cat, memo, amount, last=False, h=46):
    bb = '' if last else f'border-bottom: 1px solid {C["LINE_ROW"]};'
    if cat:
        left = (f'<span style="display: inline-flex; align-items: center; gap: 6px; width: 96px; flex-shrink: 0;"><span style="width: 8px; height: 8px; border-radius: 99px; background: {CAT[cat]};"></span>'
                f'<span style="font-size: 12.5px; font-weight: 500; color: {C["INK2"]}; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">{cat}</span></span>')
    else:
        left = f'<span style="width: 96px; flex-shrink: 0; font-size: 12.5px; font-weight: 500; color: {C["INK3"]};">분류 안 함</span>'
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
RECENT = [('커피', 4500, '카페/간식'), ('편의점', 6500, None), ('점심', 9000, '식비'), ('버스', 1500, '교통')]      # 계획 §4-2 도면의 칩 · 오늘 기록과 같은 자료


def today_list(h=44):
    """키보드 경계 아래 — `오늘 기록` 라벨 + 3행 + `+ 1건 더 보기`(오늘 4건 37,000원 중 3건 · 계획 §4-2 도면)."""
    return (f'<div style="display: flex; flex-direction: column; flex-shrink: 0;">'
            f'<div style="height: 18px; display: flex; align-items: center; margin-bottom: 4px;">{field_label("오늘 기록")}</div>'
            + tx_row('카페/간식', '커피', 4500, h=h) + tx_row('식비', '점심', 9000, h=h) + tx_row(None, '편의점', 6500, last=True, h=h)
            + more_row('1건 더 보기') + '</div>')


def day_sheet_body(w_=390, fail=None, amount='12,000', memo='편의점', selected=None, keyboard=True):
    """하루 시트 본문(오늘). keyboard=True 는 키보드 열림(기본 아트보드) — 링크까지. False 는 키보드를 내린 상태 — 그 아래 `오늘 기록` 목록 · `+ 1건 더 보기` · `9월 8일 다 적었어요`까지."""
    pad = 18 if w_ >= 390 else 14
    recent = recent_row([recent_chip(*r) for r in RECENT], pad)
    below = '' if keyboard else (f'<div style="margin-top: 4px;">{today_list()}</div>'
                                 f'<div style="margin-top: auto; padding-bottom: 12px; flex-shrink: 0;">{day_done_btn("9월 8일 다 적었어요")}</div>')
    return (sheet_header('9월 8일 소비 기록', '오늘 4건 37,000원')
            + f'<div style="flex: 1; min-height: 0; overflow: hidden; padding: 12px {pad}px 0; display: flex; flex-direction: column; gap: 10px;">'
            + amount_field(amount, focused=keyboard)
            + unsaved_line('1.2만원', fail)
            + memo_field(memo)
            + category_row(selected)
            + recent
            + f'<div style="margin-top: 2px; flex-shrink: 0;">{save_btn()}</div>'
            + f'<div style="padding-top: 2px; flex-shrink: 0;">{links_row()}</div>'
            + below
            + '</div>')


def day_sheet_body_short(w_=360):
    """360 × 640 — 키보드를 내리고 본문을 아래로 민 상태. 위 영역(금액 · 메모 · 분류는 위로 밀려 올라감)만 스크롤되고 `저장`은 푸터에 고정(계획 §8 좁은 화면)."""
    pad = 18 if w_ >= 390 else 14
    recent = recent_row([recent_chip(*r) for r in RECENT], pad)
    return (sheet_header('9월 8일 소비 기록', '오늘 4건 37,000원')
            + f'<div style="flex: 1; min-height: 0; overflow: hidden; padding: 12px {pad}px 0; display: flex; flex-direction: column; gap: 10px;">'
            + f'<div style="flex-shrink: 0;">{recent}</div>'
            + f'<div style="flex-shrink: 0;">{links_row()}</div>'
            + today_list()
            + f'<div style="padding-bottom: 12px; flex-shrink: 0;">{day_done_btn("9월 8일 다 적었어요")}</div>'
            + '</div>'
            + f'<div style="padding: 10px {pad}px 14px; border-top: 1px solid {C["LINE_SOFT"]}; background: {C["SURF"]}; flex-shrink: 0;">{save_btn()}</div>')


w('DaySheet', sheet_frame(day_sheet_body(), keyboard=True))
# 같은 시트에서 키보드를 내린 상태 — 키보드 경계 아래(오늘 기록 · + 1건 더 보기 · 다 적었어요)가 보인다
w('DaySheetScrolled', sheet_frame(day_sheet_body(keyboard=False)))
# 가장 작은 화면 360 × 640 — 목록 3행 + `+ 1건 더 보기` + `저장`까지 보이고 위 영역만 스크롤 · 푸터 고정
w('DaySheet360', sheet_frame(day_sheet_body_short(360), w_=360, h_=640))


# ══════════════ 2. 목록 우선 — 기록 있는 과거 날 ══════════════
list_body = (
    sheet_header('9월 3일 소비 기록', '3건 58,500원', today=False, next_on=True)      # 오늘(9월 8일)보다 앞선 날 — › 는 오늘에서만 멈춘다(DaySheetEdit 와 같게)
    + f'<div style="flex: 1; min-height: 0; overflow: hidden; padding: 14px 18px 0; display: flex; flex-direction: column; gap: 12px;">'
    + f'<div style="display: flex; flex-direction: column; gap: 8px;">'          # 제목이 날짜·건수·합계를 이미 말해서 구역 제목은 두지 않는다
    + card(tx_row('교통', '택시', 45000) + tx_row('식비', '점심', 9000) + tx_row(None, '간식', 4500, last=True), pad='2px 14px')
    + '</div>'
    + dashed_row('추가')
    + f'<div style="flex-shrink: 0;">{links_row()}</div>'
    + f'<div style="margin-top: auto; padding-bottom: 12px; flex-shrink: 0;">{day_done_btn("9월 3일 다 적었어요")}</div>'      # 소비 1건 이상이면 시간과 무관하게 보인다
    + '</div>')
w('DaySheetList', sheet_frame(list_body))


# ══════════════ 3. 수정 모드 ══════════════
edit_body = (
    sheet_header('9월 3일 기록 수정', '9월 3일 3건 58,500원', today=False, next_on=True)
    + f'<div style="flex: 1; min-height: 0; overflow: hidden; padding: 14px 18px 0; display: flex; flex-direction: column; gap: 12px;">'
    + amount_field('45,000', focused=True, selected=True)
    + f'<div style="font-size: 11.5px; line-height: 1.45; color: {C["INK3"]}; padding: 0 2px;"><span style="font-weight: 600; color: {C["INK2"]};">4.5만원</span></div>'
    + memo_field('택시')
    + category_row('교통', right='')
    + f'<div style="display: flex; gap: 8px; margin-top: 2px;">{btn("저장", "primary", h=52, radius=14, size=16).replace("width: 100%;", "flex: 1.6;")}{btn("삭제", "secondary", h=52, radius=14, size=15).replace("width: 100%;", "flex: 1;")}</div>'
    + '</div>')
w('DaySheetEdit', sheet_frame(edit_body, keyboard=True))


# ══════════════ 4. 완료 카드 — 홈 위 ══════════════
# 저장 뒤 홈: 히어로는 Main과 같은 자리·모양이고 값만 12,000원 저장 뒤로(57.9 → 58.2, 208 → 210만원, 여유 8 → 6만원, 2.1%p → 1.8%p · 하루 47,270 → 46,730원).
hero_after = s1.hero_block
for a, b in [('>57.9<', '>58.2<'), ('2.1%p 여유', '1.8%p 여유'), ('inset: 0 42.1% 0 0', 'inset: 0 41.8% 0 0'),
             ('>208<span', '>210<span'), ('>8<span style="font-size: 13px; font-weight: 500; color: #0F7B47;">만원', '>6<span style="font-size: 13px; font-weight: 500; color: #0F7B47;">만원')]:
    assert hero_after.count(a) == 1, a
    hero_after = hero_after.replace(a, b)
limit_after = (s1.limit_block.replace('남은 한도 104만원', '남은 한도 103만원').replace('inset: 0 48.1% 0 0', 'inset: 0 47.6% 0 0')
               .replace('하루 47,270원', '하루 46,730원'))      # 1단계 장 — 라벨은 v3 그대로 `하루 …`(`앞으로 하루`는 v5 · 3단계부터 · 계획 §9-3 · §10)
assert limit_after.count('하루 46,730원') == 1 and '앞으로 하루' not in limit_after and limit_after.count('남은 한도 103만원') == 1 and limit_after.count('inset: 0 47.6% 0 0') == 1

# 셋째 줄 — 이 장의 저장은 DaySheet 에서 분류를 고르지 않은(`나중에 분류`) 편의점 12,000원이라 계획 §4-4 우선순위의 4순위 문장이 온다.
# 소비율 줄 `소비율 57.9% → 58.2%`는 앞선 조건이 하나도 없을 때만(6순위) — 히어로의 58.2% 등 값은 그대로다.
DONE_THIRD = '소비에는 이미 포함됐어요 · 분류하면 예상을 다시 계산해요'      # 계획 §4-4 원문
DONE_CARD = ('<!--dc-keep--><div style="position: absolute; left: 14px; right: 14px; bottom: 78px; background: #101828; border-radius: 16px; padding: 13px 14px 12px; color: #FFFFFF; box-shadow: 0 8px 24px rgba(0,0,0,.28);">'
             '<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px;">'
             '<span style="display: inline-flex; align-items: center; gap: 7px; font-size: 14px; font-weight: 700;"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#3DD489" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg>저장했어요</span>'
             '<span style="font-size: 12px; font-weight: 600; color: rgba(255,255,255,.72);">닫기</span></div>'
             '<div style="font-size: 13.5px; font-weight: 500; margin-top: 7px; color: #FFFFFF;">9월 8일 · <span style="font-weight: 700;">12,000원</span> 저장 · 오늘 5건 49,000원</div>'
             f'<div style="font-size: 12.5px; margin-top: 3px; color: rgba(255,255,255,.72);">{DONE_THIRD}</div>'
             '<div style="display: flex; gap: 8px; margin-top: 11px;">'
             '<span style="display: inline-flex; align-items: center; justify-content: center; height: 36px; padding: 0 14px; border-radius: 10px; border: 1px solid rgba(255,255,255,.55); color: #FFFFFF; font-size: 13px; font-weight: 700;">한 건 더</span>'
             '<span style="display: inline-flex; align-items: center; justify-content: center; height: 36px; padding: 0 12px; border-radius: 10px; border: 1px solid rgba(255,255,255,.28); color: #FFFFFF; font-size: 13px; font-weight: 600;">방금 기록한 12,000원 취소</span></div>'
             '</div><!--/dc-keep-->')

# 달력은 저장 결과를 반영한다 — 오늘(8일) 칸 3.7만 → 4.9만, 상태 줄 `오늘 5건 49,000원`.
calendar_after = calendar_card(False, states={TODAY: (fmt_sum(49_000), False, False, False)}, status='오늘 5건 49,000원')
assert calendar_after.count('>4.9만<') == 1 and '3.7만' not in calendar_after
# 완료 카드 아래 끝(766)과 탭 바(778) 사이 12px 틈에 밑의 한도 카드 글자 윗절반이 비치지 않게, 본문을 한도 카드 시작 위에서 자른다.
# 실제 글꼴 실측: 다음 안내 아래 끝 748.1 · 한도 카드 시작 757.1 · 탭 바 위 끝 778 → 본문 아래 끝을 756 으로(778 − 22). 틈에는 장 바탕만 보인다.
# 한도 카드 · 순자산 카드는 HTML 에 그대로 둔다(기준표 5번 46,730원 · 103만원 · 47.6%). 달력 · 다음 안내 높이가 바뀌면 이 값을 다시 잴 것.
DONE_BODY_CUT = 22
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


fixed_chips = ''.join(cat_chip(n) for n in ['주거/관리', '통신', '보험', '구독'])
notice_fixed = neutral_notice(
    f'<span style="font-size: 13.5px; font-weight: 600; color: {C["INK"]};">매달 나가는 돈인가요?</span>'
    f'<div style="display: flex; gap: 6px; flex-wrap: wrap;">{fixed_chips}</div>'
    f'<div style="display: flex; align-items: center; gap: 12px;"><span style="font-size: 12.5px; font-weight: 600; color: {C["BRAND"]};">저축·투자 &rsaquo;</span><span style="font-size: 12.5px; font-weight: 600; color: {C["BRAND"]};">대출상환 &rsaquo;</span>'
    f'<span style="margin-left: auto; font-size: 12.5px; font-weight: 600; color: {C["INK2"]}; white-space: nowrap;">그대로 저장</span></div>')
block_fixed = confirm_block(amount_field('700,000', focused=False) + notice_fixed)
block_rule = confirm_block(
    amount_field('55,000', focused=False)
    + neutral_notice(
        f'<span style="font-size: 13px; line-height: 1.45; color: {C["INK"]};">이번 달 휴대폰 요금 55,000원은 <b style="font-weight: 600;">25일에 자동으로 기록돼요</b></span>'
        f'<div style="display: flex; gap: 8px;">{nowrap_btn(smallbtn("이번 달은 이미 기록했어요", "soft", h=34))}{nowrap_btn(smallbtn("그대로 저장", "secondary", h=34))}</div>'))
block_dup = confirm_block(
    amount_field('55,000', focused=False)
    + neutral_notice(
        f'<span style="font-size: 13px; line-height: 1.45; color: {C["INK"]};">같은 날 통신 55,000원(반복)이 <b style="font-weight: 600;">이미 있어요</b></span>'
        f'<div style="display: flex; gap: 8px;">{nowrap_btn(smallbtn("그래도 저장", "secondary", h=34))}{nowrap_btn(smallbtn("취소", "secondary", h=34))}</div>'))
block_fail = confirm_block(
    amount_field('12,000', focused=True)
    + unsaved_line('1.2만원', fail='저장하지 못했어요. 적은 내용은 그대로 있어요.')
    )
# 왼쪽 — DaySheet와 같은 창(머리줄 · 금액 · 메모 · 분류 · 저장)에 ①의 안내를 넣고 그 자리에 번호를 얹는다. 최근 기록 · 이체 링크 · 키보드 자리는 뺀다.
confirm_sheet = (
    f'<div style="background: {C["SURF"]}; border: 1px solid {C["LINE"]}; border-radius: 26px 26px 18px 18px; overflow: hidden; display: flex; flex-direction: column;">'
    + sheet_header('9월 8일 소비 기록', '오늘 4건 37,000원')
    + f'<div style="padding: 12px 18px 18px; display: flex; flex-direction: column; gap: 10px;">'
    + amount_field('700,000', focused=False)
    + f'<div style="position: relative;">{notice_fixed}{mark(1, pos="position: absolute; top: -6px; right: -6px; flex-shrink: 0;")}</div>'
    + memo_field('월세') + category_row(None)
    + f'<div style="margin-top: 2px;">{save_btn()}</div></div></div>')
confirm_left = (
    f'<div style="width: 362px; flex-shrink: 0; display: flex; flex-direction: column; gap: 8px;">{confirm_sheet}'
    f'<p style="margin: 2px 2px 0; font-size: 12px; line-height: 1.5; color: {C["INK3"]};">네 안내 모두 '
    f'<b style="font-weight: 600; color: {C["INK2"]};">금액 칸 바로 아래</b> 이 자리에 뜹니다. 그림은 1번의 경우입니다.</p></div>')
CONFIRM_CASES = [
    (1, '큰 금액을 적었을 때', '월급의 10%가 넘으면 매달 나가는 돈인지 물어봅니다.', block_fixed),
    (2, '곧 자동으로 기록될 돈을 미리 적었을 때', '이미 기록했다고 하면 이번 달 자동 기록은 건너뜁니다.', block_rule),
    (3, '같은 날 같은 돈이 이미 있을 때', '알려만 주고 막지 않습니다.', block_dup),
    (4, '저장이 안 됐을 때', '창은 그대로 열려 있고 적은 값도 남아 있습니다.', block_fail)]
CONFIRM_MEMO = [
    (1, '적은 금액이 월급(실수령)의 10% 이상일 때 뜹니다. 그림은 월급 360만원이라 36만원부터입니다. 그대로 저장해도 됩니다. '
        '그대로 저장하면 &lsquo;분류 안 함&rsquo;으로 저장되고, 예상 소비에는 적은 금액 그대로 더해집니다.'),
    (2, '켜져 있는 반복 지출과 금액 차이가 5% 안이거나 메모가 같고, 아직 결제일 전일 때 뜹니다.'),
    (3, '같은 날 자동으로 기록된 반복 지출이 이미 있을 때 뜹니다. 금액이 비슷하다는 이유만으로 지우거나 자동 기록을 건너뛰지 않습니다.'),
    (4, '안내는 금액 칸 아래에 그대로 남습니다. 저장 완료 카드는 뜨지 않습니다.')]


def memo_row(n, text, last=False):
    bb = '' if last else f' border-bottom: 1px solid {C["LINE_ROW"]};'
    return (f'<div style="display: flex; gap: 10px; padding: 7px 0;{bb}">{mark(n, pos="margin-top: 1px; flex-shrink: 0;")}'
            f'<div style="font-size: 12px; line-height: 1.55; color: {C["INK2"]};">{text}</div></div>')


confirm_memo = (f'<div style="background: {C["SURF"]}; border: 1px solid {C["LINE"]}; border-radius: 18px; padding: 10px 18px 8px;">'
                f'<div style="font-size: 12px; font-weight: 700; color: {C["INK"]}; padding: 2px 0 4px;">구현 메모</div>'
                + ''.join(memo_row(n, t, last=(n == 4)) for n, t in CONFIRM_MEMO) + '</div>')
w('DaySheetConfirm', spec_frame(
    1200, 900, '저장을 눌렀는데 한 번 더 물어보는 경우',
    '아래 네 경우에는 바로 저장하지 않고 금액 칸 아래에 안내가 한 줄 뜹니다. 저장을 한 번 더 누르면 그대로 저장됩니다.',
    f'<div style="display: flex; gap: 32px; align-items: flex-start;">{confirm_left}'
    f'{case_grid([(case_cap(n, t, d), blk) for n, t, d, blk in CONFIRM_CASES])}</div>{confirm_memo}', sub_w=760), keep_all=True)


# ══════════════ 6. 분류하기 시트 ══════════════
def check(on):
    if on:
        return f'<span style="width: 22px; height: 22px; border-radius: 7px; background: {C["BRAND"]}; display: inline-flex; align-items: center; justify-content: center; flex-shrink: 0;">{icon("check", 14, "#FFFFFF", 3)}</span>'
    return f'<span style="width: 22px; height: 22px; border-radius: 7px; background: {C["SURF"]}; border: 1.5px solid {C["INPUT"]}; flex-shrink: 0;"></span>'


def group_row(memo, count, amount, reco, chosen, expanded=False, picked=None):
    """picked = 묶음에서 고른 건수(일부를 제외했을 때). 금액 줄에 `3건 중 2건 · 합계`로 보여 준다."""
    total = f'{count}건 중 {picked}건 · {won(amount)}' if picked is not None else won(amount)
    chip = (f'<span style="display: inline-flex; align-items: center; gap: 5px; height: 30px; padding: 0 10px; border-radius: 8px; '
            f'{"background: " + C["BRAND_SOFT"] + "; border: 1.5px solid " + C["BRAND"] + ";" if chosen else "background: " + C["SURF"] + "; border: 1px solid " + C["BORDER"] + ";"} '
            f'font-size: 12px; font-weight: 600; color: {C["INK"]}; white-space: nowrap;"><span style="width: 8px; height: 8px; border-radius: 99px; background: {CAT[reco]};"></span>{reco}'
            + ('' if chosen else f'<span style="font-size: 10.5px; font-weight: 500; color: {C["INK3"]};">추천</span>') + '</span>')
    return (f'<div style="display: flex; align-items: center; gap: 10px; height: 52px; border-bottom: 1px solid {C["LINE_ROW"]};">'
            f'<div style="display: flex; flex-direction: column; gap: 2px; flex: 1; min-width: 0;">'
            f'<span style="font-size: 14px; font-weight: 600; color: {C["INK"]};">{memo} <span style="font-weight: 500; color: {C["INK3"]};">×{count}</span></span>'
            f'<span style="font-size: 12px; color: {C["INK2"]};">{total}</span></div>{chip}'
            f'{icon("up" if expanded else "down", 16, C["INK4"], 2)}</div>')


def sub_row(date, amount, on, last=False):
    bb = '' if last else f'border-bottom: 1px solid {C["LINE_ROW"]};'
    return (f'<div style="display: flex; align-items: center; gap: 10px; height: 40px; padding-left: 8px; {bb}">{check(on)}'
            f'<span style="flex: 1; font-size: 13px; color: {C["INK2"]};">{date}</span>'
            f'<span style="font-size: 13px; font-weight: 600; color: {C["INK"] if on else C["DIS"]};">{won(amount)}</span></div>')


def single_row(memo, amount, reco=None, chosen=False, last=False):
    bb = '' if last else f'border-bottom: 1px solid {C["LINE_ROW"]};'
    if reco:
        chip = (f'<span style="display: inline-flex; align-items: center; gap: 5px; height: 30px; padding: 0 10px; border-radius: 8px; '
                f'{"background: " + C["BRAND_SOFT"] + "; border: 1.5px solid " + C["BRAND"] + ";" if chosen else "background: " + C["SURF"] + "; border: 1px solid " + C["BORDER"] + ";"} '
                f'font-size: 12px; font-weight: 600; color: {C["INK"]}; white-space: nowrap;"><span style="width: 8px; height: 8px; border-radius: 99px; background: {CAT[reco]};"></span>{reco}'
                + ('' if chosen else f'<span style="font-size: 10.5px; font-weight: 500; color: {C["INK3"]};">추천</span>') + '</span>')
    else:
        chip = f'<span style="font-size: 12.5px; font-weight: 600; color: {C["BRAND"]}; white-space: nowrap;">분류 고르기 &rsaquo;</span>'
    return (f'<div style="display: flex; align-items: center; gap: 10px; height: 52px; {bb}">'
            f'<div style="display: flex; flex-direction: column; gap: 2px; flex: 1; min-width: 0;">'
            f'<span style="font-size: 14px; font-weight: 600; color: {C["INK"]};">{memo}</span>'
            f'<span style="font-size: 12px; color: {C["INK2"]};">{won(amount)}</span></div>{chip}</div>')


# 분류 안 함 7건 = 내역 장 LedgerV5(gen_screens.LEDGER_V5)의 분류 안 함 행과 같은 자료다 — 합 32,000원(히어로 각주 NOTE_A · EtcSubline · MonthlyCloseV5 와 같은 값).
# 9/1 커피 · 9/3 간식 · 9/4 커피 · 9/5 커피 · 9/5 버스 · 9/5 메모 없음(제목 `분류 안 함 기록`) 3,000 · 9/8 편의점 6,500. 오늘(9/8) 커피는 카페/간식으로 분류된 기록이라 여기 없다.
# gen_screens 는 import 하면 장을 다시 쓰므로 글자로 둔다 — 그쪽 분류 안 함 행이 바뀌면 여기도 맞춘다(아래 assert 가 건수 · 합계를 지킨다).
CLS_COFFEE = [(1, 4500, True), (4, 4500, True), (5, 4500, False)]            # (날짜, 금액, 고름) — 같은 메모 `커피` 묶음 · 5일은 `제외` 본보기
CLS_SINGLE = [('간식', 4500, '식비'), ('버스', 4500, None), ('편의점', 6500, None), ('', 3000, None)]      # (메모 · 없으면 `분류 안 함 기록`, 금액, 추천 | None = `분류 고르기 ›`)
CLS_COUNT = len(CLS_COFFEE) + len(CLS_SINGLE)
CLS_PICKED = sum(1 for _, _, on in CLS_COFFEE if on)                         # 추천을 눌러 정한 것은 커피 묶음뿐(간식의 `식비 추천`은 아직 안 누름)
assert CLS_COUNT == 7 and sum(a for _, a, _ in CLS_COFFEE) + sum(a for _, a, _ in CLS_SINGLE) == 32_000      # `분류 안 함 7건` · `분류 안 한 32,000원`

classify_body = (
    f'<div style="display: flex; justify-content: center; padding: 9px 0 0; flex-shrink: 0;"><span style="width: 38px; height: 4px; border-radius: 99px; background: {C["BORDER"]};"></span></div>'
    f'<div style="display: flex; align-items: flex-start; justify-content: space-between; gap: 10px; padding: 12px 18px 14px; border-bottom: 1px solid {C["LINE_SOFT"]}; flex-shrink: 0;"><div style="min-width: 0;">'
    f'<h2 style="margin: 0; font-size: 18px; font-weight: 700; letter-spacing: -0.025em; color: {C["INK"]};">분류하기 · {CLS_COUNT}건</h2>'
    f'<p style="margin: 4px 0 0; font-size: 12.5px; line-height: 1.45; color: {C["INK3"]};">같은 메모끼리 묶었어요. 추천은 눌러야 정해지고, 정한 것만 저장돼요.</p></div>'
    f'<span style="font-size: 13px; font-weight: 600; color: {C["INK2"]}; padding-top: 4px; flex-shrink: 0; white-space: nowrap;">닫기</span></div>'
    f'<div style="flex: 1; min-height: 0; overflow: hidden; padding: 6px 18px 0; display: flex; flex-direction: column;">'
    + group_row('커피', len(CLS_COFFEE), sum(a for _, a, on in CLS_COFFEE if on), '카페/간식', chosen=True, expanded=True, picked=CLS_PICKED)
    + f'<div style="background: {C["INSET"]}; border-radius: 0 0 12px 12px; padding: 0 10px 2px; margin-bottom: 2px;">'
    + ''.join(sub_row(f'9월 {d}일' + ('' if on else ' · 제외'), a, on, last=(i == len(CLS_COFFEE) - 1)) for i, (d, a, on) in enumerate(CLS_COFFEE))
    + '</div>'
    + ''.join(single_row(m or '분류 안 함 기록', a, reco, chosen=False, last=(i == len(CLS_SINGLE) - 1)) for i, (m, a, reco) in enumerate(CLS_SINGLE))
    + '</div>'
    f'<div style="padding: 12px 18px 20px; border-top: 1px solid {C["LINE_SOFT"]}; flex-shrink: 0; display: flex; flex-direction: column; gap: 8px;">'
    + btn(f'{CLS_PICKED}건 저장', 'primary', h=52, radius=14, size=16)
    + f'<p style="margin: 0; text-align: center; font-size: 11.5px; line-height: 1.5; color: {C["INK3"]};">나머지 {CLS_COUNT - CLS_PICKED}건은 분류 안 함으로 남아요</p></div>')
w('ClassifySheet', sheet_frame(classify_body, scrim_text='배경을 눌러 닫기'))


# ══════════════ 7. 히어로 이력 부족 — 홈 ══════════════
def hero_insufficient(second='예상에 사용할 지난 소비 기록이 아직 없어요'):
    return hero(
        eyebrow_row('이번 달 기록한 소비', '')
        + f'<div style="display: flex; align-items: flex-end; justify-content: space-between; gap: 10px; margin-top: 8px;">'
        f'<div style="display: flex; align-items: baseline; gap: 2px;"><span style="font-size: 54px; font-weight: 700; letter-spacing: -0.045em; line-height: 1; color: {C["INK"]};">5,000</span>'
        f'<span style="font-size: 25px; font-weight: 600; letter-spacing: -0.02em; color: {C["INK2"]};">원</span></div>'
        f'<div style="display: flex; flex-direction: column; align-items: flex-end; gap: 1px; padding-bottom: 4px;">'
        f'<span style="font-size: 11px; font-weight: 500; color: {C["INK3"]};">월급의</span>'
        f'<span style="font-size: 14px; font-weight: 600; color: {C["INK"]};">0.1%</span></div></div>'
        + f'<div style="display: flex; align-items: baseline; justify-content: space-between; gap: 10px; margin-top: 5px;">'
        f'<span style="font-size: 13px; font-weight: 500; color: {C["INK2"]};">아직 기록하지 않은 소비는 포함되지 않았어요</span></div>'
        f'<div style="font-size: 12px; line-height: 1.45; color: {C["INK3"]}; margin-top: 3px;">{second}</div>'
        + f'<div style="margin-top: 15px;"><div style="position: relative; height: 10px; border-radius: 99px; background: {C["TRACK"]}; overflow: visible;">'
        f'<div style="position: absolute; left: 60%; top: -5px; width: 2px; height: 20px; border-radius: 2px; background: {C["INK"]};"></div></div>'
        f'<div style="position: relative; height: 15px; margin-top: 5px;"><span style="position: absolute; left: 0; font-size: 11px; color: {C["INK3"]};">0%</span>'
        f'<span style="position: absolute; left: 60%; transform: translateX(-50%); font-size: 11px; font-weight: 600; color: {C["INK"]}; white-space: nowrap;">내 목표 60%</span>'
        f'<span style="position: absolute; right: 0; font-size: 11px; color: {C["INK3"]};">100%</span></div></div>'
        + metric3([('월 실수령', '360', '만원', None), ('월말 예상', '—', '', C["INK4"]), ('월말 예상 여유', '—', '', C["INK4"])])
        + f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 10px; margin-top: 12px;">'
        f'<span style="font-size: 11px; line-height: 1.4; color: {C["INK3"]};">실수령 급여 기준 · 부수입·저축 이체·대출상환 제외</span>'
        f'<span style="font-size: 11.5px; font-weight: 600; color: {C["BRAND"]}; white-space: nowrap;">기준 조정 &rsaquo;</span></div>')   # 버튼 없음(2026-09-22) — 기록은 달력 날짜로


# 예상 기준 통과 전 다음 안내는 사실 안내만(계획 §3-4) — '며칠 더 기록하면 …' 같은 '시간이 지나면' 문장은 쓰지 않는다.
first_guide = guidance('info', '다음 안내', '기록한 소비 5,000원', '아직 기록하지 않은 소비는 포함하지 않았어요', None)
# 달력 — 앱을 9월 5일에 처음 연 사람: 2~4일은 시작일 이전(— 없는 옅은 빈 칸), 5~7일은 회색 —, 오늘 칸 5,000. 확인할 내용 없음.
FIRST_SINCE = 5
NO_RECORD = ('—', False, False, False)
calendar_first = calendar_card(False, since=FIRST_SINCE, review=0, status='오늘 1건 5,000원',
                               states={5: NO_RECORD, 6: NO_RECORD, 7: NO_RECORD, TODAY: (fmt_sum(5_000), False, False, False)})
assert calendar_first.count('>—<') == 3 and calendar_first.count('>5,000<') == 1 and '확인할 내용' not in calendar_first
limit_first = (s1.limit_block.replace('남은 한도 104만원', '남은 한도 216만원').replace('inset: 0 48.1% 0 0', 'inset: 0 99.8% 0 0')
               .replace('하루 47,270원', '하루 97,950원'))      # 1단계 장 — 라벨은 v3 그대로 `하루 …`
assert limit_first.count('하루 97,950원') == 1 and '앞으로 하루' not in limit_first and limit_first.count('남은 한도 216만원') == 1
# 머리줄 종 배지 — 이 사람(9월 5일 첫 실행 · 커피 5,000원 한 건)의 알림은 2건이다(InsufficientElsewhere ⑦ `알림 2건 · 머리줄 종의 숫자도 같은 2`).
# 다른 홈 장(Main 의 사람)은 3 그대로 — 이 장에서만 바꾼다.
BELL_3 = 'border: 2px solid #EDF0F7;">3</span>'
assert s1.header.count(BELL_3) == 1
header_first = s1.header.replace(BELL_3, BELL_3.replace('>3<', '>2<'))
assert header_first.count('border: 2px solid #EDF0F7;">2</span>') == 1 and BELL_3 not in header_first
w('HeroInsufficient', frame(
    f'\n  {header_first}\n\n'
    f'  <div style="flex: 1; min-height: 0; display: flex; flex-direction: column; gap: 9px; padding: 0 14px; overflow: hidden;">\n\n'
    f'    {hero_insufficient()}\n\n    {calendar_first}\n\n    {first_guide}\n\n    {limit_first}\n\n  </div>\n\n'
    f'  {bottomnav(0)}\n'))


# ══════════════ 8. 홈 맨 위 카드에 붙는 작은 안내 줄 — 구현 참고 장 ══════════════
# 앱 화면이 아니다. 왼쪽에 온전한 카드 한 장(②의 경우)을 두어 안내 줄 자리를 표시하고, 오른쪽에는 카드의 아랫부분
# (기준 줄 + 안내 줄)만 네 경우로 놓는다. 히어로 버튼은 2026-09-22에 뺐으므로 안내 줄이 카드의 마지막 줄이다. 기준 줄이 한 줄에 들어가는 실제 폭을 지키려고 견본은 카드 폭 362 그대로 2 × 2.
HERO_BASIS = '<div style="display: flex; align-items: center; justify-content: space-between; gap: 10px; margin-top: 12px;">'
assert s1.hero_block.count(HERO_BASIS) == 1 and '소비 기록하기' not in s1.hero_block and s1.hero_block.endswith('</div>')
hero_top = s1.hero_block[:s1.hero_block.index(HERO_BASIS)]                       # 카드 여는 태그 ~ 세 칸 요약
_tail = s1.hero_block[s1.hero_block.index(HERO_BASIS):]
hero_tail = _tail[:_tail.rstrip().rindex('</div>')].rstrip()                     # 기준 줄(카드 닫는 태그 앞까지)
NOTE_STYLE = f'font-size: 11px; line-height: 1.4; color: {C["INK3"]};'


def hero_tail_with(notes, marked=False):
    """기준 줄 아래에 안내 줄을 붙인다. marked = 안내 줄 자리를 옅은 파란 테두리와 알약으로 표시(왼쪽 온전한 카드용)."""
    if marked:
        # 알약은 안내 줄의 빈 오른쪽 끝에 세로 가운데로 — 윗줄의 `기준 조정 ›`를 가리지 않는다
        pill = (f'<span style="position: absolute; top: 50%; right: 4px; transform: translateY(-50%); height: 17px; padding: 0 7px; border-radius: 99px; '
                f'background: {C["INK"]}; color: #FFFFFF; font-size: 10.5px; font-weight: 700; display: inline-flex; align-items: center; white-space: nowrap;">안내 줄</span>')
        extra = (f'<div style="position: relative; margin-top: 4px; border-radius: 4px; box-shadow: 0 0 0 3px rgba(53,86,230,.16);">'
                 + ''.join(f'<div style="{NOTE_STYLE}">{n}</div>' for n in notes) + pill + '</div>')
    else:
        extra = ''.join(f'<div style="{NOTE_STYLE} margin-top: 4px;">{n}</div>' for n in notes)
    return hero_tail + extra


def hero_fragment(notes):
    """카드의 아랫부분만 — 위 테두리 없이 아래 모서리만 둥글게 해서 잘라 낸 조각으로 보이게."""
    return (f'<div style="background: {C["SURF"]}; border: 1px solid {C["LINE"]}; border-top: none; border-radius: 0 0 20px 20px; padding: 4px 16px 16px; '
            f'box-shadow: 0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24);">{hero_tail_with(notes)}</div>')


NOTE_A = '분류 안 한 32,000원은 적은 금액 그대로 예상에 더했어요'
NOTE_B = '분류 안 한 지난 기록도 평균에 넣었어요. 분류하면 다시 계산해요.'
NOTE_C = '지난 고정비 기록을 보고 앞으로 나갈 돈도 예상했어요'
NOTE_D = '기록이 한 달치뿐이라 예상이 달라질 수 있어요'
FOOTNOTE_CASES = [
    (1, '덧붙일 말이 없을 때', '기준 조정 줄로 카드가 끝납니다. 지금 홈과 같습니다.', []),
    (2, '이번 달에 분류 안 한 기록이 있을 때', '안내가 한 줄 붙습니다.', [NOTE_A]),
    (3, '지난달 기록으로 예상을 계산한 날', '안내가 두 줄 붙습니다. 이번 달 기록만으로 계산한 날에는 나오지 않습니다.', [NOTE_B, NOTE_C]),
    (4, '기록이 한 달치뿐일 때', '안내가 한 줄 붙습니다.', [NOTE_D])]
footnote_left = (
    f'<div style="width: 362px; flex-shrink: 0; display: flex; flex-direction: column; gap: 8px;">{hero_top}{hero_tail_with([NOTE_A], marked=True)}</div>'
    f'<p style="margin: 2px 2px 0; font-size: 12px; line-height: 1.5; color: {C["INK3"]};">안내 줄은 '
    f'<b style="font-weight: 600; color: {C["INK2"]};">기준 조정 줄 아래, 카드의 맨 끝</b>에 붙습니다. 그림은 2번의 경우입니다.</p></div>')
footnote_foot = (f'<p style="margin: 10px 2px 0; font-size: 12px; line-height: 1.6; color: {C["INK3"]}; max-width: 900px;">오른쪽 견본은 카드의 '
                 f'<b style="font-weight: 600; color: {C["INK2"]};">아랫부분</b>만 잘라 보여 줍니다. 카드의 나머지는 네 경우 모두 같고, 안내 줄이 붙은 만큼만 카드가 길어집니다. '
                 f'안내 문구는 기획 문서 5-3의 문구 표와 같아야 합니다.</p>')
w('HeroFootnotes', spec_frame(
    1200, 640, '홈 맨 위 카드에 붙는 작은 안내 줄',
    '예상 소비를 계산한 방식에 덧붙일 말이 있을 때만 기준 조정 줄 아래에 회색 글이 한두 줄 붙습니다.',
    f'<div style="display: flex; gap: 32px; align-items: flex-start;">{footnote_left}'
    f'{case_grid([(case_cap(n, t, d), hero_fragment(notes)) for n, t, d, notes in FOOTNOTE_CASES])}</div>{footnote_foot}', sub_w=760), keep_all=True)


# ══════════════ 9. 홈 달력 — 접힘(최근 7일 스트립) · 펼침(월 달력) · 칸 상태 · 폭/글자 크기 ══════════════
# 펼침은 어느 폭·어느 글자 크기에서도 **월 달력(7열 그리드)** 이다 — 날짜를 세로로 늘어놓은 목록으로 자동 대체하지 않는다(7판).
# 2026년 9월: 1일 화요일 · 30일 · 5주. 오늘 8일(화). 2026년 8월: 1일 토요일 · 31일 · 6주.
# 칸 숫자 = 그날 소비 합계(고정비 포함 · 이체 제외). 표기는 앱 formatSum과 같다(1만 미만 원 단위 · 1만 이상 만 단위 한 자리 · 소수 첫 자리 0은 뗀다).
# 자료 · 칸 · 접힘/펼침 카드 · 상태 줄은 gen_calendar.py 로 옮겼다(gen_v4 · gen_v4_stocks 도 쓰도록). 여기는 홈에 얹는 틀과 장만 남는다.


def limit_card(forward, two_lines=False):
    """홈 한도 카드. forward=True 면 v5 · 3단계 라벨 `앞으로 하루 47,270원`, False 면 그 전 단계의 v3 라벨 `하루 47,270원` 그대로
    (계획 §9-3 · §10 — 출시 순서 v3 → v4-1 → v5-1 → v5-2 → v4-2 → v5-3). 오른쪽 `남은 한도 104만원`. 첫 줄 왼쪽 덩어리는 nowrap.
    two_lines = 360 폭에서 `앞으로 하루 …`가 한 줄에 안 들어갈 때 — 라벨을 줄이지 않고 `남은 한도`를 둘째 줄로 내린다(첫 줄 오른쪽에는 › 만 남는다)."""
    lim_left = '<span style="font-size: 13.5px; font-weight: 600; color: #101828;">이번 달 한도 '
    remain = '<span style="font-size: 13.5px; font-weight: 600; color: #0F7B47; white-space: nowrap; flex-shrink: 0;">남은 한도 104만원</span>'
    bar_open = '<div style="position: relative; height: 8px; border-radius: 99px; background: #E8ECF5; margin-top: 9px; overflow: hidden;">'
    src = s1.limit_block
    assert src.count(lim_left) == 1 and src.count('하루 47,270원') == 1 and src.count(remain) == 1 and src.count(bar_open) == 1
    html = src.replace(lim_left, lim_left.replace('color: #101828;', 'color: #101828; white-space: nowrap;'))
    if forward:
        html = html.replace('하루 47,270원', '앞으로 하루 47,270원')
    assert html.count('앞으로 하루') == (1 if forward else 0) and html.count('하루 47,270원') == 1
    if two_lines:
        html = html.replace(remain, '').replace(bar_open, f'<div style="margin-top: 3px;">{remain}</div>\n      ' + bar_open)
    return html


def limit_forward(two_lines=False):
    """v5 · 3단계 뒤의 한도 카드 `앞으로 하루 47,270원` — LimitCardCases(gen_v5_screens)가 쓴다. 이 파일의 1 · 2단계 장은 쓰지 않는다."""
    return limit_card(True, two_lines)


def limit_stage12():
    """v5 · 1 · 2단계 홈의 한도 카드 — 라벨은 v3 그대로 `하루 47,270원`(HomeConfigured · HomeStocksOff · InsufficientElsewhere 와 같다).
    `하루 47,270원`은 360 폭에서도 `남은 한도 104만원`과 한 줄에 들어가므로 둘째 줄로 내리지 않는다."""
    return limit_card(False)


def home_expanded(width=390, pad=14, month='sep', pressed=None, limit=True):
    peek = f'<div style="height: 22px; background: {C["SURF"]}; border: 1px solid {C["LINE"]}; border-top: none; border-radius: 0 0 20px 20px; flex-shrink: 0; opacity: .55;"></div>'
    lim = ('\n\n    ' + limit_stage12()) if limit else ''
    return frame(
        f'\n  <div style="flex: 1; min-height: 0; display: flex; flex-direction: column; gap: 9px; padding: 0 14px; overflow: hidden;">\n\n'
        f'    {peek}\n\n    {calendar_card(True, pressed=pressed, pad=pad, month=month)}\n\n    {s1.guide_block}{lim}\n\n  </div>\n\n'
        f'  {bottomnav(0)}\n', w=width)


# 기본 5카드의 나머지 두 장은 v3 시안에서 그대로 잘라 온다 — 대표 목적지(Main) · 또래와 내 페이스(HomeScroll).
goal_block = s1.cut(s1.main_src, s1.M_GOAL, s1.M_LIMIT).rstrip()
assert goal_block.count('대표 목적지') == 1 and goal_block.count('<div') == goal_block.count('</div>')
_scroll_src = (OUT / 'HomeScroll.dc.html').read_text(encoding='utf-8')
P_PEER = '<div style="background: #FFFFFF; border: 1px solid #E3E8F1; border-radius: 18px; padding: 14px; flex-shrink: 0;">'
P_ROWS = '<div style="background: #FFFFFF; border: 1px solid #E3E8F1; border-radius: 18px; padding: 4px 14px; flex-shrink: 0;">'
assert _scroll_src.count(P_PEER) == 1 and _scroll_src.count(P_ROWS) == 1
peer_block = s1.cut(_scroll_src, P_PEER, P_ROWS).rstrip()
assert peer_block.count('또래와 내 페이스') == 1 and peer_block.count('<div') == peer_block.count('</div>') and '순자산 대비 소비' not in peer_block

# 홈 · 접힘 — 히어로 그대로, 첫 카드가 달력(최근 7일). 그 아래로 다음 안내 · 이번 달 한도 · 대표 목적지가 이어진다(화면 아래에서 잘림).
w('HomeCalendarStrip', frame(
    f'\n  {s1.header}\n\n'
    f'  <div style="flex: 1; min-height: 0; display: flex; flex-direction: column; gap: 9px; padding: 0 14px; overflow: hidden;">\n\n'
    f'    {s1.hero_block}\n\n    {calendar_card(False)}\n\n    {s1.guide_block}\n\n    {limit_stage12()}\n\n    {goal_block}\n\n  </div>\n\n'
    f'  {bottomnav(0)}\n'))

# 홈 · 기본 5카드 전체(2단계 검토물 '기본 구성 홈 before/after'의 after) — 스크롤 전체 길이를 한 장에.
# 달력 · 다음 안내 · 이번 달 한도 · 대표 목적지 · 또래와 내 페이스(`순자산 대비 소비`는 기본에서 빠짐). v4-2 전이라 옛 5탭. 한도 라벨은 3단계 전이라 v3 그대로 `하루 47,270원`(limit_stage12 · 같은 페이지의 다른 홈 장과 같다).
HOME_DEFAULT_H = 1330
w('HomeDefaultScroll', frame(
    f'\n  {s1.header}\n\n'
    f'  <div style="flex: 1; min-height: 0; display: flex; flex-direction: column; gap: 9px; padding: 0 14px 14px; overflow: hidden;">\n\n'
    f'    {s1.hero_block}\n\n    {calendar_card(False)}\n\n    {s1.guide_block}\n\n    {limit_stage12()}\n\n    {goal_block}\n\n    {peer_block}\n\n  </div>\n\n'
    f'  {bottomnav(0)}\n', h=HOME_DEFAULT_H))

# 홈 · 펼침 — 월 달력. 아래로 조금 스크롤한 상태(히어로 아랫단이 위에 남음). 3일 칸을 누른 순간(눌림 링) → 다음 장 하루 시트.
w('HomeCalendar', home_expanded(pressed=3))
# 같은 화면 360px — 가장 흔한 안드로이드 폭. 카드 좌우 패딩 10, 칸 폭 44.6. 목록으로 바뀌지 않는다.
w('HomeCalendar360', home_expanded(width=360, pad=10))
# ‹ 로 지난달(8월)을 보는 상태 — 6주. › 와 `이번 달로`가 살아나고, 칸을 누르면 그 날짜 하루 시트.
w('HomeCalendarPrev', home_expanded(month='aug', limit=False))


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
    (5, '오늘', '옅은 파란 칸에 굵은 날짜', '누르면 금액 입력부터 시작해요'),
    (6, '아직 오지 않은 날', '날짜만 옅게 보여요', '눌러도 열리지 않아요'),
    (7, '지난달 날짜', '첫 주의 8월 30·31일 · 기록이 옅게 보여요', '누르면 그 날짜 기록 창이 열려요'),
    (8, '다음 달 날짜', '10월 1~3일 · 아직 오지 않은 날은 날짜만 옅게', '누를 수 없어요 · 이미 지난 날이면 7번처럼 기록이 옅게 보여요'),
    (9, '빈 칸', '앱을 쓰기 시작한 날보다 앞선 날 · — 없이 날짜만 옅게', '누르면 그 날짜 기록 창이 열려요 · 밀린 숙제처럼 보이지 않게 비워 둬요'),
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
                       today=(is_sep and d == TODAY and kind != 'out'), future=(is_sep and d > TODAY))
            n = MARKS.get((m, d))
            cs.append(f'<div style="position: relative; min-width: 0;">{c_}{mark(n, True) if n else ""}</div>')
        rows.append(f'<div style="display: grid; grid-template-columns: repeat(7, minmax(0, 1fr)); border-top: 1px solid {C["LINE_SOFT"]}; padding: 2px 0;">{"".join(cs)}</div>')
    grid = (f'<div style="display: grid; grid-template-columns: repeat(7, minmax(0, 1fr)); margin-top: 8px; padding-bottom: 5px;">{wd}</div>'
            f'<div style="display: flex; flex-direction: column; border-bottom: 1px solid {C["LINE_SOFT"]};">{"".join(rows)}</div>')
    return card(month_bar('2026년 9월', prev_on=True, next_on=False) + grid
                + status_rows(text=f'9월 기록한 소비 {SEP_TOTAL:,}원 · 오늘 4건 37,000원'), pad='13px 14px 13px')


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
             f'6일 칸은 안 쓴 날로 표시했고 이체도 있어서 0과 이체가 같이 보입니다. 표시 없이 이체만 있는 날은 숫자 없이 이체만 보입니다. 칸을 누르는 순간에는 파란 테두리가 생깁니다(홈 · 달력 펼침 장).</p>')

# 9번(시작일 이전)은 왼쪽 9월 달력에 없는 상태라(그 사람은 8월에도 기록이 있다) 다른 사람의 접힌 줄을 따로 보여 준다 — HeroInsufficient 와 같은 달력.
# 번호 자리: 카드 안쪽 332를 7칸(44)이 space-between 으로 나눠 칸 간격 4 → 3일 칸(둘째)의 오른쪽 끝 = 1 + 14 + 48 + 44 = 107.
since_strip = (f'<div style="position: relative;">{calendar_first}'
               + mark(9, pos="position: absolute; top: 38px; left: 93px;") + '</div>')


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
    1330, 820, '달력 칸 읽는 법', '칸의 숫자는 그날 소비 합계입니다(고정비 포함 · 이체 제외). 왼쪽 달력의 번호를 가운데에서 찾으세요.',
    f'<div style="display: flex; gap: 28px; align-items: flex-start;">'
    f'<div style="width: 362px; flex-shrink: 0;">{marked_calendar()}</div>'
    f'<div style="width: 490px; flex-shrink: 0;">{cell_guide}{cell_foot}</div>'
    f'<div style="width: 362px; flex-shrink: 0; display: flex; flex-direction: column; gap: 22px;">'
    + sample(362, '앱을 9월 5일에 처음 연 사람의 달력', '접힌 최근 7일 줄 · 2~4일은 쓰기 시작한 날보다 앞이라 비어 있어요', since_strip)
    + fmt_card + '</div></div>', sub_w=760), keep_all=True)


# 폭과 글자 크기 — 어디서나 월 달력. 320px은 칸 39.4 × 56, 큰 글자는 칸 높이 72. 날짜 목록은 자동 대체가 아니라 큰 글자에서 고르는 보기.
LIST_ROWS = [('9월 8일 화 · 오늘', '37,000원', False), ('9월 7일 월', '—', False), ('9월 6일 일', '0원 · 이체', False),
             ('9월 5일 토', '12,000원', True), ('9월 4일 금', '4,500원', True)]
EMPTY13 = '<span style="width: 13px;"></span>'


def list_amount(a):
    if a == '—':
        return f'<span style="font-size: 16px; font-weight: 500; color: {C["INK3"]};">{a}</span>'
    col = C["INK2"] if a.startswith('0원') else C["INK"]
    return f'<span style="font-size: 16px; font-weight: 600; color: {col};">{a}</span>'


list_view = card(
    month_bar('2026년 9월', prev_on=True, next_on=False, large=True)
    + f'<div style="margin-top: 8px;">'
    + ''.join(f'<div style="display: flex; align-items: center; gap: 10px; min-height: 48px; border-top: 1px solid {C["LINE_ROW"]};"><span style="flex: 1; font-size: 16px; color: {C["INK"]};">{d}</span>{list_amount(a)}{icon("check", 14, C["INK2"], 2.8) if c else EMPTY13}</div>'
              for d, a, c in LIST_ROWS)
    + '</div>'
    + list_link(True).replace('목록으로 보기', '달력으로 보기'),
    pad='13px 14px 4px')


cal320 = calendar_card(True, pad=8).replace('2026년 9월', '9월').replace('min-width: 94px', 'min-width: 44px')
cal_large = calendar_card(True, large=True, with_list_link=True)
bar_prev320 = card(month_bar('8월', prev_on=False, next_on=True, back_pill=True, pill_below=True, label_w=44)
                   + month_grid('aug', weeks=slice(0, 1)), pad='13px 8px 13px')          # 머리 부분만 떠 있지 않게 요일 줄과 첫 주를 붙인다
cal_large320 = card(month_bar('8월', prev_on=False, next_on=True, back_pill=True, large=True, label_w=52)
                    + month_grid('aug', large=True, tight=True, weeks=slice(0, 3)), pad='13px 8px 13px')

# 접힌 최근 7일 줄 — 320px: 칸 44 × 56 그대로 · 카드 좌우 패딩 8 · 카드 안 가로 스크롤(오늘이 오른쪽 끝에서 시작, 왼쪽 칸이 잘려 보인다).
strip320 = calendar_card(False, pad=8, scroll=True)
# 큰 글자: 접힌 줄도 칸 그대로 — 칸 높이 72 · 날짜 14.5 · 합계는 칸 폭 44(47 미만)라 12 · 금액을 숨기지 않는다 · 상태 줄 14.5.
strip_large = calendar_card(False, large=True)

# 구현 수치는 견본 설명에 흩지 않고 맨 아래 한 단락으로 모은다.
sizes_memo = (f'<div style="margin-top: 24px; display: flex; flex-direction: column; gap: 4px;">'
              f'<div style="font-size: 12px; font-weight: 600; color: {C["INK2"]};">구현 메모</div>'
              f'<p style="margin: 0; font-size: 12px; line-height: 1.6; color: {C["INK3"]};">가장 좁은 폰은 화면 너비 320px, 달력 칸은 39 × 56입니다. '
              f'큰 글자에서는 칸 높이가 72가 됩니다. 좁은 폰 + 큰 글자에서는 금액 글자 크기를 12로 줄입니다. '
              f'지난달을 볼 때 &lsquo;이번 달로&rsquo; 버튼은 제목 줄 바로 아래 줄 오른쪽에 둡니다. '
              f'접힌 최근 7일 줄의 칸은 어느 폭에서나 44 × 56입니다. 가장 좁은 폰에서는 일곱 칸(308)이 카드 안쪽(276)에 다 들어가지 않아 카드 좌우 여백을 8로 줄이고 줄을 옆으로 밀어 봅니다. '
              f'처음에는 오늘이 오른쪽 끝에 보입니다. 큰 글자에서는 접힌 줄도 칸 높이 72 · 날짜 14.5이고, 칸 폭이 44라 금액 글자는 12입니다.</p></div>')

sizes_row1 = ('<div style="display: flex; gap: 36px; align-items: flex-start;">'
              + sample(292, '가장 좁은 폰', '달력 그대로. 제목은 9월만 적어요', cal320)
              + sample(362, '글자를 크게 쓰는 사람', '달력 그대로. 칸이 높아지고 글자가 커져요', cal_large)
              + sample(362, '목록으로 보기를 고르면', '스스로 고른 사람에게만. 저절로 바뀌지 않아요', list_view)
              + '</div>')
sizes_row2 = ('<div style="display: flex; gap: 36px; align-items: flex-start; margin-top: 26px;">'
              + '<div style="width: 292px; flex-shrink: 0; display: flex; flex-direction: column; gap: 24px;">'
              + sample(292, '가장 좁은 폰에서 지난달을 볼 때', '&lsquo;이번 달로&rsquo; 버튼은 제목 아랫줄로 내려가요', bar_prev320)
              + sample(292, '가장 좁은 폰 · 접어 둔 달력', '칸을 줄이지 않아요. 오늘부터 보이고 옆으로 밀어 봐요', strip320)
              + '</div>'
              + sample(292, '좁은 폰 + 큰 글자', '금액 글자를 조금 줄여 71.2만도 잘리지 않아요', cal_large320)
              + sample(362, '글자를 크게 쓰는 사람 · 접어 둔 달력', '칸이 높아지고 글자가 커져요. 금액은 숨기지 않아요', strip_large)
              + '</div>')

w('CalendarGridSizes', spec_frame(
    1150, 1490, '달력을 펼치면 어디서나 월 달력', '화면이 좁아도, 글자를 크게 써도 날짜를 세로로 늘어놓은 목록으로 바뀌지 않습니다. 접어 둔 최근 7일 줄도 칸 그대로입니다.',
    sizes_row1 + sizes_row2 + sizes_memo))
