# 화면별 조립 체크리스트

각 화면을 **위에서 아래 순서로** 조립하세요. 블록 하나를 만들 때마다 지워 나가면
빠뜨린 것이 바로 보입니다. 굵은 이름은 `SPEC-COMPONENTS.md`의 컴포넌트입니다.

값은 요약입니다. **정확한 값은 항상 `canvas/<이름>.dc.html`이 기준**이고,
더 자세한 구조는 `spec/<이름>.outline.md`에 있습니다.

다크 화면은 별도 항목이 없습니다. 같은 구조에 `canvas/_tools/darken.py`의 색 대응만 적용한 것입니다.

---

## Assets — 자산 · 구성

`canvas/Assets.dc.html` · 390×844 · 원본 `components/navi/asset-view.tsx` · 렌더 `preview/Assets.png`

> 순자산이 주 지표. 스파크라인 + 구성 막대 + 계좌 행 리스트로, 2.2의 가운데 정렬 타일 5개를 대체한다.

- [ ] **div** — “자산”
      `display:flex flex-direction:column gap:10px padding:14px 16px 12px`
- [ ] **본문(스크롤 영역)** — “순자산”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **HeroCard** — “순자산”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **div** — “현금성 자산 · 생활비 기준”
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
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px 4px`
  - [ ] **Card(18)** — “저장되지 않는 가정”
        `background:#FFFFFF border:1px dashed #B79BFF border-radius:18px padding:11px 14px 11px`
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
  - [ ] **p** — “지금 위치를 알면 목적지까지 얼마나 조절할지 보여요.”
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
        `flex:1 min-height:0 padding:14px 18px 14px display:flex flex-direction:column gap:15px`
    - [ ] **div** — “자산 이름”
          `flex:0 0 auto`
    - [ ] **div** — “유형”
          `display:flex gap:10px`
    - [ ] **div** — “연 기대수익률”
          `flex:0 0 auto`
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
        `flex:1 min-height:0 padding:14px 18px 14px display:flex flex-direction:column gap:15px`
    - [ ] **div** — “부채 이름”
          `flex:0 0 auto`
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
        `flex:1 min-height:0 padding:14px 18px 14px display:flex flex-direction:column gap:15px`
    - [ ] **div** — “유형”
    - [ ] **div** — “이름”
          `flex:0 0 auto`
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
  - [ ] **div** — “등록된 반복 거래”
        `flex:1 min-height:0 padding:14px 18px 0 display:flex flex-direction:column gap:15px`
    - [ ] **div** — “등록된 반복 거래”
    - [ ] **div** — “새 반복 거래”
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
        `flex:1 min-height:0 padding:14px 18px 0 display:flex flex-direction:column gap:12px`
    - [ ] **div** — “1”
          `display:flex flex-direction:column gap:8px`
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
  - [ ] **div** — “닫기”
        `display:flex gap:10px padding:12px 18px 20px border-top:1px solid #EFF2F8`

## AlertsEmpty — 모달 · 알림 없음

`canvas/AlertsEmpty.dc.html` · 390×844 · 원본 `components/navi/coach-panel.tsx` · 렌더 `preview/AlertsEmpty.png`

- [ ] **div** — “배경을 눌러 닫기”
      `height:40px display:flex align-items:flex-end justify-content:center`
- [ ] **BottomSheet** — “알림”
      `flex:1 min-height:0 background:#FFFFFF border-radius:26px 26px 0 0 display:flex flex-direction:column color:#101828`
  - [ ] **div**
        `display:flex justify-content:center padding:9px 0 0`
  - [ ] **div** — “알림”
        `display:flex align-items:flex-start justify-content:space-between gap:10px padding:12px 18px 14px border-bottom:1px solid #EFF2F8`
  - [ ] **div** — “지금 조치할 것이 없어요”
        `flex:1 min-height:0 padding:14px 18px 0 display:flex flex-direction:column gap:15px`
    - [ ] **div** — “지금 조치할 것이 없어요”
          `display:flex flex-direction:column align-items:center text-align:center padding:20px 10px background:#F4F6FB border-radius:14px`
    - [ ] **Callout(info)** — “자산을 넘게 갱신하지 않으면 여기에 알려드려요. 지금은 갱신이 필요한 자산이 없습니다.”
          `display:flex gap:8px padding:10px 11px background:#F4F6FB border-radius:12px`
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
        `flex:1 min-height:0 padding:14px 18px 14px display:flex flex-direction:column gap:15px`
    - [ ] **Callout(warn)** — “NAVI에는 세부 연령별 통계가 여기 넣은 값은 화면에서 항상 “내가 등록한 기준”으로 표시되”
          `display:flex gap:8px padding:10px 11px background:#FDF1E0 border-radius:12px`
    - [ ] **div** — “연령 구간”
          `display:flex gap:10px`
    - [ ] **div** — “평균 소비율”
          `display:flex gap:10px`
    - [ ] **div** — “기준 연도”
          `display:flex gap:10px`
    - [ ] **div** — “자료 출처”
          `flex:0 0 auto`
    - [ ] **Callout(info)** — “실수령 급여가 아닌 다른 소득을 기준으로 한 통계라면 내 소비율과 바로 비교할 수 없어요. 출”
          `display:flex gap:8px padding:10px 11px background:#F4F6FB border-radius:12px`
  - [ ] **div** — “취소”
        `display:flex gap:10px padding:12px 18px 20px border-top:1px solid #EFF2F8`

## StorageStates — 상태 · 저장소 로딩·복구

`canvas/StorageStates.dc.html` · 390×1324 · 원본 `app/page.tsx` · 렌더 `preview/StorageStates.png`

> 저장소 로딩·복구 상태 모음. 로딩과 "데이터 없음"은 다른 화면이다.

- [ ] **div** — “구현 참고 · 앱 화면이 아닙니다”
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

## EmptyStates — 상태 · 미입력 6종

`canvas/EmptyStates.dc.html` · 390×2480 · 원본 `app/page.tsx` · 렌더 `preview/EmptyStates.png`

> 미입력 6종. **미입력을 0원이나 좋은 성과로 표시하지 않는다**는 규칙이 그림으로 있는 시트.

- [ ] **div** — “구현 참고 · 앱 화면이 아닙니다”
      `padding:0 2px 6px`
- [ ] text 11px/600 — “A · 첫 시작 · 홈”
      `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
- [ ] **Card(20)** — “출발 준비”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px`
- [ ] text 11px/600 — “B · 급여 미입력 · 소비 기록만 있음”
      `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
- [ ] **Card(20)** — “이번 달 기록한 소비”
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
- [ ] text 11px/600 — “F · 히어로 이력 부족 · 예상을 아직 보여 주지 않을 때”
      `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
- [ ] **Card(20)** — “이번 달 기록한 소비”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px`
- [ ] **Card(20)** — “각주 둘째 줄 · 부족한 것에 따라 셋 중 하나”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:12px 16px 6px`

## PeerStates — 상태 · 또래 카드 5종

`canvas/PeerStates.dc.html` · 390×1555 · 원본 `components/navi/peer-card.tsx` · 렌더 `preview/PeerStates.png`

> 또래 카드 5종. 통계가 없으면 없다고 말한다. 평균·백분위·상위 %를 지어내지 않는다.

- [ ] **div** — “구현 참고 · 앱 화면이 아닙니다”
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

`canvas/GoalTypes.dc.html` · 390×1920 · 원본 `components/navi/goals-view.tsx` · 렌더 `preview/GoalTypes.png`

> 목적지 유형 5종의 카드 변형.

- [ ] **div** — “구현 참고 · 앱 화면이 아닙니다”
      `padding:0 2px 6px`
- [ ] text 11px/600 — “A · 일반 저축”
      `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
- [ ] **Card(18)** — “💰”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px 15px`
- [ ] text 11px/600 — “B · 투자”
      `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
- [ ] **Card(18)** — “🌱”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px 15px`
- [ ] text 11px/600 — “C · 순자산”
      `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
- [ ] **Card(18)** — “💎”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px 15px`
- [ ] text 11px/600 — “D · 부채 상환”
      `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
- [ ] **Card(18)** — “🏔️”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px 15px`
- [ ] text 11px/600 — “E · 비상금”
      `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
- [ ] **Card(18)** — “🧯”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px 15px`

## ModalErrors — 상태 · 모달 오류·저장 6종

`canvas/ModalErrors.dc.html` · 390×2100 · 원본 `모달 공통 (폼 검증·저장 경로)` · 렌더 `preview/ModalErrors.png`

> 모달 오류·저장 6종. 각 오류의 문구와 위치가 정해져 있다.

- [ ] **div** — “구현 참고 · 앱 화면이 아닙니다”
      `padding:0 2px 6px`
- [ ] text 11px/600 — “A · 필수 값 미입력 — 저장 비활성”
      `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
- [ ] **Card(18)** — “거래 추가”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:16px`
- [ ] text 11px/600 — “B · 카테고리 한도 합계가 총한도를 넘음”
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
- [ ] **div** — “저장하지 않고 닫을까요?”
      `display:flex flex-direction:column gap:8px`

## Confirmations — 상태 · 삭제·초기화 확인

`canvas/Confirmations.dc.html` · 390×1245 · 원본 `components/ui/alert-dialog.tsx 사용처` · 렌더 `preview/Confirmations.png`

> 삭제·초기화 확인 4종. 되돌릴 수 없는 동작은 무엇이 사라지는지 건수로 말한다.

- [ ] **div** — “구현 참고 · 앱 화면이 아닙니다”
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
- [ ] text 11px/600 — “D · 반복 거래 삭제”
      `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
- [ ] **Card(20)** — “ETF 자동이체 반복 거래를 삭제할까요?”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px`
- [ ] text 11px/600 — “E · 전체 초기화”
      `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
- [ ] **Card(20)** — “모두 지우고 새로 시작할까요?”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px`

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

`canvas/Tokens.dc.html` · 1200×1720 · 원본 `app/globals.css · lib/engine/constants.ts` · 렌더 `preview/Tokens.png`

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

`canvas/Components.dc.html` · 1200×2724 · 원본 `components/navi/shared.tsx · components/ui/button.tsx` · 렌더 `preview/Components.png`

> 컴포넌트·상태 시트. SPEC-COMPONENTS.md의 그림판.

- [ ] **div** — “NAVI DESIGN SYSTEM v3”
      `display:flex align-items:flex-end justify-content:space-between gap:20px border-bottom:2px solid #101828`
- [ ] **div** — “01 · 버튼 위계와 상태”
      `display:grid grid-template-columns:minmax(0, 1fr) minmax(0, 1.1fr) gap:32px`
- [ ] **div** — “07 · 행동을 어디에 놓는가 — 이번 재설계의 핵심 규칙”
      `padding:18px 20px background:#F4F6FB border-radius:16px`
- [ ] **div** — “08 · v5 달력과 하루 시트 — 새 컴포넌트 11종”

## IntroPosition — 첫 실행 · 소개 1 현재 위치

