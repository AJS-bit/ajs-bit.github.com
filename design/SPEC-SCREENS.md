# 화면별 조립 체크리스트

각 화면을 **위에서 아래 순서로** 조립하세요. 블록 하나를 만들 때마다 지워 나가면
빠뜨린 것이 바로 보입니다. 굵은 이름은 `SPEC-COMPONENTS.md`의 컴포넌트입니다.

값은 요약입니다. **정확한 값은 항상 `canvas/<이름>.dc.html`이 기준**이고,
더 자세한 구조는 `spec/<이름>.outline.md`에 있습니다.

다크 화면은 별도 항목이 없습니다. 같은 구조에 `canvas/_tools/darken.py`의 색 대응만 적용한 것입니다.

---

## Main — 홈 · 오늘의 내비게이션

`canvas/Main.dc.html` · 390×844 · 원본 `app/page.tsx` · 렌더 `preview/Main.png`

> 이번 달 소비가 월급의 몇 %인지를 **한 번에** 읽히는 화면. display 숫자는 57.9% 하나뿐이고, 나머지는 전부 그 아래 위계로 내려간다.

- [ ] **SampleBanner** — “샘플 데이터로 둘러보는 중”
      `display:flex align-items:center justify-content:space-between gap:8px height:32px padding:0 14px background:#E9EDFD`
- [ ] **Header** — “NAVI”
      `display:flex flex-direction:column gap:6px padding:12px 16px 10px`
- [ ] **본문(스크롤 영역)** — “현재 위치”
      `flex:1 min-height:0 display:flex flex-direction:column gap:9px padding:0 14px`
  - [ ] **HeroCard** — “현재 위치”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **TurnCard** — “다음 안내”
        `display:flex gap:12px background:#FFFFFF border:1px solid #E3E8F1 border-left:3px solid #DE8A2A border-radius:18px padding:13px 14px`
  - [ ] **Card(18)** — “68%”
        `display:flex align-items:center gap:12px background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px`
  - [ ] **Card(18)** — “이번 달 한도”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`

## HomeScroll — 홈 · 아래로 스크롤

`canvas/HomeScroll.dc.html` · 390×844 · 원본 `app/page.tsx` · 렌더 `preview/HomeScroll.png`

> 홈을 아래로 내린 상태. 히어로가 스크롤 밖으로 나가고 목적지·한도·또래 카드가 이어진다. 히어로는 sticky가 아니다.

- [ ] **본문(스크롤 영역)** — “저장되지 않는 가정”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px 0`
  - [ ] **div**
        `height:20px background:#FFFFFF border:1px solid #E3E8F1 border-top:none border-radius:0 0 18px 18px opacity:.55`
  - [ ] **Card(18)** — “저장되지 않는 가정”
        `background:#FFFFFF border:1px dashed #B79BFF border-radius:18px padding:14px`
  - [ ] **Card(18)** — “또래와 내 페이스”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
  - [ ] **Card(18)** — “순자산 대비 소비”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:4px 14px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`

## Assets — 자산 · 구성

`canvas/Assets.dc.html` · 390×844 · 원본 `components/navi/asset-view.tsx` · 렌더 `preview/Assets.png`

> 순자산이 주 지표. 스파크라인 + 구성 막대 + 계좌 행 리스트로, 2.2의 가운데 정렬 타일 5개를 대체한다.

- [ ] **div** — “자산”
      `display:flex flex-direction:column gap:10px padding:14px 16px 12px`
- [ ] **본문(스크롤 영역)** — “순자산”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **HeroCard** — “순자산”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **div** — “현금성 비상금”
        `display:flex gap:8px`
  - [ ] **Card(18)** — “자산 구성”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`

## Debts — 자산 · 부채

`canvas/Debts.dc.html` · 390×844 · 원본 `components/navi/asset-view.tsx` · 렌더 `preview/Debts.png`

> 부채 4건을 금리 순으로 세운다. 금리가 색을 결정한다(14.5%만 빨강). 가중평균 금리 4.44%가 요약값.

- [ ] **div** — “자산”
      `display:flex flex-direction:column gap:10px padding:14px 16px 12px`
- [ ] **본문(스크롤 영역)** — “총부채”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **HeroCard** — “총부채”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **TurnCard** — “고금리 경고”
        `display:flex gap:12px background:#FFFFFF border:1px solid #E3E8F1 border-left:3px solid #DE8A2A border-radius:18px padding:13px 14px`
  - [ ] **Card(18)** — “부채 4건”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
  - [ ] **Card(18)** — “이번 달 상환 예정”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 14px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`

## Strategy — 자산 · 상환 전략

`canvas/Strategy.dc.html` · 390×844 · 원본 `components/navi/asset-view.tsx` · 렌더 `preview/Strategy.png`

> 고금리 우선 vs 소액 우선 비교. 완제 시점은 같고 총이자만 다르다는 것이 이 화면의 결론.

- [ ] **div** — “자산”
      `display:flex flex-direction:column gap:10px padding:14px 16px 12px`
- [ ] **본문(스크롤 영역)** — “상환 방식”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **HeroCard** — “상환 방식”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **Card(18)** — “예상 완제”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
  - [ ] **Card(18)** — “완제 순서”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`

## Spending — 소비 · 이번 달

`canvas/Spending.dc.html` · 390×844 · 원본 `components/navi/spending-view.tsx` · 렌더 `preview/Spending.png`

> 이번 달 소비 속도. 누적 그래프는 오늘까지 실선, 월말까지 점선 예상선으로 오른쪽 빈 공간을 채운다.

- [ ] **div** — “소비”
      `display:flex flex-direction:column gap:10px padding:14px 16px 12px`
