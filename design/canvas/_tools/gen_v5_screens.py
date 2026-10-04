# -*- coding: utf-8 -*-
"""v5 · 달력 밖의 화면들 — 2026-09-20 최신화 점검(rank 11 · 12 · 30 · 31)에서 빠져 있던 장 6종과 다크 짝.

  InsufficientElsewhere  구현 참고 · 예상 기준 확인 전에 소비·이번 달 / 한도 / 코치 / 다음 안내 / 또래 / 알림이 어떻게 보이는지(v5-1)
  FutureProvisional      구현 참고 · 미래 · 자산 경로의 `잠정` 표시 제안 + 목표 화면 `도착 예상` 옆 자리(v5-1)
  EtcSubline             구현 참고 · 소비 · 한도의 `기타` 서브라인 `분류 안 함 7건 32,000원` + 코치 `소비 없음 확인 n일`(v5-1 · v5-2)
  LimitCardCases         구현 참고 · 한도 카드 네 사례 + 코치 · 한도 탭의 같은 라벨(v5-3)
  RecurringPrefill       앱 화면 390 × 844 · 반복 거래 다이얼로그 미리 채움(v5-3)
  ImportBackupNotes      구현 참고 · 가져오기 · 백업 안내 문구(v5-3)

손으로 쓴 장(Spending · Limits · PeerStates · Future · Goals)은 .dc.html 에서 잘라 쓰고, 생성기 산물(CoachPanel · CoachEmpty ·
AlertsPanel · RecurringDialog · ImportReview · ProfileDialog)은 한 줄짜리 파일이라 gen_modals · gen_rest 의 조각을 같은 모양으로
여기 옮겨 적었다(그 생성기를 import 하면 그쪽 장을 다시 쓰므로 하지 않는다). 원본 파일은 고치지 않는다.
앱 문구는 plan/v5-calendar.md(9판) 원문 그대로. 원문이 없어 지은 문구 · 모양은 장마다 `# 제안` 주석을 달았다.

    python3 gen_v5_screens.py
"""
import re
import gen_common
from gen_common import *
import gen_v5 as v5                      # (import 부작용: v5 1단계 장을 다시 쓴다 — 멱등)
from gen_v5 import w, spec_frame, mark, case_cap, memo_row, first_guide, limit_forward

OUT = v5.OUT
cut = v5.s1.cut


def src(name):
    return (OUT / f'{name}.dc.html').read_text(encoding='utf-8')


def swap(html, old, new, count=1):
    assert html.count(old) == count, f'×{html.count(old)} (기대 {count}): {old[:70]}'
    return html.replace(old, new)


def balanced(html):
    return html.count('<div') == html.count('</div>')


# ══════════════ 공통 조각 ══════════════
FACT_5K = '기록한 소비 5,000원 · 아직 기록하지 않은 소비는 포함하지 않았어요'       # 계획 §3-4 원문(N = 5,000 — HeroInsufficient 와 같은 사람)
# 문장 틀은 계획 §5-3 원문(`분류 안 함 N건 N원`). 건수 · 금액은 이 장이 9월(이번 달) 화면이라 LedgerV5 · ClassifySheet · 확인할 내용과 같은 9월 값 = 7건 32,000원
# (계획 예시 문장의 `4건`은 일반 예시 — 시안에서는 같은 달의 같은 돈을 같은 건수로 센다).
UNCAT_SUM = 32_000
SUBLINE = f'카테고리 없음 {v5.CLS_COUNT}건 {UNCAT_SUM:,}원'
assert SUBLINE == '카테고리 없음 7건 32,000원'


def chip_lg(text='임시 계산'):
    """`임시 계산` 칩(큰 숫자 옆). 중립 배지: 의미색 없이 회색 바탕 + 잉크. 앱에서는 버튼(누르면 까닭 한 줄)."""
    return (f'<span style="display: inline-flex; align-items: center; background: #F0F2F7; color: {C["TAB_INK"]}; font-size: 11.5px; font-weight: 600; '
            f'border-radius: 99px; padding: 4px 9px; white-space: nowrap; flex-shrink: 0;">{text}</span>')


def chip_sm(text='임시 계산'):
    """`임시 계산` 표시(행 · 카드 제목 옆). 목적지 줄의 유형 꼬리표와 같은 크기의 중립 칩."""
    return (f'<span style="display: inline-block; font-size: 10px; font-weight: 600; color: {C["TAB_INK"]}; background: #F0F2F7; border-radius: 5px; '
            f'padding: 2px 5px; white-space: nowrap; flex-shrink: 0;">{text}</span>')


def imark(n):
    """글줄 안에 끼워 넣는 번호."""
    return mark(n, pos='flex-shrink: 0; margin-left: 4px; vertical-align: 1px;')


def col(width, items, gap=22):
    return f'<div style="width: {width}px; flex-shrink: 0; display: flex; flex-direction: column; gap: {gap}px;">{"".join(items)}</div>'


def case(n, title, desc, pic):
    return f'<div style="display: flex; flex-direction: column; gap: 8px; min-width: 0;">{case_cap(n, title, desc)}{pic}</div>'


def memo_box(rows, tail=None):
    t = (f'<div style="font-size: 12px; line-height: 1.55; color: {C["INK3"]}; padding: 8px 0 4px; border-top: 1px solid {C["LINE_ROW"]};">{tail}</div>' if tail else '')
    return (f'<div style="background: {C["SURF"]}; border: 1px solid {C["LINE"]}; border-radius: 18px; padding: 10px 18px 8px;">'
            f'<div style="font-size: 12px; font-weight: 700; color: {C["INK"]}; padding: 2px 0 4px;">구현 메모</div>'
            + ''.join(memo_row(n, t_, last=(i == len(rows) - 1)) for i, (n, t_) in enumerate(rows)) + t + '</div>')


def code(text):
    return f'&lsquo;<b style="font-weight: 600; color: {C["INK"]};">{text}</b>&rsquo;'


def mini_sheet(title, desc, inner):
    """시트의 머리와 본문 일부 — 코치 · 알림처럼 아래에서 올라오는 창을 카드 폭으로 보여 줄 때."""
    return (f'<div style="background: {C["SURF"]}; border: 1px solid {C["LINE"]}; border-radius: 22px 22px 18px 18px; padding: 14px 14px 12px; display: flex; flex-direction: column; gap: 10px;">'
            f'<div><div style="font-size: 17px; font-weight: 700; letter-spacing: -0.025em; color: {C["INK"]};">{title}</div>'
            f'<div style="font-size: 12px; line-height: 1.45; color: {C["INK3"]}; margin-top: 3px;">{desc}</div></div>{inner}</div>')


# gen_modals.advice 와 같은 모양(행동 링크는 없을 수 있다 · 사실 안내용 sky 톤 추가)
def advice(tone, title, body, action, num):
    m = {"neg": (C["NEG"], C["NEG_SOFT"]), "warn": (C["WARN"], C["WARN_SOFT"]), "pos": (C["POS"], C["POS_SOFT"]), "sky": (C["SKY"], C["SKY_SOFT"])}
    c_, bg = m[tone]
    act = f'<div style="font-size: 12.5px; font-weight: 600; color: {C["BRAND"]}; margin-top: 6px;">{action} &rsaquo;</div>' if action else ''
    return (f'<div style="display: flex; gap: 11px; padding: 13px; border-radius: 14px; background: {C["SURF"]}; '
            f'border: 1px solid {C["LINE"]}; border-left: 3px solid {c_};">'
            f'<span style="width: 22px; height: 22px; border-radius: 99px; background: {bg}; color: {c_}; font-size: 11.5px; '
            f'font-weight: 700; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">{num}</span>'
            f'<div style="min-width: 0;"><div style="font-size: 14px; font-weight: 600; letter-spacing: -0.015em; color: {C["INK"]};">{title}</div>'
            f'<div style="font-size: 12.5px; line-height: 1.5; color: {C["INK2"]}; margin-top: 4px;">{body}</div>{act}</div></div>')


# gen_modals.alert 와 같은 모양
def alert(tone, ic, title, body, action, last=False):
    m = {"neg": (C["NEG"], C["NEG_SOFT"]), "warn": (C["WARN"], C["WARN_SOFT"]), "sky": (C["SKY"], C["SKY_SOFT"])}
    c_, bg = m[tone]
    bb = '' if last else f' border-bottom: 1px solid {C["LINE_ROW"]};'
    return (f'<div style="display: flex; gap: 11px; min-height: 60px; padding: 13px 0;{bb}">'
            f'<div style="width: 32px; height: 32px; border-radius: 10px; background: {bg}; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">{icon(ic, 16, c_, 2)}</div>'
            f'<div style="min-width: 0;"><div style="font-size: 13.5px; font-weight: 600; color: {C["INK"]};">{title}</div>'
            f'<div style="font-size: 12px; line-height: 1.5; color: {C["INK3"]}; margin-top: 3px;">{body}</div>'
            f'<div style="font-size: 12.5px; font-weight: 600; color: {C["BRAND"]}; margin-top: 7px;">{action} &rsaquo;</div></div></div>')


# gen_modals.group 과 같은 모양
def group(label, inner, meta=None, mb=9):
    m = f'<span style="font-size: 11.5px; color: {C["INK3"]};">{meta}</span>' if meta else ''
    return (f'<div><div style="display: flex; align-items: baseline; justify-content: space-between; gap: 8px; margin-bottom: {mb}px;">'
            f'<span style="font-size: 11px; font-weight: 600; letter-spacing: 0.07em; color: {C["INK3"]};">{label}</span>{m}</div>{inner}</div>')


# ══════════════ 잘라 오는 원본 ══════════════
SP = src('Spending')
SP_HEADER = '<div style="display: flex; flex-direction: column; gap: 10px; padding: 14px 16px 12px; flex-shrink: 0;">'
SP_CONTENT = '<div style="flex: 1; min-height: 0; display: flex; flex-direction: column; gap: 10px; padding: 0 14px; overflow: hidden;">'
SP_TOP = '<div style="background: #FFFFFF; border: 1px solid #E3E8F1; border-radius: 20px; padding: 16px 14px 14px;'
CARD18 = '<div style="background: #FFFFFF; border: 1px solid #E3E8F1; border-radius: 18px; padding: 14px; flex-shrink: 0;">'
NAV = '<div style="display: flex; align-items: flex-start; justify-content: space-between; gap: 2px; height: 66px;'
sp_header = cut(SP, SP_HEADER, SP_CONTENT).rstrip()
sp_top = cut(SP, SP_TOP, CARD18).rstrip()
assert balanced(sp_header) and balanced(sp_top) and sp_top.count('>31.1</span>') == 1 and sp_top.count('월급 대비 지금까지 쓴 돈') == 1


def strip_outer_close(html):
    """콘텐츠 컨테이너의 닫는 태그까지 딸려 온 조각에서 마지막 </div> 하나를 뺀다."""
    html = html.rstrip()
    assert html.endswith('</div>')
    return html[:html.rfind('</div>')].rstrip()


sp_cats = strip_outer_close(cut(SP, CARD18, NAV))
assert balanced(sp_cats) and sp_cats.count('카테고리별 소비') == 1

LM = src('Limits')
LM_TOP = '<div style="background: #FFFFFF; border: 1px solid #E3E8F1; border-radius: 20px; padding: 16px; box-shadow'
LM_HOW = '<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px; background: #FFFFFF; border: 1px solid #E3E8F1; border-radius: 14px;'
lm_top = cut(LM, LM_TOP, CARD18).rstrip()
lm_cats = cut(LM, CARD18, LM_HOW).rstrip()
assert balanced(lm_top) and balanced(lm_cats) and lm_cats.count('카테고리 배분') == 1


# ══════════════════════════════════════════════════════════════
# 1. InsufficientElsewhere — 예상 기준 확인 전, 홈 밖의 화면들 (rank 11 · v5-1)
# ══════════════════════════════════════════════════════════════
# HeroInsufficient 와 같은 사람: 9월 5일에 처음 열었고 오늘(8일) 커피 5,000원 한 건. 월급 360만원 · 한도 216만원. 부채와 비상금 목적지는 적어 둠.
# 예상 값(# 제안 · 계산기 미검증 예시): 무이력이라 5,000 ÷ 8일 × 30일 = 18,750원 → 월급의 0.5%.

# ① 소비 · 이번 달 — 머리 + 맨 위 카드. 큰 숫자는 지금까지 쓴 돈 ÷ 월급(5,000 ÷ 3,600,000 = 0.14% → 0.1% · 2026-09-24 — 잠정이 붙지 않는다),
#    월말 배지가 빠지고 그래프의 월말 예상 라벨에만 `잠정`, 그 아래 사실 문구.
# 계획선은 y = 118 − 0.2822 × (x − 12). 글은 선과 겹치지 않게 놓는다 — `5,000원`은 오늘 점선 세로줄 왼쪽 끝 맞춤 x 89 · y 86(x 50~89 에서 선은 y 96 이상이라 글 아래로 지나감 ·
# 2026-09-27 fix-up 2: 오늘 세로줄은 앱처럼 그림 칸 위에서 아래까지 점선 · 오늘 점 후광 없음 · Spending 과 같게).
# 2026-09-26(a11y-13 · D12 · Spending 과 같게): 계획선 글 라벨 없음(범례 줄이 말함) · 축 11px · 값 라벨 12px · 금액에 원 · `월말 예상 2만원 · 임시 계산`
# (NUMBERS §6 18,750원 — 그래프 라벨은 앱 compact() 라 만 단위로 반올림 · 2026-09-27 fix-up 2. 1.9만은 달력 칸 쓰는 법 fmt_sum 이다).
spend_svg = (
    '<svg width="362" height="150" viewBox="0 0 362 150" fill="none" style="display: block; width: 100%; height: 150px;">'
    '<path d="M12 118 L350 22.6" stroke="#B9C3D6" stroke-width="1.4" stroke-dasharray="4 4" stroke-linecap="round"/>'
    '<line x1="93.6" y1="118" x2="93.6" y2="6" stroke="#DCE2EC" stroke-width="1" stroke-dasharray="3 4"/>'      # 오늘 점선 세로줄(앱 · Spending 과 같게 · 2026-09-27 fix-up 2)
    '<path d="M12 118 L81.9 118 L93.6 117.6" stroke="#3556E6" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>'
    '<path d="M93.6 117.6 L350 116.9" stroke="#8FA6F2" stroke-width="2.2" stroke-dasharray="5 4" stroke-linecap="round" stroke-linejoin="round"/>'
    '<circle cx="93.6" cy="117.6" r="4" fill="#3556E6" stroke="#FFFFFF" stroke-width="1"/>'
    '<text x="89" y="86" text-anchor="end" font-size="12" font-weight="600" fill="#101828" stroke="#FFFFFF" stroke-width="4" stroke-linejoin="round" paint-order="stroke">5,000원</text>'
    '<circle cx="350" cy="116.9" r="3.4" fill="#8FA6F2"/>'
    '<text x="350" y="104" text-anchor="end" font-size="12" font-weight="600" fill="#4B6BDE">월말 예상 2만원 · 임시 계산</text>'
    '<line x1="12" y1="118" x2="350" y2="118" stroke="#E3E8F1" stroke-width="1"/>'
    '<text x="12" y="134" text-anchor="start" font-size="11" fill="#697182">1일</text>'
    '<text x="93.6" y="134" text-anchor="middle" font-size="11" font-weight="600" fill="#475467">8일 오늘</text>'
    '<text x="175.2" y="134" text-anchor="middle" font-size="11" fill="#697182">15일</text>'
    '<text x="256.8" y="134" text-anchor="middle" font-size="11" fill="#697182">22일</text>'
    '<text x="350" y="134" text-anchor="end" font-size="11" fill="#697182">30일</text></svg>')
PCT_UNIT = '<span style="font-size: 18px; font-weight: 600; color: #475467;">%</span>'
BADGE_CRUISE = ('<span style="display: inline-flex; align-items: center; gap: 4px; background: #E4F4EA; color: #0F7B47; font-size: 11.5px; font-weight: 600; '
                'border-radius: 99px; padding: 4px 9px;">월말에도 목표 안</span>')
PACE_ROW = '<div style="display: flex; align-items: baseline; justify-content: space-between; gap: 8px; margin-top: 13px; padding: 0 2px;">'
# 소비 탭은 D9 문장을 마감할 달이 있을 때만 붙인다(앱 spending-overview.tsx basisParts · basisLine.action 이 있을 때) — 지난 기록이 하나도 없는 이 사람은 사실 문구뿐
# (홈 히어로의 「9월을 마감하면 10월부터 월말 예상을 보여 드려요」는 홈에만 · 2026-09-27 fix-up 2 하네스).
fact_line = (f'<div style="display: flex; align-items: flex-start; gap: 4px; margin-top: 11px; padding: 0 2px;">'
             f'<span style="font-size: 12.5px; line-height: 1.45; color: {C["INK2"]};">{FACT_5K}</span>{imark(2)}</div>\n\n      ')
spend_first = swap(sp_top, '>31.1</span>', '>0.1</span>')
spend_first = swap(spend_first, PCT_UNIT, PCT_UNIT + f'\n            <span style="margin-left: 2px; align-self: center; display: inline-flex; align-items: center;">{imark(1)}</span>')
spend_first = swap(spend_first, BADGE_CRUISE, '')
spend_first = swap(spend_first, '>누적 112만원</span>', '>누적 5,000원</span>')      # 2026-09-26(DZ2 검토) Spending 그래프 머리 「누적 …」(앱) — 이 장면은 5,000원
spend_first = swap(spend_first, PACE_ROW, fact_line + PACE_ROW)
spend_first = re.sub(r'<svg width="362" height="150".*?</svg>', lambda m_: spend_svg, spend_first, count=1, flags=re.S)
assert '월말에도' not in spend_first and spend_first.count('임시 계산') == 1 and '잠정' not in spend_first and balanced(spend_first)
spend_part = (f'<div style="width: 390px; background: {C["BG"]}; border: 1px solid {C["LINE"]}; border-radius: 24px; overflow: hidden; padding-bottom: 14px;">'
              f'{sp_header}<div style="padding: 0 14px;">{spend_first}</div></div>')

# ② 한도 — 맨 위 카드(Limits 에서 잘라 옴 · 소비 경고 카드까지). 앱: 알약 `자동 ›` · `사용 5,000원 · 0%`(정수) · `오늘 포함 23일 남음 · 하루 93,700원` ·
# 달 중간에 시작해 남은 한도는 초록 대신 기본 글자색 + `9월 5일부터 기록 · 그 전 소비는 빠져 있어요`(tasks-1 · D3) · 참고 줄(ink-3 · D1). 예전 사실 줄은 한도 카드에 없다.
limit_first = swap(lm_top, 'color: #0F7B47;">104만원</span>', f'color: {C["INK"]};">216만원</span>')
limit_first = swap(limit_first, 'inset: 0 48.1% 0 0', 'inset: 0 99.8% 0 0')
limit_first = swap(limit_first, '사용 112만원 · 52%', '사용 5,000원 · 0%')
limit_first = swap(limit_first, '오늘 포함 23일 남음 · 하루 45,220원', '오늘 포함 23일 남음 · 하루 93,700원')      # D3 · NUMBERS §6
INFO_152 = '<div style="font-size: 12px; line-height: 1.45; color: #626D88; margin-top: 7px;">저축 · 상환 계획까지 지키려면 152만원 안에서 쓰면 돼요</div>'
limit_first = swap(limit_first, INFO_152, f'<div style="font-size: 12px; line-height: 1.45; color: #626D88; margin-top: 7px;">9월 5일부터 기록 · 그 전 소비는 빠져 있어요</div>'
                   + INFO_152.replace('margin-top: 7px;', 'margin-top: 3px;'))
assert balanced(limit_first) and '초과 예상' not in limit_first and '#0F7B47;">216만원' not in limit_first

