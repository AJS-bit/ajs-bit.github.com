# -*- coding: utf-8 -*-
import json
import pathlib

OUT = pathlib.Path(__file__).resolve().parent.parent

PHONE = (390, 844)
# 프레임 높이는 "실제 웹폰트로 렌더한 자연 높이 + 아래 여백 24px"이다.
# 폴백 폰트로 재면 한글 줄 높이가 짧게 나와 실제보다 작은 값이 나온다. 반드시 IBM Plex Sans KR로 재라.
TALL = {'StorageStates': 1324, 'PeerStates': 1555, 'EmptyStates': 2480, 'Confirmations': 1245,
        'ModalErrors': 2100, 'GoalTypes': 1920,
        'HomeDefaultScroll': 1330}   # v5 · 2단계 기본 5카드 홈 전체 스크롤
TALL.update({'Dark' + k: v for k, v in TALL.items()})
WIDE = {'DesktopHome': (1440, 900), 'DesktopLedger': (1440, 900), 'DarkDesktopHome': (1440, 900),
        'DarkDesktopLedger': (1440, 900),
        'DesktopHomeV5': (1440, 1000), 'DarkDesktopHomeV5': (1440, 1000),   # v5 달력이 들어간 데스크톱 홈(2026-09-21 채택)
        'Tokens': (1200, 1720), 'Components': (1200, 2724), 'DarkComponents': (1200, 2724),
        'DaySheet360': (360, 640), 'DarkDaySheet360': (360, 640),   # 작은 폰 360 × 640
        'HomeCalendar360': (360, 844), 'DarkHomeCalendar360': (360, 844),   # v5 좁은 폰
        # v5 구현 참고 장 — 폰 프레임이 아니라 가로로 넓은 설명 장
        'CalendarCells': (1330, 820), 'DarkCalendarCells': (1330, 820),
        'CalendarGridSizes': (1150, 1490), 'DarkCalendarGridSizes': (1150, 1490),
        'DaySheetConfirm': (1200, 900), 'DarkDaySheetConfirm': (1200, 900),
        'HeroFootnotes': (1200, 640), 'DarkHeroFootnotes': (1200, 640),
        # 최신화 반영(2026-09-21) — v5 구현 참고 장과 다른 화면에 닿는 곳
        'CalendarStatusLines': (1200, 1050), 'DarkCalendarStatusLines': (1200, 1050),
        'DaySheetNoSpendStates': (1200, 1160), 'DarkDaySheetNoSpendStates': (1200, 1160),
        'DoneCardStates': (1200, 1090), 'DarkDoneCardStates': (1200, 1090),
        'DaySheetStates': (1210, 1660), 'DarkDaySheetStates': (1210, 1660),
        'AlertsReview': (1200, 1040), 'DarkAlertsReview': (1200, 1040),
        'TransactionAddFromDaySheet': (960, 850), 'DarkTransactionAddFromDaySheet': (960, 850),
        'InsufficientElsewhere': (1230, 1330), 'DarkInsufficientElsewhere': (1230, 1330),
        'FutureProvisional': (1230, 1080), 'DarkFutureProvisional': (1230, 1080),
        'EtcSubline': (1200, 970), 'DarkEtcSubline': (1200, 970),
        'LimitCardCases': (1200, 960), 'DarkLimitCardCases': (1200, 960),
        'ImportBackupNotes': (1230, 1060), 'DarkImportBackupNotes': (1230, 1060),
        # v4 구현 참고 장 (gen_v4_stocks.py)
        'StockStates': (1180, 880), 'DarkStockStates': (1180, 880),
        'SnapshotUpdate': (1180, 762), 'DarkSnapshotUpdate': (1180, 762)}

