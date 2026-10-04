# -*- coding: utf-8 -*-
import brand_mark
import pathlib
import re
from gen_common import *

OUT = pathlib.Path(__file__).resolve().parent.parent


KEEP_ALL_FROM = '-webkit-font-smoothing: antialiased; }'
KEEP_ALL_TO = '-webkit-font-smoothing: antialiased; word-break: keep-all; }'


def w(name, body, keep_all=False):
    """keep_all=True 면 body 에 word-break: keep-all 을 넣어 한글이 낱말 중간에서 갈라지지 않게 한다."""
    html = doc(body)
    if keep_all:
        assert html.count(KEEP_ALL_FROM) == 1
        html = html.replace(KEEP_ALL_FROM, KEEP_ALL_TO)
    (OUT / f'{name}.dc.html').write_text(html, encoding='utf-8')
    print('wrote', name)


# ══════════════ 1. 첫 실행 · 시작 방법 고르기 ══════════════
# 앱 components/navi/data-choice-screen.tsx(a724aac · first-run-19 · D8 · AMEND 1). 흐름 = 소개 3장 → 홈 구성 → 이 화면(‹ 뒤로 = 홈 구성) → 홈.
# 문구는 안드로이드 앱(DATA_CHOICE_COPY.native) — 웹 문구(「이 브라우저에만 저장해요」 · 「브라우저 데이터를 지우면 …」)는 캔버스 노트에 적는다.
NAV_ARROW = '<path d="m3 11 19-9-9 19-2-8-8-2Z"/>'


def choice(title, body, ic_svg, primary):
    # 앱 data-choice-screen 실측(2026-09-27 fix-up): 칸 16 · 간격 12 · 제목 600 / -0.015em · 설명 13 / 1.45(위 여백 없음) · 파란 칸 설명은 흰색
    bg, bd, fg, sub, tile, chev = ((C["BRAND"], 'none', '#FFFFFF', '#FFFFFF', 'rgba(255,255,255,.18)', '#FFFFFF') if primary else
                                   (C["SURF"], f'1px solid {C["LINE"]}', C["INK"], C["INK3"], C["INSET"], C["INK3"]))
    # 2026-09-27 fix-up 2: 앱 .v4-data-choice-option { min-height: 84px } · 제목 줄 높이 1.35 + 설명 위 3(앱 글 묶음 · 같은 높이)
    return (f'<div style="display: flex; align-items: center; gap: 12px; min-height: 84px; padding: 16px; border-radius: 18px; background: {bg}; border: {bd};">'
            f'<div style="width: 40px; height: 40px; border-radius: 12px; background: {tile}; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">{ic_svg}</div>'
            f'<div style="flex: 1; min-width: 0;"><div style="font-size: 16px; font-weight: 600; line-height: 1.35; letter-spacing: -0.015em; color: {fg};">{title}</div>'
            f'<div style="font-size: 13px; line-height: 1.45; color: {sub}; margin-top: 3px;">{body}</div></div>'
            f'{icon("right", 18, chev, 2)}</div>')


# 앱 아이콘 WalletCards(lucide wallet-cards)
WALLET_CARDS = ('<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round">'
                '<rect width="18" height="18" x="3" y="3" rx="2"/><path d="M3 9a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2"/>'
                '<path d="M3 11h3c.8 0 1.6.3 2.1.9l1.1.9c1.6 1.6 4.1 1.6 5.7 0l1.1-.9c.5-.5 1.3-.9 2.1-.9H21"/></svg>')
w('Onboarding', frame(
    f'<div style="flex: 1; min-height: 0; display: flex; flex-direction: column; padding: 0 20px; overflow: hidden;">'
    f'<div style="display: flex; align-items: center; gap: 8px; height: 56px; margin-top: 8px; flex-shrink: 0;">'
    f'<span style="width: 32px; height: 44px; margin-left: -6px; display: inline-flex; align-items: center; justify-content: center; flex-shrink: 0;">{icon("left", 22, C["INK2"], 2)}</span>'      # 앱 뒤로 버튼 32 폭 · x 14 → 마크 x 54(2026-09-27 fix-up 3 · 예전 44 · 마크 x 60)
    f'<div style="width: 32px; height: 32px; border-radius: 10px; background: linear-gradient(140deg, #3556E6 0%, #7A3FE4 100%); '
    f'display: flex; align-items: center; justify-content: center; flex-shrink: 0;">'
    f'{brand_mark.svg(32)}</div>'
    f'<span style="font-size: 12px; font-weight: 500; color: {C["INK3"]};">시작 방법 고르기</span></div>'
    f'<h1 style="margin: 6px 0 0; font-size: 22px; font-weight: 700; letter-spacing: -0.03em; line-height: 1.35; color: {C["INK"]};">어떤 데이터로 시작할까요?</h1>'
    f'<p style="margin: 6px 0 0; font-size: 13.5px; line-height: 1.5; color: {C["INK2"]};">'
    f'NAVI는 인터넷 없이 실행되고, 자산 · 소비 · 목적지를 이 기기에 암호화해 저장해요. 샘플은 기능을 둘러보는 가상 데이터예요.</p>'
    f'<div style="display: flex; flex-direction: column; gap: 10px; margin-top: 20px;">'
    + choice('내 데이터로 시작', '월급과 첫 소비부터 가볍게 시작해요.', WALLET_CARDS, True)
    + choice('샘플로 둘러보기', '가상의 직장인 데이터로 모든 기능을 둘러봐요.',
             f'<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="{C["INK2"]}" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round">{NAV_ARROW}</svg>', False)
    + f'</div>'
    f'<div style="height: 1px; background: {C["LINE"]}; margin: 20px 2px 0;"></div>'
    f'<p style="margin: 16px 2px 0; font-size: 13px; line-height: 1.6; color: {C["INK3"]};">'
    f'앱을 삭제하거나 앱 데이터를 지우면 기록도 사라져요. 기기를 바꾸기 전에 설정에서 백업 파일을 저장해 주세요.</p>'
    f'</div>'), keep_all=True)


# ══════════════ 2. 저장소 로딩 · 실패 · 복구 ══════════════
def big_state(ic, icol, ibg, title, body, actions, extra=""):
    return card(
        f'<div style="display: flex; flex-direction: column; align-items: center; text-align: center; padding: 6px 4px;">'
        f'<div style="width: 48px; height: 48px; border-radius: 15px; background: {ibg}; display: flex; align-items: center; justify-content: center;">{icon(ic, 24, icol, 2)}</div>'
        f'<div style="font-size: 16px; font-weight: 700; letter-spacing: -0.02em; color: {C["INK"]}; margin-top: 13px;">{title}</div>'
        f'<div style="font-size: 12.5px; line-height: 1.55; color: {C["INK2"]}; margin-top: 6px;">{body}</div>'
        f'{extra}<div style="display: flex; gap: 8px; width: 100%; margin-top: 15px;">{actions}</div></div>', pad="18px 16px")


DEBTS_H = 909      # 자연 높이 885 + 24(범례 두 줄 · 이번 달 상환 예정까지)
PAYOFF_H = 924      # 자연 높이 900 + 24(저장된 상환 계획이에요 카드까지)
GOALDESIGN_H = 1231      # 자연 높이 1207 + 24(저장하면 이렇게 바뀌어요 · 다른 금액으로 계산해 보기까지 · 추천 칸 120 × 126 앱 실측)
GOALSSTATES_H = 4432      # 2026-09-27 fix-up 3 자연 4408 + 24(A 가정 줄 여백 · D ① 목록 카드를 따로) · 2026-09-27 fix-up 2 자연 4364 + 24(D ① 식 줄 · 홈 여유 안내 · D ③ 펼친 부채 목적지 칸 넷) · 자연 높이 4051 + 24(2026-09-27 fix-up · D ① ~ ④ · C 목적지 추가) · 예전 2706 + 24
GOALDESIGNSTATES_H = 1421      # 자연 높이 1397 + 24
STORAGE_H = 2787      # 자연 높이 2763 + 24(2026-09-30 A 마크 줄 32 → 40 · 앱 저장소 화면) · 2026-09-27 fix-up 2 자연 2755 + 24(실제 웹폰트로 잼 · 가져오기 오류 줄 가운데 · 아이콘 없음)
REF_PILL = (f'<span style="display: inline-block; margin-bottom: 8px; font-size: 11px; font-weight: 600; letter-spacing: 0.02em; '
            f'color: {C["INK2"]}; border: 1px solid {C["LINE"]}; background: {C["SURF"]}; border-radius: 99px; padding: 4px 10px; '
            f'white-space: nowrap;">구현 참고 · 앱 화면이 아닙니다</span>')

# 앱 components/navi/storage-error-screen.tsx · app/page.tsx(a724aac · a11y-5 · first-run-22 · D8 · D10 · a11y-17).
# 확인 창은 앱 AlertDialog 모양 — 아이콘 칸 없이 가운데 제목 · 본문, 옅은 띠의 바닥, 390 폭에서 버튼은 세로(주 행동 먼저).
def brand_row():
    """A · 불러오는 중 위의 마크 줄 — 앱 저장소 화면(StorageLoadingScreen · StorageErrorView)의 `.setup-brand .brand-mark` 는 40 × 40 ·
    모서리 11(globals.css `.brand-mark` 40 · 뒤의 `.brand-mark` 가 모서리를 --radius-control 11 로 · svg 100% — 2026-09-30 앱 번들 실측 ·
    SPEC §2 「저장소 화면 40」). 예전 판은 머리줄 크기 32 로 줄여 그렸다. 「NAVI」 글자(17 · 사이 9)는 예전 그대로다(앱은 23 · 0.09em · 사이 11)."""
    return (f'<div style="display: flex; align-items: center; gap: 9px; padding: 2px 4px 4px;">'
            f'{brand_mark.tile(40, 11)}'
            f'<span style="font-size: 17px; font-weight: 700; letter-spacing: 0.06em; color: {C["INK"]};">NAVI</span></div>')


def err_card(extra_under_primary='', start_enabled=False, tail=''):
    """B · 불러오기 실패 — 원본 저장(주) · 백업으로 복구 · 새로 시작(원본 저장 전엔 꺼짐) · 다시 불러오기(글자 버튼)."""
    start_btn = (btn('새로 시작', 'secondary', h=44) if start_enabled else
                 btn('새로 시작', 'disabled', h=44) + f'<div style="font-size: 11.5px; line-height: 1.45; color: {C["INK3"]}; margin-top: -2px;">원본을 파일로 저장한 뒤에 새로 시작할 수 있어요</div>')
    return card(
        f'<div style="display: flex; flex-direction: column; align-items: center; text-align: center; padding: 6px 4px 2px;">'
        f'<div style="width: 44px; height: 44px; border-radius: 14px; background: {C["NEG_SOFT"]}; display: flex; align-items: center; justify-content: center;">{icon("warn", 22, C["NEG"], 2)}</div>'
        f'<div style="font-size: 16px; font-weight: 700; letter-spacing: -0.02em; color: {C["INK"]}; margin-top: 12px;">저장된 기록을 불러오지 못했어요</div>'
        f'<div style="font-size: 12.5px; line-height: 1.55; color: {C["INK2"]}; margin-top: 6px;">기기에 저장된 기록을 읽지 못했어요. 원본은 지우지 않고 그대로 두었어요.</div>'
        f'<div style="display: flex; flex-direction: column; gap: 8px; width: 100%; margin-top: 15px;">'
        f'{btn("원본을 파일로 저장", "primary", h=44)}{extra_under_primary}{btn("백업으로 복구", "secondary", h=44)}{start_btn}</div>'
        f'<span style="font-size: 13px; font-weight: 600; color: {C["BRAND"]}; margin-top: 12px;">다시 불러오기</span>{tail}</div>', pad="18px 16px")


def alert_dialog(title, body, buttons):
    """앱 AlertDialog — 가운데 제목 · 본문, 1px 선 위 옅은 띠에 버튼을 세로로."""
    return (f'<div style="background: {C["SURF"]}; border: 1px solid {C["LINE"]}; border-radius: 20px; overflow: hidden; '
            f'box-shadow: 0 16px 40px -18px rgba(16,24,40,.35);">'
            f'<div style="padding: 20px 18px 16px; text-align: center;">'
            f'<div style="font-size: 16px; font-weight: 700; letter-spacing: -0.02em; line-height: 1.4; color: {C["INK"]};">{title}</div>'
            f'<div style="font-size: 12.5px; line-height: 1.55; color: {C["INK2"]}; margin-top: 6px;">{body}</div></div>'
            f'<div style="display: flex; flex-direction: column; gap: 8px; padding: 12px 14px 14px; background: {C["INSET"]}; border-top: 1px solid {C["LINE"]};">{buttons}</div></div>')


def cap(t):
    return f'<div style="font-size: 11.5px; line-height: 1.5; color: {C["INK3"]}; padding: 0 4px;">{t}</div>'


