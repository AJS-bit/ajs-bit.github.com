# -*- coding: utf-8 -*-
"""라이트 아트보드를 다크 토큰으로 변환한다. 데이터 팔레트와 브랜드 그라디언트는 유지."""
import re
import pathlib

SRC = pathlib.Path(__file__).resolve().parent.parent

MAP = {
    '#EDF0F7': '#080C16',   # canvas
    '#FFFFFF': '#121A2B',   # surface
    '#F8FAFD': '#151D30',
    '#FAFBFD': '#151D30',   # 강조 행
    '#E3E8F1': '#232D45',   # line
    '#EFF2F8': '#1E2739',   # line-soft
    '#F3F5FA': '#1E2739',   # line-row
    '#E8ECF5': '#232D45',   # track
    '#F4F6FB': '#1A2337',   # inset
    '#F0F2F7': '#1E2739',   # mute badge bg
    '#101828': '#EAEFF8',   # ink
    '#475467': '#A5B2C9',   # ink-2
    '#5B6880': '#8595AE',
    '#626D88': '#8595AE',   # ink-3
    '#697182': '#7E8AA2',   # ink-4
    '#606B7D': '#8A95AB',
    '#B4BECD': '#5D6B85',   # disabled
    '#C4CCDA': '#46536E',
    '#D7DEEA': '#2E3A54',
    '#CFD7E6': '#39455F',   # input line
    '#B9C3D6': '#4E5B76',
    '#D6DDE9': '#2E3A54',
    '#DCE2EC': '#263049',
    '#3556E6': '#7FA0FF',   # brand
    '#2743C4': '#A8BCF5',
    '#E9EDFD': '#1B2748',   # brand soft
    '#3B4E8F': '#A8BCF5',
    '#6B85EC': '#5E7DDA',   # saving
    '#8FA6F2': '#6C86D8',
    '#4B6BDE': '#8FA6F2',
    '#0F7B47': '#3DD489',   # positive
    '#E4F4EA': '#0F2C22',
    '#9CCDB2': '#2A6B4A',
    '#C9E5D5': '#1E4534',
    '#14603D': '#8FD9B4',
    '#6FBE94': '#2A6B4A',
    '#B45309': '#F5B544',   # warning
    '#FDF1E0': '#2E2617',
    '#DE8A2A': '#A9772C',
    '#7A3E0A': '#F0C88A',
    '#C0342F': '#E8635F',   # negative
    '#FCEBEA': '#331C1F',
    '#D9827E': '#8E4C49',
    '#7C221E': '#FFB3B0',
    '#7A3FE4': '#B79BFF',   # violet
    '#6E6BEE': '#9AA0FF',
    '#F1EAFD': '#241D3D',
    '#6B32D6': '#C4A9FF',
    '#4E2496': '#C9B4FF',
    '#F7F4FE': '#1E1B33',
    '#B79BFF': '#B79BFF',
    '#0A72AC': '#5CC3F5',   # sky
    '#E4F2FB': '#12293C',
    '#0A5F8F': '#9CD8F5',
    '#7EC4E8': '#2A5A78',
    '#2A3245': '#04070E',   # modal scrim
}
KEYS = sorted(MAP, key=len, reverse=True)
PAT = re.compile('|'.join(re.escape(k) for k in KEYS), re.IGNORECASE)

BRAND_GRAD_DARK = 'linear-gradient(140deg, #7FA0FF 0%, #B79BFF 100%)'
BRAND_GRAD = 'linear-gradient(140deg, #3556E6 0%, #7A3FE4 100%)'
ARROW = 'M20.28 2.32 2.88 9.62c-.9.4-.8 1.7.1 2l6.6 2.2c.3.1.5.3.6.6l2.2 6.6c.3.9 1.6 1 2 .1L21.68 3.72c.3-.8-.6-1.7-1.4-1.4Z'


KEEP = re.compile(r'<!--dc-keep-->(.*?)<!--/dc-keep-->', re.S)

