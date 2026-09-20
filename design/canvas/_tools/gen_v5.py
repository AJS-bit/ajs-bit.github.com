# -*- coding: utf-8 -*-
"""v5 · 1단계 아트보드 — 하루 시트(안전하고 쉬운 한 건의 기록).

plan/v5-calendar.md §3-4 · §4 · §5-4 · §10 1단계 검토물: 시트 기본(키보드 열림) · 목록 우선 · 수정 모드 ·
완료 카드 · 확인/겹침 · 분류하기 · 히어로 이력 부족 · 360px · 히어로 조건부 각주 조합. 라이트를 만들고
darken()으로 다크 짝을 쓴다. 홈은 Main.dc.html을 잘라 쓴다(히어로 1px 불변 원칙).

키보드는 그리지 않는다 — 시스템 숫자 키보드가 차지하는 자리를 빈 판으로만 표시한다(가짜 키 없음).

    python3 gen_v5.py
"""
import re
import gen_common
from gen_common import *
import gen_v4 as s1                     # cut · header · hero_block · guide_block · limit_block · OUT
from gen_v4_stocks import nav_v4        # (import 부작용: 2~5단계 파일도 다시 쓴다 — 멱등)
from darken import darken

OUT = s1.OUT
V5 = ['HomeCalendarStrip', 'HomeCalendar', 'HomeCalendar360', 'HomeCalendarPrev', 'DaySheet', 'DaySheetList', 'DaySheetEdit', 'DoneCard', 'DaySheetConfirm',
      'ClassifySheet', 'HeroInsufficient', 'DaySheet360', 'HeroFootnotes', 'CalendarCells', 'CalendarGridSizes']

KB_H = 280          # 시스템 숫자 키보드가 덮는 높이(자리만 표시)
SCRIM_H = 60


def w(name, body, keep_all=False):
    light = doc(body, keep_all=keep_all)
    (OUT / f'{name}.dc.html').write_text(light, encoding='utf-8')
    (OUT / f'Dark{name}.dc.html').write_text(darken(light), encoding='utf-8')
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
    tail = (f'<span style="width: 7px; height: 7px; border-radius: 99px; background: {CAT[cat]}; flex-shrink: 0;" title="{cat}"></span>'
            if cat else f'<span style="font-size: 11px; color: {C["INK3"]};">분류 안 함</span>')
    return (f'<span style="display: inline-flex; align-items: center; gap: 7px; height: 32px; padding: 0 11px; border-radius: 8px; background: {C["INSET"]}; '
            f'font-size: 12px; font-weight: 500; color: {C["INK"]}; white-space: nowrap;">{memo} <span style="font-weight: 600;">{amount:,}</span>{tail}</span>')


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


def sheet_frame(inner, w_=390, keyboard=False, scrim_text='배경을 눌러 닫기 · 저장 전 내용은 앱 재시작 시 사라져요'):
    kb = kb_block(w_) if keyboard else ''
    return (f'<div style="width: {w_}px; height: 844px; background: #2A3245; color: {C["INK"]}; display: flex; flex-direction: column; overflow: hidden; position: relative; font-variant-numeric: tabular-nums;">'
            f'{scrim_line(scrim_text)}'
            f'<div style="flex: 1; min-height: 0; background: {C["SURF"]}; border-radius: 26px 26px 0 0; display: flex; flex-direction: column; overflow: hidden;">{inner}</div>{kb}</div>')


def save_btn(label='저장'):
    return btn(label, 'primary', h=52, radius=14, size=16)


def links_row():
    return (f'<div style="display: flex; align-items: center; gap: 14px;">'
            f'<span style="font-size: 12.5px; font-weight: 600; color: {C["BRAND"]};">저축·투자로 기록 &rsaquo;</span>'
            f'<span style="font-size: 12.5px; font-weight: 600; color: {C["BRAND"]};">대출상환으로 기록 &rsaquo;</span></div>')


