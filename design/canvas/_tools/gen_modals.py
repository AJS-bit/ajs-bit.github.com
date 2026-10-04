# -*- coding: utf-8 -*-
import pathlib
from gen_common import *

OUT = pathlib.Path(__file__).resolve().parent.parent


def w(name, body, keep_all=True):
    """모달 · 시트 장은 설명 문장이 많아 word-break: keep-all 을 기본으로 켠다(gen_common.doc 의 기본값은 그대로 False)."""
    (OUT / f'{name}.dc.html').write_text(doc(body, keep_all=keep_all), encoding='utf-8')
    print('wrote', name)


def group(label, inner, meta=None, fixed=False, mb=9):
    """fixed=True 면 본문이 넘칠 때 이 구역이 눌리지 않는다(목록 마지막 행이 상자 테두리에 닿는 것 방지)."""
    m = f'<span style="font-size: 11.5px; color: {C["INK3"]};">{meta}</span>' if meta else ''
    root = '<div style="flex-shrink: 0;">' if fixed else '<div>'
    return (f'{root}<div style="display: flex; align-items: baseline; justify-content: space-between; gap: 8px; margin-bottom: {mb}px;">'
            f'<span style="font-size: 11px; font-weight: 600; letter-spacing: 0.07em; color: {C["INK3"]};">{label}</span>{m}</div>{inner}</div>')


def foldrow(label, meta=None, open_=False):
    m = f'<span style="font-size: 12px; color: {C["INK3"]};">{meta}</span>' if meta else ''
    return (f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px; height: 48px; '
            f'padding: 0 13px; border-radius: 12px; background: {C["INSET"]}; flex-shrink: 0;">'
            f'<span style="font-size: 13.5px; font-weight: 600; color: {C["INK"]};">{label}</span>'
            f'<div style="display: flex; align-items: center; gap: 8px;">{m}{icon("up" if open_ else "down", 16, C["INK4"], 2)}</div></div>')


def checkbox(text, on=True, tone="brand"):
    col = C["BRAND"] if tone == "brand" else C["NEG"]
    box = (f'<span style="width: 20px; height: 20px; border-radius: 6px; background: {col}; display: flex; align-items: center; '
           f'justify-content: center; flex-shrink: 0;">{icon("check", 13, "#FFFFFF", 3)}</span>') if on else (
        f'<span style="width: 20px; height: 20px; border-radius: 6px; border: 1.5px solid {C["INPUT"]}; flex-shrink: 0;"></span>')
    return (f'<div style="display: flex; align-items: flex-start; gap: 9px;">{box}'
            f'<span style="font-size: 12.5px; line-height: 1.5; color: {C["INK2"]};">{text}</span></div>')


def kv(k, v, vcol=None, h=42, last=False):
    return (f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px; min-height: {h}px; '
            f'{"" if last else "border-bottom: 1px solid " + C["LINE_ROW"] + ";"}">'
            f'<span style="font-size: 13px; color: {C["INK2"]};">{k}</span>'
            f'<span style="font-size: 13.5px; font-weight: 600; color: {vcol or C["INK"]};">{v}</span></div>')


# ══════════════ 0. 이 파일이 쓰는 장의 높이 ══════════════
# 긴 시트는 본문이 다 보이게 폰 한 화면(844)보다 길게 그린다(2026-09-25 · 앱 창은 스크롤). 값 = 실제 웹폰트로 잰 자연 높이 + 여백.
# gen_canvas.py TALL · screens.json 과 같아야 한다(sync_screens.py 가 어긋나면 알려 준다).
# 2026-09-27 fix-up 5 — 앱 c6b7de3 치수로: 내 수치 자연 1205 · 반복 기록 겹침 921 · 코칭 918(+ 24) · 목적지 추가(부채 상환)는 자연 824 라 한 화면 844
# (fix-up 6 — 한 화면 장인 목적지 추가 · 월급 입력은 sheet(grow_up=True): 본문이 길어지면 위 막이 줄어 아래가 잘리지 않는다)
H = {'ProfileDialog': 1229, 'ProfileDialogNoItems': 844, 'GoalDialogPreview': 981, 'AlertsPanelInfo': 844, 'RecurringDialog': 844, 'RecurringDialogOverlap': 945,
     'CoachPanel': 942, 'ImportReview': 905, 'GoalDialog': 844, 'MonthlyCloseV5': 1099,
     'Confirmations': 2265, 'MonthlyClose': 982}      # 확인 창 7종 자연 2241 + 24(2026-09-27 fix-up 5 앱 AlertDialog 치수 — 버튼 32)


def rowbtn(text, mt=0):
    """시트 안의 한 줄 버튼(회색 바탕 · 파란 ›) — 「월 추가 상환액 15만원 · 상환 계획에서 바꿔요 ›」 같은 이동 줄.
    앱 .navi-numbers-link-row 그대로: 안쪽 8 13 · 높이 48 · 13 / 500 / 18.85 ink-2(2026-09-27 fix-up 5 · 예전 14 / 500 ink)."""
    return (f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px; min-height: 48px; padding: 8px 13px; '
            f'border-radius: 12px; background: {C["INSET"]}; flex-shrink: 0; margin-top: {mt}px;">'
            f'<span style="font-size: 13px; font-weight: 500; line-height: 18.85px; color: {C["INK2"]};">{text}</span>{icon("right", 16, C["BRAND"], 2.2)}</div>')


def tri(open_=False, col=None):
    col = col or C["INK3"]
    path = 'M0 1.5 9 1.5 4.5 7.5Z' if open_ else 'M1.5 0 7.5 4.5 1.5 9Z'
    return (f'<svg width="9" height="9" viewBox="0 0 9 9" style="flex-shrink: 0;"><path d="{path}" fill="{col}"/></svg>')


def fold_line(text, open_=False, border=True, body=''):
    """접힌 칸 「▸ 표시 이름 · 순자산 참고선」 — 앱 details.profile-other-fidelity 그대로: 위 12 · 선 1(line-soft) · 안쪽 위 10 ·
    요약 11.5 / 400 ink-3 · 삼각 표시 뒤 3 · 열면 12 아래에 body(2026-09-27 fix-up 5 · 예전 13 / 선 line / 안쪽 13)."""
    bt = f'border-top: 1px solid {C["LINE_SOFT"]}; padding-top: 10px;' if border else ''
    return (f'<div style="margin-top: 12px; {bt} flex-shrink: 0;">'
            f'<div style="display: flex; align-items: center; gap: 3px; font-size: 11.5px; line-height: 17px; color: {C["INK3"]};">'
            f'{tri(open_)}<span>{text}</span></div>{body}</div>')


def pair(a, b, mt=0):
    return f'<div style="display: flex; gap: 10px; align-items: flex-start; margin-top: {mt}px;">{a}{b}</div>'


def xbtn():
    return (f'<div style="width: 36px; height: 36px; border-radius: 11px; background: {C["INSET"]}; display: flex; align-items: center; '
            f'justify-content: center; flex-shrink: 0;">{icon("x", 17, C["INK2"], 2.2)}</div>')


def del_x(label='삭제'):
    return (f'<div style="display: flex; align-items: center; gap: 8px; flex-shrink: 0;">{smallbtn(label, "danger", "trash", h=32)}{xbtn()}</div>')


# ══════════════ 1. 설정 · 내 수치 (D5 · home-9 · components/navi/numbers-sheet.tsx) ══════════════
TARGET_CARD = (
    f'<div style="padding: 13px; background: {C["INSET"]}; border-radius: 14px;">'
    f'<div style="display: flex; align-items: baseline; justify-content: space-between; gap: 8px;">'
    f'<span style="font-size: 13px; color: {C["INK2"]};">월급의 얼마까지 쓸까요?</span>'
    f'<span style="font-size: 22px; font-weight: 700; letter-spacing: -0.03em; color: {C["INK"]};">60<span style="font-size: 14px; font-weight: 600; color: {C["INK2"]};">%</span></span></div>'
    f'<div style="margin-top: 9px;">{slider(60)}</div>'
    f'<div style="display: flex; align-items: center; margin-top: 4px;">'
    f'<span style="flex: 1; font-size: 11px; color: {C["INK4"]};">0%</span>'
    f'<span style="font-size: 11.5px; font-weight: 600; color: {C["INK"]}; white-space: nowrap;">월 216만원까지</span>'
    f'<span style="flex: 1; text-align: right; font-size: 11px; color: {C["INK4"]};">100%</span></div>'
    f'<div style="margin-top: 11px;">{note("처음 값 60%는 통계 평균이나 정답이 아니라 <b style=font-weight:600>바꿔도 되는 계획 시작값</b>이에요. 0%로 저장해도 60%로 되돌리지 않아요.", "mute")}</div></div>')

LOCK_NOTE = (      # 앱 .profile-information(위 9 · 안쪽 10 11 · 11.5 / 17.25 · 링크는 같은 문단의 글자 버튼 11.5 / 500 — 2026-09-27 fix-up 5)
    f'<div style="display: flex; gap: 8px; padding: 10px 11px; background: {C["INSET"]}; border-radius: 12px; margin-top: 9px;">'
    f'<span style="flex-shrink: 0; margin-top: 1px;">{icon("lock", 14, C["INK3"], 1.9)}</span>'
    f'<div style="min-width: 0; font-size: 11.5px; line-height: 17.25px; color: {C["INK3"]};">자산 5건 · 부채 4건의 합계라서 여기서는 고칠 수 없어요. '
    f'<span style="font-weight: 500; color: {C["BRAND"]}; white-space: nowrap;">자산 탭에서 고치기 &rsaquo;</span></div></div>')


# 앱 numbers-sheet 하네스(390 × 844 · 시트 윗변 60) 그대로 — 「선택 사항」 = 이름 뒤 9 · 접힌 칸은 「추가 설정」 묶음 안 맨 끝(위 12) ·
# 연 칸은 그 12 아래 세로 간격 10(2026-09-27 fix-up 5 · 예전 시트 윗변 40 · 접힌 칸이 따로 15 아래 · 글 13 · 줄 14).
NUM_OPEN = (
    f'<div style="margin-top: 12px; display: flex; flex-direction: column; gap: 10px;">'
    + solo(field('표시 이름', '예: 주성', ph=True)).replace('font-size: 15px; font-weight: 400;', 'font-size: 14px; font-weight: 500;', 1)
    + f'<div><div style="font-size: 12px; font-weight: 600; line-height: 18px; color: {C["INK2"]}; margin-bottom: 7px;">한 달에 순자산의 몇 %까지 쓸까요?</div>'
      f'<div style="display: flex; align-items: center; gap: 5px; width: 192px; height: 46px; padding: 0 12px; border-radius: 11px; border: 1px solid {C["INPUT"]}; background: {C["SURF"]};">'
      f'<span style="flex: 1; text-align: right; font-size: 17px; font-weight: 600; color: {C["INK"]};">1.8</span><span style="font-size: 13px; font-weight: 500; color: {C["INK3"]};">%</span></div></div>'
    + f'<div style="font-size: 12px; line-height: 18px; color: {C["INK3"]};">참고로만 보여 줘요 · 지금 순자산이면 월 168만원 · 연 21.6%</div></div>')


def profile_sheet(items=True, h=844, scrim=60):
    extra = pair(field('부수입', '30', '만원', optional=True, readback='30만원', opt_gap=9),
                 field('투자 자산 기본 수익률', '5', '%', optional=True, opt_gap=9))
    if items:
        extra += (pair(field('총자산', '18,210', '만원', state='readonly', readback='1억 8,210만원'),
                       field('총부채', '8,860', '만원', state='readonly', readback='8,860만원'), mt=12)
                  + LOCK_NOTE + rowbtn('월 추가 상환액 15만원 · 상환 계획에서 바꿔요', mt=12)
                  + fold_line('표시 이름 · 순자산 참고선', open_=True, body=NUM_OPEN))      # 자산 · 부채가 있는 장은 접힌 칸을 연 모습(2026-09-27 fix-up 3 · 앱 numbers-sheet)
    else:
        extra += rowbtn('자산 · 부채는 자산 탭에서 하나씩 넣어요', mt=12) + fold_line('표시 이름 · 순자산 참고선')
    return sheet(
        '내 수치', '월급과 소비 목표만 있으면 홈의 숫자가 계산돼요. 나머지는 언제든 채워도 돼요.',
        group('기본', pair(field('월급 (실수령)', '360', '만원', readback='360만원'),
                          field('나이', '28', '세', optional=True, w=104, helper='또래 비교에만 써요', opt_gap=9))) +
        group('소비 목표', TARGET_CARD) +
        group('추가 설정', extra),
        sheet_footer('취소', '저장'), scrim_h=scrim, h=h, body_pb=14 if items else 0)      # 항목 없는 장은 844 한 화면 — 앱도 본문이 2px 넘쳐 스크롤(아래 14 여백은 화면 밖)