- [ ] **본문(스크롤 영역)** — “57.9”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **HeroCard** — “57.9”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px 14px 14px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **Card(18)** — “카테고리별 소비”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`

## Ledger — 소비 · 내역

`canvas/Ledger.dc.html` · 390×844 · 원본 `components/navi/spending-view.tsx` · 렌더 `preview/Ledger.png`

> 거래 내역. 날짜 그룹 헤더 + DataRow 반복. 금액은 전부 오른쪽 정렬 tabular.

- [ ] **div** — “소비”
      `display:flex flex-direction:column gap:10px padding:14px 16px 12px`
- [ ] **본문(스크롤 영역)** — “메모·카테고리 검색”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **Card(18)** — “메모·카테고리 검색”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
  - [ ] **Card(18)** — “9월 8일”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:4px 14px 10px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`

## Limits — 소비 · 한도

`canvas/Limits.dc.html` · 390×844 · 원본 `components/navi/spending-view.tsx` · 렌더 `preview/Limits.png`

> 카테고리별 한도. 진행바가 한도를 넘으면 색이 바뀐다. 조정 버튼은 섹션 제목과 같은 줄에 두지 않는다.

- [ ] **div** — “소비”
      `display:flex flex-direction:column gap:10px padding:14px 16px 12px`
- [ ] **본문(스크롤 영역)** — “이번 달 총한도”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **HeroCard** — “이번 달 총한도”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **Card(18)** — “카테고리 배분”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
  - [ ] **div** — “이 한도는 어떻게 계산했나요?”
        `display:flex align-items:center justify-content:space-between gap:8px background:#FFFFFF border:1px solid #E3E8F1 border-radius:14px padding:0 14px height:50px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`

## SpendingPast — 소비 · 지난 달(마감)

`canvas/SpendingPast.dc.html` · 390×844 · 원본 `components/navi/spending-view.tsx` · 렌더 `preview/SpendingPast.png`

> 지난 달 마감본. 마감된 달은 값이 고정이라 "예상"이 없다. 편집 불가 표시가 핵심.

- [ ] **div** — “소비”
      `display:flex flex-direction:column gap:10px padding:14px 16px 12px`
- [ ] **div** — “마감한 달이라 · 기록은 내역에서 수정”
      `display:flex align-items:center gap:7px padding:0 16px 10px`
- [ ] **본문(스크롤 영역)** — “마감한 달”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **HeroCard** — “마감한 달”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **Card(18)** — “31일 동안 이렇게 썼어요”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
  - [ ] **Card(18)** — “카테고리”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
- [ ] **div**
      `height:12px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`

## Goals — 목적지 · 내 목적지

`canvas/Goals.dc.html` · 390×844 · 원본 `components/navi/goals-view.tsx` · 렌더 `preview/Goals.png`

> 목적지 목록. GoalRing + 도착 예상 시점. 배분이 모자라면 얼마가 부족한지 숫자로 말한다.

- [ ] **div** — “목적지”
      `display:flex flex-direction:column gap:10px padding:14px 16px 12px`
- [ ] **본문(스크롤 영역)** — “월 저축 배분”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **HeroCard** — “월 저축 배분”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:15px 16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **Card(18)** — “진행 중인 목적지”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px 8px`
  - [ ] **div** — “목적지 추가”
        `display:flex align-items:center justify-content:center gap:6px height:46px border-radius:14px border:1.5px dashed #B9C3D6 background:rgba(255,255,255,.55) color:#3556E6 font-size:14px font-weight:600`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`

## GoalDesign — 목적지 · 새 목적지 설계

`canvas/GoalDesign.dc.html` · 390×844 · 원본 `components/navi/goal-tools.tsx` · 렌더 `preview/GoalDesign.png`

> 새 목적지를 만들 때 목표액·기간에서 월 납입액이 역산되는 화면.

- [ ] **div** — “목적지”
      `display:flex flex-direction:column gap:10px padding:14px 16px 12px`
- [ ] **본문(스크롤 영역)** — “추천 목적지에서 시작”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **Card(18)** — “추천 목적지에서 시작”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 14px`
  - [ ] **HeroCard** — “이름”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:15px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`

## Future — 미래 · 자산 경로

`canvas/Future.dc.html` · 390×844 · 원본 `components/navi/future-view.tsx` · 렌더 `preview/Future.png`

> 10년 뒤 순자산 경로. 보수/기준/낙관 밴드와 마일스톤 도달 시점.

- [ ] **div** — “미래”
      `display:flex flex-direction:column gap:10px padding:14px 16px 12px`
- [ ] **본문(스크롤 영역)** — “기간”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **HeroCard** — “기간”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:14px 14px 13px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **Card(18)** — “다음 자산 지점”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px 6px`
  - [ ] **Card(18)** — “월 소비를 줄인다면”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 14px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`

## Payoff — 미래 · 상환 계획

`canvas/Payoff.dc.html` · 390×844 · 원본 `components/navi/future-view.tsx` · 렌더 `preview/Payoff.png`

> 상환 계획. 전략별 완제 시점·총이자 비교와 완제 순서.

- [ ] **div** — “미래”
      `display:flex flex-direction:column gap:10px padding:14px 16px 12px`
- [ ] **본문(스크롤 영역)** — “저장되지 않는 가정”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **Card(18)** — “저장되지 않는 가정”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px border:1px dashed #B79BFF`
  - [ ] **Card(18)** — “고금리 우선”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 14px`
  - [ ] **Card(18)** — “이 계획을 저장할까요?”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`

## Onboarding — 첫 실행

`canvas/Onboarding.dc.html` · 390×844 · 원본 `app/page.tsx` · 렌더 `preview/Onboarding.png`

> 첫 실행. 아직 아무 데이터가 없는 상태에서 무엇부터 넣으면 되는지만 말한다.