TITLES = {
    'Main': '홈 · 오늘의 내비게이션', 'HomeScroll': '홈 · 아래로 스크롤',
    'Assets': '자산 · 구성', 'Debts': '자산 · 부채', 'Strategy': '자산 · 상환 전략',
    'Spending': '소비 · 이번 달', 'Ledger': '소비 · 내역', 'Limits': '소비 · 한도',
    'Goals': '목적지 · 내 목적지', 'GoalDesign': '목적지 · 새 목적지 설계',
    'Future': '미래 · 자산 경로', 'Payoff': '미래 · 상환 계획', 'Onboarding': '첫 실행',
    'LimitEditor': '모달 · 한도 조정', 'TransactionAdd': '모달 · 거래 추가',
    'ProfileDialog': '모달 · 내 수치 입력', 'AssetDialog': '모달 · 자산 추가',
    'DebtDialog': '모달 · 부채 수정', 'GoalDialog': '모달 · 목적지 추가',
    'RecurringDialog': '모달 · 반복 거래', 'MonthlyClose': '모달 · 월 마감',
    'ImportReview': '모달 · 백업 불러오기', 'CoachPanel': '모달 · 코칭',
    'AlertsPanel': '모달 · 알림', 'AlertsEmpty': '모달 · 알림 없음', 'PeerDialog': '모달 · 또래 기준 등록',
    'StorageStates': '상태 · 저장소 로딩·복구', 'PeerStates': '상태 · 또래 카드 5종',
    'EmptyStates': '상태 · 미입력 6종', 'Confirmations': '상태 · 삭제·초기화 확인',
    'ModalErrors': '상태 · 모달 오류·저장 6종', 'GoalTypes': '상태 · 목적지 유형 5종',
    'SpendingPast': '소비 · 지난 달(마감)', 'GoalContribute': '모달 · 적립액 추가',
    'CoachEmpty': '모달 · 코칭 기록 없음',
    'DesktopHome': '데스크톱 · 홈', 'DesktopLedger': '데스크톱 · 소비 내역',
    'Tokens': '토큰 · 색 · 타이포 · 간격', 'Components': '컴포넌트 · 상태',
    # v4 · 1단계 (gen_v4.py)
    'IntroPosition': '첫 실행 · 소개 1 현재 위치', 'IntroRoute': '첫 실행 · 소개 2 항로',
    'IntroDestination': '첫 실행 · 소개 3 목적지', 'HomeSetup': '첫 실행 · 홈 구성',
    'HomeConfigured': '홈 · 구성 반영 · 탭 합치기 전',
    # v4 · 2~5단계 (gen_v4_stocks.py)
    'DestGoals': '목적지 · 내 목적지 (5탭)', 'DestFuture': '목적지 · 자산 경로 (5탭)', 'HomeStocksOff': '홈 · 주식 꺼짐 (4탭)',
    'StocksMine': '주식 · 내 종목', 'HoldingAdd': '모달 · 보유 기록', 'StocksEmpty': '주식 · 빈 상태', 'HomeStocksCard': '홈 · 주식 요약 카드',
    'StocksHome': '주식 · 둘러보기', 'StockListGrowth': '주식 · 성장주 목록', 'StockListDividend': '주식 · 배당주 목록',
    'StockDetail': '주식 · 종목 상세', 'StockThemes': '주식 · 테마', 'StockStates': '참고 · 주식 탭 특수한 상황 6가지',
    'StockSettings': '모달 · 설정 › 주식', 'SnapshotUpdate': '참고 · 종목 데이터 새로 받기',
    # v5 · 1단계 (gen_v5.py)
    'DaySheet': '하루 시트 · 오늘 (키보드 열림)', 'DaySheetList': '하루 시트 · 기록 있는 과거 날 (목록 우선)',
    'DaySheetEdit': '하루 시트 · 수정 모드', 'DoneCard': '홈 · 저장 뒤 완료 카드', 'DaySheetConfirm': '참고 · 저장을 한 번 더 물어보는 경우',
    'ClassifySheet': '분류하기 시트', 'HeroInsufficient': '홈 · 히어로 이력 부족', 'DaySheet360': '하루 시트 · 360 × 640 작은 폰',
    'HeroFootnotes': '참고 · 홈 맨 위 카드의 안내 줄',
    'HomeCalendarStrip': '홈 · 달력 접힘 (최근 7일)', 'HomeCalendar': '홈 · 달력 펼침 (월 달력) · 3일 칸 누름',
    'HomeCalendar360': '홈 · 달력 펼침 · 360px (월 달력 그대로)', 'HomeCalendarPrev': '홈 · 달력 펼침 · ‹ 지난달 8월 보기',
    'CalendarCells': '참고 · 달력 칸 읽는 법', 'CalendarGridSizes': '참고 · 달력을 펼치면 어디서나 월 달력',
    # 최신화 반영(2026-09-21) 새 장
    'HomeSetupStocksOn': '첫 실행 · 홈 구성 · 주식 켬',
    'SettingsHomeEntry': '설정 · 「홈 구성 ›」 행',
    'HomeLayoutEdit': '설정 › 홈 구성 (처음 실행 뒤에 다시 고칠 때)',
    'DestPayoff': '목적지 · 상환 계획',
    'DaySheetScrolled': '하루 시트 · 키보드를 내린 모습',
    'DaySheetNoSpend': '하루 시트 · 소비 0건인 날 (오늘은 안 썼어요)',
    'ReviewListSheet': '확인할 내용 목록 시트',
    'HomeDefaultScroll': '홈 · 기본 5카드 전체 (v5 · 2단계)',
    'CalendarStatusLines': '참고 · 달력 아래 한 줄이 바뀌는 경우',
    'DaySheetNoSpendStates': '참고 · 안 쓴 날을 표시하는 경우',
    'DoneCardStates': '참고 · 저장 완료 카드의 경우들',
    'DaySheetStates': '참고 · 기록 창의 글이 바뀌는 경우',
    'LedgerV5': '소비 · 내역 (v5 · 분류 안 함 칩 · 날짜별 합계)',
    'MonthlyCloseV5': '월 마감 (v5 · 분류 안 함 안내)',
    'TransactionAddFromDaySheet': '참고 · 거래 추가 — 하루 시트에서 넘어왔을 때',
    'AlertsReview': '참고 · 달력이 없을 때 「확인할 내용」이 보이는 곳',
    'InsufficientElsewhere': '참고 · 예상 기준을 확인하기 전 — 홈 밖의 화면들',
    'FutureProvisional': '참고 · 미래 · 자산 경로의 잠정 표시',
    'EtcSubline': '참고 · 분류 안 한 소비와 안 쓴 날 — 소비 · 한도 · 코치',
    'LimitCardCases': '참고 · 이번 달 한도 카드의 네 가지 경우',
    'RecurringPrefill': '반복 거래 · 방금 저장한 거래로 미리 채움',
    'ImportBackupNotes': '참고 · 가져오기 · 백업 안내',
    'DesktopHomeV5': '데스크톱 홈 · 달력 포함 (v5 뒤)',
}