# ③ 코치 — 앱 목록(이 사람 · 9월 8일): 카테고리 비중 · 카드 할부(투자 자산 기본 수익률 비교 · 상환 계획 ›) · 기록한 소비 사실 · `다른 안내 2개 더 보기` + 카테고리 절감 가정.
coach_saving = (f'<div style="border: 1.5px dashed {C["VIO_LINE"]}; background: {C["VIO_SOFT"]}; border-radius: 14px; padding: 11px 12px; display: flex; flex-direction: column; gap: 8px;">'
                f'<div style="display: flex; align-items: center; justify-content: space-between;"><span style="font-size: 11.5px; font-weight: 600; color: {C["VIO_STRONG"]};">저장되지 않는 가정</span>'
                f'<span style="font-size: 12px; font-weight: 700; color: {C["VIO_STRONG"]};">−10%</span></div>'
                f'<div style="position: relative; height: 16px;"><div style="position: absolute; left: 0; right: 0; top: 6px; height: 4px; border-radius: 99px; background: #E4D8FB;"></div>'
                f'<div style="position: absolute; left: 0; width: 25%; top: 6px; height: 4px; border-radius: 99px; background: {C["VIO"]};"></div>'
                f'<span style="position: absolute; left: calc(25% - 8px); top: 0; width: 16px; height: 16px; border-radius: 99px; background: #FFFFFF; border: 2px solid {C["VIO"]};"></span></div>'
                f'<div style="display: flex; align-items: center; margin-top: -4px;"><span style="flex: 1; font-size: 11px; color: {C["INK4"]};">0%</span>'      # 앱 .coach-saving-labels(2026-09-27 fix-up 4)
                f'<span style="font-size: 11.5px; font-weight: 600; color: {C["VIO_STRONG"]}; white-space: nowrap;">카테고리별 −10% 가정</span>'
                f'<span style="flex: 1; text-align: right; font-size: 11px; color: {C["INK4"]};">40%</span></div>'
                f'<div style="background: {C["SURF"]}; border-radius: 10px; padding: 8px 10px;"><div style="font-size: 11px; color: {C["INK3"]};">카페/간식 · 월 500원</div>'
                f'<div style="font-size: 14px; font-weight: 700; color: {C["VIO_STRONG"]}; margin-top: 2px;">1년이면 6,000원</div></div></div>')
SAVING_FOLD = (f'<div style="display: flex; align-items: center; justify-content: space-between; height: 44px; font-size: 11.5px; font-weight: 500; color: #4E2496;">'
               f'계산 기준{icon("down", 14, "#4E2496", 2)}</div>')      # 앱 details.coach-saving-details(접힌 모습 · 2026-09-27 fix-up 4)
coach_first = mini_sheet('코칭', '저장된 기록을 보고 중요한 순서로 알려 드려요.',
                         f'<div style="display: flex; flex-direction: column; gap: 8px;">'
                         + advice('warn', '카페/간식이 소비의 100%예요', '이번 달 5,000원.', '카페/간식 기록 보기', 1)
                         + advice('warn', '카드 할부 금리 14.5%가 투자 자산 기본 수익률 연 5.0%보다 높아요', '이 부채를 갚는 쪽이 투자보다 확실히 유리해요. 100만원을 갚으면 1년에 10만원 이득이에요.', '상환 계획', 2)
                         + advice('sky', '기록한 소비 5,000원', '아직 기록하지 않은 소비는 포함하지 않았어요', None, 3)
                         + f'<div style="display: flex; align-items: center; justify-content: space-between; font-size: 12.5px; font-weight: 600; color: {C["INK"]}; padding: 2px 2px;">'
                           f'다른 안내 2개 더 보기<span style="font-size: 11.5px; font-weight: 500; color: {C["INK3"]};">낮은 순서 ⌄</span></div>'
                         + f'<div style="font-size: 11.5px; font-weight: 600; color: {C["INK2"]}; padding: 2px 2px 0;">카테고리 절감 가정</div>' + coach_saving + SAVING_FOLD + '</div>')

# ⑤ 또래 카드 — PeerStates 의 B 에서 월말 예상으로 판단하는 초록 줄만 `이번 달 기록 · 기록한 소비 5,000원` 한 줄로(앱 · home-13).
PS = src('PeerStates')
i_b = PS.index('B · 나이대 있음')
i_card = PS.index('<div style="background: #FFFFFF; border: 1px solid #E3E8F1; border-radius: 18px; padding: 14px;">', i_b)
i_c = PS.index('<div style="font-size: 11px; font-weight: 600; letter-spacing: 0.06em; color: #606B7D; padding: 6px 2px 0;">C ·', i_card)
peer_b = PS[i_card:i_c].rstrip()
assert balanced(peer_b) and peer_b.count('월말에도 소비 목표 60% 안이에요') == 1      # 2026-09-26(DZ2) PeerStates 소비 목표(D4)
peer_first = re.sub(r'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px; margin-top: 13px; padding: 10px 12px; background: #E4F4EA; border-radius: 12px;">.*?</div>',
                    lambda m_: (f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px; margin-top: 13px; padding: 10px 12px; background: {C["INSET"]}; border-radius: 12px;">'
                                f'<span style="font-size: 12.5px; color: {C["INK2"]}; white-space: nowrap;">이번 달 기록</span>'
                                f'<span style="font-size: 13px; font-weight: 600; color: {C["INK"]}; white-space: nowrap;">기록한 소비 5,000원</span></div>'),
                    peer_b, count=1, flags=re.S)
assert balanced(peer_first) and '월말에도' not in peer_first

# ⑥ 알림 — 예상으로 만든 알림은 목록에도 개수에도 없다. 중요 · 참고로 묶는다(home-10). 이 사람은 중요 1(카드 할부) — 자산은 9월 5일에 넣어 잔액 확인일이 35일 안이라 참고 행이 없다(NUMBERS §0-3).
bell = (f'<div style="display: flex; align-items: center; gap: 8px; padding: 8px 10px; background: {C["INSET"]}; border-radius: 12px;">'
        f'<div style="width: 36px; height: 36px; border-radius: 11px; background: {C["SURF"]}; display: flex; align-items: center; justify-content: center; position: relative; flex-shrink: 0;">'
        f'{icon("bell", 19, C["INK2"], 1.9)}<span style="position: absolute; top: 3px; right: 3px; min-width: 15px; height: 15px; border-radius: 99px; background: {C["NEG"]}; color: #FFFFFF; '
        f'font-size: 10px; font-weight: 700; display: flex; align-items: center; justify-content: center; padding: 0 4px; border: 2px solid {C["SURF"]};">1</span></div>'
        f'<span style="font-size: 12px; line-height: 1.45; color: {C["INK3"]};">머리줄 종의 숫자 = 중요 1</span></div>')
ALERT_GROUP = f'<div style="font-size: 11.5px; font-weight: 600; color: {C["INK3"]}; padding: 6px 0 0;">%s</div>'
alerts_first = mini_sheet('알림 1건', '저장된 기록을 기준으로 만든 알림이에요. 읽어도 기록은 바뀌지 않아요.',
                          f'<div style="display: flex; flex-direction: column;">' + ALERT_GROUP % '중요 1'
                          + alert('neg', 'bank', '카드 할부 금리가 14.5%예요', '보유 부채 중 가장 높아요. 투자 수익보다 갚는 쪽이 확실해요.', '상환 계획', last=True) + '</div>'
                          + note('자산의 잔액 확인일이 없거나 35일 넘게 갱신하지 않으면 여기에 알려 드려요. 지금은 갱신이 필요한 자산이 없어요.', 'mute') + bell)
assert '적자' not in alerts_first

guide_first = v5.first_guide.replace(' flex-shrink: 0;">', '">', 1)
guide_nodebt = v5.guide_missing_day.replace(' flex-shrink: 0;">', '">', 1)
guide_pair = (f'<div style="display: flex; flex-direction: column; gap: 8px;">{guide_first}'
              f'<div style="font-size: 12px; line-height: 1.5; color: {C["INK3"]}; padding: 4px 2px 0;">연 10% 이상 부채가 없으면 — 빠진 날 안내</div>{guide_nodebt}</div>')

ins_memo = memo_box([
    (1, f'소비 · 이번 달 — 큰 숫자는 지금까지 쓴 돈 ÷ 월급(0.1%)이라 기준과 상관없이 그대로입니다. 월말 배지 {code("월말에도 목표 안")} · {code("월말엔 목표 초과")} · {code("월말엔 월급 초과")}가 없고, 그래프의 월말 예상 라벨에만 <span style="white-space: nowrap;">{code("임시 계산")}을</span> 붙입니다. '
        f'이번 달 기록이 0건이면 큰 숫자는 —, 그래프는 {code("9월 기록이 아직 없어요")}와 {code("월말 예상 —")}이고 월말 예상 점선도 없습니다.'),
    (2, f'그 자리에 사실 문구 {code("기록한 소비 N원 · 아직 기록하지 않은 소비는 포함하지 않았어요")}가 옵니다. 마감하지 않은 지난달이 있을 때만 그 아래에 '
        f'{code("월말 예상을 보려면 … 마감해 주세요 · …부터 마감하기 ›")}(한 달이면 {code("8월을 마감하면 월말 예상을 볼 수 있어요 · 8월 마감하기 ›")})가 붙습니다 — 지난 기록이 하나도 없는 이 사람은 사실 문구뿐입니다'
        f'(홈 히어로의 {code("9월을 마감하면 10월부터 월말 예상을 보여 드려요")}는 소비 탭에 없음). 색 · 아이콘으로 좋다 · 나쁘다를 말하지 않습니다.'),
    (3, f'한도 탭 — 알약 {code("자동 ›")} · 남은 일수는 오늘 포함 · 달 중간에 시작한 사람은 남은 한도를 초록 대신 기본 글자색으로 쓰고 {code("9월 5일부터 기록 · 그 전 소비는 빠져 있어요")}를 붙입니다. '
        f'참고 줄 {code("저축 · 상환 계획까지 지키려면 152만원 안에서 쓰면 돼요")}는 회색 12px(판정 아님). 카테고리 줄의 {code("초과 예상")}은 없습니다.'),
    (4, f'코치 — 예상에서 나오는 안내(월말 예상 · 매달 모을 수 있는 돈 · 모든 목적지가 제때 도착해요)가 없습니다. 카테고리 비중 · 고금리 부채처럼 기록에서 나오는 안내와 사실 안내만 남습니다.'),
    (5, f'다음 안내 — 늘 있는 안내가 있으면 그것(카드 할부 금리 · 상환 계획 보기 ›), 없으면 빠진 날 안내 {code("어제 쓴 돈도 적어 볼까요? · 7일 적기 ›")}. 홈(HeroInsufficient)과 같은 카드입니다.'),
    (6, f'또래 카드 — 월말 예상으로 판단하는 {code("월말에도 소비 목표 60% 안이에요")} 줄 대신 {code("이번 달 기록 · 기록한 소비 5,000원")}. 나머지(나이대 · 기준 등록 · 자세히 접힘)는 그대로입니다. '
        f'월급이 있고 이번 달 기록이 0건이면 제목이 {code("이번 달 기록이 아직 없어요")} · 버튼은 {code("소비 기록하기")} 하나입니다(월급 입력을 다시 묻지 않음).'),
    (7, f'알림 — 예상으로 만든 알림은 목록과 개수(제목 · 머리줄 종 배지)에서 모두 빠집니다. 목록은 중요 · 참고로 묶고, 종 배지 = 중요 수(1)입니다.')],
    tail=f'판정은 하나입니다 — 월말 예상 기준(지난달 마감)이 서기 전이면 위 일곱 곳이 전부 이 모양이고, 서면 전부 원래 화면으로 돌아갑니다. 그래서 월말 예상으로 판단하는 {code("월말에도 목표 안")}이 어디에도 없습니다. '
         f'판정은 늘 사용자가 정한 선(소비 목표 · 한도)으로만 합니다. 지금까지 쓴 돈의 비율(홈 · 소비의 큰 숫자)은 사실이라 그대로 보입니다. '
         f'기준이 섰어도 이번 달 기록이 0건이면 코치 · 다음 안내 · 또래 카드는 판정하지 않고 {code("이번 달 기록이 아직 없어요")}라고만 씁니다(판정 = 기준 · 이번 달 기록 1건 이상).')

ins_body = (
    f'<div style="display: flex; gap: 24px; align-items: flex-start;">'
    + col(390, [case(1, '소비 · 이번 달', '큰 숫자는 지금까지 쓴 돈이라 그대로, 배지가 없고 그래프의 월말 예상에 임시 계산이 붙습니다.', spend_part),
                case(5, '다음 안내', '늘 있는 안내가 먼저, 없으면 빠진 날 안내.', guide_pair)])
    + col(362, [case(3, '소비 · 한도', '예상 각주와 초과 예상 표시가 없습니다. 시작한 날 줄이 붙습니다.', limit_first),
                case(4, '코치', '기록에서 나온 안내와 사실 안내만 남습니다.', coach_first)])
    + col(362, [case(6, '또래와 내 페이스', '월말 예상으로 판단하는 줄이 사실 한 줄로 바뀝니다.', peer_first),
                case(7, '알림', '예상으로 만든 알림은 목록에도 개수에도 없습니다.', alerts_first)])
    + '</div>' + ins_memo)
INS_W, INS_H = 1230, 1864      # 2026-09-27 fix-up 4 자연 1840 + 24(④ 코치 절감 가정 눈금 줄 · 계산 기준) ·     # 2026-09-27 fix-up 2 자연 1767 + 24(① D9 줄 뺌 · 메모 2 가 길어짐) · 2026-09-26 자연 1748 + 24(코치 목록 · 절감 가정 · 다음 안내 두 견본 · 한도 시작일 줄)
w('InsufficientElsewhere', spec_frame(
    INS_W, INS_H, '월말 예상 기준이 서기 전 — 홈 밖의 화면들',
    '홈의 이력 부족 상태(HeroInsufficient)와 같은 사람입니다 — 9월 5일에 처음 열었고 오늘 커피 5,000원 한 건을 적었습니다. '
    '지난달을 마감해 월말 예상 기준이 서기 전에는 예상에서 나오는 판단을 어느 화면에서도 하지 않고, 기록한 사실만 말합니다.',
    ins_body, sub_w=860), keep_all=True)


# ══════════════════════════════════════════════════════════════
# 2. FutureProvisional — 미래 · 자산 경로의 `잠정` (rank 12 · v5-1 · v3 내비)
# ══════════════════════════════════════════════════════════════
FU = src('Future')
i0 = FU.index('<div style="width: 390px; height: ')      # 2026-09-26(DZ2) Future 가 본문 높이(1099)로 늘었다
i1 = FU.index('</x-dc>')
future_phone = FU[i0:i1].rstrip()
# 참고 장 안의 그림 — 아래 가정 카드 제목까지 보이게 860 으로 자른다(앱 화면은 스크롤)
future_phone = re.sub(r'width: 390px; height: \d+px;', 'width: 390px; height: 860px;', future_phone, count=1)
assert balanced(future_phone)
EOK = '<span style="font-size: 17px; font-weight: 600; color: #475467;">억원</span>'
MILE = '<span style="font-size: 14px; font-weight: 600; color: #101828;">다음 자산 지점</span>'
SIM = '10년 뒤 +0원</span>'      # 절감 카드 머리(0원 = 보통 카드 · 배지 없음 · 2026-09-27 사용자 결정 3)
CLOSE_LINE = f'8월을 마감하면 확정돼요 · <span style="font-weight: 600; color: {C["BRAND"]}; white-space: nowrap;">8월 마감하기 &rsaquo;</span>'      # D9 앱 문구(칩을 누르면)


def future_with(marks=True):
    m1, m2, m3 = (imark(1), imark(2), imark(3)) if marks else ('', '', '')
    html = swap(future_phone, EOK, EOK + f'\n            <span style="margin-left: 5px; align-self: center; display: inline-flex; align-items: center;">{chip_lg()}{m1}</span>')
    html = swap(html, MILE, MILE + f'\n        <span style="display: inline-flex; align-items: center; margin-left: 2px;">{chip_sm()}{m2}</span>')
    html = swap(html, SIM, SIM + m3)
    return html


future_prov = future_with()
assert future_prov.count('임시 계산') == 2 and '잠정' not in future_prov and balanced(future_prov)
future_left = (f'<div style="width: 392px; flex-shrink: 0; border-radius: 24px; overflow: hidden; border: 1px solid {C["LINE"]};">{future_prov}</div>')

# 표시 모양 — 두 크기
chip_spec = (f'<div style="background: {C["SURF"]}; border: 1px solid {C["LINE"]}; border-radius: 18px; padding: 14px; display: flex; flex-direction: column; gap: 12px;">'
             f'<div style="display: flex; align-items: center; gap: 12px;">{chip_lg()}<span style="font-size: 12px; line-height: 1.5; color: {C["INK2"]};">화면의 큰 숫자 옆 · 11.5px · 회색 바탕 알약 · 누르면 까닭 한 줄</span></div>'
             f'<div style="display: flex; align-items: center; gap: 12px;"><span style="width: 62px; display: inline-flex; justify-content: center; flex-shrink: 0;">{chip_sm()}</span>'
             f'<span style="font-size: 12px; line-height: 1.5; color: {C["INK2"]};">카드 제목 · 목록의 날짜 옆 · 10px</span></div>'
             f'<div style="font-size: 12px; line-height: 1.5; color: {C["INK3"]}; border-top: 1px solid {C["LINE_ROW"]}; padding-top: 10px;">'
             f'초록 · 주황 · 빨강 · 가정 보라를 쓰지 않습니다. 좋다 · 나쁘다가 아니라 아직 지난달을 마감하기 전이라는 뜻이기 때문입니다.</div></div>')


def balanced_at(html, a):
    depth = 0
    for m_ in re.finditer(r'<div\b|</div>', html[a:]):
        depth += 1 if m_.group(0) == '<div' else -1
        if depth == 0:
            return html[a:a + m_.end()]
    raise ValueError


# 목적지 화면 — 8월 마감 전(tasks-5 · D9 · NUMBERS §7 · 앱 캡처 W/tools/dz4/cap_goals_prov.cjs): 맨 위 카드가 `목적지에 매달 필요한 돈 146만원 매달 필요`로 바뀌고
# 매달 모을 수 있는 돈 숫자 · 부족 판단을 숨긴다. 줄은 `매달 N만원 필요` + 도착 예상 옆 칩(목표일 대비 늦음은 말하지 않음). 부채 상환 줄은 상환 계획에서 나오므로 칩 없음.
GO = src('Goals')
GO_CARD = '<div style="background: #FFFFFF; border: 1px solid #E3E8F1; border-radius: 18px; padding: 12px 14px 8px; flex-shrink: 0;">'
assert GO.count(GO_CARD) == 1
goals_card = balanced_at(GO, GO.index(GO_CARD))
for a_, b_ in [('1,020 / 1,500만원 · 매달 70만원', '1,020 / 1,500만원 · <span style="white-space: nowrap;">매달 80만원 필요</span>'),
               ('도착 예상 2027년 4월 · <span style="color: #C0342F;">목표일보다 약 <span style="white-space: nowrap;">1개월</span> 늦어요</span>', f'도착 예상 2027년 4월 {chip_sm()}'),
               ('2,100 / 5,000만원 · 매달 19만원', '2,100 / 5,000만원 · <span style="white-space: nowrap;">매달 66만원 필요</span>'),
               ('도착 예상 2033년 12월 · <span style="color: #C0342F;">목표일보다 약 <span style="white-space: nowrap;">4년 3개월</span> 늦어요</span> · 수익률 연 5.0%', f'도착 예상 2033년 12월 · <span style="white-space: nowrap;">수익률 연 5.0%</span> {chip_sm()}'),
               ('도착 예상 2031년 1월 · 미래 탭 계산', f'도착 예상 2031년 1월 · 미래 탭 계산 {chip_sm()}')]:
    goals_card = swap(goals_card, a_, b_)
assert goals_card.count('임시 계산') == 3 and '다 갚는 달 2030년 11월 · 상환 계획대로</div>' in goals_card and balanced(goals_card)
goals_top = (f'<div style="background: {C["SURF"]}; border: 1px solid {C["LINE"]}; border-radius: 18px; padding: 14px; display: flex; flex-direction: column; gap: 6px;">'
             f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px;"><span style="font-size: 11.5px; font-weight: 600; color: {C["INK3"]};">목적지에 매달 필요한 돈</span>'
             f'<span style="font-size: 12px; font-weight: 600; color: {C["BRAND"]}; white-space: nowrap;">매달 모으는 돈 바꿔 보기 &rsaquo;</span></div>'
             f'<div style="display: flex; align-items: baseline; gap: 6px;"><span style="font-size: 26px; font-weight: 700; letter-spacing: -0.03em; color: {C["INK"]};">146<span style="font-size: 15px; font-weight: 600; color: {C["INK2"]};">만원</span></span>'
             f'<span style="font-size: 12.5px; color: {C["INK2"]};">매달 필요</span></div>'
             f'<span style="font-size: 12px; line-height: 1.45; color: {C["INK3"]};">매달 모을 수 있는 돈은 지난달을 마감한 뒤 계산해요</span>'
             + note('지금은 임시 계산이라 부족하거나 여유가 있다고 판단하지 않아요.', 'mute')
             + f'<span style="font-size: 12px; line-height: 1.45; color: {C["INK3"]};">{CLOSE_LINE}</span></div>')
goals_block = f'<div style="display: flex; flex-direction: column; gap: 10px;">{goals_top}{goals_card}</div>'