def tx_row(cat, memo, amount, last=False):
    bb = '' if last else f'border-bottom: 1px solid {C["LINE_ROW"]};'
    if cat:
        left = (f'<span style="display: inline-flex; align-items: center; gap: 6px; width: 96px; flex-shrink: 0;"><span style="width: 8px; height: 8px; border-radius: 99px; background: {CAT[cat]};"></span>'
                f'<span style="font-size: 12.5px; font-weight: 500; color: {C["INK2"]}; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">{cat}</span></span>')
    else:
        left = f'<span style="width: 96px; flex-shrink: 0; font-size: 12.5px; font-weight: 500; color: {C["INK3"]};">분류 안 함</span>'
    return (f'<div style="display: flex; align-items: center; gap: 10px; height: 46px; {bb}">{left}'
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


# ══════════════ 1. 시트 기본 — 오늘 · 키보드 열림 ══════════════
def day_sheet_body(w_=390, fail=None, amount='12,000', memo='편의점', selected=None):
    pad = 18 if w_ >= 390 else 14
    recent = recent_row([recent_chip('커피', 4500, '카페/간식'), recent_chip('간식', 6500), recent_chip('점심', 9000, '식비'), recent_chip('버스', 1500, '교통')], pad)
    return (sheet_header('9월 8일 소비 기록', '오늘 4건 37,000원')
            + f'<div style="flex: 1; min-height: 0; overflow: hidden; padding: 12px {pad}px 0; display: flex; flex-direction: column; gap: 10px;">'
            + amount_field(amount, focused=True)
            + unsaved_line('1.2만원', fail)
            + memo_field(memo)
            + category_row(selected)
            + recent
            + f'<div style="margin-top: 2px;">{save_btn()}</div>'
            + f'<div style="padding-top: 4px;">{links_row()}</div>'
            + '</div>')


w('DaySheet', sheet_frame(day_sheet_body(), keyboard=True))
w('DaySheet360', sheet_frame(day_sheet_body(360), w_=360, keyboard=True))


# ══════════════ 2. 목록 우선 — 기록 있는 과거 날 ══════════════
list_body = (
    sheet_header('9월 3일 소비 기록', '3건 58,500원', today=False)
    + f'<div style="flex: 1; min-height: 0; overflow: hidden; padding: 14px 18px 0; display: flex; flex-direction: column; gap: 12px;">'
    + f'<div style="display: flex; flex-direction: column; gap: 8px;">'          # 제목이 날짜·건수·합계를 이미 말해서 구역 제목은 두지 않는다
    + card(tx_row('교통', '택시', 45000) + tx_row('식비', '점심', 9000) + tx_row(None, '간식', 4500, last=True), pad='2px 14px')
    + '</div>'
    + dashed_row('추가')
    + f'<div style="margin-top: auto; padding-bottom: 20px;">{links_row()}</div>'
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
               .replace('하루 47,270원', '앞으로 하루 46,730원'))
assert limit_after.count('앞으로 하루 46,730원') == 1 and limit_after.count('남은 한도 103만원') == 1 and limit_after.count('inset: 0 47.6% 0 0') == 1

DONE_CARD = ('<!--dc-keep--><div style="position: absolute; left: 14px; right: 14px; bottom: 78px; background: #101828; border-radius: 16px; padding: 13px 14px 12px; color: #FFFFFF; box-shadow: 0 8px 24px rgba(0,0,0,.28);">'
             '<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px;">'
             '<span style="display: inline-flex; align-items: center; gap: 7px; font-size: 14px; font-weight: 700;"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#3DD489" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg>저장했어요</span>'
             '<span style="font-size: 12px; font-weight: 600; color: rgba(255,255,255,.72);">닫기</span></div>'
             '<div style="font-size: 13.5px; font-weight: 500; margin-top: 7px; color: #FFFFFF;">9월 8일 · <span style="font-weight: 700;">12,000원</span> 저장 · 오늘 5건 49,000원</div>'
             '<div style="font-size: 12.5px; margin-top: 3px; color: rgba(255,255,255,.72);">소비율 57.9% → 58.2%</div>'
             '<div style="display: flex; gap: 8px; margin-top: 11px;">'
             '<span style="display: inline-flex; align-items: center; justify-content: center; height: 36px; padding: 0 14px; border-radius: 10px; border: 1px solid rgba(255,255,255,.55); color: #FFFFFF; font-size: 13px; font-weight: 700;">한 건 더</span>'
             '<span style="display: inline-flex; align-items: center; justify-content: center; height: 36px; padding: 0 12px; border-radius: 10px; border: 1px solid rgba(255,255,255,.28); color: #FFFFFF; font-size: 13px; font-weight: 600;">방금 기록한 12,000원 취소</span></div>'
             '</div><!--/dc-keep-->')

w('DoneCard', frame(
    f'\n  {s1.header}\n\n'
    f'  <div style="flex: 1; min-height: 0; display: flex; flex-direction: column; gap: 9px; padding: 0 14px; overflow: hidden; position: relative;">\n\n'
    f'    {hero_after}\n\n    {s1.guide_block}\n\n    {limit_after}\n\n    {s1.networth_card}\n\n  </div>\n\n'
    f'  {bottomnav(0)}\n  {DONE_CARD}\n').replace('overflow: hidden; font-variant-numeric: tabular-nums;">', 'overflow: hidden; position: relative; font-variant-numeric: tabular-nums;">', 1))


# ══════════════ 5. 저장 직전 확인 · 반복 겹침 — 구현 참고 장 ══════════════
# 앱 화면이 아니다. 왼쪽에 실제 하루 기록 창을 두어 안내가 뜨는 자리를 보여 주고, 오른쪽에 네 경우를 2 × 2로 놓는다
# (견본을 카드 폭 362보다 좁히면 ②의 버튼 두 개가 넘친다). 수치·조건은 견본 설명이 아니라 맨 아래 구현 메모에 모은다.
def nowrap_btn(html):
    """안내 상자 안 버튼 — 낱말 중간에서 꺾이거나 눌리지 않게."""
    return html.replace('font-weight: 600;">', 'font-weight: 600; white-space: nowrap; flex-shrink: 0;">', 1)


def confirm_block(inner):
    return (f'<div style="background: {C["SURF"]}; border: 1px solid {C["LINE"]}; border-radius: 18px; padding: 14px; display: flex; flex-direction: column; gap: 10px;">{inner}</div>')


fixed_chips = ''.join(cat_chip(n) for n in ['주거/관리', '통신', '보험', '구독'])
notice_fixed = (
    f'<div style="padding: 11px 12px; background: {C["WARN_SOFT"]}; border-radius: 12px; display: flex; flex-direction: column; gap: 9px;">'
    f'<span style="font-size: 13.5px; font-weight: 600; color: {C["WARN_INK"]};">매달 나가는 돈인가요?</span>'
    f'<div style="display: flex; gap: 6px; flex-wrap: wrap;">{fixed_chips}</div>'
    f'<div style="display: flex; align-items: center; gap: 12px;"><span style="font-size: 12.5px; font-weight: 600; color: {C["BRAND"]};">저축·투자 &rsaquo;</span><span style="font-size: 12.5px; font-weight: 600; color: {C["BRAND"]};">대출상환 &rsaquo;</span>'
    f'<span style="margin-left: auto; font-size: 12.5px; font-weight: 600; color: {C["INK2"]};">그대로 저장</span></div></div>')
block_fixed = confirm_block(amount_field('700,000', focused=False) + notice_fixed)
block_rule = confirm_block(
    amount_field('55,000', focused=False)
    + f'<div style="padding: 11px 12px; background: {C["WARN_SOFT"]}; border-radius: 12px; display: flex; flex-direction: column; gap: 9px;">'
    f'<span style="font-size: 13px; line-height: 1.45; color: {C["WARN_INK"]};">이번 달 휴대폰 요금 55,000원은 <b style="font-weight: 600;">25일에 자동으로 기록돼요</b></span>'
    f'<div style="display: flex; gap: 8px;">{nowrap_btn(smallbtn("이번 달은 이미 기록했어요", "soft", h=34))}{nowrap_btn(smallbtn("그대로 저장", "secondary", h=34))}</div></div>'
    )
block_dup = confirm_block(
    amount_field('55,000', focused=False)
    + f'<div style="padding: 11px 12px; background: {C["WARN_SOFT"]}; border-radius: 12px; display: flex; flex-direction: column; gap: 9px;">'
    f'<span style="font-size: 13px; line-height: 1.45; color: {C["WARN_INK"]};">같은 날 통신 55,000원(반복)이 <b style="font-weight: 600;">이미 있어요</b></span>'
    f'<div style="display: flex; gap: 8px;">{nowrap_btn(smallbtn("그래도 저장", "secondary", h=34))}{nowrap_btn(smallbtn("취소", "secondary", h=34))}</div></div>'
    )
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
    """picked = 묶음에서 고른 건수(일부를 제외했을 때). 금액 줄에 `4건 중 3건 · 합계`로 보여 준다."""
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


classify_body = (
    f'<div style="display: flex; justify-content: center; padding: 9px 0 0; flex-shrink: 0;"><span style="width: 38px; height: 4px; border-radius: 99px; background: {C["BORDER"]};"></span></div>'
    f'<div style="display: flex; align-items: flex-start; justify-content: space-between; gap: 10px; padding: 12px 18px 14px; border-bottom: 1px solid {C["LINE_SOFT"]}; flex-shrink: 0;"><div style="min-width: 0;">'
    f'<h2 style="margin: 0; font-size: 18px; font-weight: 700; letter-spacing: -0.025em; color: {C["INK"]};">분류하기 · 7건</h2>'
    f'<p style="margin: 4px 0 0; font-size: 12.5px; line-height: 1.45; color: {C["INK3"]};">같은 메모끼리 묶었어요. 추천은 눌러야 정해지고, 정한 것만 저장돼요.</p></div>'
    f'<span style="font-size: 13px; font-weight: 600; color: {C["INK2"]}; padding-top: 4px; flex-shrink: 0; white-space: nowrap;">닫기</span></div>'
    f'<div style="flex: 1; min-height: 0; overflow: hidden; padding: 6px 18px 0; display: flex; flex-direction: column;">'
    + group_row('커피', 4, 4500 * 3, '카페/간식', chosen=True, expanded=True, picked=3)      # 달력 칸과 같은 날짜(1 · 4 · 5 · 8일) — 5일은 제외
    + f'<div style="background: {C["INSET"]}; border-radius: 0 0 12px 12px; padding: 0 10px 2px; margin-bottom: 2px;">'
    + sub_row('9월 1일', 4500, True) + sub_row('9월 4일', 4500, True) + sub_row('9월 5일 · 제외', 4500, False) + sub_row('9월 8일', 4500, True, last=True)
    + '</div>'
    + single_row('간식', 6500, '식비', chosen=False)
    + single_row('편의점', 12000)
    + single_row('택시', 9000, last=True)
    + '</div>'
    f'<div style="padding: 12px 18px 20px; border-top: 1px solid {C["LINE_SOFT"]}; flex-shrink: 0; display: flex; flex-direction: column; gap: 8px;">'
    + btn('3건 저장', 'primary', h=52, radius=14, size=16)
    + f'<p style="margin: 0; text-align: center; font-size: 11.5px; line-height: 1.5; color: {C["INK3"]};">나머지 4건은 분류 안 함으로 남아요</p></div>')
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
        f'<span style="font-size: 11.5px; font-weight: 600; color: {C["BRAND"]}; white-space: nowrap;">기준 조정 &rsaquo;</span></div>'
        + f'<div style="margin-top: 10px;">{btn("소비 기록하기", "primary", "plus", h=46)}</div>')