`canvas/IntroPosition.dc.html` · 390×844 · 원본 `v4 미구현 · plan/v4-stocks.md §3` · 렌더 `preview/IntroPosition.png`

- [ ] **div** — “소개 1 / 3”
      `flex:1 min-height:0 display:flex flex-direction:column padding:0 20px`
  - [ ] **div** — “소개 1 / 3”
        `display:flex align-items:center justify-content:space-between gap:8px height:56px margin-top:8px`
  - [ ] **div** — “현재 위치”
        `margin-top:36px display:flex flex-direction:column gap:10px`
  - [ ] text 11px/600 — “현재 위치”
        `display:block margin-top:30px font-size:11px font-weight:600 letter-spacing:0.07em color:#3556E6`
  - [ ] **h1** — “이번 달 소비가 월급의 몇 %인지 숫자 하나로 봅니다.”
        `font-size:23px font-weight:700 letter-spacing:-0.03em line-height:1.4 color:#101828`
  - [ ] **div** — “다음”
        `margin-top:auto display:flex flex-direction:column gap:16px`

## IntroRoute — 첫 실행 · 소개 2 항로

`canvas/IntroRoute.dc.html` · 390×844 · 원본 `v4 미구현 · plan/v4-stocks.md §3` · 렌더 `preview/IntroRoute.png`

- [ ] **div** — “소개 2 / 3”
      `flex:1 min-height:0 display:flex flex-direction:column padding:0 20px`
  - [ ] **div** — “소개 2 / 3”
        `display:flex align-items:center justify-content:space-between gap:8px height:56px margin-top:8px`
  - [ ] **div** — “항로”
        `margin-top:36px display:flex flex-direction:column gap:10px`
  - [ ] text 11px/600 — “항로”
        `display:block margin-top:30px font-size:11px font-weight:600 letter-spacing:0.07em color:#3556E6`
  - [ ] **h1** — “목표까지 얼마나 남았는지, 지금 무엇을 하면 되는지 알려줍니다.”
        `font-size:23px font-weight:700 letter-spacing:-0.03em line-height:1.4 color:#101828`
  - [ ] **div** — “다음”
        `margin-top:auto display:flex flex-direction:column gap:16px`

## IntroDestination — 첫 실행 · 소개 3 목적지

`canvas/IntroDestination.dc.html` · 390×844 · 원본 `v4 미구현 · plan/v4-stocks.md §3` · 렌더 `preview/IntroDestination.png`

- [ ] **div** — “소개 3 / 3”
      `flex:1 min-height:0 display:flex flex-direction:column padding:0 20px`
  - [ ] **div** — “소개 3 / 3”
        `display:flex align-items:center justify-content:space-between gap:8px height:56px margin-top:8px`
  - [ ] **div** — “목적지”
        `margin-top:36px display:flex flex-direction:column gap:10px`
  - [ ] text 11px/600 — “목적지”
        `display:block margin-top:30px font-size:11px font-weight:600 letter-spacing:0.07em color:#3556E6`
  - [ ] **h1** — “비상금 · 투자 · 상환, 언제 도착할지 날짜로 알려줍니다.”
        `font-size:23px font-weight:700 letter-spacing:-0.03em line-height:1.4 color:#101828`
  - [ ] **div** — “다음”
        `margin-top:auto display:flex flex-direction:column gap:16px`

## HomeSetup — 첫 실행 · 홈 구성

`canvas/HomeSetup.dc.html` · 390×844 · 원본 `v4 미구현 · plan/v4-stocks.md §3` · 렌더 `preview/HomeSetup.png`

- [ ] **div** — “홈 구성”
      `padding:0 20px`
- [ ] **div** — “홈에 무엇을 둘까요?”
      `flex:1 min-height:0 padding:0 20px`
  - [ ] **div** — “홈에 무엇을 둘까요?”
        `display:flex flex-direction:column margin-top:0px`
- [ ] **div** — “이 구성으로 시작”
      `padding:8px 20px 24px display:flex flex-direction:column gap:8px`

## HomeConfigured — 홈 · 첫 실행 구성 반영

`canvas/HomeConfigured.dc.html` · 390×844 · 원본 `v4 미구현 · plan/v4-stocks.md §3` · 렌더 `preview/HomeConfigured.png`

- [ ] **Header** — “NAVI”
      `display:flex flex-direction:column gap:6px padding:12px 16px 10px`
- [ ] **본문(스크롤 영역)** — “현재 위치”
      `flex:1 min-height:0 display:flex flex-direction:column gap:8px padding:0 14px`
  - [ ] **HeroCard** — “현재 위치”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **Card(18)** — “이번 달 달력”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 14px 13px`
  - [ ] **TurnCard** — “다음 안내”
        `display:flex gap:12px background:#FFFFFF border:1px solid #E3E8F1 border-left:3px solid #DE8A2A border-radius:18px padding:13px 14px`
  - [ ] **Card(18)** — “이번 달 한도”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px`
  - [ ] **Card(18)** — “순자산”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:4px 14px`
  - [ ] **Card(18)** — “상환 계획”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:4px 14px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`

## DestGoals — 목적지 · 내 목적지 (5탭)

`canvas/DestGoals.dc.html` · 390×844 · 원본 `v4 미구현 · plan/v4-stocks.md §4·§5` · 렌더 `preview/DestGoals.png`

- [ ] **div** — “목적지”
      `display:flex flex-direction:column gap:10px padding:14px 16px 12px`
- [ ] **본문(스크롤 영역)** — “월 저축 배분”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **HeroCard** — “월 저축 배분”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:15px 16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **Card(18)** — “진행 중인 목적지”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px 8px`
  - [ ] **div** — “새 목적지 설계”
        `display:flex align-items:center justify-content:center gap:6px height:46px border-radius:14px border:1.5px dashed #B9C3D6 background:rgba(255,255,255,.55) color:#3556E6 font-size:14px font-weight:600`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`

## DestFuture — 목적지 · 자산 경로 (5탭)

`canvas/DestFuture.dc.html` · 390×844 · 원본 `v4 미구현 · plan/v4-stocks.md §4·§5` · 렌더 `preview/DestFuture.png`

- [ ] **div** — “목적지”
      `display:flex flex-direction:column gap:10px padding:14px 16px 12px`
- [ ] **본문(스크롤 영역)** — “기간”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **HeroCard** — “기간”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:14px 14px 13px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **Card(18)** — “다음 자산 지점”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px 4px`
  - [ ] **Card(18)** — “저장되지 않는 가정”
        `background:#FFFFFF border:1px dashed #B79BFF border-radius:18px padding:11px 14px 11px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`

## HomeStocksOff — 홈 · 주식 꺼짐 (4탭)

`canvas/HomeStocksOff.dc.html` · 390×844 · 원본 `v4 미구현 · plan/v4-stocks.md §4·§5` · 렌더 `preview/HomeStocksOff.png`

- [ ] **본문(스크롤 영역)** — “현재 위치”
      `flex:1 min-height:0 display:flex flex-direction:column gap:8px justify-content:flex-end padding:0 14px 27px`
  - [ ] **HeroCard** — “현재 위치”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **Card(18)** — “이번 달 달력”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 14px 13px`
  - [ ] **TurnCard** — “다음 안내”
        `display:flex gap:12px background:#FFFFFF border:1px solid #E3E8F1 border-left:3px solid #DE8A2A border-radius:18px padding:13px 14px`
  - [ ] **Card(18)** — “이번 달 한도”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px`
  - [ ] **Card(18)** — “순자산”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:4px 14px`
  - [ ] **Card(18)** — “상환 계획”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:4px 14px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`

## StocksMine — 주식 · 내 종목

`canvas/StocksMine.dc.html` · 390×844 · 원본 `v4 미구현 · plan/v4-stocks.md §4·§5` · 렌더 `preview/StocksMine.png`

- [ ] **div** — “주식”
      `display:flex flex-direction:column gap:10px padding:14px 16px 12px`
- [ ] **본문(스크롤 영역)** — “이번 달 저축·투자 여력”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **div** — “이번 달 저축·투자 여력”
        `display:flex align-items:center gap:10px padding:10px 14px background:#E9EDFD border-radius:14px`
  - [ ] **Card(18)** — “보유”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px 8px`
  - [ ] **Card(18)** — “관심”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px 6px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`

## HoldingAdd — 모달 · 보유 기록

`canvas/HoldingAdd.dc.html` · 390×844 · 원본 `v4 미구현 · plan/v4-stocks.md §4·§5` · 렌더 `preview/HoldingAdd.png`

- [ ] **div** — “배경을 눌러 닫기”
      `height:60px display:flex align-items:flex-end justify-content:center`
- [ ] **BottomSheet** — “보유 기록”
      `flex:1 min-height:0 background:#FFFFFF border-radius:26px 26px 0 0 display:flex flex-direction:column color:#101828`
  - [ ] **div**
        `display:flex justify-content:center padding:9px 0 0`
  - [ ] **div** — “보유 기록”
        `display:flex align-items:flex-start justify-content:space-between gap:10px padding:12px 18px 14px border-bottom:1px solid #EFF2F8`
  - [ ] **div** — “종목”
        `flex:1 min-height:0 padding:14px 18px 14px display:flex flex-direction:column gap:15px`
    - [ ] **div** — “종목”
          `flex:0 0 auto`
    - [ ] **div** — “수량”
          `display:flex gap:10px`
    - [ ] **div** — “종가”
          `display:flex gap:10px`
    - [ ] **Callout(info)** — “종가는 직접 넣는 값이라 실시간 시세가 아니에요. 가격 옆에는 늘 이 기준일이 붙습니다.”
          `display:flex gap:8px padding:10px 11px background:#F4F6FB border-radius:12px`
    - [ ] **div** — “연결 계좌”
          `flex:0 0 auto`
    - [ ] **div** — “계좌 평가액에 반영”
          `display:flex align-items:center justify-content:space-between gap:10px padding:12px 13px background:#F4F6FB border-radius:14px`
  - [ ] **div** — “취소”
        `display:flex gap:10px padding:12px 18px 20px border-top:1px solid #EFF2F8`

## StocksEmpty — 주식 · 빈 상태

`canvas/StocksEmpty.dc.html` · 390×844 · 원본 `v4 미구현 · plan/v4-stocks.md §4·§5` · 렌더 `preview/StocksEmpty.png`

- [ ] **div** — “주식”
      `display:flex flex-direction:column gap:10px padding:14px 16px 12px`
- [ ] **본문(스크롤 영역)** — “이번 달 저축·투자 여력”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **div** — “이번 달 저축·투자 여력”
        `display:flex align-items:center gap:10px padding:10px 14px background:#E9EDFD border-radius:14px`
  - [ ] **Card(18)** — “아직 기록한 종목이 없어요”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:4px 14px`
  - [ ] **Card(18)** — “이 화면에 없는 것”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`

## HomeStocksCard — 홈 · 주식 요약 카드

`canvas/HomeStocksCard.dc.html` · 390×844 · 원본 `v4 미구현 · plan/v4-stocks.md §4·§5` · 렌더 `preview/HomeStocksCard.png`