# 기준이 선 뒤 — 같은 자리, 표시 없음(Future 원본 그대로의 숫자 줄) · 칩을 누른 모습(까닭 한 줄)
NUM0 = '<div style="display: flex; align-items: flex-end; justify-content: space-between; gap: 10px; margin-top: 14px; padding: 0 2px;">'
NUM1 = '<div style="margin-top: 10px; padding-top: 8px;">\n        <svg width="362"'      # 2026-09-27 fix-up: Future 그래프 칸 158(위 8)
num_block = cut(FU, NUM0, NUM1).rstrip()
assert balanced(num_block)
confirmed_block = (f'<div style="background: {C["SURF"]}; border: 1px solid {C["LINE"]}; border-radius: 18px; padding: 2px 14px 14px;">{num_block}</div>')
tapped_block = (f'<div style="background: {C["SURF"]}; border: 1px solid {C["LINE"]}; border-radius: 18px; padding: 2px 14px 14px;">'
                + swap(num_block, EOK, EOK + f'<span style="margin-left: 5px; align-self: center; display: inline-flex;">{chip_lg()}</span>')
                + f'<div style="font-size: 12px; line-height: 1.45; color: {C["INK3"]}; margin-top: 8px; padding: 0 2px;">{CLOSE_LINE}</div></div>')

fut_memo = memo_box([
    (1, f'{code("10년 뒤 순자산 약 3.82억원")} 옆에 {code("임시 계산")}. 값은 계산한 그대로이고, 흐리게 하거나 {code("—")}로 가리지 않습니다. 칩은 버튼이라 누르면 그 아래에 {code("8월을 마감하면 확정돼요 · 8월 마감하기 ›")}가 한 줄 열립니다(두 달 이상이면 {code("지난 몇 달을 마감하면 확정돼요 · 6월부터 마감하기 ›")}). 각주에는 이유 문장을 붙이지 않습니다.'),
    (2, f'다음 자산 지점은 도착 달 세 줄이 모두 같은 예상에서 나오므로 줄마다 붙이지 않고 카드 제목 옆에 한 번만 붙입니다.'),
    (3, f'절감 카드에는 붙이지 않습니다. 0원이면 보통 카드(실선 · 배지 없음 · {code("10년 뒤 +0원")} 기본 글자색)이고, 0 위로 움직이면 그때만 보라 점선 + {code("저장되지 않는 가정")}이 붙습니다 — 사용자가 넣은 가정은 이미 모양으로 구분됩니다(2026-09-27 결정).'),
    (4, f'목적지 화면 — 맨 위 카드가 {code("목적지에 매달 필요한 돈 146만원 매달 필요")}로 바뀌고 매달 모을 수 있는 돈 숫자와 부족 · 여유 판단을 숨깁니다. 줄은 {code("매달 N만원 필요")}이고 도착 예상 옆에 작은 칩(목표일보다 늦다는 말은 하지 않음). '
        f'부채 상환 목적지의 {code("다 갚는 달")}은 상환 계획에서 나오므로 붙이지 않고, 순자산 목적지는 미래 경로에서 나오므로 붙입니다.'),
    (5, f'8월을 마감하면 칩과 까닭 줄이 함께 사라집니다. 소비 · 이번 달은 그래프의 월말 예상 라벨에 임시 계산을 붙입니다(InsufficientElsewhere 1번 · 큰 숫자는 지금까지 쓴 돈이라 붙이지 않음). 소비 기록이 아직 없는 사람의 목적지는 칩 대신 {code("첫 소비를 기록하면 매달 모을 수 있는 돈을 계산해 드려요 · 오늘 쓴 돈 적기 ›")}입니다.')])

fut_right = (f'<div style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 22px;">'
             f'<div style="display: grid; grid-template-columns: repeat(2, 362px); gap: 22px 20px; align-items: start;">'
             + case(4, '목적지 화면 · 8월 마감 전', '맨 위 카드와 줄마다 도착 예상 옆에 칩이 붙습니다.', goals_block)
             + f'<div style="display: flex; flex-direction: column; gap: 22px;">'
             + f'<div style="display: flex; flex-direction: column; gap: 8px;"><div><div style="font-size: 14px; font-weight: 700; letter-spacing: -0.01em; color: {C["INK"]};">표시 모양</div>'
               f'<div style="font-size: 12px; line-height: 1.5; color: {C["INK3"]}; margin-top: 3px;">크기는 둘, 색은 회색 하나입니다.</div></div>{chip_spec}</div>'
             + case(1, '큰 숫자 옆 칩을 누르면', '까닭 한 줄이 열리고 바로 마감 창으로 갈 수 있습니다.', tapped_block)
             + case(5, '8월을 마감한 뒤', '같은 자리에서 표시만 사라집니다.', confirmed_block)
             + '</div></div>' + fut_memo + '</div>')
FUT_W, FUT_H = 1230, 1256      # 2026-09-26 자연 1232 + 24(목적지 맨 위 카드 · 칩을 누른 모습)
w('FutureProvisional', spec_frame(
    FUT_W, FUT_H, '미래 · 목적지 — 월말 예상 기준이 서기 전의 임시 계산 표시',
    '8월을 마감하기 전에도 미래 · 목적지 화면의 예상 값은 그대로 보여 주되 임시 계산이라고 표시합니다. '
    '왼쪽이 그 상태의 미래 화면이고, 번호는 표시가 붙는 자리입니다.',
    f'<div style="display: flex; gap: 32px; align-items: flex-start;">{future_left}{fut_right}</div>', sub_w=860), keep_all=True)


# ══════════════════════════════════════════════════════════════
# 3. EtcSubline — `기타` 서브라인 · 코치 `소비 없음 확인 n일` (rank 30 · v5-1 · v5-2)
# ══════════════════════════════════════════════════════════════
# 캐논(9월 8일): 기타 6만원 / 한도 10만원(NUMBERS §5 · 직접 50만원인 주거/관리 뒤 자동 배분) · 그중 카테고리 없음 7건 32,000원.
# 소비 · 이번 달의 카테고리 카드는 쓴 돈 위 다섯(주거/관리 · 식비 · 보험 · 통신 · 교통 7만원)이라 캐논에서는 기타 줄이 없다.
# 그림은 앱이 실제로 내는 예 — 캐논에 9월 7일 메모 없는 300,000원을 카테고리 없이 더 적은 날(하네스 2026-09-27 · W/tools/fix1/cap_etc.cjs):
# 142만원 / 216만원 · 주거/관리 47 → 기타 36만원 / 10만원 「카테고리 없음 8건 332,000원」 「한도의 360%」(회색) → 식비 24 → 보험 12 → 통신 8 (쓴 돈 순 · 교통 7만원은 여섯째).
# 부줄은 이름 · 금액 줄과 막대 사이(앱 .spending-category-main > .category-uncategorized-note · 11px · 500 · ink-3). 아이콘은 앱 기타 글리프(가로 점 셋).
CHEV14 = icon("right", 14, C["INK4"], 2.2)
DOTS3 = ('<svg width="15" height="15" viewBox="0 0 24 24" fill="#64748b"><circle cx="5" cy="12" r="1.7"/><circle cx="12" cy="12" r="1.7"/><circle cx="19" cy="12" r="1.7"/></svg>')
ETC_EXAMPLE_SUB = '카테고리 없음 8건 332,000원'
etc_row_spend = (
    f'<div style="display: flex; align-items: center; gap: 10px; padding: 7px 0;">'
    f'<div style="width: 30px; height: 30px; border-radius: 10px; background: #64748b18; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">{DOTS3}</div>'
    f'<div style="flex: 1; min-width: 0;">'
    f'<div style="display: flex; align-items: baseline; justify-content: space-between; gap: 8px;">'
    f'<span style="font-size: 13.5px; font-weight: 600; color: #101828;">기타</span>'
    f'<span style="font-size: 13px; font-weight: 600; color: #101828; white-space: nowrap;">36만원<span style="font-size: 11.5px; font-weight: 500; color: #626D88;"> / 10만원</span></span></div>'
    f'<div style="display: flex; align-items: center; gap: 4px; margin-top: 2px;"><span style="font-size: 11px; font-weight: 500; color: #626D88; white-space: nowrap;">{ETC_EXAMPLE_SUB}</span>{imark(1)}</div>'
    f'<div style="position: relative; height: 6px; border-radius: 99px; background: #EFF2F8; margin-top: 6px; overflow: hidden;">'
    f'<div style="position: absolute; inset: 0 0 0 0; border-radius: 99px; background: #64748b;"></div></div>'
    f'</div>'
    f'<span style="display: inline-flex; align-items: center; justify-content: flex-end; gap: 2px; min-width: 80px; font-size: 12px; font-weight: 600; color: #626D88; white-space: nowrap; flex-shrink: 0;">한도의 360%{CHEV14}</span></div>')
ROW46 = '<div style="display: flex; align-items: center; gap: 10px; height: 46px;">'
assert sp_cats.count(ROW46) == 5
_starts = [m_.start() for m_ in re.finditer(re.escape(ROW46), sp_cats)]
_rows = [balanced_at(sp_cats, a) for a in _starts]      # 줄마다 균형 잡힌 div 하나
assert all(balanced(r) for r in _rows) and '교통' in _rows[4] and '주거/관리' in _rows[0]
_head = sp_cats[:_starts[0]].replace('112만원 / 216만원', '142만원 / 216만원', 1)
assert '142만원 / 216만원' in _head
spend_etc = (_head.rstrip() + '\n        ' + '\n\n        '.join([_rows[0], etc_row_spend, _rows[1], _rows[2], _rows[3]])
             + '\n      </div>\n    </div>')      # 쓴 돈 순 다섯: 주거/관리 · 기타 · 식비 · 보험 · 통신(교통은 여섯째라 빠짐)
assert balanced(spend_etc) and spend_etc.count(ETC_EXAMPLE_SUB) == 1 and '교통' not in spend_etc

# 한도 · 카테고리 배분 — Limits(DZ2)의 카드 그대로(기타 이름 칸 안 `카테고리 없음 7건 32,000원` · 13개 · 직접 1개). 번호만 얹는다(이름 옆).
# 2026-09-27 fix-up: 부줄은 앱처럼 이름 칸(68) 안 「기타」 아래 두 줄(막대 왼쪽) — 예전 줄 아래 온 폭 한 줄은 앱에 없는 모양.
SUB_LIMIT = '>기타</span><span style="font-size: 11px; font-weight: 500; line-height: 1.35; color: #626D88; word-break: keep-all;">카테고리 없음 7건 32,000원</span>'
assert lm_cats.count(SUB_LIMIT) == 1
limit_etc = lm_cats.replace(SUB_LIMIT, SUB_LIMIT.replace('>기타</span>', f'>기타{imark(3)}</span>', 1), 1)
assert balanced(limit_etc)

# 코치 — 이번 달 기록이 0건이면 판정하지 않는다(앱 · 9월 기록을 비우고 2 · 4 · 6일 안 썼어요 표시 · W/tools/dz4/cap_etc.cjs). 안 썼어요 날은 기록 건수가 아니다.
SAVING_EMPTY = (f'<div style="border: 1.5px dashed {C["VIO_LINE"]}; background: {C["VIO_SOFT"]}; border-radius: 14px; padding: 11px 12px; display: flex; flex-direction: column; gap: 8px;">'
                f'<div style="display: flex; align-items: center; justify-content: space-between;"><span style="font-size: 11.5px; font-weight: 600; color: {C["VIO_STRONG"]};">저장되지 않는 가정</span>'
                f'<span style="font-size: 12px; font-weight: 700; color: {C["VIO_STRONG"]};">−10%</span></div>'
                f'<div style="position: relative; height: 16px;"><div style="position: absolute; left: 0; right: 0; top: 6px; height: 4px; border-radius: 99px; background: #E4D8FB;"></div>'
                f'<div style="position: absolute; left: 0; width: 25%; top: 6px; height: 4px; border-radius: 99px; background: {C["VIO"]};"></div>'
                f'<span style="position: absolute; left: calc(25% - 8px); top: 0; width: 16px; height: 16px; border-radius: 99px; background: #FFFFFF; border: 2px solid {C["VIO"]};"></span></div>'
                f'<div style="display: flex; align-items: center; margin-top: -4px;"><span style="flex: 1; font-size: 11px; color: {C["INK4"]};">0%</span>'      # 앱 .coach-saving-labels(2026-09-27 fix-up 4)
                f'<span style="font-size: 11.5px; font-weight: 600; color: {C["VIO_STRONG"]}; white-space: nowrap;">카테고리별 −10% 가정</span>'
                f'<span style="flex: 1; text-align: right; font-size: 11px; color: {C["INK4"]};">40%</span></div>'
                f'<span style="font-size: 12px; line-height: 1.45; color: {C["VIO_STRONG"]};">이번 달 변동비 기록이 있으면 줄였을 때의 효과를 비교해요.</span></div>')
coach_need = mini_sheet('코칭', '저장된 기록을 보고 중요한 순서로 알려 드려요.',
                        f'<div style="display: flex; flex-direction: column; gap: 8px;">'
                        + advice('warn', '카드 할부 금리 14.5%가 투자 자산 기본 수익률 연 5.0%보다 높아요', '이 부채를 갚는 쪽이 투자보다 확실히 유리해요. 100만원을 갚으면 1년에 10만원 이득이에요.', '상환 계획', 1)
                        + advice('sky', f'이번 달 기록이 아직 없어요{imark(5)}', '달력에서 날짜를 눌러 쓴 돈을 적어 보세요', '오늘 쓴 돈 적기', 2)
                        + advice('sky', "'비상금 6개월'에 매달 필요한 돈", '목표일까지 6개월, 목표액과 목표일로 계산하면 매달 80만원이 필요해요.', '목적지 보기', 3)      # 앱 셋째 카드(2026-09-27 fix-up 2 · tools/fix2/cap_coach0.cjs)
                        + f'<div style="font-size: 11.5px; font-weight: 600; color: {C["INK2"]}; padding: 2px 2px 0;">카테고리 절감 가정</div>' + SAVING_EMPTY + SAVING_FOLD + '</div>')
coach_first_day = mini_sheet('코칭', '저장된 기록을 보고 중요한 순서로 알려 드려요.',
                             f'<div style="display: flex; flex-direction: column; gap: 8px;">'
                             + advice('sky', f'이번 달 기록이 아직 없어요{imark(6)}', '달력에서 날짜를 눌러 쓴 돈을 적어 보세요', '오늘 쓴 돈 적기', 1)
                             + f'<div style="font-size: 11.5px; font-weight: 600; color: {C["INK2"]}; padding: 2px 2px 0;">카테고리 절감 가정</div>' + SAVING_EMPTY + SAVING_FOLD + '</div>')

etc_memo = memo_box([
    (1, f'소비 · 이번 달의 카테고리별 소비 — 기타가 쓴 돈 위 다섯에 들 때만 그 이름 · 금액 줄 아래 {code("카테고리 없음 N건 N원")}(링크 없음). 금액 · 막대 · {code("한도의 N%")}는 엔진 값 그대로(카테고리 없음도 소비이고 한도 사용량입니다). 카테고리 없는 몫 때문에 넘은 기타 줄은 회색 — 판정은 카테고리 없는 금액을 빼고 해요. 다른 카테고리가 제 한도를 넘으면 빨강입니다(LimitCardCases ③ {code("한도의 141%")}). '
        f'시안 사용자 9월 8일은 교통 7만원이 다섯째라 이 줄은 한도 탭에만 보입니다({code(SUBLINE)}) — 그림은 9월 7일에 메모 없는 300,000원을 카테고리 없이 더 적은 날의 앱 화면입니다.'),
    (2, f'{code("기타 한도")} 경고와 코치의 가장 큰 카테고리 비중은 카테고리 없는 금액을 빼고 다시 판단합니다. 화면에 따로 문장을 두지 않습니다(카테고리를 고르면 원래 판정으로 돌아갑니다).'),
    (3, f'소비 · 한도의 카테고리 배분에도 같은 부줄 — 이름 칸(68) 안 「기타」 아래 11px 두 줄(막대 왼쪽 · 줄 높이가 그만큼 늘어요). 머리 {code("13개 · 직접 1개")}(주거/관리 50만원을 직접 정함). '
        f'한도 탭의 기타 막대는 판정 금액 — 카테고리 없는 32,000원을 뺀 28,000원 ÷ 10만원 = 28%(소비 탭 막대는 쓴 돈 그대로).'),
    (4, f'직접 정한 고정비 한도는 고정비 예상에 반영하지 않는다(계획 §12-15)는 규칙은 그대로이지만 화면 문장은 두지 않습니다.'),
    (5, f'코치 — 이번 달 기록이 0건이면 판정하지 않고 {code("이번 달 기록이 아직 없어요 · 달력에서 날짜를 눌러 쓴 돈을 적어 보세요 · 오늘 쓴 돈 적기 ›")}. 안 썼어요로 표시한 날은 기록 건수에 들지 않습니다(예전 {code("소비 없음 확인 n일")}은 쓰지 않음 — 이름은 {code("안 썼어요")}).'),
    (6, f'코칭 · 월급만 넣은 첫날도 같은 카드 하나 + 카테고리 절감 가정({code("이번 달 변동비 기록이 있으면 줄였을 때의 효과를 비교해요.")}). 월급도 없으면 코칭 · 기록 없음(CoachEmpty)의 {code("이렇게 시작해 보세요")}입니다.')])

etc_body = (f'<div style="display: flex; gap: 24px; align-items: flex-start;">'
            + col(362, [case(1, '소비 · 이번 달 — 카테고리별 소비', '기타가 다섯 안에 들면 이름 아래에 카테고리 없는 몫을 따로 적습니다. 예: 9월 7일에 메모 없는 30만원을 카테고리 없이 더 적은 날.', spend_etc)])
            + col(362, [case(3, '소비 · 한도 — 카테고리 배분', '같은 부줄이 기타 이름 아래에(시안 사용자 9월 8일).', limit_etc)])
            + col(362, [case(5, '코치 — 이번 달 기록이 없을 때', '판정하지 않고 적을 곳만 알려 줍니다. 기록에서 나오지 않는 안내(카드 할부 · 목적지)와 절감 가정은 그대로입니다.', coach_need),
                        case(6, '코칭 · 월급만 넣은 첫날', '같은 카드 하나와 절감 가정.', coach_first_day)])
            + '</div>' + etc_memo)
ETC_W, ETC_H = 1200, 1715      # 2026-09-27 fix-up 4 자연 1691 + 24(⑤ ⑥ 코치 눈금 줄 · 계산 기준) ·     # 2026-09-27 fix-up 3 자연 1545 + 24(메모 1 · 3 문장) · 2026-09-27 fix-up 2 자연 1508 + 24(⑤ 코치 셋째 카드 · 카테고리 절감 가정) · 2026-09-26 자연 1240 + 24(코치 두 견본 · 절감 가정)
w('EtcSubline', spec_frame(
    ETC_W, ETC_H, '카테고리 없는 소비와 안 쓴 날 — 소비 · 한도 · 코치에서',
    '하루 시트에서 카테고리 없이 저장한 소비는 기타로 들어가요. 소비 · 한도 화면은 기타 아래에 그 몫을 따로 적고, '
    '코치는 이번 달 기록이 없으면 판정하지 않고 적을 곳만 알려 줍니다.',
    etc_body, sub_w=860), keep_all=True)


# ══════════════════════════════════════════════════════════════
# 4. LimitCardCases — 한도 카드 네 사례 + 코치 라벨 (rank 31 · v5-3)
# ══════════════════════════════════════════════════════════════
CHEV = ('<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#697182" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink: 0;"><path d="m9 18 6-6-6-6"/></svg>')
GRAD = 'linear-gradient(90deg, #6E6BEE 0%, #7A3FE4 100%)'          # 홈 한도 카드(Main)의 막대 그대로


def limit_case(label, right, right_color, row2, used_pct=0.0, bar=GRAD, extra=None):
    """홈 `이번 달 한도` 카드(Main 과 같은 틀): 제목 옆 회색 글 · 오른쪽 값 › · 둘째 줄 · (시작일 줄) · 막대."""
    lab = f' <span style="font-weight: 500; color: #626D88;">{label}</span>' if label else ''
    fill = (f'<div style="position: absolute; inset: 0 {100 - used_pct:g}% 0 0; border-radius: 99px; background: {bar};"></div>' if used_pct > 0 else '')
    ex = f'<div style="font-size: 12px; line-height: 1.45; color: #626D88; margin-top: 2px;">{extra}</div>' if extra else ''
    return (f'<div style="background: #FFFFFF; border: 1px solid #E3E8F1; border-radius: 18px; padding: 12px 14px;">'
            f'<div style="display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 4px 8px;">'
            f'<span style="font-size: 13.5px; font-weight: 600; color: #101828; white-space: nowrap;">이번 달 한도{lab}</span>'
            f'<div style="display: flex; align-items: center; gap: 4px; margin-left: auto;"><span style="font-size: 13.5px; font-weight: 600; color: {right_color}; white-space: nowrap;">{right}</span>{CHEV}</div></div>'
            f'<div style="font-size: 13px; line-height: 1.45; color: #475467; margin-top: 4px;">{row2}</div>{ex}'
            f'<div style="position: relative; height: 8px; border-radius: 99px; background: #E8ECF5; margin-top: 9px; overflow: hidden;">{fill}</div></div>')