first_guide = guidance('info', '다음 안내', '오늘 첫 기록을 남겼어요', '며칠 더 기록하면 월말 예상을 보여 드려요.', None)
limit_first = (s1.limit_block.replace('남은 한도 104만원', '남은 한도 216만원').replace('inset: 0 48.1% 0 0', 'inset: 0 99.8% 0 0')
               .replace('하루 47,270원', '앞으로 하루 97,950원'))
assert limit_first.count('앞으로 하루 97,950원') == 1 and limit_first.count('남은 한도 216만원') == 1
w('HeroInsufficient', frame(
    f'\n  {s1.header}\n\n'
    f'  <div style="flex: 1; min-height: 0; display: flex; flex-direction: column; gap: 9px; padding: 0 14px; overflow: hidden;">\n\n'
    f'    {hero_insufficient()}\n\n    {first_guide}\n\n    {limit_first}\n\n  </div>\n\n'
    f'  {bottomnav(0)}\n'))


# ══════════════ 8. 홈 맨 위 카드에 붙는 작은 안내 줄 — 구현 참고 장 ══════════════
# 앱 화면이 아니다. 왼쪽에 온전한 카드 한 장(②의 경우)을 두어 안내 줄 자리를 표시하고, 오른쪽에는 카드의 아랫부분
# (기준 줄 + 안내 줄 + 버튼)만 네 경우로 놓는다. 기준 줄이 한 줄에 들어가는 실제 폭을 지키려고 견본은 카드 폭 362 그대로 2 × 2.
HERO_BASIS = '<div style="display: flex; align-items: center; justify-content: space-between; gap: 10px; margin-top: 12px;">'
HERO_BTN = '<div style="display: flex; align-items: center; justify-content: center; gap: 6px; height: 46px; margin-top: 10px;'
assert s1.hero_block.count(HERO_BASIS) == 1 and s1.hero_block.count(HERO_BTN) == 1
assert s1.hero_block.index(HERO_BASIS) < s1.hero_block.index(HERO_BTN) and s1.hero_block.endswith('</div>')
hero_top = s1.hero_block[:s1.hero_block.index(HERO_BASIS)]                       # 카드 여는 태그 ~ 세 칸 요약
_tail = s1.hero_block[s1.hero_block.index(HERO_BASIS):]
hero_tail = _tail[:_tail.rstrip().rindex('</div>')].rstrip()                     # 기준 줄 + 버튼(카드 닫는 태그 앞까지)
NOTE_STYLE = f'font-size: 11px; line-height: 1.4; color: {C["INK3"]};'