w('ProfileDialog', profile_sheet(True, H['ProfileDialog']))
# 자산 · 부채를 하나도 넣지 않은 사람 — 총자산 · 총부채 칸 대신 자산 탭으로 가는 줄 하나(D5 · first-run-2). 월 추가 상환액 줄도 없다.
w('ProfileDialogNoItems', profile_sheet(False, H['ProfileDialogNoItems']))


# ══════════════ 1-2. 월급 입력 (D5 · first-run-22 · components/navi/salary-sheet.tsx) ══════════════
w('SalarySheet', sheet(
    '월급 입력', '월급의 몇 %를 썼는지 계산하는 기준이에요.',
    solo(field('월급 (실수령)', '360', '만원', readback='360만원', helper='부수입 · 저축 이체 · 대출상환은 빼고 넣어 주세요.')) +
    # 앱 salary-sheet 하네스(390 × 844 · 시트 윗변 447): 살아 있는 줄 = 도움말 6 아래 13 / 600 / 19.5 · 「다른 수치도 입력하기 ›」 = 15 아래 높이 44 글자 버튼 13 / 600(2026-09-27 fix-up 5)
    f'<div style="font-size: 13px; font-weight: 600; line-height: 19.5px; color: {C["INK"]}; margin-top: -9px; flex-shrink: 0;">소비 목표 60% · 월 216만원까지</div>'
    f'<div style="display: flex; align-items: center; height: 44px; font-size: 13px; font-weight: 600; color: {C["BRAND"]}; flex-shrink: 0;">다른 수치도 입력하기 &rsaquo;</div>',
    # 시트는 아래에 붙고 위 막(447)이 줄어든다 — 본문 자연 높이가 곧 시트 높이라 글꼴이 조금 달라도 아래가 잘리지 않는다(2026-09-27 fix-up 6 · 예전 막 447 고정 · 여유 0)
    sheet_footer('나중에', '저장'), scrim_h=447, body_pb=14, grow_up=True))


# ══════════════ 1-3. 순자산 대비 소비 (home-8 · components/navi/net-worth-ratio-sheet.tsx) ══════════════
NWR_TOP = 551      # 앱 하네스(390 × 844) 시트 윗변 — 시트 높이 293
nwr_btn = lambda label, primary: (
    f'<div style="flex: 1; display: flex; align-items: center; justify-content: center; gap: 2px; height: 44px; border-radius: 10px; font-size: 14px; font-weight: 600; white-space: nowrap; '
    + (f'background: {C["BRAND"]}; color: #FFFFFF;">{label}</div>' if primary else
       f'background: {C["BG"]}; border: 1px solid {C["LINE"]}; color: {C["INK"]};">{label}{icon("right", 16, C["INK"], 2.2)}</div>'))
w('NetWorthRatioSheet', frame(
    f'<div style="height: {NWR_TOP}px; flex-shrink: 0;"></div>'
    f'<div style="flex: 1; min-height: 0; position: relative; background: {C["SURF"]}; border: 1px solid {C["LINE"]}; border-bottom: 0; border-radius: 26px 26px 0 0; display: flex; flex-direction: column; overflow: hidden;">'
    f'<span style="position: absolute; top: 8px; left: 50%; margin-left: -19px; width: 38px; height: 4px; border-radius: 99px; background: {C["BORDER"]};"></span>'
    f'<div style="padding: 24px 56px 20px 20px; display: flex; flex-direction: column; gap: 8px; flex-shrink: 0;">'
    f'<h2 style="margin: 0; font-size: 21px; font-weight: 750; line-height: 25.2px; letter-spacing: -0.025em; color: {C["INK"]};">순자산 대비 소비</h2>'
    f'<div style="margin-top: 10px; display: flex; flex-direction: column; gap: 8px;">'
    f'<p style="margin: 0; font-size: 15px; line-height: 24px; color: {C["INK"]};">이번 달 지금까지 쓴 112만원은 내 순자산 9,350만원의 1.2%예요.</p>'
    f'<p style="margin: 0; font-size: 15px; line-height: 24px; color: {C["INK"]};">월말 예상 208만원으로 치면 2.2%예요.</p>'
    f'<p style="margin: 0; font-size: 13px; line-height: 20.8px; color: {C["INK3"]};">순자산은 가진 자산에서 갚을 부채를 뺀 금액이에요. 순자산이 클수록 같은 소비도 작은 비율이 돼요.</p></div></div>'
    f'<div style="margin-top: auto; display: flex; gap: 10px; padding: 14px 20px 15px; border-top: 1px solid {C["LINE_SOFT"]}; flex-shrink: 0;">'
    f'{nwr_btn("자산 탭에서 보기", False)}{nwr_btn("닫기", True)}</div></div>',
    bg='#CFD3E1'))      # 앱: 밝게 흐린 겉 · 닫기 안내 없음 · 본문이 DialogHeader 안(선 없음) · 기본 Dialog 크기(2026-09-27 fix-up 4 · 예전 18 / 700 · 354 · 48)


# ══════════════ 2. 자산 추가 · 수정 (assets-1 · assets-4 · assets-14 · assets-17 · components/navi/asset-view.tsx) ══════════════
w('AssetDialog', sheet(
    '자산 추가', '이름과 지금 금액만 있으면 저장돼요.',
    f'{solo(field("자산 이름", "ETF 계좌", required=True))}'
    + pair(select_field('유형', '투자', helper='현금+투자자산에 들어가요 · 비상금에는 안 들어가요'),
           field('지금 금액', '4,890', '만원', required=True, w=142, readback='4,890만원'))
    + solo(field('수익률 (연)', '6.5', '%', optional=True, helper='비워 두면 투자 자산 기본 수익률 연 5.0%를 써요 · 설정에서 바꿀 수 있어요')),
    sheet_footer('취소', '자산 추가'), scrim_h=190, body_pb=14))

# 자산 수정 — 시안 사용자의 생활비 통장(현금성 · 1,460만원 · 직접 넣은 수익률 연 2.5% · 9월 1일 확인)
w('AssetEditDialog', sheet(
    '자산 수정', '지금 통장에 찍힌 금액으로 고치세요. 지난 기록은 그대로 남아요.',
    f'{solo(field("자산 이름", "생활비 통장", required=True))}'
    + pair(select_field('유형', '현금성', helper='비상금(생활비 몇 달 치)과 현금+투자자산에 들어가요'),
           field('지금 금액', '1,460', '만원', required=True, w=142, readback='1,460만원'))
    + solo(field('수익률 (연)', '2.5', '%', optional=True, helper='비워 두면 현금성 기본 수익률 연 3.0%를 써요'))
    # 앱 .asset-rate-source — 수익률 도움말 6 아래 11.5 / 17.25 ink-2 · 시트 윗변 190(앱 하네스 · 2026-09-27 fix-up 5 · 예전 12 / 1.6 · 170)
    + f'<div style="font-size: 11.5px; line-height: 17.25px; color: {C["INK2"]}; margin-top: -9px; flex-shrink: 0;">지금 적용 연 2.5% · 직접 입력<br>마지막 확인 2026년 9월 1일</div>',
    sheet_footer('취소', '변경 저장'), scrim_h=190, body_pb=14, header_right=del_x()))


# ══════════════ 2-2. 잔액 한 번에 확인 (assets-15 · components/navi/balance-check-sheet.tsx) ══════════════
# 자산 › 자산 구성의 주황 띠 「잔액 확인이 필요한 자산 2개 · 한 번에 확인 ›」(AssetsStale)를 누른 모습 — 같은 날(9월 8일)의 시안 사용자에서
# ETF 계좌 마지막 확인 7월 30일 · 청약저축 확인 기록 없음. 확인이 필요한 자산만 줄로 나온다(2026-09-27 fix-up 4 · 예전 그림은 10월 7일 이후 다섯 줄).
# 앱 b574373 하네스 그대로: 시트 윗변 190(내용이 짧아도 높이 654) · 줄 카드 안쪽 12 · 이름 12.5 / 600 · 부제 11 · 금액 칸 46 · 되읽기 · 「그대로예요」 82 × 46.
def bal_row(name, sub, man, readback):
    box = (f'<div style="flex: 1; min-width: 0;"><div style="display: flex; align-items: center; gap: 4px; height: 46px; padding: 0 10px; border-radius: 11px; '
           f'border: 1px solid {C["INPUT"]}; background: {C["SURF"]};"><span style="flex: 1; text-align: right; font-size: 12.5px; font-weight: 600; color: {C["INK"]};">{man}</span>'
           f'<span style="font-size: 11.5px; color: {C["INK3"]};">만원</span></div>'
           f'<div style="font-size: 12px; font-weight: 500; line-height: 16px; color: {C["INK3"]}; margin-top: 4px;">= {readback}</div></div>')
    same = (f'<div style="display: flex; align-items: center; justify-content: center; width: 82px; height: 46px; border-radius: 13px; background: {C["BG"]}; '
            f'border: 1px solid {C["LINE"]}; font-size: 12.5px; font-weight: 600; color: {C["INK"]}; white-space: nowrap; flex-shrink: 0;">그대로예요</div>')
    return (f'<div style="padding: 12px; border-radius: 14px; background: {C["SURF"]}; border: 1px solid {C["LINE"]}; flex-shrink: 0;">'
            f'<div style="font-size: 12.5px; font-weight: 600; line-height: 19px; color: {C["INK"]};">{name}</div>'
            f'<div style="font-size: 11px; line-height: 16px; color: {C["INK3"]}; margin-top: 2px;">{sub}</div>'
            f'<div style="display: flex; align-items: flex-start; gap: 8px; margin-top: 8px;">{box}{same}</div></div>')


w('AssetBalanceCheck', sheet(
    '잔액 한 번에 확인', '통장·증권 앱에서 지금 금액을 보고, 같으면 「그대로예요」를 누르세요.',
    f'<div style="font-size: 11.5px; font-weight: 600; line-height: 17px; color: {C["INK3"]}; flex-shrink: 0;">2개 중 0개 확인함</div>'
    + f'<div style="display: flex; flex-direction: column; gap: 10px; flex-shrink: 0;">'
    + bal_row('ETF 계좌', '투자 · 마지막 확인 7월 30일', '4,890', '4,890만원')
    + bal_row('청약저축', '기타 · 확인 기록 없음', '500', '500만원') + '</div>',
    btn('닫기', 'secondary', h=48), scrim_h=190, body_gap=15, header_right=''))


# ══════════════ 3. 부채 수정 (assets-1 · assets-7 · assets-17 · assets-23 · D6) ══════════════
w('DebtDialog', sheet(
    '카드 할부 수정', '금리와 매달 내는 돈으로 다 갚는 달을 계산해요.',
    f'{solo(field("부채 이름", "카드 할부", required=True))}'
    + pair(select_field('유형', '카드/리볼빙'), field('남은 원금', '180', '만원', required=True, w=142, readback='180만원'))
    + pair(field('연 금리', '14.5', '%', required=True),
           field('월 최소 상환액', '20', '만원', w=142, readback='20만원', helper='매달 내는 돈(원금+이자) · 이자만 내면 이자를 적어요'))
    + note('연 14.5%는 보유한 부채 중 가장 높아요. 상환 계획에서 순서를 확인하세요.', 'warn', 'warn')
    + note('다 갚았다면 삭제하지 말고 남은 원금을 0으로 저장하세요. 연결된 부채 상환 목적지가 다 갚은 것으로 남아요.', 'mute'),
    sheet_footer('취소', '변경 저장'), scrim_h=110, body_pb=14, header_right=del_x()))      # 시트 윗변 110 = 앱 하네스(2026-09-27 fix-up 5 · 예전 90)