# 캐논 값(NUMBERS §4 · 앱 homeLimitView 에 시안 사용자 + 기록 한 건) — 앱 캡처의 `직접 73만원` 예는 캐논이 아니라 쓰지 않는다.
lc_none = v5.s1.limit_empty()
lc_zero = limit_case('오늘 포함 하루 0원', '남은 한도 0원', C["INK"], '216만원 중 216만원 썼어요', 100)
lc_over = limit_case(None, '3만원 넘음', C["NEG"], '이번 달 한도는 이미 넘었어요 · 216만원 중 219만원 썼어요', 100, C["NEG"])
lc_last = limit_case('이번 달 마지막 날', '이번 달 남은 한도 9만원', C["POS"], '216만원 중 207만원 썼어요', 95.8)
lc_before = v5.limit_before()
lc_start = v5.limit_first.replace(' flex-shrink: 0;">', '">', 1)
lc_base = limit_forward().replace(' flex-shrink: 0;">', '">', 1)
assert lc_base.count('오늘 포함 하루 45,220원') == 1 and lc_start.count('9월 5일부터 기록') == 1

# 한도 탭 맨 위 카드(Limits 에서 잘라 옴) — 넘음(자동 · 쓴 돈 219만원) · 마지막 날(9월 30일 · 남은 9만원)
LM_CARD = balanced_at(LM, LM.index(LM_TOP))
lm_over = LM_CARD
for a_, b_ in [('<span style="font-size: 11px; font-weight: 500; color: #626D88;">남은 한도</span>', '<span style="font-size: 11px; font-weight: 500; color: #626D88;">한도를</span>'),
               ('color: #0F7B47;">104만원</span>', f'color: {C["NEG"]};">3만원 넘었어요</span>'),
               ('inset: 0 48.1% 0 0; border-radius: 99px; background: linear-gradient(90deg, #3556E6 0%, #6E6BEE 100%);', f'inset: 0 0% 0 0; border-radius: 99px; background: {C["NEG"]};'),
               ('사용 112만원 · 52%', '사용 219만원 · 101%'), ('오늘 포함 23일 남음 · 하루 45,220원', '오늘 포함 23일 남음 · 남은 한도 없음')]:
    lm_over = swap(lm_over, a_, b_)
lm_last = LM_CARD
for a_, b_ in [('color: #0F7B47;">104만원</span>', 'color: #0F7B47;">9만원</span>'), ('inset: 0 48.1% 0 0', 'inset: 0 4.2% 0 0'),
               ('사용 112만원 · 52%', '사용 207만원 · 96%'), ('오늘 포함 23일 남음 · 하루 45,220원', '이번 달 마지막 날 · 남은 한도 9만원'),
               ('지키려면 152만원 안에서', '지키려면 133만원 안에서')]:      # 9월 30일 참고 값(앱 하네스 · 목표일이 다가와 목적지 필요액이 커짐 · 2026-09-27 fix-up 3)
    lm_last = swap(lm_last, a_, b_)

# 카테고리 줄이 넘었을 때(예: 식비 한도를 직접 17만원으로 정한 달 · 쓴 돈 24만원은 캐논) — 한도 탭 줄 둘째 줄 `▲ 7만원 넘음`(a11y-3 · D3) · 소비 탭 줄 오른쪽 `한도의 141%`
cat_over = (f'<div style="background: #FFFFFF; border: 1px solid #E3E8F1; border-radius: 18px; padding: 6px 14px;">'
            f'<div style="display: flex; align-items: center; gap: 10px; min-height: 52px;">'
            f'<span style="width: 8px; height: 8px; border-radius: 3px; background: {CAT["식비"]}; flex-shrink: 0;"></span>'
            f'<span style="font-size: 13.5px; font-weight: 500; color: #101828; width: 52px; flex-shrink: 0;">식비</span>'
            f'<div style="flex: 1; min-width: 0; position: relative; height: 6px; border-radius: 99px; background: #EFF2F8; overflow: hidden;"><div style="position: absolute; inset: 0 0% 0 0; border-radius: 99px; background: {C["NEG"]};"></div></div>'
            f'<div style="display: flex; flex-direction: column; align-items: flex-end; flex-shrink: 0;"><span style="font-size: 13px; font-weight: 600; color: {C["NEG"]}; white-space: nowrap;">24만원<span style="font-size: 11.5px; font-weight: 500; color: #626D88;"> / 17만원</span></span>'
            f'<span style="font-size: 11.5px; font-weight: 600; color: {C["NEG"]}; white-space: nowrap;">▲ 7만원 넘음</span></div>{CHEV}</div>'
            f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px; padding: 8px 0 6px; border-top: 1px solid #F3F5FA;">'
            f'<span style="font-size: 12px; color: #626D88;">소비 탭 같은 줄의 오른쪽</span><span style="font-size: 12px; font-weight: 600; color: {C["NEG"]}; white-space: nowrap;">한도의 141% ›</span></div></div>')

coach_daily = advice('pos', '한도 안에서 쓰고 있어요', '이번 달 한도는 104만원 남았어요. 오늘 포함 남은 23일 동안 하루 45,220원씩 쓰면 한도(216만원)를 지켜요.', None, 8)
coach_over = advice('warn', '이번 달 한도를 3만원 넘었어요', '한도 216만원 중 219만원 썼어요. 이대로면 월말엔 100만원 넘어요. 오늘 포함 남은 23일은 꼭 필요한 곳에만 써 보세요.', '이번 달 한도', 3)      # 앱 순위 3(219만원 · 적자 · 월말 소비 목표 다음 · 2026-09-27 fix-up 5)
coach_last = advice('pos', '한도 안에서 쓰고 있어요', '오늘이 이번 달 마지막 날이에요. 이번 달 남은 한도 9만원', None, 7)      # 앱 순위 7(9월 30일 · 207만원 · 2026-09-27 fix-up 5)

lc_left = (f'<div style="width: 362px; flex-shrink: 0; display: flex; flex-direction: column; gap: 8px;">'
           f'<div><div style="font-size: 14px; font-weight: 700; letter-spacing: -0.01em; color: {C["INK"]};">평소 — 한도가 남아 있을 때</div>'
           f'<div style="font-size: 12px; line-height: 1.5; color: {C["INK3"]}; margin-top: 3px;">남은 한도 ÷ 오늘 포함 남은 날(23일) · 10원 단위. 홈의 하루 숫자는 이것 하나입니다.</div></div>{lc_base}'
           f'<p style="margin: 2px 2px 0; font-size: 12px; line-height: 1.5; color: {C["INK3"]};">오른쪽 경우들은 <b style="font-weight: 600; color: {C["INK2"]};">제목 옆 회색 글 · 오른쪽 값 · 둘째 줄</b>이 바뀌는 것입니다. '
           f'넘었을 때는 하루 금액 대신 넘은 금액을 빨갛게, 하루 0원이라고 쓰지 않습니다.</p>'
           f'<div style="margin-top: 14px; display: flex; flex-direction: column; gap: 8px;">{case_cap(5, "소비 · 한도 맨 위 카드 — 넘었을 때", "남은 한도 자리가 한도를 N 넘었어요 · 남은 한도 없음 · 빨간 막대.")}{lm_over}</div>'
           f'<div style="margin-top: 14px; display: flex; flex-direction: column; gap: 8px;">{case_cap(5, "소비 · 한도 맨 위 카드 — 마지막 날", "남은 일수 자리가 이번 달 마지막 날 · 남은 한도.")}{lm_last}</div></div>')
lc_grid = (f'<div style="flex: 1; min-width: 0; display: grid; grid-template-columns: repeat(2, 362px); gap: 24px 20px; align-items: start;">'
           + case(1, '한도를 아직 안 정했을 때', '0이 아니라 회색 —. 막대도 비어 있습니다(월급도 직접 한도도 없음).', lc_none)
           + case(2, '남은 한도가 꼭 0원일 때', '남은 날이 있고 남은 한도가 실제로 0.', lc_zero)
           + case(3, '한도를 넘었을 때', '오른쪽에 넘은 금액(빨강) · 둘째 줄이 이미 넘었다고 말합니다.', lc_over)
           + case(4, '이번 달 마지막 날', '하루 금액 대신 이번 달 남은 한도.', lc_last)
           + case(8, '이번 달 첫 기록 전', '총한도만 말하고 막대는 비어 있습니다.', lc_before)
           + case(8, '달 중간에 시작한 달', '남은 한도는 초록 대신 기본 글자색 · 시작일 줄.', lc_start)
           + case(3, '카테고리 줄이 넘었을 때', '한도 탭은 둘째 줄에 ▲ N 넘음, 소비 탭은 한도의 N%.', cat_over)
           + case(6, '코치 — 평소', '본문의 하루 금액도 같은 값 · 같은 라벨(낮은 순서 · 다른 안내 안).', coach_daily)
           + case(6, '코치 — 넘었을 때', '넘은 금액 · 월말 예상 넘음 · 이번 달 한도 ›.', coach_over)
           + case(7, '코치 — 마지막 날', '한도 카드와 같은 문구로 바뀝니다.', coach_last)
           + '</div>')
LC_MEMO_ROWS = [
    (1, f'{code("오늘 포함 하루 —")} · 오른쪽 {code("—")} · {code("한도를 아직 안 정했어요")} — 판정 선이 없을 때(월급도 직접 한도도 없음). 0원과 합치지 않습니다.'),
    (2, f'{code("오늘 포함 하루 0원")} — 남은 한도가 실제로 0원일 때만.'),
    (3, f'넘음 — 오른쪽 {code("3만원 넘음")}(빨강) · 둘째 줄 {code("이번 달 한도는 이미 넘었어요 · 216만원 중 219만원 썼어요")} · 빨간 막대. {code("하루 0원")}이라고 쓰지 않습니다. 카드 · 줄은 {code("N 넘음")}, 한도 탭은 {code("한도를 N 넘었어요")}.'),
    (4, f'{code("이번 달 마지막 날")} — 남은 날이 오늘 하루뿐이면 하루 금액 대신 {code("이번 달 남은 한도 9만원")}.'),
    (5, f'소비 · 한도 맨 위 카드도 같은 규칙 — {code("오늘 포함 23일 남음 · 하루 45,220원")} / {code("남은 한도 없음")} / {code("이번 달 마지막 날 · 남은 한도 9만원")}. 참고 줄 {code("저축 · 상환 계획까지 지키려면 152만원 …")}은 회색 12px(판정 아님) — 목표일이 다가오면 목적지 필요액이 커져 9월 30일엔 133만원입니다. '
        f'넘었을 때 그 아래 소비 경고 카드 첫 줄은 {code("이번 달 한도를 3만원 넘었어요 · 한도 216만원 중 219만원 썼어요. · 이번 달 한도 ›")}, 직접 정한 한도면 알약이 {code("직접 ›")}.'),
    (6, f'코치 본문의 하루 금액도 {code("오늘 포함 하루 45,220원씩")}으로 한도 카드와 같게 씁니다. 넘었으면 {code("이번 달 한도를 3만원 넘었어요")} + {code("이번 달 한도 ›")} — 그날(219만원) 코치 목록에서는 {code("이대로면 이번 달 18만원 적자예요")} · {code("월말엔 소비 목표 60%를 넘어요")} 다음 셋째예요.'),
    (7, f'코치 — 마지막 날이면 본문이 {code("오늘이 이번 달 마지막 날이에요. 이번 달 남은 한도 9만원")}(9월 30일 · 207만원 · 목록 일곱째).'),
    (8, f'남은 날은 오늘을 포함해 셉니다(마지막 날 = 1일 · max(1, 30 − 8 + 1) = 23). 첫 기록 전은 {code("총 216만원")} + {code("소비를 기록하면 남은 한도가 보여요")}, 달 중간에 시작한 달은 {code("9월 5일부터 기록 · 그 전 소비는 빠져 있어요")}.')]
assert [n_ for n_, _ in LC_MEMO_ROWS] == [1, 2, 3, 4, 5, 6, 7, 8]
lc_memo = memo_box(LC_MEMO_ROWS)
LC_W, LC_H = 1200, 1464      # 2026-09-30 한도 카드 시작일 줄 위 여백 2 → 4(앱과 같게) 자연 1440 + 24 · 2026-09-27 fix-up 5 자연 1438 + 24(메모 6 · 7 코치 순위) · fix-up 3 자연 1420 + 24(메모의 번호를 뗌) · DZ4 검토 — 자연 1438 + 24(메모 줄이 늘었는데 높이를 안 고쳐 아래 여백이 6이던 것) · 이전 자연 1420 + 24(첫 기록 전 · 시작한 달 · 카테고리 넘음 · 한도 탭 두 카드 · 코치 넘음)
w('LimitCardCases', spec_frame(
    LC_W, LC_H, '이번 달 한도 카드 — 하루 금액 자리의 경우들',
    '홈 한도 카드의 하루 금액은 늘 오늘 포함 남은 날로 나눈 값입니다. 한도가 없을 때 · 0원일 때 · 넘었을 때 · 마지막 날 · 첫 기록 전 · 달 중간 시작을 같은 표시로 합치지 않습니다.',
    f'<div style="display: flex; gap: 32px; align-items: flex-start;">{lc_left}{lc_grid}</div>{lc_memo}', sub_w=860), keep_all=True)


# ══════════════════════════════════════════════════════════════
# 5. RecurringPrefill — 반복 거래 다이얼로그 미리 채움 (rank 31 · v5-3 · 앱 화면 390 × 844)
# ══════════════════════════════════════════════════════════════
# 하루 시트에서 9월 8일 월세 700,000원을 주거/관리로 저장 → 완료 카드 `매달 반복으로 만들기 ›` → 이 창(앱 · record-2 · spending-13 · D4 반복 기록).
# RecurringDialog(gen_modals)와 같은 틀 — 등록된 규칙이 먼저, 그 아래 `새 규칙`. 모달 조각은 import 하지 않고 같은 모양으로 옮겨 적었다(그쪽 장을 다시 쓰지 않게).
# 휴대폰 요금 55,000원: 앱 compact() 는 `6만원`, 시안 금액 쓰는 법(gen_calendar.fmt_sum)은 `5.5만원` — 앱을 고치자는 제안(DZ0 · DZ2 확인할 것 ①)이라 시안 쓰는 법대로 둔다.
def _tri(col=None):
    return f'<svg width="9" height="9" viewBox="0 0 9 9" style="flex-shrink: 0;"><path d="M1.5 0 7.5 4.5 1.5 9Z" fill="{col or C["INK3"]}"/></svg>'


def _pair(a_, b_, mt=0):
    return f'<div style="display: flex; gap: 10px; align-items: flex-start; margin-top: {mt}px;">{a_}{b_}</div>'


rules = []
for i, (name, meta, amt, on) in enumerate([("ETF 자동이체", "매월 6일 · 저축·투자", "30만원", True),      # LedgerV5 9월 6일 자동 기록 · 달력 9월 6일 · 8월 6일 이체와 같은 날
                                           ("휴대폰 요금", "매월 25일 · 통신", "5.5만원", True),      # DaySheetConfirm `이번 달 휴대폰 요금 55,000원은 25일에 자동으로 기록돼요`와 같은 규칙
                                           ("헬스장", "꺼 둠 · 문화/여가", "5만원", False)]):
    c_ = C["INK"] if on else C["INK4"]
    bb = f'border-bottom: 1px solid {C["LINE_ROW"]};' if i < 2 else ''
    rules.append(
        f'<div style="display: flex; align-items: center; gap: 10px; min-height: 52px; {bb}">'
        f'<div style="flex: 1; min-width: 0;"><div style="font-size: 13.5px; font-weight: 600; color: {c_};">{name}</div>'
        f'<div style="font-size: 11px; color: {C["INK4"] if not on else C["INK3"]};">{meta}</div></div>'
        f'<span style="font-size: 13.5px; font-weight: 600; color: {c_};">{amt}</span>'
        f'{toggle(on)}{icon("more", 16, C["INK4"], 2.2)}</div>')
# 앱 .recurring-prefill-note — 위 4 · 아래 10 · 안쪽 8 12 · 모서리 11 · 12 / 400 / 18 ink-2(2026-09-27 fix-up 5 · 예전 안쪽 10 12 · 아래 12 · 12.5 / 1.55)
PREFILL_NOTE = (f'<div style="display: flex; flex-direction: column; padding: 8px 12px; background: {C["INSET"]}; border-radius: 11px; margin: 4px 0 10px; font-size: 12px; line-height: 18px; color: {C["INK2"]};">'
                f'<span>방금 저장한 기록에서 채웠어요</span><span>이번 달 반복 기록은 이 기록으로 이미 있어요</span></div>')      # 앱 문구(spending-13) · 두 줄 같은 모양(앱 — 첫 줄도 굵지 않음)
# 반복 규칙 안내 상자 · 시작 월 = gen_modals RULE_NOTE · new_rule 과 같은 앱 치수(위 11 · 안쪽 10 11 · 접힌 칸 11.5 / 500 ink-3 · 삼각 뒤 3 · 시작 월 10 아래 · 2026-09-27 fix-up 5)
RULE_NOTE_V5 = (
    f'<div style="display: flex; gap: 8px; padding: 10px 11px; background: {C["INSET"]}; border-radius: 12px; margin-top: 11px;">'
    f'<span style="flex-shrink: 0; margin-top: 1px;">{icon("info", 14, C["INK3"], 1.9)}</span>'
    f'<div style="min-width: 0;"><div style="font-size: 11.5px; line-height: 17.25px; color: {C["INK3"]};">이번 달 결제일이 이미 지났으면 저장하자마자 이번 달 기록이 만들어져요 · 이미 적어 둔 같은 기록이 있으면 먼저 물어봐요</div>'
    f'<div style="display: flex; align-items: center; gap: 3px; margin-top: 6px; font-size: 11.5px; font-weight: 500; line-height: 17.25px; color: {C["INK3"]};">{_tri()}반복 기록이 만들어지는 방식</div></div></div>')
MONTH_FIELD = (f'<div style="margin-top: 10px;"><div style="font-size: 12px; font-weight: 600; color: {C["INK2"]}; margin-bottom: 7px;">시작 월</div>'
               f'<div style="display: flex; align-items: center; justify-content: space-between; height: 46px; padding: 0 12px; border-radius: 11px; '
               f'border: 1px solid {C["INPUT"]}; background: {C["SURF"]};"><span style="font-size: 15px; color: {C["INK"]};">2026년 10월</span>'
               f'{icon("cal", 16, C["INK2"], 1.9)}</div></div>')
PREFILL_H = 877      # 2026-09-27 fix-up 5 자연 853 + 24(앱 치수 — 채움 안내 12 / 18 · 규칙 안내 · 시작 월 10 아래) · DZ4 검토 자연 870 + 24(채움 안내 두 줄 같은 모양) · 이전 자연 868 + 24(목록이 먼저 · 새 규칙 안내 상자 · 시작 월 한 줄 · 적용 안내)
w('RecurringPrefill', sheet(
    '반복 기록', '매달 반복되는 기록이에요. 앱을 열면 시작 월부터 이미 지난 결제일도 기록으로 만들어요.',
    group('등록된 반복 기록', f'<div style="padding: 0 13px; background: {C["SURF"]}; border: 1px solid {C["LINE"]}; border-radius: 14px;">{"".join(rules)}</div>',
          meta='3건 · 켜짐 2건')
    + group('새 반복 기록', PREFILL_NOTE
            + _pair(field("이름", "월세", required=True), field("금액", "700,000", "원", required=True, w=136))      # 앱 이름 208 · 금액 136
            + _pair(select_field("카테고리", "주거/관리", required=True), field("결제일", "8", "일", w=104), mt=12)
            + MONTH_FIELD + RULE_NOTE_V5),
    sheet_footer('닫기', '반복 기록 추가'), scrim_h=40, h=PREFILL_H), keep_all=True)


# ══════════════════════════════════════════════════════════════
# 6. ImportBackupNotes — 가져오기 · 백업 안내 문구 (rank 31 · v5-3)
# ══════════════════════════════════════════════════════════════
IMPORT_NOTE = '불러온 기록의 카테고리 없음 표시도 함께 반영돼요 · 확인 표시는 전체 교체에서만 반영돼요 · 이미 있는 기록은 그대로예요'           # 앱 문구(D4)
UNCHECK_NOTE = '9월 5일 표시가 풀렸어요'                                                                                                  # 계획 §8 원문(` · 다시 표시`는 링크)