- [ ] **본문(스크롤 영역)** — “현재 위치”
      `flex:1 min-height:0 display:flex flex-direction:column gap:8px justify-content:flex-end padding:0 14px 27px`
  - [ ] **HeroCard** — “현재 위치”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **Card(18)** — “이번 달 달력”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 14px 13px`
  - [ ] **TurnCard** — “다음 안내”
        `display:flex gap:12px background:#FFFFFF border:1px solid #E3E8F1 border-left:3px solid #DE8A2A border-radius:18px padding:13px 14px`
  - [ ] **Card(18)** — “주식 요약”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:4px 14px`
  - [ ] **Card(18)** — “이번 달 한도”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px`
  - [ ] **Card(18)** — “순자산”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:4px 14px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`

## StocksHome — 주식 · 둘러보기

`canvas/StocksHome.dc.html` · 390×844 · 원본 `v4 미구현 · plan/v4-stocks.md §4·§5` · 렌더 `preview/StocksHome.png`

- [ ] **div** — “주식”
      `display:flex flex-direction:column gap:10px padding:14px 16px 12px`
- [ ] **본문(스크롤 영역)** — “이번 달 저축·투자 여력”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **div** — “이번 달 저축·투자 여력”
        `display:flex align-items:center gap:10px padding:10px 14px background:#E9EDFD border-radius:14px`
  - [ ] **Callout(warn)** — “비상금이 68%예요. 투자보다 비상금을 먼저 채우는 걸 권해요.”
        `display:flex align-items:center gap:8px padding:9px 12px background:#FDF1E0 border-radius:12px`
  - [ ] **Card(18)** — “내 종목”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:4px 14px`
  - [ ] **div** — “성장”
        `display:grid grid-template-columns:repeat(2, minmax(0, 1fr)) gap:10px`
  - [ ] **p** — “데이터 기준일 2026-09-04 종가 · 설정에서 새로 받기 기준에 맞는 종목을 보여주는 것”
        `font-size:11px line-height:1.5 color:#626D88`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`

## StockListGrowth — 주식 · 성장주 목록

`canvas/StockListGrowth.dc.html` · 390×844 · 원본 `v4 미구현 · plan/v4-stocks.md §4·§5` · 렌더 `preview/StockListGrowth.png`

- [ ] **div** — “성장주”
      `display:flex align-items:center gap:6px padding:12px 12px 12px`
- [ ] **본문(스크롤 영역)** — “매출 성장”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **div** — “매출 성장”
        `display:flex flex-direction:column gap:9px`
  - [ ] **Card(18)** — “삼성전자”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:2px 14px 0`
  - [ ] **p** — “데이터 기준일 2026-09-04 종가 · 설정에서 새로 받기 기준에 맞는 종목을 보여주는 것”
        `font-size:11px line-height:1.5 color:#626D88`

## StockListDividend — 주식 · 배당주 목록

`canvas/StockListDividend.dc.html` · 390×844 · 원본 `v4 미구현 · plan/v4-stocks.md §4·§5` · 렌더 `preview/StockListDividend.png`

- [ ] **div** — “배당주”
      `display:flex align-items:center gap:6px padding:12px 12px 12px`
- [ ] **본문(스크롤 영역)** — “높은 배당수익률”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **div** — “높은 배당수익률”
        `display:flex flex-direction:column gap:9px`
  - [ ] **Card(18)** — “KT&G”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:2px 14px 0`
  - [ ] **p** — “데이터 기준일 2026-09-04 종가 · 설정에서 새로 받기 기준에 맞는 종목을 보여주는 것”
        `font-size:11px line-height:1.5 color:#626D88`

## StockDetail — 주식 · 종목 상세

`canvas/StockDetail.dc.html` · 390×844 · 원본 `v4 미구현 · plan/v4-stocks.md §4·§5` · 렌더 `preview/StockDetail.png`

- [ ] **div** — “삼성전자”
      `display:flex align-items:center gap:6px padding:12px 12px 12px`
- [ ] **본문(스크롤 영역)** — “71,200”
      `flex:1 min-height:0 display:flex flex-direction:column gap:8px padding:0 14px 12px`
  - [ ] **HeroCard** — “71,200”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:12px 14px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **Card(18)** — “성장주 목록에 있는 이유”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px 4px`
  - [ ] **Card(18)** — “연 매출”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:11px 14px`
  - [ ] **Card(18)** — “저장되지 않는 가정”
        `background:#FFFFFF border:1px dashed #B79BFF border-radius:18px padding:12px 14px`
- [ ] **div** — “관심 추가”
      `display:flex gap:8px padding:10px 14px 20px background:#FFFFFF border-top:1px solid #E3E8F1`

## StockThemes — 주식 · 테마

`canvas/StockThemes.dc.html` · 390×844 · 원본 `v4 미구현 · plan/v4-stocks.md §4·§5` · 렌더 `preview/StockThemes.png`

- [ ] **div** — “테마”
      `display:flex align-items:center gap:6px padding:12px 12px 12px`
- [ ] **본문(스크롤 영역)** — “테마는 기준으로 거른 목록이 아니라 예요. 한 종목이 여러 테마에 들어갈 수 있어요.”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **Callout(info)** — “테마는 기준으로 거른 목록이 아니라 예요. 한 종목이 여러 테마에 들어갈 수 있어요.”
        `display:flex gap:8px padding:10px 11px background:#F4F6FB border-radius:12px`
  - [ ] **div** — “반도체”
        `display:grid grid-template-columns:repeat(2, minmax(0, 1fr)) gap:8px`
  - [ ] **p** — “데이터 기준일 2026-09-04 종가 · 설정에서 새로 받기 기준에 맞는 종목을 보여주는 것”
        `font-size:11px line-height:1.5 color:#626D88`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`

## StockStates — 참고 · 주식 탭 특수한 상황 6가지

`canvas/StockStates.dc.html` · 1180×880 · 원본 `v4 미구현 · plan/v4-stocks.md §4·§5` · 렌더 `preview/StockStates.png`

- [ ] text 11px/600 — “구현 참고 · 앱 화면이 아닙니다”
      `font-size:11px font-weight:600 letter-spacing:0.02em color:#475467 border:1px solid #E3E8F1 background:#FFFFFF border-radius:99px padding:4px 10px`
- [ ] text 20px/700 — “주식 탭 · 특수한 상황 6가지”
      `font-size:20px font-weight:700 letter-spacing:-0.025em color:#101828`
- [ ] text 13px/400 — “경고 띠는 알려주기만 하고 아무것도 막지 않아요. 자료가 없는 기준은 —로 두고 충족 수에서 ”
      `font-size:13px line-height:1.55 color:#626D88`
- [ ] **div** — “주식 홈 · 위쪽”
      `display:flex gap:28px align-items:flex-start`

## StockSettings — 모달 · 설정 › 주식

`canvas/StockSettings.dc.html` · 390×844 · 원본 `v4 미구현 · plan/v4-stocks.md §4·§5` · 렌더 `preview/StockSettings.png`

- [ ] **div** — “배경을 눌러 닫기”
      `height:60px display:flex align-items:flex-end justify-content:center`
- [ ] **BottomSheet** — “주식”
      `flex:1 min-height:0 background:#FFFFFF border-radius:26px 26px 0 0 display:flex flex-direction:column color:#101828`
  - [ ] **div**
        `display:flex justify-content:center padding:9px 0 0`
  - [ ] **div** — “주식”
        `display:flex align-items:flex-start justify-content:space-between gap:10px padding:12px 18px 14px border-bottom:1px solid #EFF2F8`
  - [ ] **div** — “종목 데이터”
        `flex:1 min-height:0 padding:14px 18px 0 display:flex flex-direction:column gap:15px`
    - [ ] **div** — “종목 데이터”
    - [ ] **div** — “기준값”
    - [ ] **div** — “기능”
  - [ ] **div** — “취소”
        `display:flex gap:10px padding:12px 18px 20px border-top:1px solid #EFF2F8`

## SnapshotUpdate — 참고 · 종목 데이터 새로 받기

`canvas/SnapshotUpdate.dc.html` · 1180×762 · 원본 `v4 미구현 · plan/v4-stocks.md §4·§5` · 렌더 `preview/SnapshotUpdate.png`

- [ ] text 11px/600 — “구현 참고 · 앱 화면이 아닙니다”
      `font-size:11px font-weight:600 letter-spacing:0.02em color:#475467 border:1px solid #E3E8F1 background:#FFFFFF border-radius:99px padding:4px 10px`
- [ ] text 20px/700 — “종목 데이터 새로 받기 · 순서대로”
      `font-size:20px font-weight:700 letter-spacing:-0.025em color:#101828`
- [ ] text 13px/400 — “주식 설정에서 [새로 받기]를 누르면 이 순서로 바뀌어요. 받다가 실패해도 지금 데이터로 그대”
      `font-size:13px line-height:1.55 color:#626D88`
- [ ] **div** — “시작 · 주식 설정에서 [새로 받기]를 누르면”
      `display:flex gap:28px align-items:flex-start`

## DaySheet — 하루 시트 · 오늘 (키보드 열림)

`canvas/DaySheet.dc.html` · 390×844 · 원본 `v5 미구현 · plan/v5-calendar.md §4·§5-4·§3-4` · 렌더 `preview/DaySheet.png`

- [ ] **div** — “배경을 눌러 닫기 · 앱이 다시 시작되면 저장하지 않은 내용은 사라져요”
      `height:60px display:flex align-items:flex-end justify-content:center padding:0 20px 12px text-align:center`
- [ ] **BottomSheet** — “9월 8일 소비 기록”
      `flex:1 min-height:0 background:#FFFFFF border-radius:26px 26px 0 0 display:flex flex-direction:column`
  - [ ] **div**
        `display:flex justify-content:center padding:9px 0 0`
  - [ ] **div** — “9월 8일 소비 기록”
        `display:flex align-items:flex-start justify-content:space-between gap:10px padding:12px 18px 12px border-bottom:1px solid #EFF2F8`
  - [ ] **div** — “금액”
        `flex:1 min-height:0 padding:12px 18px 0 display:flex flex-direction:column gap:10px`
    - [ ] **div** — “금액”
          `display:flex align-items:center justify-content:space-between gap:10px height:48px padding:0 14px border-radius:12px background:#FFFFFF border:1.5px solid #3556E6 box-shadow:0 0 0 3px rgba(53,86,230,.16)`
    - [ ] **div** — “· 저장을 눌러야 기록돼요”
          `font-size:11.5px line-height:1.45 color:#626D88 padding:0 2px`
    - [ ] **div** — “메모”
          `display:flex align-items:center justify-content:space-between gap:10px height:44px padding:0 14px border-radius:12px background:#FFFFFF border:1px solid #CFD7E6`
    - [ ] **div** — “분류”
          `display:flex flex-direction:column gap:8px`
    - [ ] **div** — “최근 기록”
          `display:flex flex-direction:column gap:8px`
    - [ ] **div** — “저장”
          `margin-top:2px`
    - [ ] **div** — “저축·투자로 기록 ›”
