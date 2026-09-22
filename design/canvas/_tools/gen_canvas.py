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
    'HomeConfigured': '홈 · 첫 실행 구성 반영',
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
    'HomeDefaultScroll': '홈 · 기본 5카드 전체 스크롤',
    'CalendarStatusLines': '참고 · 달력 아래 한 줄이 바뀌는 경우',
    'DaySheetNoSpendStates': '참고 · 안 쓴 날을 표시하는 경우',
    'DoneCardStates': '참고 · 저장 완료 카드의 경우들',
    'DaySheetStates': '참고 · 기록 창의 글이 바뀌는 경우',
    'LedgerV5': '소비 · 내역 (분류 안 함 칩 · 날짜별 합계)',
    'MonthlyCloseV5': '모달 · 월 마감 (분류 안 함 안내)',
    'TransactionAddFromDaySheet': '참고 · 거래 추가 — 하루 시트에서 넘어왔을 때',
    'InsufficientElsewhere': '참고 · 예상 기준을 확인하기 전 — 홈 밖의 화면들',
    'FutureProvisional': '참고 · 미래 · 자산 경로의 잠정 표시',
    'EtcSubline': '참고 · 분류 안 한 소비와 안 쓴 날 — 소비 · 한도 · 코치',
    'LimitCardCases': '참고 · 이번 달 한도 카드의 네 가지 경우',
    'RecurringPrefill': '반복 거래 · 방금 저장한 거래로 미리 채움',
    'ImportBackupNotes': '참고 · 가져오기 · 백업 안내',
    'DesktopHomeV5': '데스크톱 · 홈',
    'TourHome1': '첫 실행 안내 · 홈 1 / 3 현재 위치',
    'TourHome2': '첫 실행 안내 · 홈 2 / 3 달력으로 기록',
    'TourHome3': '첫 실행 안내 · 홈 3 / 3 다음 안내',
    'TourAssets1': '첫 실행 안내 · 자산 1 / 3 세 탭',
    'TourAssets2': '첫 실행 안내 · 자산 2 / 3 순자산',
    'TourAssets3': '첫 실행 안내 · 자산 3 / 3 현금성 자산',
    'TourSpending1': '첫 실행 안내 · 소비 1 / 3 세 탭',
    'TourSpending2': '첫 실행 안내 · 소비 2 / 3 속도 그래프',
    'TourSpending3': '첫 실행 안내 · 소비 3 / 3 카테고리',
    'TourGoals1': '첫 실행 안내 · 목적지 1 / 3 월 저축 배분',
    'TourGoals2': '첫 실행 안내 · 목적지 2 / 3 도착 예상',
    'TourGoals3': '첫 실행 안내 · 목적지 3 / 3 목적지 추가',
    'TourFuture1': '첫 실행 안내 · 미래 1 / 3 자산 경로',
    'TourFuture2': '첫 실행 안내 · 미래 2 / 3 다음 지점',
    'TourFuture3': '첫 실행 안내 · 미래 3 / 3 가정',
    'TourDebts1': '첫 실행 안내 · 부채 1 / 3 총부채',
    'TourDebts2': '첫 실행 안내 · 부채 2 / 3 고금리 경고',
    'TourDebts3': '첫 실행 안내 · 부채 3 / 3 부채 목록',
    'TourStrategy1': '첫 실행 안내 · 상환 전략 1 / 3 상환 방식',
    'TourStrategy2': '첫 실행 안내 · 상환 전략 2 / 3 예상 완제',
    'TourStrategy3': '첫 실행 안내 · 상환 전략 3 / 3 완제 순서',
    'TourLedger1': '첫 실행 안내 · 내역 1 / 3 검색 · 칩',
    'TourLedger2': '첫 실행 안내 · 내역 2 / 3 날짜 묶음',
    'TourLedger3': '첫 실행 안내 · 내역 3 / 3 거래 추가',
    'TourLimits1': '첫 실행 안내 · 한도 1 / 3 총한도',
    'TourLimits2': '첫 실행 안내 · 한도 2 / 3 카테고리 배분',
    'TourLimits3': '첫 실행 안내 · 한도 3 / 3 계산 근거',
    'TourGoalDesign1': '첫 실행 안내 · 새 목적지 설계 1 / 3 두 탭',
    'TourGoalDesign2': '첫 실행 안내 · 새 목적지 설계 2 / 3 추천',
    'TourGoalDesign3': '첫 실행 안내 · 새 목적지 설계 3 / 3 입력',
    'TourPayoff1': '첫 실행 안내 · 상환 계획 1 / 3 가정',
    'TourPayoff2': '첫 실행 안내 · 상환 계획 2 / 3 비교',
    'TourPayoff3': '첫 실행 안내 · 상환 계획 3 / 3 저장',
}