def diffrow(label, count, tone, desc, last=False):      # gen_modals.diffrow 와 같은 모양
    m = {"new": (C["POS"], C["POS_SOFT"]), "dup": (C["TAB_INK"], C["LINE_SOFT"]), "conf": (C["WARN"], C["WARN_SOFT"]), "chk": (C["SKY"], C["SKY_SOFT"])}
    c_, bg = m[tone]
    bb = '' if last else f'border-bottom: 1px solid {C["LINE_ROW"]};'
    return (f'<div style="display: flex; align-items: center; gap: 10px; min-height: 48px; {bb}">'
            f'<span style="min-width: 34px; height: 24px; border-radius: 7px; background: {bg}; color: {c_}; font-size: 12px; '
            f'font-weight: 700; display: flex; align-items: center; justify-content: center; padding: 0 7px;">{count}</span>'
            f'<div style="flex: 1; min-width: 0;"><div style="font-size: 13px; font-weight: 600; color: {C["INK"]};">{label}</div>'
            f'<div style="font-size: 11px; color: {C["INK3"]};">{desc}</div></div>{icon("right", 15, C["INK4"], 2)}</div>')


checkbox_on = (f'<div style="display: flex; align-items: flex-start; gap: 9px;"><span style="width: 20px; height: 20px; border-radius: 6px; background: {C["BRAND"]}; display: flex; '
               f'align-items: center; justify-content: center; flex-shrink: 0;">{icon("check", 13, "#FFFFFF", 3)}</span>'
               f'<span style="font-size: 12.5px; line-height: 1.5; color: {C["INK2"]};">데이터 종류와 적용 후 내역을 확인했어요.</span></div>')
import_sheet = sheet(
    '백업 불러오기', 'navi-backup-2026-09-01.json · 저장하기 전에 무엇이 바뀌는지 먼저 봐요.',      # 앱 설정 › 백업 불러오기(app/page.tsx) · ImportReview 와 같게 — 「저장 전에」는 복구 화면 쪽
    group('적용 방식', segmented(['합치기', '전체 교체'], 0) +
          f'<div style="margin-top: 9px;">{note("「합치기」는 겹치지 않는 기록만 넣어요. 「전체 교체」를 고르면 지금 기록이 모두 사라져요.", "mute")}</div>') +
    group('불러올 항목', f'<div style="padding: 0 13px; background: {C["SURF"]}; border: 1px solid {C["LINE"]}; border-radius: 14px;">'
                          f'{diffrow("새로 추가", 24, "new", "기록 21 · 자산 2 · 목적지 1")}'
                          f'{diffrow("이미 있음 · 건너뜀", 8, "dup", "같은 기록 ID")}'
                          f'{diffrow("값이 다름 · 기존 유지", 2, "conf", "같은 ID의 내용이 다름")}'
                          f'{diffrow("검토 필요", 1, "chk", "비슷한 기존 기록 있음", last=True)}</div>') +
    group('적용 후', f'<div style="display: flex; gap: 8px;">'
                      f'<div style="flex: 1; padding: 12px; background: {C["INSET"]}; border-radius: 13px;">'
                      f'<div style="font-size: 11.5px; color: {C["INK3"]};">지금</div>'
                      f'<div style="font-size: 18px; font-weight: 600; color: {C["INK"]}; margin-top: 3px;">기록 97건</div>'
                      f'<div style="font-size: 11.5px; color: {C["INK3"]}; margin-top: 2px;">순자산 9,350만원</div></div>'
                      f'<div style="display: flex; align-items: center;">{icon("arrowr", 16, C["INK4"], 2.2)}</div>'
                      f'<div style="flex: 1; padding: 12px; background: {C["BRAND_SOFT"]}; border-radius: 13px;">'
                      f'<div style="font-size: 11.5px; color: {C["BRAND"]};">적용 후</div>'
                      f'<div style="font-size: 18px; font-weight: 600; color: {C["INK"]}; margin-top: 3px;">기록 118건</div>'
                      f'<div style="font-size: 11.5px; color: {C["INK3"]}; margin-top: 2px;">순자산 9,850만원</div></div></div>'
                      f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px; height: 44px; margin-top: 10px; padding: 0 13px; border-radius: 12px; background: {C["INSET"]};">'
                      f'<span style="font-size: 13px; font-weight: 600; color: {C["INK"]};">백업 설정 · 상세 내역</span><span style="font-size: 12px; font-weight: 600; color: {C["INK3"]};">내 데이터 &rsaquo;</span></div>'
                      f'<div style="font-size: 11.5px; line-height: 1.5; color: {C["INK3"]}; margin-top: 8px;">순자산 목적지의 모은 돈은 불러온 뒤의 자산 · 부채 잔액으로 계산해요.</div>'
                      # 앱 import-review .import-quick-entry-note = 확인 칸 바로 위 마지막 줄(2026-09-27 fix-up 3 · 예전엔 불러올 항목 목록 바로 아래)
                      f'<div style="display: flex; align-items: flex-start; gap: 4px; margin-top: 8px; padding: 0 2px;">'
                      f'<span style="font-size: 11.5px; line-height: 1.5; color: {C["INK3"]};">{IMPORT_NOTE}</span>{imark(1)}</div>'),
    sheet_footer('취소', '이 내용으로 적용'),
    sticky=f'<div style="padding: 12px 18px; background: {C["INSET"]}; border-top: 1px solid {C["LINE"]}; flex-shrink: 0;">{checkbox_on}</div>', scrim_h=8, h=884)
# 앱 가져오기 창은 거의 온 높이 시트라 위 어두운 띠에 「배경을 눌러 닫기」 글이 없다(지도 ImportBackupNotes · language-ia-11) — 8px 띠만 남긴다
import_sheet = swap(import_sheet, '<span style="font-size: 11.5px; font-weight: 500; color: rgba(255,255,255,.62);">배경을 눌러 닫기</span>', '')
import_left = f'<div style="width: 390px; flex-shrink: 0; border-radius: 24px; overflow: hidden;">{import_sheet}</div>'

# ② 백업 — 설정 시트의 `데이터` 구역(D5 · tasks-10 #1): 저장 방식 한 줄 · 백업 내보내기 · 백업 불러오기 · 모든 데이터 지우기. 내보낸 결과는 시트 안에 한 줄.
# 예전 안내 상자(확인 표시 · 분류 안 함 표시도 함께 저장돼요 …)는 앱에 없다 — 앱에 넣을지는 확인할 것(CHANGED).
backup_part = (f'<div style="background: {C["SURF"]}; border: 1px solid {C["LINE"]}; border-radius: 18px; padding: 14px;">'
               + group('데이터', f'<div style="font-size: 12px; line-height: 1.45; color: {C["INK3"]}; margin-bottom: 9px;">이 기기에 암호화해 저장해요</div>'
                                 f'<div style="display: flex; gap: 8px;">'
                                 f'{btn("백업 내보내기", "secondary", "download", h=44).replace("width: 100%;", "flex: 1;")}'
                                 f'{btn("백업 불러오기", "secondary", "upload", h=44).replace("width: 100%;", "flex: 1;")}</div>'
                                 f'<div style="display: flex; align-items: center; gap: 6px; margin-top: 8px; font-size: 12px; color: {C["POS"]};">{icon("check", 13, C["POS"], 2.6)}백업 파일을 저장했어요</div>'
                                 f'<div style="margin-top: 10px;">{btn("모든 데이터 지우기", "danger", "refresh", h=44)}</div>')
               + '</div>')
# ③ 가져온 소비가 `안 썼어요` 날에 들어갔을 때 — 달력 카드의 상태 줄 자리에 중립 안내(# 제안 — 놓이는 자리 · 모양)
uncheck_part = (f'<div style="background: {C["SURF"]}; border: 1px solid {C["LINE"]}; border-radius: 18px; padding: 12px 14px;">'
                f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 10px; padding: 10px 12px; background: {C["INSET"]}; border-radius: 12px;">'
                f'<span style="font-size: 13px; color: {C["INK"]}; white-space: nowrap;">{UNCHECK_NOTE}</span>'
                f'<span style="font-size: 12.5px; font-weight: 600; color: {C["BRAND"]}; white-space: nowrap; flex-shrink: 0;">다시 표시</span></div></div>')


def path_row(name, mark_txt, check_txt, last=False):
    bb = '' if last else f' border-bottom: 1px solid {C["LINE_ROW"]};'
    return (f'<div style="display: flex; gap: 10px; padding: 9px 0;{bb}"><span style="width: 96px; flex-shrink: 0; font-size: 12.5px; font-weight: 600; color: {C["INK"]};">{name}</span>'
            f'<span style="flex: 1; min-width: 0; font-size: 12px; line-height: 1.5; color: {C["INK2"]};">{mark_txt}</span>'
            f'<span style="flex: 1; min-width: 0; font-size: 12px; line-height: 1.5; color: {C["INK2"]};">{check_txt}</span></div>')


path_table = (f'<div style="background: {C["SURF"]}; border: 1px solid {C["LINE"]}; border-radius: 18px; padding: 10px 18px 6px;">'
              f'<div style="display: flex; gap: 10px; padding: 2px 0 6px; border-bottom: 1px solid {C["LINE"]};"><span style="width: 96px; flex-shrink: 0; font-size: 11.5px; font-weight: 600; color: {C["INK3"]};">경로</span>'
              f'<span style="flex: 1; font-size: 11.5px; font-weight: 600; color: {C["INK3"]};">카테고리 없음 표시</span><span style="flex: 1; font-size: 11.5px; font-weight: 600; color: {C["INK3"]};">확인 표시(다 적었어요 · 안 썼어요)</span></div>'
              + path_row('전체 복원', '그대로 돌아옵니다', '그대로 돌아옵니다')
              + path_row('골라서 가져오기', '새로 추가된 기록의 표시만 따라옵니다. 이미 있어 건너뛴 기록에는 씌우지 않습니다', '오지 않습니다. 소비가 새로 들어간 날짜의 지금 확인만 풀립니다')
              + path_row('같은 파일을 다시', '사용자가 뺀 표시를 되살리지 않습니다', '바뀌지 않습니다', last=True) + '</div>')
ib_memo = memo_box([
    (1, f'가져오기 화면 — 확인 칸 바로 위 회색 글 한 줄(두 줄로 접힘 · 적용 후 · 백업 설정 · 순자산 목적지 안내 다음). 「합치기」는 값이 다른 기록을 덮어쓰지 않습니다(기존 유지).'),
    (2, f'백업은 설정 시트 › 데이터에서 합니다. 내보낸 결과(「백업 파일을 저장했어요」 · 실패하면 「백업 파일을 저장하지 못했습니다. 다시 시도해 주세요.」)는 시트 안에 한 줄로 남습니다. 저장 방식 한 줄은 폰 「이 기기에 암호화해 저장해요」 · 웹 「이 브라우저에만 저장해요」.'),
    (3, f'가져온 소비가 안 썼어요로 표시한 날에 들어가면 그 날의 표시가 풀리고, 달력 카드에서 {code("9월 5일 표시가 풀렸어요 · 다시 표시")}로 알립니다. 의미색 없이 중립 상자입니다.')])
ib_right = (f'<div style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 22px;">'
            f'<div style="display: grid; grid-template-columns: repeat(2, 362px); gap: 22px 20px; align-items: start;">'
            + case(2, '백업을 내보내는 자리 — 설정 › 데이터', '결과는 시트 안에 한 줄로 남습니다.', backup_part)
            + case(3, '가져온 뒤 — 표시가 풀린 날', '안 썼어요로 표시한 날에 소비가 들어왔을 때.', uncheck_part)
            + '</div>'
            + f'<div style="display: flex; flex-direction: column; gap: 8px;"><div style="font-size: 14px; font-weight: 700; letter-spacing: -0.01em; color: {C["INK"]};">경로마다 돌아오는 것</div>{path_table}</div>'
            + ib_memo + '</div>')
IB_W, IB_H = 1230, 1103      # DZ4 검토 — 자연 1079 + 24(가져오기 창 884 · 위 「배경을 눌러 닫기」 띠 뺌 · 백업 설정 줄 · 목적지 안내)
w('ImportBackupNotes', spec_frame(
    IB_W, IB_H, '가져오기 · 백업 — 확인 표시와 카테고리 없음 표시가 어떻게 따라오는지',
    '달력의 확인 표시(다 적었어요 · 안 썼어요)와 카테고리 없음 표시는 백업 파일에 함께 들어갑니다. 전체 복원과 골라서 가져오기가 다르게 돌려주므로 가져오기 화면에 그 사실을 적습니다.',
    f'<div style="display: flex; gap: 32px; align-items: flex-start;">{import_left}{ib_right}</div>', sub_w=860), keep_all=True)

# ══════════════════════════════════════════════════════════════
# 7. 새 장(2026-09-26 · DZ4) — PayoffStates · FutureStates · HomeGlanceRows · SampleModeTabs · DebtUnpayable
# ══════════════════════════════════════════════════════════════
VIO_B = C["VIO_STRONG"]


def vio_badge(text='저장되지 않는 가정'):
    return (f'<span style="display: inline-flex; align-items: center; gap: 4px; background: {C["VIO_SOFT"]}; color: {VIO_B}; font-size: 11.5px; font-weight: 600; '
            f'border-radius: 99px; padding: 4px 10px; white-space: nowrap;">{icon("spark", 11, VIO_B, 2.2)}{text}</span>')


def vio_card(inner, pad='14px'):
    return (f'<div style="background: {C["SURF"]}; border: 1.5px dashed {C["VIO_LINE"]}; border-radius: 18px; padding: {pad};">{inner}</div>')


def plain_card(inner, pad='14px'):
    return f'<div style="background: {C["SURF"]}; border: 1px solid {C["LINE"]}; border-radius: 18px; padding: {pad};">{inner}</div>'


def pay_compare(name, eta, months, interest, sel=None, reco=False, sub=None):
    """상환 방식 카드(Payoff 와 같은 틀) — sel = None | 'brand'(저장된 계획) | 'vio'(초안)."""
    col = {'brand': C["BRAND"], 'vio': C["VIO"]}.get(sel)
    bd = f'1.5px solid {col}' if col else f'1px solid {C["LINE"]}'
    bg = {'brand': C["BRAND_SOFT"], 'vio': C["VIO_SOFT"]}.get(sel, C["SURF"])
    tag = (f'<span style="background: {col or C["BRAND"]}; color: #FFFFFF; font-size: 10px; font-weight: 700; border-radius: 6px; padding: 3px 6px; flex-shrink: 0;">추천</span>') if reco else ''
    subl = f'<div style="font-size: 11px; line-height: 1.4; color: {C["INK3"]};">{sub}</div>' if sub else f'<div style="font-size: 11px; color: {C["INK3"]};">{months}</div>'
    return (f'<div style="flex: 1; min-width: 0; padding: 12px; border-radius: 14px; border: {bd}; background: {bg};">'
            f'<div style="display: flex; align-items: center; gap: 5px;"><span style="font-size: 13px; font-weight: 700; white-space: nowrap; color: {col or C["INK"]};">{name}</span>{tag}</div>'
            f'<div style="font-size: 11.5px; color: {C["INK3"]}; margin-top: 8px;">다 갚는 달</div>'
            f'<div style="font-size: 15px; font-weight: 600; letter-spacing: -0.02em; color: {C["INK"]};">{eta}</div>{subl}'
            f'<div style="font-size: 11.5px; color: {C["INK3"]}; margin-top: 8px;">총이자</div>'
            f'<div style="font-size: 15px; font-weight: 600; letter-spacing: -0.02em; color: {C["INK"] if interest != "—" else C["INK4"]};">{interest}</div></div>')


def info_lines(lines):
    body = ''.join(f'<span>{t}</span>' for t in lines)
    return (f'<div style="display: flex; gap: 8px; padding: 10px 11px; background: {C["INSET"]}; border-radius: 12px; margin-top: 10px;">'
            f'<span style="flex-shrink: 0; margin-top: 1px;">{icon("info", 14, C["INK3"], 1.9)}</span>'
            f'<div style="display: flex; flex-direction: column; gap: 3px; font-size: 11.5px; line-height: 1.5; color: {C["INK3"]};">{body}</div></div>')


def slider_ends(right='월 200만원'):
    return (f'<div style="display: flex; justify-content: space-between; margin-top: 5px;"><span style="font-size: 11px; color: {C["INK4"]};">최소 상환만</span>'
            f'<span style="font-size: 11px; color: {C["INK4"]};">{right}</span></div>')


B2 = lambda t: f'<span style="font-weight: 700; color: {C["INK2"]};">{t}</span>'
Q = lambda t: f'<p style="margin: 10px 0 0; font-size: 15px; font-weight: 600; letter-spacing: -0.015em; color: {C["INK"]};">{t}</p>'

# ── PayoffStates · 미래 › 상환 계획의 경우들(NUMBERS §10 · 앱 payoff-plan) ──
draft_slider = vio_card(
    vio_badge() + Q('월 추가 상환을 얼마나 할까요?')
    + f'<div style="display: flex; align-items: baseline; gap: 6px; margin-top: 8px;"><span style="font-size: 14px; color: {C["INK3"]};">15만원</span>'
      f'<span style="font-size: 14px; color: {VIO_B};">→</span><span style="font-size: 25px; font-weight: 700; letter-spacing: -0.03em; color: {VIO_B};">20</span>'
      f'<span style="font-size: 15px; font-weight: 600; color: {VIO_B};">만원</span></div>'
    + f'<div style="font-size: 12.5px; font-weight: 600; color: {VIO_B}; margin-top: 4px;">최소 77만원 + 추가 20만원 = 매월 97만원</div>'
    + f'<div style="font-size: 12.5px; color: {C["INK2"]}; margin-top: 10px;">지금 계획에서 매달 남는 돈 약 90만원</div>'
    + f'<div style="margin-top: 8px;">{slider(10, C["VIO"])}</div>' + slider_ends()
    + f'<div style="font-size: 12px; line-height: 1.5; color: {C["INK3"]}; margin-top: 8px;">저축 · 상환 계획까지 지키려면 152만원 → 147만원 안에서 쓰면 돼요<br>소비 목표 216만원(월급의 60%)은 그대로예요</div>'
    + info_lines(['월 최소 상환액 77만원은 줄일 수 없어 슬라이더에서 뺐어요.']))      # 앱: 초안에도 참고 줄 아래 안내 상자가 남는다(2026-09-27 fix-up 3)
draft_compare = plain_card(
    f'<div style="display: flex; gap: 8px;">{pay_compare("고금리 우선", "2035년 9월", "9년 뒤", "1,614만원", sel="vio", reco=True)}{pay_compare("소액 우선", "2035년 10월", "9년 1개월 뒤", "1,643만원")}</div>'
    + info_lines(['고금리 우선이 이자를 30만원 덜 내고 1개월 먼저 끝나요', '추가 상환이 없으면 2038년 10월 · 이자 2,248만원', B2('3년 1개월 빨리 끝나고 이자 634만원 덜 내요')]), pad='13px 14px')
draft_save = plain_card(
    f'<div style="font-size: 14px; font-weight: 600; color: {C["INK"]};">이 계획을 저장할까요?</div>'
    f'<div style="font-size: 11.5px; line-height: 1.5; color: {C["INK3"]}; margin-top: 3px;">저장해야 홈 · 자산 경로 · 목적지 계산에 반영돼요.</div>'
    f'<div style="display: flex; gap: 8px; margin-top: 11px;">{btn("가정 종료", "secondary", h=44).replace("width: 100%;", "flex: 1;")}{btn("상환 계획 저장", "primary", h=44).replace("width: 100%;", "flex: 1.4;")}</div>')
payoff_draft = f'<div style="display: flex; flex-direction: column; gap: 10px;">{draft_slider}{draft_compare}{draft_save}</div>'

unpay_slider = plain_card(
    f'<div>{badge("저장된 계획", "pos", "check")}</div>' + Q('월 추가 상환을 얼마나 할까요?')
    + f'<div style="display: flex; align-items: baseline; gap: 2px; margin-top: 8px;"><span style="font-size: 25px; font-weight: 700; letter-spacing: -0.03em;">20</span><span style="font-size: 15px; font-weight: 600; color: {C["INK2"]};">만원</span></div>'
    + f'<div style="font-size: 12.5px; font-weight: 600; color: {C["INK2"]}; margin-top: 4px;">최소 — + 추가 20만원 = 매월 —</div>')