- [ ] **div** — “시스템 숫자 키보드 자리”
      `position:absolute left:0 right:0 bottom:0 height:280px background:#E8ECF5 border-top:1px solid #D7DEEA display:flex align-items:center justify-content:center flex-direction:column gap:4px`

## DaySheetList — 하루 시트 · 기록 있는 과거 날 (목록 우선)

`canvas/DaySheetList.dc.html` · 390×844 · 원본 `v5 미구현 · plan/v5-calendar.md §4·§5-4·§3-4` · 렌더 `preview/DaySheetList.png`

- [ ] **div** — “배경을 눌러 닫기 · 앱이 다시 시작되면 저장하지 않은 내용은 사라져요”
      `height:60px display:flex align-items:flex-end justify-content:center padding:0 20px 12px text-align:center`
- [ ] **BottomSheet** — “9월 3일 소비 기록”
      `flex:1 min-height:0 background:#FFFFFF border-radius:26px 26px 0 0 display:flex flex-direction:column`
  - [ ] **div**
        `display:flex justify-content:center padding:9px 0 0`
  - [ ] **div** — “9월 3일 소비 기록”
        `display:flex align-items:flex-start justify-content:space-between gap:10px padding:12px 18px 12px border-bottom:1px solid #EFF2F8`
  - [ ] **div** — “교통”
        `flex:1 min-height:0 padding:14px 18px 0 display:flex flex-direction:column gap:12px`
    - [ ] **div** — “교통”
          `display:flex flex-direction:column gap:8px`
    - [ ] **div** — “추가”
          `display:flex align-items:center justify-content:center gap:6px height:46px border-radius:14px border:1.5px dashed #B9C3D6 background:rgba(255,255,255,.55) color:#3556E6 font-size:14px font-weight:600`
    - [ ] **div** — “저축·투자로 기록 ›”
    - [ ] **div** — “9월 3일 다 적었어요”
          `margin-top:auto`

## DaySheetEdit — 하루 시트 · 수정 모드

`canvas/DaySheetEdit.dc.html` · 390×844 · 원본 `v5 미구현 · plan/v5-calendar.md §4·§5-4·§3-4` · 렌더 `preview/DaySheetEdit.png`

- [ ] **div** — “배경을 눌러 닫기 · 앱이 다시 시작되면 저장하지 않은 내용은 사라져요”
      `height:60px display:flex align-items:flex-end justify-content:center padding:0 20px 12px text-align:center`
- [ ] **BottomSheet** — “9월 3일 기록 수정”
      `flex:1 min-height:0 background:#FFFFFF border-radius:26px 26px 0 0 display:flex flex-direction:column`
  - [ ] **div**
        `display:flex justify-content:center padding:9px 0 0`
  - [ ] **div** — “9월 3일 기록 수정”
        `display:flex align-items:flex-start justify-content:space-between gap:10px padding:12px 18px 12px border-bottom:1px solid #EFF2F8`
  - [ ] **div** — “금액”
        `flex:1 min-height:0 padding:14px 18px 0 display:flex flex-direction:column gap:12px`
    - [ ] **div** — “금액”
          `display:flex align-items:center justify-content:space-between gap:10px height:48px padding:0 14px border-radius:12px background:#FFFFFF border:1.5px solid #3556E6 box-shadow:0 0 0 3px rgba(53,86,230,.16)`
    - [ ] **div** — “4.5만원”
          `font-size:11.5px line-height:1.45 color:#626D88 padding:0 2px`
    - [ ] **div** — “메모”
          `display:flex align-items:center justify-content:space-between gap:10px height:44px padding:0 14px border-radius:12px background:#FFFFFF border:1px solid #CFD7E6`
    - [ ] **div** — “분류”
          `display:flex flex-direction:column gap:8px`
    - [ ] **div** — “저장”
          `display:flex gap:8px margin-top:2px`
- [ ] **div** — “시스템 숫자 키보드 자리”
      `position:absolute left:0 right:0 bottom:0 height:280px background:#E8ECF5 border-top:1px solid #D7DEEA display:flex align-items:center justify-content:center flex-direction:column gap:4px`

## DoneCard — 홈 · 저장 뒤 완료 카드

`canvas/DoneCard.dc.html` · 390×844 · 원본 `v5 미구현 · plan/v5-calendar.md §4·§5-4·§3-4` · 렌더 `preview/DoneCard.png`

- [ ] **Header** — “NAVI”
      `display:flex flex-direction:column gap:6px padding:12px 16px 10px`
- [ ] **본문(스크롤 영역)** — “현재 위치”
      `flex:1 min-height:0 display:flex flex-direction:column gap:9px padding:0 14px position:relative`
  - [ ] **HeroCard** — “현재 위치”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **Card(18)** — “이번 달 달력”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 14px 13px`
  - [ ] **TurnCard** — “다음 안내”
        `display:flex gap:12px background:#FFFFFF border:1px solid #E3E8F1 border-left:3px solid #DE8A2A border-radius:18px padding:13px 14px`
  - [ ] **Card(18)** — “이번 달 한도”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px`
  - [ ] **Card(18)** — “순자산”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:4px 14px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`
- [ ] **div** — “저장했어요”
      `position:absolute left:14px right:14px bottom:78px background:#101828 border-radius:16px padding:13px 14px 12px color:#FFFFFF box-shadow:0 8px 24px rgba(0,0,0,.28)`

## DaySheetConfirm — 참고 · 저장을 한 번 더 물어보는 경우

`canvas/DaySheetConfirm.dc.html` · 1200×900 · 원본 `v5 미구현 · plan/v5-calendar.md §4·§5-4·§3-4` · 렌더 `preview/DaySheetConfirm.png`

- [ ] text 11px/600 — “구현 참고 · 앱 화면이 아닙니다”
      `font-size:11px font-weight:600 letter-spacing:0.02em color:#475467 border:1px solid #E3E8F1 background:#FFFFFF border-radius:99px padding:4px 10px`
- [ ] text 20px/700 — “저장을 눌렀는데 한 번 더 물어보는 경우”
      `font-size:20px font-weight:700 letter-spacing:-0.025em color:#101828`
- [ ] text 13px/400 — “아래 네 경우에는 바로 저장하지 않고 금액 칸 아래에 안내가 한 줄 뜹니다. 저장을 한 번 더”
      `font-size:13px line-height:1.55 color:#626D88`
- [ ] **div** — “오늘 4건 37,000원”
      `display:flex gap:32px align-items:flex-start`
- [ ] **Card(18)** — “구현 메모”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:10px 18px 8px`

## ClassifySheet — 분류하기 시트

`canvas/ClassifySheet.dc.html` · 390×844 · 원본 `v5 미구현 · plan/v5-calendar.md §4·§5-4·§3-4` · 렌더 `preview/ClassifySheet.png`

- [ ] **div** — “배경을 눌러 닫기”
      `height:60px display:flex align-items:flex-end justify-content:center padding:0 20px 12px text-align:center`
- [ ] **BottomSheet** — “분류하기 · 7건”
      `flex:1 min-height:0 background:#FFFFFF border-radius:26px 26px 0 0 display:flex flex-direction:column`
  - [ ] **div**
        `display:flex justify-content:center padding:9px 0 0`
  - [ ] **div** — “분류하기 · 7건”
        `display:flex align-items:flex-start justify-content:space-between gap:10px padding:12px 18px 14px border-bottom:1px solid #EFF2F8`
  - [ ] **div** — “커피”
        `flex:1 min-height:0 padding:6px 18px 0 display:flex flex-direction:column`
    - [ ] **div** — “커피”
          `display:flex align-items:center gap:10px height:52px border-bottom:1px solid #F3F5FA`
    - [ ] **div** — “9월 1일”
          `background:#F4F6FB border-radius:0 0 12px 12px padding:0 10px 2px`
    - [ ] **div** — “간식”
          `display:flex align-items:center gap:10px height:52px border-bottom:1px solid #F3F5FA`
    - [ ] **div** — “버스”
          `display:flex align-items:center gap:10px height:52px border-bottom:1px solid #F3F5FA`
    - [ ] **div** — “편의점”
          `display:flex align-items:center gap:10px height:52px border-bottom:1px solid #F3F5FA`
    - [ ] **div** — “분류 안 함 기록”
          `display:flex align-items:center gap:10px height:52px`
  - [ ] **div** — “2건 저장”
        `padding:12px 18px 20px border-top:1px solid #EFF2F8 display:flex flex-direction:column gap:8px`

## HeroInsufficient — 홈 · 히어로 이력 부족

`canvas/HeroInsufficient.dc.html` · 390×844 · 원본 `v5 미구현 · plan/v5-calendar.md §4·§5-4·§3-4` · 렌더 `preview/HeroInsufficient.png`

- [ ] **Header** — “NAVI”
      `display:flex flex-direction:column gap:6px padding:12px 16px 10px`
- [ ] **본문(스크롤 영역)** — “이번 달 기록한 소비”
      `flex:1 min-height:0 display:flex flex-direction:column gap:9px padding:0 14px`
  - [ ] **HeroCard** — “이번 달 기록한 소비”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **Card(18)** — “이번 달 달력”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 14px 13px`
  - [ ] **Card(18)** — “다음 안내”
        `display:flex gap:12px background:#FFFFFF border:1px solid #E3E8F1 border-left:3px solid #7EC4E8 border-radius:18px padding:13px 14px`
  - [ ] **Card(18)** — “이번 달 한도”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`

## DaySheet360 — 하루 시트 · 360 × 640 작은 폰

`canvas/DaySheet360.dc.html` · 360×640 · 원본 `v5 미구현 · plan/v5-calendar.md §4·§5-4·§3-4` · 렌더 `preview/DaySheet360.png`

- [ ] **div** — “배경을 눌러 닫기 · 앱이 다시 시작되면 저장하지 않은 내용은 사라져요”
      `height:60px display:flex align-items:flex-end justify-content:center padding:0 20px 12px text-align:center`
- [ ] **BottomSheet** — “9월 8일 소비 기록”
      `flex:1 min-height:0 background:#FFFFFF border-radius:26px 26px 0 0 display:flex flex-direction:column`
  - [ ] **div**
        `display:flex justify-content:center padding:9px 0 0`
  - [ ] **div** — “9월 8일 소비 기록”
        `display:flex align-items:flex-start justify-content:space-between gap:10px padding:12px 18px 12px border-bottom:1px solid #EFF2F8`
  - [ ] **div** — “최근 기록”
        `flex:1 min-height:0 padding:12px 14px 0 display:flex flex-direction:column gap:10px`
    - [ ] **div** — “최근 기록”
    - [ ] **div** — “저축·투자로 기록 ›”
    - [ ] **div** — “오늘 기록”
          `display:flex flex-direction:column`
    - [ ] **div** — “9월 8일 다 적었어요”
  - [ ] **div** — “저장”
        `padding:10px 14px 14px border-top:1px solid #EFF2F8 background:#FFFFFF`

## HeroFootnotes — 참고 · 홈 맨 위 카드의 안내 줄

