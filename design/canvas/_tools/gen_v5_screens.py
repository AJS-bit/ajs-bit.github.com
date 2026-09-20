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
SUBLINE = f'분류 안 함 {v5.CLS_COUNT}건 {UNCAT_SUM:,}원'
assert SUBLINE == '분류 안 함 7건 32,000원'


def chip_lg(text='잠정'):
    """# 제안 — `잠정` 표시(큰 숫자 옆). 중립 배지: 의미색 없이 회색 바탕 + 잉크."""
    return (f'<span style="display: inline-flex; align-items: center; background: #F0F2F7; color: {C["TAB_INK"]}; font-size: 11.5px; font-weight: 600; '
            f'border-radius: 99px; padding: 4px 9px; white-space: nowrap; flex-shrink: 0;">{text}</span>')


def chip_sm(text='잠정'):
    """# 제안 — `잠정` 표시(행 · 카드 제목 옆). `홈 대표` 칩과 같은 크기의 중립 칩."""
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
assert balanced(sp_header) and balanced(sp_top) and sp_top.count('57.9') == 1


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

# ① 소비 · 이번 달 — 머리 + 맨 위 카드. 배지가 빠지고 예상 값 옆에 `잠정`, 그 아래 사실 문구.
# 계획선은 y = 118 − 0.2822 × (x − 12). 글은 선과 겹치지 않게 놓는다 — `계획선 · …` 라벨은 v3 Spending 과 같은 y 86(그 x 구간의 선은 y 68 이하라 글 위로 지나감),
# `5,000원`은 y 80(x 74~113 에서 선은 y 89 이상이라 글 아래로 지나감 · 세로 안내선은 글 바로 밑 84 까지).
spend_svg = (
    '<svg width="362" height="150" viewBox="0 0 362 150" fill="none" style="display: block; width: 100%; height: 150px;">'
    '<path d="M12 118 L350 22.6" stroke="#B9C3D6" stroke-width="1.4" stroke-dasharray="4 4" stroke-linecap="round"/>'
    '<line x1="93.6" y1="118" x2="93.6" y2="84" stroke="#DCE2EC" stroke-width="1"/>'
    '<path d="M12 118 L81.9 118 L93.6 117.6" stroke="#3556E6" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>'
    '<path d="M93.6 117.6 L350 116.9" stroke="#8FA6F2" stroke-width="2.2" stroke-dasharray="5 4" stroke-linecap="round" stroke-linejoin="round"/>'
    '<circle cx="93.6" cy="117.6" r="4" fill="#3556E6"/><circle cx="93.6" cy="117.6" r="7.5" fill="#3556E6" fill-opacity="0.15"/>'
    '<text x="93.6" y="80" text-anchor="middle" font-size="11" font-weight="600" fill="#101828">5,000원</text>'
    '<circle cx="350" cy="116.9" r="3.4" fill="#8FA6F2"/>'
    '<text x="350" y="104" text-anchor="end" font-size="11" font-weight="600" fill="#4B6BDE">월말 예상 1.9만 · 잠정</text>'
    '<text x="188" y="86" text-anchor="start" font-size="10" fill="#697182">계획선 · 한도 216만까지</text>'
    '<line x1="12" y1="118" x2="350" y2="118" stroke="#E3E8F1" stroke-width="1"/>'
    '<text x="12" y="133" text-anchor="start" font-size="10.5" fill="#697182">1일</text>'
    '<text x="93.6" y="133" text-anchor="middle" font-size="10.5" font-weight="600" fill="#475467">8일 오늘</text>'
    '<text x="175.2" y="133" text-anchor="middle" font-size="10.5" fill="#697182">15일</text>'
    '<text x="256.8" y="133" text-anchor="middle" font-size="10.5" fill="#697182">22일</text>'
    '<text x="350" y="133" text-anchor="end" font-size="10.5" fill="#697182">30일</text></svg>')
PCT_UNIT = '<span style="font-size: 18px; font-weight: 600; color: #475467;">%</span>'
BADGE_CRUISE = ('<span style="display: inline-flex; align-items: center; gap: 4px; background: #E4F4EA; color: #0F7B47; font-size: 11.5px; font-weight: 600; '
                'border-radius: 99px; padding: 4px 9px;">목표 안에서 순항 중</span>')
PACE_ROW = '<div style="display: flex; align-items: baseline; justify-content: space-between; gap: 8px; margin-top: 13px; padding: 0 2px;">'
fact_line = (f'<div style="display: flex; align-items: flex-start; gap: 4px; margin-top: 11px; padding: 0 2px;">'
             f'<span style="font-size: 12.5px; line-height: 1.45; color: {C["INK2"]};">{FACT_5K}</span>{imark(2)}</div>\n\n      ')
spend_first = swap(sp_top, '>57.9</span>', '>0.5</span>')
spend_first = swap(spend_first, PCT_UNIT, PCT_UNIT + f'\n            <span style="margin-left: 6px; align-self: center; display: inline-flex; align-items: center;">{chip_lg()}{imark(1)}</span>')
spend_first = swap(spend_first, BADGE_CRUISE, '')
spend_first = swap(spend_first, PACE_ROW, fact_line + PACE_ROW)
spend_first = re.sub(r'<svg width="362" height="150".*?</svg>', lambda m_: spend_svg, spend_first, count=1, flags=re.S)
assert '순항' not in spend_first and spend_first.count('잠정') == 2 and balanced(spend_first)
spend_part = (f'<div style="width: 390px; background: {C["BG"]}; border: 1px solid {C["LINE"]}; border-radius: 24px; overflow: hidden; padding-bottom: 14px;">'
              f'{sp_header}<div style="padding: 0 14px;">{spend_first}</div></div>')

# ② 한도 — 맨 위 카드. v5-1 시점이라 라벨은 `하루`(v5-3 뒤 `앞으로 하루`).
limit_first = swap(lm_top, '>104만원</span>', '>216만원</span>')
limit_first = swap(limit_first, 'inset: 0 48.1% 0 0', 'inset: 0 99.8% 0 0')
limit_first = swap(limit_first, '사용 112만원 · 52%', '사용 5,000원 · 0.2%')
limit_first = swap(limit_first, '22일 남음 · 하루 47,270원', '22일 남음 · 하루 97,950원')
LM_BTN = '<div style="display: flex; align-items: center; justify-content: center; gap: 6px; height: 44px; margin-top: 13px;'
limit_first = swap(limit_first, LM_BTN,
                   f'<div style="margin-top: 9px; font-size: 12px; line-height: 1.45; color: {C["INK2"]};">{FACT_5K}</div>\n\n      ' + LM_BTN)
assert balanced(limit_first) and '초과 예상' not in limit_first