# ══════════════ 4. 목적지 추가 — 부채 상환 (goals-15 · assets-23 · components/navi/goal-dialog.tsx) ══════════════
types = []
TYPES = [("일반 저축", "wallet", C["BRAND"]), ("비상금", "shield", C["SKY"]), ("투자", "chart", C["VIO"]),
         ("순자산", "target", C["POS"]), ("부채 상환", "bank", C["WARN"])]
for i, (name, ic, col) in enumerate(TYPES):
    sel = i == 4
    types.append(
        f'<div style="flex: 1; min-width: 0; padding: 10px 6px; border-radius: 12px; text-align: center; '
        f'border: {"1.5px solid " + col if sel else "1px solid " + C["LINE"]}; background: {col + "14" if sel else C["SURF"]};">'
        f'<div style="display: flex; justify-content: center;">{icon(ic, 17, col if sel else C["INK3"], 1.9)}</div>'
        f'<div style="font-size: 11px; font-weight: {700 if sel else 500}; color: {col if sel else C["INK2"]}; margin-top: 5px; white-space: nowrap;">{name}</div></div>')

# 시안 사용자의 부채 넷 — 앱과 같은 순서(기록 순) · 「{유형} · {잔액} · 연 {금리}」(assets-23 유형 이름)
# 예시 = 아직 없는 목적지 「카드 할부 다 갚기」(2026-09-27 fix-up — 시안 사용자에게는 「신용대출 다 갚기」가 이미 있어 같은 목적지를 또 만드는 그림이 됐다)
DEBT_PICK = [("주택담보대출", "주택담보 · 전세대출 · 6,200만원 · 연 3.4%", False), ("신용대출", "신용대출 · 2,200만원 · 연 6.8%", False),
             ("학자금대출", "학자금 · 280만원 · 연 2.5%", False), ("카드 할부", "카드/리볼빙 · 180만원 · 연 14.5%", True)]
debtpick = []
for i, (name, sub, on) in enumerate(DEBT_PICK):
    box = (f'<span style="width: 20px; height: 20px; border-radius: 6px; background: {C["BRAND"]}; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">{icon("check", 13, "#FFFFFF", 3)}</span>'
           if on else f'<span style="width: 20px; height: 20px; border-radius: 6px; border: 1.5px solid {C["INPUT"]}; background: {C["SURF"]}; flex-shrink: 0;"></span>')
    # 앱 .goal-debt-row-fidelity — 줄 높이 46(선 포함) · 아래 선 line-row(마지막 없음) · 이름 13.5 / 600 · 부제 11 / 16.5(2026-09-27 fix-up 5 · 예전 44 · 선 없음)
    bb = f'border-bottom: 1px solid {C["LINE_ROW"]};' if i < len(DEBT_PICK) - 1 else ''
    debtpick.append(
        f'<div style="display: flex; align-items: center; gap: 10px; min-height: 46px; {bb}">{box}'
        f'<div style="flex: 1; min-width: 0;"><div style="font-size: 13.5px; font-weight: 600; color: {C["INK"]};">{name}</div>'
        f'<div style="font-size: 11px; line-height: 16.5px; color: {C["INK3"]};">{sub}</div></div></div>')

w('GoalDialog', sheet(
    '목적지 추가', '유형에 따라 필요한 값이 달라져요.',
    group('유형', f'<div style="display: flex; gap: 6px;">{"".join(types)}</div>') +
    f'{solo(field("이름", "카드 할부 다 갚기", required=True))}'
    # 접힌 칸 「▸ 표시 아이콘 🏔️」 = 앱 .goal-display-fidelity — 이름 칸 6 아래 · 요약 위아래 2 · 11.5 · 삼각 뒤 3 · 그림 왼쪽 4(2026-09-27 fix-up 5 · 예전 13 / 14)
    + f'<div style="display: flex; align-items: center; gap: 3px; height: 23px; margin-top: -9px; font-size: 11.5px; color: {C["INK3"]}; flex-shrink: 0;">{tri()}<span>표시 아이콘</span><span style="margin-left: 4px; font-size: 11.5px;">🏔️</span></div>'
    + group('갚을 부채', f'<div style="padding: 0 13px; background: {C["INSET"]}; border-radius: 14px; flex-shrink: 0;">{"".join(debtpick)}</div>',
            meta='1개 골랐어요 · 180만원', fixed=True)
    + pair(select_field('우선순위', '1순위 · 가장 먼저'), field('목표일', '2029. 06. 30.', required=True, w=160))
    + note('남은 빚과 상환 계획으로 다 갚는 달을 계산해요<br>목표액과 진행률은 실제 남은 원금에서 자동으로 계산해요. 매달 모으는 돈에서 따로 나눠 넣지 않아요.', 'mute'),
    # 앱 .dialog-body 아래 안쪽 0(목적지 추가 창). 본문 아래 빈칸 20 + 위 막 40 → 12 까지 줄어듦 = 글꼴이 달라 본문이 48 까지 길어져도 잘리지 않음(2026-09-27 fix-up 6)
    sheet_footer('취소', '목적지 추가'), scrim_h=40, body_pb=0, h=H['GoalDialog'], grow_up=True))



# ══════════════ 4-2. 목적지 추가 — 저축 유형 · 저장 전 미리 보기 (goals-15 · goals-3 · D1 · 2026-09-27 fix-up 3 · 앱 goal-dialog.tsx) ══════════════
# 시안 사용자(9월 8일)에 「여행 자금 · 300만원 · 1년(2027. 09. 08.) · 2순위」를 넣은 앱 화면(하네스) 그대로. 미리 보기 상자 = 이대로면 매달 · 도착 →
# 저장하면 이렇게 바뀌어요(새 목적지 · 늦어지는 목적지는 도착이 빨강) → D1 참고 줄(ink-3 · 이번 달 한도는 그대로). 숫자는 앱 배분(naviGoalAllocation) 값.
types_saving = []
for i, (name, ic, col) in enumerate(TYPES):
    sel = i == 0
    types_saving.append(
        f'<div style="flex: 1; min-width: 0; padding: 10px 6px; border-radius: 12px; text-align: center; '
        f'border: {"1.5px solid " + col if sel else "1px solid " + C["LINE"]}; background: {col + "14" if sel else C["SURF"]};">'
        f'<div style="display: flex; justify-content: center;">{icon(ic, 17, col if sel else C["INK3"], 1.9)}</div>'
        f'<div style="font-size: 11px; font-weight: {700 if sel else 500}; color: {col if sel else C["INK2"]}; margin-top: 5px; white-space: nowrap;">{name}</div></div>')
RED = lambda s: f'<span style="color: {C["NEG"]};">{s}</span>'
NW_ = lambda s: f'<span style="white-space: nowrap;">{s}</span>'
def date_chip(label, on=False):
    st = (f'border: 1px solid {C["BRAND"]}; background: {C["BRAND_SOFT"]}; color: {C["BRAND"]}; font-weight: 600;' if on else
          f'border: 1px solid {C["BORDER"]}; background: {C["SURF"]}; color: {C["INK2"]}; font-weight: 500;')
    return f'<span style="display: inline-flex; align-items: center; height: 30px; padding: 0 10px; border-radius: 10px; font-size: 12.5px; white-space: nowrap; flex-shrink: 0; {st}">{label}</span>'
gd_date = (f'<div style="width: 160px; flex-shrink: 0;"><div style="font-size: 12px; font-weight: 600; line-height: 18px; color: {C["INK2"]}; margin-bottom: 7px;">목표일 <span style="color: {C["NEG"]};">*</span></div>'
           f'<div style="display: flex; gap: 6px;">{date_chip("6개월")}{date_chip("1년", True)}{date_chip("2년")}</div>'
           f'<div style="display: flex; align-items: center; height: 46px; padding: 0 12px; margin-top: 6px; border-radius: 11px; border: 1px solid {C["INPUT"]}; background: {C["SURF"]}; '
           f'font-size: 15px; color: {C["INK"]};">2027. 09. 08.</div></div>')
KEEP = lambda t: f'<span style="white-space: nowrap;">{t}</span>'      # 앱 .goal-save-preview-keep — 금액 · 날짜는 줄 끝에서 갈라지지 않는다
gd_preview = (f'<div style="padding: 10px 12px; background: {C["INSET"]}; border-radius: 12px; flex-shrink: 0; display: flex; flex-direction: column; gap: 6px; font-size: 13px; line-height: 19.5px; color: {C["INK2"]};">'
              f'<div>이대로면 매달 {KEEP("25만원")}씩 모아야 해요 · {KEEP("2027년 9월")}에 도착</div>'
              f'<div style="display: flex; flex-direction: column; gap: 4px;">'
              f'<div style="font-size: 12.5px; font-weight: 600; line-height: 18.125px;">저장하면 이렇게 바뀌어요</div>'
              f'<div style="display: flex; flex-direction: column; gap: 4px; font-size: 12.5px; line-height: 18.75px;">'
              f'<div>여행 자금 매달 {KEEP("25만원")} · {KEEP("2027년 9월")} 도착 예상</div>'
              f'<div>비상금 6개월 매달 {KEEP("70만")} → {KEEP("51만원")} · {RED("도착 " + KEEP("2027년 4월") + " → " + KEEP("2027년 7월"))}</div>'
              f'<div>투자 계좌 5,000만원 매달 {KEEP("19만")} → {KEEP("14만원")} · {RED("도착 " + KEEP("2033년 12월") + " → " + KEEP("2035년 5월"))}</div></div></div>'
              f'<div style="font-size: 12px; line-height: 18px; color: {C["INK3"]};">저장하면 \'저축 · 상환 계획까지 지키려면\' 금액이 152만원 → 127만원으로 바뀌어요. 이번 달 한도는 그대로예요.</div></div>')
w('GoalDialogPreview', sheet(
    '목적지 추가', '유형에 따라 필요한 값이 달라져요.',
    group('유형', f'<div style="display: flex; gap: 6px;">{"".join(types_saving)}</div>') +
    f'{solo(field("이름", "여행 자금", required=True))}'
    + f'<div style="display: flex; align-items: center; gap: 3px; height: 23px; margin-top: -9px; font-size: 11.5px; color: {C["INK3"]}; flex-shrink: 0;">{tri()}<span>표시 아이콘</span><span style="margin-left: 4px; font-size: 11.5px;">🎯</span></div>'
    + pair(field('목표액', '300', '만원', required=True, readback='300만원'), field('지금 모은 돈', '', '만원'))
    + pair(select_field('우선순위', '2순위 · 보통', w=None), gd_date)
    + gd_preview
    + note('수익 없이 넣은 돈만 계산해요', 'mute'),
    sheet_footer('취소', '목적지 추가'), scrim_h=40, body_pb=14, h=H['GoalDialogPreview']))


# ══════════════ 5. 반복 기록 (record-2 · D4 · components/navi/spending-view.tsx) ══════════════
def rule_rows():
    rules = []
    # 시안 사용자의 규칙 셋(NUMBERS §17 · W/design-state.json settings.recurringRules · RecurringPrefill · DesktopLedger 와 같게 · 2026-09-27 fix-up 2 — 옛 v3 샘플 5일 · 2만원을 거둠).
    # 휴대폰 요금 55,000원은 2026-09-21 금액 쓰는 법대로 5.5만원(앱 compact 6만원은 앱 후속).
    for i, (name, meta, amt, on) in enumerate([("ETF 자동이체", "매월 6일 · 저축·투자", "30만원", True),
                                               ("휴대폰 요금", "매월 25일 · 통신", "5.5만원", True),
                                               ("헬스장", "꺼 둠 · 문화/여가", "5만원", False)]):
        col = C["INK"] if on else C["INK4"]
        rules.append(
            f'<div style="display: flex; align-items: center; gap: 10px; min-height: 52px; '
            f'{"border-bottom: 1px solid " + C["LINE_ROW"] + ";" if i < 2 else ""}">'
            f'<div style="flex: 1; min-width: 0;"><div style="font-size: 13.5px; font-weight: 600; color: {col};">{name}</div>'
            f'<div style="font-size: 11px; color: {C["INK4"] if not on else C["INK3"]};">{meta}</div></div>'
            f'<span style="font-size: 13.5px; font-weight: 600; color: {col};">{amt}</span>'
            f'{toggle(on)}{icon("more", 16, C["INK4"], 2.2)}</div>')
    return (f'<div style="padding: 0 13px; background: {C["SURF"]}; border: 1px solid {C["LINE"]}; border-radius: 14px;">{"".join(rules)}</div>')