def grey_btn(label):
    """앱 AlertDialogCancel — 회색 채움(Confirmations 의 「취소」와 같은 색 · 2026-09-27 fix-up 2 · 예전 흰 외곽선)."""
    return btn(label, 'secondary', h=44).replace('background: #FFFFFF; border: 1px solid #D7DEEA; color: #475467;', f'background: #E8ECF5; border: none; color: {C["INK"]};')


def err_line(text):
    """앱 가져오기 오류 줄 — 아이콘 없이 가운데 맞춘 옅은 빨강 상자(storage-error-screen · 2026-09-27 fix-up 2)."""
    return (f'<div role="alert" style="padding: 10px 12px; background: {C["NEG_SOFT"]}; border-radius: 12px; text-align: center; '
            f'font-size: 12px; line-height: 1.5; color: #7C221E;">{text}</div>')


SAVED_LINE = f'<div style="font-size: 12px; font-weight: 600; color: {C["POS"]}; margin-top: -2px;">원본을 파일로 저장했어요</div>'
FAIL_LINE = (f'<div style="font-size: 12px; line-height: 1.45; color: {C["NEG"]}; margin-top: -2px;">원본을 파일로 저장하지 못했습니다. 다시 눌러 보세요.</div>')

w('StorageStates', state_sheet(
    '저장소 로딩 · 실패 · 복구',
    '기록을 불러오거나 복구할 때 생길 수 있는 경우입니다. 실제로는 한 번에 하나만 보입니다.',
    [('A · 불러오는 중',
      brand_row() +
      card(f'<div style="display: flex; flex-direction: column; align-items: center; text-align: center; padding: 14px 4px;">'
           f'<div style="width: 44px; height: 44px; border-radius: 99px; border: 3px solid {C["TRACK"]}; border-top-color: {C["BRAND"]};"></div>'
           f'<div style="font-size: 14px; font-weight: 600; color: {C["INK"]}; margin-top: 14px;">저장된 기록을 불러오는 중</div>'
           f'<div style="font-size: 12px; color: {C["INK3"]}; margin-top: 4px;">잠시만 기다려 주세요</div></div>', pad="18px 16px")),
     ('B · 불러오기 실패', err_card()),
     ('B′ · 원본을 파일로 저장한 뒤',
      err_card(SAVED_LINE, start_enabled=True) +
      cap('「새로 시작」을 누르면 한 번 더 묻습니다. 원본을 저장하지 못하면 주 버튼 아래에 빨간 줄이 한 번 뜹니다(role=alert).') +
      card(f'<div style="display: flex; flex-direction: column; gap: 8px;">{btn("원본을 파일로 저장", "primary", h=44)}{FAIL_LINE}</div>', pad="12px 14px") +
      alert_dialog('새로 시작할까요?', '저장해 둔 원본 파일은 그대로 있어요. 앱의 기록은 비우고 처음 설정부터 시작해요.',
                   btn('새로 시작', 'primary', h=44) + grey_btn('취소')) +
      cap('원본 저장에 두 번 실패한 뒤에는 확인 창이 빨간 쪽으로 바뀝니다.') +
      alert_dialog('새로 시작할까요?', '원본을 파일로 저장하지 못했어요. 새로 시작하면 이 기기에 남은 기록은 되살릴 수 없어요.',
                   btn('그래도 새로 시작', 'danger', h=44) + grey_btn('취소'))),
     ('C · 백업 파일을 읽지 못함 — 같은 화면 안의 오류 줄',
      err_card(tail=f'<div style="width: 100%; margin-top: 13px; text-align: left;">'
               + err_line('백업 파일을 읽지 못했습니다. NAVI 또는 자산 나침반의 JSON 백업을 골라 주세요. 지금 기록은 그대로예요.') + '</div>') +
      cap('읽을 수 있는 백업을 고르면 이 카드 아래에 「백업 불러오기」가 열립니다 — 「{파일} · 저장 전에 무엇이 바뀌는지 먼저 봐요.」 · 불러올 항목 · 지금 → 적용 후 · '
          '「데이터 종류와 적용 후 내역을 확인했어요.」 · 취소 / 「이 내용으로 적용」(확인 전엔 회색). 바로 덮어쓰지 않아요.')),
     ('D · 샘플에서 내 데이터로 전환',
      alert_dialog('샘플을 치우고 내 데이터로 시작할까요?', '지금 보는 샘플만 지워져요. 샘플은 백업되지 않아요.',
                   btn('내 데이터로 시작', 'primary', h=44) + grey_btn('계속 둘러보기')) +
      cap('샘플 모드 맨 위 띠 「샘플 데이터로 둘러보는 중 · 내 데이터로 시작 ›」에서 열립니다. 「내 데이터로 시작」을 누르면 월급 입력 시트가 열려요.'))],
    h=STORAGE_H).replace('<h2 ', REF_PILL + '<h2 ', 1), keep_all=True)


def kvrow(k, v, vcol, strong=False, last=False):
    return (f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px; min-height: 40px; '
            f'{"" if last else "border-bottom: 1px solid " + C["LINE_ROW"] + ";"}">'
            f'<span style="font-size: 13px; font-weight: {600 if strong else 400}; color: {C["INK"] if strong else C["INK2"]};">{k}</span>'
            f'<span style="font-size: {15 if strong else 13.5}px; font-weight: 600; letter-spacing: -0.02em; color: {vcol};">{v}</span></div>')


# ══════════════ 3. 자산 › 부채 ══════════════
# 앱 asset-view.tsx(a724aac · assets-23 유형 이름 · goals-21 평균 금리 · D4 · D6). 행 아래줄 = 「{유형} · 월 최소 N만원」(상환 방식 · 잔여 회차 없음).
DEBTS = [("주택담보대출", "주택담보 · 전세대출", 6200, "3.4", 32, C["INK"]),
         ("신용대출", "신용대출", 2200, "6.8", 20, C["INK"]),
         ("학자금대출", "학자금", 280, "2.5", 5, C["INK"]),
         ("카드 할부", "카드/리볼빙", 180, "14.5", 20, C["NEG"])]
DEBT_MIX = [("주택담보 · 전세대출", 70, "#94a3b8"), ("신용대출", 25, "#f59e0b"), ("학자금", 3, "#64748b"), ("카드/리볼빙", 2, C["NEG"])]
rows = []
for i, (name, meta, bal, rate, minpay, col) in enumerate(DEBTS):
    hi = badge('최고 금리', 'neg') if col == C["NEG"] else ''          # 금리가 있는 부채가 둘 이상일 때 가장 높은 것 하나
    rows.append(
        f'<div style="display: flex; align-items: center; gap: 10px; min-height: 52px; '
        f'{"border-bottom: 1px solid " + C["LINE_SOFT"] + ";" if i < len(DEBTS) - 1 else ""}">'
        f'<div style="flex: 1; min-width: 0;">'
        f'<div style="display: flex; align-items: center; gap: 6px;">'
        f'<span style="font-size: 13.5px; font-weight: 600; color: {C["INK"]};">{name}</span>{hi}</div>'
        f'<div style="font-size: 11px; color: {C["INK3"]}; margin-top: 2px;">{meta} · 월 최소 {minpay}만원</div></div>'
        f'<div style="text-align: right;">{amount(f"{bal:,}")}'
        f'<div style="font-size: 11.5px; font-weight: 600; color: {col};">연 {rate}%</div></div>'
        f'{icon("more", 16, C["INK4"], 2.2)}</div>')
legend = ''.join(f'<span style="display: inline-flex; align-items: center; gap: 5px; font-size: 11px; color: {C["INK2"]}; white-space: nowrap;">'
                 f'<span style="width: 8px; height: 8px; border-radius: 99px; background: {c}; flex-shrink: 0;"></span>{t} {v}%</span>'
                 for t, v, c in DEBT_MIX)

w('Debts', frame(
    screen_header('자산', tabs=['자산 구성', '부채', '상환 계획'], active=1) +
    content([
        hero(eyebrow_row('총부채', badge('평균 금리 연 4.4%', 'mute')) +
             f'<div style="display: flex; align-items: flex-end; justify-content: space-between; gap: 10px; margin-top: 6px;">'
             f'<div style="display: flex; align-items: baseline; gap: 2px;">'
             f'<span style="font-size: 38px; font-weight: 700; letter-spacing: -0.04em; line-height: 1.05; color: {C["INK"]};">8,860</span>'
             f'<span style="font-size: 19px; font-weight: 600; color: {C["INK2"]};">만원</span></div>'
             f'<div style="display: flex; flex-direction: column; align-items: flex-end; gap: 1px; padding-bottom: 3px;">'
             f'<span style="font-size: 11px; font-weight: 500; color: {C["INK3"]};">월 최소 상환</span>'
             f'<span style="font-size: 17px; font-weight: 600; letter-spacing: -0.02em; color: {C["INK"]};">77만원</span></div></div>'
             f'<div style="display: flex; height: 10px; border-radius: 99px; overflow: hidden; margin-top: 14px; gap: 2px;">'
             + ''.join(f'<div style="width: {v}%; background: {c};"></div>' for _, v, c in DEBT_MIX) +
             f'</div>'
             f'<div style="display: flex; align-items: flex-start; justify-content: space-between; gap: 10px; margin-top: 8px;">'
             f'<div style="display: flex; flex-wrap: wrap; gap: 4px 11px; min-width: 0;">{legend}</div>'
             f'<span style="font-size: 11px; color: {C["INK3"]}; white-space: nowrap; flex-shrink: 0;">총자산의 48.7%</span></div>'),
        guidance('warn', '상환 안내', '카드 할부 · 연 14.5%',
                 '금리와 잔액에 따라 갚는 순서가 달라져요. 상환 방식은 상환 계획에서 비교해요.', '상환 계획 보기'),
        card(section_head('부채 4건', '8,860만원', smallbtn('추가', 'soft', 'plus')) +
             f'<div style="display: flex; flex-direction: column; margin-top: 6px;">{"".join(rows)}</div>'),
        card(f'<div style="display: flex; align-items: baseline; justify-content: space-between; gap: 8px;">'
             f'<span style="font-size: 13.5px; font-weight: 600; color: {C["INK"]};">이번 달 상환 예정</span>'
             f'<span style="font-size: 15px; font-weight: 600; letter-spacing: -0.02em; color: {C["INK"]};">92만원</span></div>'
             f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px; margin-top: 6px;">'
             f'<span style="font-size: 11.5px; color: {C["INK3"]};">최소 77만원 + 추가 15만원</span>'
             f'<span style="font-size: 11.5px; color: {C["INK3"]};">소비율에는 포함되지 않아요</span></div>', pad="13px 14px"),
    ], gap=10) + bottomnav(1), h=DEBTS_H), keep_all=True)


# ══════════════ 4. 자산 › 상환 계획 (읽기 전용 요약) ══════════════
# D6 · future-7: 상환 방식 · 월 추가 상환액은 미래 › 상환 계획에서만 바꾼다. 여기는 저장된 계획의 요약 + 「상환 계획 바꾸기 ›」.
# 숫자 = NUMBERS §9(앱 달 규칙 — 다 갚는 달 2036년 5월 · 카드 2027년 3월 · 신용 2030년 11월 · 학자금 2031년 9월) · 비교 문장 D15.
order = []
for i, (name, eta) in enumerate([("카드 할부", "2027년 3월 다 갚음"),
                                  ("신용대출", "2030년 11월 다 갚음"),
                                  ("학자금대출", "2031년 9월 다 갚음"),
                                  ("주택담보대출", "2036년 5월 다 갚음")]):
    order.append(
        f'<div style="display: flex; align-items: center; gap: 11px; min-height: 46px; '
        f'{"border-bottom: 1px solid " + C["LINE_SOFT"] + ";" if i < 3 else ""}">'
        f'<span style="width: 22px; height: 22px; border-radius: 99px; background: {C["BRAND_SOFT"] if i == 0 else C["TRACK"]}; '
        f'color: {C["BRAND"] if i == 0 else "#606B7D"}; font-size: 11.5px; font-weight: 700; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">{i+1}</span>'
        f'<span style="flex: 1; font-size: 13.5px; font-weight: 600; color: {C["INK"]};">{name}</span>'
        f'<span style="font-size: 12px; color: {C["INK3"]}; white-space: nowrap;">{eta}</span></div>')

