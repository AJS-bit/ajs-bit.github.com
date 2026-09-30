# -*- coding: utf-8 -*-
import json
import pathlib

OUT = pathlib.Path(__file__).resolve().parent.parent

PHONE = (390, 844)
# 프레임 높이는 "실제 웹폰트로 렌더한 자연 높이 + 아래 여백 24px"이다.
# 폴백 폰트로 재면 한글 줄 높이가 짧게 나와 실제보다 작은 값이 나온다. 반드시 IBM Plex Sans KR로 재라.
TALL = {'StorageStates': 2787, 'PeerStates': 2972,   # 2026-09-30 저장소 A 마크 40(자연 2763 + 24) · 2026-09-26 DZ2 저장소 B′ · C · D 확인 창 / 또래 6종(D 세 가지 이유)
        # 2026-09-26 DZ2 앱 따라잡기 — 탭 장은 본문을 다 보여 주는 높이(자연 높이 + 24 · 첫 실행 안내는 gen_tour 가 844 로 자른다)
        'StocksMine': 912,   # 2026-09-27 fix-up 관심 5종목 끝까지(자연 888 + 24)
        'SpendingPast': 1212, 'SpendingPastOpen': 1264, 'SpendingPastChanged': 1212,   # 2026-09-27 fix-up 2 월 마감 카드 앱 글자 크기 ·   # 2026-09-27 fix-up 지난 달 월 요약도 본문 전체(자연 + 24)
        'GoalsStates': 4432, 'GoalDesignStates': 1421,   # 2026-09-26 DZ2 새 장(목적지 · 새 목적지 설계의 상태)
        'Assets': 977, 'Debts': 909, 'Spending': 957, 'Limits': 1106, 'Goals': 992, 'GoalDesign': 1231, 'Future': 1204, 'Payoff': 924,
        'Confirmations': 2265,   # 2026-09-27 fix-up 5 자연 2241 + 24(앱 AlertDialog 버튼 32) · 2026-09-25 확인 창 7종 1245 → 2300 · EmptyStates 는 2026-09-26 WIDE 로(가로 설명 장)
        'ModalErrors': 3290, 'GoalTypes': 2170,   # 2026-09-27 fix-up 5 오류 7종 자연 3266 + 24 ·   # 2026-09-25 오류 7종 2100 → 3289 · 목적지 유형 앱 칸 1920 → 2104
        # 2026-09-25 앱 따라잡기(DZ1) — 본문을 다 보여 주는 긴 시트(gen_modals.H · 손편집 LimitEditor)
        'ProfileDialog': 1229, 'LimitEditor': 1297, 'RecurringDialogOverlap': 945, 'GoalContribute': 892,   # 2026-09-27 fix-up 5 앱 c6b7de3 치수(자연 1205 · 1273 · 921 · 868 + 24) · 목적지 추가(부채 상환)는 자연 838 → 한 화면 844
        'CoachPanel': 942, 'ImportReview': 905, 'MonthlyCloseV5': 1099,   # 코칭 자연 918 + 24
        'MonthlyClose': 982,   # 원본 전용(캔버스 밖) · 다시 연 마감 창
        'HomeDefaultScroll': 1555,   # 2026-09-30 펼친 달력이 홈의 기본 · 자연 1531 + 24 · 2026-09-27 fix-up 캐논 각주 두 줄 · 자연 1217 + 24 · 2026-09-26 DZ4 앱 기본 카드 4개(다음 안내 · 한도 · 순자산 · 상환 계획) · 자연 1242 + 24
        'HomeMonthStart': 1432, 'HomeSampleMode': 1537,   # 2026-09-30 펼친 10월 · 9월(자연 1408 · 1513 + 24) · 2026-09-26 DZ4 새 홈 장(10월 2일 첫 주 · 샘플 모드) — 자연 높이 + 24
        'RecurringPrefill': 877, 'SettingsNotify': 903,   # 2026-09-27 fix-up 5 반복 기록 미리 채움 자연 853 + 24 ·   # 2026-09-26 DZ4 반복 기록 목록이 먼저 · 알림 테스트 줄 아래 백업 줄
        'HomeConfigured': 1492,   # 2026-09-30 펼친 빈 9월(자연 1468 + 24)
        'HeroInsufficient': 1501, 'HomeTargetSaved': 1510,   # 2026-09-30 펼친 달력 아래 기본 카드 넷(순자산 · 상환 계획 한 줄까지)이 끝까지 보이는 전체 스크롤(자연 1475 · 1486 + 24 · 앱 docH 1501 · 1510 — 시작일 줄 위 여백 4(앱과 같게 · 2026-09-30 마지막 점검) · 한도 카드에서 끝나던 판 1356 · 1457 · 예전 844)
        'HomePrimaryGoal': 1509, 'AssetsStale': 1033, 'GoalDialogPreview': 981}   # 2026-09-27 fix-up 3 새 장(자연 + 24)   # 2026-09-26 DZ3 첫 실행 뒤 홈(내 데이터 · 빈 히어로 · 시작 순서 · 카드 3개) 전체 — 자연 1154 + 24