def hero_tail_with(notes, marked=False):
    """기준 줄과 버튼 사이에 안내 줄을 붙인다. marked = 안내 줄 자리를 옅은 파란 테두리와 알약으로 표시(왼쪽 온전한 카드용)."""
    if marked:
        # 알약은 안내 줄의 빈 오른쪽 끝에 세로 가운데로 — 윗줄의 `기준 조정 ›`도 아래 버튼도 가리지 않는다
        pill = (f'<span style="position: absolute; top: 50%; right: 4px; transform: translateY(-50%); height: 17px; padding: 0 7px; border-radius: 99px; '
                f'background: {C["INK"]}; color: #FFFFFF; font-size: 10.5px; font-weight: 700; display: inline-flex; align-items: center; white-space: nowrap;">안내 줄</span>')
        extra = (f'<div style="position: relative; margin-top: 4px; border-radius: 4px; box-shadow: 0 0 0 3px rgba(53,86,230,.16);">'
                 + ''.join(f'<div style="{NOTE_STYLE}">{n}</div>' for n in notes) + pill + '</div>')
    else:
        extra = ''.join(f'<div style="{NOTE_STYLE} margin-top: 4px;">{n}</div>' for n in notes)
    return hero_tail.replace(HERO_BTN, extra + HERO_BTN, 1)