# ③ 코치 — 확정 부채 안내(사실)는 그대로, 예상에서 나오는 안내 대신 사실 안내.
coach_first = mini_sheet('코칭', '저장된 기록을 보고 중요한 순서로 알려드려요.',
                         f'<div style="display: flex; flex-direction: column; gap: 8px;">'
                         + advice('neg', '카드 할부 금리 14.5%를 먼저 정리하세요', '잔액은 전체의 2%뿐이지만 금리가 신용대출의 2.1배예요. 고금리 우선 전략에서 1순위입니다.', '상환 전략 열기', 1)
                         + advice('sky', '기록한 소비 5,000원', '아직 기록하지 않은 소비는 포함하지 않았어요', None, 2) + '</div>')

# ⑤ 또래 카드 — PeerStates 의 B 에서 초록 줄(`목표 60% 안에서 순항 중`)만 사실 문구로.
PS = src('PeerStates')
i_b = PS.index('B · 연령 구간 있음')
i_card = PS.index('<div style="background: #FFFFFF; border: 1px solid #E3E8F1; border-radius: 18px; padding: 14px;">', i_b)
i_c = PS.index('<div style="font-size: 11px; font-weight: 600; letter-spacing: 0.06em; color: #606B7D; padding: 6px 2px 0;">C ·', i_card)
peer_b = PS[i_card:i_c].rstrip()
assert balanced(peer_b) and peer_b.count('순항 중') == 1
peer_first = re.sub(r'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px; margin-top: 13px; padding: 10px 12px; background: #E4F4EA; border-radius: 12px;">.*?</div>',
                    lambda m_: (f'<div style="margin-top: 13px; padding: 10px 12px; background: {C["INSET"]}; border-radius: 12px; font-size: 12.5px; line-height: 1.45; color: {C["INK2"]};">{FACT_5K}</div>'),
                    peer_b, count=1, flags=re.S)
assert balanced(peer_first) and '순항' not in peer_first

# ⑥ 알림 — `이번 달 적자입니다`는 목록에도 개수에도 없다. 확정 부채 · 비상금(사실)은 그대로.
bell = (f'<div style="display: flex; align-items: center; gap: 8px; padding: 8px 10px; background: {C["INSET"]}; border-radius: 12px;">'
        f'<div style="width: 36px; height: 36px; border-radius: 11px; background: {C["SURF"]}; display: flex; align-items: center; justify-content: center; position: relative; flex-shrink: 0;">'
        f'{icon("bell", 19, C["INK2"], 1.9)}<span style="position: absolute; top: 3px; right: 3px; min-width: 15px; height: 15px; border-radius: 99px; background: {C["NEG"]}; color: #FFFFFF; '
        f'font-size: 10px; font-weight: 700; display: flex; align-items: center; justify-content: center; padding: 0 4px; border: 2px solid {C["SURF"]};">2</span></div>'
        f'<span style="font-size: 12px; line-height: 1.45; color: {C["INK3"]};">머리줄 종의 숫자도 같은 2</span></div>')
alerts_first = mini_sheet('알림 2건', '저장된 기록을 기준으로 만든 알림이에요. 읽어도 기록은 바뀌지 않아요.',
                          f'<div style="display: flex; flex-direction: column;">'
                          + alert('neg', 'bank', '카드 할부 금리가 14.5%예요', '보유 부채 중 가장 높습니다', '상환 전략')
                          + alert('sky', 'shield', '비상금이 목표의 68%예요', '1,020 / 1,500만원 · 480만원 남음', '목적지 배분', last=True) + '</div>' + bell)
assert '적자' not in alerts_first

guide_first = first_guide.replace(' flex-shrink: 0;">', '">', 1)

ins_memo = memo_box([
    (1, f'소비 · 이번 달 — 숫자 옆 배지 {code("목표 안에서 순항 중")} · {code("월급을 넘는 소비")}가 없습니다. 예상 값(소비율 · 월말 예상)은 공식대로 계산해 보여 주되 {code("잠정")}을 붙입니다.'),
    (2, f'그 자리에 사실 문구 {code("기록한 소비 N원 · 아직 기록하지 않은 소비는 포함하지 않았어요")} 한 줄만 남습니다. 색 · 아이콘으로 좋다 · 나쁘다를 말하지 않습니다.'),
    (3, f'한도 탭 — 예상에서 나오는 한도 각주와 카테고리 줄의 {code("초과 예상")}이 없습니다. 이미 넘은 한도는 예상이 아니라 사실이므로 그대로 표시합니다.'),
    (4, f'코치 — {code("예상 잔여자금률 77% — 축적 여력이 큽니다")} · {code("모든 목표가 궤도에 있습니다")}가 없습니다. 고금리 부채처럼 확정된 안내는 그대로입니다.'),
    (5, f'다음 안내 — {code("지금의 저축·투자 흐름을 유지하세요")}가 없습니다. 홈(HeroInsufficient)과 같은 카드입니다.'),
    (6, f'또래 카드 — {code("목표 60% 안에서 순항 중")} 줄이 없습니다. 나머지(연령 구간 · 기준 등록)는 그대로입니다.'),
    (7, f'알림 — 예상으로 만든 {code("이번 달 적자입니다")}는 목록과 개수(제목 · 머리줄 종 배지)에서 모두 빠집니다. 알림 생성은 그대로 두고 표시할 때 거릅니다.')],
    tail=f'판정은 하나입니다 — 예상 기준 확인 규칙(계획 §3-4)을 통과하기 전이면 위 일곱 곳이 전부 이 모양이고, 통과하면 전부 원래 화면으로 돌아갑니다. 그래서 {code("순항 중")}이 어디에도 없습니다.')

ins_body = (
    f'<div style="display: flex; gap: 24px; align-items: flex-start;">'
    + col(390, [case(1, '소비 · 이번 달', '배지가 없고, 예상 값에는 잠정이 붙습니다.', spend_part),
                case(5, '다음 안내', '흐름을 유지하라는 권고 대신 사실만.', guide_first)])
    + col(362, [case(3, '소비 · 한도', '예상 각주와 초과 예상 표시가 없습니다.', limit_first),
                case(4, '코치', '확정된 안내와 사실 안내만 남습니다.', coach_first)])
    + col(362, [case(6, '또래와 내 페이스', '순항 문구가 있던 줄이 사실 문구로 바뀝니다.', peer_first),
                case(7, '알림', '예상으로 만든 적자 알림은 목록에도 개수에도 없습니다.', alerts_first)])
    + '</div>' + ins_memo)
INS_W, INS_H = 1230, 1330
w('InsufficientElsewhere', spec_frame(
    INS_W, INS_H, '예상 기준을 확인하기 전 — 홈 밖의 화면들',
    '홈의 이력 부족 상태(HeroInsufficient)와 같은 사람입니다 — 9월 5일에 처음 열었고 오늘 커피 5,000원 한 건을 적었습니다. '
    '지난 소비 기록을 확인하기 전에는 예상에서 나오는 판단을 어느 화면에서도 하지 않고, 기록한 사실만 말합니다.',
    ins_body, sub_w=860), keep_all=True)