TALL.update({'Dark' + k: v for k, v in TALL.items()})
WIDE = {'DesktopHome': (1440, 900), 'DesktopLedger': (1440, 976), 'DarkDesktopHome': (1440, 900),
        'DarkDesktopLedger': (1440, 976),   # 2026-09-27 fix-up 앱 머리 자리(격자 166) + 오른쪽 카드 넷(773) — 예전 900 은 넷째 카드가 잘림
        'DesktopHomeV5': (1440, 1273), 'DarkDesktopHomeV5': (1440, 1273),   # 자연 1249 + 24(2026-09-27 fix-up · 히어로 각주 두 줄 · 앱 기본 카드 순자산 · 상환 계획 한 줄)
        'EmptyStates': (2002, 2667), 'DarkEmptyStates': (2002, 2667),   # 2026-09-30 A 칸 펼친 빈 달력 · 자연 2643 + 24 · 2026-09-27 fix-up 2 자연 2329 + 24 ·   # 2026-09-27 fix-up C · F 합계 고치기 줄 뺌 · 자연 2311 + 24 ·   # 2026-09-26 DZ3 390 × 2800 → 가로 설명 장(일곱 경우 + 화면별 빈 카드 · 자연 2336 + 24)   # v5 달력이 들어간 데스크톱 홈(2026-09-21 채택 · 2026-09-24 1000 → 1070 달력 안내 줄 · 적기 줄)
        'Tokens': (1200, 2273), 'Components': (1200, 4826), 'DarkComponents': (1200, 4826),   # 2026-09-30 08 ② · ③ 설명(자연 4802 + 24) ·   # 2026-09-27 fix-up 5 토큰 달력 색 여섯 · 컴포넌트 04 잠긴 칸 안내 상자 · 확인 창 앱 치수(자연 2249 · 4749 + 24) ·   # 2026-09-27 fix-up 2 토큰 warning DARK 한 줄 · 컴포넌트 01 저장 중 두 가지 ·   # 2026-09-26 DZ4 토큰(앱 tokens.v3.css · sky · 첫 실행 안내 층 · D1 · D13) · 컴포넌트 01~07 새 내용 + 09 탭 머리줄 + 10 판정 줄   # 2026-09-26 DZ3 2920 → 2979(08절 달력 카드 범례 줄 · 자연 2955 + 24)
        'DaySheet360': (360, 640), 'DarkDaySheet360': (360, 640),   # 작은 폰 360 × 640
        'HomeCalendar360': (360, 844), 'DarkHomeCalendar360': (360, 844),   # v5 좁은 폰
        # v5 구현 참고 장 — 폰 프레임이 아니라 가로로 넓은 설명 장
        'CalendarCells': (1330, 880), 'DarkCalendarCells': (1330, 880),   # 2026-09-26 DZ4 범례 줄
        'CalendarGridSizes': (1150, 1745), 'DarkCalendarGridSizes': (1150, 1745),   # 2026-09-26 DZ3 범례 줄 1670 → 1714
        'DaySheetConfirm': (1200, 1221), 'DarkDaySheetConfirm': (1200, 1221),   # 2026-09-27 fix-up 4 하루 시트 상자 모형(자연 1197 + 24)   # 2026-09-26 DZ4 칸 이름 위 · 견본마다 기본 행동 저장
        'HeroFootnotes': (1200, 800), 'DarkHeroFootnotes': (1200, 800),
        'HeroOverTarget': (1230, 765), 'DarkHeroOverTarget': (1230, 765),   # 2026-09-27 fix-up 5 자연 741 + 24(729 에서 12px 잘려 있던 것) · fix-up 2 새 장(홈 맨 위 카드 · 소비 목표를 넘을 때)   # 2026-09-26 DZ4 다섯 경우(합계 고치기 줄)
        # 최신화 반영(2026-09-21) — v5 구현 참고 장과 다른 화면에 닿는 곳
        'CalendarStatusLines': (1200, 2673), 'DarkCalendarStatusLines': (1200, 2673),   # 2026-09-30 자연 2649 + 24(3초 안내 = 안내 줄 자리) ·   # 2026-09-27 fix-up 5 자연 2605 + 24(이체만 견본 · 확인할 내용 2개) · fix-up 2 확인할 내용 행 ·   # 2026-09-26 DZ4 저녁 링크 뒤 · 이체만 · 항목 하나 · 첫 주 · 막힌 ‹ · 그 달 0건   # 2026-09-26 DZ3 범례 줄 1570 → 1613 ·   # 2026-09-24 후속 1160 → 1500(처음 쓰는 날 · 펼친 달력 오늘 0건 견본) → 1540(최종 점검 후속 · 미래 견본의 확인할 내용 행 · 메모) → 1570(통합 점검 · 샘플 문장 위 줄)
        'DaySheetNoSpendStates': (1200, 1252), 'DarkDaySheetNoSpendStates': (1200, 1252),   # 2026-09-27 fix-up 5 실제 웹폰트 자연 1228 + 24 · fix-up 4 이체 줄 두 줄   # 2026-09-24 후속 1160 → 1190(오늘 칸 + → 0 → + 견본)
        'DoneCardStates': (1200, 1534), 'DarkDoneCardStates': (1200, 1534),   # 2026-09-26 DZ4 칩 줄 · 띠 · 옮겼어요 · 저축·투자
        'DaySheetStates': (1210, 1919), 'DarkDaySheetStates': (1210, 1919),
        'TransactionAddFromDaySheet': (960, 908), 'DarkTransactionAddFromDaySheet': (960, 908),   # 2026-09-25 850 → 908(날짜 · 금액 두 줄 · 다른 입구)
        'AssetDebtTypes': (1400, 770), 'DarkAssetDebtTypes': (1400, 770),   # 2026-09-27 fix-up 5 자연 746 + 24 ·   # 2026-09-25 자산 · 부채 유형 목록 참고 장(gen_modals)
        'InsufficientElsewhere': (1230, 1864), 'DarkInsufficientElsewhere': (1230, 1864),   # 2026-09-27 fix-up 4 절감 가정 눈금 줄 · 계산 기준(자연 1840 + 24)   # 2026-09-27 fix-up 2 ·   # 2026-09-26 DZ4 코치 목록 · 다음 안내 두 견본   # 2026-09-26 DZ2 검토 1390 → 1453(자른 탭 장이 길어짐)
        'FutureProvisional': (1230, 1256), 'DarkFutureProvisional': (1230, 1256),
        'EtcSubline': (1200, 1715), 'DarkEtcSubline': (1200, 1715),   # 2026-09-27 fix-up 4 절감 가정 눈금 줄 · 계산 기준 둘(자연 1691 + 24)   # 2026-09-27 fix-up 2 코치 셋째 카드 · 절감 가정
        'LimitCardCases': (1200, 1464), 'DarkLimitCardCases': (1200, 1464),   # 2026-09-27 fix-up 5 자연 1438 + 24 ·   # 2026-09-26 DZ4 첫 기록 전 · 시작한 달 · 카테고리 넘음 · 한도 탭 두 카드   # 2026-09-26 DZ3 평소 카드에 둘째 줄(home-3) 960 → 977(자연 953 + 24)
        'ImportBackupNotes': (1230, 1103), 'DarkImportBackupNotes': (1230, 1103),
        'NotifyCases': (1200, 1435), 'DarkNotifyCases': (1200, 1435),   # 2026-09-27 fix-up 4 알림 줄 56(자연 1411 + 24)   # 2026-09-26 DZ4 꺼져 있을 때 · 처음 묻는 카드
        # 2026-09-26 DZ4 새 구현 참고 장(gen_v5_screens)
        'PayoffStates': (1230, 1501), 'DarkPayoffStates': (1230, 1501), 'FutureStates': (1230, 1749), 'DarkFutureStates': (1230, 1749),
        'HomeGlanceRows': (1230, 1045), 'DarkHomeGlanceRows': (1230, 1045), 'SampleModeTabs': (1290, 823), 'DarkSampleModeTabs': (1290, 823),
        'DebtUnpayable': (1230, 936), 'DarkDebtUnpayable': (1230, 936),   # 기기 알림 참고 장 (gen_notify.py · 2026-09-23)
        # v4 구현 참고 장 (gen_v4_stocks.py)
        'StockStates': (1180, 975), 'DarkStockStates': (1180, 975),   # 2026-09-27 fix-up 2 식 줄 두 줄 ·   # 2026-09-26 DZ3 6 → 8가지(지난달 미마감 · 월급 없음) 880 → 961
        'SnapshotUpdate': (1180, 750), 'DarkSnapshotUpdate': (1180, 750),
        'TourRules': (1200, 1760), 'DarkTourRules': (1200, 1760)}   # 2026-09-26 DZ5 첫 실행 안내 규칙 참고 장(gen_tour · 자연 1658 + 24 · 검토에서 배치 줄 하나 더)   # 2026-09-26 DZ3 ④ 닫은 뒤 알림을 뺌(D10) 762 → 750