w('Strategy', frame(
    screen_header('자산', tabs=['자산 구성', '부채', '상환 계획'], active=2) +
    content([
        hero(eyebrow_row('저장된 상환 계획', badge('저장된 계획', 'pos', 'check')) +
             f'<div style="font-size: 16.5px; font-weight: 700; letter-spacing: -0.02em; color: {C["INK"]}; margin-top: 10px;">고금리 우선 · 월 추가 15만원</div>'
             f'<div style="font-size: 12.5px; color: {C["INK2"]}; margin-top: 4px;">최소 77만원 + 추가 15만원 = 매월 92만원</div>'
             f'<div style="margin-top: 14px;">{btn("상환 계획 바꾸기 ›", "secondary", h=44).replace(C["INK2"] + "; font-size", C["BRAND"] + "; font-size")}</div>'),
        card(f'<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 0;">'
             f'<div style="padding-right: 12px;">'
             f'<div style="font-size: 11.5px; font-weight: 500; color: {C["INK3"]};">다 갚는 달</div>'
             f'<div style="font-size: 21px; font-weight: 600; letter-spacing: -0.025em; color: {C["INK"]}; margin-top: 3px;">2036년 5월</div>'
             f'<div style="font-size: 11px; color: {C["INK3"]}; margin-top: 2px;">9년 8개월 뒤</div></div>'
             f'<div style="padding-left: 12px; border-left: 1px solid {C["LINE_SOFT"]};">'
             f'<div style="font-size: 11.5px; font-weight: 500; color: {C["INK3"]};">총이자</div>'
             f'<div style="font-size: 21px; font-weight: 600; letter-spacing: -0.025em; color: {C["INK"]}; margin-top: 3px;">1,734만원</div>'
             f'<div style="font-size: 11px; line-height: 1.45; font-weight: 600; color: {C["POS"]}; margin-top: 2px;">소액 우선보다 이자 30만원 덜 내요</div></div></div>'),
        card(section_head('갚는 순서', '고금리 우선') +
             f'<div style="display: flex; flex-direction: column; margin-top: 6px;">{"".join(order)}</div>'),
    ]) + bottomnav(1)), keep_all=True)


# ══════════════ 5. 소비 › 내역 (모바일) ══════════════
def tx(cat, ic, memo, link_txt, amt, badges="", muted=False):
    col = C["INK2"] if muted else C["INK"]
    b = f'<span style="display: inline-flex; gap: 5px; margin-left: 6px;">{badges}</span>' if badges else ''
    return (f'<div style="display: flex; align-items: center; gap: 11px; min-height: 54px; border-top: 1px solid {C["LINE_ROW"]};">'
            f'{caticon(cat, ic, 34)}'
            f'<div style="flex: 1; min-width: 0;">'
            f'<div style="font-size: 13.5px; font-weight: 500; color: {C["INK"]};">{memo}{b}</div>'
            f'<div style="font-size: 11px; color: {C["INK3"]}; margin-top: 2px;">{cat} · {link_txt}</div></div>'
            f'<span style="font-size: 14.5px; font-weight: 600; letter-spacing: -0.02em; color: {col};">{amt}</span>'
            f'{icon("more", 16, C["INK4"], 2.2)}</div>')


minib = lambda t, tone: (f'<span style="font-size: 10px; font-weight: 600; color: '
                         f'{C["TAB_INK"] if tone == "mute" else C["BRAND"]}; background: '
                         f'{C["LINE_SOFT"] if tone == "mute" else C["BRAND_SOFT"]}; border-radius: 5px; padding: 2px 5px;">{t}</span>')

daygroup = lambda d, w_, s: (f'<div style="display: flex; align-items: baseline; justify-content: space-between; gap: 10px; padding: 12px 0 6px;">'
                             f'<span style="font-size: 13px; font-weight: 600; color: {C["INK"]};">{d} '
                             f'<span style="font-weight: 500; color: {C["INK3"]};">{w_}</span></span>'
                             f'<span style="font-size: 12.5px; font-weight: 600; color: {C["INK2"]}; white-space: nowrap;">{s}</span></div>')

# 날짜 합계는 소비만 센다 — 소비율에서 빠지는 이체는 회색 덧말로 따로 적는다
excl = lambda t: f' <span style="font-weight: 500; color: {C["INK4"]};">· {t}</span>'

w('Ledger', frame(
    screen_header('소비', tabs=['이번 달', '내역', '한도'], active=1,
                  trailing=f'<div style="display: flex; align-items: center; gap: 8px;">{month_stepper()}{add_tx_button()}</div>') +
    content([
        card(f'<div style="display: flex; align-items: center; gap: 8px;">'
             f'<div style="flex: 1; display: flex; align-items: center; gap: 9px; height: 40px; padding: 0 12px; border-radius: 11px; background: {C["INSET"]};">'
             f'{icon("search", 16, "#606B7D", 1.9)}<span style="font-size: 13.5px; color: {C["INK4"]};">메모·카테고리 검색</span></div>'
             f'<div style="width: 40px; height: 40px; border-radius: 11px; border: 1px solid {C["LINE"]}; display: flex; align-items: center; justify-content: center;">{icon("repeat", 17, C["INK2"], 1.9)}</div></div>'
             f'<div style="display: flex; gap: 6px; margin-top: 10px; overflow: hidden;">'
             f'<div style="display: inline-flex; align-items: center; gap: 4px; height: 32px; padding: 0 12px; border-radius: 99px; background: {C["BRAND_SOFT"]}; color: {C["BRAND"]}; font-size: 12.5px; font-weight: 600; flex-shrink: 0;">전체 32건{icon("down", 13, C["BRAND"], 2)}</div>'
             f'<div style="display: inline-flex; align-items: center; gap: 5px; height: 32px; padding: 0 12px; border-radius: 99px; border: 1px solid {C["LINE"]}; color: {C["INK2"]}; font-size: 12.5px; font-weight: 500; flex-shrink: 0;">{catdot("식비", 8)}식비</div>'
             f'<div style="display: inline-flex; align-items: center; gap: 5px; height: 32px; padding: 0 12px; border-radius: 99px; border: 1px solid {C["LINE"]}; color: {C["INK2"]}; font-size: 12.5px; font-weight: 500; flex-shrink: 0;">{catdot("주거/관리", 8)}주거</div>'
             f'<div style="display: inline-flex; align-items: center; height: 32px; padding: 0 12px; border-radius: 99px; border: 1px solid {C["LINE"]}; color: {C["INK3"]}; font-size: 12.5px; font-weight: 500; flex-shrink: 0;">더보기</div></div>'
             f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px; margin-top: 11px; padding-top: 10px; border-top: 1px solid {C["LINE_SOFT"]};">'
             f'<span style="font-size: 12px; color: {C["INK2"]};">일반 소비 <span style="font-weight: 600; color: {C["INK"]};">112만원</span></span>'
             f'<span style="font-size: 11.5px; color: {C["INK3"]};">이체 63만 · 상환 92만은 제외</span></div>'),
        card(daygroup('9월 8일', '화요일 · 오늘', '32,000원') +
             tx('식비', 'rice', '점심 · 팀 회식', '생활비 통장', '−32,000') +
             daygroup('9월 7일', '월요일', '118,400원') +
             tx('교통', 'bus', '교통카드 충전', '계좌 미지정', '−50,000') +
             tx('쇼핑', 'bag', '생필품', '신용카드', '−62,000') +
             tx('카페/간식', 'coffee', '카페', '생활비 통장', '−6,400') +
             daygroup('9월 5일', '토요일', '20,000원' + excl('이체 30만원 제외')) +
             tx('저축/투자', 'leaf', 'ETF 자동이체', '생활비 → ETF 계좌', '−300,000',
                badges=minib('소비율 제외', 'mute') + minib('반복', 'brand'), muted=True) +
             tx('통신', 'phone', '휴대폰 요금', '생활비 통장', '−20,000', badges=minib('반복', 'brand')) +
             daygroup('9월 3일', '목요일', '470,000원') +
             tx('주거/관리', 'house', '월세 · 관리비', '생활비 통장', '−470,000'),
             pad="4px 14px 10px"),
    ]) + bottomnav(2)))


# ══════════════ 5-2. 소비 › 내역 — v5-1 이후 (LedgerV5) ══════════════
# plan/v5-calendar.md §9-6 · §3-3: 필터 칩 `분류 안 함 7건` · 분류 안 함 행(부제 `분류 안 함`, 메모 없으면 제목 `분류 안 함 기록`, 점선 없음) ·
# 날짜 그룹 헤더 `소비 8.7만 · 이체 30만`(0인 항목 생략) + 확인한 날 체크 · 행 ⋯ 에 `매달 반복으로 만들기`(분류 안 함 행 제외).
# 날짜별 합계는 달력 시안(gen_calendar.SEP)과 같은 값이어야 한다 — 아래 assert 가 지킨다. v3 기준 그림 `Ledger` 는 그대로 둔다.
# 9월 8일(오늘) 행은 하루 시트의 `오늘 기록`(계획 §4-2 도면 · gen_v5.RECENT)과 같은 자료다 — 커피 4,500 = 카페/간식 · 편의점 6,500 = 분류 안 함.
# 9월 6일 이체는 등록된 반복 거래 `ETF 자동이체`(매월 6일 · RecurringPrefill 등록 목록)가 자동으로 기록한 행이다 — `소비율 제외` + `반복` 배지(v3 Ledger 의 같은 행과 같은 모양).
from gen_calendar import SEP, SEP_CHECK, SEP_TRANSFER, SEP_TOTAL, fmt_sum

WEEKDAY = ['일요일', '월요일', '화요일', '수요일', '목요일', '금요일', '토요일']

# (날짜, [(카테고리 | None = 분류 안 함, 아이콘, 메모, 계좌 글, 금액, 종류)]) — 종류 'spend' | 'transfer'(손으로 적은 이체) | 'transfer-auto'(반복 거래가 자동 기록한 이체)
LEDGER_V5 = [
    (8, [('카페/간식', 'coffee', '커피', '계좌 미지정', 4_500, 'spend'),
         ('식비', 'rice', '점심', '계좌 미지정', 9_000, 'spend'),
         ('쇼핑', 'bag', '생필품', '계좌 미지정', 17_000, 'spend'),
         (None, None, '편의점', None, 6_500, 'spend')]),
    (6, [('저축/투자', 'leaf', 'ETF 자동이체', '생활비 통장 → ETF 계좌', 300_000, 'transfer-auto')]),
    (5, [(None, None, '버스', None, 4_500, 'spend'),
         (None, None, '', None, 3_000, 'spend'),
         (None, None, '커피', None, 4_500, 'spend')]),
    (4, [(None, None, '커피', None, 4_500, 'spend')]),
    (3, [('교통', 'bus', '택시', '계좌 미지정', 45_000, 'spend'),
         ('식비', 'rice', '점심', '계좌 미지정', 9_000, 'spend'),
         (None, None, '간식', None, 4_500, 'spend')]),
    # 9월 1일 — 고정비가 먼저 나간 날(2026-09-24 · 합 1,008,000원 = 달력 칸 `101만`). 9/1~9/8 카테고리 합이 소비 · 한도 장의 값과 같다:
    # 주거/관리 47만 · 식비 24만 · 보험 12만 · 통신 8만 · 교통 7만 · 쇼핑 3만 · 문화/여가 1만 · 기타 6만(분류 안 함 32,000 포함 — EtcSubline) · 합계 112만원.
    # 주거/관리 47만은 관리비 · 공과금이고 월세가 아니다 — 월세 700,000원은 9월 8일에 적는 장면(DaySheetConfirm → 완료 카드 → RecurringPrefill `결제일 8`)이라
    # 9월 1일에 월세가 있으면 같은 달 월세가 두 번이 된다(2026-09-24 후속 · 전에는 월세 400,000 + 관리비 70,000).
    (1, [('주거/관리', 'house', '관리비', '생활비 통장', 320_000, 'spend'),
         ('주거/관리', 'house', '전기·가스·수도', '생활비 통장', 150_000, 'spend'),
         ('보험', 'shield', '보험료', '생활비 통장', 120_000, 'spend'),
         ('통신', 'phone', '인터넷·TV', '생활비 통장', 80_000, 'spend'),
         ('구독', 'repeat', 'OTT·음악', '계좌 미지정', 35_500, 'spend'),
         ('식비', 'rice', '장보기', '계좌 미지정', 214_500, 'spend'),
         ('교통', 'bus', '교통카드 충전', '계좌 미지정', 25_000, 'spend'),
         ('쇼핑', 'bag', '생활용품', '계좌 미지정', 13_000, 'spend'),
         ('문화/여가', 'spark', '영화', '계좌 미지정', 10_000, 'spend'),
         ('기타', 'tag', '세탁소', '계좌 미지정', 28_000, 'spend'),
         (None, None, '커피', None, 4_500, 'spend'),
         ('식비', 'rice', '점심', '계좌 미지정', 7_500, 'spend')]),
]
for _d, _rows in LEDGER_V5:       # 칸 숫자 = 내역 날짜 헤더와 같은 숫자(§12-22)
    assert sum(r[4] for r in _rows if r[5] == 'spend') == (SEP[_d] or 0), _d
# 9월 카테고리 합(분류 안 함은 기타로 센다) = 소비 · 이번 달 카테고리 카드와 한도 장의 값(만원)
_cat = {}
for _d, _rows in LEDGER_V5:
    for r in _rows:
        if r[5] == 'spend':
            _cat[r[0] or '기타'] = _cat.get(r[0] or '기타', 0) + r[4]
