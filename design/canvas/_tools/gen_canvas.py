# -*- coding: utf-8 -*-
import json
import pathlib

OUT = pathlib.Path('/home/user/ajs-bit.github.com/design/canvas')

PHONE = (390, 844)
TALL = {'StorageStates': 1264, 'PeerStates': 1552, 'EmptyStates': 1718, 'Confirmations': 1300,
        'ModalErrors': 2030, 'GoalTypes': 1846}
TALL.update({'Dark' + k: v for k, v in TALL.items()})
WIDE = {'DesktopHome': (1440, 900), 'DesktopLedger': (1440, 900), 'DarkDesktopHome': (1440, 900),
        'DarkDesktopLedger': (1440, 900),
        'Tokens': (1200, 1580), 'Components': (1200, 1440), 'DarkComponents': (1200, 1440)}

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
    'AlertsPanel': '모달 · 알림', 'PeerDialog': '모달 · 또래 기준 등록',
    'StorageStates': '상태 · 저장소 로딩·복구', 'PeerStates': '상태 · 또래 카드 5종',
    'EmptyStates': '상태 · 미입력 5종', 'Confirmations': '상태 · 삭제·초기화 확인',
    'ModalErrors': '상태 · 모달 오류·저장 6종', 'GoalTypes': '상태 · 목적지 유형 5종',
    'SpendingPast': '소비 · 지난 달(마감)', 'GoalContribute': '모달 · 적립액 추가',
    'CoachEmpty': '모달 · 코칭 기록 없음',
    'DesktopHome': '데스크톱 · 홈', 'DesktopLedger': '데스크톱 · 소비 내역',
    'DarkDesktopHome': '데스크톱 · 홈 (다크)', 'DarkDesktopLedger': '데스크톱 · 소비 내역 (다크)',
    'Tokens': '토큰 · 색 · 타이포 · 간격', 'Components': '컴포넌트 · 상태',
    'DarkComponents': '컴포넌트 · 상태 (다크)',
}
TITLES.update({
    'DarkStorageStates': '상태 · 저장소 로딩·복구 (다크)',
    'DarkEmptyStates': '상태 · 미입력 5종 (다크)',
    'DarkPeerStates': '상태 · 또래 카드 5종 (다크)',
    'DarkModalErrors': '상태 · 모달 오류·저장 6종 (다크)',
    'DarkConfirmations': '상태 · 삭제·초기화 확인 (다크)',
    'DarkGoalTypes': '상태 · 목적지 유형 5종 (다크)',
})

PAGES = [
    ('page-1', '모바일 · 화면',
     ['Main', 'HomeScroll', 'Assets', 'Debts', 'Strategy', 'Spending',
      'Ledger', 'Limits', 'SpendingPast', 'Goals', 'GoalDesign', 'Future', 'Payoff', 'Onboarding']),
    ('page-2', '모바일 · 모달',
     ['ProfileDialog', 'TransactionAdd', 'LimitEditor', 'AssetDialog', 'DebtDialog', 'GoalDialog',
      'RecurringDialog', 'GoalContribute', 'MonthlyClose', 'ImportReview', 'CoachPanel', 'CoachEmpty',
      'AlertsPanel', 'PeerDialog']),
    ('page-3', '상태 카탈로그',
     ['StorageStates', 'EmptyStates', 'PeerStates', 'GoalTypes', 'ModalErrors', 'Confirmations']),
    ('page-4', '데스크톱',
     ['DesktopHome', 'DesktopLedger', 'DarkDesktopHome', 'DarkDesktopLedger']),
    ('page-5', '다크 · 화면',
     ['DarkHome', 'DarkHomeScroll', 'DarkAssets', 'DarkDebts', 'DarkStrategy', 'DarkSpending',
      'DarkLedger', 'DarkLimits', 'DarkSpendingPast', 'DarkGoals', 'DarkGoalDesign', 'DarkFuture',
      'DarkPayoff', 'DarkOnboarding']),
    ('page-6', '다크 · 모달',
     ['DarkProfileDialog', 'DarkTransactionAdd', 'DarkLimitEditor', 'DarkAssetDialog', 'DarkDebtDialog',
      'DarkGoalDialog', 'DarkRecurringDialog', 'DarkGoalContribute', 'DarkMonthlyClose', 'DarkImportReview',
      'DarkCoachPanel', 'DarkCoachEmpty', 'DarkAlertsPanel', 'DarkPeerDialog']),
    ('page-7', '다크 · 상태 카탈로그',
     ['DarkStorageStates', 'DarkEmptyStates', 'DarkPeerStates', 'DarkGoalTypes', 'DarkModalErrors',
      'DarkConfirmations']),
    ('page-8', '디자인 시스템', ['Tokens', 'Components', 'DarkComponents']),
]