unpay_compare = plain_card(
    f'<div style="display: flex; gap: 8px;">{pay_compare("고금리 우선", "다 갚지 못해요", None, "—", sel="brand", sub="잔액이 늘어요")}{pay_compare("소액 우선", "다 갚지 못해요", None, "—", sub="잔액이 늘어요")}</div>'
    # 앱: 매달 이자 문장은 방식 카드 아래 보통 한 줄, 상자에는 까닭 · 기준선 두 줄만(2026-09-27 fix-up 3)
    + f'<div style="font-size: 12px; line-height: 1.5; color: {C["INK2"]}; margin-top: 10px;">매달 이자가 약 300,000원이에요. 이보다 많이 갚아야 잔액이 줄어요.</div>'
    + info_lines([f'전세자금대출은 월 30만원보다 많이 내야 줄어요 · <span style="font-weight: 600; color: {C["BRAND"]};">부채 수정 &rsaquo;</span>',
                  '추가 상환이 없으면 지금 조건으로는 다 갚지 못해요']), pad='13px 14px')
payoff_unpay = f'<div style="display: flex; flex-direction: column; gap: 10px;">{unpay_slider}{unpay_compare}</div>'

minonly = plain_card(
    f'<div>{badge("저장된 계획", "pos", "check")}</div>' + Q('월 추가 상환을 얼마나 할까요?')
    + f'<div style="display: flex; align-items: baseline; gap: 2px; margin-top: 8px;"><span style="font-size: 25px; font-weight: 700; letter-spacing: -0.03em;">0</span><span style="font-size: 15px; font-weight: 600; color: {C["INK2"]};">만원</span></div>'
    + f'<div style="font-size: 12.5px; font-weight: 600; color: {C["INK2"]}; margin-top: 4px;">최소 상환만 매월 77만원</div>'
    + f'<div style="display: flex; margin-top: 12px;">{pay_compare("최소 상환만", "2039년 3월", "12년 6개월 뒤", "2,662만원", sel="brand")}</div>'      # 앱 카드는 「N년 N개월 뒤」만(2026-09-27 fix-up)
    + f'<div style="font-size: 11.5px; line-height: 1.5; color: {C["INK3"]}; margin-top: 6px;">고금리 우선 · 소액 우선 카드는 그 위에 그대로 있고, 셋째 카드로 골라 둔 모습입니다.</div>'
    + info_lines(['예전 버전에서 고른 설정이에요. 방식을 고르고 저장하면 바뀌어요.']))

short_slider = vio_card(
    vio_badge() + Q('월 추가 상환을 얼마나 할까요?')
    + f'<div style="display: flex; align-items: baseline; gap: 6px; margin-top: 8px;"><span style="font-size: 14px; color: {C["INK3"]};">15만원</span>'
      f'<span style="font-size: 14px; color: {VIO_B};">→</span><span style="font-size: 25px; font-weight: 700; letter-spacing: -0.03em; color: {VIO_B};">150</span>'
      f'<span style="font-size: 15px; font-weight: 600; color: {VIO_B};">만원</span></div>'
    + f'<div style="font-size: 12.5px; font-weight: 600; color: {VIO_B}; margin-top: 4px;">최소 77만원 + 추가 150만원 = 매월 227만원</div>'
    + f'<div style="font-size: 12.5px; color: {C["INK2"]}; margin-top: 10px;">지금 계획에서 매달 남는 돈 약 90만원</div>'
    + f'<div style="margin-top: 8px;">{slider(75, C["VIO"])}</div>' + slider_ends()
    + f'<div style="margin-top: 8px;">{note("매달 45만원이 모자라 모아 둔 돈에서 꺼내 써요", "warn", "warn")}</div>'      # 앱 payoff-plan: 슬라이더 끝 글자 뒤 · 참고 줄 앞(2026-09-27 fix-up)
    + f'<div style="font-size: 12px; line-height: 1.5; color: {C["INK3"]}; margin-top: 8px;">저축 · 상환 계획까지 지키려면 152만원 → 49만원 안에서 쓰면 돼요<br>소비 목표 216만원(월급의 60%)은 그대로예요</div>'
    + info_lines(['월 최소 상환액 77만원은 줄일 수 없어 슬라이더에서 뺐어요.']))      # 앱: 초안에도 참고 줄 아래 안내 상자가 남는다(2026-09-27 fix-up 3)

cap_rows = ''.join(
    f'<div style="font-size: 12.5px; line-height: 1.5; color: {C["INK2"]}; padding: 8px 0; {"border-top: 1px solid " + C["LINE_ROW"] + ";" if i else ""}">{t}</div>'
    for i, t in enumerate(['지금 계획에서 매달 남는 돈 약 90만원',
                           '지금 계획에서도 매달 45만원이 모자라요',
                           '지금 계획에서 매달 남는 돈 — · 소비 기록 후 계산해요',
                           '지금 계획에서 매달 남는 돈 — · 지난달 마감 뒤 계산해요',
                           f'월급을 넣으면 매달 남는 돈을 계산해요 · <span style="font-weight: 600; color: {C["BRAND"]};">월급 입력하기 &rsaquo;</span>']))
cap_card = plain_card(cap_rows, pad='6px 14px')
# 시안 사용자는 두 방식이 갈린다 — 같은 결과는 앱 샘플 부채(카드 할부 · 마이너스통장 · 전세자금대출 · 월 추가 30만원)의 값 그대로(앱 Payoff--demo-tie).
# 카드에는 실제 달 · 기간 · 이자를 쓰고(「같은 달」 같은 자리 글자 없음) 추천 칩만 없다.
tie_card = plain_card(f'<div style="display: flex; gap: 8px;">{pay_compare("고금리 우선", "2034년 7월", "7년 10개월 뒤", "1,333만원", sel="brand")}{pay_compare("소액 우선", "2034년 7월", "7년 10개월 뒤", "1,333만원")}</div>'
                      + info_lines(['두 방식 모두 카드 할부 → 마이너스통장 → 전세자금대출 순서라 결과가 같아요', '추가 상환이 없으면 2038년 3월 · 이자 1,996만원',
                                    B2('3년 8개월 빨리 끝나고 이자 663만원 덜 내요')]), pad='13px 14px')

PAY_MEMO = memo_box([
    (1, f'초안 — 슬라이더나 방식을 저장된 계획과 다르게 바꾼 동안만 보라 점선 + {code("저장되지 않는 가정")}. 예전 값은 회색 작게 · 새 값은 보라 크게, 풀이 줄도 보라. 고른 카드도 보라. 오른쪽 위 {code("되돌리기")}는 없고 맨 아래 {code("가정 종료")} · {code("상환 계획 저장")}.'),
    (2, f'다 갚지 못할 때(월 최소 상환액을 넣지 않은 부채) — 다 갚는 달 {code("다 갚지 못해요")} · 총이자 {code("—")} · {code("추천")} 없음 · 까닭(매달 이자)과 {code("부채 수정 ›")}. 계산할 수 없는 이자는 보이지 않습니다.'),
    (3, f'예전 버전의 {code("최소 상환만")}을 고른 사람 — 셋째 카드로 골라 두고 {code("예전 버전에서 고른 설정이에요 …")}. 기준선이 아니라 저장된 방식입니다.'),
    (4, f'매달 남는 돈이 모자라면 슬라이더 위에 주황 한 줄. 참고 줄은 늘 회색이고 판정이 아닙니다 — 목적지 필요액이 가처분의 70%로 잘려 49만원이 됩니다.'),
    (5, f'두 방식의 다 갚는 달이 같고 이자 차이가 1만원 안이면 {code("추천")} 없이 순서를 말합니다(앱 샘플 부채 예). 저장된 계획은 파란 카드 · 초록 {code("저장된 계획")} 배지(보라 아님).')])
payoff_states = (f'<div style="display: flex; gap: 24px; align-items: flex-start;">'
                 + col(362, [case(1, '초안 — 15만원에서 20만원으로 밀었을 때', '저장 전이라 보라 점선 · 저장 칸이 열립니다.', payoff_draft)])
                 + col(362, [case(2, '다 갚지 못할 때', '예: 전세자금대출 1억 · 연 3.6% · 월 최소 상환액 빈칸 · 월 추가 20만원.', payoff_unpay),
                             case(3, '예전에 최소 상환만을 고른 사람', '셋째 카드로 저장된 방식을 보여 줍니다.', minonly)])
                 + col(362, [case(4, '매달 남는 돈이 모자라는 초안', '월 추가 150만원 — 매달 45만원 모자람.', short_slider),
                             case(4, '슬라이더 위 한 줄의 경우들', '월급 · 기록 · 마감이 없으면 금액 대신 까닭.', cap_card),
                             case(5, '두 방식의 결과가 같을 때', '추천 없이 갚는 순서를 말합니다. 예: 앱 샘플 부채 · 월 추가 30만원.', tie_card)])
                 + '</div>' + PAY_MEMO)
PAY_W, PAY_H = 1230, 1501      # 2026-09-27 fix-up 3 자연 1477 + 24(초안 둘에 최소 상환 안내 상자) · 자연 1422 + 24(DZ4 검토 — 같은 결과 카드에 앱 샘플 값 · 풀이 세 줄)
w('PayoffStates', spec_frame(PAY_W, PAY_H, '미래 › 상환 계획 — 초안 · 다 갚지 못함 · 최소 상환만 · 모자람',
                             '저장된 계획(Payoff 장)에서 슬라이더나 방식을 바꾸면 초안이 됩니다. 숫자는 시안 사용자의 저장된 계획(고금리 우선 · 월 추가 15만원)에서 출발합니다.',
                             payoff_states, sub_w=860), keep_all=True)


# ── FutureStates · 미래 › 자산 경로의 경우들(NUMBERS §11 · future-1/2/5/11/12/19/21) ──
FUT_VAL = lambda v, col=None, unit='억원': (f'<span style="font-size: 13px; font-weight: 500; color: {C["INK2"]};">약</span>'
                                          f'<span style="font-size: 33px; font-weight: 700; letter-spacing: -0.04em; line-height: 1.05; color: {col or C["INK"]};">{v}</span>'
                                          f'<span style="font-size: 17px; font-weight: 600; color: {col or C["INK2"]};">{unit}</span>')


def fut_top(val_html, right_label, right_val, right_col=None, pre=''):
    return (f'{pre}<div style="display: flex; align-items: flex-end; justify-content: space-between; gap: 10px;">'
            f'<div><div style="font-size: 11px; font-weight: 600; letter-spacing: 0.06em; color: {C["INK3"]};">10년 뒤 순자산</div>'
            f'<div style="display: flex; align-items: baseline; gap: 3px; margin-top: 3px;">{val_html}</div></div>'
            f'<div style="display: flex; flex-direction: column; align-items: flex-end; gap: 1px; padding-bottom: 3px;">'
            f'<span style="font-size: 11px; font-weight: 500; color: {C["INK3"]}; white-space: nowrap;">{right_label}</span>'
            f'<span style="font-size: 15px; font-weight: 600; letter-spacing: -0.02em; color: {right_col or C["POS"]}; white-space: nowrap;">{right_val}</span></div></div>')


# 가정 15만(앱 하네스 · naviProject spendDelta 150,000 · 2026-09-27 fix-up 3): 10년 뒤 보통 404,948,913원(약 4.05억) · 늘어나는 폭 311,448,913 → 약 3.11억 · 10년 뒤 차이 +약 2,300만원 ·
# 범위(나쁠 때 ~ 좋을 때) 297,327,160 ~ 577,850,663 → 2.97억 ~ 5.78억. 앱은 가정이 있으면 보라 점선 경로 하나 + 범위 띠(보통 초록 선 없음) · 범례 「가정 · 범위」 · 해 축 6개 · 금액 눈금(Future 그래프와 같은 축).
# 보라 점선 상자는 큰 숫자 부분만 두른다(카드 전체가 아님 · 앱 future-view).
CUT_BASE = [93_500_000, 118_110_561, 144_081_502, 171_450_846, 200_297_680, 230_631_966, 262_380_645, 295_611_189, 330_396_139, 366_811_736, 404_948_913]
CUT_BAD = [93_500_000, 111_941_256, 130_861_861, 150_252_500, 170_142_408, 190_489_051, 211_164_075, 232_176_706, 253_538_122, 275_259_914, 297_327_160]
CUT_GOOD = [93_500_000, 125_254_871, 159_903_239, 197_698_818, 238_963_296, 283_979_371, 332_980_445, 386_378_209, 444_631_669, 508_250_817, 577_850_663]
_fx = lambda i: 10 + i * 34.2                      # Future 그래프와 같은 좌표(362 × 150 · 1억 = 19.33px · 바닥 132)
_fy = lambda v: 132 - v / 1e8 * (116 / 6)
path = lambda pts: 'M' + ' L'.join(f'{x:.1f} {y:.1f}' for x, y in pts)
_pb = [(_fx(i), _fy(v)) for i, v in enumerate(CUT_BASE)]
_band = [(_fx(i), _fy(v)) for i, v in enumerate(CUT_GOOD)] + [(_fx(i), _fy(v)) for i, v in reversed(list(enumerate(CUT_BAD)))]
YEARS = ''.join(f'<text x="{_fx(i):.1f}" y="146" text-anchor="{"start" if i == 0 else ("end" if i == 10 else "middle")}" font-size="11"{" font-weight=" + chr(34) + "600" + chr(34) if i == 10 else ""} fill="{"#475467" if i == 10 else "#697182"}">{2026 + i}</text>' for i in range(0, 11, 2))
cut_svg = (f'<svg width="334" height="138" viewBox="0 0 362 150" fill="none" style="display: block; width: 100%; height: auto; margin-top: 8px;">'
           f'<defs><linearGradient id="cutfill" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="{C["VIO"]}" stop-opacity="0.22"/><stop offset="100%" stop-color="{C["VIO"]}" stop-opacity="0"/></linearGradient></defs>'
           + ''.join(f'<line x1="10" y1="{_fy(v * 1e8):.1f}" x2="352" y2="{_fy(v * 1e8):.1f}" stroke="#EDF0F7" stroke-width="1"/><text x="12" y="{_fy(v * 1e8) - 4:.1f}" font-size="11" fill="#B9C3D6">{v}억</text>' for v in (2, 4, 6))
           + f'<path d="{path(_band)} Z" fill="{C["VIO"]}" fill-opacity="0.13"/>'
           f'<path d="{path(_pb)} L352.0 132.0 L10.0 132.0 Z" fill="url(#cutfill)"/>'
           f'<path d="{path(_pb)}" stroke="{C["VIO"]}" stroke-width="2.8" stroke-dasharray="6 5" stroke-linecap="round" stroke-linejoin="round"/>'
           f'<circle cx="10" cy="{_pb[0][1]:.1f}" r="3.6" fill="{C["VIO"]}"/><text x="16" y="127.9" font-size="12" font-weight="600" fill="#475467">오늘 9,350만</text>'
           f'<circle cx="352" cy="{_pb[-1][1]:.1f}" r="4" fill="{C["VIO"]}"/><circle cx="352" cy="{_pb[-1][1]:.1f}" r="7.5" fill="{C["VIO"]}" fill-opacity="0.16"/>'
           f'<line x1="10" y1="132" x2="352" y2="132" stroke="#E3E8F1" stroke-width="1"/>{YEARS}</svg>')
LEG_DASH = f'<span style="width: 14px; height: 0; border-top: 2.6px dashed {C["VIO"]}; flex-shrink: 0;"></span>'
LEG_BAND = f'<span style="width: 14px; height: 9px; border-radius: 3px; background: {C["VIO"]}; opacity: .22; flex-shrink: 0;"></span>'
FUT_FOOT = (f'<p style="margin: 7px 0 0; padding: 0 2px; font-size: 11.5px; line-height: 1.45; color: {C["INK3"]};">물가 · 세금은 빼고 계산했어요 · '
            f'<span style="font-weight: 600; color: {C["BRAND"]};">자세히 &rsaquo;</span></p>')
cut_hero = plain_card(
    f'<div style="border: 1px dashed {C["VIO_LINE"]}; border-radius: 14px; padding: 12px;">'
    f'<div style="margin-bottom: 8px;">{vio_badge()}</div>'
    + fut_top(FUT_VAL('4.05', VIO_B), '지금 9,350만원 대비', '↑ 약 3.11억원', VIO_B)
    + f'<div style="font-size: 12px; line-height: 1.5; color: {C["INK2"]}; margin-top: 6px;">월 15만원 절감 가정 · 원래 약 3.82억원 · <span style="font-weight: 600; color: {VIO_B}; white-space: nowrap;">가정 종료</span></div></div>'
    + cut_svg
    + f'<div style="display: flex; align-items: center; gap: 12px; margin-top: 6px; padding: 0 2px; font-size: 11px; color: {C["INK2"]};">'
      f'<span style="display: inline-flex; align-items: center; gap: 5px;">{LEG_DASH}가정 4.05억</span>'
      f'<span style="display: inline-flex; align-items: center; gap: 5px;">{LEG_BAND}범위 2.97억 ~ 5.78억</span></div>'
    + FUT_FOOT)
def cut_slider(pct, col, right, fill=None):
    """절감 카드 조절 줄 — 앱 .future-cut-control(390 폭): 「0원 [슬라이더] 45만원」 한 줄 · 사이 9 · 6 아래 · 손잡이 20(Radix 안쪽 맞춤 = pct × (폭 − 20))
    (2026-09-27 fix-up 5 · 예전 양끝 글자가 슬라이더 아래 따로 한 줄 — Future 장과 같게)."""
    kl = f'calc({pct}% - {pct * 20 / 100:.2f}px)'
    fl = (f'<div style="position: absolute; left: 0; width: calc({pct}% - {pct * 20 / 100:.2f}px + 10px); top: 8px; height: 5px; border-radius: 99px; background: {fill};"></div>' if fill and pct > 0 else '')
    return (f'<div style="display: flex; align-items: center; gap: 9px; margin-top: 6px;">'
            f'<span style="font-size: 11px; color: {C["INK4"]}; white-space: nowrap; flex-shrink: 0;">0원</span>'
            f'<div style="position: relative; height: 20px; flex: 1; min-width: 0;">'
            f'<div style="position: absolute; left: 0; right: 0; top: 8px; height: 5px; border-radius: 99px; background: {C["TRACK"]};"></div>{fl}'
            f'<div style="position: absolute; left: {kl}; top: 0; width: 20px; height: 20px; border-radius: 99px; background: #FFFFFF; border: 2.5px solid {col}; box-shadow: 0 2px 6px rgba(16,24,40,.2);"></div></div>'
            f'<span style="font-size: 11px; color: {C["INK4"]}; white-space: nowrap; flex-shrink: 0;">{right}</span></div>')


CUT_FOOTNOTE = f'<div style="font-size: 11.5px; line-height: 16.675px; color: {C["INK3"]}; margin-top: 8px;">줄인 만큼은 모두 매달 모으는 돈에 더한다고 봐요.</div>'      # 앱 .future-cut-footnote 8 아래
cut_card = vio_card(
    f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px;">{vio_badge()}<span style="font-size: 13px; font-weight: 700; color: {VIO_B}; white-space: nowrap;">10년 뒤 +약 2,300만원</span></div>'
    + Q('월 소비를 15만원 줄이면 얼마나 달라질까요?')
    + cut_slider(33.3, C["VIO"], '45만원', C["VIO"])
    + CUT_FOOTNOTE
    + f'<div style="display: flex; align-items: center; gap: 6px; margin-top: 10px; padding-top: 10px; border-top: 1px solid {C["LINE_ROW"]}; font-size: 12px; color: {C["INK2"]};">'
      f'다음 자산 지점 카드 제목 옆 {chip_sm("가정 반영")}</div>')
cut_zero = plain_card(
    f'<div style="display: flex; align-items: center; justify-content: flex-end; min-height: 25px;"><span style="font-size: 13px; font-weight: 600; color: {C["INK2"]}; white-space: nowrap;">10년 뒤 +0원</span></div>'
    + f'<p style="margin: 7px 0 0; font-size: 13.5px; font-weight: 600; letter-spacing: -0.015em; color: {C["INK"]};">한 달에 얼마를 아끼면? 밀어서 시험해 보세요</p>'
    + cut_slider(0, C["BRAND"], '45만원')
    + CUT_FOOTNOTE, pad='11px 14px')
# ② 소비 기록이 없을 때(앱 NEW-FutureNoSpending): 경로 카드(— · 중립 칸 · 각주) → 다음 자산 지점(값 —) → 절감 카드(보통 카드 · 「10년 뒤 —」 · 잠긴 슬라이더)
no_spend = plain_card(
    fut_top(f'<span style="font-size: 33px; font-weight: 700; color: {C["INK4"]};">—</span>', '지금 9,350만원 대비', '—', C["INK4"])
    + f'<div style="margin-top: 12px; padding: 14px; background: {C["INSET"]}; border-radius: 14px; text-align: center;">'
      f'<div style="font-size: 14px; font-weight: 600; color: {C["INK"]};">소비를 며칠 기록하면 경로를 그려요</div>'
      f'<div style="font-size: 12px; line-height: 1.5; color: {C["INK2"]}; margin-top: 4px;">월급에서 얼마가 남는지 알아야 앞으로의 자산을 계산할 수 있어요. 기록하지 않은 소비를 0원으로 보지 않아요.</div>'
      f'<div style="display: flex; justify-content: center; margin-top: 10px;">{btn("소비 기록하기", "secondary", h=40, full=False).replace("gap: 6px;", "gap: 6px; padding: 0 16px;", 1)}</div></div>'      # 앱 — 가운데 회색 보조 버튼
    + FUT_FOOT)