- [ ] **div** — “NAVI”
      `flex:1 min-height:0 display:flex flex-direction:column padding:0 20px`
  - [ ] **div**
        `height:92px`
  - [ ] **div**
        `width:62px height:62px border-radius:20px background:linear-gradient(140deg, #3556E6 0%, #7A3FE4 100%) display:flex align-items:center justify-content:center`
  - [ ] **div** — “NAVI”
        `display:flex align-items:baseline gap:9px margin-top:18px`
  - [ ] **h1** — “월급의 얼마를 쓰고 있는지부터”
        `font-size:26px font-weight:700 letter-spacing:-0.035em line-height:1.35 color:#101828`
  - [ ] text 14px/400 — “지금 위치를 알면 목적지까지 얼마나 조절하면 되는지 보입니다.”
        `font-size:14px line-height:1.6 color:#475467`
  - [ ] **div** — “모든 기록은 이 기기에만”
        `margin-top:24px`
  - [ ] **div** — “내 데이터로 시작하기”
        `margin-top:auto display:flex flex-direction:column gap:10px`

## ProfileDialog — 모달 · 내 수치 입력

`canvas/ProfileDialog.dc.html` · 390×844 · 원본 `components/navi/shared.tsx` · 렌더 `preview/ProfileDialog.png`

> 실수령 급여·총수입 등 기준 수치 입력. 이 값이 홈의 분모다.

- [ ] **div** — “배경을 눌러 닫기”
      `height:60px display:flex align-items:flex-end justify-content:center`
- [ ] **BottomSheet** — “내 수치 입력”
      `flex:1 min-height:0 background:#FFFFFF border-radius:26px 26px 0 0 display:flex flex-direction:column color:#101828`
  - [ ] **div**
        `display:flex justify-content:center padding:9px 0 0`
  - [ ] **div** — “내 수치 입력”
        `display:flex align-items:flex-start justify-content:space-between gap:10px padding:12px 18px 14px border-bottom:1px solid #EFF2F8`
  - [ ] **div** — “기본”
        `flex:1 min-height:0 padding:14px 18px 0 display:flex flex-direction:column gap:15px`
    - [ ] **div** — “기본”
    - [ ] **div** — “소비 목표”
    - [ ] **div** — “추가 설정”
    - [ ] **div** — “데이터”
  - [ ] **div** — “취소”
        `display:flex gap:10px padding:12px 18px 20px border-top:1px solid #EFF2F8`

## TransactionAdd — 모달 · 거래 추가

`canvas/TransactionAdd.dc.html` · 390×844 · 원본 `components/navi/transaction-link-fields.tsx` · 렌더 `preview/TransactionAdd.png`

> 거래 추가. 잔액 반영 토글과 계좌 연결이 여기 있다.

- [ ] **div** — “배경을 눌러 닫기”
      `height:60px display:flex align-items:flex-end justify-content:center`
- [ ] **BottomSheet** — “거래 추가”
      `flex:1 min-height:0 background:#FFFFFF border-radius:26px 26px 0 0 display:flex flex-direction:column color:#101828`
  - [ ] **div**
        `display:flex justify-content:center padding:9px 0 0`
  - [ ] **div** — “거래 추가”
        `display:flex align-items:center justify-content:space-between gap:10px padding:12px 18px 13px border-bottom:1px solid #EFF2F8`
  - [ ] **div** — “거래 종류”
        `flex:1 min-height:0 padding:14px 18px 0 display:flex flex-direction:column gap:15px`
    - [ ] **div** — “거래 종류”
    - [ ] **div** — “날짜”
          `display:flex gap:10px`
    - [ ] **div** — “카테고리”
    - [ ] **div** — “메모”
    - [ ] **div** — “잔액에도 반영하기”
          `background:#F4F6FB border-radius:14px padding:13px`
    - [ ] **div** — “일반 소비는 월급 대비 소비율과 카테고리 한도에 함께 반영됩니다. 저축·투자 이체와 대출상환은”
          `display:flex gap:7px padding:0 2px`
  - [ ] **div** — “취소”
        `display:flex gap:10px padding:12px 18px 20px border-top:1px solid #EFF2F8`

## LimitEditor — 모달 · 한도 조정

`canvas/LimitEditor.dc.html` · 390×844 · 원본 `components/navi/spending-analysis.tsx` · 렌더 `preview/LimitEditor.png`

> 한도 조정. 합계가 예산을 넘는지 즉시 보여준다.

- [ ] **div** — “배경을 눌러 닫기”
      `height:74px display:flex align-items:flex-end justify-content:center`
- [ ] **BottomSheet** — “한도 조정”
      `flex:1 min-height:0 background:#FFFFFF border-radius:26px 26px 0 0 display:flex flex-direction:column color:#101828`
  - [ ] **div**
        `display:flex justify-content:center padding:9px 0 0`
  - [ ] **div** — “한도 조정”
        `display:flex align-items:flex-start justify-content:space-between gap:10px padding:12px 18px 14px border-bottom:1px solid #EFF2F8`
  - [ ] **div** — “이번 달 총한도”
        `flex:1 min-height:0 padding:14px 18px 0`
    - [ ] **div** — “이번 달 총한도”
          `background:#F4F6FB border-radius:16px padding:13px`
    - [ ] **div** — “카테고리 배분”
          `display:flex align-items:center justify-content:space-between gap:8px margin-top:17px`
    - [ ] **div** — “주거/관리”
          `display:flex flex-direction:column margin-top:6px`
  - [ ] **div** — “배분 합계가 총한도와 같아요”
        `display:flex align-items:center justify-content:space-between gap:8px padding:11px 18px background:#E4F4EA border-top:1px solid #C9E5D5`
  - [ ] **div** — “취소”
        `display:flex gap:10px padding:12px 18px 20px border-top:1px solid #EFF2F8`

## AssetDialog — 모달 · 자산 추가

`canvas/AssetDialog.dc.html` · 390×844 · 원본 `components/navi/asset-view.tsx` · 렌더 `preview/AssetDialog.png`

> 자산 추가. 이름과 평가액만 필수.

- [ ] **Scrim여백** — “배경을 눌러 닫기”
      `height:190px display:flex align-items:flex-end justify-content:center`
