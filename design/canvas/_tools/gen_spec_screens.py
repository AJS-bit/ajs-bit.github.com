"""화면별 조립 체크리스트(SPEC-SCREENS.md)를 아트보드에서 뽑아 만든다.

각 화면의 블록을 위에서 아래 순서로 나열하므로, 구현하면서 하나씩 지워 나갈 수 있다.
빠뜨린 블록이 바로 보이는 것이 목적이다.
"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from outline import T, role, sd
import re

HERE = pathlib.Path(__file__).resolve().parent
CANVAS = HERE.parent
DESIGN = CANVAS.parent

# 화면이 무엇을 읽히려는 화면인지. 이게 없으면 블록 목록은 그냥 div 목록이다.
INTENT = {
 'Main': '이번 달 소비가 월급의 몇 %인지를 **한 번에** 읽히는 화면. display 숫자는 57.9% 하나뿐이고, 나머지는 전부 그 아래 위계로 내려간다.',
 'HomeScroll': '홈을 아래로 내린 상태. 히어로가 스크롤 밖으로 나가고 목적지·한도·또래 카드가 이어진다. 히어로는 sticky가 아니다.',
 'Assets': '순자산이 주 지표. 스파크라인 + 구성 막대 + 계좌 행 리스트로, 2.2의 가운데 정렬 타일 5개를 대체한다.',
 'Debts': '부채 4건을 금리 순으로 세운다. 금리가 색을 결정한다(14.5%만 빨강). 가중평균 금리 4.44%가 요약값.',
 'Strategy': '고금리 우선 vs 소액 우선 비교. 완제 시점은 같고 총이자만 다르다는 것이 이 화면의 결론.',
 'Spending': '이번 달 소비 속도. 누적 그래프는 오늘까지 실선, 월말까지 점선 예상선으로 오른쪽 빈 공간을 채운다.',
 'Ledger': '거래 내역. 날짜 그룹 헤더 + DataRow 반복. 금액은 전부 오른쪽 정렬 tabular.',
 'Limits': '카테고리별 한도. 진행바가 한도를 넘으면 색이 바뀐다. 조정 버튼은 섹션 제목과 같은 줄에 두지 않는다.',
 'SpendingPast': '지난 달 마감본. 마감된 달은 값이 고정이라 "예상"이 없다. 편집 불가 표시가 핵심.',
 'Goals': '목적지 목록. GoalRing + 도착 예상 시점. 배분이 모자라면 얼마가 부족한지 숫자로 말한다.',
 'GoalDesign': '새 목적지를 만들 때 목표액·기간에서 월 납입액이 역산되는 화면.',
 'Future': '10년 뒤 순자산 경로. 보수/기준/낙관 밴드와 마일스톤 도달 시점.',
 'Payoff': '상환 계획. 전략별 완제 시점·총이자 비교와 완제 순서.',
 'Onboarding': '첫 실행. 아직 아무 데이터가 없는 상태에서 무엇부터 넣으면 되는지만 말한다.',
 'ProfileDialog': '실수령 급여·총수입 등 기준 수치 입력. 이 값이 홈의 분모다.',
 'TransactionAdd': '거래 추가. 잔액 반영 토글과 계좌 연결이 여기 있다.',
 'LimitEditor': '한도 조정. 합계가 예산을 넘는지 즉시 보여준다.',
 'AssetDialog': '자산 추가. 이름과 평가액만 필수.',
 'DebtDialog': '부채 수정. 금리·최소상환액이 상환 시뮬레이션의 입력이다.',
 'GoalDialog': '목적지 추가. 유형에 따라 입력 필드가 바뀐다.',
 'RecurringDialog': '반복 거래. 기존 반복 규칙 형식을 바꾸지 않는다.',
 'GoalContribute': '목적지에 적립액을 더한다. 시뮬레이션이 아니라 기록이다.',
 'MonthlyClose': '월 마감. 마감하면 그 달 값이 고정된다는 것을 분명히 말한다.',
 'ImportReview': '백업 불러오기 검토. 무엇이 덮어써지는지 건수로 보여준 뒤 확인받는다.',
 'CoachPanel': '코칭 기록. 저장된 조언이 시간 순으로 쌓인다.',
 'CoachEmpty': '코칭 기록이 없을 때. 0건을 성과처럼 보이게 하지 않는다.',
 'AlertsPanel': '알림 목록. 읽음/안읽음이 구분된다.',
 'PeerDialog': '또래 기준 등록. 나이대는 초반(0~3)/중반(4~6)/후반(7~9)으로만 나눈다.',
 'StorageStates': '저장소 로딩·복구 상태 모음. 로딩과 "데이터 없음"은 다른 화면이다.',
 'EmptyStates': '미입력 5종. **미입력을 0원이나 좋은 성과로 표시하지 않는다**는 규칙이 그림으로 있는 시트.',
 'PeerStates': '또래 카드 5종. 통계가 없으면 없다고 말한다. 평균·백분위·상위 %를 지어내지 않는다.',
 'GoalTypes': '목적지 유형 5종의 카드 변형.',
 'ModalErrors': '모달 오류·저장 6종. 각 오류의 문구와 위치가 정해져 있다.',
 'Confirmations': '삭제·초기화 확인 4종. 되돌릴 수 없는 동작은 무엇이 사라지는지 건수로 말한다.',
 'DesktopHome': '데스크톱 홈. 사이드바 + 2열. 모바일 카드를 그냥 늘리지 않고 가로를 실제로 쓴다.',
 'DesktopLedger': '데스크톱 내역. 표 형태. 소비율 제외 행은 배경으로 구분한다.',
 'Tokens': '토큰 시트. 구현이 아니라 참조용.',
 'Components': '컴포넌트·상태 시트. SPEC-COMPONENTS.md의 그림판.',
}


def frame_blocks(path):
    t = path.read_text()
    body = re.search(r'</helmet>(.*?)</x-dc>', t, re.S).group(1)
    p = T(); p.feed(body)
    root = p.root.kids[0]           # 화면 프레임
    rows = []

    def first_text(n, depth=0):
        if n.text:
            return n.text
        if depth > 4:
            return ''
        for k in n.kids:
            s = first_text(k, depth + 1)
            if s:
                return s
        return ''

    def emit(n, ind):
        for k in n.kids:
            if k.tag in ('svg', 'script', 'style'):
                continue
            r = role(k) or ''
            txt = first_text(k)[:52]
            if not r and not txt:
                continue
            rows.append((ind, r, txt, sd(k.style)))

    emit(root, 0)
    # 본문(flex:1) 안쪽 한 겹 더
    out = []
    for k in root.kids:
        if 'flex: 1' in k.style or 'flex:1' in k.style:
            sub = []
            for c in k.kids:
                if c.tag in ('svg', 'script', 'style'):
                    continue
                sub.append(c)
            out = sub
    return rows, out, root


def render(name):
    path = CANVAS / f'{name}.dc.html'
    t = path.read_text()
    body = re.search(r'</helmet>(.*?)</x-dc>', t, re.S).group(1)
    p = T(); p.feed(body)
    root = p.root.kids[0]

    def first_text(n, d=0):
        if n.text:
            return n.text
        if d > 5:
            return ''
        for k in n.kids:
            s = first_text(k, d + 1)
            if s:
                return s
        return ''

    lines = []

    def walk(n, depth):
        for k in n.kids:
            if k.tag in ('svg', 'script', 'style'):
                continue
            r = role(k)
            txt = first_text(k)[:52].replace('|', '\\|')
            label = r if r else k.tag
            if depth == 0 or (depth == 1 and (r or txt)):
                lines.append((depth, label, txt, sd(k.style)))
                if depth == 0:
                    walk(k, 1)
    # 프레임 바로 아래 = 1단계, 본문 안 = 2단계
    def descend(n, depth):
        for c in n.kids:
            if c.tag in ('svg', 'script', 'style'):
                continue
            lines.append((depth, role(c) or c.tag, first_text(c)[:52].replace('|', '\\|'), sd(c.style)))
            # 스크롤 영역·시트처럼 "안에 진짜 내용이 있는" 껍데기는 한 겹 더 편다
            if depth < 2 and 'flex: 1' in c.style:
                descend(c, depth + 1)

    descend(root, 0)
    return lines


def main():
    man = json.loads((DESIGN / 'screens.json').read_text())['artboards']
    light = [a for a in man['artboards'] if a['theme'] == 'light'] if isinstance(man, dict) else \
            [a for a in man if a['theme'] == 'light']
    buf = ['# 화면별 조립 체크리스트', '',
           '각 화면을 **위에서 아래 순서로** 조립하세요. 블록 하나를 만들 때마다 지워 나가면',
           '빠뜨린 것이 바로 보입니다. 굵은 이름은 `SPEC-COMPONENTS.md`의 컴포넌트입니다.', '',
           '값은 요약입니다. **정확한 값은 항상 `canvas/<이름>.dc.html`이 기준**이고,',
           '더 자세한 구조는 `spec/<이름>.outline.md`에 있습니다.', '',
           '다크 화면은 별도 항목이 없습니다. 같은 구조에 `canvas/_tools/darken.py`의 색 대응만 적용한 것입니다.', '',
           '---', '']
    for a in light:
        n = a['name']
        buf.append(f"## {n} — {a['title']}")
        buf.append('')
        buf.append(f"`canvas/{a['file']}` · {a['w']}×{a['h']} · 원본 `{a['source']}` · 렌더 `preview/{n}.png`")
        buf.append('')
        if n in INTENT:
            buf.append(f"> {INTENT[n]}")
            buf.append('')
        for depth, label, txt, digest in render(n):
            pad = '  ' * depth
            head = f"{pad}- [ ] **{label}**" if label and not label.startswith('text ') else f"{pad}- [ ] {label}"
            if txt:
                head += f" — “{txt}”"
            buf.append(head)
            if digest:
                buf.append(f"{pad}      `{digest}`")
        buf.append('')
    (DESIGN / 'SPEC-SCREENS.md').write_text('\n'.join(buf) + '\n')
    print(len(light), 'screens ->', (DESIGN / 'SPEC-SCREENS.md').stat().st_size, 'bytes')


if __name__ == '__main__':
    main()
