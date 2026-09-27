# -*- coding: utf-8 -*-
"""모달의 오류·저장 상태 카탈로그 아트보드."""
import pathlib
from gen_common import (C, icon, doc, state_sheet, card, field, note, btn,
                        smallbtn, section_head, badge, bar, toggle)

OUT = pathlib.Path(__file__).resolve().parent.parent


def modal_head(title, meta=None):
    m = f'<span style="font-size: 11.5px; color: {C["INK3"]};">{meta}</span>' if meta else ''
    return (f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px; '
            f'padding-bottom: 11px; margin-bottom: 13px; border-bottom: 1px solid {C["LINE_SOFT"]};">'
            f'<div style="display: flex; align-items: baseline; gap: 7px;">'
            f'<span style="font-size: 15px; font-weight: 700; letter-spacing: -0.02em; color: {C["INK"]};">{title}</span>{m}</div>'
            f'<div style="width: 28px; height: 28px; border-radius: 9px; background: {C["INSET"]}; display: flex; '
            f'align-items: center; justify-content: center; flex-shrink: 0;">{icon("x", 15, C["INK2"], 2.2)}</div></div>')


def footer(left, right):
    return (f'<div style="display: flex; gap: 9px; margin-top: 14px; padding-top: 13px; '
            f'border-top: 1px solid {C["LINE_SOFT"]};">'
            f'{left.replace("width: 100%;", "flex: 1;")}{right.replace("width: 100%;", "flex: 1.4;")}</div>')


def choice(label, meta):
    return (f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px; height: 42px; '
            f'padding: 0 12px; border-radius: 11px; border: 1px solid {C["BORDER"]}; background: {C["SURF"]};">'
            f'<span style="font-size: 13px; font-weight: 600; color: {C["INK"]}; white-space: nowrap;">{label}</span>'
            f'<span style="display: inline-flex; align-items: center; gap: 5px; flex-shrink: 0;">'
            f'<span style="font-size: 11.5px; color: {C["INK3"]};">{meta}</span>{icon("right", 14, C["INK4"], 2.2)}</span></div>')


def placeholder(text):
    return f'<span style="font-weight: 400; color: {C["DIS"]};">{text}</span>'


def spinner(size=16, color=None):
    color = color or "#FFFFFF"
    # 라이트/다크 모두에서 보이도록 리터럴 hex만 쓴다(다크 변환이 매핑한다).
    return (f'<span style="width: {size}px; height: {size}px; border-radius: 99px; border: 2px solid #8FA6F2; '
            f'border-top-color: {color}; display: inline-block; flex-shrink: 0;"></span>')


def saving_btn():
    return (f'<div style="display: flex; align-items: center; justify-content: center; gap: 8px; height: 46px; flex: 1.4; '
            f'border-radius: 13px; background: {C["BRAND"]}; opacity: .72; color: #FFFFFF; font-size: 15px; font-weight: 600;">'
            f'{spinner()}저장 중</div>')


# ── A · 필수 값 미입력 — 저장을 누르면 빠진 칸을 알려 준다(D11 · assets-20) ─────────────────────
# 앱 NaviForm 은 저장 버튼을 누를 수 있게 둔다. 누르면 빈 칸에 빨간 테두리 + 「{칸}을/를 넣어 주세요」, 바닥줄 위 요약 「빠진 칸이 있어요 · …」, 첫 빈 칸으로 초점.
def seg3(active):
    cells = []
    for i, t in enumerate(['소비', '저축·투자', '대출상환']):
        if i == active:
            cells.append(f'<div style="flex: 1; height: 34px; border-radius: 8px; background: {C["SURF"]}; display: flex; align-items: center; justify-content: center; font-size: 12.5px; font-weight: 600; color: {C["INK"]}; box-shadow: 0 1px 2px rgba(16,24,40,.08);">{t}</div>')
        else:
            cells.append(f'<div style="flex: 1; height: 34px; border-radius: 8px; display: flex; align-items: center; justify-content: center; font-size: 12.5px; font-weight: 500; color: {C["TAB_INK"]};">{t}</div>')
    return f'<div style="display: flex; gap: 4px; background: {C["INSET"]}; border-radius: 11px; padding: 3px;">{"".join(cells)}</div>'