# ══════════════════════════════════════════════════════════════
# 2. FutureProvisional — 미래 · 자산 경로의 `잠정` (rank 12 · v5-1 · v3 내비)
# ══════════════════════════════════════════════════════════════
FU = src('Future')
i0 = FU.index('<div style="width: 390px; height: 844px;')
i1 = FU.index('</x-dc>')
future_phone = FU[i0:i1].rstrip()
# 각주에 이유 한 문장이 붙어 한 줄 길어진다 — 참고 장 안의 그림이라 아래 가정 카드가 잘리지 않게 16px 늘린다(앱 화면은 스크롤)
future_phone = swap(future_phone, 'width: 390px; height: 844px;', 'width: 390px; height: 860px;')
assert balanced(future_phone)
EOK = '<span style="font-size: 17px; font-weight: 600; color: #475467;">억원</span>'
MILE = '<span style="font-size: 14px; font-weight: 600; color: #101828;">다음 자산 지점</span>'
FOOT = '월 63만원 적립과 현재 자산 구성이 유지된다고 가정합니다.</p>'
SIM = '저장되지 않는 가정\n        </span>'
PROV_WHY = '지난 소비 기록을 아직 확인하지 않아 잠정 값이에요.'          # 제안 — 계획에 원문 없음


def future_with(marks=True):
    m1, m2, m3 = (imark(1), imark(2), imark(3)) if marks else ('', '', '')
    html = swap(future_phone, EOK, EOK + f'\n            <span style="margin-left: 5px; align-self: center; display: inline-flex; align-items: center;">{chip_lg()}{m1}</span>')
    html = swap(html, MILE, MILE + f'\n        <span style="display: inline-flex; align-items: center; margin-left: 2px;">{chip_sm()}{m2}</span>')
    html = swap(html, FOOT, FOOT.replace('</p>', f' {PROV_WHY}</p>'))
    html = swap(html, SIM, SIM.replace('\n', m3 + '\n'))
    return html


future_prov = future_with()
assert future_prov.count('잠정') == 3 and balanced(future_prov)
future_left = (f'<div style="width: 392px; flex-shrink: 0; border-radius: 24px; overflow: hidden; border: 1px solid {C["LINE"]};">{future_prov}</div>')

# 표시 모양 — 두 크기
chip_spec = (f'<div style="background: {C["SURF"]}; border: 1px solid {C["LINE"]}; border-radius: 18px; padding: 14px; display: flex; flex-direction: column; gap: 12px;">'
             f'<div style="display: flex; align-items: center; gap: 12px;">{chip_lg()}<span style="font-size: 12px; line-height: 1.5; color: {C["INK2"]};">화면의 큰 숫자 옆 · 11.5px · 회색 바탕 알약</span></div>'
             f'<div style="display: flex; align-items: center; gap: 12px;"><span style="width: 41px; display: inline-flex; justify-content: center; flex-shrink: 0;">{chip_sm()}</span>'
             f'<span style="font-size: 12px; line-height: 1.5; color: {C["INK2"]};">카드 제목 · 목록의 날짜 옆 · 10px · 홈 대표 칩과 같은 크기</span></div>'
             f'<div style="font-size: 12px; line-height: 1.5; color: {C["INK3"]}; border-top: 1px solid {C["LINE_ROW"]}; padding-top: 10px;">'
             f'초록 · 주황 · 빨강 · 가정 보라를 쓰지 않습니다. 좋다 · 나쁘다가 아니라 아직 확인 전이라는 뜻이기 때문입니다.</div></div>')

# 목표 화면 — 진행 중인 목적지 카드(Goals)에서 앞 세 줄
GO = src('Goals')
GO_CARD = '<div style="background: #FFFFFF; border: 1px solid #E3E8F1; border-radius: 18px; padding: 12px 14px 8px; flex-shrink: 0;">'
GO_ROW = '<div style="display: flex; align-items: center; gap: 11px; padding: 11px 0; border-top: 1px solid #F3F5FA;">'
assert GO.count(GO_CARD) == 1
g0 = GO.index(GO_CARD)
pos, g_rows = g0, []
for _ in range(4):
    pos = GO.index(GO_ROW, pos + 1)
    g_rows.append(pos)
goals_card = GO[g0:g_rows[3]].rstrip() + '\n    </div>'
assert balanced(goals_card)
goals_card = swap(goals_card, '도착 예상 2027년 11월</div>', f'도착 예상 2027년 11월 {chip_sm()}</div>')
# 칩은 날짜 옆(메모 4번). 글 칸이 180px 라 한 줄에 다 안 들어간다 — 날짜 + 칩을 nowrap 으로 묶어 칩이 혼자 떨어지지 않게 하고, 넘치면 `· 연 5.0% 가정`이 통째로 내려간다
goals_card = swap(goals_card, '2032년 6월 도착 · 연 5.0% 가정</div>',
                  f'<span style="white-space: nowrap;">2032년 6월 도착 {chip_sm()}</span> <span style="white-space: nowrap;">· 연 5.0% 가정</span></div>')
assert goals_card.count('잠정') == 2 and '완제 예상 2030년 10월 · 상환 계획 반영</div>' in goals_card

# 기준을 확인한 뒤 — 같은 자리, 표시 없음(Future 원본 그대로의 숫자 줄)
NUM0 = '<div style="display: flex; align-items: flex-end; justify-content: space-between; gap: 10px; margin-top: 14px; padding: 0 2px;">'
NUM1 = '<div style="margin-top: 10px;">\n        <svg width="362"'
num_block = cut(FU, NUM0, NUM1).rstrip()
assert balanced(num_block)
confirmed_block = (f'<div style="background: {C["SURF"]}; border: 1px solid {C["LINE"]}; border-radius: 18px; padding: 2px 14px 14px;">{num_block}</div>')

fut_memo = memo_box([
    (1, f'{code("10년 뒤 순자산 약 3.21억원")} 옆에 {code("잠정")}. 값은 공식대로 계산한 그대로이고, 숫자를 흐리게 하거나 {code("—")}로 가리지 않습니다. 각주 끝에 이유 한 문장을 붙입니다.'),
    (2, f'다음 자산 지점은 도착일 세 줄이 모두 같은 예상에서 나오므로 줄마다 붙이지 않고 카드 제목 옆에 한 번만 붙입니다.'),
    (3, f'보라 점선 {code("저장되지 않는 가정")} 카드에는 붙이지 않습니다 — 기록에서 계산한 기본 예측(초록 선 · 월 63만원 적립)과 사용자가 넣은 가정은 이미 모양으로 구분됩니다.'),
    (4, f'목표 화면은 목적지마다 {code("도착 예상")} 날짜 옆에 작은 칩. 부채 상환 목적지의 {code("완제 예상")}은 소비 예상이 아니라 상환 계획에서 나오므로 붙이지 않습니다.'),
    (5, f'예상 기준 확인 규칙(계획 §3-4)을 통과하면 칩과 이유 문장이 함께 사라집니다. 소비 · 이번 달의 예상 값에도 같은 칩을 씁니다(InsufficientElsewhere 1번). v4-2 뒤 목적지 탭(DestFuture · DestGoals)도 같은 자리입니다.')])