assert {k: _cat[k] for k in ('주거/관리', '식비', '보험', '통신', '교통', '쇼핑', '문화/여가', '기타')} == {
    '주거/관리': 470_000, '식비': 240_000, '보험': 120_000, '통신': 80_000, '교통': 70_000, '쇼핑': 30_000, '문화/여가': 10_000, '기타': 60_000}
assert sum(_cat.values()) == SEP_TOTAL == 1_120_000
assert not any('월세' in r[2] for _, rows in LEDGER_V5 for r in rows)      # 월세는 9월 8일 장면(DaySheetConfirm · RecurringPrefill)에만
V5_COUNT = sum(len(rows) for _, rows in LEDGER_V5)
V5_UNCAT = [r for _, rows in LEDGER_V5 for r in rows if r[0] is None]
assert len(V5_UNCAT) == 7 and sum(r[4] for r in V5_UNCAT) == 32_000      # `분류 안 함 7건` · 히어로 각주 `분류 안 한 32,000원`
V5_TRANSFER = sum(r[4] for _, rows in LEDGER_V5 for r in rows if r[5].startswith('transfer'))
assert V5_TRANSFER == 300_000 and {d for d, rows in LEDGER_V5 if any(r[5].startswith('transfer') for r in rows)} == SEP_TRANSFER      # 내역의 이체 날짜 = 달력의 이체 배지 날짜


def head_sum(n):
    """날짜 헤더의 금액 — 달력 칸과 같은 formatSum 하나(`.0`은 fmt_sum 이 뗀다 — 300,000 → `30만`. 머리글만의 예외 없음)."""
    return fmt_sum(n)


MENU_IC = {'수정': 'pencil', '매달 반복으로 만들기': 'cal_days', '삭제': 'trash'}      # 앱 CalendarDays(2026-09-27 fix-up 2)


def row_menu(items):
    """행 ⋯ 를 눌렀을 때 뜨는 메뉴 — 앱처럼 항목마다 아이콘(연필 · 달력 · 휴지통), 삭제만 빨강, 굵기 없음.
    폭은 앱 메뉴와 같게 좁아 「매달 반복으로 만들기」가 두 줄로 꺾인다."""
    cells = ''.join(
        f'<div style="display: flex; align-items: center; gap: 10px; min-height: 44px; padding: 10px 14px; font-size: 14px; font-weight: 400; line-height: 1.35; '
        f'color: {C["NEG"] if danger else C["INK"]};">{icon(MENU_IC[t], 16, C["NEG"] if danger else C["INK2"], 1.9)}<span>{t}</span></div>'
        for i, (t, strong, danger) in enumerate(items))
    # 앱 메뉴 = 행 아래 4px(top: calc(100% + 4px)) · 156 폭 · 여백 6 · 반경 12 · 항목 44 / 60(두 줄) · 14 / 400(2026-09-27 fix-up 3 — 예전 top 40 은 행 안에서 떠 날짜 머리를 반쯤 가렸다)
    return (f'<div style="position: absolute; right: 0; top: calc(100% + 4px); z-index: 2; width: 156px; background: {C["SURF"]}; border: 1px solid {C["LINE"]}; '
            f'border-radius: 12px; padding: 6px 0; box-shadow: 0 1px 2px rgba(16,24,40,.04), 0 12px 28px -12px rgba(16,24,40,.32);">{cells}</div>')


UNCAT_CHIP = (f'<span style="font-size: 10.5px; font-weight: 600; color: {C["TAB_INK"]}; background: {C["LINE_SOFT"]}; border-radius: 5px; '
              f'padding: 2px 6px; margin-left: 7px; white-space: nowrap; vertical-align: 1px;">카테고리 없음</span>')


def tx5(cat, ic, memo, link_txt, amt, kind, menu=''):
    """v5 내역 행. 카테고리 행 부제 = 카테고리(계좌를 연결했으면 「{카테고리} · {자산 이름}」 · 「계좌 미지정」은 쓰지 않음).
    카테고리 없는 행 = 메모가 있으면 제목 메모 + 회색 칩 「카테고리 없음」 · 부제 없음, 메모가 없으면 제목 「카테고리 없음」 · 칩 없음.
    소비율에서 빠지는 이체 행은 금액에 − 가 없고 회색."""
    if cat is None:
        tile = (f'<div style="width: 34px; height: 34px; border-radius: 10px; background: {C["INSET"]}; display: flex; align-items: center; '
                f'justify-content: center; flex-shrink: 0;"><span style="font-size: 16px; font-weight: 700; line-height: 1; color: {C["INK3"]};">?</span></div>')      # 앱 .ledger-category-unclassified 굵은 글자 「?」(2026-09-27 fix-up)
        title, sub = ((memo + UNCAT_CHIP) if memo else '카테고리 없음'), ''
    else:
        tile, title = caticon(cat, ic, 34), memo
        sub = cat if (not link_txt or link_txt == '계좌 미지정') else f'{cat} · {link_txt}'
    muted = kind.startswith('transfer')
    badges = (minib('소비율 제외', 'mute') if muted else '') + (minib('반복', 'brand') if kind == 'transfer-auto' else '')      # `반복` 배지는 자동 기록된 반복 기록에만 단다(9월 6일 ETF 자동이체)
    b = f'<span style="display: inline-flex; gap: 5px; margin-left: 6px;">{badges}</span>' if badges else ''
    sub_html = f'<div style="font-size: 11px; color: {C["INK3"]}; margin-top: 2px; white-space: nowrap;">{sub}</div>' if sub else ''
    return (f'<div style="position: relative; display: flex; align-items: center; gap: 11px; min-height: 54px; border-top: 1px solid {C["LINE_ROW"]};">'
            f'{tile}<div style="flex: 1; min-width: 0;">'
            f'<div style="font-size: 13.5px; font-weight: 500; color: {C["INK"]}; white-space: nowrap;">{title}{b}</div>{sub_html}</div>'
            f'<span style="font-size: 14.5px; font-weight: 600; letter-spacing: -0.02em; color: {C["INK2"] if muted else C["INK"]}; white-space: nowrap; flex-shrink: 0;">{"" if muted else "&minus;"}{amt:,}</span>'
            f'<span style="flex-shrink: 0; display: inline-flex;">{icon("more", 16, C["INK2"] if menu else C["INK4"], 2.2)}</span>{menu}</div>')


def daygroup5(day, rows):
    spend = sum(r[4] for r in rows if r[5] == 'spend')
    transfer = sum(r[4] for r in rows if r[5].startswith('transfer'))
    parts = ([f'소비 {head_sum(spend)}'] if spend else []) + ([f'이체 {head_sum(transfer)}'] if transfer else [])     # 0인 항목은 생략
    chk = (f'<span style="display: inline-flex; flex-shrink: 0;">{icon("check", 12, C["INK2"], 2.8)}</span>') if day in SEP_CHECK else ''
    wd = WEEKDAY[(1 + day) % 7] + (' · 오늘' if day == 8 else '')           # 2026-09-01 = 화요일
    return (f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 10px; padding: 12px 0 6px;">'
            f'<span style="font-size: 13px; font-weight: 600; color: {C["INK"]}; white-space: nowrap;">9월 {day}일 '
            f'<span style="font-weight: 500; color: {C["INK3"]};">{wd}</span></span>'
            f'<span style="display: inline-flex; align-items: center; gap: 5px; font-size: 12.5px; font-weight: 600; color: {C["INK2"]}; white-space: nowrap; flex-shrink: 0;">'
            f'{" · ".join(parts)}{chk}</span></div>')


MENU_ROW = (8, 1)      # ⋯ 메뉴를 펼쳐 보이는 행 — 9월 8일 둘째 행(식비 · 점심). 카테고리 없는 행의 메뉴에는 `매달 반복으로 만들기`가 없다.
ledger5_rows = ''
for _d, _rows in LEDGER_V5:
    ledger5_rows += daygroup5(_d, _rows)
    for _i, _r in enumerate(_rows):
        _menu = row_menu([('수정', False, False), ('매달 반복으로 만들기', True, False), ('삭제', False, True)]) if (_d, _i) == MENU_ROW else ''
        ledger5_rows += tx5(*_r, menu=_menu)

chip5 = lambda inner, on=False, strong=False: (
    f'<div style="display: inline-flex; align-items: center; gap: 4px; height: 32px; padding: 0 10px; border-radius: 99px; '
    + (f'background: {C["BRAND_SOFT"]}; color: {C["BRAND"]}; font-weight: 600;' if on else
       f'border: 1px solid {C["LINE"]}; color: {C["INK"] if strong else C["INK2"]}; font-weight: {600 if strong else 500};')
    + f' font-size: 12.5px; white-space: nowrap; flex-shrink: 0;">{inner}</div>')

REPEAT_BTN = (f'<div style="display: inline-flex; align-items: center; gap: 6px; height: 40px; padding: 0 12px; border-radius: 11px; border: 1px solid {C["LINE"]}; '
              f'background: {C["SURF"]}; font-size: 13px; font-weight: 600; color: {C["INK"]}; white-space: nowrap; flex-shrink: 0;">{icon("cal_days", 16, C["INK2"], 1.9)}반복 기록</div>')
UNCAT_BAND = (f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px; height: 42px; margin-top: 10px; padding: 0 12px; '
              f'border-radius: 12px; background: {C["WARN_SOFT"]}; border: 1px solid {C["WARN_RULE"]};">'
              f'<span style="font-size: 12.5px; color: {C["WARN_INK"]}; white-space: nowrap;">카테고리 없는 기록 <b style="font-weight: 700;">{len(V5_UNCAT)}건</b></span>'
              f'<span style="font-size: 12.5px; font-weight: 700; color: {C["WARN_INK"]}; white-space: nowrap;">카테고리 고르기 &rsaquo;</span></div>')
BASIS_CARD = (f'<div style="display: flex; align-items: center; justify-content: space-between; height: 46px; padding: 0 14px; background: {C["SURF"]}; '
              f'border: 1px solid {C["LINE"]}; border-radius: 16px; flex-shrink: 0;"><span style="font-size: 13.5px; font-weight: 600; color: {C["INK"]};">기록 기준</span>'
              f'{icon("right", 16, C["INK3"], 2)}</div>')

w('LedgerV5', frame(
    screen_header('소비', tabs=['이번 달', '내역', '한도'], active=1,
                  trailing=f'<div style="display: flex; align-items: center; gap: 8px;">{month_stepper()}{add_tx_button()}</div>') +
    content([
        card(f'<div style="display: flex; align-items: center; gap: 8px;">'
             f'<div style="flex: 1; min-width: 0; display: flex; align-items: center; gap: 9px; height: 40px; padding: 0 12px; border-radius: 11px; background: {C["INSET"]};">'
             f'{icon("search", 16, "#606B7D", 1.9)}<span style="font-size: 13.5px; color: {C["INK4"]}; white-space: nowrap;">메모·카테고리 검색</span></div>'
             f'{REPEAT_BTN}</div>'
             + UNCAT_BAND +
             f'<div style="display: flex; gap: 5px; margin-top: 10px; overflow: hidden;">'
             + chip5(f'전체 {V5_COUNT}건{icon("down", 13, C["BRAND"], 2)}', on=True)
             + chip5(f'{catdot("식비", 8)}식비')
             + chip5(f'{catdot("주거/관리", 8)}주거/관리')
             + chip5(f'카테고리 없음 {len(V5_UNCAT)}건')
             + chip5('더보기') +
             f'</div>'
             f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px; margin-top: 11px; padding-top: 10px; border-top: 1px solid {C["LINE_SOFT"]};">'
             f'<span style="font-size: 12px; color: {C["INK2"]}; white-space: nowrap;">일반 소비 <span style="font-weight: 600; color: {C["INK"]};">{SEP_TOTAL // 10_000}만원</span></span>'
             f'<span style="font-size: 11.5px; color: {C["INK3"]}; white-space: nowrap;">이체 {V5_TRANSFER // 10_000}만원 · 상환 0원은 제외</span></div>'),
        card(ledger5_rows, pad="4px 14px 10px"),
        BASIS_CARD,
    ]) + bottomnav(2)), keep_all=True)