def lab(text):
    return f'<div style="font-size: 12px; font-weight: 600; color: {C["INK2"]}; margin-bottom: 7px;">{text}</div>'


def date_value(text):
    return f'<span style="display: inline-flex; align-items: center; gap: 8px;">{icon("cal", 16, C["INK3"], 1.8)}{text}</span>'


def red_box(text, mt=12):
    return (f'<div style="margin-top: {mt}px; padding: 10px 12px; border-radius: 11px; background: {C["NEG_SOFT"]}; '
            f'font-size: 12.5px; line-height: 1.5; color: {C["NEG"]};">{text}</div>')


READONLY_CAT = (f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 12px; margin-top: 12px;">'
                f'<span style="font-size: 13px; color: {C["INK2"]};">카테고리</span>'
                f'<div style="text-align: right;"><div style="font-size: 14px; font-weight: 700; color: {C["INK"]};">저축·투자</div>'
                f'<div style="font-size: 11px; color: {C["INK3"]}; margin-top: 2px;">소비율에 안 들어가요</div></div></div>')

a = card(
    modal_head('기록 추가') +
    lab('기록 종류') + seg3(1) +
    '<div style="display: flex; flex-direction: column; margin-top: 12px;">' +
    field('날짜', date_value('2026. 09. 08.')).replace('flex: 1; min-width: 0;', 'min-width: 0;', 1) + '</div>' +
    '<div style="display: flex; flex-direction: column; margin-top: 12px;">' +
    field('금액', '', unit='원', required=True, state='error', helper='금액을 넣어 주세요').replace('flex: 1; min-width: 0;', 'min-width: 0;', 1) + '</div>' +
    READONLY_CAT +
    red_box('빠진 칸이 있어요 · 금액') +
    footer(btn('취소', 'secondary'), btn('저장', 'primary')),
    pad='16px')
a = (f'<div style="display: flex; flex-direction: column; gap: 8px; flex-shrink: 0;">{a}'
     + note('하루 시트만 예외 — 금액이 비면 「저장」은 회색으로 누를 수 없고 아래에 「금액을 넣으면 저장할 수 있어요」가 붙습니다(카테고리 고르기 시트의 「0건 저장」도 같음).', 'mute') + '</div>')

# ── B · 직접 정한 카테고리 합계가 총한도보다 큼(한도 조정 · D2 · spending-8) ──────────────────────
# 칸 오류가 아니다 — 빨간 칸 · 빗금 막대 · 고치는 방법 버튼 없이, 바닥줄 위에 주황 상자 하나. 「한도 저장」은 그대로 누를 수 있다.
def lim_row(ic, cat, color, sub, value, manual, last=False):
    bd = '' if last else f'border-bottom: 1px solid {C["LINE_ROW"]};'
    val_col = C["INK"] if manual else C["DIS"]
    return (f'<div style="display: flex; align-items: center; gap: 10px; min-height: 52px; {bd}">'
            f'<div style="width: 30px; height: 30px; border-radius: 9px; background: {color}20; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">{icon(ic, 15, color, 1.9)}</div>'
            f'<div style="flex: 1; min-width: 0;"><div style="font-size: 13.5px; font-weight: 600; color: {C["INK"]};">{cat}</div>'
            f'<div style="font-size: 11px; color: {C["INK3"]};">{sub}</div></div>'
            f'<div style="display: flex; align-items: center; gap: 3px; width: 96px; height: 40px; padding: 0 10px; border-radius: 11px; '
            f'border: {"1.5px solid " + C["BRAND"] if manual and cat == "식비" else "1px solid " + C["INPUT"]}; background: {C["SURF"]}; flex-shrink: 0;">'
            f'<span style="flex: 1; text-align: right; font-size: 15px; font-weight: {600 if manual else 500}; color: {val_col};">{value}</span>'
            f'<span style="font-size: 12px; color: {C["INK3"]};">만원</span></div></div>')