`canvas/HeroFootnotes.dc.html` · 1200×640 · 원본 `v5 미구현 · plan/v5-calendar.md §4·§5-4·§3-4` · 렌더 `preview/HeroFootnotes.png`

- [ ] text 11px/600 — “구현 참고 · 앱 화면이 아닙니다”
      `font-size:11px font-weight:600 letter-spacing:0.02em color:#475467 border:1px solid #E3E8F1 background:#FFFFFF border-radius:99px padding:4px 10px`
- [ ] text 20px/700 — “홈 맨 위 카드에 붙는 작은 안내 줄”
      `font-size:20px font-weight:700 letter-spacing:-0.025em color:#101828`
- [ ] text 13px/400 — “예상 소비를 계산한 방식에 덧붙일 말이 있을 때만 기준 조정 줄 아래에 회색 글이 한두 줄 붙”
      `font-size:13px line-height:1.55 color:#626D88`
- [ ] **div** — “현재 위치”
      `display:flex gap:32px align-items:flex-start`
- [ ] **p** — “오른쪽 견본은 카드의 만 잘라 보여 줍니다. 카드의 나머지는 네 경우 모두 같고, 안내 줄이 ”
      `font-size:12px line-height:1.6 color:#626D88`

## HomeCalendarStrip — 홈 · 달력 접힘 (최근 7일)

`canvas/HomeCalendarStrip.dc.html` · 390×844 · 원본 `v5 미구현 · plan/v5-calendar.md §3` · 렌더 `preview/HomeCalendarStrip.png`

- [ ] **Header** — “NAVI”
      `display:flex flex-direction:column gap:6px padding:12px 16px 10px`
- [ ] **본문(스크롤 영역)** — “현재 위치”
      `flex:1 min-height:0 display:flex flex-direction:column gap:9px padding:0 14px`
  - [ ] **HeroCard** — “현재 위치”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **Card(18)** — “이번 달 달력”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 14px 13px`
  - [ ] **TurnCard** — “다음 안내”
        `display:flex gap:12px background:#FFFFFF border:1px solid #E3E8F1 border-left:3px solid #DE8A2A border-radius:18px padding:13px 14px`
  - [ ] **Card(18)** — “이번 달 한도”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px`
  - [ ] **Card(18)** — “68%”
        `display:flex align-items:center gap:12px background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`

## HomeCalendar — 홈 · 달력 펼침 (월 달력) · 3일 칸 누름

`canvas/HomeCalendar.dc.html` · 390×844 · 원본 `v5 미구현 · plan/v5-calendar.md §3` · 렌더 `preview/HomeCalendar.png`

- [ ] **본문(스크롤 영역)** — “2026년 9월”
      `flex:1 min-height:0 display:flex flex-direction:column gap:9px padding:0 14px`
  - [ ] **div**
        `height:22px background:#FFFFFF border:1px solid #E3E8F1 border-top:none border-radius:0 0 20px 20px opacity:.55`
  - [ ] **Card(18)** — “2026년 9월”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 14px 13px`
  - [ ] **TurnCard** — “다음 안내”
        `display:flex gap:12px background:#FFFFFF border:1px solid #E3E8F1 border-left:3px solid #DE8A2A border-radius:18px padding:13px 14px`
  - [ ] **Card(18)** — “이번 달 한도”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`

## HomeCalendar360 — 홈 · 달력 펼침 · 360px (월 달력 그대로)

`canvas/HomeCalendar360.dc.html` · 360×844 · 원본 `v5 미구현 · plan/v5-calendar.md §3` · 렌더 `preview/HomeCalendar360.png`

- [ ] **본문(스크롤 영역)** — “2026년 9월”
      `flex:1 min-height:0 display:flex flex-direction:column gap:9px padding:0 14px`
  - [ ] **div**
        `height:22px background:#FFFFFF border:1px solid #E3E8F1 border-top:none border-radius:0 0 20px 20px opacity:.55`
  - [ ] **Card(18)** — “2026년 9월”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 10px 13px`
  - [ ] **TurnCard** — “다음 안내”
        `display:flex gap:12px background:#FFFFFF border:1px solid #E3E8F1 border-left:3px solid #DE8A2A border-radius:18px padding:13px 14px`
  - [ ] **Card(18)** — “이번 달 한도”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`

## HomeCalendarPrev — 홈 · 달력 펼침 · ‹ 지난달 8월 보기

`canvas/HomeCalendarPrev.dc.html` · 390×844 · 원본 `v5 미구현 · plan/v5-calendar.md §3` · 렌더 `preview/HomeCalendarPrev.png`

- [ ] **본문(스크롤 영역)** — “2026년 8월”
      `flex:1 min-height:0 display:flex flex-direction:column gap:9px padding:0 14px`
  - [ ] **div**
        `height:22px background:#FFFFFF border:1px solid #E3E8F1 border-top:none border-radius:0 0 20px 20px opacity:.55`
  - [ ] **Card(18)** — “2026년 8월”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 14px 13px`
  - [ ] **TurnCard** — “다음 안내”
        `display:flex gap:12px background:#FFFFFF border:1px solid #E3E8F1 border-left:3px solid #DE8A2A border-radius:18px padding:13px 14px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`

## CalendarCells — 참고 · 달력 칸 읽는 법

`canvas/CalendarCells.dc.html` · 1330×820 · 원본 `v5 미구현 · plan/v5-calendar.md §3` · 렌더 `preview/CalendarCells.png`

- [ ] text 11px/600 — “구현 참고 · 앱 화면이 아닙니다”
      `font-size:11px font-weight:600 letter-spacing:0.02em color:#475467 border:1px solid #E3E8F1 background:#FFFFFF border-radius:99px padding:4px 10px`
- [ ] text 20px/700 — “달력 칸 읽는 법”
      `font-size:20px font-weight:700 letter-spacing:-0.025em color:#101828`
- [ ] text 13px/400 — “칸의 숫자는 그날 소비 합계입니다(고정비 포함 · 이체 제외). 왼쪽 달력의 번호를 가운데에서”
      `font-size:13px line-height:1.55 color:#626D88`
- [ ] **div** — “2026년 9월”
      `display:flex gap:28px align-items:flex-start`

## CalendarGridSizes — 참고 · 달력을 펼치면 어디서나 월 달력

`canvas/CalendarGridSizes.dc.html` · 1150×1490 · 원본 `v5 미구현 · plan/v5-calendar.md §3` · 렌더 `preview/CalendarGridSizes.png`

- [ ] text 11px/600 — “구현 참고 · 앱 화면이 아닙니다”
      `font-size:11px font-weight:600 letter-spacing:0.02em color:#475467 border:1px solid #E3E8F1 background:#FFFFFF border-radius:99px padding:4px 10px`
- [ ] text 20px/700 — “달력을 펼치면 어디서나 월 달력”
      `font-size:20px font-weight:700 letter-spacing:-0.025em color:#101828`
- [ ] text 13px/400 — “화면이 좁아도, 글자를 크게 써도 날짜를 세로로 늘어놓은 목록으로 바뀌지 않습니다. 접어 둔 ”
      `font-size:13px line-height:1.55 color:#626D88`
- [ ] **div** — “가장 좁은 폰”
      `display:flex gap:36px align-items:flex-start`
- [ ] **div** — “가장 좁은 폰에서 지난달을 볼 때”
      `display:flex gap:36px align-items:flex-start margin-top:26px`
- [ ] **div** — “구현 메모”
      `margin-top:24px display:flex flex-direction:column gap:4px`

## DesktopHomeV5 — 데스크톱 · 홈

`canvas/DesktopHomeV5.dc.html` · 1440×1000 · 원본 `v5 · 데스크톱 달력 자리(2026-09-21 결정 · plan/v5-calendar.md §10 10판 메모)` · 렌더 `preview/DesktopHomeV5.png`

- [ ] **div** — “NAVI”
      `width:232px background:#FFFFFF display:flex flex-direction:column padding:22px 16px 18px`
- [ ] **div** — “샘플 데이터로 둘러보는 중 · 표시된 이름과 금액은 실제 정보가 아닙니다”
      `flex:1 display:flex flex-direction:column padding:18px 28px 22px`
  - [ ] **div** — “샘플 데이터로 둘러보는 중 · 표시된 이름과 금액은 실제 정보가 아닙니다”
        `display:flex align-items:center justify-content:space-between gap:12px height:38px padding:0 16px background:#E9EDFD border-radius:12px`
  - [ ] **div** — “2026년 9월 8일 · 이번 달 22일 남음”
        `display:flex align-items:flex-end justify-content:space-between gap:12px margin-top:18px`
  - [ ] **div** — “현재 위치”
        `display:grid grid-template-columns:minmax(0, 1.6fr) minmax(0, 1fr) gap:18px margin-top:16px align-items:start`

## HomeSetupStocksOn — 첫 실행 · 홈 구성 · 주식 켬

`canvas/HomeSetupStocksOn.dc.html` · 390×844 · 원본 `v4 미구현 · plan/v4-stocks.md §3` · 렌더 `preview/HomeSetupStocksOn.png`

- [ ] **div** — “홈 구성”
      `padding:0 20px`
- [ ] **div** — “홈에 무엇을 둘까요?”
      `flex:1 min-height:0 padding:0 20px`
  - [ ] **div** — “홈에 무엇을 둘까요?”
        `display:flex flex-direction:column margin-top:-83px`
- [ ] **div** — “이 구성으로 시작”
      `padding:8px 20px 24px display:flex flex-direction:column gap:8px`

## SettingsHomeEntry — 설정 · 「홈 구성 ›」 행

`canvas/SettingsHomeEntry.dc.html` · 390×844 · 원본 `v4 미구현 · plan/v4-stocks.md §3 · plan/v5-calendar.md §12-2` · 렌더 `preview/SettingsHomeEntry.png`

- [ ] **div** — “배경을 눌러 닫기”
      `height:60px display:flex align-items:flex-end justify-content:center`
- [ ] **BottomSheet** — “내 수치 입력”
      `flex:1 min-height:0 background:#FFFFFF border-radius:26px 26px 0 0 display:flex flex-direction:column color:#101828`
  - [ ] **div**
        `display:flex justify-content:center padding:9px 0 0`
  - [ ] **div** — “내 수치 입력”
        `display:flex align-items:flex-start justify-content:space-between gap:10px padding:12px 18px 14px border-bottom:1px solid #EFF2F8`
  - [ ] **div** — “소비 목표”
        `flex:1 min-height:0 padding:14px 18px 14px display:flex flex-direction:column justify-content:flex-end gap:15px`
    - [ ] **div** — “소비 목표”
    - [ ] **div** — “추가 설정”
    - [ ] **div** — “홈 화면”
    - [ ] **div** — “데이터”
  - [ ] **div** — “취소”
        `display:flex gap:10px padding:12px 18px 20px border-top:1px solid #EFF2F8`

## HomeLayoutEdit — 설정 › 홈 구성 (처음 실행 뒤에 다시 고칠 때)

`canvas/HomeLayoutEdit.dc.html` · 390×844 · 원본 `v4 미구현 · plan/v4-stocks.md §3 · plan/v5-calendar.md §12-2 · §7` · 렌더 `preview/HomeLayoutEdit.png`