NOTES = {
    'page-1': ('note-screens', 640,
               '읽는 순서: 결과 → 근거 → 행동\n\n'
               '화면마다 display 크기 숫자는 딱 하나입니다. 홈은 월급 대비 소비율, 자산은 순자산, 소비는 계획 대비 속도, '
               '목적지는 월 배분, 미래는 10년 뒤 순자산.\n\n'
               '그 값을 바꾸는 버튼은 값 바로 옆이나 아래에 놓입니다. 탭 위에 떠 있던 CTA는 모두 없앴습니다.'),
    'page-2': ('note-modals', 640,
               '모달은 헤더 / 스크롤 본문 / 고정 하단 행동 세 층\n\n'
               '모바일은 상단 반경 26의 바텀시트이고 하단 버튼은 항상 보입니다. 추가와 수정은 제목·저장 버튼 문구·삭제 버튼 '
               '유무로만 구분하고 필드 순서는 같습니다.\n\n'
               '한도 조정·월 마감·백업 불러오기처럼 되돌리기 어려운 저장에는 본문과 버튼 사이에 고정 확인 줄을 둡니다.'),
    'page-3': ('note-states', 640,
               '없는 값을 지어내지 않는다\n\n'
               '미입력은 회색 —로만 표시하고 0원·0%·좋은 성과로 바꾸지 않습니다. 급여가 0원이고 부수입만 있는 상태는 '
               '소비율을 —로 두고 총수입 대비 소비를 대안 지표로 제시합니다.\n\n'
               '또래 카드는 5가지 상태 어디에서도 확인되지 않은 평균·백분위·상위 %를 만들지 않습니다.\n\n'
               '모달 오류 6종도 같은 규칙을 씁니다. 오류는 무엇이 잘못됐고 어떻게 고치는지를 같이 말하고, '
               '저장에 실패해도 입력한 값을 지우지 않습니다.'),
    'page-4': ('note-desktop', 640,
               '데스크톱은 넓이를 두 번째 열로 쓴다\n\n'
               '2.2의 데스크톱은 사이드바 224px + 가운데 한 열이라 히어로 카드 안이 텅 비어 보였습니다.\n\n'
               'v3는 본문을 1.6fr / 1fr로 나눕니다. 왼쪽은 주지표와 그래프, 오른쪽은 다음 안내·대표 목적지·또래·한도처럼 '
               '곁눈질로 보는 정보. 사이드바에도 각 탭의 현재 수치를 넣었습니다.'),
    'page-5': ('note-dark-screens', 640,
               '다크는 토큰 매핑만 바뀐다\n\n'
               '표면·잉크·상태색은 라이트와 1:1로 대응하고, 레이아웃·타이포·간격은 완전히 동일합니다.\n\n'
               '브랜드 그라디언트(140° #3556E6 → #7A3FE4)와 카테고리·자산 고정 팔레트는 다크에서도 같은 값입니다. '
               '채운 버튼만 반전됩니다 — 밝은 브랜드색 배경에 어두운 글자.'),
    'page-6': ('note-dark-modals', 640,
               '다크 모달\n\n'
               '시트 배경은 surface(#121A2B), 스크림은 #04070E입니다. 그림자는 더 깊고 불투명하게 바뀝니다.\n\n'
               '보라 가정 배지, 회색 — 미입력, 주황/빨강 경고의 의미는 라이트와 동일하게 유지됩니다.'),
    'page-7': ('note-dark-states', 640,
               '다크에서도 상태 규칙은 같다\n\n'
               '회색 — 미입력, 보라 = 저장되지 않은 가정, 주황 = 개인 목표 초과, 빨강 = 100% 초과. '
               '네 가지 의미는 라이트와 다크에서 완전히 같은 자리에 쓰입니다.\n\n'
               '오류 카드의 빨강만 다크에서 밝기를 올려(#C0342F → #E8635F) 어두운 표면 위에서 읽히게 했습니다.'),
    'page-8': ('note-system', 640,
               '타이포 9단계 · 카테고리 색은 그대로\n\n'
               '2.2에는 17·18·20·21·23·26·32px가 섞여 있었습니다. v3는 display / metric-xl / metric / title / '
               'section / body / label / meta / eyebrow 9단계만 씁니다.\n\n'
               '카테고리·자산 고정 팔레트는 거래와 차트의 정체성이라 2.2 값을 그대로 유지합니다.\n\n'
               '토큰 시트는 01 LIGHT / 02 DARK 두 절로 라이트와 다크 값을 한 장에 나란히 적어 둔 명세라 다크 사본을 따로 두지 않습니다. 컴포넌트 시트는 실제 컴포넌트를 보여 주므로 다크 버전을 함께 둡니다.'),
}