- [ ] **BottomSheet** — “자산 추가”
      `flex:1 min-height:0 background:#FFFFFF border-radius:26px 26px 0 0 display:flex flex-direction:column color:#101828`
  - [ ] **div**
        `display:flex justify-content:center padding:9px 0 0`
  - [ ] **div** — “자산 추가”
        `display:flex align-items:flex-start justify-content:space-between gap:10px padding:12px 18px 14px border-bottom:1px solid #EFF2F8`
  - [ ] **div** — “자산 이름”
        `flex:1 min-height:0 padding:14px 18px 0 display:flex flex-direction:column gap:15px`
    - [ ] **div** — “자산 이름”
          `flex:1`
    - [ ] **div** — “유형”
          `display:flex gap:10px`
    - [ ] **div** — “연 기대수익률”
          `flex:1`
    - [ ] **Callout(info)** — “거래에서 를 켜면 이 계좌의 평가액이 함께 바뀝니다. 0원이어도 계좌 기록은 남습니다.”
          `display:flex gap:8px padding:10px 11px background:#F4F6FB border-radius:12px`
  - [ ] **div** — “취소”
        `display:flex gap:10px padding:12px 18px 20px border-top:1px solid #EFF2F8`

## DebtDialog — 모달 · 부채 수정

`canvas/DebtDialog.dc.html` · 390×844 · 원본 `components/navi/asset-view.tsx` · 렌더 `preview/DebtDialog.png`

> 부채 수정. 금리·최소상환액이 상환 시뮬레이션의 입력이다.

- [ ] **div** — “배경을 눌러 닫기”
      `height:110px display:flex align-items:flex-end justify-content:center`
- [ ] **BottomSheet** — “카드 할부 수정”
      `flex:1 min-height:0 background:#FFFFFF border-radius:26px 26px 0 0 display:flex flex-direction:column color:#101828`
  - [ ] **div**
        `display:flex justify-content:center padding:9px 0 0`
  - [ ] **div** — “카드 할부 수정”
        `display:flex align-items:flex-start justify-content:space-between gap:10px padding:12px 18px 14px border-bottom:1px solid #EFF2F8`
  - [ ] **div** — “부채 이름”
        `flex:1 min-height:0 padding:14px 18px 0 display:flex flex-direction:column gap:15px`
    - [ ] **div** — “부채 이름”
          `flex:1`
    - [ ] **div** — “유형”
          `display:flex gap:10px`
    - [ ] **div** — “연 금리”
          `display:flex gap:10px`
    - [ ] **Callout(warn)** — “연 14.5%는 보유한 부채 중 가장 높아요. 고금리 우선 전략에서 1순위로 상환됩니다.”
          `display:flex gap:8px padding:10px 11px background:#FDF1E0 border-radius:12px`
    - [ ] **Callout(info)** — “남은 원금을 0으로 두면 완납으로 기록되고 목록에는 남습니다. 삭제하면 연결된 거래의 부채 연”
          `display:flex gap:8px padding:10px 11px background:#F4F6FB border-radius:12px`
  - [ ] **div** — “취소”
        `display:flex gap:10px padding:12px 18px 20px border-top:1px solid #EFF2F8`

## GoalDialog — 모달 · 목적지 추가

`canvas/GoalDialog.dc.html` · 390×844 · 원본 `components/navi/goals-view.tsx` · 렌더 `preview/GoalDialog.png`

> 목적지 추가. 유형에 따라 입력 필드가 바뀐다.

- [ ] **div** — “배경을 눌러 닫기”
      `height:40px display:flex align-items:flex-end justify-content:center`
- [ ] **BottomSheet** — “목적지 추가”
      `flex:1 min-height:0 background:#FFFFFF border-radius:26px 26px 0 0 display:flex flex-direction:column color:#101828`
  - [ ] **div**
        `display:flex justify-content:center padding:9px 0 0`
  - [ ] **div** — “목적지 추가”
        `display:flex align-items:flex-start justify-content:space-between gap:10px padding:12px 18px 14px border-bottom:1px solid #EFF2F8`
  - [ ] **div** — “유형”
        `flex:1 min-height:0 padding:14px 18px 0 display:flex flex-direction:column gap:15px`
    - [ ] **div** — “유형”
    - [ ] **div** — “이름”
          `flex:1`
    - [ ] **div** — “갚을 부채 선택”
    - [ ] **div** — “우선순위”
          `display:flex gap:10px`
    - [ ] **Callout(info)** — “부채 상환 목적지는 적립 대신 을 따릅니다. 목표액·적립액 입력란이 없고 홈 대표로도 지정할 ”
          `display:flex gap:8px padding:10px 11px background:#F4F6FB border-radius:12px`
  - [ ] **div** — “취소”
        `display:flex gap:10px padding:12px 18px 20px border-top:1px solid #EFF2F8`

## RecurringDialog — 모달 · 반복 거래

`canvas/RecurringDialog.dc.html` · 390×844 · 원본 `components/navi/spending-view.tsx` · 렌더 `preview/RecurringDialog.png`

> 반복 거래. 기존 반복 규칙 형식을 바꾸지 않는다.

- [ ] **div** — “배경을 눌러 닫기”
      `height:40px display:flex align-items:flex-end justify-content:center`
- [ ] **BottomSheet** — “반복 거래”
      `flex:1 min-height:0 background:#FFFFFF border-radius:26px 26px 0 0 display:flex flex-direction:column color:#101828`
  - [ ] **div**
        `display:flex justify-content:center padding:9px 0 0`
  - [ ] **div** — “반복 거래”
        `display:flex align-items:flex-start justify-content:space-between gap:10px padding:12px 18px 14px border-bottom:1px solid #EFF2F8`
  - [ ] **div** — “등록된 규칙”
        `flex:1 min-height:0 padding:14px 18px 0 display:flex flex-direction:column gap:15px`
    - [ ] **div** — “등록된 규칙”
    - [ ] **div** — “새 규칙”
  - [ ] **div** — “닫기”
        `display:flex gap:10px padding:12px 18px 20px border-top:1px solid #EFF2F8`

## GoalContribute — 모달 · 적립액 추가

`canvas/GoalContribute.dc.html` · 390×844 · 원본 `components/navi/goals-view.tsx` · 렌더 `preview/GoalContribute.png`