def hero_fragment(notes):
    """카드의 아랫부분만 — 위 테두리 없이 아래 모서리만 둥글게 해서 잘라 낸 조각으로 보이게."""
    return (f'<div style="background: {C["SURF"]}; border: 1px solid {C["LINE"]}; border-top: none; border-radius: 0 0 20px 20px; padding: 4px 16px 16px; '
            f'box-shadow: 0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24);">{hero_tail_with(notes)}</div>')


NOTE_A = '분류 안 한 32,000원은 적은 금액 그대로 예상에 더했어요'
NOTE_B = '분류 안 한 지난 기록도 평균에 넣었어요. 분류하면 다시 계산해요.'
NOTE_C = '지난 고정비 기록을 보고 앞으로 나갈 돈도 예상했어요'
NOTE_D = '기록이 한 달치뿐이라 예상이 달라질 수 있어요'
FOOTNOTE_CASES = [
    (1, '덧붙일 말이 없을 때', '기준 조정 줄 바로 아래에 버튼이 옵니다. 지금 홈과 같습니다.', []),
    (2, '이번 달에 분류 안 한 기록이 있을 때', '안내가 한 줄 붙습니다.', [NOTE_A]),
    (3, '지난달 기록으로 예상을 계산한 날', '안내가 두 줄 붙습니다. 이번 달 기록만으로 계산한 날에는 나오지 않습니다.', [NOTE_B, NOTE_C]),
    (4, '기록이 한 달치뿐일 때', '안내가 한 줄 붙습니다.', [NOTE_D])]