# ── 다크에서도 '떠 있어야' 하는 두 요소 ────────────────────────────────────────────────
# 라이트의 꺼진 토글 손잡이와 세그먼트 선택 칸은 흰색(#FFFFFF)이 트랙보다 밝아서 떠 보인다.
# MAP 대로 #FFFFFF → surface(#121A2B)로 바꾸면 다크에서는 트랙(#232D45 · #1A2337)보다 어두워져
# 손잡이는 구멍처럼, 선택 칸은 파인 자리처럼 보인다. 그래서 이 둘만 MAP 보다 먼저 집어 따로 칠한다.
# 켜진 토글(브랜드 트랙 #7FA0FF 위 surface 손잡이 · 6.9:1)은 잘 읽히므로 그대로 둔다.
KNOB_OFF_DARK = '#8595AE'   # 꺼진 토글 손잡이 = ink-3 · 트랙 #232D45 위 4.5:1
# 세그먼트 선택 칸 = 트랙보다 밝은 표면. 열쇠는 라이트 트랙 색 — 화면 탭(#E3E8F1 → 다크 트랙 #232D45 · 그 위 1.21:1, 라이트는 1.23:1)과
# 모달(#F4F6FB → 다크 트랙 #1A2337 · 그 위 1.38:1). 지금은 두 곳이 같은 값이다
SEG_ON_DARK = {'#E3E8F1': '#2E3A54', '#F4F6FB': '#2E3A54'}

# 꺼진 토글 = 알약 트랙(#E3E8F1 · flex-start) 바로 안의 둥근 흰 손잡이. 46 × 27(모바일) · 34 × 20(데스크톱) 둘 다 잡는다
TOGGLE_OFF = re.compile(
    r'(<(?:div|span)\s+style="[^"]*?border-radius:\s*99px;\s*background:\s*#E3E8F1;[^"]*?justify-content:\s*flex-start;[^"]*"\s*>\s*'
    r'<span\s+style="[^"]*?border-radius:\s*99px;\s*background:\s*)#FFFFFF(\s*;?\s*"\s*>\s*</span>)', re.I)
# 세그먼트 = 트랙(#E3E8F1 화면 탭 · #F4F6FB 모달) 바로 안에 글자만 든 칸이 늘어선 것. 그 안에서 흰 칸(선택)만 바꾼다
SEG_TRACK = re.compile(
    r'<div\s+style="display:\s*flex;\s*gap:\s*\d+px;\s*background:\s*(#E3E8F1|#F4F6FB);\s*border-radius:\s*\d+px;\s*padding:\s*\d+px;?\s*"\s*>'
    r'(?:\s*<div\s+style="[^"]*"\s*>[^<]*</div>)+\s*</div>', re.I)
SEG_CELL_ON = re.compile(r'(<div\s+style="[^"]*?background:\s*)#FFFFFF(\s*;[^"]*"\s*>)', re.I)
# 검산용 — 위 정규식이 놓친 토글 · 세그먼트가 있으면(마크업이 달라졌으면) 조용히 넘어가지 않고 멈춘다
_STYLE = re.compile(r'style="([^"]*)"')
_SEG_SHADOW = re.compile(r'box-shadow:\s*0 1px 2px rgba\(16,24,40,\.0[68]\)\s*;?\s*$')
_PILL = re.compile(r'border-radius:\s*99px', re.I)
_TRACK_OFF = re.compile(r'background:\s*#E3E8F1', re.I)
_KNOB_LEFT = re.compile(r'justify-content:\s*flex-start', re.I)
_KNOB, _SEG = '\x00KNOB\x00', '\x00SEG{}\x00'   # _SEG 의 {} = 라이트 트랙 색에서 # 을 뗀 것(# 이 붙어 있으면 MAP 이 표시까지 바꿔 버린다)