def month_field(label, value):
    return (f'<div style="flex: 0 0 auto; min-width: 0;"><div style="font-size: 12px; font-weight: 600; color: {C["INK2"]}; margin-bottom: 7px;">{label}</div>'
            f'<div style="display: flex; align-items: center; justify-content: space-between; height: 46px; padding: 0 12px; border-radius: 11px; '
            f'border: 1px solid {C["INPUT"]}; background: {C["SURF"]};"><span style="font-size: 15px; color: {C["INK"]};">{value}</span>'
            f'{icon("cal", 16, C["INK2"], 1.9)}</div></div>')


# 앱 .recurring-information-fidelity(위 11 · 안쪽 10 11 · 11.5 / 17.25) · 안의 접힌 칸 「▸ 반복 기록이 만들어지는 방식」(6 아래 · 11.5 / 500 ink-3 · 삼각 뒤 3)
# (2026-09-27 fix-up 5 · 예전 안쪽 11 12 · 접힌 칸 12.5 / 500 ink-2 · 7 아래 · 삼각 뒤 6)
RULE_NOTE = (
    f'<div style="display: flex; gap: 8px; padding: 10px 11px; background: {C["INSET"]}; border-radius: 12px; margin-top: 11px;">'
    f'<span style="flex-shrink: 0; margin-top: 1px;">{icon("info", 14, C["INK3"], 1.9)}</span>'
    f'<div style="min-width: 0;"><div style="font-size: 11.5px; line-height: 17.25px; color: {C["INK3"]};">이번 달 결제일이 이미 지났으면 저장하자마자 이번 달 기록이 만들어져요 · 이미 적어 둔 같은 기록이 있으면 먼저 물어봐요</div>'
    f'<div style="display: flex; align-items: center; gap: 3px; margin-top: 6px; font-size: 11.5px; font-weight: 500; line-height: 17.25px; color: {C["INK3"]};">{tri()}반복 기록이 만들어지는 방식</div></div></div>')


def new_rule(name, amt, cat, day, start):
    # 앱 .recurring-name-amount-fidelity — 이름 208 · 금액 136(사이 10) · 결제 줄 12 아래 · 시작 월은 그 격자 안 10 아래(2026-09-27 fix-up 5 · 예전 금액 142 · 시작 월 12)
    return (pair(field('이름', name, required=True), field('금액', amt, '원', required=True, w=136))
            + pair(select_field('카테고리', cat, required=True), field('결제일', day, '일', w=104), mt=12)
            + f'<div style="margin-top: 10px;">{month_field("시작 월", start)}</div>' + RULE_NOTE)


RECUR_DESC = '매달 반복되는 기록이에요. 앱을 열면 시작 월부터 이미 지난 결제일도 기록으로 만들어요.'
w('RecurringDialog', sheet(
    '반복 기록', RECUR_DESC,
    group('등록된 반복 기록', rule_rows(), meta='3건 · 켜짐 2건') +
    group('새 반복 기록', new_rule('넷플릭스', '13,500', '구독', '15', '2026년 10월')),
    sheet_footer('닫기', '반복 기록 추가'), scrim_h=40, h=H['RecurringDialog']))

# 겹침 확인(record-2) — 9월 1일에 이미 적은 관리비 320,000원(LedgerV5)과 같은 규칙을 이번 달부터 만들 때
OVERLAP_BTN = lambda t, soft: (
    f'<span style="display: inline-flex; align-items: center; height: 34px; padding: 0 11px; border-radius: 9px; font-size: 13px; font-weight: 600; white-space: nowrap; flex-shrink: 0; '
    + (f'background: {C["BRAND_SOFT"]}; border: 1px solid transparent; color: {C["BRAND"]};">' if soft else
       f'background: {C["SURF"]}; border: 1px solid {C["LINE"]}; color: {C["INK2"]};">') + f'{t}</span>')
# 앱 .recurring-overlap-confirm — 규칙 묶음 12 아래 · 안쪽 11 12 · 모서리 12 · 질문 13 / 600 / 18.85 · 버튼 줄 9 아래 · 버튼 34(안쪽 0 11 · 모서리 9)
# (2026-09-27 fix-up 5 · 예전 안쪽 14 · 질문 14 / 700 · 버튼 38 · 11 아래)
OVERLAP_BOX = (
    f'<div style="padding: 11px 12px; margin-top: 12px; background: {C["INSET"]}; border-radius: 12px; flex-shrink: 0; display: flex; flex-direction: column; gap: 9px;">'
    f'<div style="font-size: 13px; font-weight: 600; line-height: 18.85px; color: {C["INK"]};">9월 1일에 같은 금액(주거/관리 320,000원)이 이미 있어요 — 이번 달은 건너뛸까요?</div>'
    f'<div style="display: flex; gap: 8px;">{OVERLAP_BTN("이번 달은 건너뛰기", True)}{OVERLAP_BTN("그래도 추가", False)}</div></div>')
w('RecurringDialogOverlap', sheet(
    '반복 기록', RECUR_DESC,
    group('등록된 반복 기록', rule_rows(), meta='3건 · 켜짐 2건') +
    group('새 반복 기록', new_rule('관리비', '320,000', '주거/관리', '1', '2026년 9월')) + OVERLAP_BOX,
    sheet_footer('닫기', '이번 달은 건너뛰기'), scrim_h=40, h=H['RecurringDialogOverlap']))


# ══════════════ 6. 월 마감 — 이미 마감한 달을 다시 연 모습 (MonthlyClose — 원본 전용 · 캔버스 밖) ══════════════
# 옛 v3 그림(총수입 · 실수령 급여 · 저축·투자 이체 칸)을 앱 a724aac 의 「마감값 보기·고치기 ›」 모습으로 바꿨다(D4 · D9 · spending-6 ·
# 앱 캡처 shots/app/MonthlyCloseV5-reedit.png). 값은 8월 마감값(NUMBERS §5 — 3,900,000 · 3,600,000 · 920,000 · 1,715,200원 · 47.6%).
# 캔버스에는 첫 마감 MonthlyCloseV5 가 오르고, 이 모습은 자산 · 소비 페이지 노트에 글로 적혀 있다. 아래 MonthlyCloseV5 의 조각을 쓰므로 그 뒤에서 쓴다.
# ══════════════ 6-2. 8월 첫 마감 (MonthlyCloseV5 · spending-2 · spending-5 · spending-6 · D9 · components/navi/monthly-close-dialog.tsx) ══════════════
# 8월을 아직 마감하지 않은 날(6월만 마감)에 「8월 마감하기」를 눌렀을 때. 앱 첫 마감: 월급 + 부수입 = 지금 값, 그중 월급 = 비움,
# 대출상환 = 등록된 대출 월 최소 상환액 합(77만원), 월말 자산 · 부채 = 8월 기록(자산 180,400,000 · 부채 89,200,000), 소비 합계 = 8월 기록 1,715,200원.
# 카테고리 없음 3건 = 8월 달력(gen_calendar.AUG)의 11일 6,700 · 24일 5,600 · 26일 8,900원 칸.
from gen_calendar import AUG
UNCAT_AUG_DAYS = (11, 24, 26)
UNCAT_AUG_SUM = sum(AUG[d] for d in UNCAT_AUG_DAYS)
assert UNCAT_AUG_SUM == 21_200
UNCAT_LINE = (
    f'<div style="flex-shrink: 0; padding: 11px 13px; border: 1px solid {C["LINE"]}; border-radius: 12px; font-size: 12.5px; line-height: 1.55; color: {C["INK2"]};">'
    f'<span style="font-weight: 600; color: {C["INK"]};">카테고리 없음 {len(UNCAT_AUG_DAYS)}건 · {UNCAT_AUG_SUM:,}원이 기타로 들어가요</span> · 다음 달 한도 배분에도 기타로 들어가요 · '
    f'<span style="font-weight: 600; color: {C["BRAND"]}; white-space: nowrap;">카테고리 고르기 &rsaquo;</span></div>')


def tag_label(label, tag):
    return (f'{label} <span style="display: inline-block; margin-left: 4px; font-size: 11.5px; font-weight: 500; color: {C["INK3"]}; '
            f'background: {C["INSET"]}; border-radius: 99px; padding: 1px 8px;">{tag}</span>')


SALARY_LINK = (f'<div style="display: flex; justify-content: space-between; gap: 8px; margin-top: 6px; font-size: 11.5px;">'
               f'<span style="color: {C["INK3"]};">비우면 월급 대비 소비율이 안 나와요</span>'
               f'<span style="font-weight: 600; color: {C["BRAND"]}; white-space: nowrap;">지금 월급 3,600,000원 넣기</span></div>')

w('MonthlyCloseV5', sheet(
    '8월 마감', '그 달의 실제 수치를 확정해요. 저장한 값으로만 그 달 소비율을 계산해요.',
    f'<div style="flex-shrink: 0; padding: 10px 12px; background: {C["WARN_SOFT"]}; border-radius: 12px; font-size: 12.5px; color: {C["WARN_INK"]};">지금 값으로 채운 칸은 그 달 값으로 고쳐 주세요</div>' +
    group('그 달의 실제 수치',
          solo(field(tag_label('월급 + 부수입', '지금 값'), '3,900,000', '원'))
          + f'<div style="margin-top: 12px;">{solo(field("그중 월급", "", "원"))}{SALARY_LINK}</div>'
          + f'<div style="margin-top: 12px;">{solo(field(tag_label("대출상환", "등록된 대출 월 최소 상환액"), "770,000", "원"))}</div>',
          meta='원 단위', fixed=True) +
    UNCAT_LINE +
    group('자동으로 채워진 값',
          f'<div style="padding: 2px 13px; background: {C["INSET"]}; border-radius: 14px;">'
          f'{kv("일반 소비 합계", "1,715,200원")}'
          f'{kv("월급 대비 소비율", "<span style=" + chr(34) + "color: " + C["INK3"] + "; font-weight: 500;" + chr(34) + ">— &nbsp;월급을 넣으면 보여요</span>")}'
          f'{kv("월말 총자산", "180,400,000원")}{kv("월말 총부채", "89,200,000원", last=True)}</div>', fixed=True) +
    f'<div style="display: flex; align-items: center; justify-content: space-between; height: 46px; padding: 0 14px; border-radius: 12px; border: 1px solid {C["LINE"]}; flex-shrink: 0;">'
    f'<span style="font-size: 13.5px; font-weight: 600; color: {C["BRAND"]};">바뀐 게 있으면 자산 고치기 &rsaquo;</span>{icon("down", 16, C["INK3"], 2)}</div>'
    f'<div style="font-size: 12px; line-height: 1.5; color: {C["INK3"]}; flex-shrink: 0;">소비 합계는 기록에서 계산해요. 마감 뒤 기록을 고치면 합계를 고치라고 알려 드려요.</div>',
    sheet_footer('취소', '마감 저장', save_kind='disabled'),
    sticky=f'<div style="padding: 11px 18px 12px; background: {C["INSET"]}; border-top: 1px solid {C["LINE"]}; flex-shrink: 0;">'
           f'<div style="font-size: 12px; color: {C["WARN_INK"]}; margin-bottom: 9px;">월급 칸이 비어 있어요 · 이 달 월급 대비 소비율은 —로 남아요</div>'
           f'{checkbox("이 달의 수입·상환·잔액을 확인했고, 빠진 소비 기록이 없는지 살펴봤어요", False)}</div>',
    scrim_h=40, body_gap=12, body_pb=14, h=H['MonthlyCloseV5']))