# ══════════════ 6. 목적지 › 새 목적지 설계 ══════════════
# 앱 goal-tools.tsx(a724aac) · 값은 NUMBERS §8 — 추천 = 시안 사용자의 goalPresets()(비상금 6개월은 이미 있어 빠짐) ·
# 필드 이름 「지금 모은 돈」 「수익률 (연)」(D4) · 만원 칸 되읽기(D11) · 기간 「년 | 개월」(goals-15) · 보라 = 저장되지 않는 가정(D13) ·
# 결과 문장 · 「저장하면 이렇게 바뀌어요」(goals-3) · 원금만 = 지금 모은 돈 + 반올림 전 필요액 × 개월(2,539만).
PRESET_IC = {
    'debt': '<path d="m8 3 4 8 5-5 5 15H2L8 3Z"/>',
    'net': '<path d="M12 2 22 12 12 22 2 12Z"/>',
    'house': '<path d="m3 10 9-7 9 7v10a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2Z"/>',
    'fi': '<path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/>',
}
presets = []
for name, target, ic, col in [("부채 다 갚기", "8,860만원", 'debt', C["INK3"]), ("순자산 1억", "1억원", 'net', C["BRAND"]),
                              ("내 집 마련 종잣돈", "2억원", 'house', C["VIO"]), ("생활비 25년치 모으기", "6억 2,520만원", 'fi', C["POS"])]:
    # 앱 goal-design-preset-grid 와 같게(2026-09-26 DZ2 검토 · 하네스 실측) — 칸 폭 120 고정 · 안쪽 11/10 · 이름 12.5 · 금액 10.5 · 글은 칸 안에서 줄바꿈 · 칸 높이 126(앱은 금액 칸(MotionAmount)이 29.4 높이라 한 줄이어도 아래가 비고, 가장 긴 칸 「생활비 25년치 모으기」 두 줄에 맞춰 네 칸이 120 × 126)
    presets.append(
        f'<div style="flex: 0 0 120px; width: 120px; min-height: 126px; padding: 11px 10px; border-radius: 14px; border: 1px solid {C["LINE"]}; background: {C["SURF"]};">'
        f'<div style="width: 26px; height: 26px; border-radius: 8px; background: {col}18; display: flex; align-items: center; justify-content: center;">'
        f'<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="{col}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{PRESET_IC[ic]}</svg></div>'
        f'<div style="font-size: 12.5px; font-weight: 600; line-height: normal; color: {C["INK"]}; margin-top: 7px;">{name}</div>'
        f'<div style="font-size: 10.5px; line-height: 1.4; color: {C["INK3"]}; margin-top: 2px;">목표액 <span style="white-space: nowrap;">{target}</span></div></div>')

# 그래프: 오늘 500만 → 7년 뒤 3,000만. 보라 실선 = 매달 24만원(242,686원)을 연 4% 월 복리로 넣은 잔액, 회색 점선 = 원금만(500만 + 242,686 × 개월)
_G_REQ, _G_MR = 242_685.628, (1.04) ** (1 / 12) - 1


def _g_fv(m):
    bal = 5_000_000
    for _ in range(m):
        bal = bal * (1 + _G_MR) + _G_REQ
    return bal


def _G_Y(v):
    return 83.2 - (v - 5_000_000) / 25_000_000 * 64.1          # 500만 → y 83.2 · 3,000만 → y 19.1


def _G_X(yr):
    return 10 + 306 * yr / 7


_g_need = ' L'.join(f'{_G_X(k):.1f} {_G_Y(_g_fv(12 * k)):.1f}' for k in range(8))
_g_prin = ' L'.join(f'{_G_X(k):.1f} {_G_Y(5_000_000 + _G_REQ * 12 * k):.1f}' for k in range(8))
assert round((5_000_000 + _G_REQ * 84) / 10_000) == 2539 and abs(_g_fv(84) - 30_000_000) < 5_000
_g_lab_y = 70          # 점선 아래(x 180 ~ 255 에서 점선은 y 54 이하)
goal_chart = (
    f'<svg width="326" height="122" viewBox="0 0 326 122" fill="none" style="display: block; width: 100%; height: 122px;">'
    f'<defs><linearGradient id="gfill" x1="0" y1="0" x2="0" y2="1">'
    f'<stop offset="0%" stop-color="{C["VIO"]}" stop-opacity="0.22"/><stop offset="100%" stop-color="{C["VIO"]}" stop-opacity="0"/></linearGradient></defs>'
    f'<line x1="10" y1="19.1" x2="316" y2="19.1" stroke="{C["LINE"]}" stroke-width="1" stroke-dasharray="4 4"/>'
    f'<text x="10" y="13" font-size="11" fill="{C["INK4"]}">목표 3,000만</text>'
    f'<path d="M{_g_need} L316 96 L10 96 Z" fill="url(#gfill)"/>'
    f'<path d="M{_g_need}" stroke="{C["VIO"]}" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>'
    f'<path d="M{_g_prin}" stroke="{C["INK4"]}" stroke-width="1.6" stroke-dasharray="4 4" stroke-linecap="round" stroke-linejoin="round"/>'
    f'<circle cx="316" cy="19.1" r="3.6" fill="{C["VIO"]}"/><circle cx="10" cy="83.2" r="3" fill="{C["VIO"]}"/>'
    f'<text x="180" y="{_g_lab_y:.1f}" font-size="11" fill="{C["INK4"]}">원금만 2,539만</text>'
    f'<line x1="10" y1="96" x2="316" y2="96" stroke="{C["LINE"]}" stroke-width="1"/>'
    f'<text x="10" y="113" font-size="11" fill="{C["INK4"]}">오늘 500만</text>'
    f'<text x="316" y="113" text-anchor="end" font-size="11" font-weight="600" fill="{C["INK2"]}">7년 뒤 3,000만</text></svg>')


def unit_toggle():
    """기간 칸 바로 아래 「년 | 개월」 — 고른 쪽 흰 바탕 파란 글자."""
    return (f'<div style="display: flex; gap: 4px; margin-top: 6px;">'
            f'<span style="flex: 1; height: 28px; border-radius: 8px; border: 1px solid {C["LINE"]}; background: {C["SURF"]}; display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 600; color: {C["BRAND"]};">년</span>'
            f'<span style="flex: 1; height: 28px; border-radius: 8px; background: {C["TRACK"]}; display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 500; color: {C["TAB_INK"]};">개월</span></div>')


def period_field(w=None):
    # 앱 새 목적지 설계 둘째 줄 = 지금 모은 돈 · 기간 · 수익률 (연) 세 칸 같은 폭(102 · 104 · 104 · 간격 10) — 2026-09-27 fix-up 3(예전 118 · 100 · 96)
    f_ = field("기간", "7", "년", required=True, w=w)
    assert f_.endswith('</div></div>')
    return f_[:-len('</div>')] + unit_toggle() + '</div>'


def RED_T(t):
    """빨간 글 — 날짜 · 기간은 줄 끝에서 갈라지지 않게 묶는다."""
    t = re.sub(r'(\d{4}년 \d{1,2}월|\d+년 \d+개월)', r'<span style="white-space: nowrap;">\1</span>', t)
    return f'<span style="color: {C["NEG"]};">{t}</span>'


preview = (f'<div style="margin-top: 12px;">'
           f'<div style="font-size: 13px; font-weight: 700; color: {C["INK"]};">저장하면 이렇게 바뀌어요</div>'
           f'<div style="display: flex; flex-direction: column; gap: 4px; margin-top: 6px; font-size: 12px; line-height: 1.5; color: {C["INK2"]};">'
           f'<div>결혼 자금 매달 13만원 · 2038년 2월 도착 예상 · {RED_T("목표일보다 약 4년 5개월 늦어요")}</div>'
           f'<div>비상금 6개월 매달 70만 → 60만원 · {RED_T("도착 2027년 4월 → 2027년 5월")}</div>'
           f'<div>투자 계좌 5,000만원 매달 19만 → 17만원 · {RED_T("도착 2033년 12월 → 2034년 8월")}</div></div></div>')

w('GoalDesign', frame(
    screen_header('목적지', tabs=['내 목적지', '새 목적지 설계'], active=1) +
    content([
        card(f'<div style="font-size: 11px; font-weight: 600; letter-spacing: 0.07em; color: {C["INK3"]};">추천 목적지에서 시작</div>'
             f'<div style="display: flex; gap: 8px; margin-top: 9px; overflow: hidden;">{"".join(presets)}</div>', pad="13px 14px"),
        hero(f'<div style="display: flex; gap: 10px; align-items: flex-start;">{field("이름", "결혼 자금", w=None)}{field("목표액", "3,000", "만원", required=True, w=124, readback="3,000만원")}</div>'
             f'<div style="display: flex; gap: 10px; margin-top: 12px; align-items: flex-start;">'
             f'{field("지금 모은 돈", "500", "만원", w=None, readback="500만원")}{period_field()}'
             f'{field("수익률 (연)", "4", "%", w=None)}</div>'
             f'<div style="font-size: 11.5px; line-height: 1.45; color: {C["INK3"]}; margin-top: 10px;">수익률을 비워 두면 일반 저축(수익률 0%)으로 계산해요.</div>'
             f'<div style="margin-top: 13px; padding: 13px; background: {C["VIO_SOFT"]}; border-radius: 14px;">'
             f'<div style="display: flex; align-items: flex-end; justify-content: space-between; gap: 10px;">'
             f'<div><div style="font-size: 11.5px; font-weight: 600; color: {C["VIO_STRONG"]};">매달 넣어야 할 돈</div>'
             f'<div style="display: flex; align-items: baseline; gap: 2px; margin-top: 3px;">'
             f'<span style="font-size: 30px; font-weight: 700; letter-spacing: -0.035em; color: {C["VIO_STRONG"]};">24</span>'
             f'<span style="font-size: 16px; font-weight: 600; color: {C["VIO_STRONG"]};">만원</span></div></div>'
             f'{badge("저장되지 않는 가정", "vio", "spark")}</div>'
             f'<div style="font-size: 11.5px; line-height: 1.5; color: #4E2496; margin-top: 6px;">'
             f'다른 목적지에 이미 매달 90만원을 다 나눴어요 · 지금도 매달 57만원이 모자라요. 저장하면 기존 목적지 몫이 줄어요.</div></div>'
             f'<div style="margin-top: 12px;">{goal_chart}</div>'
             f'{preview}'
             f'<div style="margin-top: 14px;">{btn("목적지로 저장", "primary")}</div>', pad=15),
        card(f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px;">'
             f'<span style="font-size: 13.5px; font-weight: 500; color: {C["INK2"]};">다른 금액으로 계산해 보기 · 계산 기준</span>{icon("right", 16, C["INK3"], 2)}</div>', pad="15px 14px"),
    ]) + bottomnav(3), h=GOALDESIGN_H), keep_all=True)


# ══════════════ 7. 미래 › 상환 계획 (저장된 계획) ══════════════
# D6 · future-4/6/11/22 · D15: 기본 장 = 저장된 상태(월 추가 15만원 · 고금리 우선). 보라 점선 · 「저장되지 않는 가정」 · 「가정 종료」 · 「상환 계획 저장」은
# 슬라이더나 방식을 바꾼 초안에만(PayoffStates). 숫자 = NUMBERS §10(앱 달 규칙 — 2036년 5월 · 기준선 2038년 10월).
def compare(name, eta, months, interest, best=False):
    bd = f'1.5px solid {C["BRAND"]}' if best else f'1px solid {C["LINE"]}'
    bg = C["BRAND_SOFT"] if best else C["SURF"]
    tag = (f'<span style="background: {C["BRAND"]}; color: #FFFFFF; font-size: 10px; font-weight: 700; '
           f'border-radius: 6px; padding: 3px 6px; flex-shrink: 0;">추천</span>') if best else ''
    return (f'<div style="flex: 1; min-width: 0; padding: 13px; border-radius: 14px; border: {bd}; background: {bg};">'
            f'<div style="display: flex; align-items: center; gap: 5px;">'
            f'<span style="font-size: 13px; font-weight: 700; white-space: nowrap; color: {C["BRAND"] if best else C["INK"]};">{name}</span>{tag}</div>'
            f'<div style="font-size: 11.5px; color: {C["INK3"]}; margin-top: 9px;">다 갚는 달</div>'
            f'<div style="font-size: 16px; font-weight: 600; letter-spacing: -0.02em; color: {C["INK"]};">{eta}</div>'
            f'<div style="font-size: 11px; color: {C["INK3"]};">{months}</div>'
            f'<div style="font-size: 11.5px; color: {C["INK3"]}; margin-top: 8px;">총이자</div>'
            f'<div style="font-size: 16px; font-weight: 600; letter-spacing: -0.02em; color: {C["INK"]};">{interest}</div></div>')


PAYOFF_MAX = 200          # 슬라이더 끝 = max(200만, 초안 올림 10만)(future-11)
info_box = (f'<div style="display: flex; gap: 8px; padding: 10px 11px; background: {C["INSET"]}; border-radius: 12px;">'
            f'<span style="flex-shrink: 0; margin-top: 1px;">{icon("info", 14, C["INK3"], 1.9)}</span>'
            f'<div style="display: flex; flex-direction: column; gap: 3px; font-size: 11.5px; line-height: 1.5; color: {C["INK3"]};">'
            f'<span>고금리 우선이 이자를 30만원 덜 내요 · 끝나는 달은 같아요</span>'
            f'<span>추가 상환이 없으면 2038년 10월 · 이자 2,248만원</span>'
            f'<span style="font-weight: 700; color: {C["INK2"]};">2년 5개월 빨리 끝나고 이자 514만원 덜 내요</span></div></div>')