- [ ] **div** — “홈 구성”
      `padding:0 20px`
- [ ] **div** — “소비율과 달력은 늘 맨 위에 있어요. 그 아래에 둘 카드를 4개까지 골라 주세요.”
      `flex:1 min-height:0 padding:0 20px`
  - [ ] **div** — “소비율과 달력은 늘 맨 위에 있어요. 그 아래에 둘 카드를 4개까지 골라 주세요.”
        `display:flex flex-direction:column margin-top:0px`
- [ ] **div** — “저장”
      `padding:8px 20px 24px display:flex flex-direction:column gap:8px`

## DestPayoff — 목적지 · 상환 계획

`canvas/DestPayoff.dc.html` · 390×844 · 원본 `v4 미구현 · plan/v4-stocks.md §4` · 렌더 `preview/DestPayoff.png`

- [ ] **div** — “목적지”
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

## DaySheetScrolled — 하루 시트 · 키보드를 내린 모습

`canvas/DaySheetScrolled.dc.html` · 390×844 · 원본 `v5 · plan/v5-calendar.md §4` · 렌더 `preview/DaySheetScrolled.png`

- [ ] **div** — “배경을 눌러 닫기 · 앱이 다시 시작되면 저장하지 않은 내용은 사라져요”
      `height:60px display:flex align-items:flex-end justify-content:center padding:0 20px 12px text-align:center`
- [ ] **BottomSheet** — “9월 8일 소비 기록”
      `flex:1 min-height:0 background:#FFFFFF border-radius:26px 26px 0 0 display:flex flex-direction:column`
  - [ ] **div**
        `display:flex justify-content:center padding:9px 0 0`
  - [ ] **div** — “9월 8일 소비 기록”
        `display:flex align-items:flex-start justify-content:space-between gap:10px padding:12px 18px 12px border-bottom:1px solid #EFF2F8`
  - [ ] **div** — “금액”
        `flex:1 min-height:0 padding:12px 18px 0 display:flex flex-direction:column gap:10px`
    - [ ] **div** — “금액”
          `display:flex align-items:center justify-content:space-between gap:10px height:48px padding:0 14px border-radius:12px background:#FFFFFF border:1px solid #CFD7E6`
    - [ ] **div** — “· 저장을 눌러야 기록돼요”
          `font-size:11.5px line-height:1.45 color:#626D88 padding:0 2px`
    - [ ] **div** — “메모”
          `display:flex align-items:center justify-content:space-between gap:10px height:44px padding:0 14px border-radius:12px background:#FFFFFF border:1px solid #CFD7E6`
    - [ ] **div** — “분류”
          `display:flex flex-direction:column gap:8px`
    - [ ] **div** — “최근 기록”
          `display:flex flex-direction:column gap:8px`
    - [ ] **div** — “저장”
          `margin-top:2px`
    - [ ] **div** — “저축·투자로 기록 ›”
    - [ ] **div** — “오늘 기록”
          `margin-top:4px`
    - [ ] **div** — “9월 8일 다 적었어요”
          `margin-top:auto`

## DaySheetNoSpend — 하루 시트 · 소비 0건인 날 (오늘은 안 썼어요)

`canvas/DaySheetNoSpend.dc.html` · 390×844 · 원본 `v5 · plan/v5-calendar.md §4 · §8` · 렌더 `preview/DaySheetNoSpend.png`

- [ ] **div** — “배경을 눌러 닫기 · 앱이 다시 시작되면 저장하지 않은 내용은 사라져요”
      `height:60px display:flex align-items:flex-end justify-content:center padding:0 20px 12px text-align:center`
- [ ] **BottomSheet** — “9월 8일 소비 기록”
      `flex:1 min-height:0 background:#FFFFFF border-radius:26px 26px 0 0 display:flex flex-direction:column`
  - [ ] **div**
        `display:flex justify-content:center padding:9px 0 0`
  - [ ] **div** — “9월 8일 소비 기록”
        `display:flex align-items:flex-start justify-content:space-between gap:10px padding:12px 18px 12px border-bottom:1px solid #EFF2F8`
  - [ ] **div** — “금액”
        `flex:1 min-height:0 padding:12px 18px 0 display:flex flex-direction:column gap:10px`
    - [ ] **div** — “금액”
          `display:flex align-items:center justify-content:space-between gap:10px height:48px padding:0 14px border-radius:12px background:#FFFFFF border:1px solid #CFD7E6`
    - [ ] text 11.5px/400 — “금액을 넣거나, 안 썼으면 「오늘은 안 썼어요」로 표시해요”
          `font-size:11.5px line-height:1.45 color:#626D88 padding:0 2px`
    - [ ] **div** — “메모”
          `display:flex align-items:center justify-content:space-between gap:10px height:44px padding:0 14px border-radius:12px background:#FFFFFF border:1px solid #CFD7E6`
    - [ ] **div** — “분류”
          `display:flex flex-direction:column gap:8px`
    - [ ] **div** — “최근 기록”
          `display:flex flex-direction:column gap:8px`
    - [ ] **div** — “저장”
          `margin-top:2px`
    - [ ] **div** — “저축·투자로 기록 ›”
    - [ ] **div** — “오늘 기록”
          `position:relative margin-top:4px`
    - [ ] **div** — “오늘은 안 썼어요”
          `position:relative margin-top:auto`

## ReviewListSheet — 확인할 내용 목록 시트

`canvas/ReviewListSheet.dc.html` · 390×844 · 원본 `v5 · plan/v5-calendar.md §3-3` · 렌더 `preview/ReviewListSheet.png`

- [ ] **div** — “시안 주석 · 앱에는 보이지 않아요”
      `flex:1 min-height:0 display:flex flex-direction:column justify-content:center`
  - [ ] **div** — “시안 주석 · 앱에는 보이지 않아요”
        `padding:12px 14px border:1px dashed rgba(255,255,255,.32) border-radius:12px display:flex flex-direction:column gap:7px`
- [ ] **div** — “배경을 눌러 닫기”
      `height:60px display:flex align-items:flex-end justify-content:center padding:0 20px 12px text-align:center`
- [ ] **BottomSheet** — “확인할 내용 2개”
      `background:#FFFFFF border-radius:26px 26px 0 0 display:flex flex-direction:column`

## HomeDefaultScroll — 홈 · 기본 5카드 전체 스크롤

`canvas/HomeDefaultScroll.dc.html` · 390×1330 · 원본 `v5 · plan/v5-calendar.md §3-1 · §10 2단계` · 렌더 `preview/HomeDefaultScroll.png`

- [ ] **Header** — “NAVI”
      `display:flex flex-direction:column gap:6px padding:12px 16px 10px`
- [ ] **본문(스크롤 영역)** — “현재 위치”
      `flex:1 min-height:0 display:flex flex-direction:column gap:9px padding:0 14px 14px`
  - [ ] **HeroCard** — “현재 위치”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **Card(18)** — “이번 달 달력”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 14px 13px`
  - [ ] **TurnCard** — “다음 안내”
        `display:flex gap:12px background:#FFFFFF border:1px solid #E3E8F1 border-left:3px solid #DE8A2A border-radius:18px padding:13px 14px`
  - [ ] **Card(18)** — “이번 달 한도”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px`
  - [ ] **Card(18)** — “68%”
        `display:flex align-items:center gap:12px background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px`
  - [ ] **Card(18)** — “또래와 내 페이스”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`

## CalendarStatusLines — 참고 · 달력 아래 한 줄이 바뀌는 경우

`canvas/CalendarStatusLines.dc.html` · 1200×1050 · 원본 `v5 · plan/v5-calendar.md §3-3` · 렌더 `preview/CalendarStatusLines.png`

- [ ] text 11px/600 — “구현 참고 · 앱 화면이 아닙니다”
      `font-size:11px font-weight:600 letter-spacing:0.02em color:#475467 border:1px solid #E3E8F1 background:#FFFFFF border-radius:99px padding:4px 10px`
- [ ] text 20px/700 — “달력 아래 한 줄이 바뀌는 경우”
      `font-size:20px font-weight:700 letter-spacing:-0.025em color:#101828`
- [ ] text 13px/400 — “접어 둔 달력의 날짜 칸 아래에는 오늘 합계를 말하는 한 문장이 있습니다. 아래 경우에는 그 ”
      `font-size:13px line-height:1.55 color:#626D88`
- [ ] **div** — “이번 달 달력”
      `display:flex gap:32px align-items:flex-start`

## DaySheetStates — 참고 · 기록 창의 글이 바뀌는 경우

`canvas/DaySheetStates.dc.html` · 1210×1660 · 원본 `v5 · plan/v5-calendar.md §4 · §8` · 렌더 `preview/DaySheetStates.png`

- [ ] text 11px/600 — “구현 참고 · 앱 화면이 아닙니다”
      `font-size:11px font-weight:600 letter-spacing:0.02em color:#475467 border:1px solid #E3E8F1 background:#FFFFFF border-radius:99px padding:4px 10px`
- [ ] text 20px/700 — “기록 창의 글이 바뀌는 경우”
      `font-size:20px font-weight:700 letter-spacing:-0.025em color:#101828`
- [ ] text 13px/400 — “기록 창은 하나이고, 날짜 · 시간 · 입력한 값에 따라 아래 다섯 자리의 글과 모양만 바뀝니”
      `font-size:13px line-height:1.55 color:#626D88`
- [ ] **div** — “오늘 4건 37,000원”
      `display:flex gap:32px align-items:flex-start`
- [ ] **Card(18)** — “구현 메모”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:10px 18px 8px`

## DaySheetNoSpendStates — 참고 · 안 쓴 날을 표시하는 경우

`canvas/DaySheetNoSpendStates.dc.html` · 1200×1160 · 원본 `v5 · plan/v5-calendar.md §4 · §8` · 렌더 `preview/DaySheetNoSpendStates.png`

- [ ] text 11px/600 — “구현 참고 · 앱 화면이 아닙니다”
      `font-size:11px font-weight:600 letter-spacing:0.02em color:#475467 border:1px solid #E3E8F1 background:#FFFFFF border-radius:99px padding:4px 10px`
- [ ] text 20px/700 — “안 쓴 날을 표시하는 경우”
      `font-size:20px font-weight:700 letter-spacing:-0.025em color:#101828`
- [ ] text 13px/400 — “소비가 한 건도 없는 날에만 기록 창 맨 아래에 오늘은 안 썼어요가 보입니다. 누르면 달력 칸”
      `font-size:13px line-height:1.55 color:#626D88`
- [ ] **div** — “오늘 소비는 아직 기록이 없어요 · 이체 300,000원(소비율 제외)”
      `display:flex gap:32px align-items:flex-start`