w('MonthlyClose', sheet(
    '8월 마감', '그 달의 실제 수치를 확정해요. 저장한 값으로만 그 달 소비율을 계산해요.',
    f'<div style="flex-shrink: 0; display: flex; gap: 8px; padding: 10px 12px; background: {C["WARN_SOFT"]}; border-radius: 12px; font-size: 12.5px; line-height: 1.5; color: {C["WARN_INK"]};">'
    f'<span style="flex-shrink: 0; margin-top: 1px;">{icon("warn", 15, C["WARN"], 2)}</span>'
    f'<span>이미 9월 2일에 마감한 달이에요. 다시 저장하면 전에 저장한 값을 덮어써요.</span></div>' +
    group('그 달의 실제 수치',
          solo(field('월급 + 부수입', '3,900,000', '원'))
          + f'<div style="margin-top: 12px;">{solo(field("그중 월급", "3,600,000", "원"))}'
            f'<div style="margin-top: 6px; font-size: 11.5px; color: {C["INK3"]};">비우면 월급 대비 소비율이 안 나와요</div></div>'
          + f'<div style="margin-top: 12px;">{solo(field("대출상환", "920,000", "원"))}</div>',
          meta='원 단위', fixed=True) +
    UNCAT_LINE +
    group('자동으로 채워진 값',
          f'<div style="padding: 2px 13px; background: {C["INSET"]}; border-radius: 14px;">'
          f'{kv("일반 소비 합계", "1,715,200원")}{kv("월급 대비 소비율", "47.6%")}'
          f'{kv("월말 총자산", "180,400,000원")}{kv("월말 총부채", "89,200,000원", last=True)}</div>', fixed=True),
    sheet_footer('취소', '마감 저장', save_kind='disabled'),
    sticky=f'<div style="padding: 11px 18px 12px; background: {C["INSET"]}; border-top: 1px solid {C["LINE"]}; flex-shrink: 0;">'
           f'{checkbox("이 달의 수입·상환·잔액을 확인했고, 빠진 소비 기록이 없는지 살펴봤어요", False)}</div>',
    scrim_h=40, body_gap=12, body_pb=14, h=H['MonthlyClose']))


# ══════════════ 7. 백업 불러오기 (language-ia-11 · D4 · components/navi/import-review.tsx) ══════════════
def diffrow(label, count, tone, desc, last=False):
    m = {"new": (C["POS"], C["POS_SOFT"]), "dup": (C["TAB_INK"], C["LINE_SOFT"]),
         "conf": (C["WARN"], C["WARN_SOFT"]), "chk": (C["SKY"], C["SKY_SOFT"])}
    col, bg = m[tone]
    return (f'<div style="display: flex; align-items: center; gap: 10px; min-height: 48px; '
            f'{"" if last else "border-bottom: 1px solid " + C["LINE_ROW"] + ";"}">'
            f'<span style="min-width: 34px; height: 24px; border-radius: 7px; background: {bg}; color: {col}; font-size: 12px; '
            f'font-weight: 700; display: flex; align-items: center; justify-content: center; padding: 0 7px;">{count}</span>'
            f'<div style="flex: 1; min-width: 0;"><div style="font-size: 13px; font-weight: 600; color: {C["INK"]};">{label}</div>'
            f'<div style="font-size: 11px; color: {C["INK3"]};">{desc}</div></div>'
            f'{icon("right", 15, C["INK4"], 2)}</div>')

w('ImportReview', sheet(
    '백업 불러오기', 'navi-backup-2026-09-01.json · 저장하기 전에 무엇이 바뀌는지 먼저 봐요.',
    group('적용 방식', segmented(['합치기', '전체 교체'], 0) +
          f'<div style="margin-top: 9px;">{note("「합치기」는 겹치지 않는 기록만 넣어요. 「전체 교체」를 고르면 지금 기록이 모두 사라져요.", "mute")}</div>') +
    group('불러올 항목', f'<div style="padding: 0 13px; background: {C["SURF"]}; border: 1px solid {C["LINE"]}; border-radius: 14px;">'
                          f'{diffrow("새로 추가", 24, "new", "기록 21 · 자산 2 · 목적지 1")}'
                          f'{diffrow("이미 있음 · 건너뜀", 8, "dup", "같은 기록 ID")}'
                          f'{diffrow("값이 다름 · 기존 유지", 2, "conf", "같은 ID의 내용이 다름")}'
                          f'{diffrow("검토 필요", 1, "chk", "비슷한 기존 기록 있음", last=True)}</div>', fixed=True) +
    group('적용 후', f'<div style="display: flex; gap: 8px;">'
                      f'<div style="flex: 1; padding: 12px; background: {C["INSET"]}; border-radius: 13px;">'
                      f'<div style="font-size: 11.5px; color: {C["INK3"]};">지금</div>'
                      f'<div style="font-size: 18px; font-weight: 600; color: {C["INK"]}; margin-top: 3px;">기록 97건</div>'
                      f'<div style="font-size: 11.5px; color: {C["INK3"]}; margin-top: 2px;">순자산 9,350만원</div></div>'
                      f'<div style="display: flex; align-items: center;">{icon("arrowr", 16, C["INK4"], 2.2)}</div>'
                      f'<div style="flex: 1; padding: 12px; background: {C["BRAND_SOFT"]}; border-radius: 13px;">'
                      f'<div style="font-size: 11.5px; color: {C["BRAND"]};">적용 후</div>'
                      f'<div style="font-size: 18px; font-weight: 600; color: {C["INK"]}; margin-top: 3px;">기록 118건</div>'
                      f'<div style="font-size: 11.5px; color: {C["INK3"]}; margin-top: 2px;">순자산 9,850만원</div></div></div>', fixed=True) +
    f'<div style="display: flex; align-items: center; justify-content: space-between; min-height: 40px; flex-shrink: 0;">'
    f'<span style="font-size: 13px; font-weight: 600; color: {C["INK"]};">백업 설정 · 상세 내역 <span style="font-weight: 500; font-size: 12px; color: {C["INK3"]}; margin-left: 6px;">내 데이터</span></span>'
    f'{icon("right", 15, C["INK4"], 2)}</div>'
    f'<div style="font-size: 11.5px; line-height: 1.5; color: {C["INK3"]}; flex-shrink: 0;">불러온 기록의 카테고리 없음 표시도 함께 반영돼요 · 확인 표시는 전체 교체에서만 반영돼요 · 이미 있는 기록은 그대로예요</div>',
    sheet_footer('취소', '이 내용으로 적용'),
    sticky=f'<div style="padding: 12px 18px; background: {C["INSET"]}; border-top: 1px solid {C["LINE"]}; flex-shrink: 0;">'
           f'{checkbox("데이터 종류와 적용 후 내역을 확인했어요.", True)}</div>', scrim_h=40, body_gap=13, h=H['ImportReview']))


# ══════════════ 8. 코칭 (home-11 · D6 · D13 · lib/navi-insights.ts — 시안 사용자의 엔진 목록 · NUMBERS §12) ══════════════
def advice(tone, title, body, action, num):
    m = {"neg": (C["NEG"], C["NEG_SOFT"]), "warn": (C["WARN"], C["WARN_SOFT"]), "pos": (C["POS"], C["POS_SOFT"]),
         "info": (C["SKY"], C["SKY_SOFT"])}
    col, bg = m[tone]
    # 앱 .coach-priority-item — 제목 14 / 600 줄 21 · 본문 12.5 / 18.75 · 이동 글자 8 아래 줄 19(2026-09-27 fix-up 5 · 예전 제목 줄 1.4 · 이동 6 아래)
    act = f'<div style="font-size: 12.5px; font-weight: 600; line-height: 19px; color: {C["BRAND"]}; margin-top: 8px;">{action} &rsaquo;</div>' if action else ''
    return (f'<div style="display: flex; gap: 11px; padding: 13px; border-radius: 14px; background: {C["SURF"]}; '
            f'border: 1px solid {C["LINE"]}; border-left: 3px solid {col};">'
            f'<span style="width: 22px; height: 22px; border-radius: 99px; background: {bg}; color: {col}; font-size: 11.5px; '
            f'font-weight: 700; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">{num}</span>'
            f'<div style="min-width: 0;"><div style="font-size: 14px; font-weight: 600; letter-spacing: -0.015em; line-height: 21px; color: {C["INK"]};">{title}</div>'
            f'<div style="font-size: 12.5px; line-height: 18.75px; color: {C["INK2"]}; margin-top: 4px;">{body}</div>{act}</div></div>')


def cut_tile(label, value):
    # 앱 .coach-saving-tile — 안쪽 10 11 · 이름 11.5 · 값 15 / 600 2 아래(2026-09-27 fix-up 5 · 예전 9 11 · 14.5 / 700 · 3)
    return (f'<div style="flex: 1; min-width: 0; padding: 10px 11px; background: {C["SURF"]}; border-radius: 11px;">'
            f'<div style="font-size: 11.5px; color: {C["INK3"]};">{label}</div>'
            f'<div style="font-size: 15px; font-weight: 600; color: {C["VIO_STRONG"]}; margin-top: 2px;">{value}</div></div>')


w('CoachPanel', sheet(
    '코칭', '저장된 기록을 보고 중요한 순서로 알려 드려요.',
    f'<div style="display: flex; flex-direction: column; gap: 9px; flex-shrink: 0;">'
    f'{advice("warn", "주거/관리가 소비의 42%예요", "이번 달 47만원.", "주거/관리 기록 보기", 1)}'
    f'{advice("warn", "고정비가 소비의 63%예요", "매달 71만원이 저절로 나가요. 고정비는 한 번 줄이면 매달 아껴지니 통신 · 구독 · 보험부터 살펴보세요.", None, 2)}'
    f'{advice("warn", "카드 할부 금리 14.5%가 투자 자산 기본 수익률 연 5.0%보다 높아요", "이 부채를 갚는 쪽이 투자보다 확실히 유리해요. 100만원을 갚으면 1년에 10만원 이득이에요.", "상환 계획", 3)}</div>'
    f'{foldrow("다른 안내 7개 더 보기", "낮은 순서")}'
    + group('카테고리 절감 가정',
            f'<div style="padding: 13px; background: {C["VIO_SOFT"]}; border-radius: 14px; border: 1px dashed {C["VIO_LINE"]};">'      # 앱 .coach-saving-card 안쪽 13(예전 11 13)
            f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px;">'
            f'{badge("저장되지 않는 가정", "vio", "spark")}'
            f'<span style="font-size: 12.5px; font-weight: 600; color: {C["VIO_STRONG"]};">−10%</span></div>'
            f'<div style="margin-top: 10px;">{slider(25, C["VIO"])}</div>'
            f'<div style="display: flex; align-items: center; margin-top: 4px;">'
            f'<span style="flex: 1; font-size: 11px; color: {C["INK4"]};">0%</span>'
            f'<span style="font-size: 11.5px; font-weight: 600; color: {C["VIO_STRONG"]}; white-space: nowrap;">카테고리별 −10% 가정</span>'
            f'<span style="flex: 1; text-align: right; font-size: 11px; color: {C["INK4"]};">40%</span></div>'
            f'<div style="display: flex; gap: 8px; margin-top: 11px;">'
            f'{cut_tile("식비 · 월 2.4만원", "약 0.2개월 빨리 도착")}{cut_tile("교통 · 월 7,000원", "1년이면 8.4만원")}</div></div>'
            # 접힌 「계산 기준」 = 앱 details.coach-saving-details — 8 아래 높이 44 · 11.5 / 500 #4E2496(2026-09-27 fix-up 5 · 예전 11 아래 12.5 / 600)
            f'<div style="display: flex; align-items: center; justify-content: space-between; height: 44px; margin-top: 8px; font-size: 11.5px; font-weight: 500; color: #4E2496;">'
            f'<span>계산 기준 · 다른 카테고리 4개</span>{icon("down", 14, "#4E2496", 2)}</div>', mb=9),
    btn('닫기', 'secondary', h=48), scrim_h=40, body_gap=15, body_pb=14, h=H['CoachPanel']), keep_all=True)      # 본문 간격 15 · 제목 아래 9 = 앱 .coach-sheet-body