MILE_DASH = f'<span style="font-size: 13px; font-weight: 600; color: {C["INK4"]};">—</span>'
no_spend_mile = plain_card(
    f'<div style="display: flex; align-items: center; gap: 6px; padding-bottom: 4px;">{icon("pin", 15, C["BRAND"], 1.9)}<span style="font-size: 14px; font-weight: 600; color: {C["INK"]};">다음 자산 지점</span></div>'
    + ''.join(f'<div style="display: flex; align-items: center; justify-content: space-between; min-height: 40px; border-top: 1px solid {C["LINE_ROW"]};">'
              f'<span style="font-size: 13.5px; font-weight: 600; color: {C["INK"]};">{n}</span>{MILE_DASH}</div>' for n in ('1억원', '1억 5,000만원', '2억원')), pad='13px 14px 5px')
no_spend_cut = plain_card(
    f'<div style="display: flex; align-items: center; justify-content: flex-end; min-height: 25px;"><span style="font-size: 13px; font-weight: 600; color: {C["INK4"]}; white-space: nowrap;">10년 뒤 —</span></div>'
    + f'<p style="margin: 7px 0 0; font-size: 13.5px; font-weight: 600; letter-spacing: -0.015em; color: {C["INK"]};">소비를 기록하면 조정할 수 있어요</p>'
    + cut_slider(0, C["DIS"], '—')
    + CUT_FOOTNOTE, pad='11px 14px')
no_spend_all = f'<div style="display: flex; flex-direction: column; gap: 10px;">{no_spend}{no_spend_mile}{no_spend_cut}</div>'
# 이 사람은 전세자금대출 1억만 있다(월 최소 비움) — 순자산 = 1억 8,210만 − 1억 = 8,210만원(앱 NEW-FutureDebtGrowing · 2026-09-27 fix-up)
debt_grow = plain_card(
    fut_top(f'<span style="font-size: 33px; font-weight: 700; color: {C["INK4"]};">—</span>', '지금 8,210만원 대비', '—', C["INK4"])
    # 앱 .future-blocked-pane(c6b7de3 · 같은 상태): 가운데 정렬 블록 — 경고 그림 20 · 굵은 제목 15 / 600 / 21 · 본문 13 / 19.5 ink-3 · 「부채 수정 ›」 따로 버튼(44 · 안쪽 0 10 · 4 아래)
    # (2026-09-27 fix-up 5 · 예전 작은 주황 안내 상자에 그림 · 글 · 링크가 한 줄)
    + f'<div style="margin-top: 12px; display: flex; flex-direction: column; align-items: center; gap: 6px; padding: 16px 14px; background: {C["WARN_SOFT"]}; border-radius: 14px; text-align: center;">'
      f'{icon("warn", 20, C["WARN"], 2)}'
      f'<div style="font-size: 15px; font-weight: 600; line-height: 21px; color: {C["WARN_INK"]};">잔액이 늘어나는 대출이 있어 경로를 그릴 수 없어요</div>'
      f'<div style="font-size: 13px; line-height: 19.5px; color: {C["INK3"]};">전세자금대출은 월 30만원보다 많이 내야 줄어요.</div>'
      f'<div style="display: inline-flex; align-items: center; height: 44px; padding: 0 10px; margin-top: 4px; border-radius: 13px; background: {C["BG"]}; border: 1px solid {C["LINE"]}; '
      f'font-size: 12.5px; font-weight: 600; color: {C["WARN"]}; white-space: nowrap;">부채 수정 &rsaquo;</div></div>'
    + FUT_FOOT
    + f'<div style="margin-top: 10px; font-size: 12px; color: {C["INK3"]};">다음 자산 지점 카드는 없고, 절감 카드는 보통 카드 「부채 조건을 고치면 조정할 수 있어요」</div>')
draft_notice = (f'<div style="padding: 12px 14px; background: {C["WARN_SOFT"]}; border-radius: 14px; display: flex; flex-direction: column; gap: 4px;">'
                f'<span style="font-size: 13.5px; font-weight: 700; color: {C["WARN_INK"]};">저장 전 상환 가정으로 비교 중</span>'
                f'<span style="font-size: 12px; line-height: 1.5; color: {C["WARN_INK"]};">월 추가 20만원 · 고금리 우선. 저장된 계획은 아직 바뀌지 않았어요.</span>'
                f'<div style="margin-top: 6px;">{btn("상환 계획 확인", "secondary", h=40, size=13.5)}</div></div>')      # 앱 — 카드 안 온 폭 버튼
short_row = plain_card(
    f'<div style="display: flex; align-items: center; gap: 6px; font-size: 12px; font-weight: 600; color: {C["WARN_INK"]}; background: {C["WARN_SOFT"]}; border-radius: 10px; padding: 8px 10px;">'
    f'{icon("warn", 13, C["WARN"], 2)}매달 45만원 부족 · 모아 둔 돈을 꺼내 쓰는 경로예요</div>'
    f'<div style="margin-top: 10px; font-size: 12px; color: {C["INK3"]};">(상환 초안 월 추가 150만원을 들고 왔을 때 · 10년 뒤 순자산 줄 바로 위)</div>')
# ④ 자세히 두 칸을 연 모습(앱 future-view · 하네스 2026-09-27 fix-up 3): 투자 환경별 비교 · 전체 경로 / 계산 방법 자세히
def fold_head(t):
    return (f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px; padding-bottom: 10px; border-bottom: 1px solid {C["LINE"]};">'
            f'<span style="font-size: 13.5px; font-weight: 600; color: {C["INK"]};">{t}</span>'
            f'<span style="font-size: 18px; font-weight: 500; line-height: 1; color: {C["BRAND"]};">−</span></div>')


cmp_rows = ''.join(
    f'<div style="display: flex; align-items: center; gap: 8px; padding: 9px 0 9px {12 if on else 0}px; {"border-left: 3px solid " + C["POS"] + "; margin-left: 0;" if on else ""}'
    f'{"border-top: 1px solid " + C["LINE_ROW"] + ";" if i else ""}">'
    f'<div style="flex: 1; min-width: 0;"><div style="font-size: 12px; {"font-weight: 600; " if on else ""}color: {C["INK"] if on else C["INK2"]};">{n} · 앞으로 모을 돈 연 {r}</div>'
    f'<div style="font-size: 11.5px; {"font-weight: 600; " if on else ""}color: {C["INK"] if on else C["INK3"]}; margin-top: 2px;">지금보다 약 {d}억원 늘어요</div></div>'
    f'<div style="font-size: 14px; font-weight: 700; color: {C["INK"]}; white-space: nowrap;">약 {v}억원</div></div>'
    for i, (n, r, v, d, on) in enumerate([('나쁠 때', '-0.3%', '2.8', '1.86', False), ('보통', '5.0%', '3.82', '2.88', True), ('좋을 때', '10.5%', '5.47', '4.54', False)]))
# 부채 잔액(보통 · 월 추가 15만원 · 고금리 우선) — 8,860만 → 2036년 5월 0원(116개월 뒤 · naviProject debts)
DEBT_Y = [88_600_000, 81_204_055, 73_336_694, 65_006_861, 56_184_974, 46_913_239, 37_319_707, 27_394_863, 17_127_266, 6_505_078]
_dx = lambda m: 12 + m / 120 * 314
_dy = lambda v: 70 - v / 88_600_000 * 52
_dpts = [(_dx(i * 12), _dy(v)) for i, v in enumerate(DEBT_Y)] + [(_dx(116), _dy(0)), (_dx(120), _dy(0))]
debt_svg = (f'<svg width="334" height="92" viewBox="0 0 334 92" fill="none" style="display: block; width: 100%; height: auto; margin-top: 6px;">'
            f'<text x="12" y="13" font-size="11" fill="#697182">8,860만</text><text x="12" y="66" font-size="11" fill="#697182">0</text>'
            f'<line x1="12" y1="70" x2="326" y2="70" stroke="#E3E8F1" stroke-width="1"/>'
            f'<path d="{path(_dpts)}" stroke="{C["WARN"]}" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>'
            + ''.join(f'<text x="{_dx(i * 12):.1f}" y="86" text-anchor="{"start" if i == 0 else ("end" if i == 10 else "middle")}" font-size="11" fill="#697182">{2026 + i}</text>' for i in range(0, 11, 2))
            + '</svg>')
MILE_ROWS = [('1억원', '', '4개월 뒤 · 2027년 1월'), ('1억 5,000만원', '', '2년 5개월 뒤 · 2029년 2월'), ('2억원', '', '4년 4개월 뒤 · 2031년 1월'),
             ('3억원', '', '7년 8개월 뒤 · 2034년 5월'), ('4억원', '', '10년 안에 닿기 어려워요'), ('6억 2,520만원', '생활비 25년치', '10년 안에 닿기 어려워요')]
mile_list = ''.join(
    f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px; min-height: 36px; {"border-top: 1px solid " + C["LINE_ROW"] + ";" if i else ""}">'
    f'<span style="font-size: 13px; font-weight: 600; color: {C["INK"]}; white-space: nowrap;">{n}'
    + (f' <span style="font-size: 11px; font-weight: 500; color: {C["INK3"]};">{s}</span>' if s else '') + '</span>'
    f'<span style="font-size: 12px; color: {C["INK2"]}; white-space: nowrap;">{r}</span></div>'
    for i, (n, s, r) in enumerate(MILE_ROWS))
SUBH = lambda t, mt=14: f'<div style="font-size: 12.5px; font-weight: 600; color: {C["INK2"]}; margin-top: {mt}px;">{t}</div>'
extra_open = plain_card(
    fold_head('투자 환경별 비교 · 전체 경로')
    + f'<div style="font-size: 13px; font-weight: 700; color: {C["INK"]}; margin-top: 12px;">10년 뒤 투자 환경별 비교</div>{cmp_rows}'
    + SUBH('부채 잔액') + debt_svg
    + SUBH('순자산 지점', 10) + f'<div style="margin-top: 4px;">{mile_list}</div>'
    + f'<div style="font-size: 11.5px; line-height: 1.55; color: {C["INK3"]}; margin-top: 10px;">색칠한 띠는 나쁠 때 ~ 좋을 때 사이예요. 일어날 확률이 아니에요. '
      f'기간 · 투자 환경 · 소비 절감 · 저장 안 한 상환 가정은 다른 탭에 다녀와도 그대로이고, 앱을 닫으면 처음으로 돌아가요. 저장된 기록은 바뀌지 않아요.</div>', pad='13px 14px')
TILES = [('계산 기준일', '2026년 9월 8일'), ('최근 기록일', '2026년 9월 8일'), ('자산 갱신일', '2026년 9월 1일'), ('지금 자산', '1억 8,210만원 · 5개'),
         ('지금 부채', '8,860만원 · 4개'), ('예측 조건', '10년 · 보통 · 앞으로 모을 돈 연 5.0%'),
         ('앞으로 모을 돈의 수익률', '나쁠 때 -0.3% · 보통 5.0% · 좋을 때 10.5%'), ('지금 가진 자산의 평균 수익률', '연 2.4% · 자산마다 넣은 수익률로'),
         ('이번 달 월말 예상 소비', '208만원'), ('매달 모으는 돈', '90만원'), ('매달 추가 상환', '15만원')]
tiles = (f'<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 7px; margin-top: 12px;">'
         + ''.join(f'<div style="padding: 9px 10px; background: {C["INSET"]}; border-radius: 12px;"><div style="font-size: 11px; line-height: 1.4; color: {C["INK3"]};">{k}</div>'
                   f'<div style="font-size: 12.5px; font-weight: 700; line-height: 1.4; color: {C["INK"]}; margin-top: 3px;">{v}</div></div>' for k, v in TILES) + '</div>')
how_open = plain_card(
    fold_head('계산 방법 자세히') + tiles
    + f'<div style="font-size: 11.5px; line-height: 1.55; color: {C["INK3"]}; margin-top: 10px;">자산마다 넣은 수익률(없으면 종류별 기본값)로 계산해요. 지금의 월급 · 소비 · 모으는 돈 · 대출 금리가 그대로 이어진다고 봐요. '
      f'물가(연 2.5%) · 세금 · 수수료는 빼고 계산했어요. 모으는 돈이 모자란 달에는 투자 수익을 붙이지 않아요. 실제 수익이나 도착 시점을 보장하지 않아요.</div>', pad='13px 14px')
details = f'<div style="display: flex; flex-direction: column; gap: 10px;">{extra_open}{how_open}</div>'
FUTS_MEMO = memo_box([
    (1, f'절감 가정이 0원보다 클 때만 가정입니다 — 큰 숫자 부분을 보라 점선 상자로 두르고 {code("저장되지 않는 가정")} · {code("월 15만원 절감 가정 · 원래 약 3.82억원 · 가정 종료")}, 경로는 보라 점선 하나 + 범위 띠(보통 초록 선 없음) · 범례 {code("가정 4.05억 · 범위 2.97억 ~ 5.78억")}. 절감 카드도 보라 점선 · 배지. '
        f'0원이면 절감 카드는 보통 카드(실선 · 배지 없음 · {code("10년 뒤 +0원")} 기본 글자색 · 손잡이 파랑)이고 머리 줄 높이는 배지 자리 그대로라 움직여도 카드가 흔들리지 않습니다(2026-09-27 결정).'),
    (2, f'소비 기록이 없으면 경로를 그리지 않고 {code("—")} + 중립 칸 한 장(기록하지 않은 소비를 0원으로 보지 않음) · 다음 자산 지점은 값 {code("—")} · 절감 카드는 보통 카드 {code("10년 뒤 —")}와 잠긴 슬라이더. 잔액이 늘어나는 대출이 있으면 주황 칸 + {code("부채 수정 ›")}.'),
    (3, f'미래 › 상환 계획에서 저장하지 않은 초안을 들고 자산 경로로 오면 맨 위 주황 알림 {code("저장 전 상환 가정으로 비교 중")}. 매달 남는 돈이 모자라면 {code("매달 45만원 부족 · …")}.'),
    (4, f'두 칸을 모두 연 모습 — 투자 환경별 10년 뒤(모두 {code("약")} · 100만원 단위) · 부채 잔액(8,860만 → 2036년 5월 0) · 순자산 지점 여섯 줄 · 띠 설명, 그리고 계산 기준 열한 칸(날짜는 연도까지) · 계산 방법 문단.')])
future_states = (f'<div style="display: flex; gap: 24px; align-items: flex-start;">'
                 + col(362, [case(1, '절감 가정 15만원', '큰 숫자 상자와 경로가 보라 점선으로 바뀝니다. 위 기간 · 투자 환경 칩은 Future 장과 같아 뺐습니다.', cut_hero),
                             case(1, '절감 카드 — 15만원일 때', '머리에 10년 뒤 차이.', cut_card), case(1, '절감 카드 — 0원일 때(Future 장)', '보통 카드. 움직이는 순간 위처럼 바뀝니다.', cut_zero),
                             case(3, '저장 전 상환 초안을 들고 왔을 때', '맨 위 주황 알림.', draft_notice), case(3, '매달 남는 돈이 모자랄 때', '10년 뒤 순자산 위 한 줄.', short_row)])
                 + col(362, [case(2, '소비 기록이 없을 때', '경로 대신 기록하자는 칸 하나 · 지점은 — · 절감 카드는 보통 카드.', no_spend_all),
                             case(2, '잔액이 늘어나는 대출이 있을 때', '경로를 그리지 않고 까닭과 고칠 곳.', debt_grow)])
                 + col(362, [case(4, '자세히를 열었을 때', '투자 환경별 비교 · 전체 경로와 계산 방법 자세히 두 칸.', details)])
                 + '</div>' + FUTS_MEMO)
FUTS_W, FUTS_H = 1230, 1749      # 2026-09-27 fix-up 3 자연 1725 + 24(① 앱 그래프 · 0원 카드 · ② 지점 · 절감 카드 · ④ 두 칸 연 모습) · 자연 1360 + 24(DZ4 검토 — 「상환 계획 확인」 버튼 · 「소비 기록하기」 보조 버튼)
w('FutureStates', spec_frame(FUTS_W, FUTS_H, '미래 › 자산 경로 — 가정 · 기록 없음 · 늘어나는 대출 · 초안 · 자세히',
                             '기본(Future 장)은 절감 가정 0원입니다. 숫자는 시안 사용자 9월 8일(보통 5.0% · 10년 뒤 약 3.82억원).', future_states, sub_w=860), keep_all=True)


# ── HomeGlanceRows · 홈 `자산 한눈에` 줄 펼침(home-12 · NUMBERS §3) ──
def glance_row(label, value, open_=False, last=False, tag=None):
    t = f'<span style="font-size: 11px; font-weight: 600; color: {C["INK2"]}; background: {C["INSET"]}; border-radius: 99px; padding: 2px 7px;">{tag}</span>' if tag else ''
    bb = '' if last else f'border-bottom: 1px solid {C["LINE_ROW"]};'
    return (f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px; min-height: 48px; {bb}">'
            f'<span style="font-size: 13.5px; color: {C["INK"]};">{label}</span><span style="display: inline-flex; align-items: center; gap: 6px;">'
            f'<span style="font-size: 15px; font-weight: 700; color: {C["INK"]}; white-space: nowrap;">{value}</span>{t}{icon("up" if open_ else "down", 16, C["INK2"], 2)}</span></div>')


def glance_panel(lines, link):
    body = ''.join(f'<div style="font-size: 12.5px; line-height: 1.5; color: {C["INK2"] if i == 0 else C["INK3"]}; margin-top: {0 if i == 0 else 4}px;">{t}</div>' for i, t in enumerate(lines))
    return (f'<div style="padding: 2px 0 12px; border-bottom: 1px solid {C["LINE_ROW"]};">{body}'
            f'<div style="font-size: 12.5px; font-weight: 600; color: {C["BRAND"]}; margin-top: 6px;">{link} &rsaquo;</div></div>')


def glance_card(open_=None):
    rows = [('burn', '순자산 대비 월말 예상', '2.2%', None), ('score', '자산 종합 점수', '58점', '보통'), ('future', '10년 뒤 순자산', '약 3.82억원', None)]
    html = f'<div style="font-size: 12px; font-weight: 600; color: {C["INK2"]}; padding: 2px 0 4px;">자산 한눈에</div>'
    for i, (k, lab, val, tag) in enumerate(rows):
        last = i == len(rows) - 1
        html += glance_row(lab, val, open_ == k, last and open_ != k, tag)
        if open_ == k == 'burn':
            html += glance_panel(['이번 달 월말 예상 소비 208만원이 내 순자산 9,350만원의 2.2%예요.', '순자산이 클수록 같은 소비도 작은 비율이 돼요.', '지금까지 쓴 돈 112만원 기준으로는 1.2%예요.'], '자산 탭에서 순자산 보기')
        if open_ == k == 'future':
            html += glance_panel(['지금 속도로 모으면 10년 뒤 순자산은 약 3.82억원이에요.', '물가 · 세금은 빼고 계산했어요.'], '미래 탭에서 경로 보기')
        if open_ == k == 'score':
            parts = [('자산 대비 소비', 23, 40), ('매달 모을 수 있는 돈', 14, 30), ('부채 건전성', 6, 15), ('비상금', 15, 15)]
            bars = ''.join(f'<div style="margin-top: 9px;"><div style="display: flex; justify-content: space-between; font-size: 12px; color: {C["INK2"]};"><span>{n}</span><span style="font-weight: 600; color: {C["INK"]};">{v}/{m}</span></div>'
                           f'<div style="position: relative; height: 5px; border-radius: 99px; background: {C["TRACK"]}; margin-top: 4px;"><div style="position: absolute; inset: 0 {100 - v / m * 100:.1f}% 0 0; border-radius: 99px; background: {C["BRAND"]};"></div></div></div>' for n, v, m in parts)
            ring = (f'<div style="width: 78px; height: 78px; border-radius: 99px; background: conic-gradient({C["BRAND"]} 0% 58%, {C["TRACK"]} 58% 100%); display: flex; align-items: center; justify-content: center; flex-shrink: 0;">'
                    f'<div style="width: 64px; height: 64px; border-radius: 99px; background: {C["SURF"]}; display: flex; flex-direction: column; align-items: center; justify-content: center;">'
                    f'<span style="font-size: 22px; font-weight: 700; color: {C["INK"]};">58</span><span style="font-size: 10px; color: {C["INK3"]};">/ 100</span></div></div>')
            html += (f'<div style="padding: 6px 0 12px; border-bottom: 1px solid {C["LINE_ROW"]};"><div style="display: flex; align-items: center; gap: 12px;">{ring}'
                     f'<div><span style="font-size: 11px; font-weight: 600; color: {C["POS"]}; background: {C["POS_SOFT"]}; border-radius: 99px; padding: 2px 8px;">보통</span>'
                     f'<div style="font-size: 12px; line-height: 1.5; color: {C["INK2"]}; margin-top: 5px;">소비 · 매달 모을 수 있는 돈 · 부채 · 비상금을 함께 본 점수예요.</div></div></div>{bars}</div>')
    return plain_card(html, pad='10px 14px 4px')