- [ ] **Card(18)** — “구현 메모”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:10px 18px 8px`

## DoneCardStates — 참고 · 저장 완료 카드의 경우들

`canvas/DoneCardStates.dc.html` · 1200×1090 · 원본 `v5 · plan/v5-calendar.md §4-4` · 렌더 `preview/DoneCardStates.png`

- [ ] text 11px/600 — “구현 참고 · 앱 화면이 아닙니다”
      `font-size:11px font-weight:600 letter-spacing:0.02em color:#475467 border:1px solid #E3E8F1 background:#FFFFFF border-radius:99px padding:4px 10px`
- [ ] text 20px/700 — “저장 완료 카드의 경우들”
      `font-size:20px font-weight:700 letter-spacing:-0.025em color:#101828`
- [ ] text 13px/400 — “저장이 끝나면 홈 아래쪽에 뜨는 카드 하나가 제목 · 셋째 줄 · 행동만 바꿔 가며 모든 경우”
      `font-size:13px line-height:1.55 color:#626D88`
- [ ] **div** — “저장했어요”
      `display:flex gap:32px align-items:flex-start`

## LedgerV5 — 소비 · 내역 (분류 안 함 칩 · 날짜별 합계)

`canvas/LedgerV5.dc.html` · 390×844 · 원본 `v5 · plan/v5-calendar.md §9 · components/navi/spending-tab.tsx` · 렌더 `preview/LedgerV5.png`

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

## MonthlyCloseV5 — 모달 · 월 마감 (분류 안 함 안내)

`canvas/MonthlyCloseV5.dc.html` · 390×844 · 원본 `v5 · plan/v5-calendar.md §9` · 렌더 `preview/MonthlyCloseV5.png`

- [ ] **div** — “배경을 눌러 닫기”
      `height:40px display:flex align-items:flex-end justify-content:center`
- [ ] **BottomSheet** — “2026년 8월 마감”
      `flex:1 min-height:0 background:#FFFFFF border-radius:26px 26px 0 0 display:flex flex-direction:column color:#101828`
  - [ ] **div**
        `display:flex justify-content:center padding:9px 0 0`
  - [ ] **div** — “2026년 8월 마감”
        `display:flex align-items:flex-start justify-content:space-between gap:10px padding:12px 18px 14px border-bottom:1px solid #EFF2F8`
  - [ ] **div** — “이미 에 마감한 달입니다. 다시 저장하면 기존 마감값을 덮어씁니다.”
        `flex:1 min-height:0 padding:14px 18px 12px display:flex flex-direction:column gap:12px`
    - [ ] **Callout(warn)** — “이미 에 마감한 달입니다. 다시 저장하면 기존 마감값을 덮어씁니다.”
          `display:flex gap:8px padding:10px 11px background:#FDF1E0 border-radius:12px`
    - [ ] **div** — “그 달의 실제 수치”
    - [ ] **div** — “· 다음 달 한도 배분에도 기타로 들어가요 ·”
          `padding:10px 12px border:1px solid #E3E8F1 border-radius:12px font-size:12px line-height:1.5 color:#475467`
    - [ ] **div** — “자동으로 채워진 값”
  - [ ] **div** — “이 달의 수입·상환·잔액을 확인했고, 빠진 소비 기록이 없는지 살펴봤어요”
        `padding:12px 18px background:#F4F6FB border-top:1px solid #E3E8F1`
  - [ ] **div** — “취소”
        `display:flex gap:10px padding:12px 18px 20px border-top:1px solid #EFF2F8`

## TransactionAddFromDaySheet — 참고 · 거래 추가 — 하루 시트에서 넘어왔을 때

`canvas/TransactionAddFromDaySheet.dc.html` · 960×850 · 원본 `v5 · plan/v5-calendar.md §4` · 렌더 `preview/TransactionAddFromDaySheet.png`

- [ ] text 11px/600 — “구현 참고 · 앱 화면이 아닙니다”
      `font-size:11px font-weight:600 letter-spacing:0.02em color:#475467 border:1px solid #E3E8F1 background:#FFFFFF border-radius:99px padding:4px 10px white-space:nowrap`
- [ ] text 20px/700 — “거래 추가 — 하루 시트에서 넘어왔을 때”
      `font-size:20px font-weight:700 letter-spacing:-0.025em color:#101828`
- [ ] text 13px/400 — “하루 시트 아래의 링크 「저축·투자로 기록 ›」를 누르면 소비 탭의 거래 추가 창이 이 모습으”
      `font-size:13px line-height:1.55 color:#626D88`
- [ ] **div** — “거래 추가”
      `display:flex gap:28px align-items:flex-start`

## InsufficientElsewhere — 참고 · 예상 기준을 확인하기 전 — 홈 밖의 화면들

`canvas/InsufficientElsewhere.dc.html` · 1230×1330 · 원본 `v5 · plan/v5-calendar.md §3-4 · §9-22` · 렌더 `preview/InsufficientElsewhere.png`

- [ ] text 11px/600 — “구현 참고 · 앱 화면이 아닙니다”
      `font-size:11px font-weight:600 letter-spacing:0.02em color:#475467 border:1px solid #E3E8F1 background:#FFFFFF border-radius:99px padding:4px 10px`
- [ ] text 20px/700 — “예상 기준을 확인하기 전 — 홈 밖의 화면들”
      `font-size:20px font-weight:700 letter-spacing:-0.025em color:#101828`
- [ ] text 13px/400 — “홈의 이력 부족 상태(HeroInsufficient)와 같은 사람입니다 — 9월 5일에 처음 ”
      `font-size:13px line-height:1.55 color:#626D88`
- [ ] **div** — “1”
      `display:flex gap:24px align-items:flex-start`
- [ ] **Card(18)** — “구현 메모”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:10px 18px 8px`

## FutureProvisional — 참고 · 미래 · 자산 경로의 잠정 표시

`canvas/FutureProvisional.dc.html` · 1230×1080 · 원본 `v5 · plan/v5-calendar.md §3-4` · 렌더 `preview/FutureProvisional.png`

- [ ] text 11px/600 — “구현 참고 · 앱 화면이 아닙니다”
      `font-size:11px font-weight:600 letter-spacing:0.02em color:#475467 border:1px solid #E3E8F1 background:#FFFFFF border-radius:99px padding:4px 10px`
- [ ] text 20px/700 — “미래 · 자산 경로 — 예상 기준을 확인하기 전의 잠정 표시”
      `font-size:20px font-weight:700 letter-spacing:-0.025em color:#101828`
- [ ] text 13px/400 — “지난 소비 기록을 확인하기 전에도 미래 · 목표 화면의 예상 값은 그대로 보여 주되 잠정이라고”
      `font-size:13px line-height:1.55 color:#626D88`
- [ ] **div** — “미래”
      `display:flex gap:32px align-items:flex-start`

## LimitCardCases — 참고 · 이번 달 한도 카드의 네 가지 경우

`canvas/LimitCardCases.dc.html` · 1200×960 · 원본 `v5 · plan/v5-calendar.md §10 3단계` · 렌더 `preview/LimitCardCases.png`

- [ ] text 11px/600 — “구현 참고 · 앱 화면이 아닙니다”
      `font-size:11px font-weight:600 letter-spacing:0.02em color:#475467 border:1px solid #E3E8F1 background:#FFFFFF border-radius:99px padding:4px 10px`
- [ ] text 20px/700 — “이번 달 한도 카드 — 하루 금액 자리의 네 가지 경우”
      `font-size:20px font-weight:700 letter-spacing:-0.025em color:#101828`
- [ ] text 13px/400 — “3단계에서 홈 한도 카드의 하루 47,270원이 앞으로 하루 47,270원으로 바뀝니다. 한도”
      `font-size:13px line-height:1.55 color:#626D88`
- [ ] **div** — “평소 — 한도가 남아 있을 때”
      `display:flex gap:32px align-items:flex-start`
- [ ] **Card(18)** — “구현 메모”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:10px 18px 8px`

## RecurringPrefill — 반복 거래 · 방금 저장한 거래로 미리 채움

`canvas/RecurringPrefill.dc.html` · 390×844 · 원본 `v5 · plan/v5-calendar.md §10 3단계` · 렌더 `preview/RecurringPrefill.png`

- [ ] **div** — “배경을 눌러 닫기”
      `height:40px display:flex align-items:flex-end justify-content:center`
- [ ] **BottomSheet** — “반복 거래”
      `flex:1 min-height:0 background:#FFFFFF border-radius:26px 26px 0 0 display:flex flex-direction:column color:#101828`
  - [ ] **div**
        `display:flex justify-content:center padding:9px 0 0`
  - [ ] **div** — “반복 거래”
        `display:flex align-items:flex-start justify-content:space-between gap:10px padding:12px 18px 14px border-bottom:1px solid #EFF2F8`
  - [ ] **div** — “새 반복 거래”
        `flex:1 min-height:0 padding:14px 18px 0 display:flex flex-direction:column gap:15px`
    - [ ] **div** — “새 반복 거래”
    - [ ] **div** — “등록된 반복 거래”
  - [ ] **div** — “닫기”
        `display:flex gap:10px padding:12px 18px 20px border-top:1px solid #EFF2F8`

## EtcSubline — 참고 · 분류 안 한 소비와 안 쓴 날 — 소비 · 한도 · 코치

`canvas/EtcSubline.dc.html` · 1200×970 · 원본 `v5 · plan/v5-calendar.md §5-3 · §9` · 렌더 `preview/EtcSubline.png`

- [ ] text 11px/600 — “구현 참고 · 앱 화면이 아닙니다”
      `font-size:11px font-weight:600 letter-spacing:0.02em color:#475467 border:1px solid #E3E8F1 background:#FFFFFF border-radius:99px padding:4px 10px`
- [ ] text 20px/700 — “분류 안 한 소비와 안 쓴 날 — 소비 · 한도 · 코치에서”
      `font-size:20px font-weight:700 letter-spacing:-0.025em color:#101828`
- [ ] text 13px/400 — “하루 시트에서 분류 없이 저장한 소비는 기타로 들어갑니다. 소비 · 한도 화면은 기타 아래에 ”
      `font-size:13px line-height:1.55 color:#626D88`
- [ ] **div** — “1”
      `display:flex gap:24px align-items:flex-start`
- [ ] **Card(18)** — “구현 메모”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:10px 18px 8px`

## ImportBackupNotes — 참고 · 가져오기 · 백업 안내

`canvas/ImportBackupNotes.dc.html` · 1230×1060 · 원본 `v5 · plan/v5-calendar.md §10 3단계` · 렌더 `preview/ImportBackupNotes.png`

- [ ] text 11px/600 — “구현 참고 · 앱 화면이 아닙니다”
      `font-size:11px font-weight:600 letter-spacing:0.02em color:#475467 border:1px solid #E3E8F1 background:#FFFFFF border-radius:99px padding:4px 10px`
- [ ] text 20px/700 — “가져오기 · 백업 — 확인 표시와 분류 안 함 표시가 어떻게 따라오는지”
      `font-size:20px font-weight:700 letter-spacing:-0.025em color:#101828`
- [ ] text 13px/400 — “달력의 확인 표시(다 적었어요 · 안 썼어요)와 분류 안 함 표시는 백업 파일에 함께 들어갑니”
      `font-size:13px line-height:1.55 color:#626D88`