PAGES = [
    ('page-1', '모바일 · 화면', 6,
     ['Main', 'HomeScroll', 'Assets', 'Debts', 'Strategy', 'Spending',
      'Ledger', 'Limits', 'SpendingPast', 'Goals', 'GoalDesign', 'Future', 'Payoff', 'Onboarding']),
    ('page-2', '모바일 · 모달', 6,
     ['ProfileDialog', 'TransactionAdd', 'LimitEditor', 'AssetDialog', 'DebtDialog', 'GoalDialog',
      'RecurringDialog', 'GoalContribute', 'MonthlyClose', 'ImportReview', 'CoachPanel', 'CoachEmpty',
      'AlertsPanel', 'AlertsEmpty', 'PeerDialog']),
    ('page-3', '상태 카탈로그', 6,
     ['StorageStates', 'EmptyStates', 'PeerStates', 'GoalTypes', 'ModalErrors', 'Confirmations']),
    ('page-4', '데스크톱', 3, ['DesktopHome', 'DesktopLedger', 'DesktopHomeV5']),
    ('page-5', '디자인 시스템', 2, ['Tokens', 'Components']),
    ('page-6', 'v4 · 1단계 첫 실행', 5,
     ['IntroPosition', 'IntroRoute', 'IntroDestination', 'HomeSetup', 'HomeConfigured',
      'HomeSetupStocksOn', 'SettingsHomeEntry', 'HomeLayoutEdit']),
    ('page-7', 'v4 · 2단계 내비', 4, ['DestGoals', 'DestFuture', 'DestPayoff', 'HomeStocksOff']),
    ('page-8', 'v4 · 3단계 주식 뼈대', 4, ['StocksMine', 'HoldingAdd', 'StocksEmpty', 'HomeStocksCard']),
    ('page-9', 'v4 · 4단계 카테고리', 6, ['StocksHome', 'StockListGrowth', 'StockListDividend', 'StockDetail', 'StockThemes', 'StockStates']),
    ('page-10', 'v4 · 5단계 설정', 2, ['StockSettings', 'SnapshotUpdate']),
    ('page-11', 'v5 · 달력과 하루 시트 (1 · 2단계)', 5,
     ['HomeCalendarStrip', 'HomeCalendar', 'DaySheetList', 'DaySheet', 'DoneCard',
      'HomeCalendar360', 'HomeCalendarPrev', 'HeroInsufficient', 'DaySheetEdit', 'ClassifySheet',
      'DaySheetScrolled', 'DaySheetNoSpend', 'ReviewListSheet', 'DaySheet360', 'HomeDefaultScroll']),
    ('page-12', 'v5 · 구현 참고 장', 2,
     ['CalendarCells', 'CalendarGridSizes', 'CalendarStatusLines', 'HeroFootnotes',
      'DaySheetConfirm', 'DaySheetStates', 'DaySheetNoSpendStates', 'DoneCardStates']),
    ('page-13', 'v5 · 다른 화면에 닿는 곳', 3,
     ['LedgerV5', 'MonthlyCloseV5', 'TransactionAddFromDaySheet',
      'AlertsReview', 'InsufficientElsewhere', 'FutureProvisional']),
    ('page-14', 'v5 · 3단계 한도 라벨 · 반복 거래 · 백업', 2,
     ['LimitCardCases', 'RecurringPrefill', 'EtcSubline', 'ImportBackupNotes']),
]


def dark_of(name):
    """라이트 아트보드의 다크 짝. 없으면 None."""
    twin = 'DarkHome' if name == 'Main' else f'Dark{name}'
    return twin if (OUT / f'{twin}.dc.html').exists() else None