# 페이지는 단계(v3 · v4 · v5)가 아니라 화면 종류로 묶는다(2026-09-22 사용자 요청 — "이제 다 v5"). 이름은 내용 그대로.
# 캔버스에 올리지 않는 원본 전용 장(SOURCE_ONLY)은 생성기가 잘라 쓰는 옛 그림이라 저장소에만 둔다 — 달력 없는 홈 둘 · 옛 내역 · 옛 월 마감 · 옛 데스크톱 홈.
SOURCE_ONLY = ['Main', 'HomeScroll', 'Ledger', 'MonthlyClose', 'DesktopHome']
PAGES = [
    ('home', '홈', 5,
     ['HomeCalendarStrip', 'HomeCalendar', 'HomeCalendarPrev', 'HomeCalendar360', 'HomeDefaultScroll',
      'HomeConfigured', 'HomeStocksCard', 'DoneCard', 'HeroInsufficient']),
    ('daysheet', '하루 시트 · 기록', 5,
     ['DaySheet', 'DaySheetList', 'DaySheetEdit', 'DaySheetScrolled', 'DaySheetNoSpend',
      'DaySheet360', 'ClassifySheet', 'ReviewListSheet', 'RecurringPrefill', 'TransactionAddFromDaySheet']),
    ('assets-spending', '자산 · 소비', 4,
     ['Assets', 'Debts', 'Strategy', 'Spending', 'LedgerV5', 'Limits', 'SpendingPast', 'MonthlyCloseV5']),
    ('dest-future', '목적지 · 미래 (지금 5탭 → 탭 합친 뒤)', 4,
     ['Goals', 'GoalDesign', 'Future', 'Payoff', 'DestGoals', 'DestFuture', 'DestPayoff', 'HomeStocksOff']),
    ('first-run', '첫 실행', 4,
     ['IntroPosition', 'IntroRoute', 'IntroDestination', 'Onboarding',
      'HomeSetup', 'HomeSetupStocksOn', 'SettingsHomeEntry', 'HomeLayoutEdit']),
    ('tour', '첫 실행 안내 · 화면마다 3단계', 3,
     ['TourHome1', 'TourHome2', 'TourHome3', 'TourAssets1', 'TourAssets2', 'TourAssets3',
      'TourSpending1', 'TourSpending2', 'TourSpending3', 'TourGoals1', 'TourGoals2', 'TourGoals3',
      'TourFuture1', 'TourFuture2', 'TourFuture3',
      'TourDebts1', 'TourDebts2', 'TourDebts3', 'TourStrategy1', 'TourStrategy2', 'TourStrategy3',
      'TourLedger1', 'TourLedger2', 'TourLedger3', 'TourLimits1', 'TourLimits2', 'TourLimits3',
      'TourGoalDesign1', 'TourGoalDesign2', 'TourGoalDesign3', 'TourPayoff1', 'TourPayoff2', 'TourPayoff3']),
    ('stocks', '주식', 4,
     ['StocksMine', 'HoldingAdd', 'StocksEmpty', 'StocksHome', 'StockListGrowth', 'StockListDividend',
      'StockDetail', 'StockThemes', 'StockStates', 'SnapshotUpdate']),
    ('modals', '모달 · 설정', 5,
     ['ProfileDialog', 'TransactionAdd', 'LimitEditor', 'AssetDialog', 'DebtDialog', 'GoalDialog',
      'RecurringDialog', 'GoalContribute', 'ImportReview', 'CoachPanel', 'CoachEmpty',
      'AlertsPanel', 'AlertsEmpty', 'PeerDialog', 'StockSettings']),
    ('desktop', '데스크톱', 2, ['DesktopHomeV5', 'DesktopLedger']),
    ('states', '상태 · 구현 참고', 3,
     ['StorageStates', 'EmptyStates', 'PeerStates', 'GoalTypes', 'ModalErrors', 'Confirmations',
      'CalendarCells', 'CalendarGridSizes', 'CalendarStatusLines', 'HeroFootnotes', 'DaySheetConfirm',
      'DaySheetStates', 'DaySheetNoSpendStates', 'DoneCardStates', 'InsufficientElsewhere', 'FutureProvisional',
      'LimitCardCases', 'EtcSubline', 'ImportBackupNotes']),
    ('system', '디자인 시스템', 2, ['Tokens', 'Components']),
]