w('Payoff', frame(
    screen_header('미래', tabs=['자산 경로', '상환 계획'], active=1) +
    content([
        card(f'<div style="display: flex; align-items: center; gap: 8px;">{badge("저장된 계획", "pos", "check")}</div>'
             f'<p style="margin: 11px 0 0; font-size: 15px; font-weight: 600; letter-spacing: -0.015em; color: {C["INK"]};">월 추가 상환을 얼마나 할까요?</p>'
             f'<div style="display: flex; align-items: baseline; gap: 2px; margin-top: 8px;">'
             f'<span style="font-size: 25px; font-weight: 700; letter-spacing: -0.03em; color: {C["INK"]};">15</span>'
             f'<span style="font-size: 15px; font-weight: 600; color: {C["INK2"]};">만원</span></div>'
             f'<div style="font-size: 12.5px; font-weight: 600; color: {C["INK2"]}; margin-top: 4px;">최소 77만원 + 추가 15만원 = 매월 92만원</div>'
             f'<div style="font-size: 12.5px; color: {C["INK2"]}; margin-top: 10px;">지금 계획에서 매달 남는 돈 약 90만원</div>'
             f'<div style="margin-top: 8px;">{slider(round(15 / PAYOFF_MAX * 100, 1), C["BRAND"])}</div>'
             f'<div style="display: flex; align-items: center; justify-content: space-between; margin-top: 5px;">'
             f'<span style="font-size: 11px; color: {C["INK4"]};">최소 상환만</span>'
             f'<span style="font-size: 11px; color: {C["INK4"]};">월 {PAYOFF_MAX}만원</span></div>'
             f'<div style="font-size: 12px; line-height: 1.45; color: {C["INK3"]}; margin-top: 8px;">저축 · 상환 계획까지 지키려면 이번 달 152만원 안에서 쓰면 돼요</div>'
             f'<div style="margin-top: 10px;">{note("월 최소 상환액 77만원은 줄일 수 없어 슬라이더에서 뺐어요.", "mute")}</div>'),
        card(f'<div style="display: flex; gap: 8px;">{compare("고금리 우선", "2036년 5월", "9년 8개월 뒤", "1,734만원", best=True)}'
             f'{compare("소액 우선", "2036년 5월", "9년 8개월 뒤", "1,764만원")}</div>'
             f'<div style="margin-top: 11px;">{info_box}</div>',
             pad="13px 14px"),
        card(f'<div style="font-size: 13.5px; font-weight: 600; color: {C["INK"]};">저장된 상환 계획이에요</div>'
             f'<div style="font-size: 11.5px; line-height: 1.5; color: {C["INK3"]}; margin-top: 3px;">슬라이더나 방식을 바꾸면 보라 점선으로 바뀌고, 저장해야 홈 · 자산 경로 · 목적지 계산에 반영돼요.</div>'),
    ]) + bottomnav(4), h=PAYOFF_H), keep_all=True)


# ══════════════ 8. 목적지 · 새 목적지 설계 — 상태 장(2026-09-26 새 장 · DZ2) ══════════════
# 앱 goals-view.tsx · goal-tools.tsx(a724aac)를 시안 사용자(design-state.json)로 띄운 값 — 매달 모으는 돈 110만원 가정(슬라이더 +4칸) ·
# 비상금 6개월 한 줄 펼침 · 비상금이 도착한 목적지(1,500 / 1,500만원) · 설계 처음 · 다른 금액 30만원 가정. goals-2/4/7/9/10/14/16/24/26/28 · D13.
VIO_T = lambda t: f'<span style="color: {C["VIO_STRONG"]};">{t}</span>'
NOWRAP = lambda t: f'<span style="white-space: nowrap;">{t}</span>'
GS_MORE = icon("more", 16, C["INK4"], 2.2)


def gs_ring(pct, col, lab):
    return (f'<div style="width: 44px; height: 44px; border-radius: 99px; background: conic-gradient({col} 0% {pct}%, {C["TRACK"]} {pct}% 100%); display: flex; align-items: center; justify-content: center; flex-shrink: 0;">'
            f'<div style="width: 33px; height: 33px; border-radius: 99px; background: {C["SURF"]}; display: flex; align-items: center; justify-content: center; font-size: 11.5px; font-weight: 700; color: {lab};">{pct}<span style="font-size: 8.5px; font-weight: 600;">%</span></div></div>')


def gs_chip(t, fg, bg):
    return f'<span style="font-size: 10px; font-weight: 600; color: {fg}; background: {bg}; border-radius: 5px; padding: 2px 5px; white-space: nowrap;">{t}</span>'


def gs_add(bg, fg):
    return (f'<div style="display: inline-flex; align-items: center; gap: 3px; height: 32px; padding: 0 10px; border-radius: 9px; background: {bg}; color: {fg}; font-size: 12.5px; font-weight: 600; flex-shrink: 0;">'
            f'{icon("plus", 13, fg, 2.4)}적립</div>')


def gs_row(ring_html, name, chip_html, l1, l2, btn_html='', frame_=False, top=True):
    bd = f'border: 1px dashed {C["VIO_LINE"]}; border-radius: 13px; padding: 11px 6px; margin: 4px -6px;' if frame_ else (f'padding: 11px 0; border-top: 1px solid {C["LINE_ROW"]};' if top else 'padding: 11px 0;')
    return (f'<div style="display: flex; align-items: center; gap: 11px; {bd}">{ring_html}'
            f'<div style="flex: 1; min-width: 0;"><div style="display: flex; align-items: center; gap: 5px;"><span style="font-size: 14px; font-weight: 600; color: {C["INK"]};">{name}</span>{chip_html}</div>'
            f'<div style="font-size: 12px; color: {C["INK2"]}; margin-top: 2px;">{l1}</div>'
            f'<div style="font-size: 11.5px; line-height: 1.45; color: {C["INK3"]}; margin-top: 1px;">{l2}</div></div>{btn_html}{GS_MORE}</div>')


def gs_pill(t):
    # 앱 목적지 모자람 알약 = 11px · 600 · 여백 0 10 · 높이 30(2026-09-27 fix-up 2 · Goals 손편집 장과 같게)
    return (f'<span style="display: inline-flex; align-items: center; height: 30px; padding: 0 10px; border-radius: 99px; border: 1px solid {C["WARN_RULE"]}; '
            f'background: {C["SURF"]}; color: {C["WARN_INK"]}; font-size: 11px; font-weight: 600; white-space: nowrap;">{t} &rsaquo;</span>')


def gs_warn(text):
    return (f'<div style="margin-top: 11px; padding: 10px 11px 11px; background: {C["WARN_SOFT"]}; border-radius: 12px;">'
            f'<div style="display: flex; gap: 8px;"><span style="flex-shrink: 0; margin-top: 2px;">{icon("warn", 15, C["WARN"], 2)}</span>'
            f'<span style="font-size: 12.5px; line-height: 1.5; color: {C["WARN_INK"]};">{text}</span></div>'
            f'<div style="display: flex; gap: 8px; flex-wrap: wrap; margin-top: 9px; padding-left: 23px;">{gs_pill("목표일 늦추기")}{gs_pill("우선순위 바꾸기")}</div></div>')


def gs_bar(pct):
    return (f'<div style="position: relative; height: 9px; border-radius: 99px; background: {C["TRACK"]}; margin-top: 11px; overflow: hidden;">'
            f'<div style="position: absolute; inset: 0 {100 - pct:.1f}% 0 0; border-radius: 99px; background: linear-gradient(90deg, #3556E6 0%, #7A3FE4 100%);"></div></div>')


GS_HEAD = (f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px;">'
           f'<span style="font-size: 11px; font-weight: 600; letter-spacing: 0.07em; color: {C["INK3"]};">매달 모으는 돈</span>'
           f'<span style="font-size: 12.5px; font-weight: 600; color: {C["BRAND"]}; white-space: nowrap;">매달 모으는 돈 바꿔 보기 &rsaquo;</span></div>')
GS_FORMULA = (f'<div style="font-size: 11.5px; line-height: 1.5; color: {C["INK2"]}; margin-top: 6px; letter-spacing: -0.02em; white-space: nowrap;">'
              f'월급 + 부수입 390만 − 월말 예상 소비 208만 − 대출상환 92만 = 90만원</div>'
              f'<div style="font-size: 11.5px; line-height: 1.5; color: {C["INK3"]}; margin-top: 4px;">홈의 \'월말 예상 여유 8만원\'은 소비 목표(월급의 60%)에서 월말 예상 소비를 뺀 돈이라 이 금액과 달라요.</div>')


def gs_amount(num, label, right, col=C["INK"], chip_=''):
    return (f'<div style="display: flex; align-items: flex-end; justify-content: space-between; gap: 10px; margin-top: 7px;">'
            f'<div style="display: flex; align-items: baseline; gap: 2px;"><span style="font-size: 30px; font-weight: 700; letter-spacing: -0.035em; line-height: 1.05; color: {col};">{num}</span>'
            f'<span style="font-size: 16px; font-weight: 600; color: {col if col != C["INK"] else C["INK2"]};">만원</span>'
            f'{chip_}<span style="font-size: 12.5px; font-weight: 500; color: {C["INK3"]}; margin-left: 5px; white-space: nowrap;">{label}</span></div>'
            f'<span style="font-size: 12.5px; font-weight: 500; color: {C["INK3"]}; white-space: nowrap; padding-bottom: 2px;">모두 도착하려면 <span style="font-weight: 600; color: {C["INK"]};">{right}</span></span></div>')


VIO_CARD = f'background: {C["SURF"]}; border: 1.5px dashed {C["VIO_LINE"]}; border-radius: 20px; padding: 15px 16px;'
late2 = lambda t: f'<span style="color: {C["NEG"]};">목표일보다 약 {NOWRAP(t)} 늦어요</span>'
EMER_RING, INV_RING = gs_ring(68, '#38bdf8', '#0A72AC'), gs_ring(42, C["VIO"], C["VIO"])
DEBT_ROW = gs_row(gs_ring(31, C["WARN"], C["WARN"]), '신용대출 다 갚기', gs_chip('부채 상환', C["WARN"], C["WARN_SOFT"]),
                  '남은 원금 2,200만원 · 연 6.8%', '다 갚는 달 2030년 11월 · 상환 계획대로')
NET_ROW = gs_row(gs_ring(47, C["BRAND"], C["BRAND"]), '순자산 2억원', gs_chip('순자산', C["BRAND"], C["BRAND_SOFT"]),
                 '9,350만 / 2억원 · 자산에서 자동으로 계산', '도착 예상 2031년 1월 · 미래 탭 계산')
LIST_HEAD = (f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px; padding-bottom: 6px;">'
             f'<span style="font-size: 14px; font-weight: 600; color: {C["INK"]};">진행 중인 목적지</span>'
             f'<span style="font-size: 12px; font-weight: 500; color: {C["INK3"]};">우선순위 순으로 보여요</span></div>')
GA = gs_chip('가정', C["VIO_STRONG"], C["VIO_SOFT"])

# A · 매달 모으는 돈 110만원 가정(goals-9 · goals-10 · D13)
a_top = (f'<div style="{VIO_CARD}">{GS_HEAD}<div style="margin-top: 8px;">{badge("저장되지 않는 가정", "vio", "spark")}</div>'
         + gs_amount('110', '가정', '146만원')      # 앱: 큰 숫자는 보통 글자 + 작은 글 「가정」(「목적지에 나눠 넣는 중」 자리) — 보라는 점선 · 배지 · 바뀐 줄
         + f'<div style="font-size: 12px; color: {C["INK3"]}; margin-top: 5px;">저장되지 않는 가정 금액이에요</div>'
         + gs_bar(110 / 146 * 100)
         + gs_warn('목적지에 매달 <b style="font-weight: 700;">36만원</b>이 더 필요해요. 늦어지는 목적지: 투자 계좌 5,000만원. 목표일을 늦추거나 우선순위를 바꾸면 앱이 다시 나눠요.') + '</div>')