fut_right = (f'<div style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 22px;">'
             f'<div style="display: grid; grid-template-columns: repeat(2, 362px); gap: 22px 20px; align-items: start;">'
             + case(4, '목표 화면 · 진행 중인 목적지', '도착 예상 날짜 옆에 작은 칩이 붙습니다.', goals_card)
             + f'<div style="display: flex; flex-direction: column; gap: 22px;">'
             + f'<div style="display: flex; flex-direction: column; gap: 8px;"><div><div style="font-size: 14px; font-weight: 700; letter-spacing: -0.01em; color: {C["INK"]};">표시 모양</div>'
               f'<div style="font-size: 12px; line-height: 1.5; color: {C["INK3"]}; margin-top: 3px;">크기는 둘, 색은 회색 하나입니다.</div></div>{chip_spec}</div>'
             + case(5, '지난 기록을 확인한 뒤', '같은 자리에서 표시만 사라집니다.', confirmed_block)
             + '</div></div>' + fut_memo + '</div>')
FUT_W, FUT_H = 1230, 1080
w('FutureProvisional', spec_frame(
    FUT_W, FUT_H, '미래 · 자산 경로 — 예상 기준을 확인하기 전의 잠정 표시',
    '지난 소비 기록을 확인하기 전에도 미래 · 목표 화면의 예상 값은 그대로 보여 주되 잠정이라고 표시합니다. '
    '왼쪽이 그 상태의 미래 화면(v4-2 전이라 옛 다섯 탭)이고, 번호는 표시가 붙는 자리입니다.',
    f'<div style="display: flex; gap: 32px; align-items: flex-start;">{future_left}{fut_right}</div>', sub_w=860), keep_all=True)


# ══════════════════════════════════════════════════════════════
# 3. EtcSubline — `기타` 서브라인 · 코치 `소비 없음 확인 n일` (rank 30 · v5-1 · v5-2)
# ══════════════════════════════════════════════════════════════
# `기타` 6만원 / 한도 5만원(엔진 소진율 120%) 중 분류 안 함 32,000원 → 뺀 사용량 28,000원(56%)으로 경고를 다시 판단 → 경고 없음. (# 제안 · 예시 숫자)
assert 60_000 - UNCAT_SUM == 28_000 and 28_000 * 100 // 50_000 == 56 and 60_000 * 100 // 50_000 == 120      # 메모 2번의 28,000원(56%) · 기타 줄의 120%
REJUDGE = '분류 안 한 32,000원을 빼고 한도 경고를 판단했어요 · 분류하면 다시 판단해요'     # 제안 — 계획에 원문 없음
FIXED_LIMIT = '직접 정한 고정비 한도는 고정비 예상에 반영되지 않아요. 고정비 예상은 지난 기록과 이번 달 실제 금액으로 계산해요.'     # 제안 — 계획에 원문 없음

etc_row_spend = (
    f'<div style="display: flex; align-items: flex-start; gap: 10px; padding: 8px 0 2px;">'
    f'<div style="width: 30px; height: 30px; border-radius: 10px; background: #64748b18; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">{icon("tag", 15, "#64748b", 1.9)}</div>'
    f'<div style="flex: 1; min-width: 0;">'
    f'<div style="display: flex; align-items: baseline; justify-content: space-between; gap: 8px;">'
    f'<span style="font-size: 13.5px; font-weight: 600; color: #101828;">기타</span>'
    f'<span style="font-size: 13px; font-weight: 600; color: #101828;">6<span style="font-size: 11.5px; font-weight: 500; color: #626D88;"> / 5만원</span></span></div>'
    f'<div style="position: relative; height: 6px; border-radius: 99px; background: #EFF2F8; margin-top: 6px; overflow: hidden;">'
    f'<div style="position: absolute; inset: 0 0 0 0; border-radius: 99px; background: #64748b;"></div></div>'
    f'<div style="display: flex; align-items: center; gap: 6px; margin-top: 6px;"><span style="font-size: 11.5px; color: #626D88; white-space: nowrap;">{SUBLINE}</span>{imark(1)}'
    f'<span style="margin-left: auto; font-size: 11.5px; font-weight: 600; color: #3556E6; white-space: nowrap; flex-shrink: 0;">분류하기 &rsaquo;</span></div>'
    f'</div>'
    f'<span style="font-size: 12px; font-weight: 600; color: #626D88; width: 32px; text-align: right; flex-shrink: 0; margin-top: 7px;">120%</span></div>')
rejudge_line = (f'<div style="display: flex; align-items: flex-start; gap: 4px; margin-top: 10px; padding-top: 10px; border-top: 1px solid #F3F5FA;">'
                f'<span style="font-size: 11.5px; line-height: 1.5; color: #626D88;">{REJUDGE}</span>{imark(2)}</div>')
# 카테고리 카드: 교통 · 쇼핑 줄을 빼고(자리를 줄이려고) `기타` 줄과 재판정 한 줄을 붙인다
ROW46 = '<div style="display: flex; align-items: center; gap: 10px; height: 46px;">'
assert sp_cats.count(ROW46) == 5
r4 = [m_.start() for m_ in re.finditer(re.escape(ROW46), sp_cats)][3]
spend_etc = sp_cats[:r4].rstrip() + '\n\n        ' + etc_row_spend + '\n      </div>\n      ' + rejudge_line + '\n    </div>'
assert balanced(spend_etc) and spend_etc.count(SUBLINE) == 1