glance_empty = plain_card(''.join(
    f'<div style="font-size: 12px; line-height: 1.5; color: {C["INK2"]}; padding: 7px 0; {"border-top: 1px solid " + C["LINE_ROW"] + ";" if i else ""}">{t}</div>'
    for i, t in enumerate([f'자산이 없으면 — 자산을 넣으면 월말 예상 소비를 순자산과 견줘 볼 수 있어요. · <span style="font-weight: 600; color: {C["BRAND"]}; white-space: nowrap;">자산 추가 &rsaquo;</span>',
                           '순자산이 0원 이하면 — 순자산이 0원 이하라 순자산 대비 비율은 계산하지 않아요.',
                           f'이번 달 기록이 0건이면 — 이번 달 소비를 기록하면 월말 예상 소비가 순자산의 몇 %인지 보여 드려요. · <span style="font-weight: 600; color: {C["BRAND"]}; white-space: nowrap;">오늘 쓴 돈 적기 &rsaquo;</span>',
                           '점수를 계산할 기록이 없으면 — 점수를 계산할 기록이 아직 없어요.',
                           '월말 예상이 임시 계산이면 — 월말 예상은 아직 임시 계산이라 달라질 수 있어요.',
                           '0 < 비율 < 0.05%면 — 0.1% 미만'])), pad='6px 14px')
GL_MEMO = memo_box([(1, f'한 번에 한 줄만 펼칩니다. 펼친 칸은 그 줄 바로 아래. 금액 쓰는 법은 미래 탭과 같은 {code("약")} + 100만원 단위.'),
                    (2, f'자산 종합 점수 = 자산 대비 소비 40 + 매달 모을 수 있는 돈 30 + 부채 건전성 15 + 비상금 15(시안 사용자 58점 · 보통). 지난달을 마감하기 전이면 {code("지난달을 마감한 뒤 점수를 보여 드려요.")}.')])
glance_body = (f'<div style="display: flex; gap: 20px; align-items: flex-start;">'
               + col(270, [case(1, '접힘', '홈 구성에서 켠 사람만.', glance_card())])
               + col(270, [case(1, '순자산 대비 월말 예상', '월말 예상과 지금까지 쓴 돈 두 기준.', glance_card('burn'))])
               + col(270, [case(2, '자산 종합 점수', '네 부분 점수.', glance_card('score'))])
               + col(270, [case(1, '10년 뒤 순자산', '미래 탭과 같은 값.', glance_card('future')), case(1, '값이 없을 때', '0원 · 0%로 채우지 않습니다.', glance_empty)])
               + '</div>' + GL_MEMO)
GL_W, GL_H = 1230, 1045      # 자연 1021 + 24
w('HomeGlanceRows', spec_frame(GL_W, GL_H, '홈 · 자산 한눈에 — 줄을 펼쳤을 때', '홈 구성에서 「자산 한눈에」를 켠 사람의 카드입니다. 줄을 누르면 그 아래에 풀이가 열립니다.', glance_body, sub_w=860), keep_all=True)


# ── SampleModeTabs · 샘플 모드 띠(모든 탭 · D8 · language-ia-21 · first-run-17) ──
def tab_top(name, h=196, html=None, strip=True):
    src_ = html if html is not None else src(name)
    i0_ = src_.index('<div style="width: 390px; height: ')
    body_ = src_[i0_:src_.index('</x-dc>')].rstrip()
    return (f'<div style="width: 392px; height: {h}px; overflow: hidden; border-radius: 22px; border: 1px solid {C["LINE"]}; background: {C["BG"]}; flex-shrink: 0;">'
            f'{v5.sample_strip() if strip else ""}{body_}</div>')


# 샘플은 지난달들을 마감하지 않았다 — 홈은 배지 없는 HomeSampleMode(띠 포함), 목적지는 맨 위 카드가 임시 계산(`목적지에 매달 필요한 돈`)이다(앱 NEW-SampleModeTabs).
GO_TOP0 = '<div style="background: #FFFFFF; border: 1px solid #E3E8F1; border-radius: 20px; padding: 15px 16px;'
assert GO.count(GO_TOP0) == 1
_go_top = balanced_at(GO, GO.index(GO_TOP0))
assert '매달 모으는 돈 바꿔 보기' in _go_top and '목적지에 나눠 넣는 중' in _go_top
SAMPLE_CLOSE = f'지난 몇 달을 마감하면 확정돼요 · <span style="font-weight: 600; color: {C["BRAND"]}; white-space: nowrap;">6월부터 마감하기 &rsaquo;</span>'      # D9 · 두 달 이상
goals_sample = GO.replace(_go_top, swap(goals_top, CLOSE_LINE, SAMPLE_CLOSE), 1)
smt_tabs = [('홈', tab_top('HomeSampleMode', strip=False)), ('자산', tab_top('Assets')), ('소비', tab_top('Spending')),
            ('목적지', tab_top('Goals', html=goals_sample)), ('미래', tab_top('Future'))]
smt = (f'<div style="display: flex; gap: 20px; flex-wrap: wrap;">'
       + ''.join(f'<div style="display: flex; flex-direction: column; gap: 8px;"><div style="font-size: 14px; font-weight: 700; color: {C["INK"]};">{lab}</div>{pic}</div>'
                 for lab, pic in smt_tabs)
       + '</div>'
       + memo_box([(1, f'샘플 모드에서는 모든 탭 머리줄 위에 띠 하나 {code("샘플 데이터로 둘러보는 중 · 내 데이터로 시작 ›")}만 둡니다. 다른 샘플 안내 · 저장 안내는 없습니다.'),
                   (2, f'{code("내 데이터로 시작 ›")}을 누르면 파란 확인 창 {code("샘플을 치우고 내 데이터로 시작할까요?")}(상태 페이지 StorageStates D) → 월급 입력 시트가 열립니다.'),
                   (3, '그림은 각 탭의 머리줄 · 세그먼트까지만 잘랐습니다(띠의 자리). 샘플 홈 전체는 HomeSampleMode 장 — 샘플은 지난달들을 마감하지 않아 월말 예상 배지 · 매달 모을 수 있는 돈이 임시 계산입니다.')]))
SMT_W, SMT_H = 1290, 823      # 자연 799 + 24
w('SampleModeTabs', spec_frame(SMT_W, SMT_H, '샘플 모드 — 모든 탭 맨 위 띠', '샘플로 둘러보는 동안 다섯 탭 모두 머리줄 위에 같은 띠가 있습니다.', smt, sub_w=860), keep_all=True)


# ── DebtUnpayable · 월 최소 상환액을 비워 둔 부채(tasks-4 · D7 · D11 · D15) — 예: 전세자금대출 1억 · 연 3.6% · 월 추가 20만원 ──
du_form = (f'<div style="background: {C["SURF"]}; border: 1px solid {C["LINE"]}; border-radius: 22px; padding: 16px; display: flex; flex-direction: column; gap: 12px;">'
           f'<div><div style="font-size: 17px; font-weight: 700; color: {C["INK"]};">부채 추가</div><div style="font-size: 12px; color: {C["INK3"]}; margin-top: 3px;">금리와 매달 내는 돈으로 다 갚는 달을 계산해요.</div></div>'
           + field('부채 이름', '전세자금대출', required=True)
           + f'<div style="display: flex; gap: 10px;">{select_field("유형", "주택담보 · 전세대출")}{field("남은 원금", "10,000", "만원", required=True, w=132, readback="1억원")}</div>'
           + f'<div style="display: flex; gap: 10px;">{field("연 금리", "3.6", "%", required=True)}{field("월 최소 상환액", "", "만원", w=132, helper="매달 내는 돈(원금+이자) · 이자만 내면 이자를 적어요")}</div>'
           + f'<div role="status" style="padding: 10px 12px; border-radius: 12px; background: {C["WARN_SOFT"]}; font-size: 12px; line-height: 1.5; color: {C["WARN_INK"]};">'      # 앱 — 주황 칸 · 아이콘 없음
             f'월 상환액이 비어 있어요. 이대로 저장하면 다 갚는 달과 총이자를 계산하지 않아요. 이자만 내고 있다면 그대로 저장해도 돼요.</div>'
           + f'<div style="display: flex; gap: 8px;">{btn("취소", "secondary", h=44).replace("width: 100%;", "flex: 1;")}{btn("그대로 저장", "primary", h=44).replace("width: 100%;", "flex: 1.4;")}</div></div>')
du_debts = plain_card(
    f'<div style="display: flex; justify-content: space-between; align-items: flex-start;"><span style="font-size: 11px; font-weight: 600; color: {C["INK3"]};">총부채</span>'
    f'<span style="font-size: 11px; font-weight: 600; color: {C["INK2"]}; background: {C["INSET"]}; border-radius: 99px; padding: 3px 8px;">평균 금리 연 3.6%</span></div>'
    f'<div style="display: flex; justify-content: space-between; align-items: flex-end; margin-top: 6px;"><span style="font-size: 30px; font-weight: 700; letter-spacing: -0.04em;">1<span style="font-size: 16px; font-weight: 600; color: {C["INK2"]};">억원</span></span>'
    f'<span style="text-align: right;"><span style="display: block; font-size: 11px; color: {C["INK3"]};">월 최소 상환</span><span style="font-size: 15px; font-weight: 600; color: {C["INK4"]};">—</span> '
    f'<span style="font-size: 10.5px; font-weight: 600; color: {C["INK2"]}; background: {C["INSET"]}; border-radius: 99px; padding: 2px 7px;">입력 필요</span></span></div>'
    f'<div style="font-size: 12px; color: {C["INK2"]}; margin-top: 10px; padding-top: 10px; border-top: 1px solid {C["LINE_ROW"]};">전세자금대출 · 주택담보 · 전세대출 · 월 최소 — '
    f'<span style="font-size: 10.5px; font-weight: 600; color: {C["INK2"]}; background: {C["INSET"]}; border-radius: 99px; padding: 2px 7px;">입력 필요</span></div>'
    f'<div style="display: flex; justify-content: space-between; margin-top: 10px; padding-top: 10px; border-top: 1px solid {C["LINE_ROW"]};"><span style="font-size: 13px; font-weight: 600;">이번 달 상환 예정</span><span style="color: {C["INK4"]}; font-weight: 600;">—</span></div>'
    f'<div style="font-size: 12px; color: {C["INK3"]}; margin-top: 3px;">이 부채의 월 최소 상환액을 넣으면 보여요 · <span style="font-weight: 600; color: {C["BRAND"]};">상환액 넣기 &rsaquo;</span></div>')
du_strategy = plain_card(
    f'<div style="display: flex; justify-content: space-between; align-items: center;"><span style="font-size: 11px; font-weight: 600; color: {C["INK3"]};">저장된 상환 계획</span>{badge("저장된 계획", "pos", "check")}</div>'
    f'<div style="font-size: 15px; font-weight: 700; margin-top: 8px;">고금리 우선 · 월 추가 20만원</div>'
    f'<div style="font-size: 12px; color: {C["INK2"]}; margin-top: 3px;">최소 — + 추가 20만원 = 매월 —</div>'
    f'<div style="margin-top: 10px;">{btn("상환 계획 바꾸기 ›", "outline", h=40)}</div>'
    f'<div style="display: flex; gap: 12px; margin-top: 12px; padding-top: 12px; border-top: 1px solid {C["LINE_ROW"]};">'
    f'<div style="flex: 1;"><div style="font-size: 11px; color: {C["INK3"]};">다 갚는 달</div><div style="font-size: 15px; font-weight: 700;">다 갚지 못해요</div>'
    f'<div style="font-size: 11px; line-height: 1.45; color: {C["INK3"]}; margin-top: 2px;">매달 이자가 약 300,000원이에요. 이보다 많이 갚아야 잔액이 줄어요.</div></div>'
    f'<div style="width: 70px;"><div style="font-size: 11px; color: {C["INK3"]};">총이자</div><div style="font-size: 15px; font-weight: 700; color: {C["INK4"]};">—</div></div></div>'
    f'<div style="font-size: 12px; color: {C["INK3"]}; margin-top: 8px;">월 상환액을 넣으면 다 갚는 달을 계산해요 · <span style="font-weight: 600; color: {C["BRAND"]};">상환액 넣기 &rsaquo;</span></div>')
du_order = plain_card(      # 앱 section.strategy-order — 머리 「갚는 순서 · 고금리 우선」 + 번호 줄(2026-09-27 fix-up 4)
    section_head('갚는 순서', '고금리 우선')
    + f'<div style="display: flex; align-items: center; gap: 11px; min-height: 46px; margin-top: 6px;">'
      f'<span style="width: 22px; height: 22px; border-radius: 99px; background: {C["BRAND_SOFT"]}; color: {C["BRAND"]}; font-size: 11.5px; font-weight: 700; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">1</span>'
      f'<span style="flex: 1; font-size: 13.5px; font-weight: 600; color: {C["INK"]};">전세자금대출</span>'
      f'<span style="font-size: 12px; color: {C["INK3"]}; white-space: nowrap;">다 갚지 못해요</span></div>')
du_strategy = f'<div style="display: flex; flex-direction: column; gap: 10px;">{du_strategy}{du_order}</div>'
du_home = line_card_v5 = (f'<div style="background: {C["SURF"]}; border: 1px solid {C["LINE"]}; border-radius: 18px; padding: 10px 14px; display: flex; justify-content: space-between; align-items: center; gap: 8px;">'
                          f'<div><div style="font-size: 13.5px; font-weight: 600;">상환 계획</div><div style="font-size: 11.5px; color: {C["INK3"]};">월 상환액을 넣으면 다 갚는 달을 계산해요</div></div>'
                          f'<span style="font-size: 11.5px; color: {C["INK3"]}; white-space: nowrap;">매달 갚는 돈 <b style="font-size: 15px; color: {C["INK"]};">20만원</b></span></div>')
DU_MEMO = memo_box([(1, f'새 부채의 연 금리는 빈칸에서 시작하고(자리 글자 {code("예: 6.5")}) 필수입니다. 월 최소 상환액이 비면 두 단계 — 주황 안내가 뜨고 버튼이 {code("그대로 저장")}.'),
                    (2, f'저장한 뒤 부채 화면은 {code("월 최소 상환 —")} + {code("입력 필요")}, 이번 달 상환 예정 {code("—")} + {code("상환액 넣기 ›")}. 0원이나 좋은 결과로 보이지 않습니다.'),
                    (3, f'자산 › 상환 계획(읽기 전용 요약)은 {code("다 갚지 못해요")} · 총이자 {code("—")} · 까닭 한 줄. 미래 › 상환 계획의 같은 경우는 PayoffStates 2번. 홈 상환 계획 줄도 같은 문장.')])
du_body = (f'<div style="display: flex; gap: 24px; align-items: flex-start;">'
           + col(362, [case(1, '부채 추가 — 월 최소 상환액 빈칸', '저장 전에 한 번 더 알립니다.', du_form)])
           + col(362, [case(2, '자산 › 부채', '월 최소 상환 — · 입력 필요.', du_debts), case(3, '홈 · 상환 계획 한 줄', '다 갚는 달 대신 까닭.', du_home)])
           + col(362, [case(3, '자산 › 상환 계획', '다 갚지 못해요 · 총이자 —.', du_strategy)])
           + '</div>' + DU_MEMO)
DU_W, DU_H = 1230, 936      # 자연 912 + 24(DZ4 검토 — 주황 안내 아이콘 뺌 · 되읽기)
w('DebtUnpayable', spec_frame(DU_W, DU_H, '월 최소 상환액을 비워 둔 부채 — 다 갚지 못할 때',
                              '예: 전세자금대출 1억 · 연 3.6%만 있고 월 최소 상환액을 비웠습니다(월 추가 20만원). 계산할 수 없는 값은 0원이 아니라 —입니다.', du_body, sub_w=860), keep_all=True)



# ── AssetsStale · 자산 › 자산 구성 — 잔액 확인이 필요한 자산이 있을 때(assets-15 · 앱 asset-view · lib/navi-asset-freshness · 2026-09-27 fix-up 3) ──
# 시안 사용자에서 한 가지만 바꾼 앱 화면(하네스): ETF 계좌 마지막 확인 7월 30일(40일 전) · 청약저축 확인 기록 없음 → 자산 구성 머리 아래 주황 띠
# 「잔액 확인이 필요한 자산 2개 · 한 번에 확인 ›」(누르면 모달 페이지 AssetBalanceCheck) · 두 줄에 주황 「확인 필요」 칩 · 부제 끝 「· 마지막 확인 7월 30일」/「· 확인 기록 없음」.
# 같은 날 알림에는 참고 1줄(AlertsPanelInfo). 나머지 값은 Assets 장 그대로.
AS = src('Assets')
i0 = AS.index('<div style="width: 390px; height: ')
AS_BODY = AS[i0:AS.index('</x-dc>')].rstrip()
STALE_CHIP = (f'<span style="display: inline-flex; align-items: center; height: 20px; padding: 0 7px; border-radius: 99px; background: {C["WARN_SOFT"]}; '
              f'color: {C["WARN_INK"]}; font-size: 11px; font-weight: 600; white-space: nowrap; flex-shrink: 0;">확인 필요</span>')
STALE_BAND = (f'\n      <div style="display: flex; align-items: center; min-height: 44px; margin-top: 12px; padding: 10px 14px; border-radius: 12px; background: {C["WARN_SOFT"]}; '
              f'font-size: 13px; font-weight: 700; line-height: 1.4; color: {C["WARN_INK"]};">잔액 확인이 필요한 자산 2개 · 한 번에 확인 &rsaquo;</div>\n')
AS_HEAD_END = '          추가\n        </div>\n      </div>\n'
stale = swap(AS_BODY, AS_HEAD_END, AS_HEAD_END + STALE_BAND)
for name, sub, tail in [('ETF 계좌', '투자 · 수익률 연 6.5%', ' · 마지막 확인 7월 30일'), ('청약저축', '기타 · 수익률 연 1.8%', ' · 확인 기록 없음')]:
    stale = swap(stale, f'<div style="font-size: 13.5px; font-weight: 600; color: #101828;">{name}</div>\n            <div style="font-size: 11px; color: #626D88;">{sub}</div>',
                 f'<div style="display: flex; align-items: center; gap: 6px; min-width: 0;"><span style="font-size: 13.5px; font-weight: 600; color: #101828; white-space: nowrap;">{name}</span>{STALE_CHIP}</div>\n'
                 f'            <div style="font-size: 11px; line-height: 1.4; color: #626D88;">{sub}{tail}</div>')
# 부제가 한 줄 넘게 길어질 수 있어 두 줄의 높이를 늘릴 수 있게(앱 행은 내용 높이)
stale = stale.replace('<div style="display: flex; align-items: center; gap: 9px; height: 48px;', '<div style="display: flex; align-items: center; gap: 9px; min-height: 48px; padding: 4px 0;')
AST_H = 1033      # 자연 1009 + 24(gen_canvas TALL · screens.json 과 같게)
stale = re.sub(r'width: 390px; height: \d+px;', f'width: 390px; height: {AST_H}px;', stale, count=1)
assert balanced(stale) and stale.count('확인 필요') == 2
w('AssetsStale', stale, keep_all=True)


NEW = {'InsufficientElsewhere': (INS_W, INS_H), 'FutureProvisional': (FUT_W, FUT_H), 'EtcSubline': (ETC_W, ETC_H),
       'LimitCardCases': (LC_W, LC_H), 'RecurringPrefill': (390, PREFILL_H), 'ImportBackupNotes': (IB_W, IB_H),
       'PayoffStates': (PAY_W, PAY_H), 'FutureStates': (FUTS_W, FUTS_H), 'HomeGlanceRows': (GL_W, GL_H), 'SampleModeTabs': (SMT_W, SMT_H),
       'DebtUnpayable': (DU_W, DU_H), 'AssetsStale': (390, AST_H)}
if __name__ == '__main__':
    for n_, (w_, h_) in NEW.items():
        print(f'{n_}: {w_} × {h_}')