> 목적지에 적립액을 더한다. 시뮬레이션이 아니라 기록이다.

- [ ] **div** — “배경을 눌러 닫기”
      `height:60px display:flex align-items:flex-end justify-content:center`
- [ ] **BottomSheet** — “비상금 6개월 적립액 추가”
      `flex:1 min-height:0 background:#FFFFFF border-radius:26px 26px 0 0 display:flex flex-direction:column color:#101828`
  - [ ] **div**
        `display:flex justify-content:center padding:9px 0 0`
  - [ ] **div** — “비상금 6개월 적립액 추가”
        `display:flex align-items:flex-start justify-content:space-between gap:10px padding:12px 18px 14px border-bottom:1px solid #EFF2F8`
  - [ ] **div** — “68”
        `flex:1 min-height:0 padding:14px 18px 0 display:flex flex-direction:column gap:15px`
    - [ ] **Card(18)** — “68”
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px 15px`
    - [ ] **div** — “추가 적립액”
    - [ ] **Card(18)** — “저장하면 이렇게 바뀝니다”
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 15px`
    - [ ] **Callout(info)** — “이 기록은 바꿉니다. 통장 잔액이나 소비 거래에 중복 반영되지 않아요.”
          `display:flex gap:8px padding:10px 11px background:#F4F6FB border-radius:12px`
    - [ ] **Card(18)** — “최근 적립”
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 15px`
  - [ ] **div** — “취소”
        `display:flex gap:10px padding:12px 18px 20px border-top:1px solid #EFF2F8`

## MonthlyClose — 모달 · 월 마감

`canvas/MonthlyClose.dc.html` · 390×844 · 원본 `components/navi/spending-analysis.tsx` · 렌더 `preview/MonthlyClose.png`

> 월 마감. 마감하면 그 달 값이 고정된다는 것을 분명히 말한다.

- [ ] **div** — “배경을 눌러 닫기”
      `height:40px display:flex align-items:flex-end justify-content:center`
- [ ] **BottomSheet** — “2026년 8월 마감”
      `flex:1 min-height:0 background:#FFFFFF border-radius:26px 26px 0 0 display:flex flex-direction:column color:#101828`
  - [ ] **div**
        `display:flex justify-content:center padding:9px 0 0`
  - [ ] **div** — “2026년 8월 마감”
        `display:flex align-items:flex-start justify-content:space-between gap:10px padding:12px 18px 14px border-bottom:1px solid #EFF2F8`
  - [ ] **div** — “이미 에 마감한 달입니다. 다시 저장하면 기존 마감값을 덮어씁니다.”
        `flex:1 min-height:0 padding:14px 18px 0 display:flex flex-direction:column gap:15px`
    - [ ] **Callout(warn)** — “이미 에 마감한 달입니다. 다시 저장하면 기존 마감값을 덮어씁니다.”
          `display:flex gap:8px padding:10px 11px background:#FDF1E0 border-radius:12px`
    - [ ] **div** — “그 달의 실제 수치”
    - [ ] **div** — “자동으로 채워진 값”
    - [ ] **Callout(info)** — “급여를 비워 두면 그 달은 로 남습니다. 지금 급여로 과거를 채우지 않아요.”
          `display:flex gap:8px padding:10px 11px background:#F4F6FB border-radius:12px`
  - [ ] **div** — “위 수치가 실제와 같음을 확인했습니다.”
        `padding:12px 18px background:#F4F6FB border-top:1px solid #E3E8F1`
  - [ ] **div** — “취소”
        `display:flex gap:10px padding:12px 18px 20px border-top:1px solid #EFF2F8`

## ImportReview — 모달 · 백업 불러오기

`canvas/ImportReview.dc.html` · 390×844 · 원본 `components/navi/import-review.tsx` · 렌더 `preview/ImportReview.png`

> 백업 불러오기 검토. 무엇이 덮어써지는지 건수로 보여준 뒤 확인받는다.

- [ ] **div** — “배경을 눌러 닫기”
      `height:40px display:flex align-items:flex-end justify-content:center`
- [ ] **BottomSheet** — “백업 불러오기”
      `flex:1 min-height:0 background:#FFFFFF border-radius:26px 26px 0 0 display:flex flex-direction:column color:#101828`
  - [ ] **div**
        `display:flex justify-content:center padding:9px 0 0`
  - [ ] **div** — “백업 불러오기”
        `display:flex align-items:flex-start justify-content:space-between gap:10px padding:12px 18px 14px border-bottom:1px solid #EFF2F8`
  - [ ] **div** — “적용 방식”
        `flex:1 min-height:0 padding:14px 18px 0 display:flex flex-direction:column gap:15px`
    - [ ] **div** — “적용 방식”
    - [ ] **div** — “불러올 항목”
    - [ ] **div** — “적용 후”
  - [ ] **div** — “바뀌는 내용을 확인했습니다.”
        `padding:12px 18px background:#F4F6FB border-top:1px solid #E3E8F1`
  - [ ] **div** — “취소”
        `display:flex gap:10px padding:12px 18px 20px border-top:1px solid #EFF2F8`

## CoachPanel — 모달 · 코칭

`canvas/CoachPanel.dc.html` · 390×844 · 원본 `components/navi/coach-panel.tsx` · 렌더 `preview/CoachPanel.png`

> 코칭 기록. 저장된 조언이 시간 순으로 쌓인다.

- [ ] **div** — “배경을 눌러 닫기”
      `height:40px display:flex align-items:flex-end justify-content:center`