b = card(
    modal_head('한도 조정') +
    f'<div style="display: flex; align-items: baseline; gap: 7px; margin-bottom: 4px;">'
    f'<span style="font-size: 13.5px; font-weight: 600; color: {C["INK"]};">카테고리 배분</span>'
    f'<span style="font-size: 11.5px; color: {C["INK3"]};">단위 만원 · 비우면 자동</span></div>' +
    lim_row('rice', '식비', '#f97316', '직접 180만원', '180', True) +
    lim_row('house', '주거/관리', '#8b5cf6', '직접 56만원', '56', True) +
    lim_row('coffee', '카페/간식', '#d97706', '자동 0원', '0', False, last=True) +
    f'<div style="margin-top: 12px; padding: 11px 12px; border-radius: 12px; background: {C["WARN_SOFT"]}; border: 1px solid {C["WARN_RULE"]};">'
    f'<div style="display: flex; align-items: center; gap: 6px; font-size: 12.5px; font-weight: 600; color: {C["WARN_INK"]};">{icon("warn", 14, C["WARN"], 2)}직접 정한 카테고리 합계가 총한도보다 커요</div>'
    f'<div style="text-align: right; font-size: 13px; font-weight: 700; color: {C["WARN_INK"]}; margin-top: 4px;">236만원 / 216만원</div>'
    f'<div style="font-size: 11.5px; color: {C["WARN_INK"]}; margin-top: 3px;">직접 정한 금액을 줄이거나 총한도를 늘려 주세요.</div></div>' +
    footer(btn('취소', 'secondary'), btn('한도 저장', 'primary')),
    pad='16px')

# ── C · 저장 중 — 입력 잠금(D10 · components/navi/form-dialog.tsx) ─────────────────────────
c = card(
    modal_head('자산 추가') +
    f'<div style="opacity: .55;">'
    '<div style="display: flex; gap: 10px;">' +
    field('자산 이름', '청약저축') + field('지금 금액', '500', unit='만원', w=150) +
    '</div></div>' +
    f'<div style="display: flex; gap: 9px; margin-top: 14px; padding-top: 13px; border-top: 1px solid {C["LINE_SOFT"]};">'
    f'{btn("취소", "disabled").replace("width: 100%;", "flex: 1;")}'
    f'{btn("자산 추가", "primary").replace("width: 100%;", "flex: 1.4; opacity: .6;")}</div>'
    f'<div style="font-size: 12px; color: {C["INK3"]}; margin-top: 9px;">기기에 저장 중… 잠시만 기다려 주세요.</div>',
    pad='16px')

# ── D · 저장 실패 — 실패한 자리 옆에 한 번 · 무엇이 그대로인지(a11y-6 · D10) ──────────────────
def mini_cap(text):
    return f'<div style="font-size: 11.5px; font-weight: 600; color: {C["INK3"]}; margin-bottom: 7px;">{text}</div>'

d_form = card(
    mini_cap('기록 추가 · 저장을 눌렀는데 기기에 못 씀') +
    f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 10px; padding: 11px 12px; background: {C["INSET"]}; border-radius: 12px;">'
    f'<div><div style="font-size: 13px; font-weight: 600; color: {C["INK"]};">잔액에도 반영하기</div>'
    f'<div style="font-size: 11px; color: {C["INK3"]}; margin-top: 2px;">선택한 출금·입금 계좌에 함께 반영해요</div></div>{toggle(False)}</div>' +
    footer(btn('취소', 'secondary'), btn('저장', 'primary')) +
    f'<div style="font-size: 12px; line-height: 1.5; color: {C["NEG"]}; margin-top: 10px;">기기에 저장하지 못했습니다. 입력한 값은 그대로 있어요. 저장 공간을 확인한 뒤 다시 저장해 주세요.</div>',
    pad='14px')
