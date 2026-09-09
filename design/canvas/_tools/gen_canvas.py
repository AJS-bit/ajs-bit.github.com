# -*- coding: utf-8 -*-
import json
import pathlib

OUT = pathlib.Path('/home/user/ajs-bit.github.com/design/canvas')

PHONE = (390, 844)
# 프레임 높이는 "실제 웹폰트로 렌더한 자연 높이 + 아래 여백 24px"이다.
# 폴백 폰트로 재면 한글 줄 높이가 짧게 나와 실제보다 작은 값이 나온다. 반드시 IBM Plex Sans KR로 재라.
TALL = {'StorageStates': 1309, 'PeerStates': 1595, 'EmptyStates': 1718, 'Confirmations': 1228,
        'ModalErrors': 2061, 'GoalTypes': 1767}
TALL.update({'Dark' + k: v for k, v in TALL.items()})
WIDE = {'DesktopHome': (1440, 900), 'DesktopLedger': (1440, 900), 'DarkDesktopHome': (1440, 900),
        'DarkDesktopLedger': (1440, 900),
        'Tokens': (1200, 1684), 'Components': (1200, 1471), 'DarkComponents': (1200, 1471)}

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
    'Tokens': '토큰 · 색 · 타이포 · 간격', 'Components': '컴포넌트 · 상태',
}

PAGES = [
    ('page-1', '모바일 · 화면', 6,
     ['Main', 'HomeScroll', 'Assets', 'Debts', 'Strategy', 'Spending',
      'Ledger', 'Limits', 'SpendingPast', 'Goals', 'GoalDesign', 'Future', 'Payoff', 'Onboarding']),
    ('page-2', '모바일 · 모달', 6,
     ['ProfileDialog', 'TransactionAdd', 'LimitEditor', 'AssetDialog', 'DebtDialog', 'GoalDialog',
      'RecurringDialog', 'GoalContribute', 'MonthlyClose', 'ImportReview', 'CoachPanel', 'CoachEmpty',
      'AlertsPanel', 'PeerDialog']),
    ('page-3', '상태 카탈로그', 6,
     ['StorageStates', 'EmptyStates', 'PeerStates', 'GoalTypes', 'ModalErrors', 'Confirmations']),
    ('page-4', '데스크톱', 2, ['DesktopHome', 'DesktopLedger']),
    ('page-5', '디자인 시스템', 2, ['Tokens', 'Components']),
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
               '— 밝은 브랜드색 배경에 어두운 글자.'),
    'page-2': ('note-modals', 640,
               '모달은 헤더 / 스크롤 본문 / 고정 하단 행동 세 층\n\n'
               '제목은 무엇을 하는 창인지, 부제는 무엇이 저장되는지 말합니다. 필수는 라벨 옆 *, 선택은 라벨 옆 회색 "선택"입니다.\n\n'
               '한도 조정·월 마감·백업 불러오기처럼 되돌리기 어려운 저장에는 본문과 버튼 사이에 고정 확인 줄을 둡니다.\n\n'
               '── 아래 줄은 다크입니다. 시트 배경은 surface(#121A2B), 스크림은 #04070E이고 그림자는 더 깊고 '
               '불투명해집니다. 보라 가정 배지, 회색 — 미입력, 주황/빨강 경고의 의미는 라이트와 같습니다.'),
    'page-3': ('note-states', 640,
               '없는 값을 지어내지 않는다\n\n'
               '미입력은 회색 —로만 표시하고 0원·0%·좋은 성과로 바꾸지 않습니다. 급여가 0원이고 부수입만 있는 상태는 '
               '소비율을 —로 두고 총수입 대비 소비를 대안 지표로 제시합니다.\n\n'
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
               '── 아래 줄은 다크입니다.'),
    'page-5': ('note-system', 640,
               '타이포 9단계 · 카테고리 색은 그대로\n\n'
               '2.2에는 17·18·20·21·23·26·32px가 섞여 있었습니다. v3는 display / metric-xl / metric / title / '
               'section / body / label / meta / eyebrow 9단계만 씁니다.\n\n'
               '카테고리·자산 고정 팔레트는 거래와 차트의 정체성이라 2.2 값을 그대로 유지합니다.\n\n'
               '토큰 시트는 01 LIGHT / 02 DARK 두 절과 상태색 카드의 DARK 줄로 두 모드 값을 한 장에 다 적어 둔 '
               '명세라 다크 사본을 따로 두지 않습니다. 컴포넌트 시트는 실제 컴포넌트를 보여 주므로 아래 줄에 다크를 둡니다.'),
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
    'launch': {'view': 'canvas', 'page': 'page-1'},
}

(OUT / 'canvas.json').write_text(json.dumps(canvas, ensure_ascii=False, indent=2), encoding='utf-8')

have = {p.name.replace('.dc.html', '') for p in OUT.glob('*.dc.html')}
listed = {a['file'].replace('.dc.html', '') for a in artboards}
print(f'{len(artboards)} artboards across {len(PAGES)} pages')
print('배치 안 된 파일:', sorted(have - listed) or '없음')
print('파일 없는 항목:', sorted(listed - have) or '없음')