LROW_LAST = '<div style="display: flex; align-items: center; gap: 10px; height: 44px;">'
LROW = '<div style="display: flex; align-items: center; gap: 10px; height: 44px; border-bottom: 1px solid #F3F5FA;">'
MORE = '<div style="display: flex; align-items: center; justify-content: center; gap: 5px; height: 38px; margin-top: 6px; border-top: 1px solid #F3F5FA;'
assert lm_cats.count(LROW) == 5 and lm_cats.count(LROW_LAST) == 1 and lm_cats.count(MORE) == 1
l3 = [m_.start() for m_ in re.finditer(re.escape(LROW), lm_cats)][3]          # 주거/관리 · 식비 · 쇼핑까지 두고 `기타`
etc_row_limit = (
    f'<div style="padding: 0 0 9px;">{LROW_LAST}'
    f'<span style="width: 8px; height: 8px; border-radius: 3px; background: #64748b; flex-shrink: 0;"></span>'
    f'<span style="font-size: 13.5px; font-weight: 500; color: #101828; width: 68px; flex-shrink: 0;">기타</span>'
    f'<div style="flex: 1; min-width: 0; position: relative; height: 6px; border-radius: 99px; background: #EFF2F8; overflow: hidden;">'
    f'<div style="position: absolute; inset: 0 0 0 0; border-radius: 99px; background: #64748b;"></div></div>'
    f'<span style="font-size: 13px; font-weight: 600; color: #101828; width: 74px; text-align: right; flex-shrink: 0;">6<span style="font-size: 11.5px; font-weight: 500; color: #626D88;"> / 5만</span></span></div>'
    f'<div style="display: flex; align-items: center; gap: 6px; padding-left: 18px; margin-top: -6px;"><span style="font-size: 11.5px; color: #626D88; white-space: nowrap;">{SUBLINE}</span>{imark(3)}</div></div>')
fixed_line = (f'<div style="display: flex; align-items: flex-start; gap: 4px; padding: 10px 0 4px; border-top: 1px solid #F3F5FA;">'
              f'<span style="font-size: 11.5px; line-height: 1.5; color: #626D88;">{FIXED_LIMIT}</span>{imark(4)}</div>')
limit_etc = lm_cats[:l3].rstrip() + '\n\n        ' + etc_row_limit + '\n\n      </div>\n\n      ' + fixed_line + '\n    </div>'
assert balanced(limit_etc) and limit_etc.count(SUBLINE) == 1

# 코치 — `소비 기록이 필요합니다` 본문에 `소비 없음 확인 n일` 병기(v5-2 — 안 썼어요가 생긴 뒤)
NEED_BODY = '이번 달 소비 기록이 아직 없어요 · 소비 없음 확인 3일'          # 제안 — 앞 절은 계획에 원문 없음(`소비 없음 확인 n일`만 원문)
coach_need = mini_sheet('코칭', '저장된 기록을 보고 중요한 순서로 알려드려요.',
                        advice('sky', f'소비 기록이 필요합니다{imark(5)}', NEED_BODY, '소비 기록하기', 1))          # 번호는 제목 옆 — 본문 끝에 달면 269px 칸에서 번호만 둘째 줄로 떨어진다


# gen_rest.step 과 같은 모양(CoachEmpty 의 '두 가지만 있으면 시작합니다' 카드)
def step(num, title, body, action='', done=False, last=False):
    mk = (f'<span style="width: 24px; height: 24px; border-radius: 99px; background: {C["POS_SOFT"]}; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">{icon("check", 14, C["POS"], 3)}</span>'
          if done else
          f'<span style="width: 24px; height: 24px; border-radius: 99px; background: {C["BRAND"]}; color: #FFFFFF; display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 700; flex-shrink: 0;">{num}</span>')
    bb = '' if last else f' border-bottom: 1px solid {C["LINE_ROW"]};'
    return (f'<div style="display: flex; align-items: center; gap: 11px; min-height: 52px;{bb}">{mk}<div style="flex: 1; min-width: 0;">'
            f'<div style="font-size: 13.5px; font-weight: 600; color: {C["INK"] if not done else C["INK3"]};">{title}</div>'
            f'<div style="font-size: 11.5px; color: {C["INK4"]}; margin-top: 2px;">{body}</div></div>{action}</div>')


coach_empty_steps = card(
    f'<div style="font-size: 12.5px; font-weight: 600; color: {C["INK2"]}; margin-bottom: 4px;">두 가지만 있으면 시작합니다</div>'
    + step('1', '월 실수령 급여', '360만원', done=True)
    + step('2', '이번 달 소비 기록 3건', f'카테고리별 비교가 가능해지는 최소치 · 소비 없음 확인 3일{imark(6)}',
           f'<span style="font-size: 11.5px; font-weight: 600; color: {C["INK4"]}; flex-shrink: 0; white-space: nowrap;">0 / 3건</span>', last=True),
    pad='14px 15px').replace(' flex-shrink: 0;', '', 1)

etc_memo = memo_box([
    (1, f'소비 · 이번 달의 카테고리별 소비 — {code("기타")} 줄 아래 {code(SUBLINE)}. 금액 · 막대 · 120%는 엔진 값 그대로(분류 안 함도 소비이고 한도 사용량입니다).'),
    (2, f'{code("기타 한도")} 경고와 코치의 최대 카테고리 비중은 분류 안 한 금액을 뺀 28,000원(56%)으로 다시 판단합니다. 그래서 120%인데도 경고가 없고, 무엇이 달라졌는지 카드 아래 한 줄로 말합니다. 분류하면 원래 판정으로 돌아갑니다.'),
    (3, f'소비 · 한도의 카테고리 배분에도 같은 서브라인. 줄 높이 44는 그대로 두고 그 아래 한 줄을 더합니다.'),
    (4, f'직접 정한 고정비 한도는 고정비 예상에 반영하지 않는다(계획 §12-15)는 사실을 배분 카드 맨 아래 문장으로 적습니다.'),
    (5, f'코치 {code("소비 기록이 필요합니다")} — 판정은 그대로 두고 본문에 {code("소비 없음 확인 n일")}을 함께 적어, 안 썼다고 표시한 날이 미입력처럼 보이지 않게 합니다(2단계 — 안 썼어요가 생긴 뒤).'),
    (6, f'코칭 · 기록 없음(CoachEmpty)의 소비 기록 줄에도 같은 말을 붙입니다. {code("0 / 3건")}은 그대로 — 안 쓴 날은 소비 기록 건수에 들어가지 않습니다.')])

etc_body = (f'<div style="display: flex; gap: 24px; align-items: flex-start;">'
            + col(362, [case(1, '소비 · 이번 달 — 카테고리별 소비', '기타 아래에 분류 안 한 몫을 따로 적습니다.', spend_etc)])
            + col(362, [case(3, '소비 · 한도 — 카테고리 배분', '같은 서브라인과 고정비 한도 문장.', limit_etc)])
            + col(362, [case(5, '코치 — 소비 기록이 없을 때', '안 썼다고 표시한 날 수를 함께 적습니다.', coach_need),
                        case(6, '코칭 · 기록 없음', '첫 실행 뒤의 빈 코칭에도 같은 말.', coach_empty_steps)])
            + '</div>' + etc_memo)
ETC_W, ETC_H = 1200, 970
w('EtcSubline', spec_frame(
    ETC_W, ETC_H, '분류 안 한 소비와 안 쓴 날 — 소비 · 한도 · 코치에서',
    '하루 시트에서 분류 없이 저장한 소비는 기타로 들어갑니다. 소비 · 한도 화면은 기타 아래에 그 몫을 따로 적고, '
    '코치는 안 썼다고 표시한 날을 미입력과 구분해 적습니다.',
    etc_body, sub_w=860), keep_all=True)


