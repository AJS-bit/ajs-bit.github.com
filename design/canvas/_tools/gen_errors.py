# -*- coding: utf-8 -*-
"""모달의 오류·저장 상태 카탈로그 아트보드."""
import pathlib
from gen_common import (C, icon, doc, state_sheet, card, field, note, btn,
                        smallbtn, section_head, badge, bar)

OUT = pathlib.Path('/home/user/ajs-bit.github.com/design/canvas')


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


# ── A · 필수 값 미입력 ────────────────────────────────────────────────
a = card(
    modal_head('거래 추가', '9월 8일') +
    '<div style="display: flex; gap: 10px;">' +
    field('금액', placeholder('0'), unit='원', required=True, state='error',
          helper='금액을 입력해 주세요') +
    '</div>' +
    '<div style="display: flex; gap: 10px; margin-top: 13px;">' +
    field('카테고리', '식비', w=None) +
    '</div>' +
    '<div style="margin-top: 13px;">' +
    note('<b style=font-weight:600>0원과 미입력은 다릅니다.</b> 0원을 저장하면 그날 소비가 0원으로 기록되고, '
         '비워 두면 아무것도 기록되지 않습니다.', 'mute') +
    '</div>' +
    footer(btn('취소', 'secondary'), btn('저장', 'disabled')),
    pad='16px')

# ── B · 값이 규칙에 어긋남 ────────────────────────────────────────────
over_bar = (f'<div style="position: relative; height: 10px; border-radius: 99px; background: {C["TRACK"]}; margin-top: 10px;">'
            f'<div style="position: absolute; inset: 0 8.5% 0 0; border-radius: 99px 0 0 99px; background: {C["BRAND"]};"></div>'
            f'<div style="position: absolute; right: 0; top: 0; bottom: 0; width: 8.5%; border-radius: 0 99px 99px 0; '
            f'background: repeating-linear-gradient(135deg, {C["NEG"]} 0 4px, #E0908C 4px 8px);"></div>'
            f'<div style="position: absolute; left: 91.5%; top: -5px; width: 2px; height: 20px; border-radius: 2px; background: {C["INK"]};"></div></div>'
            f'<div style="display: flex; justify-content: space-between; margin-top: 7px;">'
            f'<span style="font-size: 11px; color: {C["INK3"]};">배분 합 <b style=font-weight:600>236만원</b></span>'
            f'<span style="font-size: 11px; font-weight: 600; color: {C["NEG"]};">총한도 216만원 &middot; 20만원 초과</span></div>')

b = card(
    modal_head('카테고리 배분 편집', '13개') +
    '<div style="display: flex; align-items: center; justify-content: space-between; gap: 10px;">' +
    field('식비', '65', unit='만원', state='error', helper='이 값을 넣으면 배분 합이 총한도를 넘습니다') +
    '</div>' +
    over_bar +
    f'<div style="margin-top: 13px;">' +
    note('총한도를 넘는 배분은 저장할 수 없습니다. 아래 중 하나를 고르거나 다른 카테고리를 줄여 주세요.', 'neg', 'warn') +
    '</div>'
    f'<div style="display: flex; flex-direction: column; gap: 7px; margin-top: 11px;">'
    f'{choice("식비를 45만원으로 되돌리기", "배분 합 216만원")}'
    f'{choice("총한도를 236만원으로 올리기", "실수령 급여의 65.6%")}</div>' +
    footer(btn('취소', 'secondary'), btn('저장', 'disabled')),
    pad='16px')

# ── C · 저장 중 ──────────────────────────────────────────────────────
c = card(
    modal_head('자산 추가') +
    f'<div style="opacity: .55;">'
    '<div style="display: flex; gap: 10px;">' +
    field('이름', '주택청약') + field('금액', '1,860', unit='만원', w=150) +
    '</div></div>' +
    f'<div style="margin-top: 13px;">' + note('기기에 저장하는 중이에요. 창을 닫아도 저장은 계속됩니다.', 'mute', 'loader') + '</div>' +
    f'<div style="display: flex; gap: 9px; margin-top: 14px; padding-top: 13px; border-top: 1px solid {C["LINE_SOFT"]};">'
    f'{btn("취소", "disabled").replace("width: 100%;", "flex: 1;")}{saving_btn()}</div>',
    pad='16px')