NOTES = {
    'page-1': ('note-screens', 640,
               '읽는 순서: 결과 → 근거 → 행동\n\n'
               '화면마다 display 크기 숫자는 딱 하나입니다. 홈은 월급 대비 소비율, 자산은 순자산, 소비는 계획 대비 속도, '
               '목적지는 월 배분, 미래는 10년 뒤 순자산.\n\n'
               '그 값을 바꾸는 버튼은 값 바로 옆이나 아래에 놓입니다. 탭 위에 떠 있던 CTA는 모두 없앴습니다.\n\n'
               '── 아래 줄은 같은 화면의 다크입니다. 레이아웃·타이포·간격은 1px도 다르지 않고 토큰만 바뀝니다. '
               '브랜드 그라디언트와 카테고리·자산 고정 팔레트는 다크에서도 같은 값이고, 채운 버튼만 반전됩니다 '
               '— 밝은 브랜드색 배경에 어두운 글자.'
               '\n\n이 페이지는 v3 기준 그림입니다 — 목표 · 미래 탭은 v4 · 2단계에서 「목적지」로 합쳐지고, 홈은 v5 · 1단계에서 이번 달 달력이 히어로 아래 첫 카드로 들어갑니다(해당 페이지 참조).'),
    'page-2': ('note-modals', 640,
               '모달은 헤더 / 스크롤 본문 / 고정 하단 행동 세 층\n\n'
               '제목은 무엇을 하는 창인지, 부제는 무엇이 저장되는지 말합니다. 필수는 라벨 옆 *, 필수가 아닌 칸은 라벨 옆 회색 "선택 사항"입니다.\n\n'
               '한도 조정·월 마감·백업 불러오기처럼 되돌리기 어려운 저장에는 본문과 버튼 사이에 고정 확인 줄을 둡니다.\n\n'
               '월 마감 모달은 v5 · 1단계에서 체크박스 문구와 분류 안 함 안내가 바뀝니다 — 「v5 · 다른 화면에 닿는 곳」 페이지의 월 마감(v5) 장 참조. 이 페이지의 월 마감은 v3 기준 그림입니다. 거래 추가 · 반복 거래 · 백업 불러오기의 v5 모습도 그 페이지와 「v5 · 3단계」 페이지에 있습니다.\n\n'
               '── 아래 줄은 다크입니다. 시트 배경은 surface(#121A2B), 스크림은 #04070E이고 그림자는 더 깊고 '
               '불투명해집니다. 보라 가정 배지, 회색 — 미입력, 주황/빨강 경고의 의미는 라이트와 같습니다.'),
    'page-3': ('note-states', 640,
               '없는 값을 지어내지 않는다\n\n'
               '미입력은 회색 —로만 표시하고 0원·0%·좋은 성과로 바꾸지 않습니다. 급여가 0원이고 부수입만 있는 상태는 '
               '소비율을 —로 두고 총수입 대비 소비를 대안 지표로 제시합니다.\n\n'
               '미입력 상태는 여섯 가지입니다 — 여섯째 F는 v5의 히어로 이력 부족(예상을 아직 보여 주지 않을 때)이고, 그때는 이번 달 기록한 소비만 보여 주며 월말 예상 · 여유는 —, 순항 배지는 내지 않습니다.\n\n'
               '또래 카드는 5가지 상태 어디에서도 확인되지 않은 평균·백분위·상위 %를 만들지 않습니다.\n\n'
               '모달 오류 6종도 같은 규칙을 씁니다. 오류는 무엇이 잘못됐고 어떻게 고치는지를 같이 말하고, '
               '저장에 실패해도 입력한 값을 지우지 않습니다.\n\n'
               '── 아래 줄은 다크입니다. 회색 — 미입력, 보라 = 저장되지 않은 가정, 주황 = 개인 목표 초과, '
               '빨강 = 100% 초과. 네 의미는 두 모드에서 완전히 같은 자리에 쓰입니다. 오류 카드의 빨강만 '
               '다크에서 밝기를 올려(#C0342F → #E8635F) 어두운 표면 위에서 읽히게 했습니다.'),
    'page-4': ('note-desktop', 640,
               '데스크톱은 넓이를 두 번째 열로 쓴다\n\n'
               '2.2의 데스크톱은 사이드바 224px + 가운데 한 열이라 히어로 카드 안이 텅 비어 보였습니다.\n\n'
               'v3는 본문을 1.6fr / 1fr로 나눕니다. 왼쪽은 주지표와 그래프, 오른쪽은 다음 안내·대표 목적지·또래·한도처럼 '
               '곁눈질로 보는 정보. 사이드바에도 각 탭의 현재 수치를 넣었습니다.\n\n'
               '셋째 장은 v5 달력이 들어간 데스크톱 홈입니다 — 달력은 히어로 아래 왼쪽 열 첫 자리에 7열 월 달력을 펼친 채로 두고 그래프를 그 오른쪽에 둡니다(세 가지 배치를 그려 보고 2026-09-21에 이 안으로 정함 · 달력을 왼쪽 열 전체 폭으로 넓히는 안과 접힌 최근 7일로 두는 안은 빈 자리가 커서 버림). 한도 라벨은 v5 · 3단계의 「앞으로 하루 47,270원」이고, 사이드바는 v4 · 2단계 뒤 모습입니다 — 목표 · 미래 대신 「목적지」 하나이고, 주식을 켠 사용자 기준이라 「주식」 칸이 있는 5칸입니다(주식을 끄면 4칸).\n\n'
               '둘째 장 데스크톱 내역은 v3 기준 그림입니다 — v5 · 1단계 뒤에는 모바일 내역(v5) 장과 같은 규칙(필터 칩 「분류 안 함 N건」 · 날짜 머리글의 「소비 · 이체」 합계 = 달력 칸 · 확인한 날 ✓ · 행 ⋯의 「매달 반복으로 만들기」)을 따릅니다.\n\n'
               '── 아래 줄은 다크입니다.'),
    'page-5': ('note-system', 640,
               '타이포 9단계 · 카테고리 색은 그대로\n\n'
               '2.2에는 17·18·20·21·23·26·32px가 섞여 있었습니다. v3는 display / metric-xl / metric / title / '
               'section / body / label / meta / eyebrow 9단계만 씁니다.\n\n'
               '카테고리·자산 고정 팔레트는 거래와 차트의 정체성이라 2.2 값을 그대로 유지합니다.\n\n'
               '토큰 시트는 01 LIGHT / 02 DARK 두 절과 상태색 카드의 DARK 줄로 두 모드 값을 한 장에 다 적어 둔 '
               '명세라 다크 사본을 따로 두지 않습니다. 컴포넌트 시트는 실제 컴포넌트를 보여 주므로 아래 줄에 다크를 둡니다.'),
    'page-6': ('note-v4-stage1', 640,
               'v4 · 1단계 — 첫 실행 소개 3장 · 홈 구성 1장 · 구성값을 반영한 홈 1장 · 둘째 줄: 주식을 켠 구성 · 설정 창의 「홈 구성 ›」 행 · 설정 › 홈 구성\n\n'
               '소개 3장은 한 장에 한 문장이고, 그림은 새 일러스트가 아니라 홈·목적지의 실제 컴포넌트입니다. '
               '어느 장에서든 건너뛰기 → 바로 구성 화면으로 갑니다.\n\n'
               '구성 화면: 소비율 히어로는 고정, 아래 카드는 최대 5개. 목록 첫 행은 이번 달 달력(기본 켜짐 · 최근 7일 미리보기)입니다. '
               '기본 5카드는 달력 · 다음 안내 · 이번 달 한도 · 대표 목적지 · 또래와 내 페이스이고, 순자산 대비 소비는 목록에 남되 기본에서만 빠집니다(v5 계획 §3-1). 기본 배열은 v5 · 2단계와 함께 바뀌고 그 전까지 기본 홈은 v3 그대로입니다. '
               '달력도 상한 5에 셉니다 — 이 시안은 달력 · 다음 안내 · 이번 달 한도 · 순자산 한 줄 · 상환 계획 한 줄을 고른 상태라 5 / 5입니다. '
               '이 구성 화면은 처음 설치해 처음 실행할 때만 뜹니다. 그 뒤에는 설정 › 홈 구성으로만 들어갑니다(사용자 결정). 둘째 줄 둘째 · 셋째 장이 그 길입니다 — 설정 창의 「홈 구성 ›」 행과, 그 행으로 들어간 홈 구성 화면(건너뛰기 대신 닫기, 「이 구성으로 시작」 대신 저장 · 시안은 달력을 끈 4 / 5 상태와 그때의 안내 문장). 둘째 줄 첫 장은 구성 화면에서 주식을 켠 변형 — 목록 끝에 주식 요약 행이 생기고 달력 · 다음 안내 · 주식 요약 · 이번 달 한도 · 순자산 한 줄로 5 / 5입니다(3단계 페이지의 주식 켠 홈과 같은 구성). "주식도 볼까요?"는 기본 꺼짐 — '
               '켜면 주식 요약 카드와 주식 탭이 생기지만 그 화면은 2·3단계 시안입니다.\n\n'
               '다섯째 장 "홈 · 구성 반영"은 그 선택대로 홈이 그려진 결과입니다 — 히어로 바로 아래 첫 카드가 이번 달 달력(접힘 = 최근 7일)입니다. '
               '헤더·히어로·다음 안내·이번 달 한도는 v3 홈(Main)에서 그대로 잘라 왔고, 카드 순서는 구성 화면의 목록 순서를 따릅니다. '
               '구성을 다시 바꾸는 길은 설정 › 홈 구성 하나입니다.\n\n'
               '구성 다음 장은 기존 첫 실행 화면(모바일 · 화면 페이지의 "첫 실행": 내 데이터로 시작 / 샘플로 둘러보기)이라 '
               '여기 다시 두지 않았습니다.\n\n'
               '── 아래 줄은 다크입니다. darken.py로 만든 토큰 매핑 사본입니다.'),
    'page-7': ('note-v4-stage2', 640,
               'v4 · 2단계 — 내비 재편 (계획 §4 권장안)\n\n'
               '이 단계는 v5 · 1~2단계 뒤에 나갑니다 — 그래서 홈 장(주식 꺼짐)은 히어로 아래 첫 카드가 이번 달 달력입니다. 자산 · 소비 탭 본문은 v3 그대로이고 내비만 바뀝니다. 셋째 세그먼트 상환 계획은 DestPayoff 장.\n\n'
               '목표 + 미래 → "목적지" 한 탭. 세그먼트 3개(내 목적지 · 자산 경로 · 상환 계획)이고 본문은 v3 목적지·미래 화면을 그대로 잘라 왔습니다 — 바뀌는 것은 내비와, 내 목적지 목록 끝 점선 버튼의 이름(「+ 목적지 추가」 → 「새 목적지 설계 ›」)뿐입니다. '
               '"새 목적지 설계"는 내 목적지 목록 끝의 점선 버튼으로 들어갑니다(v3 원칙 4).\n\n'
               '주식을 켠 사용자: 홈 · 자산 · 소비 · 주식 · 목적지 (5탭). 주식을 끈 사용자: 홈 · 자산 · 소비 · 목적지 (4탭) — 넷째 장. 주식 흔적은 탭·카드·설정 어디에도 없습니다. 셋째 장은 상환 계획 세그먼트(v3 상환 계획 본문 그대로 · 가정 카드는 보라 점선).\n\n'
               '── 아래 줄은 다크입니다.'),
    'page-8': ('note-v4-stage3', 640,
               'v4 · 3단계 — 주식탭 뼈대 (사용자 입력만, 스냅숏 없음)\n\n'
               '이 단계도 v5 뒤입니다 — 넷째 장의 홈은 달력 · 다음 안내 · 주식 요약 · 이번 달 한도 · 순자산(5 / 5)이고 한도 라벨은 v5 · 3단계의 「앞으로 하루 47,270원」입니다.\n\n'
               '보유는 수량·평단, 관심은 이름과 메모. 종가는 직접 넣는 값이라 가격 옆에 늘 "9/4 종가"가 붙고(직접 넣은 값이라는 안내는 카드 머리말에 한 번), 비워 두면 —입니다. '
               '보유 평가액 1,244만원 = 수량 × 종가 (삼성전자 60주 · SK하이닉스 20주 · KODEX 200 120주, 매입 대비 +36만원).\n\n'
               '"계좌 평가액에 반영" 토글은 기본 꺼짐(§9-6). 켜면 ETF 계좌 평가액에 더해져 자산·순자산·미래 경로로 흐릅니다.\n\n'
               '넷째 장은 홈 구성에서 주식을 켠 사용자의 홈 — 주식 요약 카드 한 줄이 들어갑니다.\n\n'
               '── 아래 줄은 다크입니다.'),
    'page-9': ('note-v4-stage4', 640,
               'v4 · 4단계 — 카테고리 탐색 (내장 스냅숏)\n\n'
               '주식 홈: 투자 여력 띠(이번 달 저축·투자 여력 27만원) → 가드레일 한 줄(막지 않음) → 내 종목 → 성장 · 저평가 · 배당 · 테마. '
               '목록의 모든 행에 이유 한 줄과 충족 수가 붙고 색으로 좋다·나쁘다를 칠하지 않습니다. 없는 값은 —이고 분모가 줄어듭니다(2/2).\n\n'
               '종목 상세: 왜 이 목록에 있나(기준 3개 ✓·실제 숫자) → 52주 위치 바 → 핵심 숫자 → "내 항로에 넣어보기"(보라 점선 · 저장되지 않는 가정). '
               '월 15만원을 더 넣으면 투자 계좌 5,000만원 도착이 2032년 6월 → 2030년 12월(calc/goals.py의 months_to와 같은 식).\n\n'
               '종목명은 실재하지만 수치는 전부 디자인 검증용 가상값입니다 — design/stocks-snapshot.sample.json 참고. 추천·매수·매도라는 말은 어디에도 없습니다.\n\n'
               '── 아래 줄은 다크입니다.'),
    'page-10': ('note-v4-stage5', 640,
               'v4 · 5단계 — 종목 데이터 새로 받기(선택) · 기준값 설정\n\n'
               '설정 › 주식: 종목 데이터 기준일과 [새로 받기] 버튼, 기준값(말 → 규칙 → 시작값, 스텝퍼), 주식 기능 끄기. 기준값은 통계가 아니라 시작값이라 바꿔도 앱이 판단하지 않습니다.\n\n'
               '새로 받기는 파일 하나를 한 번 받는 것이고 자동으로 받지는 않습니다. 실패해도 지금 데이터로 전부 동작합니다 — 둘째 장은 앱 화면이 아니라 받는 순서를 설명하는 구현 참고 장입니다.\n\n'
               '── 아래 줄은 다크입니다.'),
    'page-11': ('note-v5-stage1', 640,
               'v5 · 1 · 2단계 — 홈 달력과 하루 시트 (plan/v5-calendar.md 10판)\n\n'
               '1단계: 월 달력 카드(히어로 아래 고정) · 날짜 터치 → 하루 시트 · 상태 줄 · 확인할 내용 N개 › · 시트 맨 아래 「다 적었어요」/「오늘은 안 썼어요」 · 완료 카드 · 이력 부족 히어로. '
               '2단계: 최근 7일 스트립 · 홈 기본 배열 변경(기본 5카드) · 320px · 큰 글자 · 홈 구성 첫 행(v4 · 1단계 페이지에 반영). '
               '시트 아래 「저축·투자로 기록 ›」 · 「대출상환으로 기록 ›」는 거래 추가를 그 종류로 열고 저장하면 홈으로 돌아옵니다(「v5 · 다른 화면에 닿는 곳」 페이지).\n\n'
               '첫째 줄: 홈에 달력 카드가 히어로 바로 아래 첫 카드로 들어간 모습(접힘 = 최근 7일, 오늘이 오른쪽 끝) → 펼친 월 달력(머리줄 ‹ 2026년 9월 ›, 요일 줄, 주마다 가는 선, 3일 칸을 누른 순간) → 9월 3일 하루 시트(그 날의 기록이 먼저 보이고 + 추가, 맨 아래 「9월 3일 다 적었어요」) '
               '→ 오늘 칸을 눌렀을 때(오늘과 기록 없는 날은 입력 우선 — 금액에 자동 포커스 · 키보드 자리는 빈 판, 그날 기록은 키보드 아래 「오늘 기록」 · 셋째 줄 첫 장) → 저장 뒤 완료 카드(날짜 · 정확 금액 · 오늘 합계 · 셋째 줄은 분류를 고르지 않고 저장해서 「소비에는 이미 포함됐어요 · 분류하면 예상을 다시 계산해요」 — 소비율 변화 줄은 앞선 조건이 없고 예상 기준이 확인된 달에만, 취소는 방금 기록한 건만). '
               '펼침은 어느 폭 · 어느 글자 크기에서도 월 달력이고 세로 날짜 목록으로 저절로 바뀌지 않습니다(7판). ‹ 는 지난달까지만 갑니다.\n\n'
               '둘째 줄: 달력 펼침 360px · ‹ 로 지난달(8월)을 보는 상태 · 지난달 기록이 없는 달의 홈(큰 숫자가 예상 소비율 대신 이번 달 기록한 소비) · 수정 모드 · 분류하기.\n\n'
               '셋째 줄(최신화 반영): 키보드를 내린 하루 시트(오늘 기록 목록과 맨 아래 「9월 8일 다 적었어요」) · 소비가 0건인 날의 시트(「오늘은 안 썼어요」 · 이체만 있는 날의 둘째 줄) · 「확인할 내용 N개 ›」를 누르면 열리는 목록 시트(항목 종류는 셋뿐 · 9월 8일 시안은 그중 「8월 다시 마감 필요」 · 「분류 안 함 7건」 둘) · 작은 폰 360 × 640의 하루 시트 · 2단계 기본 5카드 홈 전체(달력 · 다음 안내 · 이번 달 한도 · 대표 목적지 · 또래와 내 페이스).\n\n'
               '칸마다 그날 소비 합계(1만 미만은 원 단위, 1만 이상은 1.2만 형식), —는 아직 기록 없음, 0은 안 썼어요로 표시한 날, ✓는 다 적었어요, 이체 배지. '
               '수치는 v3 샘플(오늘 4건 37,000원 + 편의점 12,000원 → 5건 49,000원 · 57.9% → 58.2%). '
               '이번 달 한도 카드의 라벨은 3단계 전이라 v3 그대로 「하루 47,270원」입니다(저장 뒤 「하루 46,730원」 · 지난 기록이 없는 달 「하루 97,950원」) — 「앞으로 하루 …」는 「v5 · 3단계 한도 라벨 · 반복 거래 · 백업」 페이지에서 바뀝니다. '
               '수입·환불 링크는 없고(앱에 그 흐름이 없음), 하루 기준선 막대도 없습니다(계획 §12-18). '
               '설명 장은 다음 페이지 「v5 · 구현 참고 장」으로 옮겼습니다.\n\n'
               '── 아래 줄은 다크입니다.'),
    'page-12': ('note-v5-spec', 640,
               'v5 · 구현 참고 장 — 앱 화면이 아니라 구현할 때 보는 설명 장\n\n'
               '모든 장 맨 위에 「구현 참고 · 앱 화면이 아닙니다」 알약이 있습니다. 왼쪽에 실제 화면(또는 그 일부)을 두고 번호를 붙였고, 오른쪽에 상황별 모습을 「상황 제목 + 한 줄 설명」으로 나란히 놓았습니다.\n\n'
               '달력: 달력 칸 읽는 법(번호 9개 — 9번은 앱을 쓰기 시작한 날보다 앞선 빈 칸 · 옆에 그 견본과 「칸에 금액을 쓰는 법」 표) · 달력을 펼치면 어디서나 월 달력(320px · 큰 글자 · 선택 보기인 목록 · 접어 둔 최근 7일 줄의 320px · 큰 글자) · 달력 아래 한 줄이 바뀌는 경우(오늘 합계 · 아직 기록 없음 · 안 썼다고 표시 · 18시 이후 다 적었어요 · 표시가 풀림 · 오지 않은 날 · 샘플 모드) · 홈 맨 위 카드의 안내 줄.\n\n'
               '하루 시트: 저장을 한 번 더 물어보는 경우 · 기록 창의 글이 바뀌는 경우(「전체 ›」 13칩과 고정비 구분선 · 메모 60자 · 금액 0과 빈 값 · 날짜별 머리글 · 샘플 모드) · 안 쓴 날을 표시하는 경우(— → 0 · 표시 풀기 · 이체만 있는 날) · 저장 완료 카드의 경우들(제목 3종 · 셋째 줄 우선순위 · 취소 범위).\n\n'
               '문구는 plan/v5-calendar.md의 원문이고, 계획에 원문이 없어 시안에서 정한 것은 design/CHANGES-2026-09-21.md에 따로 적었습니다.\n\n'
               '── 아래 줄은 다크입니다.'),
    'page-13': ('note-v5-elsewhere', 640,
               'v5 · 다른 화면에 닿는 곳 — 달력과 하루 시트 때문에 기존 화면에서 달라지는 모습\n\n'
               'v3 기준 그림(모바일 · 화면 / 모달 페이지)은 그대로 두고, v5 뒤의 모습을 여기에 따로 그렸습니다. v4 · 2단계 전이라 탭은 홈 · 자산 · 소비 · 목표 · 미래입니다.\n\n'
               '첫째 줄: 소비 · 내역 — 필터 칩 「분류 안 함 7건」, 날짜 머리글의 「소비 · 이체」 합계(달력 칸과 같은 값)와 확인한 날 ✓, 행의 ⋯ 메뉴 「매달 반복으로 만들기」 · 월 마감 — 새 체크박스 문구와 「분류 안 함 3건 · 21,200원이 기타로 들어가요 · 지금 분류 ›」(8월 값 — 9월의 7건 32,000원과 다른 달)(마감을 막지 않음) · '
               '거래 추가(구현 참고 장 · 번호와 흐름 주석) — 하루 시트의 「저축·투자로 기록 ›」에서 넘어와 종류 · 날짜 · 금액 · 메모가 채워진 상태, 저장하면 소비 탭이 아니라 홈으로 돌아와 완료 카드.\n\n'
               '둘째 줄(세 장 모두 구현 참고 장): 달력이 없을 때 「확인할 내용」이 보이는 곳(소비 탭 알림 · 월 마감 카드) · 예상 기준을 확인하기 전 홈 밖의 화면들(소비 · 한도 · 코치 · 다음 안내 · 또래 · 알림에서 「순항 중」 같은 판단을 하지 않고 기록한 사실만 말함) · 미래 · 자산 경로의 「잠정」 표시.\n\n'
               '「잠정」 표시의 모양은 계획에 없어 시안에서 정했습니다(회색 작은 배지 · 보라 가정 카드와 구분).\n\n'
               '── 아래 줄은 다크입니다.'),
    'page-14': ('note-v5-stage3', 640,
               'v5 · 3단계 — 한도 라벨 · 반복 거래 미리 채움 · 백업 안내 (+ 2단계의 기타 서브라인)\n\n'
               '이번 달 한도 카드의 「하루 47,270원」이 「앞으로 하루 47,270원」으로 바뀝니다. 한도를 안 정했을 때(—) · 0원일 때 · 넘었을 때(「한도보다 32,000원 많아요」) · 마지막 날(「이번 달 남은 한도 90,000원」)을 같은 표시로 합치지 않습니다 — 첫째 장.\n\n'
               '둘째 장: 완료 카드 · 내역의 「매달 반복으로 만들기 ›」로 들어온 반복 거래 창 — 이름 · 금액 · 카테고리 · 결제일이 채워져 있고 시작 월은 다음 달(2026.10), 「이번 달 건은 방금 저장한 거래로 이미 있어요」.\n\n'
               '셋째 장: 소비 · 한도 화면의 기타 아래 「분류 안 함 7건 32,000원」 서브라인, 기타 한도 경고와 코치의 최대 카테고리 비중을 미확정 금액을 빼고 다시 판정했다는 한 줄, 코치 「소비 기록이 필요합니다」 본문의 「소비 없음 확인 n일」 병기. '
               '넷째 장: 가져오기 · 백업 — 확인 표시와 분류 안 함 표시가 백업에 함께 들어가고, 전체 복원과 골라서 가져오기가 다르게 돌려준다는 안내.\n\n'
               '── 아래 줄은 다크입니다.'),
}