- [ ] **div** — “배경을 눌러 닫기”
      `display:flex gap:32px align-items:flex-start`

## TourHome1 — 첫 실행 안내 · 홈 1 / 3 현재 위치

`canvas/TourHome1.dc.html` · 390×844 · 원본 `미구현 · 첫 실행 안내 · plan/v5-calendar.md §10 11판 · design/CHANGES-2026-09-22.md` · 렌더 `preview/TourHome1.png`

- [ ] **Header** — “NAVI”
      `display:flex flex-direction:column gap:6px padding:12px 16px 10px`
- [ ] **본문(스크롤 영역)** — “현재 위치”
      `flex:1 min-height:0 display:flex flex-direction:column gap:9px padding:0 14px`
  - [ ] **HeroCard** — “현재 위치”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **Card(18)** — “이번 달 달력”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 14px 13px`
  - [ ] **TurnCard** — “다음 안내”
        `display:flex gap:12px background:#FFFFFF border:1px solid #E3E8F1 border-left:3px solid #DE8A2A border-radius:18px padding:13px 14px`
  - [ ] **Card(18)** — “이번 달 한도”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px`
  - [ ] **Card(18)** — “68%”
        `display:flex align-items:center gap:12px background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`
- [ ] **div** — “처음 안내”
      `position:absolute inset:0`

## TourHome2 — 첫 실행 안내 · 홈 2 / 3 달력으로 기록

`canvas/TourHome2.dc.html` · 390×844 · 원본 `미구현 · 첫 실행 안내 · plan/v5-calendar.md §10 11판 · design/CHANGES-2026-09-22.md` · 렌더 `preview/TourHome2.png`

- [ ] **Header** — “NAVI”
      `display:flex flex-direction:column gap:6px padding:12px 16px 10px`
- [ ] **본문(스크롤 영역)** — “현재 위치”
      `flex:1 min-height:0 display:flex flex-direction:column gap:9px padding:0 14px`
  - [ ] **HeroCard** — “현재 위치”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **Card(18)** — “이번 달 달력”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 14px 13px`
  - [ ] **TurnCard** — “다음 안내”
        `display:flex gap:12px background:#FFFFFF border:1px solid #E3E8F1 border-left:3px solid #DE8A2A border-radius:18px padding:13px 14px`
  - [ ] **Card(18)** — “이번 달 한도”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px`
  - [ ] **Card(18)** — “68%”
        `display:flex align-items:center gap:12px background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`
- [ ] **div** — “처음 안내”
      `position:absolute inset:0`

## TourHome3 — 첫 실행 안내 · 홈 3 / 3 다음 안내

`canvas/TourHome3.dc.html` · 390×844 · 원본 `미구현 · 첫 실행 안내 · plan/v5-calendar.md §10 11판 · design/CHANGES-2026-09-22.md` · 렌더 `preview/TourHome3.png`

- [ ] **Header** — “NAVI”
      `display:flex flex-direction:column gap:6px padding:12px 16px 10px`
- [ ] **본문(스크롤 영역)** — “현재 위치”
      `flex:1 min-height:0 display:flex flex-direction:column gap:9px padding:0 14px`
  - [ ] **HeroCard** — “현재 위치”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **Card(18)** — “이번 달 달력”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 14px 13px`
  - [ ] **TurnCard** — “다음 안내”
        `display:flex gap:12px background:#FFFFFF border:1px solid #E3E8F1 border-left:3px solid #DE8A2A border-radius:18px padding:13px 14px`
  - [ ] **Card(18)** — “이번 달 한도”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px`
  - [ ] **Card(18)** — “68%”
        `display:flex align-items:center gap:12px background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`
- [ ] **div** — “처음 안내”
      `position:absolute inset:0`

## TourAssets1 — 첫 실행 안내 · 자산 1 / 3 세 탭

`canvas/TourAssets1.dc.html` · 390×844 · 원본 `미구현 · 첫 실행 안내 · plan/v5-calendar.md §10 11판 · design/CHANGES-2026-09-22.md` · 렌더 `preview/TourAssets1.png`

- [ ] **div** — “자산”
      `display:flex flex-direction:column gap:10px padding:14px 16px 12px`
- [ ] **본문(스크롤 영역)** — “순자산”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **HeroCard** — “순자산”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **div** — “현금성 자산 · 생활비 기준”
        `display:flex gap:8px`
  - [ ] **Card(18)** — “자산 구성”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`
- [ ] **div** — “처음 안내”
      `position:absolute inset:0`

## TourAssets2 — 첫 실행 안내 · 자산 2 / 3 순자산

`canvas/TourAssets2.dc.html` · 390×844 · 원본 `미구현 · 첫 실행 안내 · plan/v5-calendar.md §10 11판 · design/CHANGES-2026-09-22.md` · 렌더 `preview/TourAssets2.png`

- [ ] **div** — “자산”
      `display:flex flex-direction:column gap:10px padding:14px 16px 12px`
- [ ] **본문(스크롤 영역)** — “순자산”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **HeroCard** — “순자산”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **div** — “현금성 자산 · 생활비 기준”
        `display:flex gap:8px`
  - [ ] **Card(18)** — “자산 구성”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`
- [ ] **div** — “처음 안내”
      `position:absolute inset:0`

## TourAssets3 — 첫 실행 안내 · 자산 3 / 3 현금성 자산

`canvas/TourAssets3.dc.html` · 390×844 · 원본 `미구현 · 첫 실행 안내 · plan/v5-calendar.md §10 11판 · design/CHANGES-2026-09-22.md` · 렌더 `preview/TourAssets3.png`

- [ ] **div** — “자산”
      `display:flex flex-direction:column gap:10px padding:14px 16px 12px`
- [ ] **본문(스크롤 영역)** — “순자산”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **HeroCard** — “순자산”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **div** — “현금성 자산 · 생활비 기준”
        `display:flex gap:8px`
  - [ ] **Card(18)** — “자산 구성”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`
- [ ] **div** — “처음 안내”
      `position:absolute inset:0`

## TourSpending1 — 첫 실행 안내 · 소비 1 / 3 세 탭

`canvas/TourSpending1.dc.html` · 390×844 · 원본 `미구현 · 첫 실행 안내 · plan/v5-calendar.md §10 11판 · design/CHANGES-2026-09-22.md` · 렌더 `preview/TourSpending1.png`

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
- [ ] **div** — “처음 안내”
      `position:absolute inset:0`

## TourSpending2 — 첫 실행 안내 · 소비 2 / 3 속도 그래프

`canvas/TourSpending2.dc.html` · 390×844 · 원본 `미구현 · 첫 실행 안내 · plan/v5-calendar.md §10 11판 · design/CHANGES-2026-09-22.md` · 렌더 `preview/TourSpending2.png`

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
- [ ] **div** — “처음 안내”
      `position:absolute inset:0`

## TourSpending3 — 첫 실행 안내 · 소비 3 / 3 카테고리

`canvas/TourSpending3.dc.html` · 390×844 · 원본 `미구현 · 첫 실행 안내 · plan/v5-calendar.md §10 11판 · design/CHANGES-2026-09-22.md` · 렌더 `preview/TourSpending3.png`

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
- [ ] **div** — “처음 안내”
      `position:absolute inset:0`

## TourGoals1 — 첫 실행 안내 · 목적지 1 / 3 월 저축 배분

`canvas/TourGoals1.dc.html` · 390×844 · 원본 `미구현 · 첫 실행 안내 · plan/v5-calendar.md §10 11판 · design/CHANGES-2026-09-22.md` · 렌더 `preview/TourGoals1.png`

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
- [ ] **div** — “처음 안내”
      `position:absolute inset:0`

## TourGoals2 — 첫 실행 안내 · 목적지 2 / 3 도착 예상

`canvas/TourGoals2.dc.html` · 390×844 · 원본 `미구현 · 첫 실행 안내 · plan/v5-calendar.md §10 11판 · design/CHANGES-2026-09-22.md` · 렌더 `preview/TourGoals2.png`

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
- [ ] **div** — “처음 안내”
      `position:absolute inset:0`

## TourGoals3 — 첫 실행 안내 · 목적지 3 / 3 목적지 추가

`canvas/TourGoals3.dc.html` · 390×844 · 원본 `미구현 · 첫 실행 안내 · plan/v5-calendar.md §10 11판 · design/CHANGES-2026-09-22.md` · 렌더 `preview/TourGoals3.png`

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
- [ ] **div** — “처음 안내”
      `position:absolute inset:0`

## TourFuture1 — 첫 실행 안내 · 미래 1 / 3 자산 경로

`canvas/TourFuture1.dc.html` · 390×844 · 원본 `미구현 · 첫 실행 안내 · plan/v5-calendar.md §10 11판 · design/CHANGES-2026-09-22.md` · 렌더 `preview/TourFuture1.png`

- [ ] **div** — “미래”
      `display:flex flex-direction:column gap:10px padding:14px 16px 12px`
- [ ] **본문(스크롤 영역)** — “기간”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **HeroCard** — “기간”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:14px 14px 13px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **Card(18)** — “다음 자산 지점”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px 4px`
  - [ ] **Card(18)** — “저장되지 않는 가정”
        `background:#FFFFFF border:1px dashed #B79BFF border-radius:18px padding:11px 14px 11px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`
- [ ] **div** — “처음 안내”
      `position:absolute inset:0`

## TourFuture2 — 첫 실행 안내 · 미래 2 / 3 다음 지점

`canvas/TourFuture2.dc.html` · 390×844 · 원본 `미구현 · 첫 실행 안내 · plan/v5-calendar.md §10 11판 · design/CHANGES-2026-09-22.md` · 렌더 `preview/TourFuture2.png`

- [ ] **div** — “미래”
      `display:flex flex-direction:column gap:10px padding:14px 16px 12px`
- [ ] **본문(스크롤 영역)** — “기간”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **HeroCard** — “기간”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:14px 14px 13px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **Card(18)** — “다음 자산 지점”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px 4px`
  - [ ] **Card(18)** — “저장되지 않는 가정”
        `background:#FFFFFF border:1px dashed #B79BFF border-radius:18px padding:11px 14px 11px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`
- [ ] **div** — “처음 안내”
      `position:absolute inset:0`

## TourFuture3 — 첫 실행 안내 · 미래 3 / 3 가정

`canvas/TourFuture3.dc.html` · 390×844 · 원본 `미구현 · 첫 실행 안내 · plan/v5-calendar.md §10 11판 · design/CHANGES-2026-09-22.md` · 렌더 `preview/TourFuture3.png`

- [ ] **div** — “미래”
      `display:flex flex-direction:column gap:10px padding:14px 16px 12px`
- [ ] **본문(스크롤 영역)** — “기간”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **HeroCard** — “기간”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:14px 14px 13px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **Card(18)** — “다음 자산 지점”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px 4px`
  - [ ] **Card(18)** — “저장되지 않는 가정”
        `background:#FFFFFF border:1px dashed #B79BFF border-radius:18px padding:11px 14px 11px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`
- [ ] **div** — “처음 안내”
      `position:absolute inset:0`