- [ ] **BottomSheet** — “코칭”
      `flex:1 min-height:0 background:#FFFFFF border-radius:26px 26px 0 0 display:flex flex-direction:column color:#101828`
  - [ ] **div**
        `display:flex justify-content:center padding:9px 0 0`
  - [ ] **div** — “코칭”
        `display:flex align-items:flex-start justify-content:space-between gap:10px padding:12px 18px 14px border-bottom:1px solid #EFF2F8`
  - [ ] **div** — “1”
        `flex:1 min-height:0 padding:14px 18px 0 display:flex flex-direction:column gap:15px`
    - [ ] **div** — “1”
          `display:flex flex-direction:column gap:9px`
    - [ ] **Callout(info)** — “다른 안내 4개 더 보기”
          `display:flex align-items:center justify-content:space-between gap:8px height:48px padding:0 13px border-radius:12px background:#F4F6FB`
    - [ ] **div** — “카테고리 절감 가정”
  - [ ] **div** — “닫기”
        `display:flex gap:10px padding:12px 18px 20px border-top:1px solid #EFF2F8`

## CoachEmpty — 모달 · 코칭 기록 없음

`canvas/CoachEmpty.dc.html` · 390×844 · 원본 `components/navi/coach-panel.tsx` · 렌더 `preview/CoachEmpty.png`

> 코칭 기록이 없을 때. 0건을 성과처럼 보이게 하지 않는다.

- [ ] **div** — “배경을 눌러 닫기”
      `height:60px display:flex align-items:flex-end justify-content:center`
- [ ] **BottomSheet** — “코칭”
      `flex:1 min-height:0 background:#FFFFFF border-radius:26px 26px 0 0 display:flex flex-direction:column color:#101828`
  - [ ] **div**
        `display:flex justify-content:center padding:9px 0 0`
  - [ ] **div** — “코칭”
        `display:flex align-items:flex-start justify-content:space-between gap:10px padding:12px 18px 14px border-bottom:1px solid #EFF2F8`
  - [ ] **div** — “아직 안내할 것이 없어요”
        `flex:1 min-height:0 padding:14px 18px 0 display:flex flex-direction:column gap:15px`
    - [ ] **Card(18)** — “아직 안내할 것이 없어요”
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px 15px`
    - [ ] **Card(18)** — “두 가지만 있으면 시작합니다”
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px 15px`
    - [ ] **Card(18)** — “기록이 쌓이면 이런 안내를 받습니다”
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px 15px`
  - [ ] **div** — “소비 기록하기”
        `display:flex gap:10px padding:12px 18px 20px border-top:1px solid #EFF2F8`

## AlertsPanel — 모달 · 알림

`canvas/AlertsPanel.dc.html` · 390×844 · 원본 `components/navi/coach-panel.tsx` · 렌더 `preview/AlertsPanel.png`

> 알림 목록. 읽음/안읽음이 구분된다.

- [ ] **div** — “배경을 눌러 닫기”
      `height:40px display:flex align-items:flex-end justify-content:center`
- [ ] **BottomSheet** — “알림 3건”
      `flex:1 min-height:0 background:#FFFFFF border-radius:26px 26px 0 0 display:flex flex-direction:column color:#101828`
  - [ ] **div**
        `display:flex justify-content:center padding:9px 0 0`
  - [ ] **div** — “알림 3건”
        `display:flex align-items:flex-start justify-content:space-between gap:10px padding:12px 18px 14px border-bottom:1px solid #EFF2F8`
  - [ ] **div** — “주거/관리 한도의 94%를 썼어요”
        `flex:1 min-height:0 padding:14px 18px 0 display:flex flex-direction:column gap:15px`
    - [ ] **div** — “주거/관리 한도의 94%를 썼어요”
          `display:flex flex-direction:column`
    - [ ] **Callout(info)** — “자산을 넘게 갱신하지 않으면 여기에 알려드려요. 지금은 갱신이 필요한 자산이 없습니다.”
          `display:flex gap:8px padding:10px 11px background:#F4F6FB border-radius:12px`
    - [ ] **div** — “알림이 없을 때”
  - [ ] **div** — “닫기”
        `display:flex gap:10px padding:12px 18px 20px border-top:1px solid #EFF2F8`

## PeerDialog — 모달 · 또래 기준 등록

`canvas/PeerDialog.dc.html` · 390×844 · 원본 `components/navi/peer-card.tsx` · 렌더 `preview/PeerDialog.png`

> 또래 기준 등록. 나이대는 초반(0~3)/중반(4~6)/후반(7~9)으로만 나눈다.

- [ ] **div** — “배경을 눌러 닫기”
      `height:40px display:flex align-items:flex-end justify-content:center`
- [ ] **BottomSheet** — “20대 후반 비교 기준”
      `flex:1 min-height:0 background:#FFFFFF border-radius:26px 26px 0 0 display:flex flex-direction:column color:#101828`
  - [ ] **div**
        `display:flex justify-content:center padding:9px 0 0`
  - [ ] **div** — “20대 후반 비교 기준”
        `display:flex align-items:flex-start justify-content:space-between gap:10px padding:12px 18px 14px border-bottom:1px solid #EFF2F8`
  - [ ] **div** — “NAVI에는 세부 연령별 통계가 여기 넣은 값은 화면에서 항상 “내가 등록한 기준”으로 표시되”
        `flex:1 min-height:0 padding:14px 18px 0 display:flex flex-direction:column gap:15px`
    - [ ] **Callout(warn)** — “NAVI에는 세부 연령별 통계가 여기 넣은 값은 화면에서 항상 “내가 등록한 기준”으로 표시되”
          `display:flex gap:8px padding:10px 11px background:#FDF1E0 border-radius:12px`
    - [ ] **div** — “연령 구간”
          `display:flex gap:10px`
    - [ ] **div** — “평균 소비율”
          `display:flex gap:10px`
    - [ ] **div** — “기준 연도”
          `display:flex gap:10px`
    - [ ] **div** — “자료 출처”
          `flex:1`
    - [ ] **Callout(info)** — “분모가 실수령 급여가 아닌 통계라면 내 소비율과 직접 비교할 수 없어요. 출처의 기준을 꼭 확”
          `display:flex gap:8px padding:10px 11px background:#F4F6FB border-radius:12px`
  - [ ] **div** — “취소”
        `display:flex gap:10px padding:12px 18px 20px border-top:1px solid #EFF2F8`

## StorageStates — 상태 · 저장소 로딩·복구