GAP_X = 80
PAIR_GAP = 52      # 라이트 줄 → 바로 아래 다크 줄
GROUP_GAP = 168    # 다음 라이트 줄까지


def size(f):
    if f in WIDE:
        return WIDE[f]
    return PHONE[0], TALL.get(f, PHONE[1])


def title_of(f):
    if f.startswith('Dark'):
        base = 'Main' if f == 'DarkHome' else f[4:]
        return TITLES.get(base, base) + ' (다크)'
    return TITLES.get(f, f)


artboards = []
annotations = []

for pid, pname, per_row, files in PAGES:
    y = 0
    for i in range(0, len(files), per_row):
        chunk = files[i:i + per_row]
        # 라이트 줄
        x = 0
        light_h = 0
        xs = []
        for f in chunk:
            w, h = size(f)
            xs.append((f, x, w, h))
            artboards.append({'file': f'{f}.dc.html', 'page': pid, 'x': x, 'y': y,
                              'w': w, 'h': h, 'title': title_of(f)})
            light_h = max(light_h, h)
            x += w + GAP_X
        # 다크 줄 — 같은 x에 그대로 내려 놓는다
        dy = y + light_h + PAIR_GAP
        dark_h = 0
        for f, fx, fw, _ in xs:
            twin = dark_of(f)
            if not twin:
                continue
            w, h = size(twin)
            artboards.append({'file': f'{twin}.dc.html', 'page': pid, 'x': fx, 'y': dy,
                              'w': w, 'h': h, 'title': title_of(twin)})
            dark_h = max(dark_h, h)
        y = dy + dark_h + GROUP_GAP if dark_h else y + light_h + GROUP_GAP
    nid, nw, ntext = NOTES[pid]
    annotations.append({'id': nid, 'page': pid, 'x': 0, 'y': -210, 'w': nw, 'text': ntext})
    if pid == 'page-6':
        annotations.append({'id': 'note-v4-stage1-ask', 'page': pid, 'x': 700, 'y': -210, 'w': 420, 'text': (
            '검토 부탁드릴 것\n\n'
            '1. 카드 순서 — 구성 화면의 목록 순서 그대로인지, 끌어서 바꿀 수 있어야 하는지.\n'
            '2. "저장되지 않는 가정" 카드는 시뮬레이션을 켰을 때만 나타나므로 선택 목록에서 뺐습니다.\n'
            '3. 소개 문장 셋은 계획서 §3의 문장 그대로입니다.\n'
            '4. 소개 3장의 목적지 세 곳은 v3 샘플(비상금 68% · 투자 계좌 42% · 신용대출 31%)이고 도착일은 calc 확정값입니다.\n'
            '5. 구성 반영 홈의 순자산 한 줄(9,350만원 · 1억까지 650만원 · 2027년 2월)과 상환 계획 한 줄(완제 2036년 4월 · 월 92만원)도 같은 샘플입니다.')})

canvas = {
    'pages': [{'id': p, 'name': n} for p, n, _, _ in PAGES],
    'artboards': artboards,
    'annotations': annotations,
    'launch': {'view': 'canvas', 'page': 'page-11'},   # 검토 중인 페이지를 먼저 연다
}

(OUT / 'canvas.json').write_text(json.dumps(canvas, ensure_ascii=False, indent=2), encoding='utf-8')

have = {p.name.replace('.dc.html', '') for p in OUT.glob('*.dc.html')}
listed = {a['file'].replace('.dc.html', '') for a in artboards}
print(f'{len(artboards)} artboards across {len(PAGES)} pages')
print('배치 안 된 파일:', sorted(have - listed) or '없음')
print('파일 없는 항목:', sorted(listed - have) or '없음')