d_day = card(
    mini_cap('하루 시트 · 금액 칸 아래') +
    field('금액', '12,000', unit='원') +
    f'<div style="font-size: 11.5px; color: {C["INK3"]}; margin-top: 6px;"><b style="font-weight: 600; color: {C["INK2"]};">1.2만원</b> · 저장을 눌러야 기록돼요</div>' +
    red_box('저장하지 못했어요. 적은 내용은 그대로 있어요. · <b style="font-weight: 600; color: ' + C["BRAND"] + ';">다시 시도</b>', mt=9),
    pad='14px')
d_pay = card(
    mini_cap('미래 › 상환 계획 · 저장 칸') +
    f'<div style="font-size: 14px; font-weight: 700; color: {C["INK"]};">이 계획을 저장할까요?</div>'
    f'<div style="font-size: 12px; color: {C["INK3"]}; margin-top: 3px;">저장해야 홈 · 자산 경로 · 목적지 계산에 반영돼요.</div>'
    f'<div style="display: flex; gap: 8px; margin-top: 11px;">{btn("가정 종료", "secondary", h=42).replace("width: 100%;", "flex: 1;")}'
    f'{btn("상환 계획 저장", "primary", h=42).replace("width: 100%;", "flex: 1.4;")}</div>' +
    red_box('상환 계획을 저장하지 못했습니다. 이전 계획(고금리 우선 · 월 15만원)을 그대로 써요.', mt=10),
    pad='14px')
d = f'<div style="display: flex; flex-direction: column; gap: 8px; flex-shrink: 0;">{d_form}{d_day}{d_pay}</div>'

# ── E · 저장 알림 — 아래 어두운 카드 6초 → 40px 띠 → 저장 60초 뒤 사라짐(record-6 · record-20 · D10) ─────
# 어두운 카드는 라이트/다크가 같다(<!--dc-keep-->).
TOAST_BG = '#101828'
e_card = (f'<!--dc-keep--><div style="margin: 0 -14px; background: {TOAST_BG}; border-radius: 16px; padding: 13px 14px; color: #FFFFFF; '
          f'box-shadow: 0 10px 28px -14px rgba(16,24,40,.6);">'
          f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 10px;">'
          f'<span style="display: inline-flex; align-items: center; gap: 7px; font-size: 13.5px; font-weight: 600;">{icon("check", 15, "#FFFFFF", 2.6)}한도를 저장했어요 · 총한도 216만원 · 자동</span>'
          f'<span style="font-size: 12.5px; color: rgba(255,255,255,.72); flex-shrink: 0;">닫기</span></div>'
          f'<div style="display: inline-flex; align-items: center; height: 34px; padding: 0 13px; margin-top: 11px; border-radius: 10px; '
          f'border: 1px solid rgba(255,255,255,.38); font-size: 13px; font-weight: 600;">되돌리기</div></div><!--/dc-keep-->')
# 띠 = 같은 저장(한도)의 요약이 한 줄로 줄어든 것 — 앱 .notice-strip(c6b7de3 · 시계 +7초): ✓ 요약(13 / 600 · 길면 …) · 되돌리기(13 / 700) · 닫기(13 / 600 흐리게) ·
# 사이 가운뎃점(2026-09-27 fix-up 5 · 예전 다른 저장의 요약 「12,000원 저장」).
# 폭 = 앱 .save-notice 362(x 14 ~ 376 · 안쪽 0 4 0 12 → 띠 글 칸 .notice-strip 346)에 맞춰 카드 안쪽 332 에서 양옆 14 씩 내어 써 360(카드 테두리 바로 안) —
# 처음 6초 카드도 같은 상자라 같은 폭. 요약은 앱이 346 에서 보이는 그대로 「… 총한도 216만원…」까지 글자로 끊어 둔다 —
# 글꼴 폭이 조금 달라도 「총한도 21…」로 읽히지 않게 CSS 말줄임에 맡기지 않는다(2026-09-27 fix-up 6 · 예전 332 폭 · 안쪽 0 3 0 12 에서 「총한도 21…」)
_DOT = '<span style="font-size: 14px; color: rgba(255,255,255,.5); flex-shrink: 0;">·</span>'
_CHK = icon("check", 14, "#FFFFFF", 2.6).replace('<svg ', '<svg style="flex-shrink: 0;" ', 1)
e_strip = (f'<!--dc-keep--><div style="display: flex; align-items: center; height: 40px; margin: 0 -14px; padding: 0 4px 0 12px; '
           f'background: {TOAST_BG}; border-radius: 12px; color: #FFFFFF;">'
           f'<span style="display: flex; align-items: center; gap: 6px; flex: 1; min-width: 0; padding-right: 6px;">{_CHK}'
           f'<span style="font-size: 13px; font-weight: 600; line-height: 16px; white-space: nowrap;">한도를 저장했어요 · 총한도 216만원…</span></span>'
           f'{_DOT}<b style="padding: 0 9px; font-size: 13px; font-weight: 700; white-space: nowrap; flex-shrink: 0;">되돌리기</b>'
           f'{_DOT}<span style="padding: 0 9px; font-size: 13px; font-weight: 600; color: rgba(255,255,255,.72); white-space: nowrap; flex-shrink: 0;">닫기</span></div><!--/dc-keep-->')