`canvas/StorageStates.dc.html` · 390×1309 · 원본 `app/page.tsx` · 렌더 `preview/StorageStates.png`

> 저장소 로딩·복구 상태 모음. 로딩과 "데이터 없음"은 다른 화면이다.

- [ ] **div** — “저장소 로딩 · 실패 · 복구”
      `padding:0 2px 6px`
- [ ] text 11px/600 — “A · 불러오는 중”
      `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
- [ ] **Card(18)** — “저장된 기록을 불러오는 중”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:18px 16px`
- [ ] text 11px/600 — “B · 불러오기 실패”
      `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
- [ ] **Card(18)** — “기록을 불러오지 못했어요”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:18px 16px`
- [ ] text 11px/600 — “C · 복구 파일 오류”
      `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
- [ ] **Card(18)** — “이 파일은 읽을 수 없어요”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:18px 16px`
- [ ] text 11px/600 — “D · 샘플에서 내 데이터로 전환”
      `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
- [ ] **Card(18)** — “내 데이터로 시작할까요?”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:18px 16px`

## EmptyStates — 상태 · 미입력 5종

`canvas/EmptyStates.dc.html` · 390×1718 · 원본 `app/page.tsx` · 렌더 `preview/EmptyStates.png`

> 미입력 5종. **미입력을 0원이나 좋은 성과로 표시하지 않는다**는 규칙이 그림으로 있는 시트.

- [ ] **div** — “미입력 · 빈 상태”
      `padding:0 2px 6px`
- [ ] text 11px/600 — “A · 첫 시작 · 홈”
      `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
- [ ] **Card(20)** — “출발 준비”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px`
- [ ] text 11px/600 — “B · 급여 미입력 · 소비 기록만 있음”
      `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
- [ ] **Card(20)** — “현재 위치”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px`
- [ ] text 11px/600 — “C · 급여 0원 · 부수입만 있음”
      `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
- [ ] **Card(20)** — “현재 위치”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px`
- [ ] text 11px/600 — “D · 자산 미입력”
      `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
- [ ] **Card(20)** — “아직 자산을 입력하지 않았어요”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px`
- [ ] text 11px/600 — “E · 거래 없음 vs 검색 결과 없음”
      `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
- [ ] **Card(20)** — “9월에 기록한 거래가 없어요”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px`

## PeerStates — 상태 · 또래 카드 5종

`canvas/PeerStates.dc.html` · 390×1595 · 원본 `components/navi/peer-card.tsx` · 렌더 `preview/PeerStates.png`

> 또래 카드 5종. 통계가 없으면 없다고 말한다. 평균·백분위·상위 %를 지어내지 않는다.

- [ ] **div** — “또래 카드 · 상태 5종”
      `padding:0 2px 6px`
- [ ] text 11px/600 — “A · 나이 미입력”
      `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
- [ ] **Card(18)** — “또래와 내 페이스”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
- [ ] text 11px/600 — “B · 연령 구간 있음 · 비교 기준 없음”
      `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
- [ ] **Card(18)** — “20대 후반”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
- [ ] text 11px/600 — “C · 직접 등록한 기준으로 비교 가능”
      `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
- [ ] **Card(18)** — “20대 후반”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
- [ ] text 11px/600 — “D · 급여 또는 소비 기록 부족”
      `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
- [ ] **Card(18)** — “20대 후반 · 비교 기준 등록됨”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
- [ ] text 11px/600 — “E · 입력 연도 확인 필요”
      `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
- [ ] **Card(18)** — “20대 후반”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`

## GoalTypes — 상태 · 목적지 유형 5종

`canvas/GoalTypes.dc.html` · 390×1767 · 원본 `components/navi/goals-view.tsx` · 렌더 `preview/GoalTypes.png`

> 목적지 유형 5종의 카드 변형.

- [ ] **div** — “목적지 유형 5종”
      `padding:0 2px 6px`
- [ ] text 11px/600 — “A · 일반 저축 — 수익률을 쓰지 않음”
      `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
- [ ] **Card(18)** — “💰”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px 15px`
- [ ] text 11px/600 — “B · 투자 — 수익률이 계산에 들어감”
      `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
- [ ] **Card(18)** — “🌱”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px 15px`
- [ ] text 11px/600 — “C · 순자산 — 값을 직접 넣지 않음”
      `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
- [ ] **Card(18)** — “💎”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px 15px`
- [ ] text 11px/600 — “D · 부채 상환 — 상환 계획에서 계산”
      `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
- [ ] **Card(18)** — “🏔️”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px 15px`
- [ ] text 11px/600 — “E · 비상금 — 저축과 같되 수익률 0% 고정”
      `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
- [ ] **Card(18)** — “🧯”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px 15px`

## ModalErrors — 상태 · 모달 오류·저장 6종

`canvas/ModalErrors.dc.html` · 390×2061 · 원본 `모달 공통 (폼 검증·저장 경로)` · 렌더 `preview/ModalErrors.png`

> 모달 오류·저장 6종. 각 오류의 문구와 위치가 정해져 있다.

- [ ] **div** — “모달 오류 · 저장 상태 6종”
      `padding:0 2px 6px`
- [ ] text 11px/600 — “A · 필수 값 미입력 — 저장 비활성”
      `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
- [ ] **Card(18)** — “거래 추가”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:16px`
- [ ] text 11px/600 — “B · 값이 규칙에 어긋남 — 배분 합 초과”
      `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
- [ ] **Card(18)** — “카테고리 배분 편집”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:16px`
- [ ] text 11px/600 — “C · 저장 중 — 입력 잠금”
      `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
- [ ] **Card(18)** — “자산 추가”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:16px`
- [ ] text 11px/600 — “D · 저장 실패 — 입력값 보존”
      `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
- [ ] **Card(18)** — “저장하지 못했어요”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:16px`
- [ ] text 11px/600 — “E · 저장 완료 — 무엇이 바뀌었는지”
      `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
- [ ] **Card(18)** — “저장했어요”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:16px`
- [ ] text 11px/600 — “F · 저장하지 않고 닫기”
      `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
- [ ] **Card(18)** — “저장하지 않고 닫을까요?”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:16px`