# ══════════════ 9. 알림 (home-10 · D14 · lib/navi-alert-rows.ts — 시안 사용자는 중요 1줄 · NUMBERS §12) ══════════════
def alert(tone, ic, title, body, action, muted=False):
    m = {"neg": (C["NEG"], C["NEG_SOFT"]), "warn": (C["WARN"], C["WARN_SOFT"]),
         "sky": (C["SKY"], C["SKY_SOFT"]), "pos": (C["POS"], C["POS_SOFT"]), "mute": (C["INK3"], C["INSET"])}
    col, bg = m[tone]
    a = f'<div style="font-size: 12.5px; font-weight: 600; color: {C["BRAND"]}; margin-top: 7px;">{action} &rsaquo;</div>' if action else ''
    return (f'<div style="display: flex; gap: 11px; min-height: 60px; padding: 13px 0; border-bottom: 1px solid {C["LINE_ROW"]};">'
            f'<div style="width: 32px; height: 32px; border-radius: 10px; background: {bg}; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">{icon(ic, 16, col, 2)}</div>'
            f'<div style="min-width: 0;"><div style="font-size: 13.5px; font-weight: 600; color: {C["INK"]};">{title}</div>'
            f'<div style="font-size: 12px; line-height: 1.5; color: {C["INK3"]}; margin-top: 3px;">{body}</div>{a}</div></div>')


def alert_group(label, n):
    """앱 .coach-section-heading — 11 / 600 · 줄 17 · 위 4 · 아래 9(2026-09-27 fix-up 4 · 예전 위 2 · 아래 0이라 첫 알림이 8px 위에 붙었다)."""
    return (f'<div style="font-size: 11px; font-weight: 600; line-height: 17px; letter-spacing: 0.04em; color: {C["INK3"]}; margin: 4px 0 9px;">{label} {n}</div>')


ALERTS_DESC = '저장된 기록을 기준으로 만든 알림이에요. 읽어도 기록은 바뀌지 않아요.'
STALE_NOTE = note("자산의 잔액 확인일이 없거나 35일 넘게 갱신하지 않으면 여기에 알려 드려요. 지금은 갱신이 필요한 자산이 없어요.", "mute")

w('AlertsPanel', sheet(
    '알림 1건', ALERTS_DESC,
    f'<div style="display: flex; flex-direction: column;">'
    f'{alert_group("중요", 1)}'
    f'{alert("neg", "bank", "카드 할부 금리가 14.5%예요", "보유 부채 중 가장 높아요. 투자 수익보다 갚는 쪽이 확실해요.", "상환 계획")}</div>'
    f'{STALE_NOTE}',
    btn('닫기', 'secondary', h=48), scrim_h=40))

w('AlertsEmpty', sheet(
    '알림 0건', ALERTS_DESC,
    f'<div style="display: flex; flex-direction: column; align-items: center; text-align: center; padding: 20px 10px; '
    f'background: {C["INSET"]}; border-radius: 14px;">'
    f'<div style="width: 40px; height: 40px; border-radius: 13px; background: {C["POS_SOFT"]}; display: flex; align-items: center; justify-content: center;">{icon("check", 20, C["POS"], 2.4)}</div>'
    f'<div style="font-size: 13.5px; font-weight: 600; color: {C["INK"]}; margin-top: 10px;">확인할 알림이 없어요</div>'
    f'<div style="font-size: 12px; color: {C["INK3"]}; margin-top: 4px;">기록이 바뀌면 필요한 내용을 이곳에 알려 드려요.</div></div>'
    f'{STALE_NOTE}',
    btn('닫기', 'secondary', h=48), scrim_h=40))


# 참고 알림이 있는 날(2026-09-27 fix-up 3 · 앱 하네스) — 시안 사용자에서 ETF 계좌 마지막 확인 7월 30일 · 청약저축 확인 기록 없음(자산 › 자산 구성 AssetsStale 과 같은 날).
# 중요 1(카드 할부) + 참고 1(하늘색 정보 아이콘 「자산 잔액을 확인해 주세요」 · 누르면 잔액 한 번에 확인) · 아래 안내는 첫 문장만(갱신할 자산이 있으니까).
w('AlertsPanelInfo', sheet(
    '알림 2건', ALERTS_DESC,
    f'<div style="display: flex; flex-direction: column;">'
    f'{alert_group("중요", 1)}'
    f'{alert("neg", "bank", "카드 할부 금리가 14.5%예요", "보유 부채 중 가장 높아요. 투자 수익보다 갚는 쪽이 확실해요.", "상환 계획")}'
    f'<div style="height: 31px;"></div>{alert_group("참고", 1)}'
    f'{alert("sky", "info", "자산 잔액을 확인해 주세요", "자산 2개의 잔액 확인일이 없거나 35일이 지났어요.", "자산 잔액")}</div>'
    + note("자산의 잔액 확인일이 없거나 35일 넘게 갱신하지 않으면 여기에 알려 드려요.", "mute"),
    btn('닫기', 'secondary', h=48), scrim_h=40))


# ══════════════ 10. 또래 기준 등록 (language-ia-11 · D4) ══════════════
w('PeerDialog', sheet(
    '20대 후반 비교 기준', '만 27~29세 구간에 쓸 기준을 직접 등록해요. 앱이 만든 값이 아니에요.',
    note('NAVI에는 세부 연령별 통계가 <span style="font-weight:600">들어 있지 않아요.</span> 여기 넣은 값은 화면에서 항상 “내가 등록한 기준”으로 표시되고, 순위나 상위 %로 바뀌지 않아요.', 'warn', 'warn') +
    f'<div style="display: flex; gap: 10px;">{field("나이대", "20대 후반 · 만 27~29세", state="readonly")}</div>'
    f'<div style="display: flex; gap: 10px;">{field("평균 소비율", "62", "%", required=True)}{field("조사 인원", "1200", "명", w=132)}</div>'
    f'<div style="display: flex; gap: 10px;">{field("기준 연도", "2025", "년", required=True, w=132)}{field("소비율 계산 기준", "월급 (실수령)", state="readonly")}</div>'
    f'<div style="flex: 1; min-height: 0; display: flex; flex-direction: column;">{solo(field("자료 출처", "직접 입력한 예시 기준", required=True, helper="화면에 그대로 표시돼요"))}</div>'
    f'{note("월급(실수령)이 아닌 다른 소득을 기준으로 한 통계라면 내 월말 예상과 바로 비교할 수 없어요. 출처의 기준을 꼭 확인하세요.", "mute")}',
    sheet_footer('취소', '기준 저장'), scrim_h=40, body_pb=0,
    header_right=del_x('기준 삭제')))


# ══════════════ 11. 확인 창 모음 (a11y-17 · assets-1 · record-1 · record-6 · goals-2 · D4 · D8 · D9) ══════════════
# 앱 AlertDialog(c6b7de3 하네스 · 자산 삭제 · 원 단위 확인): 왼쪽 아이콘 칸 없음 · 안쪽 16 · 제목 16 / 500 / 24 · 본문 14 / 20 ink-3(제목 6 아래) · 가운데 ·
# 아래는 옅은 띠(안쪽 16 · 1px 윗선) · 버튼은 전체 폭 세로(사이 8 · 높이 32 · 안쪽 0 10 · 모서리 13 · 16 / 400 — 누르는 영역 44 는 보이지 않는 가상 요소) · 행동 먼저, 「취소」 아래.
# (2026-09-27 fix-up 5 · 예전 버튼 40 · 14 / 600 · 제목 15.5 / 700 · 본문 12.5)
def dlg_btn(label, kind):
    m = {"danger": (C["NEG_SOFT"], C["NEG"], "1px solid transparent"), "primary": (C["BRAND"], "#FFFFFF", "1px solid transparent"),
         "plain": (C["BG"], C["INK"], f'1px solid {C["LINE"]}'), "focus": (C["BG"], C["INK"], f'2px solid {C["BRAND"]}')}
    bg, fg, bd = m[kind]
    ring = 'box-shadow: 0 0 0 3px rgba(53,86,230,.18);' if kind == 'focus' else ''
    return (f'<div style="display: flex; align-items: center; justify-content: center; height: 32px; padding: 0 10px; border-radius: 13px; background: {bg}; '
            f'border: {bd}; {ring} color: {fg}; font-size: 16px; font-weight: 400;">{label}</div>')


def confirm(title, body, buttons):
    body_html = ''.join(f'<p style="margin: 6px 0 0; font-size: 14px; line-height: 20px; color: {C["INK3"]};">{b}</p>' for b in body)
    return (f'<div style="background: {C["SURF"]}; border: 1px solid {C["LINE"]}; border-radius: 16px; overflow: hidden; flex-shrink: 0; '
            f'box-shadow: 0 1px 2px rgba(16,24,40,.04), 0 8px 24px -16px rgba(16,24,40,.28);">'
            f'<div style="padding: 16px; text-align: center;">'
            f'<div style="font-size: 16px; font-weight: 500; line-height: 24px; color: {C["INK"]};">{title}</div>{body_html}</div>'
            f'<div style="display: flex; flex-direction: column; gap: 8px; padding: 16px; background: #F8FAFD; border-top: 1px solid {C["LINE"]};">'
            + ''.join(dlg_btn(l, k) for l, k in buttons) + '</div></div>')


CONFIRM_BLOCKS = [
    ('A · 자산 삭제',
     confirm('ETF 계좌를 삭제할까요?', ['삭제하면 순자산과 미래 예측이 바로 다시 계산돼요. 지난 기록은 그대로 남아요.'],
             [('삭제', 'danger'), ('취소', 'plain')])),
    ('B · 기록 지우기 — 반복 기록이 만든 건',
     confirm('이 기록을 지울까요?', ['9월 6일 ETF 자동이체 300,000원 · 이번 달에 만들어진 이 건만 지워요 · 같은 달에 다시 생기지 않고 반복 기록은 그대로예요',
                                  '연결 계좌의 잔액을 이미 확정해서 지금 잔액은 바뀌지 않아요'],      # 캐논 9월 6일 연결은 확정됨(design-state transactionLinks settled · 앱 하네스 · 2026-09-27 fix-up 2)
             [('지우기', 'danger'), ('취소', 'plain')])),
    ('B′ · 기록 지우기 — 보통 기록',
     confirm('이 기록을 지울까요?', ['9월 8일 점심 9,000원 · 지우면 9월 소비율과 한도가 다시 계산돼요'],
             [('지우기', 'danger'), ('취소', 'plain')])),
    ('C · 목적지 삭제',
     confirm('비상금 6개월 목적지를 삭제할까요?', ['목적지를 지우면 매달 필요한 돈을 다시 계산해요.',
                                            '지금 모은 돈 1,020만원은 이 목적지에 적어 둔 숫자라 함께 지워져요. 자산 탭의 잔액은 그대로예요.'],
             [('삭제', 'danger'), ('취소', 'plain')])),
    ('D · 반복 기록 지우기',
     confirm('ETF 자동이체 반복 기록을 지울까요?', ['앞으로 자동 기록이 생기지 않아요. 이미 만들어진 지난 기록은 그대로 남아요.'],
             [('지우기', 'danger'), ('취소', 'plain')])),
    ('E · 모든 데이터 지우기',
     confirm('모든 데이터를 지울까요?', ['이 기기에 저장된 자산 · 기록 · 목적지가 모두 지워져요. 필요하면 먼저 백업을 내보내 주세요.'],
             [('모든 데이터 지우기', 'danger'), ('취소', 'plain')])),
    ('F · 원 단위로 적으셨나요? — 만원 칸에 원 단위 숫자',
     confirm('원 단위로 적으셨나요?', ['지금 금액 5,000,000만원은 500억원이에요. 5,000,000원이라면 500만원으로 저장할게요.'],
             [('500만원으로 바꿔 저장', 'primary'), ('500억원 그대로 저장', 'plain'), ('다시 고치기', 'plain')])),
    ('G · 마감한 달의 합계 고치기',
     confirm('8월 소비 합계만 새 금액으로 고칠게요', ['마감 때 1,715,200원 → 지금 기록 1,770,200원 · 수입 · 상환 · 자산 값은 그대로 둬요'],
             [('합계 고치기', 'primary'), ('취소', 'plain')])),
]