a_panel = (f'<div style="{VIO_CARD}">'
           # 앱 <details id=goal-budget-assumption> — 요약 줄(제목 + 열림 표시 −) 아래 배지 한 줄 · 절 제목 · 옅은 파랑 안내 상자(2026-09-27 fix-up · 앱 CSS 의 어긋난 구분선 · 과녁 아이콘은 앱 후속)
           f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px;"><span style="font-size: 15px; font-weight: 700; color: {C["INK"]};">매달 모으는 돈을 바꾸면?</span>'
           f'<span style="font-size: 18px; font-weight: 500; line-height: 1; color: {C["BRAND"]};">−</span></div>'
           f'<div style="margin-top: 8px;">{badge("저장되지 않는 가정", "vio", "spark")}</div>'
           f'<div style="font-size: 13px; font-weight: 600; color: {C["INK"]}; margin-top: 10px;">매달 모으는 돈을 바꿔 보세요</div>'
           f'<div style="font-size: 12px; line-height: 1.5; color: {C["BRAND"]}; margin-top: 6px; padding: 9px 11px; background: {C["BRAND_SOFT"]}; border-radius: 12px;">바꿔 본 금액으로 목적지 결과만 미리 보고 있어요. 실제 월급 · 소비나 저장된 계획은 바뀌지 않아요.</div>'
           f'<div style="display: flex; align-items: baseline; gap: 6px; margin-top: 10px;"><span style="font-size: 24px; font-weight: 700; letter-spacing: -0.03em; color: {C["INK"]};">110만원</span>'
           f'<span style="font-size: 12px; color: {C["INK3"]};">가정한 매달 모으는 돈</span></div>'
           f'<div style="margin-top: 8px;">{slider(50, C["BRAND"])}</div>'      # 앱 슬라이더는 파랑(110 / 220만원 = 50%)
           f'<div style="display: flex; align-items: center; justify-content: space-between; margin-top: 5px;"><span style="font-size: 11px; color: {C["INK4"]};">0만원</span>'
           f'<span style="display: inline-flex; align-items: center; gap: 4px; font-size: 12.5px; font-weight: 600; color: {C["BRAND"]};">{icon("refresh", 13, C["BRAND"], 2.2)}가정 종료</span>'
           f'<span style="font-size: 11px; color: {C["INK4"]};">220만원</span></div>'
           f'<div style="font-size: 11.5px; line-height: 1.5; color: {C["INK3"]}; margin-top: 8px;">부채 상환 목적지는 월 최소 상환액과 추가 상환에 이미 들어 있어 매달 모으는 돈에서 빠져요.</div></div>')
a_list = card(LIST_HEAD
              + gs_row(EMER_RING, '비상금 6개월', GA, f'1,020 / 1,500만원 · {VIO_T("매달 80만원")}', VIO_T('도착 예상 2027년 3월'), gs_add(C["SKY_SOFT"], C["SKY"]), frame_=True)
              + gs_row(INV_RING, '투자 계좌 5,000만원', GA, f'2,100 / 5,000만원 · {VIO_T("매달 30만원")}',
                       f'{VIO_T("도착 예상 2032년 3월")} · {late2("2년 6개월")} · {NOWRAP("수익률 연 5.0%")}', gs_add(C["VIO_SOFT"], C["VIO_STRONG"]), frame_=True)
              + DEBT_ROW + NET_ROW, pad="12px 14px 8px")

# B · 비상금 6개월 한 줄 펼침(goals-7 · goals-14 · goals-24 · goals-2 · goals-4)
def gs_cell(label, value, red=False, fs=14):
    return (f'<div style="padding: 10px 11px; background: {C["INSET"]}; border-radius: 12px;"><div style="font-size: 11.5px; color: {C["INK3"]};">{label}</div>'
            f'<div style="font-size: {fs}px; font-weight: 700; color: {C["NEG"] if red else C["INK"]}; margin-top: 3px;">{value}</div></div>')


b_card = card(
    gs_row(EMER_RING, '비상금 6개월', '', '1,020 / 1,500만원 · 매달 70만원', f'도착 예상 2027년 4월 · {late2("1개월")}', gs_add(C["SKY_SOFT"], C["SKY"]), top=False)
    + f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px; margin-top: 4px; font-size: 12px; color: {C["INK3"]};">'
      f'<span>조정 필요 · 비상금 · 우선순위 1</span><span style="white-space: nowrap;">목표일 2027년 3월 8일</span></div>'
    + f'<div style="margin-top: 9px; padding: 11px 12px; background: {C["INSET"]}; border-radius: 12px;">'
      f'<div style="font-size: 12.5px; color: {C["INK2"]};">자산 탭의 현금성 자산은 <b style="font-weight: 700;">1,460만원</b>이에요.</div>'
      f'<div style="display: inline-flex; align-items: center; height: 34px; padding: 0 12px; margin-top: 8px; border-radius: 10px; border: 1px solid {C["LINE"]}; background: {C["SURF"]}; font-size: 12.5px; font-weight: 600; color: {C["INK"]};">이 금액으로 맞추기</div></div>'
    + f'<div style="display: flex; align-items: center; justify-content: space-between; margin-top: 11px; font-size: 12px; color: {C["INK3"]};">'
      f'<span>자세히</span><span style="font-weight: 600; color: {C["BRAND"]};">접기 ⌃</span></div>'
    + f'<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 8px; margin-top: 8px;">'
      + gs_cell('매달 필요한 돈', '80만원') + gs_cell('이 목적지에 매달 넣을 돈', '70만원')
      + gs_cell('목표일 대비', '목표일보다 약 1개월 늦어요', red=True, fs=12) + gs_cell('도착 예상', '2027년 4월') + '</div>'      # 앱: 목표일 대비 칸만 12px 한 줄(2026-09-27 fix-up)
    + f'<div style="margin-top: 8px; padding: 10px 11px; background: {C["INSET"]}; border-radius: 12px;">'
      f'<div style="font-size: 11.5px; color: {C["INK3"]};">소비 계획에서 빼는 몫</div><div style="font-size: 14px; font-weight: 700; color: {C["INK"]}; margin-top: 3px;">매달 80만원</div>'
      f'<div style="font-size: 11px; line-height: 1.5; color: {C["INK3"]}; margin-top: 3px;">이 몫은 \'저축 · 상환 계획까지 지키려면\' 금액에서만 빠져요. 이번 달 한도는 소비 목표로만 판단해요.</div></div>'
    + f'<div style="font-size: 12px; line-height: 1.5; color: {C["INK2"]}; margin-top: 8px;">이 목적지에 쓰는 수익률 연 0.0% · 언제든 쓸 수 있는 현금이라 수익률 0%로 계산해요</div>'
    + f'<div style="display: inline-flex; align-items: center; height: 34px; padding: 0 12px; margin-top: 8px; border-radius: 10px; border: 1px solid {C["LINE"]}; background: {C["INSET"]}; font-size: 12.5px; font-weight: 600; color: {C["INK"]};">홈에 표시</div>',
    pad="12px 14px 14px")

# C · 비상금이 도착했을 때(goals-26) — 진행 중 목록 · 모두 도착하려면에서 빠지고 아래 「도착한 목적지」로
c_top = card(GS_HEAD + gs_amount('90', '목적지에 나눠 넣는 중', '66만원') + GS_FORMULA + gs_bar(100)
             + f'<div style="display: flex; gap: 8px; margin-top: 11px; padding: 10px 11px; background: {C["INSET"]}; border-radius: 12px;">'
               f'<span style="flex-shrink: 0; margin-top: 1px;">{icon("checkcircle", 15, C["WARN"], 2)}</span>'
               f'<span style="font-size: 12.5px; line-height: 1.5; color: {C["INK2"]};">나눠 넣고도 매달 <b style="font-weight: 700;">23만원</b>이 남아요. 목표일과 나눠 넣는 돈을 확인해 주세요.</span></div>',
             pad="15px 16px")
c_list = card(LIST_HEAD
              + gs_row(INV_RING, '투자 계좌 5,000만원', '', '2,100 / 5,000만원 · 매달 66만원', f'도착 예상 2029년 9월 · {NOWRAP("수익률 연 5.0%")}', gs_add(C["VIO_SOFT"], C["VIO_STRONG"]))
              + DEBT_ROW + NET_ROW, pad="12px 14px 8px")
GS_ADD_GOAL = (f'<div style="display: flex; align-items: center; justify-content: center; gap: 6px; height: 46px; border-radius: 14px; border: 1.5px dashed #B9C3D6; '
               f'background: rgba(255,255,255,.55); color: {C["BRAND"]}; font-size: 14px; font-weight: 600; flex-shrink: 0;">{icon("plus", 16, C["BRAND"], 2.2)}목적지 추가</div>')      # Goals 장과 같은 버튼(앱: 진행 중 목록 → 목적지 추가 → 도착한 목적지)
c_done = card(f'<div style="font-size: 14px; font-weight: 600; color: {C["INK"]}; padding-bottom: 6px;">도착한 목적지 1개</div>'
              + gs_row(gs_ring(100, C["POS"], C["POS"]), '비상금 6개월', gs_chip('도착했어요', C["POS"], C["POS_SOFT"]), '1,500 / 1,500만원', ''),
              pad="12px 14px 8px")
GS_CAP = lambda t: f'<div style="font-size: 11.5px; line-height: 1.5; color: {C["INK3"]}; padding: 0 4px;">{t}</div>'

# D · 목적지 줄이 바뀌는 세 경우 + 새 목적지 설계의 빨간 줄(goals-8 · goals-3 #2 · D12 · 2026-09-27 fix-up · 앱 하네스 W/tools/fix1/cap_goals_d*.cjs).
# 시안 사용자에서 한 가지씩만 바꾼 앱 화면 그대로: ① 투자 계좌 목표일을 지움 ② 투자 계좌 목표액 3억원 ③ 신용대출 다 갚기 목표일 2029년 3월 8일 ④ 설계 목표액 3억원.
RED_S = lambda t: f'<span style="color: {C["NEG"]};">{t}</span>'
d_nodate = card(
    GS_HEAD
    + f'<div style="display: flex; align-items: baseline; gap: 2px; margin-top: 7px;"><span style="font-size: 30px; font-weight: 700; letter-spacing: -0.035em; line-height: 1.05; color: {C["INK"]};">90</span>'
      f'<span style="font-size: 16px; font-weight: 600; color: {C["INK2"]};">만원</span><span style="font-size: 12.5px; font-weight: 500; color: {C["INK3"]}; margin-left: 5px; white-space: nowrap;">목적지에 나눠 넣는 중</span></div>'
    + f'<div style="text-align: right; font-size: 12.5px; font-weight: 500; color: {C["INK3"]}; margin-top: 4px;">목표일이 있는 목적지에 <span style="font-weight: 600; color: {C["INK"]};">80만원</span></div>'
    + GS_FORMULA      # 앱 goals-nodate: 식 줄 + 홈 여유 안내는 오른쪽 줄 아래 · 막대 위에 그대로(C 와 같게 · 2026-09-27 fix-up 2)
    + gs_bar(100)
    + f'<div style="display: flex; gap: 8px; margin-top: 11px; padding: 10px 11px; background: {C["WARN_SOFT"]}; border-radius: 12px;">'
      f'<span style="flex-shrink: 0; margin-top: 2px;">{icon("warn", 15, C["WARN"], 2)}</span>'
      f'<span style="font-size: 12.5px; line-height: 1.5; color: {C["WARN_INK"]};">1개 목적지의 목표일을 다시 정해 주세요. 그동안 그 목적지는 매달 나눠 넣는 계산에서 빠져요.</span></div>',
    pad="15px 16px")
# 목적지 줄은 매달 모으는 돈 카드 밖 — C 와 같은 「진행 중인 목적지」 목록 카드(앱 goals-nodate · 2026-09-27 fix-up 3 · 예전엔 위 카드 안 구분선 아래)
d_nodate += card(LIST_HEAD
                 + gs_row(EMER_RING, '비상금 6개월', '', '1,020 / 1,500만원 · 매달 80만원', '도착 예상 2027년 3월', gs_add(C["SKY_SOFT"], C["SKY"]))
                 + gs_row(INV_RING, '투자 계좌 5,000만원', '', '2,100 / 5,000만원 · 목표일을 정하면 나눠 넣어요', '목표일을 다시 정해 주세요', gs_add(C["VIO_SOFT"], C["VIO_STRONG"])),
                 pad="12px 14px 8px")
d_unreach = card(gs_row(gs_ring(7, C["VIO"], C["VIO"]), '투자 계좌 3억원', '', '2,100만 / 3억원 · 매달 19만원',
                        f'{RED_S("지금 배분으로는 도착하기 어려워요")} · {NOWRAP("수익률 연 5.0%")}', gs_add(C["VIO_SOFT"], C["VIO_STRONG"]), top=False), pad="4px 14px")