e = card(
    mini_cap('처음 6초 — 아래 탭 막대 바로 위') + e_card +
    f'<div style="height: 12px;"></div>' + mini_cap('6초 뒤 — 같은 알림이 한 줄 띠로(길면 요약 끝을 … 로 줄임)') + e_strip +
    f'<div style="font-size: 12px; line-height: 1.5; color: {C["INK3"]}; margin-top: 10px;">6초 뒤 한 줄로 줄고 1분 뒤 사라져요 · 탭을 옮겨도 남아요 · 새로 저장하면 바뀌어요. 되돌리기는 이 알림에만 있습니다.</div>',
    pad='14px')

# ── F · 저장하지 않고 닫기(a11y-17 · language-ia-11) ─────────────────────────────────
f = card(
    f'<div style="text-align: center; padding: 4px 4px 0;">'
    f'<div style="font-size: 16px; font-weight: 700; letter-spacing: -0.02em; color: {C["INK"]};">저장하지 않고 닫을까요?</div>'
    f'<div style="font-size: 12.5px; line-height: 1.55; color: {C["INK3"]}; margin-top: 6px;">'
    f'이번에 넣은 내용은 저장되지 않아요. 계속 작성하면 넣은 값을 그대로 둘 수 있어요.</div></div>'
    f'<div style="display: flex; flex-direction: column; gap: 7px; margin-top: 15px;">'
    f'<div style="display: flex; align-items: center; justify-content: center; height: 40px; border-radius: 11px; background: {C["NEG_SOFT"]}; color: {C["NEG"]}; font-size: 14px; font-weight: 600;">변경 버리고 닫기</div>'
    f'<div style="display: flex; align-items: center; justify-content: center; height: 40px; border-radius: 11px; background: #E8ECF5; border: 2px solid {C["BRAND"]}; box-shadow: 0 0 0 3px rgba(53,86,230,.18); color: {C["INK"]}; font-size: 14px; font-weight: 600;">계속 작성</div></div>',
    pad='16px')
# v5(§9-13 · §12-24): 하루 시트만은 이 확인 창을 띄우지 않는다 — 규칙 한 줄을 창 아래에 적는다(앱 문구가 아니라 구현 규칙).
f = (f'<div style="display: flex; flex-direction: column; gap: 8px; flex-shrink: 0;">{f}'
     + note('처음 초점은 「계속 작성」. 하루 시트는 예외(확인 없음 · 초안은 메모리에만, 앱을 다시 켜면 사라짐)', 'mute') + '</div>')

# ── G · 부채 상환 목적지 — 넣어 둔 부채가 없을 때(assets-20 · D16) ──────────────────────────
TYPE_TILES = [("일반 저축", "wallet", C["BRAND"]), ("비상금", "shield", C["SKY"]), ("투자", "chart", C["VIO"]),
              ("순자산", "target", C["POS"]), ("부채 상환", "bank", C["WARN"])]