w('Confirmations', state_sheet(
    '삭제 · 초기화 · 확인 창',
    '지우거나 바꾸기 전에 한 번 더 묻는 창 일곱 가지입니다. 웹에서는 E의 「이 기기에」가 「이 브라우저에」로 바뀝니다.',
    CONFIRM_BLOCKS, h=H['Confirmations'], pill='구현 참고 · 앱 화면이 아닙니다'), keep_all=True)


# ══════════════ 12. 구현 참고 장 틀 — gen_v5.spec_frame 과 같은 모양 ══════════════
# gen_v5 를 import 하면 v4 · v5 장 전체를 다시 쓰는 부작용이 있어, 승인된 틀(알약 · 제목 · 부제 · 번호 mark · 번호별 설명 줄)만 같은 값으로 옮겨 둔다.
def spec_frame(w_, h_, title, sub, body, sub_w=640):
    chip = (f'<span style="align-self: flex-start; font-size: 11px; font-weight: 600; letter-spacing: 0.02em; color: {C["INK2"]}; '
            f'border: 1px solid {C["LINE"]}; background: {C["SURF"]}; border-radius: 99px; padding: 4px 10px; white-space: nowrap;">구현 참고 · 앱 화면이 아닙니다</span>')
    return (f'<div style="width: {w_}px; height: {h_}px; background: {C["BG"]}; color: {C["INK"]}; padding: 28px 30px 30px; display: flex; '
            f'flex-direction: column; gap: 10px; overflow: hidden; font-variant-numeric: tabular-nums;">{chip}'
            f'<h2 style="margin: 2px 0 0; font-size: 20px; font-weight: 700; letter-spacing: -0.025em; color: {C["INK"]};">{title}</h2>'
            f'<p style="margin: 0 0 8px; font-size: 13px; line-height: 1.55; color: {C["INK3"]}; max-width: {sub_w}px;">{sub}</p>{body}</div>')


def mark(n, pos='flex-shrink: 0; margin-top: 1px;'):
    return (f'<span style="{pos} width: 17px; height: 17px; border-radius: 99px; background: {C["INK"]}; color: #FFFFFF; '
            f'font-size: 10.5px; font-weight: 700; display: inline-flex; align-items: center; justify-content: center; '
            f'box-shadow: 0 0 0 2px {C["SURF"]};">{n}</span>')


def guide_row(n, name, meaning, second, last=False):
    border = '' if last else f'border-bottom: 1px solid {C["LINE_ROW"]};'
    lead = mark(n) if n is not None else '<span style="width: 17px; flex-shrink: 0;"></span>'      # n=None: 번호 없는 딸린 줄(들여쓰기만)
    return (f'<div style="display: flex; gap: 11px; padding: 10px 0; {border}">{lead}'
            f'<div style="display: flex; flex-direction: column; gap: 2px; min-width: 0;">'
            f'<div style="font-size: 13.5px; line-height: 1.4; color: {C["INK2"]};"><b style="font-weight: 600; color: {C["INK"]};">{name}</b>&nbsp;&nbsp;{meaning}</div>'
            f'<div style="font-size: 12px; line-height: 1.45; color: {C["INK3"]};">{second}</div></div></div>')


def case_cap(n, title, desc):
    return (f'<div><div style="display: flex; align-items: center; gap: 7px;">{mark(n, pos="flex-shrink: 0;")}'
            f'<span style="font-size: 14px; font-weight: 700; letter-spacing: -0.01em; color: {C["INK"]};">{title}</span></div>'
            f'<div style="font-size: 12px; line-height: 1.5; color: {C["INK3"]}; margin-top: 3px;">{desc}</div></div>')


# ══════════════ 13. 기록 추가 — 하루 시트에서 넘어온 초안 (TransactionAddFromDaySheet) ══════════════
# plan/v5-calendar.md §4-2 · §9-5 · record-7 · record-13: 하루 시트의 `저축·투자로 기록 ›`가 그 종류를 미리 고르고 날짜 · 금액 · 메모를 채운 채
# 자세한 `기록 추가` 창을 연다(앱 components/navi/transaction-form — 2026-09-25 캡처와 같은 모양). 손으로 쓴 TransactionAdd.dc.html 을 읽어 값만 바꾼다(그 파일은 고치지 않는다).
def _swap(src, old, new, count=1):
    assert src.count(old) == count, (old[:60], src.count(old))
    return src.replace(old, new)


def tx_add_from_day_sheet():
    src = (OUT / 'TransactionAdd.dc.html').read_text(encoding='utf-8')
    start = src.index('  <div style="flex: 1; min-height: 0; background: #FFFFFF; border-radius: 26px 26px 0 0;')
    end = src.index('</x-dc>')
    sheet_html = src[start:end].rstrip()
    assert sheet_html.endswith('</div>')
    sheet_html = sheet_html[:-len('</div>')].rstrip()            # 바깥 390 × 844 틀의 닫는 태그는 뺀다
    # 폰 틀 없이 창만 — 높이는 내용만큼(가운데 본문의 flex: 1 을 푼다)
    sheet_html = _swap(sheet_html, 'flex: 1; min-height: 0; background: #FFFFFF; border-radius: 26px 26px 0 0;',
                       f'background: #FFFFFF; border: 1px solid {C["LINE"]}; border-radius: 26px 26px 18px 18px;')
    sheet_html = _swap(sheet_html, 'flex: 1; min-height: 0; overflow: hidden; padding: 14px 18px 0;', 'padding: 14px 18px 14px;')
    m = lambda n: mark(n, pos='margin-left: 6px; vertical-align: -3px; flex-shrink: 0;')       # 버튼 안(이미 flex 가운데 맞춤)

    # 라벨 옆 번호: 17px inline-flex 배지를 글줄에 그대로 넣으면 그 라벨 줄만 18 → 21px 로 커진다.
    # 라벨을 flex 가운데 맞춤으로 바꾸고 배지의 위아래 margin 을 -2px 로 눌러(차지하는 높이 13px < 글줄 18px) 줄 높이는 글자가 정하게 한다.
    # 원래 글자는 <span> 하나로 감싼다 — flex 안에서 `메모 ` 뒤 빈칸이 사라지지 않게.
    def label_mark(html, inner, n):
        old = f'margin-bottom: 7px;">{inner}</div>'
        new = (f'margin-bottom: 7px; display: flex; align-items: center;"><span>{inner}</span>'
               f'{mark(n, pos="margin: -2px 0 -2px 6px; flex-shrink: 0;")}</div>')
        return _swap(html, old, new)
    # ① 기록 종류 — 저축·투자가 미리 선택됨
    on = 'background: #FFFFFF; display: flex; align-items: center; justify-content: center; font-size: 13px; font-weight: 600; color: #101828; box-shadow: 0 1px 2px rgba(16,24,40,.08);">'
    off = 'display: flex; align-items: center; justify-content: center; font-size: 13px; font-weight: 500; color: #5B6880;">'
    sheet_html = _swap(sheet_html, on + '소비<', off + '소비<')
    sheet_html = _swap(sheet_html, off + '저축·투자', on + '저축·투자')
    sheet_html = label_mark(sheet_html, '기록 종류', 1)
    # ② 날짜 9월 8일 · 금액 12,000
    assert sheet_html.count('2026. 09. 08.') == 1
    sheet_html = label_mark(sheet_html, '날짜', 2)
    sheet_html = _swap(sheet_html, '>32,000</span>', '>12,000</span>')
    # 카테고리 — 저축·투자는 종류가 곧 카테고리라 고르는 칩 대신 읽기 전용 줄(상자 · 자물쇠 없음 · 앱과 같게)
    c0 = sheet_html.index('<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 8px;">')
    c0 = sheet_html.rindex('<div>', 0, c0)
    c1 = sheet_html.index('전체 &rsaquo;</div>', c0) + len('전체 &rsaquo;</div>')
    c1 = sheet_html.index('</div>', c1) + len('</div>')      # 칩 줄
    c1 = sheet_html.index('</div>', c1) + len('</div>')      # 카테고리 묶음
    readonly = (f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 12px; padding: 6px 0;">'
                f'<span style="font-size: 13px; color: {C["INK2"]};">카테고리</span>'
                f'<div style="text-align: right;"><div style="font-size: 15px; font-weight: 700; color: {C["INK"]};">저축·투자</div>'
                f'<div style="font-size: 11.5px; color: {C["INK3"]}; margin-top: 3px;">소비율에 안 들어가요</div></div></div>')
    sheet_html = sheet_html[:c0] + readonly + sheet_html[c1:]
    # ③ 메모
    sheet_html = _swap(sheet_html, '점심 · 팀 회식', '적금 추가 납입')
    sheet_html = label_mark(sheet_html, '메모 <span style="font-weight: 500; color: #697182;">선택 사항</span>', 3)
    # 잔액 반영 — 하루 시트는 계좌를 넘기지 않으므로 꺼진 채, 계좌 고르는 줄은 없다. 저축·투자 설명은 출금 · 입금 두 계좌
    sheet_html = _swap(sheet_html, '선택한 계좌의 잔액이 함께 줄어들어요', '선택한 출금·입금 계좌에 함께 반영해요')
    sheet_html = _swap(sheet_html, 'background: #3556E6; padding: 3px; display: flex; justify-content: flex-end; flex-shrink: 0;">',
                       f'background: {C["LINE"]}; padding: 3px; display: flex; justify-content: flex-start; flex-shrink: 0;">')
    a0 = sheet_html.index('<div style="display: flex; align-items: center; justify-content: space-between; gap: 10px; height: 44px; margin-top: 10px;')
    a1 = sheet_html.index('</svg>', a0)
    a1 = sheet_html.index('</div>', a1) + len('</div>')
    a1 = sheet_html.index('</div>', a1) + len('</div>')
    sheet_html = sheet_html[:a0].rstrip() + '\n' + sheet_html[a1:]
    # 맨 아래 안내 — 창에 1px 테두리가 생겨 안쪽 폭이 2px 줄면서 `저축` / `·투자와…`로 꺾였다. 한 용어는 한 줄에 묶는다(원본 파일은 그대로)
    sheet_html = _swap(sheet_html, '저축·투자와 대출상환은', '<span style="white-space: nowrap;">저축·투자와</span> 대출상환은')
    # ④ 저장
    sheet_html = _swap(sheet_html, 'font-weight: 600; color: #FFFFFF;">저장</div>',
                       f'font-weight: 600; color: #FFFFFF;">저장{m(4)}</div>')
    return sheet_html


TXADD_H = 908   # 루트 높이 — gen_canvas WIDE · screens.json 과 같게


TXADD_GUIDE = [
    (1, '기록 종류', '<b style="font-weight: 600;">저축·투자</b>가 미리 선택된 채 열립니다.',
     '하루 시트의 <b style="font-weight: 600;">저축·투자로 기록 &rsaquo;</b>를 눌렀을 때입니다. <b style="font-weight: 600;">대출상환으로 기록 &rsaquo;</b>를 눌렀으면 대출상환이 선택됩니다. '
     '저축·투자는 종류가 곧 카테고리라 「카테고리」는 고르는 칸 없이 줄 하나로 보여 줍니다.'),
    (2, '날짜 · 금액', '하루 시트에 적어 둔 값 그대로 채워집니다.', '9월 8일 시트에서 12,000원을 적고 넘어온 그림입니다. 여기서 고칠 수 있습니다.'),
    (3, '메모', '하루 시트에 적은 메모도 함께 넘어옵니다.', '칸 순서는 기록 추가 창과 같습니다(기록 종류 → 날짜 → 금액 → 카테고리 → 메모 → 잔액 반영). 순서를 바꾸지 않습니다.'),
    (4, '저장', '저장하면 <b style="font-weight: 600;">홈으로 돌아와 완료 카드</b>가 뜹니다 — 「9월 8일 · 적금 추가 납입 · 저축·투자 12,000원 저장 · 저축·투자라 소비율에는 안 들어가요」.',
     '「오늘 N건」 줄과 셋째 줄은 없습니다. 저장에 성공하면 출발한 하루 시트의 9월 8일 초안을 비웁니다. 취소하거나 저장에 실패하면 초안은 남습니다.'),
]