# ══════════════════════════════════════════════════════════════
# 4. LimitCardCases — 한도 카드 네 사례 + 코치 라벨 (rank 31 · v5-3)
# ══════════════════════════════════════════════════════════════
CHEV = ('<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#697182" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m9 18 6-6-6-6"/></svg>')
GRAD = 'linear-gradient(90deg, #6E6BEE 0%, #7A3FE4 100%)'          # 홈 한도 카드(Main)의 막대 그대로


def limit_case(label, right=None, right_color=None, below=None, used_pct=0.0):
    """홈 `이번 달 한도` 카드. label = 제목 옆 회색 글, below = 길어서 둘째 줄로 내린 글(원문 한 덩어리 그대로), right = 오른쪽 `남은 한도 …`."""
    lab = f' <span style="font-weight: 500; color: #626D88;">{label}</span>' if label else ''
    r = f'<span style="font-size: 13.5px; font-weight: 600; color: {right_color or C["POS"]}; white-space: nowrap; flex-shrink: 0;">{right}</span>' if right else ''
    b = f'<div style="margin-top: 3px; font-size: 13.5px; font-weight: 500; color: #626D88;">{below}</div>' if below else ''
    fill = (f'<div style="position: absolute; inset: 0 {100 - used_pct:g}% 0 0; border-radius: 99px; background: {GRAD};"></div>' if used_pct > 0 else '')
    return (f'<div style="background: #FFFFFF; border: 1px solid #E3E8F1; border-radius: 18px; padding: 12px 14px;">'
            f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px;">'
            f'<span style="font-size: 13.5px; font-weight: 600; color: #101828; white-space: nowrap;">이번 달 한도{lab}</span>'
            f'<div style="display: flex; align-items: center; gap: 4px;">{r}{CHEV}</div></div>{b}'
            f'<div style="position: relative; height: 8px; border-radius: 99px; background: #E8ECF5; margin-top: 9px; overflow: hidden;">{fill}</div></div>')


DASH = f'<span style="color: {C["DIS"]};">—</span>'
lc_none = limit_case(None, right=f'남은 한도 {DASH}', right_color=C["INK3"], below=f'앞으로 하루 {DASH} · 한도를 아직 안 정했어요')
lc_zero = limit_case('앞으로 하루 0원', right='남은 한도 0원', right_color=C["INK"], used_pct=100)
lc_over = limit_case(None, right='남은 한도 0원', right_color=C["INK"], below='앞으로 하루 0원 · 한도보다 32,000원 많아요', used_pct=100)
lc_last = limit_case('이번 달 남은 한도 90,000원', used_pct=95.8)
lc_base = limit_forward().replace(' flex-shrink: 0;">', '">', 1)
assert lc_base.count('앞으로 하루 47,270원') == 1

# 한도 탭 맨 위 카드의 같은 줄 · 코치 본문(# 제안 — 라벨을 뺀 앞뒤 문장은 계획에 원문 없음)
lm_line = (f'<div style="background: {C["SURF"]}; border: 1px solid {C["LINE"]}; border-radius: 14px; padding: 11px 14px; display: flex; align-items: center; justify-content: space-between; gap: 8px;">'
           f'<span style="font-size: 11.5px; color: #626D88; white-space: nowrap;">사용 112만원 · 52%</span>'
           f'<span style="font-size: 11.5px; color: #626D88; white-space: nowrap;">22일 남음 · 앞으로 하루 47,270원</span></div>')
coach_daily = advice('warn', '주거/관리가 한도의 94%예요', '이번 달 한도는 104만원 남았어요. 앞으로 하루 47,270원씩 쓰면 한도 안이에요.', '카테고리 한도 보기', 1)
coach_last = advice('warn', '주거/관리가 한도의 94%예요', '오늘이 이번 달 마지막 날이에요. 이번 달 남은 한도 90,000원', '카테고리 한도 보기', 1)

lc_left = (f'<div style="width: 362px; flex-shrink: 0; display: flex; flex-direction: column; gap: 8px;">'
           f'<div><div style="font-size: 14px; font-weight: 700; letter-spacing: -0.01em; color: {C["INK"]};">평소 — 한도가 남아 있을 때</div>'
           f'<div style="font-size: 12px; line-height: 1.5; color: {C["INK3"]}; margin-top: 3px;">남은 한도 ÷ 남은 일수. 홈의 하루 숫자는 이것 하나입니다.</div></div>{lc_base}'
           f'<p style="margin: 2px 2px 0; font-size: 12px; line-height: 1.5; color: {C["INK3"]};">오른쪽 네 경우는 모두 <b style="font-weight: 600; color: {C["INK2"]};">제목 옆 회색 글 자리</b>가 바뀌는 것입니다. '
           f'글이 길어 한 줄에 안 들어가면 줄이지 않고 둘째 줄로 내립니다.</p>'
           f'<div style="margin-top: 14px; display: flex; flex-direction: column; gap: 8px;">{case_cap(5, "소비 · 한도 맨 위 카드", "남은 일수 옆 하루 금액도 같은 라벨.")}{lm_line}</div></div>')
lc_grid = (f'<div style="flex: 1; min-width: 0; display: grid; grid-template-columns: repeat(2, 362px); gap: 24px 20px; align-items: start;">'
           + case(1, '한도를 아직 안 정했을 때', '0이 아니라 회색 —. 막대도 비어 있습니다.', lc_none)
           + case(2, '남은 한도가 꼭 0원일 때', '남은 날이 있고 남은 한도가 실제로 0.', lc_zero)
           + case(3, '한도를 넘었을 때', '0원에 넘은 금액을 함께 적습니다.', lc_over)
           + case(4, '이번 달 마지막 날', '남은 일수가 0이라 하루 금액 대신 남은 총액.', lc_last)
           + case(6, '코치 — 평소', '본문의 하루 금액도 같은 값 · 같은 라벨.', coach_daily)
           + case(7, '코치 — 마지막 날', '한도 카드와 같은 문구로 바뀝니다.', coach_last)
           + '</div>')