TITLES = {
    'Main': '홈 · 오늘의 내비게이션', 'HomeScroll': '홈 · 아래로 스크롤',
    'Assets': '자산 · 구성', 'Debts': '자산 · 부채', 'Strategy': '자산 · 상환 계획(읽기 전용 요약)',
    'Spending': '소비 · 이번 달', 'Ledger': '소비 · 내역', 'Limits': '소비 · 한도',
    'Goals': '목적지 · 내 목적지', 'GoalDesign': '목적지 · 새 목적지 설계',
    'Future': '미래 · 자산 경로', 'Payoff': '미래 · 상환 계획', 'Onboarding': '첫 실행 · 시작 방법 고르기',
    'LimitEditor': '모달 · 한도 조정', 'TransactionAdd': '모달 · 기록 추가',
    'ProfileDialog': '모달 · 내 수치', 'AssetDialog': '모달 · 자산 추가',
    'DebtDialog': '모달 · 부채 수정', 'GoalDialog': '모달 · 목적지 추가',
    'RecurringDialog': '모달 · 반복 기록', 'MonthlyClose': '모달 · 월 마감',
    'ImportReview': '모달 · 백업 불러오기', 'CoachPanel': '모달 · 코칭',
    'AlertsPanel': '모달 · 알림 (중요 1건)', 'AlertsEmpty': '모달 · 알림 0건', 'PeerDialog': '모달 · 또래 기준 등록',
    'StorageStates': '상태 · 저장소 로딩·복구 · 샘플에서 내 데이터로', 'PeerStates': '상태 · 또래 카드 6종',
    'EmptyStates': '참고 · 미입력 7종 · 화면마다의 빈 카드', 'Confirmations': '상태 · 삭제·초기화·확인 창 7종',
    'ModalErrors': '상태 · 모달 오류·저장 7종', 'GoalTypes': '상태 · 목적지 유형 5종',
    'SpendingPast': '소비 · 지난 달 (마감)', 'GoalContribute': '모달 · 적립',
    'CoachEmpty': '모달 · 코칭 기록 없음',
    'DesktopHome': '데스크톱 · 홈', 'DesktopLedger': '데스크톱 · 소비 내역',
    'Tokens': '토큰 · 색 · 타이포 · 간격', 'Components': '컴포넌트 · 상태',
    # v4 · 1단계 (gen_v4.py)
    'IntroPosition': '첫 실행 · 소개 1 현재 위치', 'IntroRoute': '첫 실행 · 소개 2 항로',
    'IntroDestination': '첫 실행 · 소개 3 목적지', 'HomeSetup': '첫 실행 · 홈 구성',
    'HomeConfigured': '홈 · 첫 실행 뒤 (내 데이터 · 카드 3개)',
    # v4 · 2~5단계 (gen_v4_stocks.py)
    'DestGoals': '목적지 · 내 목적지 (5탭)', 'DestFuture': '목적지 · 자산 경로 (5탭)', 'HomeStocksOff': '홈 · 주식 꺼짐 (4탭)',
    'StocksMine': '주식 · 내 종목 (계획 · 3단계)', 'HoldingAdd': '모달 · 보유 추가', 'StocksEmpty': '주식 · 빈 상태', 'HomeStocksCard': '홈 · 주식 요약 카드 (계획 · 3단계 뒤 · 앱에는 아직 없음)',
    'StocksHome': '주식 · 둘러보기', 'StockListGrowth': '주식 · 성장주 목록', 'StockListDividend': '주식 · 배당주 목록',
    'StockDetail': '주식 · 종목 상세', 'StockThemes': '주식 · 테마', 'StockStates': '참고 · 주식 탭 특수한 상황 8가지',
    'StockSettings': '모달 · 설정 › 주식', 'SnapshotUpdate': '참고 · 종목 데이터 새로 받기',
    # v5 · 1단계 (gen_v5.py)
    'DaySheet': '하루 시트 · 오늘 (키보드 열림)', 'DaySheetList': '하루 시트 · 기록 있는 과거 날 (목록 우선)',
    'DaySheetEdit': '하루 시트 · 수정 모드', 'DoneCard': '홈 · 저장 뒤 완료 카드', 'DaySheetConfirm': '참고 · 저장을 한 번 더 물어보는 경우',
    'ClassifySheet': '카테고리 고르기 시트', 'HeroInsufficient': '홈 · 히어로 이력 부족', 'DaySheet360': '하루 시트 · 360 × 640 작은 폰',
    'HeroFootnotes': '참고 · 홈 맨 위 카드의 안내 줄',
    'HomeCalendarStrip': '홈 · 달력을 접었을 때 (7일 줄)', 'HomeCalendar': '홈 · 달력 펼침 (월 달력 · 기본)',
    'HomeCalendar360': '홈 · 달력 펼침 · 360px (월 달력 그대로)', 'HomeCalendarPrev': '홈 · 달력 펼침 · ‹ 지난달 8월 보기',
    'CalendarCells': '참고 · 달력 칸 읽는 법', 'CalendarGridSizes': '참고 · 달력은 어느 폭 · 글자 크기에서나 월 달력',
    # 최신화 반영(2026-09-21) 새 장
    'HomeSetupStocksOn': '첫 실행 · 홈 구성 · 주식 알림 켬',
    'SettingsHomeEntry': '설정',      # 2026-09-27 fix-up — D5 설정 시트 전체(홈 구성 행만이 아님)
    'HomeLayoutEdit': '설정 › 홈 구성 (처음 실행 뒤에 다시 고칠 때)',
    'DestPayoff': '목적지 · 상환 계획 (5탭)',
    'DaySheetScrolled': '하루 시트 · 키보드를 내린 모습',
    'DaySheetNoSpend': '하루 시트 · 소비 0건인 날 (오늘은 안 썼어요)',
    'ReviewListSheet': '확인할 내용 목록 시트',
    'HomeDefaultScroll': '홈 · 기본 카드 4개 전체 스크롤',
    'CalendarStatusLines': '참고 · 달력 아래 한 줄이 바뀌는 경우',
    'DaySheetNoSpendStates': '참고 · 안 쓴 날을 표시하는 경우',
    'DoneCardStates': '참고 · 저장 완료 카드의 경우들',
    'DaySheetStates': '참고 · 기록 창의 글이 바뀌는 경우',
    'LedgerV5': '소비 · 내역 (카테고리 없음 칩 · 날짜별 합계)',
    'MonthlyCloseV5': '모달 · 8월 첫 마감 (카테고리 없음 안내)',
    'TransactionAddFromDaySheet': '참고 · 기록 추가 — 하루 시트에서 넘어왔을 때',
    'InsufficientElsewhere': '참고 · 월말 예상 기준이 서기 전 — 홈 밖의 화면들',
    'FutureProvisional': '참고 · 미래 · 목적지의 임시 계산 표시',
    'EtcSubline': '참고 · 카테고리 없는 소비와 안 쓴 날 — 소비 · 한도 · 코치',
    'LimitCardCases': '참고 · 이번 달 한도 카드의 경우들',
    'RecurringPrefill': '반복 기록 · 방금 저장한 기록으로 미리 채움',
    'ImportBackupNotes': '참고 · 가져오기 · 백업 안내',
    # 2026-09-26 DZ4 새 장
    'HomeTargetEditor': '홈 · 소비 목표 조정 열림', 'HomeMonthStart': '홈 · 달이 바뀐 첫 주 (10월 2일)', 'HomeSampleMode': '홈 · 샘플 모드',
    'DaySheetDeleted': '하루 시트 · 지운 뒤 (되돌리기)', 'DaySheetPastEmpty': '하루 시트 · 기록 없는 어제', 'DaySheetEditMoved': '하루 시트 · 수정 · 날짜를 옮길 때',
    'ClassifySheetPicker': '카테고리 고르기 시트 · 줄에서 고르기 펼침',
    'PayoffStates': '참고 · 미래 › 상환 계획의 경우들', 'FutureStates': '참고 · 미래 › 자산 경로의 경우들', 'HomeGlanceRows': '참고 · 홈 자산 한눈에 줄 펼침',
    'SampleModeTabs': '참고 · 샘플 모드 띠 (모든 탭)', 'DebtUnpayable': '참고 · 월 최소 상환액을 비운 부채',
    'DesktopHomeV5': '데스크톱 · 홈',
    'TourHome1': '첫 실행 안내 · 홈 1 / 3 이번 달 소비',
    'TourHome2': '첫 실행 안내 · 홈 2 / 3 달력으로 기록',
    'TourHome3': '첫 실행 안내 · 홈 3 / 3 다음 안내',
    'TourAssets1': '첫 실행 안내 · 자산 1 / 3 세 탭',
    'TourAssets2': '첫 실행 안내 · 자산 2 / 3 순자산',
    'TourAssets3': '첫 실행 안내 · 자산 3 / 3 현금성 비상금',
    'TourSpending1': '첫 실행 안내 · 소비 1 / 3 세 탭',
    'TourSpending2': '첫 실행 안내 · 소비 2 / 3 속도 그래프',
    'TourSpending3': '첫 실행 안내 · 소비 3 / 3 카테고리',
    'TourGoals1': '첫 실행 안내 · 목적지 1 / 3 매달 모으는 돈',
    'TourGoals2': '첫 실행 안내 · 목적지 2 / 3 도착 예상',
    'TourGoals3': '첫 실행 안내 · 목적지 3 / 3 목적지 추가',
    'TourFuture1': '첫 실행 안내 · 미래 1 / 3 자산 경로',
    'TourFuture2': '첫 실행 안내 · 미래 2 / 3 다음 지점',
    'TourFuture3': '첫 실행 안내 · 미래 3 / 3 가정',
    'SettingsNotify': '모달 · 설정 › 알림 (기기 알림)', 'NotifyCases': '참고 · 기기 알림 여섯 가지와 규칙',
    'TourDebts1': '첫 실행 안내 · 부채 1 / 3 총부채',
    'TourDebts2': '첫 실행 안내 · 부채 2 / 3 상환 안내',
    'TourDebts3': '첫 실행 안내 · 부채 3 / 3 부채 목록',
    'TourStrategy1': '첫 실행 안내 · 자산 › 상환 계획 1 / 3 저장된 계획',
    'TourStrategy2': '첫 실행 안내 · 자산 › 상환 계획 2 / 3 다 갚는 달',
    'TourStrategy3': '첫 실행 안내 · 자산 › 상환 계획 3 / 3 갚는 순서',
    'TourLedger1': '첫 실행 안내 · 내역 1 / 3 검색 · 칩',
    'TourLedger2': '첫 실행 안내 · 내역 2 / 3 날짜 묶음',
    'TourLedger3': '첫 실행 안내 · 내역 3 / 3 기록 추가',
    'TourLimits1': '첫 실행 안내 · 한도 1 / 3 총한도',
    'TourLimits2': '첫 실행 안내 · 한도 2 / 3 카테고리 배분',
    'TourLimits3': '첫 실행 안내 · 한도 3 / 3 계산 근거',
    'TourGoalDesign1': '첫 실행 안내 · 새 목적지 설계 1 / 3 두 탭',
    'TourGoalDesign2': '첫 실행 안내 · 새 목적지 설계 2 / 3 추천',
    'TourGoalDesign3': '첫 실행 안내 · 새 목적지 설계 3 / 3 입력',
    'TourPayoff1': '첫 실행 안내 · 미래 › 상환 계획 1 / 3 추가 상환',
    'TourPayoff2': '첫 실행 안내 · 미래 › 상환 계획 2 / 3 비교',
    'TourPayoff3': '첫 실행 안내 · 미래 › 상환 계획 3 / 3 저장',
    # 2026-09-26 DZ5 첫 실행 안내 새 장(앱 a724aac)
    'TourHomeChecklist': '첫 실행 안내 · 홈 3 / 3 시작 순서 (처음 시작한 빈 홈)',
    'TourHomeSample1': '첫 실행 안내 · 홈 1 / 3 샘플로 둘러보기 (흐려진 샘플 띠 아래)',
    'HeroOverTarget': '참고 · 홈 맨 위 카드 · 소비 목표를 넘을 때',
    'TourHelpReplay': '첫 실행 안내 · 제목 옆 ?로 다시 연 안내 (화면 안내)',
    'TourRules': '참고 · 첫 실행 안내 규칙 (빈 화면 · 닫기 · 다시 보기 · 배치)',
    # 2026-09-25 앱 따라잡기(DZ1) 새 장
    'ProfileDialogNoItems': '모달 · 내 수치 (자산 · 부채를 안 넣었을 때)', 'SalarySheet': '모달 · 월급 입력',
    'NetWorthRatioSheet': '모달 · 순자산 대비 소비', 'AssetEditDialog': '모달 · 자산 수정',
    'AssetBalanceCheck': '모달 · 잔액 한 번에 확인 (자산 구성의 주황 띠에서 · 확인 필요 2개)',
    'RecurringDialogOverlap': '모달 · 반복 기록 (이번 달 겹침 확인)',
    'SpendingPastOpen': '소비 · 지난 달 (마감 전)', 'SpendingPastChanged': '소비 · 지난 달 (마감 뒤 기록이 바뀜)',
    'AssetDebtTypes': '참고 · 자산 · 부채 유형 목록 · 새 부채 · 다 갚은 부채',
    # 2026-09-26 앱 따라잡기(DZ2) 새 장
    # 2026-09-27 fix-up 3 새 장(검증에서 빠진 장면으로 짚은 것)
    'HomePrimaryGoal': '홈 · 대표 목적지 카드를 켰을 때', 'HomeTargetSaved': '홈 · 소비 목표를 저장한 직후 (알림 · 종 배지 3)',
    'AssetsStale': '자산 · 잔액 확인이 필요한 자산이 있을 때', 'AlertsPanelInfo': '모달 · 알림 (중요 1 · 참고 1)',
    'GoalDialogPreview': '모달 · 목적지 추가 (일반 저축 · 저장 전 미리 보기)',
    'GoalsStates': '참고 · 목적지 상태 7종 (가정 · 펼침 · 도착 · 목표일 없음 · 도착 어려움 · 상환 늦음 · 설계 미리 보기)', 'GoalDesignStates': '참고 · 새 목적지 설계 상태 2종 (처음 · 다른 금액 가정)',
}