def _lift(text, name=''):
    """꺼진 토글 손잡이 · 세그먼트 선택 칸의 #FFFFFF 를 표시로 바꿔 둔다(MAP 치환 뒤에 다크 값으로 채운다)."""
    styles = _STYLE.findall(text)
    want_knob = sum(1 for s in styles if _PILL.search(s) and _TRACK_OFF.search(s) and _KNOB_LEFT.search(s))
    want_seg = sum(1 for s in styles if '#FFFFFF' in s.upper() and _SEG_SHADOW.search(s.strip()))
    text, got_knob = TOGGLE_OFF.subn(lambda m: m.group(1) + _KNOB + m.group(2), text)
    got_seg = 0

    def _track(m):
        nonlocal got_seg
        mark = _SEG.format(m.group(1).upper().lstrip('#'))
        block, n = SEG_CELL_ON.subn(lambda c: c.group(1) + mark + c.group(2), m.group(0))
        got_seg += n
        return block

    text = SEG_TRACK.sub(_track, text)
    assert got_knob == want_knob, f'{name}: 꺼진 토글 {want_knob}개 중 {got_knob}개만 잡혔다 — TOGGLE_OFF 를 마크업에 맞출 것'
    assert got_seg == want_seg, f'{name}: 세그먼트 선택 칸 {want_seg}개 중 {got_seg}개만 잡혔다 — SEG_TRACK 을 마크업에 맞출 것'
    return text


def darken(text, name='', knob=KNOB_OFF_DARK, seg=None):
    # <!--dc-keep-->…<!--/dc-keep--> 구간은 라이트/다크가 같아야 하는 반전 요소
    # (어두운 배경 위 흰 글자 토스트 등)이라 매핑에서 제외한다.
    kept = []

    def _stash(m):
        kept.append(m.group(1))
        return f'\x00KEEP{len(kept) - 1}\x00'

    text = KEEP.sub(_stash, text)
    text = _lift(text, name)
    out = PAT.sub(lambda m: MAP[m.group(0).upper()], text)
    out = out.replace(_KNOB, knob)
    for track, on in (seg or SEG_ON_DARK).items():
        out = out.replace(_SEG.format(track.upper().lstrip('#')), on)
    out = out.replace('rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)',
                      'rgba(0,0,0,.3), 0 10px 28px -16px rgba(0,0,0,.7)')
    out = out.replace('rgba(16,24,40,.04), 0 8px 24px -16px rgba(16,24,40,.28)',
                      'rgba(0,0,0,.3), 0 12px 32px -18px rgba(0,0,0,.75)')
    # 팝오버 메뉴(내역 ⋯) 그림자 — 아래 .04 치환보다 먼저
    out = out.replace('rgba(16,24,40,.04), 0 12px 28px -12px rgba(16,24,40,.32)',
                      'rgba(0,0,0,.3), 0 14px 32px -14px rgba(0,0,0,.8)')
    # 점선 추가 버튼의 반투명 흰 바탕 — 그대로 두면 다크에서 회색 덩어리가 되어 글자가 안 읽힌다
    out = out.replace('background: rgba(255,255,255,.55)', 'background: rgba(255,255,255,.03)')
    out = out.replace('rgba(16,24,40,.06)', 'rgba(0,0,0,.45)')
    out = out.replace('rgba(16,24,40,.08)', 'rgba(0,0,0,.5)')
    out = out.replace('rgba(16,24,40,.2)', 'rgba(0,0,0,.6)')
    out = out.replace('rgba(16,24,40,.5)', 'rgba(0,0,0,.8)')
    # 브랜드 그라디언트와 마크 화살표는 라이트/다크 동일
    out = out.replace(BRAND_GRAD_DARK, BRAND_GRAD)
    out = re.sub(r'fill="#121A2B"(\s*><path d="' + re.escape(ARROW) + r')', r'fill="#FFFFFF"\1', out)
    # 부채 해치 패턴
    out = out.replace('#E0908C 0 4px, #F0BFBD 4px 8px', '#8E4C49 0 4px, #B36F6C 4px 8px')
    # 한도 초과 구간 빗금(ModalErrors B) — 빨강은 MAP이 바꾸고 옅은 줄만 여기서
    out = out.replace('#E8635F 0 4px, #E0908C 4px 8px', '#E8635F 0 4px, #8E4C49 4px 8px')
    assert '\x00SEG' not in out, f'{name}: SEG_ON_DARK 에 없는 트랙 색의 세그먼트가 있다'
    for i, k in enumerate(kept):
        out = out.replace(f'\x00KEEP{i}\x00', k)
    return out