footnote_left = (
    f'<div style="width: 362px; flex-shrink: 0; display: flex; flex-direction: column; gap: 8px;">{hero_top}{hero_tail_with([NOTE_A], marked=True)}</div>'
    f'<p style="margin: 2px 2px 0; font-size: 12px; line-height: 1.5; color: {C["INK3"]};">안내 줄은 '
    f'<b style="font-weight: 600; color: {C["INK2"]};">기준 조정 줄과 버튼 사이</b>에 붙습니다. 그림은 2번의 경우입니다.</p></div>')
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
# 칸 숫자 = 그날 소비 합계(고정비 포함 · 이체 제외). 표기는 앱 formatSum과 같다(1만 미만 원 단위 · 1만 이상 만 단위 한 자리).
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


def cell(day, wd=None, w_=44, pressed=False, prev=False, future=False):
    """스트립 칸(접힘 · 최근 7일). 44 × 56. 달 제목이 없는 자리라 지난달 날짜는 `8/31`처럼 달을 붙인다."""
    is_today = day == TODAY and not prev
    label = f'8/{day}' if prev else str(day)
    bg = C["BRAND_SOFT"] if is_today else 'transparent'
    ring = f'box-shadow: inset 0 0 0 2px {C["BRAND"]};' if pressed else ''
    date_col = C["INK4"] if future else (C["INK"] if is_today else C["INK2"])
    parts = [f'<span style="font-size: 11px; line-height: 1; font-weight: {600 if is_today else 500}; color: {date_col};">{label}</span>']
    if not future:
        s, chk, tr, zero = day_state('aug' if prev else 'sep', day)
        col = C["INK3"] if s == '—' else (C["INK2"] if zero else C["INK"])
        parts.append(f'<span style="font-size: 11px; line-height: 13px; font-weight: 600; color: {col}; font-variant-numeric: tabular-nums;">{s}</span>')
        parts.append(_mods(chk, tr))
    else:
        parts.append('<span style="height: 13px; flex-shrink: 0;"></span><span style="height: 12px; flex-shrink: 0;"></span>')
    wdl = f'<span style="font-size: 10px; line-height: 1; font-weight: 500; color: {C["INK3"]};">{wd}</span>' if wd else ''
    return (f'<div style="width: {w_}px; height: 56px; border-radius: 10px; background: {bg}; {ring} display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 3px; flex-shrink: 0;">'
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


def calendar_card(expanded=False, pressed=None, pad=14, month='sep', large=False, with_list_link=False):
    if not expanded:
        title = (f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px;">'
                 f'<span style="font-size: 14px; font-weight: 600; color: {C["INK"]};">이번 달 달력</span>'
                 f'<span style="display: inline-flex; align-items: center; gap: 2px; font-size: 12px; font-weight: 600; color: {C["INK2"]};">펼치기{icon("down", 14, C["INK2"], 2.2)}</span></div>')
        # 최근 7일 — 오늘이 오른쪽 끝 (9/2 ~ 9/8)
        cells = ''.join(cell(d, WD[(1 + d) % 7], pressed=(pressed == d)) for d in range(2, 9))
        body = f'<div style="display: flex; justify-content: space-between; margin-top: 8px;">{cells}</div>'
        return card(title + body + status_rows(), pad=f'13px {pad}px 13px')
    if month == 'sep':
        bar = month_bar('2026년 9월', prev_on=True, next_on=False, large=large)
        status = f'9월 기록한 소비 {SEP_TOTAL:,}원 · 오늘 4건 37,000원'
    else:
        bar = month_bar('2026년 8월', prev_on=False, next_on=True, back_pill=True, large=large)
        status = f'8월 기록한 소비 {AUG_TOTAL:,}원'
    tail = status_rows(text=status, large=large) + (list_link(large) if with_list_link else '')
    return card(bar + month_grid(month, pressed, large) + tail, pad=f'13px {pad}px {4 if with_list_link else 13}px')


def home_expanded(width=390, pad=14, month='sep', pressed=None, limit=True):
    peek = f'<div style="height: 22px; background: {C["SURF"]}; border: 1px solid {C["LINE"]}; border-top: none; border-radius: 0 0 20px 20px; flex-shrink: 0; opacity: .55;"></div>'
    # 한도 카드 첫 줄은 한 줄로 고정(왼쪽 덩어리 nowrap). 360 폭에서는 회색 글을 '하루 47,270원'으로 줄여야 '남은 한도 104만원'과 한 줄에 들어간다.
    lim_left = '<span style="font-size: 13.5px; font-weight: 600; color: #101828;">이번 달 한도 '
    assert s1.limit_block.count(lim_left) == 1 and s1.limit_block.count('하루 47,270원') == 1
    lim_html = s1.limit_block.replace(lim_left, lim_left.replace('color: #101828;', 'color: #101828; white-space: nowrap;'))
    if width >= 390:
        lim_html = lim_html.replace('하루 47,270원', '앞으로 하루 47,270원')
    lim = ('\n\n    ' + lim_html) if limit else ''
    return frame(
        f'\n  <div style="flex: 1; min-height: 0; display: flex; flex-direction: column; gap: 9px; padding: 0 14px; overflow: hidden;">\n\n'
        f'    {peek}\n\n    {calendar_card(True, pressed=pressed, pad=pad, month=month)}\n\n    {s1.guide_block}{lim}\n\n  </div>\n\n'
        f'  {bottomnav(0)}\n', w=width)


# 홈 · 접힘 — 히어로 그대로, 첫 카드가 달력(최근 7일)
w('HomeCalendarStrip', frame(
    f'\n  {s1.header}\n\n'
    f'  <div style="flex: 1; min-height: 0; display: flex; flex-direction: column; gap: 9px; padding: 0 14px; overflow: hidden;">\n\n'
    f'    {s1.hero_block}\n\n    {calendar_card(False)}\n\n    {s1.guide_block}\n\n  </div>\n\n'
    f'  {bottomnav(0)}\n'))

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
    (2, '금액', '그날 쓴 돈의 합계 · 4,500이나 5.9만처럼 짧게', '누르면 그날 기록 목록이 먼저 보여요'),
    (3, '금액 아래 ✓', '다 적었어요로 표시한 날', '그날 기록을 고치면 ✓가 풀려요'),
    (4, '0', '안 쓴 날이라고 표시한 날', ('이체', '저축·대출상환이 있던 날 · 소비 합계에는 넣지 않아요')),      # 한 번호 안에서 같은 굵기의 두 줄
    (5, '오늘', '옅은 파란 칸에 굵은 날짜', '누르면 금액 입력부터 시작해요'),
    (6, '아직 오지 않은 날', '날짜만 옅게 보여요', '눌러도 열리지 않아요'),
    (7, '지난달 날짜', '첫 주의 8월 30·31일 · 기록이 옅게 보여요', '누르면 그 날짜 기록 창이 열려요'),
    (8, '다음 달 날짜', '10월 1~3일 · 아직 오지 않은 날은 날짜만 옅게', '누를 수 없어요 · 이미 지난 날이면 7번처럼 기록이 옅게 보여요'),
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

w('CalendarCells', spec_frame(
    940, 730, '달력 칸 읽는 법', '칸의 숫자는 그날 소비 합계입니다(고정비 포함 · 이체 제외). 왼쪽 달력의 번호를 오른쪽에서 찾으세요.',
    f'<div style="display: flex; gap: 28px; align-items: flex-start;">'
    f'<div style="width: 362px; flex-shrink: 0;">{marked_calendar()}</div>'
    f'<div style="flex: 1; min-width: 0;">{cell_guide}{cell_foot}</div></div>'))


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


def sample(width, title, line, inner):
    """견본 하나 — 상황을 말하는 제목 + 한 줄 설명 + 그림."""
    return (f'<div style="width: {width}px; flex-shrink: 0; display: flex; flex-direction: column; gap: 8px;">'
            f'<div><div style="font-size: 14px; font-weight: 700; letter-spacing: -0.01em; color: {C["INK"]};">{title}</div>'
            f'<div style="font-size: 12px; line-height: 1.5; color: {C["INK3"]}; margin-top: 2px;">{line}</div></div>{inner}</div>')


cal320 = calendar_card(True, pad=8).replace('2026년 9월', '9월').replace('min-width: 94px', 'min-width: 44px')
cal_large = calendar_card(True, large=True, with_list_link=True)
bar_prev320 = card(month_bar('8월', prev_on=False, next_on=True, back_pill=True, pill_below=True, label_w=44)
                   + month_grid('aug', weeks=slice(0, 1)), pad='13px 8px 13px')          # 머리 부분만 떠 있지 않게 요일 줄과 첫 주를 붙인다
cal_large320 = card(month_bar('8월', prev_on=False, next_on=True, back_pill=True, large=True, label_w=52)
                    + month_grid('aug', large=True, tight=True, weeks=slice(0, 3)), pad='13px 8px 13px')

# 구현 수치는 견본 설명에 흩지 않고 아랫줄 오른쪽 빈자리에 한 단락으로 모은다(맨 아래는 남는 높이가 없다).
sizes_memo = (f'<div style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 4px;">'
              f'<div style="font-size: 12px; font-weight: 600; color: {C["INK2"]};">구현 메모</div>'
              f'<p style="margin: 0; font-size: 12px; line-height: 1.6; color: {C["INK3"]};">가장 좁은 폰은 화면 너비 320px, 달력 칸은 39 × 56입니다. '
              f'큰 글자에서는 칸 높이가 72가 됩니다. 좁은 폰 + 큰 글자에서는 금액 글자 크기를 12로 줄입니다. '
              f'지난달을 볼 때 &lsquo;이번 달로&rsquo; 버튼은 제목 줄 바로 아래 줄 오른쪽에 둡니다.</p></div>')

sizes_row1 = ('<div style="display: flex; gap: 36px; align-items: flex-start;">'
              + sample(292, '가장 좁은 폰', '달력 그대로. 제목은 9월만 적어요', cal320)
              + sample(362, '글자를 크게 쓰는 사람', '달력 그대로. 칸이 높아지고 글자가 커져요', cal_large)
              + sample(362, '목록으로 보기를 고르면', '스스로 고른 사람에게만. 저절로 바뀌지 않아요', list_view)
              + '</div>')
sizes_row2 = ('<div style="display: flex; gap: 36px; align-items: flex-start; margin-top: 26px;">'
              + sample(292, '가장 좁은 폰에서 지난달을 볼 때', '&lsquo;이번 달로&rsquo; 버튼은 제목 아랫줄로 내려가요', bar_prev320)
              + sample(292, '좁은 폰 + 큰 글자', '금액 글자를 조금 줄여 71.2만도 잘리지 않아요', cal_large320)
              + sizes_memo + '</div>')

w('CalendarGridSizes', spec_frame(
    1150, 1300, '달력을 펼치면 어디서나 월 달력', '화면이 좁아도, 글자를 크게 써도 날짜를 세로로 늘어놓은 목록으로 바뀌지 않습니다.',
    sizes_row1 + sizes_row2))