# 페이지는 단계(v3 · v4 · v5)가 아니라 화면 종류로 묶는다(2026-09-22 사용자 요청 — "이제 다 v5"). 이름은 내용 그대로.
# 캔버스에 올리지 않는 원본 전용 장(SOURCE_ONLY)은 생성기가 잘라 쓰는 옛 그림이라 저장소에만 둔다 — 달력 없는 홈 둘 · 옛 내역 · 옛 월 마감 · 옛 데스크톱 홈.
SOURCE_ONLY = ['Main', 'HomeScroll', 'Ledger', 'MonthlyClose', 'DesktopHome']
PAGES = [
    ('home', '홈', 5,
     ['HomeCalendar', 'HomeCalendarPrev', 'HomeCalendar360', 'HomeCalendarStrip', 'HomeDefaultScroll',      # 2026-09-30 펼친 월 달력이 홈의 기본 — 접었을 때(7일 줄)는 그 뒤
      'HomePrimaryGoal', 'HomeConfigured', 'HomeStocksCard', 'DoneCard', 'HeroInsufficient',
      'HomeTargetEditor', 'HomeTargetSaved', 'HomeMonthStart', 'HomeSampleMode', 'HeroOverTarget']),
    ('daysheet', '하루 시트 · 기록', 5,
     ['DaySheet', 'DaySheetList', 'DaySheetEdit', 'DaySheetScrolled', 'DaySheetNoSpend',
      'DaySheet360', 'DaySheetPastEmpty', 'DaySheetDeleted', 'DaySheetEditMoved', 'ClassifySheet',
      'ClassifySheetPicker', 'ReviewListSheet', 'RecurringPrefill', 'TransactionAddFromDaySheet']),
    ('assets-spending', '자산 · 소비', 4,
     ['Assets', 'AssetsStale', 'Debts', 'Strategy', 'Spending', 'LedgerV5', 'Limits', 'SpendingPast', 'SpendingPastOpen', 'SpendingPastChanged', 'MonthlyCloseV5']),
    # 2026-09-27 fix-up: 참고 장 둘을 맨 끝 줄로 — 첫 줄 지금 탭 넷 · 둘째 줄 탭 합친 뒤 넷(바로 아래에서 비교) · 셋째 줄 참고 장(GoalsStates 4075 로 길다)
    ('dest-future', '목적지 · 미래 (지금 5탭 → 탭 합친 뒤)', 4,
     ['Goals', 'GoalDesign', 'Future', 'Payoff', 'DestGoals', 'DestFuture', 'DestPayoff', 'HomeStocksOff', 'GoalsStates', 'GoalDesignStates']),
    ('first-run', '첫 실행', 4,
     ['IntroPosition', 'IntroRoute', 'IntroDestination', 'HomeSetup',
      'HomeSetupStocksOn', 'Onboarding', 'SettingsHomeEntry', 'HomeLayoutEdit']),
    ('tour', '첫 실행 안내 · 화면마다 3단계', 3,
     ['TourHome1', 'TourHome2', 'TourHome3', 'TourAssets1', 'TourAssets2', 'TourAssets3',
      'TourSpending1', 'TourSpending2', 'TourSpending3', 'TourGoals1', 'TourGoals2', 'TourGoals3',
      'TourFuture1', 'TourFuture2', 'TourFuture3',
      'TourDebts1', 'TourDebts2', 'TourDebts3', 'TourStrategy1', 'TourStrategy2', 'TourStrategy3',
      'TourLedger1', 'TourLedger2', 'TourLedger3', 'TourLimits1', 'TourLimits2', 'TourLimits3',
      'TourGoalDesign1', 'TourGoalDesign2', 'TourGoalDesign3', 'TourPayoff1', 'TourPayoff2', 'TourPayoff3',
      'TourHomeChecklist', 'TourHelpReplay', 'TourRules', 'TourHomeSample1']),
    ('stocks', '주식', 4,
     ['StocksMine', 'HoldingAdd', 'StocksEmpty', 'StocksHome', 'StockListGrowth', 'StockListDividend',
      'StockDetail', 'StockThemes', 'StockStates', 'SnapshotUpdate']),
    ('modals', '모달 · 설정', 5,
     ['ProfileDialog', 'ProfileDialogNoItems', 'SalarySheet', 'NetWorthRatioSheet', 'TransactionAdd',
      'LimitEditor', 'AssetDialog', 'AssetEditDialog', 'AssetBalanceCheck', 'DebtDialog',
      'GoalDialog', 'GoalDialogPreview', 'RecurringDialog', 'RecurringDialogOverlap', 'GoalContribute', 'ImportReview',
      'CoachPanel', 'CoachEmpty', 'AlertsPanel', 'AlertsPanelInfo', 'AlertsEmpty', 'PeerDialog', 'StockSettings', 'SettingsNotify']),
    ('desktop', '데스크톱', 2, ['DesktopHomeV5', 'DesktopLedger']),
    ('states', '상태 · 구현 참고', 3,
     ['StorageStates', 'EmptyStates', 'PeerStates', 'GoalTypes', 'ModalErrors', 'Confirmations', 'AssetDebtTypes',
      'CalendarCells', 'CalendarGridSizes', 'CalendarStatusLines', 'HeroFootnotes', 'DaySheetConfirm',
      'DaySheetStates', 'DaySheetNoSpendStates', 'DoneCardStates', 'InsufficientElsewhere', 'FutureProvisional',
      'LimitCardCases', 'EtcSubline', 'ImportBackupNotes', 'NotifyCases', 'PayoffStates', 'FutureStates',
      'HomeGlanceRows', 'SampleModeTabs', 'DebtUnpayable']),
    ('system', '디자인 시스템', 2, ['Tokens', 'Components']),
]


def dark_of(name):
    """라이트 아트보드의 다크 짝. 없으면 None."""
    twin = 'DarkHome' if name == 'Main' else f'Dark{name}'
    return twin if (OUT / f'{twin}.dc.html').exists() else None