LC_MEMO_ROWS = [
    (1, f'{code("앞으로 하루 — · 한도를 아직 안 정했어요")} — 한도 미입력. 0원과 합치지 않습니다.'),
    (2, f'{code("앞으로 하루 0원")} — 남은 일수가 있고 남은 한도가 실제 0원일 때만.'),
    (3, f'{code("앞으로 하루 0원 · 한도보다 32,000원 많아요")} — 초과. 넘은 금액을 같은 줄에 적습니다.'),
    (4, f'{code("이번 달 남은 한도 90,000원")} — 남은 일수 0. 지금 계산은 이날 하루 금액을 0으로 돌려주므로 한도가 남아도 0원이 됩니다. 분모는 그대로 두고 그날만 남은 총액을 같은 자리에 보여 줍니다.'),
    (5, f'{code("22일 남음 · 앞으로 하루 47,270원")} — 소비 · 한도 맨 위 카드의 남은 일수 옆 하루 금액도 같은 라벨입니다.'),
    (6, f'코치 본문의 {code("하루 X씩")}은 {code("앞으로 하루 47,270원씩")}으로 한도 카드와 같게 씁니다.'),
    (7, f'코치 — 남은 일수 0이면 본문도 {code("이번 달 남은 한도 90,000원")}으로, 한도 카드의 마지막 날과 같은 문구로 씁니다.')]
assert [n_ for n_, _ in LC_MEMO_ROWS] == [1, 2, 3, 4, 5, 6, 7]          # 그림의 번호 1~7 과 메모 번호가 같아야 한다
lc_memo = memo_box(LC_MEMO_ROWS)
LC_W, LC_H = 1200, 960          # 메모 5 · 7번 두 줄(줄마다 약 34px)이 늘어 930 → 960. gen_canvas.py · screens.json 의 크기도 같아야 한다
w('LimitCardCases', spec_frame(
    LC_W, LC_H, '이번 달 한도 카드 — 하루 금액 자리의 네 가지 경우',
    '3단계에서 홈 한도 카드의 하루 47,270원이 앞으로 하루 47,270원으로 바뀝니다. 한도가 없을 때 · 0원일 때 · 넘었을 때 · 마지막 날을 같은 표시로 합치지 않습니다.',
    f'<div style="display: flex; gap: 32px; align-items: flex-start;">{lc_left}{lc_grid}</div>{lc_memo}', sub_w=860), keep_all=True)


# ══════════════════════════════════════════════════════════════
# 5. RecurringPrefill — 반복 거래 다이얼로그 미리 채움 (rank 31 · v5-3 · 앱 화면 390 × 844)
# ══════════════════════════════════════════════════════════════
# 하루 시트에서 9월 8일 월세 700,000원을 주거/관리로 저장 → 완료 카드 `매달 반복으로 만들기 ›` → 이 창. RecurringDialog(gen_modals)와 같은 틀.
# 등록된 목록은 v5 자료에 맞춘다 — `ETF 자동이체` 매월 6일(달력 · LedgerV5 의 9월 6일 이체) · `휴대폰 요금` 55,000원 · 25일 — 9월 8일 기준 LedgerV5 에 통신 자동 기록이 아직 없는 것과도 맞는다(25일 전).
rules = []
for i, (name, meta, amt, on) in enumerate([("ETF 자동이체", "매월 6일 · 저축/투자", "30만원", True),      # LedgerV5 9월 6일 자동 기록 · 달력 9월 6일 · 8월 6일 이체 배지와 같은 날. v3 RecurringDialog 는 `매월 5일` 그대로
                                           ("휴대폰 요금", "매월 25일 · 통신", "5.5만원", True),      # v5 장의 반복 규칙과 같은 값 — DaySheetConfirm `이번 달 휴대폰 요금 55,000원은 25일에 자동으로 기록돼요`(계획 §4-3 · §8). v3 RecurringDialog 는 `매월 5일 · 2만원` 그대로
                                           ("헬스장", "일시정지됨 · 문화/여가", "5만원", False)]):
    c_ = C["INK"] if on else C["INK4"]
    bb = f'border-bottom: 1px solid {C["LINE_ROW"]};' if i < 2 else ''
    rules.append(
        f'<div style="display: flex; align-items: center; gap: 10px; min-height: 52px; {bb}">'
        f'<div style="flex: 1; min-width: 0;"><div style="font-size: 13.5px; font-weight: 600; color: {c_};">{name}</div>'
        f'<div style="font-size: 11px; color: {C["INK4"] if not on else C["INK3"]};">{meta}</div></div>'
        f'<span style="font-size: 13.5px; font-weight: 600; color: {c_};">{amt}</span>'
        f'{toggle(on)}{icon("more", 16, C["INK4"], 2.2)}</div>')
PREFILL_NOTE = '이번 달 건은 방금 저장한 거래로 이미 있어요'          # 계획 §8 원문
w('RecurringPrefill', sheet(
    '반복 거래', '매달 자동으로 만들어지는 거래예요. 끄면 다음 달부터 생성되지 않습니다.',
    group('새 반복 거래',
          f'<div style="display: flex; gap: 10px;">{field("이름", "월세", required=True)}{field("금액", "700,000", "원", required=True, w=142)}</div>'
          f'<div style="display: flex; gap: 10px; margin-top: 12px;">{select_field("카테고리", "주거/관리")}{field("결제일", "8", "일", w=88)}'
          f'{field("시작 월", "2026.10", w=104)}</div>'
          f'<div style="margin-top: 11px;">{note(PREFILL_NOTE, "mute")}</div>'
          f'<div style="margin-top: 8px;">{note("이미 지난 달에는 만들어지지 않아요. 이미 만들어진 거래는 하나씩 고치거나 지울 수 있어요.", "mute")}</div>',
          meta='방금 저장한 거래에서 채웠어요') +
    group('등록된 반복 거래', f'<div style="padding: 0 13px; background: {C["SURF"]}; border: 1px solid {C["LINE"]}; border-radius: 14px;">{"".join(rules)}</div>',
          meta='3건 · 활성 2건'),
    sheet_footer('닫기', '반복 거래 추가'), scrim_h=40), keep_all=True)


# ══════════════════════════════════════════════════════════════
# 6. ImportBackupNotes — 가져오기 · 백업 안내 문구 (rank 31 · v5-3)
# ══════════════════════════════════════════════════════════════
IMPORT_NOTE = '가져온 기록의 분류 안 함 표시도 함께 와요 · 확인 표시는 전체 복원에서만 돌아와요 · 이미 있는 기록은 그대로예요'                     # 계획 §8 원문
BACKUP_NOTE = '확인 표시와 분류 안 함 표시도 함께 저장돼요 · 골라서 가져오기에서는 새로 가져온 기록의 분류 안 함 표시만 따라와요 · 확인 표시는 전체 복원에서만 돌아와요'   # 계획 §9-14 원문
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
               f'<span style="font-size: 12.5px; line-height: 1.5; color: {C["INK2"]};">바뀌는 내용을 확인했습니다.</span></div>')