tiles = ''.join(
    f'<div style="flex: 1; min-width: 0; padding: 8px 4px; border-radius: 11px; text-align: center; '
    f'border: {"1.5px solid " + col if i == 4 else "1px solid " + C["LINE"]}; background: {col + "14" if i == 4 else C["SURF"]};">'
    f'<div style="display: flex; justify-content: center;">{icon(ic, 15, col if i == 4 else C["INK3"], 1.9)}</div>'
    f'<div style="font-size: 10.5px; font-weight: {700 if i == 4 else 500}; color: {col if i == 4 else C["INK2"]}; margin-top: 4px; white-space: nowrap;">{name}</div></div>'
    for i, (name, ic, col) in enumerate(TYPE_TILES))
g = card(
    modal_head('목적지 추가') +
    lab('유형') + f'<div style="display: flex; gap: 5px;">{tiles}</div>' +
    f'<div style="margin-top: 13px;">{lab("갚을 부채")}'
    f'<div style="font-size: 12.5px; color: {C["INK3"]};">먼저 부채를 넣어 주세요</div>'
    f'<div style="font-size: 13px; font-weight: 600; color: {C["BRAND"]}; margin-top: 6px;">부채 추가하기 &rsaquo;</div></div>'
    f'<div style="font-size: 12px; line-height: 1.5; color: {C["INK3"]}; margin-top: 12px;">누르면 자산 › 부채로 가서 새 부채 창이 열립니다.</div>' +
    footer(btn('취소', 'secondary'), btn('목적지 추가', 'primary')),
    pad='16px')

REF_PILL = (f'<span style="display: inline-block; margin-bottom: 8px; font-size: 11px; font-weight: 600; '
            f'letter-spacing: 0.02em; color: {C["INK2"]}; border: 1px solid {C["LINE"]}; background: {C["SURF"]}; '
            f'border-radius: 99px; padding: 4px 10px; white-space: nowrap;">구현 참고 · 앱 화면이 아닙니다</span>')
BODY_CSS = '-webkit-font-smoothing: antialiased; }'

BLOCKS = [
    ('A · 필수 값 미입력 — 저장을 누르면 빠진 칸을 알려 줌', a),
    ('B · 직접 정한 카테고리 합계가 총한도보다 큼', b),
    ('C · 저장 중 — 입력 잠금', c),
    ('D · 저장 실패 — 실패한 자리 옆에 한 번', d),
    ('E · 저장 알림 — 6초 카드 → 한 줄 띠', e),
    ('F · 저장하지 않고 닫기', f),
    ('G · 부채 상환 목적지 — 넣어 둔 부채가 없을 때', g),
]

if __name__ == '__main__':
    import sys
    # 높이 = 실제 웹폰트로 잰 자연 높이 + 24(2026-09-25 · 7종 · gen_canvas TALL · screens.json 과 같게).
    # 예전 호출(`gen_errors.py 2100`)의 숫자는 이 값보다 작으면 무시한다 — 소리 없이 잘리지 않게.
    H = 3290      # 2026-09-27 fix-up 5 자연 3266 + 24(E 띠 설명 줄)
    h = max(int(sys.argv[1]), H) if len(sys.argv) > 1 else H
    body = state_sheet(
        '모달 오류 · 저장 상태 7종',
        '저장이 막히거나 실패했을 때 보이는 창 일곱 가지입니다. 실제로는 한 번에 하나만 보입니다.',
        BLOCKS, h=h)
    # 구현 참고용 시트: 제목 위에 알약을 끼운다(state_sheet 는 공용이라 그대로 둔다).
    assert body.count('<h2 ') == 1
    body = body.replace('<h2 ', REF_PILL + '<h2 ', 1)
    html = doc(body)
    # 설명 문장이 많은 참고 시트는 한국어 낱말이 중간에서 끊기지 않게 한다.
    assert html.count(BODY_CSS) == 1
    html = html.replace(BODY_CSS, BODY_CSS[:-1] + 'word-break: keep-all; }')
    (OUT / 'ModalErrors.dc.html').write_text(html, encoding='utf-8')
    print('ModalErrors.dc.html written, h =', h)