## Confirmations — 상태 · 삭제·초기화 확인

`canvas/Confirmations.dc.html` · 390×1228 · 원본 `components/ui/alert-dialog.tsx 사용처` · 렌더 `preview/Confirmations.png`

> 삭제·초기화 확인 4종. 되돌릴 수 없는 동작은 무엇이 사라지는지 건수로 말한다.

- [ ] **div** — “삭제 · 초기화 확인”
      `padding:0 2px 6px`
- [ ] text 11px/600 — “A · 자산 삭제”
      `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
- [ ] **Card(20)** — “ETF 계좌를 삭제할까요?”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px`
- [ ] text 11px/600 — “B · 거래 삭제 · 잔액 반영됨”
      `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
- [ ] **Card(20)** — “이 거래를 삭제할까요?”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px`
- [ ] text 11px/600 — “C · 목적지 삭제”
      `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
- [ ] **Card(20)** — “비상금 6개월을 삭제할까요?”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px`
- [ ] text 11px/600 — “D · 반복 규칙 삭제”
      `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
- [ ] **Card(20)** — “ETF 자동이체 규칙을 삭제할까요?”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px`
- [ ] text 11px/600 — “E · 전체 초기화”
      `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
- [ ] **Card(20)** — “모두 지우고 새로 시작할까요?”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px`

## DesktopHome — 데스크톱 · 홈

`canvas/DesktopHome.dc.html` · 1440×900 · 원본 `app/page.tsx` · 렌더 `preview/DesktopHome.png`

> 데스크톱 홈. 사이드바 + 2열. 모바일 카드를 그냥 늘리지 않고 가로를 실제로 쓴다.

- [ ] **div** — “NAVI”
      `width:232px background:#FFFFFF display:flex flex-direction:column padding:22px 16px 18px`
- [ ] **div** — “샘플 데이터로 둘러보는 중 · 표시된 이름과 금액은 실제 정보가 아닙니다”
      `flex:1 display:flex flex-direction:column padding:18px 28px 22px`
  - [ ] **div** — “샘플 데이터로 둘러보는 중 · 표시된 이름과 금액은 실제 정보가 아닙니다”
        `display:flex align-items:center justify-content:space-between gap:12px height:38px padding:0 16px background:#E9EDFD border-radius:12px`
  - [ ] **div** — “2026년 9월 8일 · 이번 달 22일 남음”
        `display:flex align-items:flex-end justify-content:space-between gap:12px margin-top:18px`
  - [ ] **div** — “현재 위치”
        `flex:1 min-height:0 display:grid grid-template-columns:minmax(0, 1.6fr) minmax(0, 1fr) gap:18px margin-top:16px`
    - [ ] **div** — “현재 위치”
          `display:flex flex-direction:column gap:16px`
    - [ ] **div** — “다음 안내”
          `display:flex flex-direction:column gap:14px`

## DesktopLedger — 데스크톱 · 소비 내역

`canvas/DesktopLedger.dc.html` · 1440×900 · 원본 `components/navi/spending-view.tsx` · 렌더 `preview/DesktopLedger.png`

> 데스크톱 내역. 표 형태. 소비율 제외 행은 배경으로 구분한다.

- [ ] **div** — “NAVI”
      `width:232px background:#FFFFFF display:flex flex-direction:column padding:22px 16px 18px`
- [ ] **div** — “소비 · 내역”
      `flex:1 display:flex flex-direction:column padding:22px 28px`
  - [ ] **div** — “소비 · 내역”
        `display:flex align-items:flex-end justify-content:space-between gap:12px`
  - [ ] **div** — “메모·카테고리로 검색”
        `flex:1 min-height:0 display:grid grid-template-columns:minmax(0, 1.75fr) minmax(0, 1fr) gap:18px margin-top:18px`
    - [ ] **Card(20)** — “메모·카테고리로 검색”
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px display:flex flex-direction:column`
    - [ ] **div** — “9월 일반 소비”
          `display:flex flex-direction:column gap:14px`

## Tokens — 토큰 · 색 · 타이포 · 간격

`canvas/Tokens.dc.html` · 1200×1684 · 원본 `app/globals.css · lib/engine/constants.ts` · 렌더 `preview/Tokens.png`

> 토큰 시트. 구현이 아니라 참조용.

- [ ] **div** — “NAVI DESIGN SYSTEM v3”
      `display:flex align-items:flex-end justify-content:space-between gap:20px border-bottom:2px solid #101828`
- [ ] **div** — “01 · 표면과 잉크 — LIGHT”
      `display:grid grid-template-columns:repeat(2, minmax(0, 1fr)) gap:26px`
- [ ] **div** — “03 · 브랜드와 상태색 — 의미가 고정된 색 · 라이트/다크 대응”
- [ ] **div** — “04 · 데이터 팔레트 — 2.2에서 그대로 유지”
- [ ] **div** — “05 · 타이포 위계”
      `display:grid grid-template-columns:minmax(0, 1.35fr) minmax(0, 1fr) gap:30px`

## Components — 컴포넌트 · 상태

`canvas/Components.dc.html` · 1200×1471 · 원본 `components/navi/shared.tsx · components/ui/button.tsx` · 렌더 `preview/Components.png`

> 컴포넌트·상태 시트. SPEC-COMPONENTS.md의 그림판.

- [ ] **div** — “NAVI DESIGN SYSTEM v3”
      `display:flex align-items:flex-end justify-content:space-between gap:20px border-bottom:2px solid #101828`
- [ ] **div** — “01 · 버튼 위계와 상태”
      `display:grid grid-template-columns:minmax(0, 1fr) minmax(0, 1.1fr) gap:32px`
- [ ] **div** — “07 · 행동을 어디에 놓는가 — 이번 재설계의 핵심 규칙”
      `margin-top:auto padding:18px 20px background:#F4F6FB border-radius:16px`