import_sheet = sheet(
    '백업 불러오기', 'navi-backup-2026-09-01.json · 기록 35건<br>적용하기 전에 무엇이 바뀌는지 먼저 확인하세요.',
    group('적용 방식', segmented(['기존에 추가', '전체 교체'], 0) +
          f'<div style="margin-top: 9px;">{note("추가는 겹치지 않는 기록만 넣습니다. 전체 교체를 고르면 현재 기록이 모두 사라져요.", "mute")}</div>') +
    group('불러올 항목', f'<div style="padding: 0 13px; background: {C["SURF"]}; border: 1px solid {C["LINE"]}; border-radius: 14px;">'
                          f'{diffrow("새로 추가", 24, "new", "거래 21 · 자산 2 · 목적지 1")}'
                          f'{diffrow("이미 있는 기록", 8, "dup", "같은 거래라 건너뜁니다")}'
                          f'{diffrow("값이 다른 기록", 2, "conf", "자산 평가액 2건 · 백업 파일 값으로 바뀝니다")}'
                          f'{diffrow("검토 필요", 1, "chk", "연결된 계좌가 없는 거래 1건", last=True)}</div>'
                          f'<div style="display: flex; align-items: flex-start; gap: 4px; margin-top: 8px; padding: 0 2px;">'
                          f'<span style="font-size: 11.5px; line-height: 1.5; color: {C["INK3"]};">{IMPORT_NOTE}</span>{imark(1)}</div>') +
    group('적용 후', f'<div style="display: flex; gap: 8px;">'
                      f'<div style="flex: 1; padding: 12px; background: {C["INSET"]}; border-radius: 13px;">'
                      f'<div style="font-size: 11.5px; color: {C["INK3"]};">지금</div>'
                      f'<div style="font-size: 18px; font-weight: 600; color: {C["INK"]}; margin-top: 3px;">거래 132건</div>'
                      f'<div style="font-size: 11.5px; color: {C["INK3"]}; margin-top: 2px;">순자산 9,350만원</div></div>'
                      f'<div style="display: flex; align-items: center;">{icon("arrowr", 16, C["INK4"], 2.2)}</div>'
                      f'<div style="flex: 1; padding: 12px; background: {C["BRAND_SOFT"]}; border-radius: 13px;">'
                      f'<div style="font-size: 11.5px; color: {C["BRAND"]};">적용 후</div>'
                      f'<div style="font-size: 18px; font-weight: 600; color: {C["INK"]}; margin-top: 3px;">거래 153건</div>'
                      f'<div style="font-size: 11.5px; color: {C["INK3"]}; margin-top: 2px;">순자산 9,410만원</div></div></div>'),
    sheet_footer('취소', '이 내용으로 적용'),
    sticky=f'<div style="padding: 12px 18px; background: {C["INSET"]}; border-top: 1px solid {C["LINE"]}; flex-shrink: 0;">{checkbox_on}</div>', scrim_h=40)
import_left = f'<div style="width: 390px; flex-shrink: 0; border-radius: 24px; overflow: hidden;">{import_sheet}</div>'

# ② 백업 안내 — 내 수치 입력(ProfileDialog)의 `데이터` 구역, 버튼 아래
backup_part = (f'<div style="background: {C["SURF"]}; border: 1px solid {C["LINE"]}; border-radius: 18px; padding: 14px;">'
               + group('데이터', f'<div style="display: flex; gap: 8px;">'
                                 f'{btn("백업 내보내기", "secondary", "download", h=44).replace("width: 100%;", "flex: 1;")}'
                                 f'{btn("불러오기", "secondary", "upload", h=44).replace("width: 100%;", "flex: 1;")}</div>'
                                 f'<div style="margin-top: 9px;">{note(BACKUP_NOTE, "mute")}</div>')
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
              f'<span style="flex: 1; font-size: 11.5px; font-weight: 600; color: {C["INK3"]};">분류 안 함 표시</span><span style="flex: 1; font-size: 11.5px; font-weight: 600; color: {C["INK3"]};">확인 표시(다 적었어요 · 안 썼어요)</span></div>'
              + path_row('전체 복원', '그대로 돌아옵니다', '그대로 돌아옵니다')
              + path_row('골라서 가져오기', '새로 추가된 기록의 표시만 따라옵니다. 이미 있어 건너뛴 기록에는 씌우지 않습니다', '오지 않습니다. 소비가 새로 들어간 날짜의 지금 확인만 풀립니다')
              + path_row('같은 파일을 다시', '사용자가 뺀 표시를 되살리지 않습니다', '바뀌지 않습니다', last=True) + '</div>')
ib_memo = memo_box([
    (1, f'가져오기 화면 — 불러올 항목 목록 바로 아래 회색 글 한 줄(두 줄로 접힘). 상자를 더하지 않아 적용 후 · 확인란이 밀려나지 않습니다.'),
    (2, f'백업 안내 — 내 수치 입력의 데이터 구역, 백업 내보내기 · 불러오기 버튼 아래 안내 상자.'),
    (3, f'가져온 소비가 안 썼어요로 표시한 날에 들어가면 그 날의 표시가 풀리고, 달력 카드에서 {code("9월 5일 표시가 풀렸어요 · 다시 표시")}로 알립니다. 의미색 없이 중립 상자입니다.')])
ib_right = (f'<div style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 22px;">'
            f'<div style="display: grid; grid-template-columns: repeat(2, 362px); gap: 22px 20px; align-items: start;">'
            + case(2, '백업을 내보내는 자리', '무엇이 파일에 들어가고 어떻게 돌아오는지.', backup_part)
            + case(3, '가져온 뒤 — 표시가 풀린 날', '안 썼어요로 표시한 날에 소비가 들어왔을 때.', uncheck_part)
            + '</div>'
            + f'<div style="display: flex; flex-direction: column; gap: 8px;"><div style="font-size: 14px; font-weight: 700; letter-spacing: -0.01em; color: {C["INK"]};">경로마다 돌아오는 것</div>{path_table}</div>'
            + ib_memo + '</div>')
IB_W, IB_H = 1230, 1060
w('ImportBackupNotes', spec_frame(
    IB_W, IB_H, '가져오기 · 백업 — 확인 표시와 분류 안 함 표시가 어떻게 따라오는지',
    '달력의 확인 표시(다 적었어요 · 안 썼어요)와 분류 안 함 표시는 백업 파일에 함께 들어갑니다. 전체 복원과 골라서 가져오기가 다르게 돌려주므로 두 화면에 그 사실을 적습니다.',
    f'<div style="display: flex; gap: 32px; align-items: flex-start;">{import_left}{ib_right}</div>', sub_w=860), keep_all=True)

NEW = {'InsufficientElsewhere': (INS_W, INS_H), 'FutureProvisional': (FUT_W, FUT_H), 'EtcSubline': (ETC_W, ETC_H),
       'LimitCardCases': (LC_W, LC_H), 'RecurringPrefill': (390, 844), 'ImportBackupNotes': (IB_W, IB_H)}
if __name__ == '__main__':
    for n_, (w_, h_) in NEW.items():
        print(f'{n_}: {w_} × {h_}')