# ── D · 저장 실패 ────────────────────────────────────────────────────
d = card(
    f'<div style="display: flex; gap: 12px;">'
    f'<div style="width: 40px; height: 40px; border-radius: 13px; background: {C["NEG_SOFT"]}; display: flex; '
    f'align-items: center; justify-content: center; flex-shrink: 0;">{icon("warn", 20, C["NEG"], 2)}</div>'
    f'<div style="min-width: 0;">'
    f'<div style="font-size: 16px; font-weight: 700; letter-spacing: -0.02em; color: {C["INK"]};">저장하지 못했어요</div>'
    f'<div style="font-size: 12.5px; line-height: 1.55; color: {C["INK2"]}; margin-top: 5px;">'
    f'기기 저장소에 쓸 수 없습니다. <b style=font-weight:600>입력한 값은 화면에 그대로 있으니</b> 다시 시도해 주세요.</div></div></div>'
    f'<div style="margin-top: 12px;">' +
    note('저장 공간이 부족할 수 있어요. 계속 실패하면 백업 파일로 내보낸 뒤 공간을 확보해 주세요.', 'mute') +
    '</div>'
    f'<div style="display: flex; gap: 9px; margin-top: 14px;">'
    f'{btn("다시 저장", ic="refresh").replace("width: 100%;", "flex: 1.4;")}'
    f'{btn("백업 내보내기", "secondary", ic="download").replace("width: 100%;", "flex: 1;")}</div>',
    pad='16px')

# ── E · 저장 완료 ────────────────────────────────────────────────────
e = card(
    f'<div style="display: flex; align-items: center; gap: 12px;">'
    f'<div style="width: 38px; height: 38px; border-radius: 99px; background: {C["POS_SOFT"]}; display: flex; '
    f'align-items: center; justify-content: center; flex-shrink: 0;">{icon("check", 19, C["POS"], 2.6)}</div>'
    f'<div style="flex: 1; min-width: 0; font-size: 15px; font-weight: 700; letter-spacing: -0.02em; color: {C["INK"]};">저장했어요</div>'
    f'{badge("되돌리기", "mute", "refresh")}</div>'
    f'<div style="font-size: 12px; color: {C["INK3"]}; margin-top: 7px;">식비 12,000원 &middot; 남은 한도 103만원 &middot; 사용 113만원</div>'
    f'<div style="position: relative; height: 3px; border-radius: 99px; background: {C["TRACK"]}; margin-top: 13px;">'
    f'<div style="position: absolute; inset: 0 62% 0 0; border-radius: 99px; background: {C["POS"]};"></div></div>'
    f'<div style="font-size: 11px; color: {C["INK4"]}; margin-top: 6px;">2초 후 자동으로 닫혀요</div>',
    pad='16px')

# ── F · 저장하지 않고 닫기 ────────────────────────────────────────────
f = card(
    f'<div style="font-size: 16px; font-weight: 700; letter-spacing: -0.02em; color: {C["INK"]};">저장하지 않고 닫을까요?</div>'
    f'<div style="font-size: 12.5px; line-height: 1.55; color: {C["INK2"]}; margin-top: 6px;">'
    f'금액과 카테고리를 입력했지만 아직 저장하지 않았습니다. 닫으면 입력한 내용이 사라집니다.</div>'
    f'<div style="display: flex; gap: 9px; margin-top: 15px;">'
    f'{btn("계속 입력", "secondary").replace("width: 100%;", "flex: 1;")}'
    f'{btn("저장하지 않고 닫기", "danger").replace("width: 100%;", "flex: 1.3;")}</div>',
    pad='16px')

BLOCKS = [
    ('A · 필수 값 미입력 — 저장 비활성', a),
    ('B · 값이 규칙에 어긋남 — 배분 합 초과', b),
    ('C · 저장 중 — 입력 잠금', c),
    ('D · 저장 실패 — 입력값 보존', d),
    ('E · 저장 완료 — 무엇이 바뀌었는지', e),
    ('F · 저장하지 않고 닫기', f),
]

if __name__ == '__main__':
    import sys
    h = int(sys.argv[1]) if len(sys.argv) > 1 else 1800
    body = state_sheet(
        '모달 오류 · 저장 상태 6종',
        '오류는 무엇이 잘못됐는지와 어떻게 고치는지를 같이 말합니다. 실패해도 입력한 값은 지우지 않습니다.',
        BLOCKS, h=h)
    (OUT / 'ModalErrors.dc.html').write_text(doc(body), encoding='utf-8')
    print('ModalErrors.dc.html written, h =', h)