def dark_of(name):
    """라이트 아트보드의 다크 짝. 없으면 None."""
    twin = 'DarkHome' if name == 'Main' else f'Dark{name}'
    return twin if (OUT / f'{twin}.dc.html').exists() else None

NOTES = {
    'home': ('note-home', 640,
             '홈 — 히어로(월급 대비 소비율 · 고정) 아래 첫 카드가 이번 달 달력. 기록의 입구는 달력 날짜(오늘 칸)이고 히어로에 「소비 기록하기」 버튼은 없다(2026-09-22).\n\n'
             '첫 줄: 달력 접힘(최근 7일) · 펼침(7열 월 달력 · 3일 칸 누름) · ‹ 지난달 · 360px 좁은 폰(월 달력 그대로) · 기본 5카드 전체 스크롤. '
             '둘째 줄: 첫 실행 홈 구성의 결과(달력 · 다음 안내 · 한도 · 순자산 · 상환) · 주식 요약 카드가 있는 홈 · 저장 뒤 완료 카드 · 예상 기준을 확인하기 전의 히어로(이력 부족).\n\n'
             '한도 라벨 「하루 47,270원」은 1 · 2단계, 「앞으로 하루」는 3단계 뒤(주식 카드 홈만). 같은 값은 모든 장에서 같다(design/CHANGES-2026-09-20.md 숫자 기준표).\n\n'
             '── 아래 줄은 다크입니다. darken.py가 라이트에서 만든 토큰 매핑 사본이고 레이아웃은 1px도 다르지 않습니다.'),
    'daysheet': ('note-daysheet', 640,
                 '하루 시트 — 날짜 칸을 누르면 홈 위에 뜨는 빠른 기록. 키보드가 열린 상태가 기본(오늘 · 기록 없는 날), 기록 있는 과거 날은 목록 우선, 수정 모드, 키보드 내린 모습, 소비 0건인 날(오늘은 안 썼어요), 360 × 640.\n\n'
                 '분류하기 시트(분류 안 함 7건 · 32,000원) · 확인할 내용 목록 · 반복 거래 미리 채움(휴대폰 요금 · 매월 25일 · 5.5만원) · 하루 시트에서 넘어온 거래 추가(구현 참고).\n\n'
                 '규칙은 plan/v5-calendar.md §4 · §5. 계산은 naviMetrics 한 곳, 초안은 메모리만, 되돌리기는 대상 지정.\n\n── 아래 줄은 다크입니다.'),
    'assets-spending': ('note-assets-spending', 640,
                        '자산 · 소비 탭 — 자산 구성 · 부채 · 상환 전략 · 소비 이번 달(계획선 그래프) · 내역(분류 안 함 칩 · 날짜별 합계) · 한도 · 지난달(마감) · 월 마감(분류 안 함 안내).\n\n'
                        '화면당 display 숫자는 하나(자산 = 순자산 · 소비 = 계획 대비 속도). 미입력은 회색 —. 가정은 보라 점선 + 「저장되지 않는 가정」.\n\n── 아래 줄은 다크입니다.'),
    'dest-future': ('note-dest-future', 640,
                    '목적지 · 미래 — 첫 줄은 지금 앱의 5탭(목표 · 새 목적지 설계 · 미래 자산 경로 · 상환 계획). '
                    '둘째 줄은 탭을 합친 뒤(v4 2단계 · plan/v4-stocks.md §4): 목표 + 미래 → 「목적지」 한 탭(세그먼트 내 목적지 · 자산 경로 · 상환 계획), 주식을 끄면 4탭 홈.\n\n'
                    '합친 탭에서 새 목적지 설계는 목록 끝 점선 버튼으로 들어간다. 시뮬레이션 값은 calc/crosscheck.py 확정값(총이자 1,734만원 · 완제 2036년 4월).\n\n── 아래 줄은 다크입니다.'),
    'first-run': ('note-first-run', 640,
                  '첫 실행 — 소개 3장(현재 위치 · 항로 · 목적지 · 한 장에 한 문장 · 어디서든 건너뛰기) → 홈 구성 → 시작 화면(내 데이터로 / 샘플로) → 홈.\n\n'
                  '홈 구성: 소비율과 이번 달 달력은 고정 행(둘 다 끌 수 없음 · 2026-09-22), 아래 카드는 4개까지, 행마다 아이콘. 「주식도 볼까요?」는 1단계부터 보이고 켜면 목록 끝에 주식 요약 행. '
                  '이 화면은 처음 설치해 처음 실행할 때만 뜨고, 그 뒤엔 설정 창의 「홈 구성 ›」 행 → 같은 목록(닫기 · 저장)으로만 바꾼다. 샘플 → 내 데이터로 넘어가도 구성은 그대로.\n\n'
                  '저장은 settings.homeLayout · settings.onboarding · settings.features(보호 파일 · 백업 형식 불변).\n\n── 아래 줄은 다크입니다.'),
    'tour': ('note-tour', 640,
             '첫 실행 안내 — 앱을 처음 설치해 첫 실행할 때, 화면에 처음 들어가면 그 화면의 안내가 1단계부터 뜹니다(2026-09-22 사용자 요청). 다섯 탭(홈 · 자산 · 소비 · 목적지 · 미래)과 탭 안의 세그먼트 화면 여섯(부채 · 상환 전략 · 내역 · 한도 · 새 목적지 설계 · 상환 계획) — 11화면 × 3단계 = 33장. 줄 순서 = 탭 다섯 → 세그먼트 여섯.\n\n'
             '어두운 막 위에 요소 하나만 밝히고(브랜드 파랑 테두리) 그 아래 12px에 카드 — 요소가 화면 아래쪽이면 카드는 위. '
             '카드 = 「처음 안내」 알약 + 「탭 n / 3」 · 제목 16 / 700 · 본문 13 / 1.55 · 「건너뛰기」(그 탭의 남은 단계를 건너뜀) · 「다음」/「알겠어요」 40px.\n\n'
             '다시 보려면 설정 › 도움말 › 「처음 안내 다시 보기」. 저장은 settings.onboarding.tourSeen = {home, assets, debts, strategy, spending, ledger, limits, goals, goalDesign, future, payoff}. '
             '좌표와 문구는 gen_tour.py의 표(실측)이고 탭 장을 고치면 다시 잽니다.\n\n── 아래 줄은 다크입니다.'),
    'stocks': ('note-stocks', 640,
               '주식 — 내 종목(보유 · 관심 · 직접 입력) · 보유 기록 모달 · 빈 상태 · 둘러보기(투자 여력 띠 · 가드레일 · 성장 / 저평가 / 배당 / 테마) · 성장주 · 배당주 목록 · 종목 상세(내 항로에 넣어보기) · 테마 · 특수한 상황 6가지 · 종목 데이터 새로 받기.\n\n'
               '추천 · 매수 · 매도라는 말을 쓰지 않는다. 가격 옆에는 항상 기준일(9/4 종가). 기준값은 사용자 것(설정 › 주식). 스냅숏 수치는 전부 가상(design/stocks-snapshot.sample.json).\n\n── 아래 줄은 다크입니다.'),
    'modals': ('note-modals', 640,
               '모달 · 설정 — 내 수치 입력 · 거래 추가 · 한도 조정 · 자산 · 부채 · 목적지 · 반복 거래 · 적립 · 백업 불러오기 · 코칭(있음 · 없음) · 알림(있음 · 없음) · 또래 기준 · 설정 › 주식.\n\n'
               '단독 행 필드는 solo, 버튼 · 배지는 nowrap. 필수 아님 표기는 「선택 사항」. 저장 실패는 창 안에 고정.\n\n── 아래 줄은 다크입니다.'),
    'desktop': ('note-desktop', 640,
                '데스크톱 1440 — 홈은 히어로 아래 왼쪽 열 첫 자리에 펼친 월 달력(폭 348 · 늘 펼침 · 접기 없음), 그래프는 그 오른쪽, 사이드바는 주식 켠 5칸(주식 수치 옆 기준일). 히어로에 「소비 기록하기」 없음. 소비 내역은 왼쪽 목록 + 오른쪽 상세.\n\n── 아래 줄은 다크입니다.'),
    'states': ('note-states', 640,
               '상태 카탈로그와 구현 참고 장 — 앱 화면이 아니라 설명 장(맨 위 알약 「구현 참고 · 앱 화면이 아닙니다」).\n\n'
               '저장소 로딩 · 복구 / 미입력 6종(F = 히어로 이력 부족) / 또래 카드 5종 / 목적지 유형 5종 / 모달 오류 · 저장 6종 / 삭제 · 초기화 확인 / 달력 칸 읽는 법 / 펼치면 어디서나 월 달력 / 달력 아래 한 줄이 바뀌는 경우 / 홈 맨 위 카드의 안내 줄 / '
               '저장을 한 번 더 물어보는 경우 / 기록 창의 글이 바뀌는 경우 / 안 쓴 날 표시 / 완료 카드의 경우들 / 예상 기준 확인 전 홈 밖의 화면 / 미래의 잠정 표시 / 한도 카드 네 경우 / 기타 서브라인 / 가져오기 · 백업 안내.\n\n── 아래 줄은 다크입니다.'),
    'system': ('note-system', 640,
               '디자인 시스템 — 토큰(색 · 타이포 · 간격 · 08절 v5 토큰)과 컴포넌트 24종 + v5 11종의 상태. 값의 최종 기준은 아트보드이고 실측 CSS는 design/SPEC-COMPONENTS.md.\n\n'
               '── 아래 줄은 다크입니다. 토큰 장만 다크가 없습니다(표 자체가 두 테마를 보여 줍니다).'),
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

canvas = {
    'pages': [{'id': p, 'name': n} for p, n, _, _ in PAGES],
    'artboards': artboards,
    'annotations': annotations,
    'launch': {'view': 'canvas', 'page': 'home'},
}

(OUT / 'canvas.json').write_text(json.dumps(canvas, ensure_ascii=False, indent=2), encoding='utf-8')

have = {p.name.replace('.dc.html', '') for p in OUT.glob('*.dc.html')}
listed = {a['file'].replace('.dc.html', '') for a in artboards}
print(f'{len(artboards)} artboards across {len(PAGES)} pages')
src = {n for n in have - listed if n in SOURCE_ONLY or (n.startswith('Dark') and (n[4:] in SOURCE_ONLY or n == 'DarkHome'))}
print('원본 전용(캔버스에 안 올림):', sorted(src) or '없음')
print('배치 안 된 파일:', sorted(have - listed - src) or '없음')
print('파일 없는 항목:', sorted(listed - have) or '없음')