def flow_step(text, strong=False):
    return (f'<span style="display: inline-flex; align-items: center; height: 32px; padding: 0 12px; border-radius: 10px; white-space: nowrap; flex-shrink: 0; '
            f'font-size: 12.5px; font-weight: 600; ' +
            (f'background: {C["BRAND_SOFT"]}; color: {C["BRAND"]};' if strong else f'background: {C["INSET"]}; color: {C["INK2"]};') + f'">{text}</span>')


_arrow = icon("arrowr", 14, C["INK4"], 2.2)
txadd_flow = card(
    f'<div style="font-size: 12px; font-weight: 700; color: {C["INK"]};">어디서 와서 어디로 가나</div>'
    f'<div style="display: flex; align-items: center; flex-wrap: wrap; gap: 6px; margin-top: 9px;">'
    + flow_step('홈 · 하루 시트') + _arrow
    + flow_step('저축·투자로 기록 &rsaquo;') + _arrow
    + flow_step('기록 추가', strong=True) + _arrow
    + flow_step('저장') + _arrow
    + flow_step('홈 · 완료 카드') + '</div>'
    f'<p style="margin: 10px 0 0; font-size: 12px; line-height: 1.55; color: {C["INK3"]};">하루 시트에는 기록 종류 · 잔액 반영 · 계좌 선택이 없어서, 저축·투자와 대출상환은 이 창에서 남깁니다. '
    f'소비율에는 들어가지 않습니다. 수입 · 환불은 어디에서도 안내하지 않습니다.</p>'
    f'<div style="font-size: 12px; font-weight: 700; color: {C["INK"]}; margin-top: 14px;">다른 입구 — 이미 적은 이체를 고칠 때</div>'
    f'<div style="display: flex; align-items: center; flex-wrap: wrap; gap: 6px; margin-top: 9px;">'
    + flow_step('하루 시트 · 이체 줄 &rsaquo;') + _arrow
    + flow_step('기록 수정', strong=True) + _arrow
    + flow_step('저장') + _arrow
    + flow_step('홈 · 「고쳤어요」') + '</div>'
    f'<p style="margin: 10px 0 0; font-size: 12px; line-height: 1.55; color: {C["INK3"]};">하루 시트 목록의 저축·투자 · 대출상환 줄 오른쪽 &rsaquo;를 누르면 같은 창이 제목 <span style="white-space: nowrap;">「기록 수정」으로</span> 열리고, 기록 종류 · 날짜 · 금액 · 메모가 그대로 채워져 있습니다. '
    f'연결 계좌의 잔액을 이미 확정한 기록(예: 9월 6일 ETF 자동이체)이면 잔액 반영 · 계좌 칸 대신 한 줄 <span style="color: {C["INK2"]};">「연결 계좌의 잔액을 직접 확정한 기록이에요. 이제부터 고치거나 지워도 소비 기록에만 반영하고 지금 잔액은 바꾸지 않아요.」</span>이 보입니다.</p>',
    pad='13px 16px')

txadd_guide = card(''.join(guide_row(*r, last=(i == len(TXADD_GUIDE) - 1)) for i, r in enumerate(TXADD_GUIDE)), pad='4px 16px')

w('TransactionAddFromDaySheet', spec_frame(
    960, TXADD_H, '기록 추가 — 하루 시트에서 넘어왔을 때',
    '하루 시트 아래의 링크 「저축·투자로 기록 ›」를 누르면 자세한 기록 추가 창이 이 모습으로 열립니다. 왼쪽 창의 번호를 오른쪽에서 찾으세요.',
    f'<div style="display: flex; gap: 28px; align-items: flex-start;">'
    f'<div style="width: 390px; flex-shrink: 0;">{tx_add_from_day_sheet()}</div>'
    f'<div style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 12px;">{txadd_guide}{txadd_flow}</div></div>', sub_w=760))


# ══════════════ 14. 자산 · 부채 유형 목록 · 새 부채 · 다 갚은 부채 (AssetDebtTypes · 구현 참고 · assets-6 · assets-7 · assets-14 · assets-23) ══════════════
# 저장하는 유형 키는 그대로 두고 화면 이름만 앱 지도(lib/navi-asset-labels.ts · navi-debt-view.ts)대로 보여 준다(D19).
ASSET_TYPE_ROWS = [('현금성', '입출금 · 예적금 · CMA · 파킹통장', True), ('투자', '주식 · ETF · 펀드 · 코인', False),
                   ('연금', '연금저축 · IRP · 퇴직연금', False), ('부동산', '전세보증금 · 월세보증금 · 집', False),
                   ('기타', '청약 · 보험 해지환급금 · 빌려준 돈', False)]
DEBT_TYPE_ROWS = [('주택담보 · 전세대출', '주택담보대출 · 전세자금대출 · 보금자리론', False), ('신용대출', '직장인 신용대출 · 마이너스통장', True),
                  ('학자금', '학자금대출 · 생활비대출', False), ('카드/리볼빙', '카드 할부 · 리볼빙 · 현금서비스', False),
                  ('자동차 할부 · 기타', '자동차 할부 · 가족·지인에게 빌린 돈', False)]


def type_list(rows, cash_chip=False):
    out = []
    for i, (name, sub, sel) in enumerate(rows):
        chip = (f'<span style="font-size: 10.5px; font-weight: 600; color: {C["POS"]}; background: {C["POS_SOFT"]}; border-radius: 6px; padding: 1px 6px; margin-left: 6px;">비상금에 포함</span>'
                if (cash_chip and i == 0) else '')
        out.append(f'<div style="display: flex; align-items: center; gap: 8px; padding: 10px 12px; border-radius: 10px; {"background: " + C["BRAND_SOFT"] + ";" if sel else ""}">'
                   f'<div style="flex: 1; min-width: 0;"><div style="display: flex; align-items: center; font-size: 13.5px; font-weight: 600; color: {C["INK"]};">{name}{chip}</div>'
                   f'<div style="font-size: 11.5px; color: {C["INK3"]}; margin-top: 2px;">{sub}</div></div>'
                   f'{icon("check", 15, C["BRAND"], 2.4) if sel else ""}</div>')
    return (f'<div style="background: {C["SURF"]}; border: 1px solid {C["LINE"]}; border-radius: 14px; padding: 5px; '
            f'box-shadow: 0 1px 2px rgba(16,24,40,.04), 0 8px 24px -16px rgba(16,24,40,.28);">{"".join(out)}</div>')


def col_cap(text):
    return f'<div style="font-size: 12.5px; font-weight: 700; color: {C["INK"]}; margin-bottom: 8px;">{text}</div>'


def col_note(text):
    return f'<p style="margin: 9px 2px 0; font-size: 12px; line-height: 1.55; color: {C["INK3"]};">{text}</p>'


NEW_DEBT_FORM = (
    f'<div style="background: {C["SURF"]}; border: 1px solid {C["LINE"]}; border-radius: 18px; overflow: hidden;">'
    f'<div style="display: flex; align-items: flex-start; justify-content: space-between; gap: 10px; padding: 14px 16px 12px; border-bottom: 1px solid {C["LINE_SOFT"]};">'
    f'<div><div style="font-size: 16.5px; font-weight: 700; letter-spacing: -0.02em; color: {C["INK"]};">부채 추가</div>'
    f'<div style="font-size: 12px; color: {C["INK3"]}; margin-top: 3px;">금리와 매달 내는 돈으로 다 갚는 달을 계산해요.</div></div>{xbtn()}</div>'
    f'<div style="display: flex; flex-direction: column; gap: 13px; padding: 13px 16px 16px;">'
    + solo(field('부채 이름', '', required=True))
    + pair(select_field('유형', '신용대출'), field('남은 원금', '', '만원', required=True, w=132))
    + pair(field('연 금리', '예: 6.5', '%', required=True, ph=True),
           field('월 최소 상환액', '', '만원', w=132, helper='매달 내는 돈(원금+이자) · 이자만 내면 이자를 적어요'))
    + f'</div><div style="display: flex; gap: 10px; padding: 12px 16px 14px; border-top: 1px solid {C["LINE_SOFT"]};">{sheet_footer("취소", "부채 추가")}</div></div>')

def _nw(t):
    """설명 문장 안에서 한 덩어리로 읽어야 하는 말(「…」 + 조사 · 현금+투자자산)이 줄 끝에서 갈라지지 않게."""
    return f'<span style="white-space: nowrap;">{t}</span>'


PAID_ROW = (
    f'<div style="background: {C["SURF"]}; border: 1px solid {C["LINE"]}; border-radius: 16px; padding: 12px 14px;">'
    f'<div style="font-size: 12px; font-weight: 600; color: {C["INK3"]};">다 갚은 부채 1건</div>'
    f'<div style="display: flex; align-items: center; gap: 10px; margin-top: 10px;">'
    f'<div style="flex: 1; min-width: 0;"><div style="display: flex; align-items: center; gap: 6px; font-size: 13.5px; font-weight: 600; color: {C["INK2"]};">자동차 할부 {badge("다 갚음", "pos")}</div>'
    f'<div style="font-size: 11.5px; color: {C["INK3"]}; margin-top: 3px;">자동차 할부 · 기타 · 월 상환 없음</div></div>'   # 앱 debtTypeLabel(personal) · asset-view.tsx 다 갚은 줄
    f'<div style="text-align: right;"><div style="font-size: 14px; font-weight: 600; color: {C["INK2"]};">0원</div>'
    f'<div style="font-size: 11.5px; color: {C["INK3"]}; margin-top: 2px;">연 5.9%</div></div></div></div>')

ADT_W, ADT_H = 1400, 770   # 자연 746 + 24(2026-09-27 fix-up 5 되읽기 · 도움말 줄 높이 앱과 같게) · 루트 크기 — gen_canvas WIDE · screens.json 과 같게
w('AssetDebtTypes', spec_frame(
    ADT_W, ADT_H, '자산 · 부채 유형 목록 · 새 부채 · 다 갚은 부채',
    '자산 · 부채 창에서 「유형」을 열었을 때의 목록과, 새 부채를 넣는 창의 처음 모습, 다 갚은 부채가 목록 끝에 남는 모습입니다. 저장하는 유형 이름은 그대로이고 화면 이름만 바꿉니다.',
    f'<div style="display: flex; gap: 22px; align-items: flex-start;">'
    f'<div style="width: 290px; flex-shrink: 0;">{col_cap("자산 유형 열기")}{type_list(ASSET_TYPE_ROWS, True)}'
    f'{col_note("유형 아래 한 줄: 현금성 「비상금(생활비 몇 달 치)과 " + _nw("현금+투자자산에") + " 들어가요」 · 투자 「" + _nw("현금+투자자산에") + " 들어가요 · 비상금에는 안 들어가요」 · 그 밖 「비상금과 " + _nw("현금+투자자산에는") + " 안 들어가요」.")}</div>'
    f'<div style="width: 290px; flex-shrink: 0;">{col_cap("부채 유형 열기")}{type_list(DEBT_TYPE_ROWS)}'
    f'{col_note("부채 줄의 부제도 이 이름을 씁니다 — 「주택담보 · 전세대출 · 월 최소 32만원」.")}</div>'
    f'<div style="width: 370px; flex-shrink: 0;">{col_cap("새 부채 — 연 금리는 비어서 시작")}{NEW_DEBT_FORM}'
    f'{col_note("연 금리는 유형 기본값을 자리 글자(예: 6.5)로만 보여 주고 채우지 " + _nw("않습니다(필수 *).") + " 월 최소 상환액을 비우고 저장하면 한 번 더 묻고 버튼이 " + _nw("「그대로 저장」으로") + " 바뀝니다.")}</div>'
    f'<div style="flex: 1; min-width: 0;">{col_cap("다 갚은 부채 — 부채 목록 맨 아래")}{PAID_ROW}'
    f'{col_note("남은 원금을 0으로 저장한 부채는 지우지 않고 「다 갚음」으로 남습니다. 연결된 부채 상환 목적지는 「다 갚았어요」가 됩니다.")}</div></div>',
    sub_w=900))