NOTES = {
    'home': ('note-home', 640,
             '홈 — 히어로(고정 · 큰 숫자와 게이지 = 이번 달 지금까지 쓴 돈 ÷ 월급 31.1%, 월말 예상 57.9%는 배지 · 아래 칸 글자로만 · 2026-09-24) 아래 첫 카드가 달력이다. '
             '홈에 들어오면 펼친 월 달력 「‹ 2026년 9월 ›」(2026-09-30부터 기본)이고, 「접기 ▴」를 누르면 7일 줄 「이번 달 소비 기록」 — 접은 것은 같은 실행 안에서만 남고 앱이 다시 시작되면 다시 펼친다(저장하지 않음 · 데스크톱은 늘 펼침). '
             '펼친 달력 때문에 홈이 314px 길어져 다음 안내는 첫 화면 아래다. 날짜 · ‹ 를 누른 3초 안내(아직 오지 않은 날 · 더 이전 달)는 날짜 위 안내 줄 자리에 뜬다. '
             '기록의 입구는 달력 날짜 — 오늘 칸의 + · 「+ 오늘 쓴 돈 적기」 버튼 · 기록이 있으면 「+ 더 적기」. 히어로에 「소비 기록하기」 버튼은 없다(2026-09-22).\n\n'
             '첫 줄: 달력 펼침(7열 월 달력 · 홈의 기본) · ‹ 지난달(더 이전 달은 없어 ‹ 가 흐리고, 누르면 3초 동안 날짜 위 안내 줄에 「더 이전 달은 소비 › 내역에서 볼 수 있어요 · 내역 보기 ›」 — 상태 페이지 CalendarStatusLines) · 360px 좁은 폰(월 달력 그대로) · 달력을 접었을 때(7일 줄) · 기본 카드 전체 스크롤. '
             '둘째 줄: 홈 구성에서 「대표 목적지」를 고른 홈(다음 안내 자리에 68% 고리 · 「대표 목적지 ⌄」로 목적지 고르기 · 비상금 6개월 1,020 / 1,500만원 · 도착까지 7개월 · 매달 70만원 — 또래 · 자산 한눈에 카드는 상태 페이지 PeerStates · HomeGlanceRows) · '
             '첫 실행 뒤 홈(내 데이터 · 빈 히어로 · 펼친 빈 9월 「9월 기록이 아직 없어요」 · 시작 순서 · 카드 3개) · 주식 요약 카드가 있는 홈(계획 · 앱에는 아직 없음) · 저장 뒤 완료 카드 · 월말 예상 기준이 서기 전의 히어로(이력 부족 · 전체 스크롤 — 한도 카드 「9월 5일부터 기록」 · 순자산 한 줄 「9월을 마감하면 다음 달부터 도착 시점을 볼 수 있어요」 · 상환 계획 한 줄까지). '
             '셋째 줄: 소비 목표 조정 열림 · 50%로 저장한 직후(전체 스크롤 · 같은 순간 종 배지 1 → 3 · 다음 안내 「월말엔 소비 목표 50%를 넘어요」 · 한도 카드 180만원 기준 · 탭 막대 위 알림 「소비 목표 50%로 저장했어요 · 한도 180만원」 + 되돌리기 — 알림은 자리를 비워 두지 않고 떠 있어 끝까지 내린 화면처럼 상환 계획 한 줄을 덮는다) · '
             '달이 바뀐 첫 주(10월 2일 · 펼친 10월 달력 — 첫 줄 9/27 ~ 9/30 은 이웃 달이라 흐리게 · 「최근 7일 소비 기록」 제목은 접었을 때만 · 0건 히어로 · 첫 기록 전 한도) · '
             '샘플 모드(32px 띠 · 펼친 달력에도 그 달 합계 줄 없이 샘플 문장 · ✓ · 안 썼어요 표시 없음이라 6일은 이체만 · 마감 전 히어로 — 월말 예상 — · 「6월부터 마감하기 ›」) · '
             '홈 맨 위 카드가 소비 목표를 넘을 때(구현 참고 · 소비 목표 50%로 낮춘 뒤 「월말엔 목표 초과」 · 쓴 돈이 넘으면 「소비 목표보다 3만원 넘음」 · 딱 닿으면 「소비 목표에 딱 닿았어요」 · 셋째 칸 「월말 예상 초과」 빨강 — 앱 하네스).\n\n'
             '2026-09-26: 기본 카드 전체 스크롤은 앱 DEFAULT_HOME_CARDS(다음 안내 · 이번 달 한도 · 순자산 한 줄 · 상환 계획 한 줄 — 대표 목적지 · 또래는 기본이 아님). '
             '저장 뒤 완료 카드 = 「9월 8일 · 편의점 · 카테고리 없음 12,000원 저장 · 오늘 5건 49,000원」 + 「지금 카테고리를 고를까요?」 칩 줄 + 「한 건 더」 · 「되돌리기」(6초 뒤 40px 띠 · 상태 페이지 DoneCardStates). '
             '이력 부족 히어로의 사람은 시안 사용자와 같은 부채(카드 할부 14.5%)가 있어 다음 안내가 카드 할부 · 종 배지 1 — 연 10% 이상 부채가 없으면 「어제 쓴 돈도 적어 볼까요? · 7일 적기 ›」(InsufficientElsewhere ⑤).\n\n'
             '2026-09-26 앱 따라잡기: 머리줄 = 글자 달린 설정 · 코칭 · 알림(종 배지 = 중요 알림 수 1) · 「오늘 포함 23일 남음」. 히어로 머리 「이번 달 소비」 + 「소비 목표 조정」 · 오른쪽 줄은 돈 「소비 목표까지 104만원 남음」 · 「순자산의 1.2% ⓘ」 · 「월급(실수령) 기준 … · 월급 · 부수입 고치기 ›」. '
             '시안 사용자(9월 8일)는 8월 마감값 = 8월 기록 합(1,715,200원)이고 9월에 카테고리 없는 기록이 7건이라 히어로 아래 각주는 두 줄(카테고리 없는 32,000원 · 고정비 이력)이고, '
             '달력의 확인할 내용은 하나라 행이 그 이름 「카테고리 없는 기록 7건 · 카테고리 고르기 ›」(누르면 카테고리 고르기가 바로 열림 · 2026-09-27 앱 하네스로 확인). '
             '마감한 달에 기록을 더한 날의 「8월 합계 고치기 ›」 줄과 「확인할 내용 2개」 목록은 상태 페이지 HeroFootnotes 2번 · 하루 시트 페이지 ReviewListSheet. '
             '10월 2일(달이 바뀐 첫 주)의 행은 「9월 카테고리 없는 기록 7건 · 마감 전에 정리 ›」. 지난달 보기(8월)도 아래로 다음 안내 → 이번 달 한도가 이어진다. '
             '달력 칸 아래에는 늘 범례 줄 「— 기록 없음 · 0 안 썼어요 · ✓ 다 적었어요」. 한도 카드는 어느 단계든 「오늘 포함 하루 45,220원」 + 둘째 줄 「216만원 중 112만원 썼어요」(좁으면 「남은 한도」가 둘째 줄 오른쪽). '
             '다음 안내는 8월 마감 뒤라 「투자 계좌 5,000만원에 매달 47만원이 더 필요해요 · 목적지 보기 ›」. 같은 값은 모든 장에서 같다.\n\n'
             '── 아래 줄은 다크입니다. darken.py가 라이트에서 만든 토큰 매핑 사본이고 레이아웃은 1px도 다르지 않습니다.'),
    'daysheet': ('note-daysheet', 640,
                 '하루 시트 — 날짜 칸을 누르면 홈 위에 뜨는 빠른 기록. 키보드가 열린 상태가 기본(오늘 · 기록 없는 날), 기록 있는 과거 날은 목록 우선, 수정 모드, 키보드 내린 모습, 소비 0건인 날(오늘은 안 썼어요), 360 × 640.\n\n'
                 '기록 없는 어제(「9월 7일은 안 썼어요」) · 지운 뒤(시트 안 「지웠어요 · 택시 45,000원 · 되돌리기」 — 시트 뒤 아래 알림 없음) · 수정 중 날짜 옮기기(「저장하면 9월 3일 → 9월 2일로 옮겨요」).\n\n'
                 '카테고리 고르기 시트(카테고리 없는 기록 7건 · 32,000원 · 최근 기록부터 · 메모 없는 기록은 한 건씩 · 줄의 「카테고리 고르기 ›」를 누르면 그 아래 전체 고르기) · 확인할 내용 목록 · 반복 기록 미리 채움(휴대폰 요금 · 매월 25일 · 5.5만원 — 금액 쓰는 법대로 · 2026-09-27 결정 · 앱 b574373 도 5.5만원) · 하루 시트에서 넘어온 기록 추가(구현 참고). '
                 '이체 행의 ›는 자세한 「기록 수정」 창을 연다 — 기록 종류 · 날짜 · 금액 · 메모가 채워지고, 연결 계좌의 잔액을 이미 확정한 기록(9월 6일 ETF 자동이체)이면 계좌 칸 대신 「연결 계좌의 잔액을 직접 확정한 기록이에요 …」 한 줄. 저장하면 홈에 「고쳤어요」.\n\n'
                 '2026-09-26 앱 구조에 맞춤: 칸 이름은 칸 위(「금액」 · 「메모」 · 빈 메모 「예: 팀 점심」), 「카테고리」 + 「나중에 고르기」(고르지 않았으면 눌린 알약), 최근 기록 칩은 앱 recentEntries 그대로(「카테고리 없음」), '
                 '「다 적었어요」 · 「안 썼어요」 아래 효과 줄, 수정 모드는 제목에 ‹ › 없이 「날짜」 칸. 9월 3일 목록은 기록 순서대로 택시 · 점심 · 간식(내역의 그 날 묶음과 같다).\n\n'
                 '시트 위 어두운 배경의 안내(「배경을 눌러 닫기 · 앱이 다시 시작되면 저장하지 않은 내용은 사라져요」 · 카테고리 고르기와 확인할 내용은 「배경을 눌러 닫기」)는 시트 윗변 바로 위(아래 12)에 붙고, 들어갈 자리가 있을 때만 보인다 — '
                 '시트가 화면 끝까지 올라오면(윗변 30 · 키보드를 내린 오늘 시트 · 360 × 640 · 키보드가 열린 모습) 안내가 없다. 키보드가 열리면 앱 창이 키보드 위로 줄어(안드로이드 에뮬레이터 확인) 시트는 30 ~ 키보드 윗변이고, '
                 '「저장」(수정 모드는 「저장」 · 「삭제」)은 본문 밖 바닥 띠에 붙는다 — 창 높이가 700 아래인 360 × 640 도 같다. 이체 줄은 메모 아래에 「소비율 제외」(메모는 낱말 단위로 두 줄까지 · 줄은 내용만큼 높아진다).\n\n'
                 '규칙은 plan/v5-calendar.md §4 · §5. 계산은 naviMetrics 한 곳, 초안은 메모리만, 되돌리기는 대상 지정.\n\n── 아래 줄은 다크입니다.'),
    'assets-spending': ('note-assets-spending', 640,
                        '자산 · 소비 탭 — 자산 구성 · 부채 · 상환 계획 · 소비 이번 달(계획선 그래프) · 내역(카테고리 없음 칩 · 날짜별 합계) · 한도 · 지난 달 월 요약 세 가지(마감함 · 마감 전 · 마감 뒤 기록이 바뀜) · 8월 첫 마감(카테고리 없음 안내).\n\n'
                        '지난 달 월 요약은 맨 위 월 마감 카드가 상태를 말한다 — 마감함 「마감값 보기·고치기 ›」, 마감 전 「8월 마감하기」 + 마감할 달 목록, 마감 뒤 바뀜 「8월 합계 고치기 ›」(한 번 묻고 합계만 고침 · 상태 장 Confirmations G). '
                        '이미 마감한 달을 「마감값 보기·고치기 ›」로 다시 열면 같은 마감 창이 저장한 값으로 열리고, 꼬리표 없이 맨 위에 「⚠ 이미 9월 2일에 마감한 달이에요. 다시 저장하면 전에 저장한 값을 덮어써요.」가 붙는다.\n\n'
                        '잔액 확인일이 없거나 35일 넘은 자산이 있으면 자산 구성 머리 아래 주황 띠 「잔액 확인이 필요한 자산 {n}개 · 한 번에 확인 ›」가 붙고, 그 줄마다 「확인 필요」 칩과 「… · 마지막 확인 {M월 D일}」/「확인 기록 없음」이 보인다 — 첫 줄 둘째 장 AssetsStale(ETF 계좌 7월 30일 · 청약저축 확인 기록 없음 · 같은 날 알림은 모달 페이지 AlertsPanelInfo). 띠를 누르면 모달 페이지의 「잔액 한 번에 확인」. 시안 사용자는 9월 1일에 다 확인해 9월 8일엔 띠가 없다.\n\n'
                        '자산 › 상환 계획은 읽기 전용 요약(저장된 계획 · 다 갚는 달 · 갚는 순서)이고, 상환 방식과 월 추가 상환액은 「상환 계획 바꾸기 ›」 → 미래 › 상환 계획에서만 바꾼다. '
                        '탭 장은 본문을 다 보여 주는 높이로 그렸다(앱은 스크롤 · 지난 달 월 요약 셋도 카테고리 카드 · 소비 추이·절감 기회까지 · 내역만 ⋯ 메뉴를 연 첫 화면 844). 한도가 넘은 달의 한도 탭은 상태 페이지 LimitCardCases.\n\n'
                        '내역은 개인 모드 시안 사용자(9월 1일 고정비 넷 · 6일 ETF 이체가 생활비 통장과 연결 · 반복 기록 매달 6일 · 25일 · 꺼 둠)이라 목록 위에 「매달 나가는 돈으로 등록할까요?」 제안 줄이 없다 — 그 줄(「보험료 120,000원이 지난달에도 있었어요 · 매달 나가는 돈으로 등록할까요?」)은 상태 · 구현 참고 페이지 DoneCardStates ④, 누른 뒤 열리는 미리 채운 반복 기록 창은 하루 시트 페이지 RecurringPrefill. '
                        '한도의 기타 줄 부줄 「카테고리 없음 7건 32,000원」은 앱처럼 이름 칸 안 「기타」 아래 두 줄(막대 왼쪽). 한도 탭의 기타 막대는 판정 금액이라 카테고리 없는 32,000원을 뺀 28,000원 ÷ 10만원 = 28%(소비 탭 막대는 쓴 돈 그대로). 내역의 ⋯ 메뉴는 행 아래 4px에 열린다.\n\n'
                        '화면당 display 숫자는 하나(자산 = 순자산 · 소비 = 월급 대비 지금까지 쓴 돈 31.1% — 계획 대비 속도는 그 아래 그래프 · 2026-09-24). 미입력은 회색 —. 가정은 보라 점선 + 「저장되지 않는 가정」.\n\n── 아래 줄은 다크입니다.'),
    'dest-future': ('note-dest-future', 640,
                    '목적지 · 미래 — 첫 줄은 지금 앱의 5탭(목적지 · 새 목적지 설계 · 미래 자산 경로 · 상환 계획). '
                    '둘째 줄은 탭을 합친 뒤(v4 2단계 · plan/v4-stocks.md §4): 목적지 + 미래 → 「목적지」 한 탭(세그먼트 내 목적지 · 자산 경로 · 상환 계획), 주식을 끄면 4탭 홈.\n\n'
                    '상환 계획(Payoff)은 저장된 계획(월 추가 15만원 · 고금리 우선 · 초록 「저장된 계획」). 슬라이더나 방식을 바꾼 초안(보라 점선 · 가정 종료 · 상환 계획 저장) · 다 갚지 못함 · 최소 상환만은 상태 페이지 PayoffStates, '
                    '절감 가정 0 원 위(보라 경로)는 FutureStates. 자산 경로는 기본 상태(10년 · 보통 · 절감 0원 — 절감 카드는 보통 카드 · 실선 · 배지 없음, 0 위로 움직일 때만 보라 점선 + 「저장되지 않는 가정」 · 2026-09-27 결정)이고, 투자 환경 칩은 새로 모을 돈의 수익률(조심스럽게 · 보통 · 좋을 때)이다. '
                    '셋째 줄은 참고 장 둘 — 목적지 상태 7종(매달 모으는 돈 110만원 가정 · 비상금 한 줄 펼침 · 도착한 목적지 · 목표일 없음 · 도착하기 어려움 · 부채 상환이 목표일보다 늦음 · 설계 저장 미리 보기의 빨간 줄)과 새 목적지 설계 상태 2종(처음 · 다른 금액 30만원 가정).\n\n'
                    '합친 탭의 목록 끝 버튼은 앱과 같은 「+ 목적지 추가」다(2026-09-27 결정 — 새 목적지 설계는 추가 창과 같은 길). 순자산 2억원 목적지의 목표일은 2058-10-08 그대로(모두 도착하려면 146만원 · 결정). 시뮬레이션 값은 calc/crosscheck.py 확정값(총이자 1,734만원 · 다 갚는 달 2036년 5월 — 앱 달 규칙).\n\n── 아래 줄은 다크입니다.'),
    'first-run': ('note-first-run', 640,
                  '첫 실행 — 소개 3장(현재 위치 · 항로 · 목적지 · 한 장에 한 문장 · 건너뛰기 → 홈 구성) → 홈 구성(「다음」 · 건너뛰기 → 시작 방법 고르기) → 시작 방법 고르기(‹ 뒤로 = 홈 구성 · 내 데이터로 시작 / 샘플로 둘러보기) → 홈. '
                  '점검의 「홈 구성 단계 없앰」은 사용자 요청으로 따르지 않았다 — HomeSetup · HomeSetupStocksOn 과 다크 짝은 남는다.\n\n'
                  '홈 구성: 고정 행 「이번 달 소비」 · 「이번 달 소비 기록」(끌 수 없음), 아래 카드는 4개까지 · 행마다 아이콘과 한 줄 설명(두 줄까지). 처음 체크 = 다음 안내 · 이번 달 한도 · 순자산 한 줄(부채 카드는 미리 체크하지 않음 · 3 / 4). '
                  '처음 체크를 그대로 두고 샘플을 고르면 샘플 홈은 기본 4개(상환 계획 한 줄 포함 · chooseSample). 4 / 4 이면 나머지 행이 흐려지고, 누르면 3초 동안 「4개까지예요 · 하나를 빼고 골라 주세요」. '
                  '「주식 화면이 나오면 알려 드릴까요?」는 settings.features.stocks 만 저장하고 화면은 그대로다 — 주식 요약 행은 없다(주식 화면이 나오면 앱 안에서 한 번 알림 · plan v4 §9). '
                  '이 화면은 처음 설치해 처음 실행할 때만 뜨고, 그 뒤엔 설정 › 홈 구성(닫기 · 저장 · 안내 줄 없음)으로만 바꾼다. '
                  '카드를 하나도 고르지 않으면(0 / 4) 목록 아래에 「이번 달 소비와 소비 기록 달력만 홈에 보여요.」 한 줄이 붙는다(home-layout-editor · 그림 없음).\n\n'
                  '흐름의 끝 장: 처음 설치에서 「내 데이터로 시작」 = HomeConfigured(홈 페이지) + 홈 안내 3단계 「시작 순서」 TourHomeChecklist(첫 실행 안내 페이지) · '
                  '「샘플로 둘러보기」 = HomeSampleMode(홈 페이지) + TourHomeSample1(흐려진 샘플 띠 아래의 홈 안내 · 2 · 3단계도 같은 띠 아래 · 첫 실행 안내 페이지) · 샘플에서 「내 데이터로 시작 ›」 = StorageStates D 확인 창(상태 페이지) → SalarySheet(모달 페이지).\n\n'
                  '샘플로 시작하면 저장 안내 없이 탭마다 맨 위 띠 「샘플 데이터로 둘러보는 중 · 내 데이터로 시작 ›」뿐. 처음 설치에서 「내 데이터로 시작」 = 홈 + 홈 안내, 샘플에서 누르면 파란 확인 창 → 월급 입력 시트(상태 페이지 StorageStates D). '
                  '저장 문구는 폰 「이 폰에만」/「이 기기에 암호화해」, 웹 「이 브라우저에만」(소개 1 자물쇠 줄 · 시작 방법 고르기 · 설정 › 데이터). '
                  '시작 방법 고르기의 웹 문구(앱 DATA_CHOICE_COPY.web 그대로): 설명 「NAVI는 입력한 자산 · 소비 · 목적지를 이 브라우저에만 저장해요. 샘플은 기능을 둘러보는 가상 데이터예요.」 · '
                  '아래 저장 줄 「이 브라우저에만 저장돼요. 브라우저 데이터를 지우면 기록도 사라질 수 있으니 설정에서 백업 파일을 내려받아 주세요.」(폰 앱은 DATA_CHOICE_COPY.native 그대로 「앱을 삭제하거나 앱 데이터를 지우면 기록도 사라져요. 기기를 바꾸기 전에 설정에서 백업 파일을 저장해 주세요.」 — Onboarding 장의 줄).\n\n'
                  '설정 › 홈 구성(HomeLayoutEdit)은 화면을 꽉 채운 페이지가 아니라 가운데 뜬 창(390 × 820 · 위 12)이다 — 위아래 12px 틈으로 흐린 홈이 비치고, 첫 화면에서는 맨 아래 「주식 화면이 나오면 알려 드릴까요?」 카드가 저장 띠에 반쯤 가려 스크롤해야 다 보인다(HomeSetup 과 같다).\n\n'
                  '저장은 settings.homeLayout · settings.onboarding · settings.features(보호 파일 · 백업 형식 불변).\n\n── 아래 줄은 다크입니다.'),
    'tour': ('note-tour', 640,
             '첫 실행 안내 — 화면에 처음 들어가면 그 화면의 안내가 1단계부터 저절로 뜹니다(2026-09-22 사용자 요청 · 유지). 다섯 탭(홈 · 자산 · 소비 · 목적지 · 미래)과 탭 안의 세그먼트 화면 여섯(부채 · 자산 › 상환 계획 · 내역 · 한도 · 새 목적지 설계 · 미래 › 상환 계획) — 11화면 × 3단계 = 33장. '
             '줄 순서 = 탭 다섯 → 세그먼트 여섯 → 마지막 줄(처음 시작한 빈 홈의 3단계 「시작 순서」 · 제목 옆 ?로 다시 연 안내 · 규칙 참고 장 · 샘플로 둘러보기로 시작한 홈의 1단계).\n\n'
             'TourHome1–3 은 내 데이터 홈을 설정 › 도움말 「처음 안내 다시 보기」로 다시 본 모습이다(처음 설치의 「내 데이터로 시작」은 빈 홈이라 TourHomeChecklist, 샘플에서 「내 데이터로 시작」하면 샘플에서 본 안내 상태를 그대로 이어받아 홈 안내가 다시 뜨지 않는다). 「샘플로 둘러보기」로 시작하면 같은 카드가 흐려진 샘플 띠 「샘플 데이터로 둘러보는 중 · 내 데이터로 시작 ›」 아래에서 뜨고 '
             '머리줄 · 히어로가 띠 높이(32)만큼 아래다 — 1단계를 TourHomeSample1 로 그렸고(바탕 HomeSampleMode), 다른 탭의 샘플 모드 안내도 같은 띠 아래다(SampleModeTabs).\n\n'
             '2026-09-30 펼친 달력(홈의 기본): 홈 2 의 대상인 달력 카드가 557px 라 카드와 한 화면에 들지 않아 위 20 으로 스크롤한 뒤 compact(카드가 달력 아래쪽에 겹침 · 꼬리 없음) · 홈 3 은 그 스크롤에서 카드가 위. '
             '처음 시작한 빈 홈의 3단계는 스크롤 662 · 샘플 홈 2 · 3 은 스크롤 495 에서 아래 · 위(gen_tour 표를 다시 잼).\n\n'
             '문구 · 단계 · 버튼은 앱(v5-stage1 a724aac · lib/navi-tour.ts) 그대로. 카드 = 알약 「처음 안내」(?로 다시 열면 「화면 안내」) + 「{화면} n / N」 · 제목 16 / 700 · 본문 13 / 1.55 · 홈 3 / 3 만 각주 한 줄 · '
             '버튼 줄 = 왼쪽 「건너뛰기」(이 화면만) · 「안내 모두 끄기」(11화면 모두) + 오른쪽 「다음」/「알겠어요」 40px.\n\n'
             '막 · 강조 · 카드 자리는 아래 탭 막대 위까지 — 탭 막대는 밝게 남고 누를 수 있다(다른 화면으로 가면 이 화면은 본 것으로). '
             '배치는 앱 placeTourCard(대상 아래 12 → 위 12 → compact · 화면 밖이면 대상을 위로 스크롤 · 스크롤은 다음 단계로 이어짐)를 이 장들의 바탕에 그대로 적용한 결과다. '
             '빈 화면이면 안내도 「?」도 없고 미뤘다가 내용이 생긴 뒤 처음 들어갈 때 뜬다. 홈이 아닌 화면은 제목 옆 「?」로 다시 보고, 홈은 설정 › 도움말 「처음 안내 다시 보기」. '
             '규칙 전체는 참고 장 TourRules.\n\n'
             '다크 = 카드 · 꼬리 #1E2739 · 선 #39455F · 막 rgba(4,7,14,.74)(gen_tour 가 darken 뒤에 덮어씀). 저장은 settings.onboarding.tourSeen 11키. '
             '좌표는 gen_tour.py 의 표(실측)이고 탭 장을 고치면 다시 잽니다. 스크롤 끝 = 마지막 내용 아래가 탭 막대 위 62px(세그먼트 화면) · 38px(홈 — 세그먼트 칸의 아래 24 가 없음).\n\n── 아래 줄은 다크입니다.'),
    'stocks': ('note-stocks', 640,
               '주식 — 앱(v5-stage1 a724aac)에는 주식 화면이 아직 없다. 앱의 주식은 설정 › 홈 구성의 「주식 화면이 나오면 알려 드릴까요? · 지금은 준비 중이에요」 한 줄뿐이라, 이 페이지는 v4 3 ~ 5단계 계획 그림이고 사용성 점검(2026-09-25) 결정에 맞춰 말 · 모양만 고쳤다.\n\n'
               '내 종목(3단계라 세그먼트 없음 · 보유 · 관심 · 직접 입력) · 보유 추가 · 빈 상태(카드 한 장 · 「보유 추가」 하나 · 빈 화면 = 보유 0 이고 관심 0) · 둘러보기(맨 위 띠 · 가드레일 · 성장 / 저평가 / 배당 / 테마) · 성장주 · 배당주 목록 · 종목 상세(내 항로에 넣어보기) · 테마 · 특수한 상황 8가지 · 종목 데이터 새로 받기. '
               '「이 화면에 없는 것」 — 실시간 시세 · 주문 · 호가 · 뉴스 · 커뮤니티 · 시세 알림은 없다(v4 §5-6).\n\n'
               '맨 위 띠 = 「목적지에 나누고 남은 돈」 = 매달 모을 수 있는 돈(월급 + 부수입 − 월말 예상 소비 − 대출상환) − 목적지에 나눠 넣는 돈. 시안 사용자는 90만원을 목적지에 다 나눠 0이라 앱의 0일 때 문장을 쓴다. '
               '제목 옆 「?」(주식 안내 · 12번째 tourSeen 키)는 v4 구현 때 만든다. 추천 · 매수 · 매도라는 말을 쓰지 않는다. 가격 옆에는 항상 기준일(9월 4일 종가). 기준값은 사용자 것(설정 › 주식). 스냅숏 수치는 전부 가상(design/stocks-snapshot.sample.json).\n\n── 아래 줄은 다크입니다.'),
    'modals': ('note-modals', 640,
               '모달 · 설정 — 내 수치(자산 · 부채가 있을 때 — 접힌 칸 「표시 이름 · 순자산 참고선」을 연 모습 · 없을 때) · 월급 입력 · 순자산 대비 소비 · 기록 추가 · 한도 조정 · 자산 추가 · 자산 수정 · '
               '잔액 한 번에 확인(자산 › 자산 구성의 주황 띠 「잔액 확인이 필요한 자산 2개 · 한 번에 확인 ›」를 누른 모습 — 같은 날 AssetsStale 의 ETF 계좌 마지막 확인 7월 30일 · 청약저축 확인 기록 없음 두 줄만 · 2개 중 0개 확인함) · 부채 · '
               '목적지 추가(부채 상환 · 일반 저축의 저장 전 미리 보기 「이대로면 매달 25만원씩 …」 · 「저장하면 이렇게 바뀌어요」) · 반복 기록(이번 달 겹침 확인) · 적립 · 백업 불러오기 · 코칭(있음 · 없음) · '
               '알림(중요 1 · 중요 1 + 참고 1 「자산 잔액을 확인해 주세요」 — 잔액 확인일이 없거나 35일 넘은 자산이 있는 날 · 0건) · 또래 기준 · 설정 › 주식(준비 중) · 설정 › 알림.\n\n'
               '이것들을 여는 설정 시트(내 수치 행 · 화면 · 홈 화면 · 기기 알림 · 도움말 · 데이터 · 닫기)는 첫 실행 페이지의 「설정」 장(SettingsHomeEntry)이다. '
               '순자산 대비 소비 · 설정 › 알림은 앱 기본 Dialog 라 겉이 어두운 막이 아니라 밝게 흐린 화면이고 「배경을 눌러 닫기」가 없다(나머지 시트 · 확인 창은 어두운 막).\n\n'
               '코칭 카드와 알림 줄은 시안 사용자에게 엔진이 내는 목록 그대로다(알림 = 중요 1건 · 머리줄 종 배지 1 · 종 배지는 중요만 센다). 자세한 기록 추가 창은 하루 시트의 「저축·투자로 기록 ›」 · 「대출상환으로 기록 ›」와 지난달보다 이른 달(7월 이전)의 「+ 기록」(그 달 마지막 날로)에서 열리고 — 지난달(8월)의 「+ 기록」은 8월 31일 하루 시트를 연다 —, 계좌에 연결된 기록 · 이체를 고칠 때는 같은 창이 제목 「기록 수정」으로 열린다. '
               '긴 시트는 본문이 다 보이게 폰 한 화면보다 길게 그렸다(앱은 창 안에서 스크롤).\n\n'
               '샘플 모드의 내 수치는 맨 아래에 주황 줄 「샘플 데이터에서 바꾼 값은 샘플에만 남아요. 내 기록을 시작하려면 먼저 「내 데이터로 시작」을 눌러 주세요.」가 붙는다(시안은 내 데이터 모드). '
               '설정 › 알림의 샘플 · 웹 · 권한 변형과, 앱을 안 켜고 있을 때 묻는 「앱을 안 켜고 있을 때 기록 · 마감을 알려 드릴까요?」(나중에 / 켜기)는 참고 장 NotifyCases에 있다.\n\n'
               '단독 행 필드는 solo, 버튼 · 배지는 nowrap. 필수 아님 표기는 「선택 사항」. 만원 칸은 쉼표 + 되읽기 「= 360만원」, 원 칸은 쉼표만. 저장 실패는 실패한 자리 옆에 한 번.\n\n── 아래 줄은 다크입니다.'),
    'desktop': ('note-desktop', 640,
                '데스크톱 1440 — 홈은 히어로 아래 왼쪽 열 첫 자리에 펼친 월 달력(폭 348 · 늘 펼침 · 접기 없음), 그래프는 그 오른쪽, 그 아래 가득 찬 폭 「순자산」 · 「상환 계획」 한 줄 카드, 오른쪽 열은 다음 안내 · 이번 달 한도(앱 기본 카드 DEFAULT_HOME_CARDS). '
                '사이드바는 앱의 5칸(홈 · 자산 9,350만 · 소비 31.1% · 목적지 4 · 미래 「10년 뒤 3.8억」)과 한도 카드 「남은 한도 104만원 · 오늘 포함 23일 · 하루 45,220원」, 아래 「설정」 · 개인 모드 프로필. 머리 오른쪽은 글자 달린 「설정 · 코칭 · 알림」 버튼(종 배지 1). 히어로 각주 두 줄(카테고리 없는 32,000원 · 고정비)과 달력 행 「카테고리 없는 기록 7건 · 카테고리 고르기 ›」는 모바일 홈과 같은 시안 사용자 값. 소비 내역은 왼쪽 기록 목록 + 오른쪽 요약 카드 넷(9월 일반 소비 · 많이 쓴 카테고리 · 반복 기록 · 소비율에서 빠지는 기록).\n\n소비 내역(DesktopLedger)은 2026-09-26 모바일 내역(LedgerV5)과 같은 9월 24건 · 카테고리 없는 기록 7건 · 9/6 ETF 자동이체(반복)로 다시 그렸다 — 결정 3-2A의 v3 샘플 예외를 거둠 · 개인 모드 · 반복 기록 매달 6일 · 25일 · 꺼 둠. 머리 자리는 앱 1440 AppTopbar 그대로(제목 위 49 · 「2026년 9월 기록」 116 · 목록과 옆 카드 166 · 장 높이 976). 연결 칸은 계좌를 고르지 않은 기록이면 회색 —. 연결 칸은 이름을 끝까지 쓴다(「생활비 통장 → ETF 계좌」) — 앱 c6b7de3 에서 칸이 이름 길이만큼 넓어져 1440 에서도 잘리지 않는다(닫음 · 예전 앱은 100px 칸이라 「생활비 통장 → ET…」). 메모 없는 카테고리 없음 기록(9월 5일 3,000원)은 카테고리 칸 「카테고리 없음」 · 제목 칸 「메모 없음」(ink-3 · 400)이다 — 앱 c6b7de3 에서 고쳤고 시안도 같게 그렸다(닫음 · 예전 앱은 두 칸 모두 「카테고리 없음」). 카테고리 없는 줄의 칸은 앱처럼 회색 칸 가운데 굵은 「?」. 반복 기록 금액은 금액 쓰는 법대로 휴대폰 요금 5.5만원(모바일 반복 기록 창과 같게 · 2026-09-27 결정: 목록의 반복 기록 금액은 만 단위 소수 한 자리 · 0 떼기 — 앱 b574373 도 5.5만원). 사이드바 프로필의 저장 문구는 웹 「이 브라우저에만 저장됨」(폰은 「이 폰에만」).\n\n소비 › 이번 달 · 한도의 데스크톱 모습은 따로 그리지 않았다 — 앱은 두 열 격자(이번 달: 왼쪽 속도 카드 · 오른쪽 카테고리별 소비 / 한도: 왼쪽 총한도 · 소비 경고 · 계산 근거 · 오른쪽 카테고리 배분)이고 글자는 모바일 장(Spending · Limits)과 같다. 머리 모양(글자 달린 머리줄 + 「2026년 9월」 + 「기록 추가」)은 소비 내역 장이 보여 준다.\n\n── 아래 줄은 다크입니다.'),
    'states': ('note-states', 640,
               '상태 카탈로그와 구현 참고 장 — 앱 화면이 아니라 설명 장(맨 위 알약 「구현 참고 · 앱 화면이 아닙니다」).\n\n'
               '저장소 로딩 · 복구와 샘플에서 내 데이터로 바꿀 때의 확인 창(샘플 모드 맨 위 띠 「내 데이터로 시작 ›」에서 열림 · 누르면 월급 입력) / 미입력 7종과 화면마다의 빈 카드(F = 히어로 이력 부족 · 가로 설명 장) / 또래 카드 6종 / 목적지 유형 5종 / 모달 오류 · 저장 7종 / 삭제 · 초기화 · 확인 창 7종 / 자산 · 부채 유형 목록 · 새 부채 · 다 갚은 부채 / 달력 칸 읽는 법 / 어느 폭 · 글자 크기에서나 월 달력 / 달력 아래 한 줄이 바뀌는 경우 / 홈 맨 위 카드의 안내 줄 / '
               '저장을 한 번 더 물어보는 경우 / 기록 창의 글이 바뀌는 경우 / 안 쓴 날 표시 / 완료 카드의 경우들 / 월말 예상 기준이 서기 전 홈 밖의 화면 / 미래 · 목적지의 임시 계산 / 한도 카드의 경우들(넘음 · 마지막 날 · 첫 기록 전 · 달 중간 시작 · 카테고리 넘음) / 기타 부줄 / 가져오기 · 백업 안내 / 기기 알림 여섯 가지와 규칙 / '
               '미래 › 상환 계획의 경우들(초안 · 다 갚지 못함 · 최소 상환만 · 모자람 · 같음) / 미래 › 자산 경로의 경우들(절감 가정 · 기록 없음 · 늘어나는 대출 · 초안 · 자세히) / 홈 자산 한눈에 줄 펼침 / 샘플 모드 띠 / 월 최소 상환액을 비운 부채.\n\n'
               '2026-09-26: 상태 줄의 새 경우 — 저녁 링크 「오늘 다 적었어요 ›」 · 이체만 있는 오늘 · 확인할 내용이 하나면 그 이름 · 1 ~ 6일 「최근 7일 소비 기록」 · 흐린 ‹ 3초 안내 · 그 달 0건.\n\n'
               '2026-09-30: 홈의 달력은 펼친 월 달력이 기본 — 날짜 · ‹ 를 누른 3초 안내(아직 오지 않은 날 · 더 이전 달)는 칸 아래가 아니라 날짜 위 안내 줄 자리(CalendarStatusLines · 칸 읽는 법 ⑥). '
               '「표시가 풀렸어요 · 다시 표시」와 샘플 문장은 그대로. 접은 7일 줄 견본은 「접기 ▴」를 누른 뒤의 모습이다. 미입력 A 칸의 첫 홈도 펼친 빈 달력.\n\n'
               '2026-09-27 결정: 미래 절감 카드는 0원이면(소비 기록이 없어 「10년 뒤 —」일 때도) 보통 카드이고, 0 위로 움직일 때만 보라 점선 + 「저장되지 않는 가정」(Future · FutureProvisional · FutureStates · 첫 실행 안내 미래 · 앱 b574373 도 같다). '
               '미래의 바탕 없음 빈 카드는 앱대로 버튼 둘(월급 입력하기 · 자산 추가 — 월급이나 자산 중 하나만 넣어도 경로를 그려서 · EmptyStates).\n\n── 아래 줄은 다크입니다.'),
    'system': ('note-system', 640,
               '디자인 시스템 — 토큰(색 · 타이포 · 간격 · 08절 v5 토큰)과 컴포넌트 24종 + v5 11종의 상태. 값의 최종 기준은 아트보드이고 실측 CSS는 design/SPEC-COMPONENTS.md.\n\n'
               '2026-09-26: 토큰은 앱 app/tokens.v3.css(a724aac)와 맞춤 — 다크 ink-3 #8595AE · line-soft · input-line · border-strong · sky(참고 · 정보) · 첫 실행 안내 층 · 보라는 저장되지 않는 가정뿐 · 넘음 색은 사용자가 정한 선으로만. '
               '컴포넌트 01~07은 앱 모양(폼 저장은 늘 눌림 · 되읽기 · 원 단위 확인 · 아래 알림 → 40px 띠 · 오류는 자리 옆), 08은 v5 장에서 다시 잘라 오고, 09 탭 머리줄(AppTopbar) · 10 판정 줄 · 참고 줄 · 비어 있는 값이 새로 붙었다.\n\n'
               '── 아래 줄은 다크입니다. 토큰 장만 다크가 없습니다(표 자체가 두 테마를 보여 줍니다).'),
}


def note_y(text, w):
    """노트를 첫 줄 아트보드 위에 놓는다 — 노트가 길어져도 아트보드를 덮지 않게 글 길이로 높이를 어림한다(2026-09-26 · 예전 고정 -210).
    캔버스 노트는 13px 안팎 · 줄 높이 1.5 로 그려진다고 보고, 한 줄에 든 글자 수를 폭 ÷ 13 으로 어림한다."""
    import math
    per = max(20, int(w / 13))
    lines = sum(max(1, math.ceil(len(p) / per)) for p in text.split('\n'))
    return -max(210, lines * 20 + 60)


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
    annotations.append({'id': nid, 'page': pid, 'x': 0, 'y': note_y(ntext, nw), 'w': nw, 'text': ntext})

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