PER_ROW = 6
GAP_X = 80
ROW_GAP = 140

artboards = []
annotations = []

for pid, pname, files in PAGES:
    x = y = 0
    row_h = 0
    col = 0
    for f in files:
        if f in WIDE:
            w, h = WIDE[f]
        else:
            w, h = PHONE[0], TALL.get(f, PHONE[1])
        if col >= PER_ROW or (f in WIDE and col > 0 and x > 0):
            x = 0
            y += row_h + ROW_GAP
            row_h = 0
            col = 0
        artboards.append({'file': f'{f}.dc.html', 'page': pid, 'x': x, 'y': y, 'w': w, 'h': h,
                          'title': TITLES.get(f.replace('Dark', '', 1) if f.startswith('Dark') else f,
                                              TITLES.get(f, f))})
        x += w + GAP_X
        row_h = max(row_h, h)
        col += 1
    nid, nw, ntext = NOTES[pid]
    annotations.append({'id': nid, 'page': pid, 'x': 0, 'y': -210, 'w': nw, 'text': ntext})

# 다크 아트보드 제목에 (다크) 표시
for a in artboards:
    stem = a['file'].replace('.dc.html', '')
    if stem.startswith('Dark') and stem != 'DarkDesktopHome':
        base = 'Main' if stem == 'DarkHome' else stem[4:]
        a['title'] = TITLES.get(base, base) + ' (다크)'

canvas = {
    'pages': [{'id': p, 'name': n} for p, n, _ in PAGES],
    'artboards': artboards,
    'annotations': annotations,
    'launch': {'view': 'canvas', 'page': 'page-1'},
}

(OUT / 'canvas.json').write_text(json.dumps(canvas, ensure_ascii=False, indent=2), encoding='utf-8')

have = {p.name.replace('.dc.html', '') for p in OUT.glob('*.dc.html')}
listed = {a['file'].replace('.dc.html', '') for a in artboards}
print(f'{len(artboards)} artboards across {len(PAGES)} pages')
print('배치 안 된 파일:', sorted(have - listed) or '없음')
print('파일 없는 항목:', sorted(listed - have) or '없음')