# ③ 펼친 부채 상환 목적지(앱 goals-latedebt-open · goals-d2.json latedebtOpen · 2026-09-27 fix-up 2): 「자세히 · 접기 ⌃」(목적지 색 주황) 아래 칸 넷 —
# 매달 갚는 돈 35만원(NUMBERS §7-1) · 매달 모으는 돈에서 빠져요 · 목표일 대비(빨강 12px 한 줄) · 다 갚는 달 — 과 「남은 빚과 상환 계획으로 다 갚는 달을 계산해요」 · 「홈에 표시」.
# 저축 목적지(B)의 칸과 같은 모양이지만 내용이 다르다(소비 계획에서 빼는 몫 · 이 금액으로 맞추기 · 수익률 줄이 없음).
d_latedebt = card(
    gs_row(gs_ring(31, C["WARN"], C["WARN"]), '신용대출 다 갚기', gs_chip('부채 상환', C["WARN"], C["WARN_SOFT"]),
           '남은 원금 2,200만원 · 연 6.8%', f'다 갚는 달 2030년 11월 · {late2("1년 8개월")}', top=False)
    + f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px; margin: 2px 0 0; font-size: 12px; color: {C["INK3"]};">'
      f'<span>상환 조정 필요 · 부채 상환 · 우선순위 2</span><span style="white-space: nowrap;">목표일 2029년 3월 8일</span></div>'
    + f'<div style="display: flex; align-items: center; justify-content: space-between; margin-top: 11px; font-size: 12px; color: {C["INK3"]};">'
      f'<span>자세히</span><span style="font-weight: 600; color: {C["WARN"]};">접기 ⌃</span></div>'
    + f'<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 8px; margin-top: 8px;">'
      + gs_cell('매달 갚는 돈', '35만원') + gs_cell('매달 모으는 돈에서', '빠져요')
      + gs_cell('목표일 대비', '목표일보다 약 1년 8개월 늦어요', red=True, fs=12) + gs_cell('다 갚는 달', '2030년 11월') + '</div>'
    + f'<div style="font-size: 12px; line-height: 1.5; color: {C["INK2"]}; margin-top: 8px;">남은 빚과 상환 계획으로 다 갚는 달을 계산해요</div>'
    + f'<div style="display: inline-flex; align-items: center; height: 34px; padding: 0 12px; margin: 8px 0 12px; border-radius: 10px; border: 1px solid {C["LINE"]}; background: {C["INSET"]}; font-size: 12.5px; font-weight: 600; color: {C["INK"]};">홈에 표시</div>',
    pad="4px 14px")
d_design = card(
    f'<div style="font-size: 13px; font-weight: 700; color: {C["INK"]};">저장하면 이렇게 바뀌어요</div>'
    f'<div style="display: flex; flex-direction: column; gap: 4px; margin-top: 6px; font-size: 12px; line-height: 1.5; color: {C["INK2"]};">'
    f'<div>결혼 자금 매달 13만원 · {RED_S("지금 배분으로는 도착하기 어려워요")}</div>'
    f'<div>비상금 6개월 매달 70만 → 60만원 · {RED_S("도착 2027년 4월 → " + NOWRAP("2027년 5월"))}</div>'
    f'<div>투자 계좌 5,000만원 매달 19만 → 17만원 · {RED_S("도착 2033년 12월 → " + NOWRAP("2034년 8월"))}</div></div>', pad="13px 15px")

w('GoalsStates', state_sheet(
    '목적지 · 상태 7종',
    '내 목적지 화면에서 모양이 바뀌는 경우들입니다. 값은 <span style="white-space: nowrap;">시안 사용자(9월 8일)를</span> 앱에 넣어 나온 그대로입니다.',
    [('A · 「매달 모으는 돈 바꿔 보기 ›」로 110만원을 넣어 본 가정', a_top + a_panel + a_list
      + GS_CAP('바뀐 목적지 줄만 보라 점선 + 「가정」 칩이고, 매달 · 도착 글자도 보라예요. 「가정 종료」를 누르거나 탭을 떠나면 원래 값(90만원)으로 돌아와요. 저장되지 않아요.')),
     ('B · 비상금 6개월 한 줄을 펼쳤을 때', b_card
      + GS_CAP('「홈에 표시」는 홈 구성에 「대표 목적지」 카드를 켠 사람에게만 뜻이 있어요 — 기본 홈에는 대표 목적지 카드가 없어요.')),
     ('C · 비상금이 도착했을 때(1,500 / 1,500만원)', c_top + c_list + GS_ADD_GOAL + c_done
      + GS_CAP('도착한 목적지는 진행 중 목록과 「모두 도착하려면」에서 빠지고 「목적지 추가」 아래 「도착한 목적지」로 옮겨 가요. 부채 상환 목적지는 「다 갚았어요」.')),
     ('D ① · 목표일이 없는 목적지가 있을 때(투자 계좌의 목표일을 지운 경우)', d_nodate
      + GS_CAP('그 목적지는 매달 나눠 넣는 계산에서 빠지고(오른쪽 줄 「목표일이 있는 목적지에 80만원」) 줄은 회색 「목표일을 다시 정해 주세요」 — 빨강이 아니에요. 남은 목적지 몫이 다시 나뉘어 비상금은 매달 80만원 · 2027년 3월이 돼요.')),
     ('D ② · 지금 배분으로는 도착하기 어려울 때(목표액 3억원 · 360개월 넘게 걸림)', d_unreach
      + GS_CAP('도착 달 대신 빨간 「지금 배분으로는 도착하기 어려워요」 · 날짜 없음. 이때 맨 위는 「모두 도착하려면 793만원」 · 「목적지에 매달 703만원이 더 필요해요」.')),
     ('D ③ · 부채 상환 목적지가 목표일보다 늦을 때(목표일 2029년 3월 8일 · 펼친 모습)', d_latedebt
      + GS_CAP('「상환 계획대로」 대신 빨간 「목표일보다 약 1년 8개월 늦어요」, 펼치면 상태가 「상환 조정 필요」 — 다 갚는 달은 상환 계획이 정해요(미래 › 상환 계획).')),
     ('D ④ · 새 목적지 설계 — 저장하면 새 목적지가 도착하기 어려울 때(목표액 3억원)', d_design
      + GS_CAP('새 목적지 줄이 빨간 「지금 배분으로는 도착하기 어려워요」, 기존 목적지가 360개월을 넘기면 「도착 … → 도착하기 어려워요」. 나머지 줄은 GoalDesign 장과 같아요.'))],
    h=GOALSSTATES_H).replace('<h2 ', REF_PILL + '<h2 ', 1), keep_all=True)


# 새 목적지 설계 — 처음(빈 칸 · goals-28) · 다른 금액으로 계산해 보기 30만원(goals-16 · D13)
def gd_field(label, value, unit=None, req=False, ph=False, w=None, rb=None):
    return field(label, value, unit, required=req, w=w, ph=ph, readback=rb)


gd_empty = hero(
    f'<div style="display: flex; gap: 10px; align-items: flex-start;">{gd_field("이름", "예: 결혼 자금", ph=True)}{gd_field("목표액", "예: 3,000", "만원", req=True, ph=True, w=124)}</div>'
    f'<div style="display: flex; gap: 10px; margin-top: 12px; align-items: flex-start;">{gd_field("지금 모은 돈", "0", "만원", ph=True)}{period_field().replace(">7</span>", ">10</span>")}{gd_field("수익률 (연)", "0", "%", ph=True)}</div>'
    f'<div style="font-size: 11.5px; line-height: 1.45; color: {C["INK3"]}; margin-top: 10px;">수익률을 비워 두면 일반 저축(수익률 0%)으로 계산해요.</div>'
    f'<div style="margin-top: 10px; font-size: 12px; line-height: 1.45; color: {C["INK3"]};">목표액과 기간을 넣으면 매달 필요한 돈을 계산해요.</div>'
    f'<div style="margin-top: 14px;">{btn("목적지로 저장", "primary")}</div>', pad=15)

_G_ASM = 300_000


def _g_fv_a(m):
    bal = 5_000_000
    for _ in range(m):
        bal = bal * (1 + _G_MR) + _G_ASM
    return bal


assert round(_g_fv_a(84) / 10_000) == 3553          # 앱 「가정 매달 30만원 · 7년 뒤 3,553만」
_g_asm = ' L'.join(f'{_G_X(k):.1f} {_G_Y(_g_fv_a(12 * k)):.1f}' for k in range(8))
asm_chart = goal_chart.replace('<circle cx="316" cy="19.1" r="3.6"',
                               f'<path d="M{_g_asm}" stroke="{C["VIO"]}" stroke-width="2" stroke-dasharray="5 4" stroke-linecap="round" stroke-linejoin="round"/>'
                               f'<circle cx="316" cy="{_G_Y(_g_fv_a(84)):.1f}" r="3.4" fill="{C["SURF"]}" stroke="{C["VIO"]}" stroke-width="2"/><circle cx="316" cy="19.1" r="3.6"', 1)
asm_chart = asm_chart.replace('viewBox="0 0 326 122"', 'viewBox="0 -8 326 130"').replace('height="122"', 'height="130"').replace('height: 122px', 'height: 130px')
gd_asm = hero(
    f'<div style="font-size: 13px; font-weight: 600; color: {C["INK"]};">결혼 자금 · 목표액 3,000만원 · 지금 모은 돈 500만원 · 7년 · 수익률 연 4%</div>'
    f'<div style="margin-top: 10px;">{asm_chart}</div>'
    f'<div style="display: flex; align-items: center; gap: 6px; margin-top: 6px; font-size: 12px; font-weight: 600; color: {C["VIO_STRONG"]};">'
    f'<span style="width: 16px; height: 0; border-top: 2px dashed {C["VIO"]};"></span>가정 매달 30만원 · 7년 뒤 3,553만</div>'
    f'<div style="font-size: 12px; line-height: 1.5; color: {C["INK3"]}; margin-top: 8px;">위의 「저장하면 이렇게 바뀌어요」는 매달 넣어야 할 돈(24만원) 기준 그대로예요.</div>', pad=15)
gd_asm_body = card(
    f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px;"><span style="font-size: 13.5px; font-weight: 600; color: {C["INK"]};">매달 30만원 넣는 가정 · 계산 기준</span>{icon("down", 16, C["INK3"], 2)}</div>'
    f'<div style="font-size: 12px; line-height: 1.55; color: {C["INK2"]}; margin-top: 8px;">매달 넣을 돈을 적어 보면 그 돈으로 모았을 때를 보라 점선으로 보여 줘요. 이 목적지 하나만 본 가정이에요. 목적지로 저장해도 이 금액은 참고로만 남고, 실제로 이 목적지에 매달 넣을 돈은 다른 목적지와 함께 나눠 정해요.</div>'
    f'<div style="margin-top: 12px;">{solo(gd_field("매달 넣을 돈 (가정)", "30", "만원", rb="30만원"))}</div>'
    f'<div style="display: flex; align-items: flex-end; justify-content: space-between; gap: 8px; margin-top: 12px; padding: 12px; background: {C["VIO_SOFT"]}; border-radius: 14px;">'
    f'<div><div style="font-size: 11.5px; font-weight: 600; color: {C["VIO_STRONG"]};">가정대로 7년 뒤</div>'
    f'<div style="font-size: 22px; font-weight: 700; letter-spacing: -0.03em; color: {C["VIO_STRONG"]}; margin-top: 2px;">3,553<span style="font-size: 14px; font-weight: 600;">만원</span></div></div>'
    f'<span style="font-size: 12px; font-weight: 600; color: {C["VIO_STRONG"]};">목표액에 닿아요</span></div>'
    f'<div style="font-size: 11.5px; line-height: 1.55; color: {C["INK3"]}; margin-top: 10px;">보라 실선: 매달 넣어야 할 돈으로 모은 금액 · 회색 점선: 원금만(수익 없이 넣은 돈) · 보라 점선: 매달 넣을 돈 (가정). 매달 말에 넣고 수익률이 그대로라고 보고 계산해요. 물가 · 세금 · 수수료는 빼고 계산했어요.</div>'
    f'<div style="font-size: 11.5px; line-height: 1.55; color: {C["INK3"]}; margin-top: 8px;">추천 목적지는 필요한 것만 고르세요. 비상금은 자산 탭의 현금성 자산으로 채워 드려요 · 비상금으로 따로 둔 돈만 넣으려면 고쳐 주세요. 생활비 25년치는 1년 소비의 25배를 참고로 쓴 값이고, 은퇴할 수 있다는 뜻은 아니에요.</div>',
    pad="14px")

w('GoalDesignStates', state_sheet(
    '새 목적지 설계 · 상태 2종',
    '처음 들어갔을 때(빈 칸)와 「다른 금액으로 계산해 보기」에 매달 넣을 돈을 넣어 본 가정입니다.',
    [('A · 처음 들어갔을 때 — 목표액과 기간이 비어 있음', gd_empty
      + GS_CAP('빈 칸은 빨간 오류가 아니라 회색 안내 한 줄이에요. 목표액 · 기간을 넣으면 매달 넣어야 할 돈과 「저장하면 이렇게 바뀌어요」가 나와요(GoalDesign 장).')),
     ('B · 「다른 금액으로 계산해 보기」에 매달 30만원을 넣었을 때', gd_asm + gd_asm_body
      + GS_CAP('보라 점선 · 「가정」은 금액을 넣은 뒤에만 그려요. 넣은 금액은 저장되지 않아요.'))],
    h=GOALDESIGNSTATES_H).replace('<h2 ', REF_PILL + '<h2 ', 1), keep_all=True)