SCREENS = ['Main', 'HomeScroll', 'Assets', 'Debts', 'Strategy', 'Spending', 'Ledger',
           'Limits', 'Goals', 'GoalDesign', 'Future', 'Payoff', 'Onboarding', 'SpendingPast']
MODALS = ['LimitEditor', 'TransactionAdd', 'ProfileDialog', 'AssetDialog', 'DebtDialog',
          'GoalDialog', 'RecurringDialog', 'MonthlyClose', 'ImportReview', 'CoachPanel',
          'AlertsPanel', 'AlertsEmpty', 'PeerDialog', 'GoalContribute', 'CoachEmpty']
STATES = ['StorageStates', 'EmptyStates', 'PeerStates', 'ModalErrors', 'Confirmations', 'GoalTypes']
SYSTEM = ['Components']
DESKTOP = ['DesktopHome', 'DesktopLedger']
V4 = ['IntroPosition', 'IntroRoute', 'IntroDestination', 'HomeSetup', 'HomeConfigured']   # gen_v4.py
V4 += ['DestGoals', 'DestFuture', 'HomeStocksOff', 'StocksMine', 'HoldingAdd', 'StocksEmpty', 'HomeStocksCard', 'StocksHome', 'StockListGrowth', 'StockListDividend', 'StockDetail', 'StockThemes', 'StockStates', 'StockSettings', 'SnapshotUpdate']   # gen_v4_stocks.py
V4 += ['HomeCalendarStrip', 'HomeCalendar', 'DaySheet', 'DaySheetList', 'DaySheetEdit', 'DoneCard', 'DaySheetConfirm', 'ClassifySheet', 'HeroInsufficient', 'DaySheet360', 'HeroFootnotes', 'CalendarCells', 'HomeCalendar360', 'HomeCalendarPrev', 'CalendarGridSizes']   # gen_v5.py (v5 1단계)
# 최신화 반영(2026-09-21) — 새 장. v3 생성기·손편집 산물은 여기서만 다크가 만들어진다
V5X = ['LedgerV5', 'MonthlyCloseV5', 'TransactionAddFromDaySheet', 'DesktopHomeV5']   # gen_screens · gen_modals · 손편집
V5X += ['HomeSetupStocksOn', 'SettingsHomeEntry', 'HomeLayoutEdit']   # gen_v4.py
V5X += ['DestPayoff']   # gen_v4_stocks.py
V5X += ['DaySheetScrolled', 'HomeDefaultScroll']   # gen_v5.py
V5X += ['DaySheetNoSpend', 'DaySheetNoSpendStates', 'ReviewListSheet', 'DoneCardStates', 'DaySheetStates', 'CalendarStatusLines']   # gen_v5_sheets.py
V5X += ['InsufficientElsewhere', 'FutureProvisional', 'EtcSubline', 'LimitCardCases', 'RecurringPrefill', 'ImportBackupNotes']   # gen_v5_screens.py

if __name__ == '__main__':
    n = 0
    for name in SCREENS + MODALS + STATES + SYSTEM + DESKTOP + V4 + V5X:
        src = SRC / f'{name}.dc.html'
        dst = SRC / ('DarkHome.dc.html' if name == 'Main' else f'Dark{name}.dc.html')
        dst.write_text(darken(src.read_text(encoding='utf-8'), name), encoding='utf-8')
        n += 1
    print(f'{n} dark artboards written')
