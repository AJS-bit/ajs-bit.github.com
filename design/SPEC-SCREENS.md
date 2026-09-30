# 화면별 조립 체크리스트

각 화면을 **위에서 아래 순서로** 조립하세요. 블록 하나를 만들 때마다 지워 나가면
빠뜨린 것이 바로 보입니다. 굵은 이름은 `SPEC-COMPONENTS.md`의 컴포넌트입니다.

값은 요약입니다. **정확한 값은 항상 `canvas/<이름>.dc.html`이 기준**이고,
더 자세한 구조는 `spec/<이름>.outline.md`에 있습니다.

다크 화면은 별도 항목이 없습니다. 같은 구조에 `canvas/_tools/darken.py`의 색 대응만 적용한 것입니다.

---

## Assets — 자산 · 구성

`canvas/Assets.dc.html` · 390×977 · 원본 `components/navi/asset-view.tsx`

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

`canvas/Debts.dc.html` · 390×909 · 원본 `components/navi/asset-view.tsx`

> 부채 4건을 잔액 순으로 세운다(주택담보 → 신용 → 학자금 → 카드). 가장 높은 금리 한 건에만 빨간 「최고 금리」 배지(카드 할부 14.5%). 요약값은 「평균 금리 연 4.4%」.

- [ ] **div** — “자산”
      `display:flex flex-direction:column gap:10px padding:14px 16px 12px`
- [ ] **본문(스크롤 영역)** — “총부채”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **HeroCard** — “총부채”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **TurnCard** — “상환 안내”
        `display:flex gap:12px background:#FFFFFF border:1px solid #E3E8F1 border-left:3px solid #DE8A2A border-radius:18px padding:13px 14px`
  - [ ] **Card(18)** — “부채 4건”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
  - [ ] **Card(18)** — “이번 달 상환 예정”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 14px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`

## Strategy — 자산 · 상환 계획(읽기 전용 요약)

`canvas/Strategy.dc.html` · 390×844 · 원본 `components/navi/asset-view.tsx`

> 자산 › 상환 계획 = 저장된 상환 계획의 읽기 전용 요약. 다 갚는 달 · 상환 방식 · 갚는 순서를 보여 주고, 바꾸는 곳은 미래 › 상환 계획 한 곳뿐(「상환 계획 바꾸기 ›」 · D6).

- [ ] **div** — “자산”
      `display:flex flex-direction:column gap:10px padding:14px 16px 12px`
- [ ] **본문(스크롤 영역)** — “저장된 상환 계획”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **HeroCard** — “저장된 상환 계획”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **Card(18)** — “다 갚는 달”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
  - [ ] **Card(18)** — “갚는 순서”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`

## Spending — 소비 · 이번 달

`canvas/Spending.dc.html` · 390×957 · 원본 `components/navi/spending-view.tsx`

> 이번 달 소비 속도. 누적 그래프는 오늘까지 실선, 월말까지 점선 예상선으로 오른쪽 빈 공간을 채운다.

- [ ] **div** — “소비”
      `display:flex flex-direction:column gap:10px padding:14px 16px 12px`
- [ ] **본문(스크롤 영역)** — “31.1”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **HeroCard** — “31.1”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px 14px 14px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **Card(18)** — “카테고리별 소비”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
  - [ ] **div** — “소비 추이·절감 기회”
        `display:flex align-items:center gap:8px height:46px padding:0 14px background:#FFFFFF border:1px solid #E3E8F1 border-radius:16px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`

## Limits — 소비 · 한도

`canvas/Limits.dc.html` · 390×1106 · 원본 `components/navi/spending-view.tsx`

> 소비 목표 기준 총한도(알약 「자동 ›」/「직접 ›」 → 한도 조정) · 참고 줄(회색 · 판정 아님 · D1) · 소비 경고 · 카테고리 배분. 「배분 편집」은 「카테고리 배분」 제목과 같은 줄 오른쪽.

- [ ] **div** — “소비”
      `display:flex flex-direction:column gap:10px padding:14px 16px 12px`
- [ ] **본문(스크롤 영역)** — “이번 달 총한도”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **HeroCard** — “이번 달 총한도”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **Card(18)** — “소비 경고”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px 14px 12px`
  - [ ] **Card(18)** — “카테고리 배분”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
  - [ ] **div** — “이 한도는 어떻게 계산했나요?”
        `display:flex align-items:center justify-content:space-between gap:8px background:#FFFFFF border:1px solid #E3E8F1 border-radius:14px padding:0 14px height:50px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`

## SpendingPast — 소비 · 지난 달 (마감)

`canvas/SpendingPast.dc.html` · 390×1212 · 원본 `components/navi/spending-view.tsx`

> 지난 달 월 요약. 맨 위 월 마감 카드가 그 달 상태(마감함 · 마감 전 · 마감 뒤 기록이 바뀜)를 말하고 「마감값 보기·고치기 ›」로 연다. 기록은 내역에서 고친다.

- [ ] **div** — “소비”
      `display:flex flex-direction:column gap:10px padding:14px 16px 12px`
- [ ] **div** — “지난 달에는 한도 탭이 없어요 · 기록은 내역에서 고쳐요”
      `display:flex align-items:center gap:7px padding:0 16px 10px`
- [ ] **본문(스크롤 영역)** — “7월 마감 · 8월 2일에 마감했어요”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **Card(18)** — “7월 마감 · 8월 2일에 마감했어요”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 15px`
  - [ ] **HeroCard** — “마감한 달”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **Card(18)** — “31일 동안 이렇게 썼어요”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
  - [ ] **Card(18)** — “카테고리”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
  - [ ] **Card(18)** — “소비 추이·절감 기회”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px 16px`
- [ ] **div**
      `height:12px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`

## Goals — 목적지 · 내 목적지

`canvas/Goals.dc.html` · 390×992 · 원본 `components/navi/goals-view.tsx`

> 목적지 목록. GoalRing + 도착 예상 시점. 배분이 모자라면 얼마가 부족한지 숫자로 말한다.

- [ ] **div** — “목적지”
      `display:flex flex-direction:column gap:10px padding:14px 16px 12px`
- [ ] **본문(스크롤 영역)** — “매달 모으는 돈”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **HeroCard** — “매달 모으는 돈”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:15px 16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **Card(18)** — “진행 중인 목적지”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px 8px`
  - [ ] **div** — “목적지 추가”
        `display:flex align-items:center justify-content:center gap:6px height:46px border-radius:14px border:1.5px dashed #B9C3D6 background:rgba(255,255,255,.55) color:#3556E6 font-size:14px font-weight:600`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`

## GoalDesign — 목적지 · 새 목적지 설계

`canvas/GoalDesign.dc.html` · 390×1231 · 원본 `components/navi/goal-tools.tsx`

> 새 목적지를 만들 때 목표액·기간에서 월 납입액이 역산되는 화면.

- [ ] **div** — “목적지”
      `display:flex flex-direction:column gap:10px padding:14px 16px 12px`
- [ ] **본문(스크롤 영역)** — “추천 목적지에서 시작”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **Card(18)** — “추천 목적지에서 시작”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 14px`
  - [ ] **HeroCard** — “이름”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:15px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **Card(18)** — “다른 금액으로 계산해 보기 · 계산 기준”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:15px 14px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`

## Future — 미래 · 자산 경로

`canvas/Future.dc.html` · 390×1204 · 원본 `components/navi/future-view.tsx`

> 10년 뒤 순자산 경로. 투자 환경 「조심스럽게 · 보통 · 좋을 때」는 보기 선택이라 보라가 아니다(D13). 다음 자산 지점 · 절감 가정(0원보다 클 때만 보라).

- [ ] **div** — “미래”
      `display:flex flex-direction:column gap:10px padding:14px 16px 12px`
- [ ] **본문(스크롤 영역)** — “기간”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **HeroCard** — “기간”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:14px 14px 13px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **Card(18)** — “다음 자산 지점”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 14px 5px`
  - [ ] **Card(18)** — “10년 뒤 +0원”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:11px 14px 11px`
  - [ ] **Card(18)** — “투자 환경별 비교 · 전체 경로”
        `display:flex align-items:center justify-content:space-between gap:8px height:70px padding:12px 14px background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px`
  - [ ] **Card(18)** — “계산 방법 자세히”
        `height:86px padding:13px background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px`
  - [ ] **div** — “앞으로의 금액은 100만원 단위로 어림해 「약」을 붙였어요. 지금 금액은 입력한 그대로예요. ”
        `display:flex gap:8px padding:2px 4px 0 margin-top:21px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`

## Payoff — 미래 · 상환 계획

`canvas/Payoff.dc.html` · 390×924 · 원본 `components/navi/future-view.tsx`

> 미래 › 상환 계획 — 상환 방식 · 월 추가 상환액을 바꾸는 유일한 곳(D6). 저장된 계획 + 「추가 상환이 없으면 …」 기준 줄 · 상환 방식 비교 한 줄(D15) · 다 갚는 달 · 갚는 순서 · 「상환 계획 저장」.

- [ ] **div** — “미래”
      `display:flex flex-direction:column gap:10px padding:14px 16px 12px`
- [ ] **본문(스크롤 영역)** — “저장된 계획”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **Card(18)** — “저장된 계획”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
  - [ ] **Card(18)** — “고금리 우선”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 14px`
  - [ ] **Card(18)** — “저장된 상환 계획이에요”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`

## Onboarding — 첫 실행 · 시작 방법 고르기

`canvas/Onboarding.dc.html` · 390×844 · 원본 `components/navi/data-choice-screen.tsx (first-run-19 · D8 · AMEND 1)`

> 첫 실행 · 시작 방법 고르기. 파란 칸 「내 데이터로 시작」(주 행동) / 흰 칸 「샘플로 둘러보기」와 저장 위치 안내만 — ‹ 뒤로 = 홈 구성(AMEND 1).

- [ ] **div** — “시작 방법 고르기”
      `flex:1 min-height:0 display:flex flex-direction:column padding:0 20px`
  - [ ] **div** — “시작 방법 고르기”
        `display:flex align-items:center gap:8px height:56px margin-top:8px`
  - [ ] text 22px/700 — “어떤 데이터로 시작할까요?”
        `font-size:22px font-weight:700 letter-spacing:-0.03em line-height:1.35 color:#101828`
  - [ ] text 13.5px/400 — “NAVI는 인터넷 없이 실행되고, 자산 · 소비 · 목적지를 이 기기에 암호화해 저장해요. 샘”
        `font-size:13.5px line-height:1.5 color:#475467`
  - [ ] **div** — “내 데이터로 시작”
        `display:flex flex-direction:column gap:10px margin-top:20px`
  - [ ] **div**
        `height:1px background:#E3E8F1`
  - [ ] text 13px/400 — “앱을 삭제하거나 앱 데이터를 지우면 기록도 사라져요. 기기를 바꾸기 전에 설정에서 백업 파일을”
        `font-size:13px line-height:1.6 color:#626D88`

## ProfileDialog — 모달 · 내 수치

`canvas/ProfileDialog.dc.html` · 390×1229 · 원본 `components/navi/shared.tsx`

> 설정 › 내 수치. 월급 (실수령) · 부수입(선택 사항) · 소비 목표 + 접힘 「표시 이름 · 순자산 참고선」. 월급이 홈의 분모다. 월 추가 상환액은 상환 계획에서 바꾸는 줄(D5).

- [ ] **div** — “배경을 눌러 닫기”
      `height:60px display:flex align-items:flex-end justify-content:center`
- [ ] **BottomSheet** — “내 수치”
      `flex:1 min-height:0 background:#FFFFFF border-radius:26px 26px 0 0 display:flex flex-direction:column color:#101828`
  - [ ] **div**
        `display:flex justify-content:center padding:9px 0 0`
  - [ ] **div** — “내 수치”
        `display:flex align-items:flex-start justify-content:space-between gap:10px padding:12px 18px 14px border-bottom:1px solid #EFF2F8`
  - [ ] **div** — “기본”
        `flex:1 min-height:0 padding:14px 18px 14px display:flex flex-direction:column gap:15px`
    - [ ] **div** — “기본”
    - [ ] **div** — “소비 목표”
    - [ ] **div** — “추가 설정”
  - [ ] **div** — “취소”
        `display:flex gap:10px padding:12px 18px 20px border-top:1px solid #EFF2F8`

## TransactionAdd — 모달 · 기록 추가

`canvas/TransactionAdd.dc.html` · 390×844 · 원본 `components/navi/transaction-link-fields.tsx`

> 기록 추가(자세히). 잔액 반영 토글과 계좌 연결이 여기 있다. 금액은 원 단위 · 쉼표(D11).

- [ ] **div** — “배경을 눌러 닫기”
      `height:60px display:flex align-items:flex-end justify-content:center`
- [ ] **BottomSheet** — “기록 추가”
      `flex:1 min-height:0 background:#FFFFFF border-radius:26px 26px 0 0 display:flex flex-direction:column color:#101828`
  - [ ] **div**
        `display:flex justify-content:center padding:9px 0 0`
  - [ ] **div** — “기록 추가”
        `display:flex align-items:center justify-content:space-between gap:10px padding:12px 18px 13px border-bottom:1px solid #EFF2F8`
  - [ ] **div** — “기록 종류”
        `flex:1 min-height:0 padding:14px 18px 0 display:flex flex-direction:column gap:15px`
    - [ ] **div** — “기록 종류”
    - [ ] **div** — “날짜”
    - [ ] **div** — “금액 *”
    - [ ] **div** — “카테고리 *”
    - [ ] **div** — “메모 선택 사항”
    - [ ] **div** — “잔액에도 반영하기”
          `background:#F4F6FB border-radius:14px padding:13px`
    - [ ] **div** — “소비는 월급 대비 소비율과 카테고리 한도에 들어가요. 저축·투자와 대출상환은 소비율에 안 들어”
          `display:flex gap:7px padding:0 2px`
  - [ ] **div** — “취소”
        `display:flex gap:10px padding:12px 18px 20px border-top:1px solid #EFF2F8`

## LimitEditor — 모달 · 한도 조정

`canvas/LimitEditor.dc.html` · 390×1297 · 원본 `components/navi/spending-analysis.tsx`

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
        `flex:1 min-height:0 padding:14px 18px 0 display:flex flex-direction:column`
    - [ ] **div** — “이번 달 총한도”
          `background:#F4F6FB border-radius:16px padding:13px`
    - [ ] **div** — “카테고리 배분”
          `display:flex align-items:center justify-content:space-between gap:8px margin-top:17px`
    - [ ] **div** — “식비”
          `display:flex flex-direction:column margin-top:6px`
    - [ ] **div** — “배분 합계가 총한도와 같아요”
          `display:flex align-items:center justify-content:space-between gap:8px margin-top:12px padding:10px 12px background:#E4F4EA border:1px solid #C9E5D5 border-radius:12px`
  - [ ] **div** — “취소”
        `display:flex gap:10px padding:12px 18px 20px border-top:1px solid #EFF2F8`

## AssetDialog — 모달 · 자산 추가

`canvas/AssetDialog.dc.html` · 390×844 · 원본 `components/navi/asset-view.tsx`

> 자산 추가. 이름과 평가액만 필수.

- [ ] **Scrim여백** — “배경을 눌러 닫기”
      `height:190px display:flex align-items:flex-end justify-content:center`
- [ ] **BottomSheet** — “자산 추가”
      `flex:1 min-height:0 background:#FFFFFF border-radius:26px 26px 0 0 display:flex flex-direction:column color:#101828`
  - [ ] **div**
        `display:flex justify-content:center padding:9px 0 0`
  - [ ] **div** — “자산 추가”
        `display:flex align-items:flex-start justify-content:space-between gap:10px padding:12px 18px 14px border-bottom:1px solid #EFF2F8`
  - [ ] **div** — “자산 이름 *”
        `flex:1 min-height:0 padding:14px 18px 14px display:flex flex-direction:column gap:15px`
    - [ ] **div** — “자산 이름 *”
          `flex:0 0 auto`
    - [ ] **div** — “유형”
          `display:flex gap:10px align-items:flex-start margin-top:0px`
    - [ ] **div** — “수익률 (연) 선택 사항”
          `flex:0 0 auto`
  - [ ] **div** — “취소”
        `display:flex gap:10px padding:12px 18px 20px border-top:1px solid #EFF2F8`

## DebtDialog — 모달 · 부채 수정

`canvas/DebtDialog.dc.html` · 390×844 · 원본 `components/navi/asset-view.tsx`

> 부채 수정. 금리·최소상환액이 상환 시뮬레이션의 입력이다.

- [ ] **div** — “배경을 눌러 닫기”
      `height:110px display:flex align-items:flex-end justify-content:center`
- [ ] **BottomSheet** — “카드 할부 수정”
      `flex:1 min-height:0 background:#FFFFFF border-radius:26px 26px 0 0 display:flex flex-direction:column color:#101828`
  - [ ] **div**
        `display:flex justify-content:center padding:9px 0 0`
  - [ ] **div** — “카드 할부 수정”
        `display:flex align-items:flex-start justify-content:space-between gap:10px padding:12px 18px 14px border-bottom:1px solid #EFF2F8`
  - [ ] **div** — “부채 이름 *”
        `flex:1 min-height:0 padding:14px 18px 14px display:flex flex-direction:column gap:15px`
    - [ ] **div** — “부채 이름 *”
          `flex:0 0 auto`
    - [ ] **div** — “유형”
          `display:flex gap:10px align-items:flex-start margin-top:0px`
    - [ ] **div** — “연 금리 *”
          `display:flex gap:10px align-items:flex-start margin-top:0px`
    - [ ] **Callout(warn)** — “연 14.5%는 보유한 부채 중 가장 높아요. 상환 계획에서 순서를 확인하세요.”
          `display:flex gap:8px padding:10px 11px background:#FDF1E0 border-radius:12px`
    - [ ] **Callout(info)** — “다 갚았다면 삭제하지 말고 남은 원금을 0으로 저장하세요. 연결된 부채 상환 목적지가 다 갚은”
          `display:flex gap:8px padding:10px 11px background:#F4F6FB border-radius:12px`
  - [ ] **div** — “취소”
        `display:flex gap:10px padding:12px 18px 20px border-top:1px solid #EFF2F8`

## GoalDialog — 모달 · 목적지 추가

`canvas/GoalDialog.dc.html` · 390×844 · 원본 `components/navi/goals-view.tsx`

> 목적지 추가. 유형에 따라 입력 필드가 바뀐다.

- [ ] **div** — “배경을 눌러 닫기”
      `flex:0 1 40px min-height:12px display:flex align-items:flex-end justify-content:center`
- [ ] **BottomSheet** — “목적지 추가”
      `flex:1 0 auto background:#FFFFFF border-radius:26px 26px 0 0 display:flex flex-direction:column color:#101828`
  - [ ] **div**
        `display:flex justify-content:center padding:9px 0 0`
  - [ ] **div** — “목적지 추가”
        `display:flex align-items:flex-start justify-content:space-between gap:10px padding:12px 18px 14px border-bottom:1px solid #EFF2F8`
  - [ ] **div** — “유형”
        `flex:1 0 auto padding:14px 18px 0 display:flex flex-direction:column gap:15px`
    - [ ] **div** — “유형”
    - [ ] **div** — “이름 *”
          `flex:0 0 auto`
    - [ ] **div** — “표시 아이콘”
          `display:flex align-items:center gap:3px height:23px margin-top:-9px font-size:11.5px color:#626D88`
    - [ ] **div** — “갚을 부채”
    - [ ] **div** — “우선순위”
          `display:flex gap:10px align-items:flex-start margin-top:0px`
    - [ ] **Callout(info)** — “남은 빚과 상환 계획으로 다 갚는 달을 계산해요 목표액과 진행률은 실제 남은 원금에서 자동으로”
          `display:flex gap:8px padding:10px 11px background:#F4F6FB border-radius:12px`
  - [ ] **div** — “취소”
        `display:flex gap:10px padding:12px 18px 20px border-top:1px solid #EFF2F8`

## RecurringDialog — 모달 · 반복 기록

`canvas/RecurringDialog.dc.html` · 390×844 · 원본 `components/navi/spending-view.tsx`

> 반복 기록. 등록된 규칙 목록(켬/꺼 둠) + 새 규칙. 기존 반복 규칙 형식을 바꾸지 않는다.

- [ ] **div** — “배경을 눌러 닫기”
      `height:40px display:flex align-items:flex-end justify-content:center`
- [ ] **BottomSheet** — “반복 기록”
      `flex:1 min-height:0 background:#FFFFFF border-radius:26px 26px 0 0 display:flex flex-direction:column color:#101828`
  - [ ] **div**
        `display:flex justify-content:center padding:9px 0 0`
  - [ ] **div** — “반복 기록”
        `display:flex align-items:flex-start justify-content:space-between gap:10px padding:12px 18px 14px border-bottom:1px solid #EFF2F8`
  - [ ] **div** — “등록된 규칙”
        `flex:1 min-height:0 padding:14px 18px 0 display:flex flex-direction:column gap:15px`
    - [ ] **div** — “등록된 규칙”
    - [ ] **div** — “새 규칙”
  - [ ] **div** — “닫기”
        `display:flex gap:10px padding:12px 18px 20px border-top:1px solid #EFF2F8`

## GoalContribute — 모달 · 적립

`canvas/GoalContribute.dc.html` · 390×892 · 원본 `components/navi/goals-view.tsx`

> 목적지에 적립액을 더한다. 시뮬레이션이 아니라 기록이다.

- [ ] **div** — “배경을 눌러 닫기”
      `height:60px display:flex align-items:flex-end justify-content:center`
- [ ] **BottomSheet** — “비상금 6개월에 적립”
      `flex:1 min-height:0 background:#FFFFFF border-radius:26px 26px 0 0 display:flex flex-direction:column color:#101828`
  - [ ] **div**
        `display:flex justify-content:center padding:9px 0 0`
  - [ ] **div** — “비상금 6개월에 적립”
        `display:flex align-items:flex-start justify-content:space-between gap:10px padding:12px 18px 14px border-bottom:1px solid #EFF2F8`
  - [ ] **div** — “68%”
        `flex:1 min-height:0 padding:14px 18px 14px display:flex flex-direction:column gap:15px`
    - [ ] **Card(18)** — “68%”
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px 15px`
    - [ ] **div** — “이번에 넣은 돈 *”
    - [ ] **Card(18)** — “저장하면 이렇게 바뀌어요”
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 15px`
    - [ ] **Callout(info)** — “이 기록은 목적지의 모은 돈만 바꿔요. 통장에 실제로 넣었다면 위에서 잔액도 함께 늘릴 수 있”
          `display:flex gap:8px padding:10px 11px background:#F4F6FB border-radius:12px`
  - [ ] **div** — “취소”
        `display:flex gap:10px padding:12px 18px 20px border-top:1px solid #EFF2F8`

## ImportReview — 모달 · 백업 불러오기

`canvas/ImportReview.dc.html` · 390×905 · 원본 `components/navi/import-review.tsx`

> 백업 불러오기 검토. 「기존에 추가」 / 「전체 교체」 · 불러올 항목 건수(새로 추가 · 이미 있음 · 값이 다름 · 기존 유지) · 지금 → 적용 후를 보여 준 뒤 확인받는다.

- [ ] **div** — “배경을 눌러 닫기”
      `height:40px display:flex align-items:flex-end justify-content:center`
- [ ] **BottomSheet** — “백업 불러오기”
      `flex:1 min-height:0 background:#FFFFFF border-radius:26px 26px 0 0 display:flex flex-direction:column color:#101828`
  - [ ] **div**
        `display:flex justify-content:center padding:9px 0 0`
  - [ ] **div** — “백업 불러오기”
        `display:flex align-items:flex-start justify-content:space-between gap:10px padding:12px 18px 14px border-bottom:1px solid #EFF2F8`
  - [ ] **div** — “적용 방식”
        `flex:1 min-height:0 padding:14px 18px 0 display:flex flex-direction:column gap:13px`
    - [ ] **div** — “적용 방식”
    - [ ] **div** — “불러올 항목”
    - [ ] **div** — “적용 후”
    - [ ] **div** — “백업 설정 · 상세 내역 내 데이터”
          `display:flex align-items:center justify-content:space-between min-height:40px`
    - [ ] text 11.5px/400 — “가져온 기록의 카테고리 없음 표시도 함께 와요 · 확인 표시는 전체 복원에서만 돌아와요 · 이”
          `font-size:11.5px line-height:1.5 color:#626D88`
  - [ ] **div** — “데이터 성격과 적용 후 내역을 확인했어요.”
        `padding:12px 18px background:#F4F6FB border-top:1px solid #E3E8F1`
  - [ ] **div** — “취소”
        `display:flex gap:10px padding:12px 18px 20px border-top:1px solid #EFF2F8`

## CoachPanel — 모달 · 코칭

`canvas/CoachPanel.dc.html` · 390×942 · 원본 `components/navi/coach-panel.tsx`

> 코칭. 저장된 기록을 보고 중요한 순서로 안내를 보여 준다(번호 · 링크 하나씩) + 카테고리 절감 가정.

- [ ] **div** — “배경을 눌러 닫기”
      `height:40px display:flex align-items:flex-end justify-content:center`
- [ ] **BottomSheet** — “코칭”
      `flex:1 min-height:0 background:#FFFFFF border-radius:26px 26px 0 0 display:flex flex-direction:column color:#101828`
  - [ ] **div**
        `display:flex justify-content:center padding:9px 0 0`
  - [ ] **div** — “코칭”
        `display:flex align-items:flex-start justify-content:space-between gap:10px padding:12px 18px 14px border-bottom:1px solid #EFF2F8`
  - [ ] **div** — “1”
        `flex:1 min-height:0 padding:14px 18px 14px display:flex flex-direction:column gap:15px`
    - [ ] **div** — “1”
          `display:flex flex-direction:column gap:9px`
    - [ ] **Callout(info)** — “다른 안내 7개 더 보기”
          `display:flex align-items:center justify-content:space-between gap:8px height:48px padding:0 13px border-radius:12px background:#F4F6FB`
    - [ ] **div** — “카테고리 절감 가정”
  - [ ] **div** — “닫기”
        `display:flex gap:10px padding:12px 18px 20px border-top:1px solid #EFF2F8`

## CoachEmpty — 모달 · 코칭 기록 없음

`canvas/CoachEmpty.dc.html` · 390×844 · 원본 `components/navi/coach-panel.tsx`

> 코칭 기록이 없을 때. 0건을 성과처럼 보이게 하지 않는다.

- [ ] **div** — “배경을 눌러 닫기”
      `height:60px display:flex align-items:flex-end justify-content:center`
- [ ] **BottomSheet** — “코칭”
      `flex:1 min-height:0 background:#FFFFFF border-radius:26px 26px 0 0 display:flex flex-direction:column color:#101828`
  - [ ] **div**
        `display:flex justify-content:center padding:9px 0 0`
  - [ ] **div** — “코칭”
        `display:flex align-items:flex-start justify-content:space-between gap:10px padding:12px 18px 14px border-bottom:1px solid #EFF2F8`
  - [ ] **div** — “아직 알려 드릴 것이 없어요”
        `flex:1 min-height:0 padding:14px 18px 0 display:flex flex-direction:column gap:15px`
    - [ ] **Card(18)** — “아직 알려 드릴 것이 없어요”
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px 15px`
    - [ ] **Card(18)** — “이렇게 시작해 보세요”
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px 15px`
    - [ ] **Card(18)** — “기록이 쌓이면 이런 안내를 받아요”
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px 15px`
  - [ ] **div** — “오늘 쓴 돈 적기”
        `display:flex gap:10px padding:12px 18px 20px border-top:1px solid #EFF2F8`

## AlertsPanel — 모달 · 알림 (중요 1건)

`canvas/AlertsPanel.dc.html` · 390×844 · 원본 `components/navi/coach-panel.tsx`

> 알림 목록. 중요 · 참고로 묶고, 머리줄 종 배지 = 중요 수. 읽어도 기록은 바뀌지 않는다.

- [ ] **div** — “배경을 눌러 닫기”
      `height:40px display:flex align-items:flex-end justify-content:center`
- [ ] **BottomSheet** — “알림 1건”
      `flex:1 min-height:0 background:#FFFFFF border-radius:26px 26px 0 0 display:flex flex-direction:column color:#101828`
  - [ ] **div**
        `display:flex justify-content:center padding:9px 0 0`
  - [ ] **div** — “알림 1건”
        `display:flex align-items:flex-start justify-content:space-between gap:10px padding:12px 18px 14px border-bottom:1px solid #EFF2F8`
  - [ ] **div** — “중요 1”
        `flex:1 min-height:0 padding:14px 18px 0 display:flex flex-direction:column gap:15px`
    - [ ] **div** — “중요 1”
          `display:flex flex-direction:column`
    - [ ] **Callout(info)** — “자산의 잔액 확인일이 없거나 35일 넘게 갱신하지 않으면 여기에 알려 드려요. 지금은 갱신이 ”
          `display:flex gap:8px padding:10px 11px background:#F4F6FB border-radius:12px`
  - [ ] **div** — “닫기”
        `display:flex gap:10px padding:12px 18px 20px border-top:1px solid #EFF2F8`

## AlertsEmpty — 모달 · 알림 0건

`canvas/AlertsEmpty.dc.html` · 390×844 · 원본 `components/navi/coach-panel.tsx`

- [ ] **div** — “배경을 눌러 닫기”
      `height:40px display:flex align-items:flex-end justify-content:center`
- [ ] **BottomSheet** — “알림 0건”
      `flex:1 min-height:0 background:#FFFFFF border-radius:26px 26px 0 0 display:flex flex-direction:column color:#101828`
  - [ ] **div**
        `display:flex justify-content:center padding:9px 0 0`
  - [ ] **div** — “알림 0건”
        `display:flex align-items:flex-start justify-content:space-between gap:10px padding:12px 18px 14px border-bottom:1px solid #EFF2F8`
  - [ ] **div** — “확인할 알림이 없어요”
        `flex:1 min-height:0 padding:14px 18px 0 display:flex flex-direction:column gap:15px`
    - [ ] **div** — “확인할 알림이 없어요”
          `display:flex flex-direction:column align-items:center text-align:center padding:20px 10px background:#F4F6FB border-radius:14px`
    - [ ] **Callout(info)** — “자산의 잔액 확인일이 없거나 35일 넘게 갱신하지 않으면 여기에 알려 드려요. 지금은 갱신이 ”
          `display:flex gap:8px padding:10px 11px background:#F4F6FB border-radius:12px`
  - [ ] **div** — “닫기”
        `display:flex gap:10px padding:12px 18px 20px border-top:1px solid #EFF2F8`

## PeerDialog — 모달 · 또래 기준 등록

`canvas/PeerDialog.dc.html` · 390×844 · 원본 `components/navi/peer-card.tsx`

> 또래 기준 등록. 나이대는 초반(0~3)/중반(4~6)/후반(7~9)으로만 나눈다.

- [ ] **div** — “배경을 눌러 닫기”
      `height:40px display:flex align-items:flex-end justify-content:center`
- [ ] **BottomSheet** — “20대 후반 비교 기준”
      `flex:1 min-height:0 background:#FFFFFF border-radius:26px 26px 0 0 display:flex flex-direction:column color:#101828`
  - [ ] **div**
        `display:flex justify-content:center padding:9px 0 0`
  - [ ] **div** — “20대 후반 비교 기준”
        `display:flex align-items:flex-start justify-content:space-between gap:10px padding:12px 18px 14px border-bottom:1px solid #EFF2F8`
  - [ ] **div** — “NAVI에는 세부 연령별 통계가 들어 있지 않아요. 여기 넣은 값은 화면에서 항상 “내가 등록”
        `flex:1 min-height:0 padding:14px 18px 0 display:flex flex-direction:column gap:15px`
    - [ ] **Callout(warn)** — “NAVI에는 세부 연령별 통계가 들어 있지 않아요. 여기 넣은 값은 화면에서 항상 “내가 등록”
          `display:flex gap:8px padding:10px 11px background:#FDF1E0 border-radius:12px`
    - [ ] **div** — “연령 구간”
          `display:flex gap:10px`
    - [ ] **div** — “평균 소비율 *”
          `display:flex gap:10px`
    - [ ] **div** — “기준 연도 *”
          `display:flex gap:10px`
    - [ ] **div** — “자료 출처 *”
          `flex:1 min-height:0 display:flex flex-direction:column`
    - [ ] **Callout(info)** — “월급(실수령)이 아닌 다른 소득을 기준으로 한 통계라면 내 월말 예상과 바로 비교할 수 없어요”
          `display:flex gap:8px padding:10px 11px background:#F4F6FB border-radius:12px`
  - [ ] **div** — “취소”
        `display:flex gap:10px padding:12px 18px 20px border-top:1px solid #EFF2F8`

## StorageStates — 상태 · 저장소 로딩·복구 · 샘플에서 내 데이터로

`canvas/StorageStates.dc.html` · 390×2779 · 원본 `app/page.tsx`

> 저장소 로딩·복구 상태 모음. 로딩과 "데이터 없음"은 다른 화면이다.

- [ ] **div** — “구현 참고 · 앱 화면이 아닙니다”
      `padding:0 2px 6px`
- [ ] text 11px/600 — “A · 불러오는 중”
      `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
- [ ] **div** — “NAVI”
      `display:flex align-items:center gap:9px padding:2px 4px 4px`
- [ ] **Card(18)** — “저장된 기록을 불러오는 중”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:18px 16px`
- [ ] text 11px/600 — “B · 불러오기 실패”
      `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
- [ ] **Card(18)** — “저장된 기록을 불러오지 못했어요”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:18px 16px`
- [ ] text 11px/600 — “B′ · 원본을 파일로 저장한 뒤”
      `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
- [ ] **Card(18)** — “저장된 기록을 불러오지 못했어요”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:18px 16px`
- [ ] text 11.5px/400 — “「새로 시작」을 누르면 한 번 더 묻습니다. 원본을 저장하지 못하면 주 버튼 아래에 빨간 줄이”
      `font-size:11.5px line-height:1.5 color:#626D88 padding:0 4px`
- [ ] **Card(18)** — “원본을 파일로 저장”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px`
- [ ] **HeroCard** — “새로 시작할까요?”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px box-shadow:0 16px 40px -18px rgba(16,24,40,.35)`
- [ ] text 11.5px/400 — “원본 저장에 두 번 실패한 뒤에는 확인 창이 빨간 쪽으로 바뀝니다.”
      `font-size:11.5px line-height:1.5 color:#626D88 padding:0 4px`
- [ ] **HeroCard** — “새로 시작할까요?”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px box-shadow:0 16px 40px -18px rgba(16,24,40,.35)`
- [ ] text 11px/600 — “C · 백업 파일을 읽지 못함 — 같은 화면 안의 오류 줄”
      `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
- [ ] **Card(18)** — “저장된 기록을 불러오지 못했어요”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:18px 16px`
- [ ] text 11.5px/400 — “읽을 수 있는 백업을 고르면 이 카드 아래에 「백업 불러오기」가 열립니다 — 「{파일} · 저”
      `font-size:11.5px line-height:1.5 color:#626D88 padding:0 4px`
- [ ] text 11px/600 — “D · 샘플에서 내 데이터로 전환”
      `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
- [ ] **HeroCard** — “샘플을 치우고 내 데이터로 시작할까요?”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px box-shadow:0 16px 40px -18px rgba(16,24,40,.35)`
- [ ] text 11.5px/400 — “샘플 모드 맨 위 띠 「샘플 데이터로 둘러보는 중 · 내 데이터로 시작 ›」에서 열립니다. 「”
      `font-size:11.5px line-height:1.5 color:#626D88 padding:0 4px`

## EmptyStates — 참고 · 미입력 7종 · 화면마다의 빈 카드

`canvas/EmptyStates.dc.html` · 2002×2353 · 원본 `app/page.tsx`

> 미입력 일곱 가지와 화면마다의 빈 카드. **미입력을 0원이나 좋은 성과로 표시하지 않는다**는 규칙이 그림으로 있는 시트.

- [ ] text 11px/600 — “구현 참고 · 앱 화면이 아닙니다”
      `font-size:11px font-weight:600 letter-spacing:0.02em color:#475467 border:1px solid #E3E8F1 background:#FFFFFF border-radius:99px padding:4px 10px`
- [ ] text 20px/700 — “미입력 · 빈 상태 — 일곱 가지 경우와 화면마다의 빈 카드”
      `font-size:20px font-weight:700 letter-spacing:-0.025em color:#101828`
- [ ] text 13px/400 — “아직 넣지 않은 값은 0원 · 0% · 좋은 결과로 보이지 않고 회색 — 와 「입력 필요」로 ”
      `font-size:13px line-height:1.55 color:#626D88`
- [ ] **div** — “A · 첫 시작 · 홈 — 내 데이터로 시작한 날(월급 · 기록 · 자산 · 부채 0)”
      `display:flex gap:28px align-items:flex-start`

## PeerStates — 상태 · 또래 카드 6종

`canvas/PeerStates.dc.html` · 390×2972 · 원본 `components/navi/peer-card.tsx`

> 또래 카드 6종. 통계가 없으면 없다고 말한다. 평균·백분위·상위 %를 지어내지 않는다.

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
- [ ] **Card(18)** — “또래와 내 페이스”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
- [ ] text 11px/600 — “D · 월급 미입력”
      `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
- [ ] **Card(18)** — “20대 후반 · 비교 기준 등록됨”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
- [ ] text 11px/600 — “D′ · 이번 달 기록 0건(월급 있음)”
      `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
- [ ] **Card(18)** — “20대 후반 · 비교 기준 등록됨”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
- [ ] text 11px/600 — “D″ · 지난달 마감 전(월말 예상 확인 전)”
      `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
- [ ] **Card(18)** — “또래와 내 페이스”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
- [ ] text 11px/600 — “E · 입력 연도 확인 필요”
      `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
- [ ] **Card(18)** — “20대 후반”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
- [ ] text 11px/600 — “F · 기준 연도가 앞날”
      `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
- [ ] **Card(18)** — “20대 후반”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`

## GoalTypes — 상태 · 목적지 유형 5종

`canvas/GoalTypes.dc.html` · 390×2170 · 원본 `components/navi/goals-view.tsx`

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

## ModalErrors — 상태 · 모달 오류·저장 7종

`canvas/ModalErrors.dc.html` · 390×3290 · 원본 `모달 공통 (폼 검증·저장 경로)`

> 모달 오류·저장 7종. 각 오류의 문구와 위치가 정해져 있다.

- [ ] **div** — “구현 참고 · 앱 화면이 아닙니다”
      `padding:0 2px 6px`
- [ ] text 11px/600 — “A · 필수 값 미입력 — 저장을 누르면 빠진 칸을 알려 줌”
      `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
- [ ] **div** — “기록 추가”
      `display:flex flex-direction:column gap:8px`
- [ ] text 11px/600 — “B · 직접 정한 카테고리 합계가 총한도보다 큼”
      `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
- [ ] **Card(18)** — “한도 조정”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:16px`
- [ ] text 11px/600 — “C · 저장 중 — 입력 잠금”
      `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
- [ ] **Card(18)** — “자산 추가”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:16px`
- [ ] text 11px/600 — “D · 저장 실패 — 실패한 자리 옆에 한 번”
      `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
- [ ] **div** — “기록 추가 · 저장을 눌렀는데 기기에 못 씀”
      `display:flex flex-direction:column gap:8px`
- [ ] text 11px/600 — “E · 저장 알림 — 6초 카드 → 한 줄 띠”
      `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
- [ ] **Card(18)** — “처음 6초 — 아래 탭 막대 바로 위”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
- [ ] text 11px/600 — “F · 저장하지 않고 닫기”
      `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
- [ ] **div** — “저장하지 않고 닫을까요?”
      `display:flex flex-direction:column gap:8px`
- [ ] text 11px/600 — “G · 부채 상환 목적지 — 넣어 둔 부채가 없을 때”
      `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
- [ ] **Card(18)** — “목적지 추가”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:16px`

## Confirmations — 상태 · 삭제·초기화·확인 창 7종

`canvas/Confirmations.dc.html` · 390×2265 · 원본 `components/ui/alert-dialog.tsx 사용처`

> 삭제·초기화·확인 창 7종. 되돌릴 수 없는 동작은 무엇이 사라지는지 말한다.

- [ ] **div** — “구현 참고 · 앱 화면이 아닙니다”
      `padding:0 2px 6px`
- [ ] text 11px/600 — “A · 자산 삭제”
      `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
- [ ] **div** — “ETF 계좌를 삭제할까요?”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 8px 24px -16px rgba(16,24,40,.28)`
- [ ] text 11px/600 — “B · 기록 지우기 — 반복 기록이 만든 건”
      `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
- [ ] **div** — “이 기록을 지울까요?”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 8px 24px -16px rgba(16,24,40,.28)`
- [ ] text 11px/600 — “B′ · 기록 지우기 — 보통 기록”
      `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
- [ ] **div** — “이 기록을 지울까요?”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 8px 24px -16px rgba(16,24,40,.28)`
- [ ] text 11px/600 — “C · 목적지 삭제”
      `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
- [ ] **div** — “비상금 6개월 목적지를 삭제할까요?”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 8px 24px -16px rgba(16,24,40,.28)`
- [ ] text 11px/600 — “D · 반복 규칙 지우기”
      `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
- [ ] **div** — “ETF 자동이체 반복 규칙을 지울까요?”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 8px 24px -16px rgba(16,24,40,.28)`
- [ ] text 11px/600 — “E · 모든 데이터 지우기”
      `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
- [ ] **div** — “모든 데이터를 지울까요?”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 8px 24px -16px rgba(16,24,40,.28)`
- [ ] text 11px/600 — “F · 원 단위로 적으셨나요? — 만원 칸에 원 단위 숫자”
      `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
- [ ] **div** — “원 단위로 적으셨나요?”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 8px 24px -16px rgba(16,24,40,.28)`
- [ ] text 11px/600 — “G · 마감한 달의 합계 고치기”
      `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
- [ ] **div** — “8월 소비 합계만 새 금액으로 고칠게요”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 8px 24px -16px rgba(16,24,40,.28)`

## DesktopLedger — 데스크톱 · 소비 내역

`canvas/DesktopLedger.dc.html` · 1440×976 · 원본 `components/navi/spending-view.tsx`

> 데스크톱 내역. 표 형태(카테고리 · 제목 · 연결 · 금액). 소비율 제외 행은 회색 금액(− 없음)과 「소비율 제외」 배지로 구분한다. 오른쪽은 요약 카드 넷.

- [ ] **div** — “NAVI”
      `width:232px background:#FFFFFF display:flex flex-direction:column padding:22px 16px 18px`
- [ ] **div** — “소비”
      `flex:1 display:flex flex-direction:column padding:40px 28px 24px`
  - [ ] **div** — “소비”
        `display:flex align-items:flex-end justify-content:space-between gap:12px`
  - [ ] **div** — “소비 · 내역”
        `display:flex align-items:flex-end justify-content:space-between gap:12px margin-top:16px`
  - [ ] **div** — “메모·카테고리 검색”
        `flex:1 min-height:0 display:grid grid-template-columns:minmax(0, 1.75fr) minmax(0, 1fr) gap:18px margin-top:18px`
    - [ ] **Card(20)** — “메모·카테고리 검색”
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px display:flex flex-direction:column`
    - [ ] **div** — “9월 일반 소비”
          `display:flex flex-direction:column gap:14px`

## Tokens — 토큰 · 색 · 타이포 · 간격

`canvas/Tokens.dc.html` · 1200×2273 · 원본 `app/globals.css · lib/engine/constants.ts`

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

`canvas/Components.dc.html` · 1200×4773 · 원본 `components/navi/shared.tsx · components/ui/button.tsx`

> 컴포넌트·상태 시트. SPEC-COMPONENTS.md의 그림판.

- [ ] **div** — “NAVI DESIGN SYSTEM v3”
      `display:flex align-items:flex-end justify-content:space-between gap:20px border-bottom:2px solid #101828`
- [ ] **div** — “01 · 버튼 위계와 상태”
      `display:grid grid-template-columns:minmax(0, 1fr) minmax(0, 1.1fr) gap:32px`
- [ ] **div** — “07 · 행동을 어디에 놓는가 — 이번 재설계의 핵심 규칙”
      `padding:18px 20px background:#F4F6FB border-radius:16px`
- [ ] **div** — “08 · v5 달력과 하루 시트 — 새 컴포넌트 11종”
- [ ] **div** — “09 · 탭 머리줄 — 모든 탭이 같은 틀(AppTopbar)”
- [ ] **div** — “10 · 판정 줄 · 참고 줄 · 비어 있는 값”

## IntroPosition — 첫 실행 · 소개 1 현재 위치

`canvas/IntroPosition.dc.html` · 390×844 · 원본 `components/navi/intro-flow.tsx (first-run-13 · plan/v4-stocks.md §3)`

- [ ] **div** — “소개 1 / 3”
      `flex:1 min-height:0 display:flex flex-direction:column padding:0 20px`
  - [ ] **div** — “소개 1 / 3”
        `display:flex align-items:center justify-content:space-between gap:8px height:56px margin-top:8px`
  - [ ] **div** — “이번 달 소비 기록”
        `margin-top:36px display:flex flex-direction:column gap:10px`
  - [ ] text 11px/600 — “현재 위치”
        `display:block margin-top:30px font-size:11px font-weight:600 letter-spacing:0.07em color:#3556E6`
  - [ ] **h1** — “쓴 돈을 달력에 숫자만 적으면 월급의 몇 %를 썼는지 바로 보여요”
        `font-size:23px font-weight:700 letter-spacing:-0.03em line-height:1.4 color:#101828`
  - [ ] **p** — “은행 · 카드 연결 없이 직접 적고, 이 폰에만 저장돼요.”
        `display:flex align-items:flex-start gap:6px font-size:13.5px line-height:1.5 color:#475467`
  - [ ] **div** — “다음”
        `margin-top:auto display:flex flex-direction:column gap:16px`

## IntroRoute — 첫 실행 · 소개 2 항로

`canvas/IntroRoute.dc.html` · 390×844 · 원본 `components/navi/intro-flow.tsx (first-run-13 · plan/v4-stocks.md §3)`

- [ ] **div** — “소개 2 / 3”
      `flex:1 min-height:0 display:flex flex-direction:column padding:0 20px`
  - [ ] **div** — “소개 2 / 3”
        `display:flex align-items:center justify-content:space-between gap:8px height:56px margin-top:8px`
  - [ ] **div** — “항로”
        `margin-top:36px display:flex flex-direction:column gap:10px`
  - [ ] text 11px/600 — “항로”
        `display:block margin-top:30px font-size:11px font-weight:600 letter-spacing:0.07em color:#3556E6`
  - [ ] **h1** — “소비 목표까지 얼마나 남았는지, 지금 무엇을 하면 되는지 알려 줘요.”
        `font-size:23px font-weight:700 letter-spacing:-0.03em line-height:1.4 color:#101828`
  - [ ] **div** — “다음”
        `margin-top:auto display:flex flex-direction:column gap:16px`

## IntroDestination — 첫 실행 · 소개 3 목적지

`canvas/IntroDestination.dc.html` · 390×844 · 원본 `components/navi/intro-flow.tsx (first-run-13 · plan/v4-stocks.md §3)`

- [ ] **div** — “소개 3 / 3”
      `flex:1 min-height:0 display:flex flex-direction:column padding:0 20px`
  - [ ] **div** — “소개 3 / 3”
        `display:flex align-items:center justify-content:space-between gap:8px height:56px margin-top:8px`
  - [ ] **div** — “목적지”
        `margin-top:36px display:flex flex-direction:column gap:10px`
  - [ ] text 11px/600 — “목적지”
        `display:block margin-top:30px font-size:11px font-weight:600 letter-spacing:0.07em color:#3556E6`
  - [ ] **h1** — “비상금 · 투자 · 상환, 언제 도착할지 날짜로 알려 줘요.”
        `font-size:23px font-weight:700 letter-spacing:-0.03em line-height:1.4 color:#101828`
  - [ ] **div** — “다음”
        `margin-top:auto display:flex flex-direction:column gap:16px`

## HomeSetup — 첫 실행 · 홈 구성

`canvas/HomeSetup.dc.html` · 390×844 · 원본 `components/navi/home-layout-editor.tsx (AMEND 1 · first-run-12/14/15/16 · plan/v4-stocks.md §3)`

- [ ] **div** — “홈 구성”
      `padding:0 20px`
- [ ] **div** — “홈에 무엇을 둘까요?”
      `flex:1 min-height:0 padding:0 20px display:flex flex-direction:column`
  - [ ] **div** — “홈에 무엇을 둘까요?”
        `display:flex flex-direction:column`
- [ ] **div** — “다음”
      `padding:8px 20px 24px display:flex flex-direction:column gap:8px background:#EDF0F7`

## HomeConfigured — 홈 · 첫 실행 뒤 (내 데이터 · 카드 3개)

`canvas/HomeConfigured.dc.html` · 390×1178 · 원본 `app/page.tsx · components/navi/start-checklist.tsx · home-hero.tsx (first-run-5 · first-run-14 · D7 · D9)`

- [ ] **Header** — “NAVI”
      `display:flex flex-direction:column gap:6px padding:12px 16px 10px`
- [ ] **본문(스크롤 영역)** — “이번 달 소비”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **HeroCard** — “이번 달 소비”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **Card(18)** — “이번 달 소비 기록”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 14px 13px`
  - [ ] **Card(18)** — “다음 안내”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px 16px 10px`
  - [ ] **Card(18)** — “이번 달 한도 오늘 포함 하루 —”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px`
  - [ ] **Card(18)** — “순자산”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:4px 14px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`

## DestGoals — 목적지 · 내 목적지 (5탭)

`canvas/DestGoals.dc.html` · 390×844 · 원본 `v4 미구현 · plan/v4-stocks.md §4·§5`

- [ ] **div** — “목적지”
      `display:flex flex-direction:column gap:10px padding:14px 16px 12px`
- [ ] **본문(스크롤 영역)** — “매달 모으는 돈”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **HeroCard** — “매달 모으는 돈”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:15px 16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **Card(18)** — “진행 중인 목적지”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px 8px`
  - [ ] **div** — “목적지 추가”
        `display:flex align-items:center justify-content:center gap:6px height:46px border-radius:14px border:1.5px dashed #B9C3D6 background:rgba(255,255,255,.55) color:#3556E6 font-size:14px font-weight:600`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`

## DestFuture — 목적지 · 자산 경로 (5탭)

`canvas/DestFuture.dc.html` · 390×844 · 원본 `v4 미구현 · plan/v4-stocks.md §4·§5`

- [ ] **div** — “목적지”
      `display:flex flex-direction:column gap:10px padding:14px 16px 12px`
- [ ] **본문(스크롤 영역)** — “기간”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **HeroCard** — “기간”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:14px 14px 13px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **Card(18)** — “다음 자산 지점”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 14px 5px`
  - [ ] **Card(18)** — “10년 뒤 +0원”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:11px 14px 11px`
  - [ ] **Card(18)** — “투자 환경별 비교 · 전체 경로”
        `display:flex align-items:center justify-content:space-between gap:8px height:70px padding:12px 14px background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px`
  - [ ] **Card(18)** — “계산 방법 자세히”
        `height:86px padding:13px background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px`
  - [ ] **div** — “앞으로의 금액은 100만원 단위로 어림해 「약」을 붙였어요. 지금 금액은 입력한 그대로예요. ”
        `display:flex gap:8px padding:2px 4px 0 margin-top:21px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`

## HomeStocksOff — 홈 · 주식 꺼짐 (4탭)

`canvas/HomeStocksOff.dc.html` · 390×844 · 원본 `v4 미구현 · plan/v4-stocks.md §4·§5`

- [ ] **본문(스크롤 영역)** — “이번 달 소비”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px justify-content:flex-end padding:0 14px 14px`
  - [ ] **HeroCard** — “이번 달 소비”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **Card(18)** — “이번 달 소비 기록”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 14px 13px`
  - [ ] **TurnCard** — “다음 안내”
        `display:flex gap:12px background:#FFFFFF border:1px solid #E3E8F1 border-left:3px solid #DE8A2A border-radius:18px padding:13px 14px`
  - [ ] **Card(18)** — “이번 달 한도 오늘 포함 하루 45,220원”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px`
  - [ ] **Card(18)** — “순자산”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:4px 14px`
  - [ ] **Card(18)** — “상환 계획”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:4px 14px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`

## StocksMine — 주식 · 내 종목 (계획 · 3단계)

`canvas/StocksMine.dc.html` · 390×912 · 원본 `v4 미구현 · plan/v4-stocks.md §4·§5`

- [ ] **div** — “주식”
      `display:flex flex-direction:column gap:10px padding:14px 16px 12px`
- [ ] **본문(스크롤 영역)** — “목적지에 나누고 남은 돈”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **div** — “목적지에 나누고 남은 돈”
        `display:flex align-items:flex-start gap:8px padding:9px 12px background:#E9EDFD border-radius:14px`
  - [ ] **Card(18)** — “보유”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px 8px`
  - [ ] **Card(18)** — “관심”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px 6px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`

## HoldingAdd — 모달 · 보유 추가

`canvas/HoldingAdd.dc.html` · 390×844 · 원본 `v4 미구현 · plan/v4-stocks.md §4·§5`

- [ ] **div** — “배경을 눌러 닫기”
      `height:60px display:flex align-items:flex-end justify-content:center`
- [ ] **BottomSheet** — “보유 추가”
      `flex:1 min-height:0 background:#FFFFFF border-radius:26px 26px 0 0 display:flex flex-direction:column color:#101828`
  - [ ] **div**
        `display:flex justify-content:center padding:9px 0 0`
  - [ ] **div** — “보유 추가”
        `display:flex align-items:flex-start justify-content:space-between gap:10px padding:12px 18px 14px border-bottom:1px solid #EFF2F8`
  - [ ] **div** — “종목 *”
        `flex:1 min-height:0 padding:14px 18px 14px display:flex flex-direction:column gap:15px`
    - [ ] **div** — “종목 *”
          `flex:0 0 auto`
    - [ ] **div** — “수량 *”
          `display:flex gap:10px`
    - [ ] **div** — “종가 선택 사항”
          `display:flex gap:10px`
    - [ ] **Callout(info)** — “종가는 직접 넣는 값이라 실시간 시세가 아니에요. 가격 옆에는 늘 이 기준일이 붙어요.”
          `display:flex gap:8px padding:10px 11px background:#F4F6FB border-radius:12px`
    - [ ] **div** — “연결 계좌 선택 사항”
          `flex:0 0 auto`
    - [ ] **div** — “계좌 지금 금액에도 반영하기”
          `display:flex align-items:center justify-content:space-between gap:10px padding:12px 13px background:#F4F6FB border-radius:14px`
  - [ ] **div** — “취소”
        `display:flex gap:10px padding:12px 18px 20px border-top:1px solid #EFF2F8`

## StocksEmpty — 주식 · 빈 상태

`canvas/StocksEmpty.dc.html` · 390×844 · 원본 `v4 미구현 · plan/v4-stocks.md §4·§5`

- [ ] **div** — “주식”
      `display:flex flex-direction:column gap:10px padding:14px 16px 12px`
- [ ] **본문(스크롤 영역)** — “등록된 종목이 없어요”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **Card(18)** — “등록된 종목이 없어요”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:4px 14px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`

## HomeStocksCard — 홈 · 주식 요약 카드 (계획 · 3단계 뒤 · 앱에는 아직 없음)

`canvas/HomeStocksCard.dc.html` · 390×844 · 원본 `v4 미구현 · plan/v4-stocks.md §4·§5`

- [ ] **본문(스크롤 영역)** — “이번 달 소비”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px justify-content:flex-end padding:0 14px 14px`
  - [ ] **HeroCard** — “이번 달 소비”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **Card(18)** — “이번 달 소비 기록”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 14px 13px`
  - [ ] **TurnCard** — “다음 안내”
        `display:flex gap:12px background:#FFFFFF border:1px solid #E3E8F1 border-left:3px solid #DE8A2A border-radius:18px padding:13px 14px`
  - [ ] **Card(18)** — “주식 요약”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:4px 14px`
  - [ ] **Card(18)** — “이번 달 한도 오늘 포함 하루 45,220원”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px`
  - [ ] **Card(18)** — “순자산”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:4px 14px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`

## StocksHome — 주식 · 둘러보기

`canvas/StocksHome.dc.html` · 390×844 · 원본 `v4 미구현 · plan/v4-stocks.md §4·§5`

- [ ] **div** — “주식”
      `display:flex flex-direction:column gap:10px padding:14px 16px 12px`
- [ ] **본문(스크롤 영역)** — “목적지에 나누고 남은 돈”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **div** — “목적지에 나누고 남은 돈”
        `display:flex align-items:flex-start gap:8px padding:9px 12px background:#E9EDFD border-radius:14px`
  - [ ] **Callout(warn)** — “비상금 6개월 목적지가 68%예요 · 비상금을 먼저 채워 보세요”
        `display:flex align-items:center gap:8px padding:9px 12px background:#FDF1E0 border-radius:12px`
  - [ ] **Card(18)** — “내 종목”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:4px 14px`
  - [ ] **div** — “성장”
        `display:grid grid-template-columns:repeat(2, minmax(0, 1fr)) gap:10px align-items:start`
  - [ ] **p** — “데이터 기준일 2026년 9월 4일 종가 · 설정 › 주식에서 새로 받기 기준에 맞는 종목을 ”
        `font-size:11px line-height:1.5 color:#626D88`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`

## StockListGrowth — 주식 · 성장주 목록

`canvas/StockListGrowth.dc.html` · 390×844 · 원본 `v4 미구현 · plan/v4-stocks.md §4·§5`

- [ ] **div** — “성장주”
      `display:flex align-items:center gap:6px padding:12px 12px 12px`
- [ ] **본문(스크롤 영역)** — “매출 성장”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **div** — “매출 성장”
        `display:flex flex-direction:column gap:9px`
  - [ ] **Card(18)** — “삼성전자”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:2px 14px 0`
  - [ ] **p** — “데이터 기준일 2026년 9월 4일 종가 · 설정 › 주식에서 새로 받기 기준에 맞는 종목을 ”
        `font-size:11px line-height:1.5 color:#626D88`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`

## StockListDividend — 주식 · 배당주 목록

`canvas/StockListDividend.dc.html` · 390×844 · 원본 `v4 미구현 · plan/v4-stocks.md §4·§5`

- [ ] **div** — “배당주”
      `display:flex align-items:center gap:6px padding:12px 12px 12px`
- [ ] **본문(스크롤 영역)** — “높은 배당수익률”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **div** — “높은 배당수익률”
        `display:flex flex-direction:column gap:9px`
  - [ ] **Card(18)** — “KT&G”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:2px 14px 0`
  - [ ] **p** — “데이터 기준일 2026년 9월 4일 종가 · 설정 › 주식에서 새로 받기 기준에 맞는 종목을 ”
        `font-size:11px line-height:1.5 color:#626D88`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`

## StockDetail — 주식 · 종목 상세

`canvas/StockDetail.dc.html` · 390×844 · 원본 `v4 미구현 · plan/v4-stocks.md §4·§5`

- [ ] **div** — “삼성전자”
      `display:flex align-items:center gap:6px padding:12px 12px 12px`
- [ ] **본문(스크롤 영역)** — “71,200”
      `flex:1 min-height:0 display:flex flex-direction:column gap:6px padding:0 14px 12px`
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

`canvas/StockThemes.dc.html` · 390×844 · 원본 `v4 미구현 · plan/v4-stocks.md §4·§5`

- [ ] **div** — “테마”
      `display:flex align-items:center gap:6px padding:12px 12px 12px`
- [ ] **본문(스크롤 영역)** — “테마는 기준으로 거른 목록이 아니라 업종별로 묶어 둔 이름표예요. 한 종목이 여러 테마에 들어”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **Callout(info)** — “테마는 기준으로 거른 목록이 아니라 업종별로 묶어 둔 이름표예요. 한 종목이 여러 테마에 들어”
        `display:flex gap:8px padding:10px 11px background:#F4F6FB border-radius:12px`
  - [ ] **div** — “반도체”
        `display:grid grid-template-columns:repeat(2, minmax(0, 1fr)) gap:8px`
  - [ ] **p** — “데이터 기준일 2026년 9월 4일 종가 · 설정 › 주식에서 새로 받기 업종별로 묶어 보여주”
        `font-size:11px line-height:1.5 color:#626D88`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`

## StockStates — 참고 · 주식 탭 특수한 상황 8가지

`canvas/StockStates.dc.html` · 1180×975 · 원본 `v4 미구현 · plan/v4-stocks.md §4·§5`

- [ ] text 11px/600 — “구현 참고 · 앱 화면이 아닙니다”
      `font-size:11px font-weight:600 letter-spacing:0.02em color:#475467 border:1px solid #E3E8F1 background:#FFFFFF border-radius:99px padding:4px 10px`
- [ ] text 20px/700 — “주식 탭 · 특수한 상황 8가지”
      `font-size:20px font-weight:700 letter-spacing:-0.025em color:#101828`
- [ ] text 13px/400 — “경고 띠는 알려주기만 하고 아무것도 막지 않아요. 자료가 없는 기준은 —로 두고 충족 수에서 ”
      `font-size:13px line-height:1.55 color:#626D88`
- [ ] **div** — “주식 홈 · 위쪽”
      `display:flex gap:28px align-items:flex-start`

## StockSettings — 모달 · 설정 › 주식

`canvas/StockSettings.dc.html` · 390×844 · 원본 `v4 미구현 · plan/v4-stocks.md §4·§5`

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

`canvas/SnapshotUpdate.dc.html` · 1180×750 · 원본 `v4 미구현 · plan/v4-stocks.md §4·§5`

- [ ] text 11px/600 — “구현 참고 · 앱 화면이 아닙니다”
      `font-size:11px font-weight:600 letter-spacing:0.02em color:#475467 border:1px solid #E3E8F1 background:#FFFFFF border-radius:99px padding:4px 10px`
- [ ] text 20px/700 — “종목 데이터 새로 받기 · 순서대로”
      `font-size:20px font-weight:700 letter-spacing:-0.025em color:#101828`
- [ ] text 13px/400 — “설정 › 주식에서 「새로 받기」를 누르면 이 순서로 바뀌어요. 받다가 실패해도 지금 데이터로 ”
      `font-size:13px line-height:1.55 color:#626D88`
- [ ] **div** — “시작 · 설정 › 주식에서 「새로 받기」를 누르면”
      `display:flex gap:28px align-items:flex-start`

## DaySheet — 하루 시트 · 오늘 (키보드 열림)

`canvas/DaySheet.dc.html` · 390×844 · 원본 `components/navi/day-sheet.tsx (plan/v5-calendar.md §4)`

- [ ] **div**
      `height:30px`
- [ ] **BottomSheet** — “9월 8일 소비 기록”
      `height:534px background:#FFFFFF border:1px solid #E3E8F1 border-bottom:0 border-radius:26px 26px 0 0 display:flex flex-direction:column`
- [ ] **div** — “시스템 숫자 키보드 자리”
      `position:absolute left:0 right:0 bottom:0 height:280px background:#E8ECF5 border-top:1px solid #D7DEEA display:flex align-items:center justify-content:center flex-direction:column gap:4px`

## DaySheetList — 하루 시트 · 기록 있는 과거 날 (목록 우선)

`canvas/DaySheetList.dc.html` · 390×844 · 원본 `components/navi/day-sheet.tsx (plan/v5-calendar.md §4)`

- [ ] **div** — “배경을 눌러 닫기 · 앱이 다시 시작되면 저장하지 않은 내용은 사라져요”
      `flex:1 min-height:0 display:flex align-items:flex-end justify-content:center padding:0 20px 12px text-align:center`
  - [ ] text 11.5px/500 — “배경을 눌러 닫기 · 앱이 다시 시작되면 저장하지 않은 내용은 사라져요”
        `font-size:11.5px font-weight:500 color:rgba(255,255,255,.62)`
- [ ] **BottomSheet** — “9월 3일 소비 기록”
      `background:#FFFFFF border:1px solid #E3E8F1 border-bottom:0 border-radius:26px 26px 0 0 display:flex flex-direction:column`

## DaySheetEdit — 하루 시트 · 수정 모드

`canvas/DaySheetEdit.dc.html` · 390×844 · 원본 `components/navi/day-sheet.tsx (plan/v5-calendar.md §4 · record-15)`

- [ ] **div**
      `height:30px`
- [ ] **BottomSheet** — “9월 3일 기록 수정”
      `height:534px background:#FFFFFF border:1px solid #E3E8F1 border-bottom:0 border-radius:26px 26px 0 0 display:flex flex-direction:column`
- [ ] **div** — “시스템 숫자 키보드 자리”
      `position:absolute left:0 right:0 bottom:0 height:280px background:#E8ECF5 border-top:1px solid #D7DEEA display:flex align-items:center justify-content:center flex-direction:column gap:4px`

## DoneCard — 홈 · 저장 뒤 완료 카드

`canvas/DoneCard.dc.html` · 390×844 · 원본 `components/navi/done-card.tsx (plan/v5-calendar.md §4-4 · record-6 · record-20)`

- [ ] **Header** — “NAVI”
      `display:flex flex-direction:column gap:6px padding:12px 16px 10px`
- [ ] **본문(스크롤 영역)** — “이번 달 소비”
      `flex:1 min-height:0 display:flex flex-direction:column gap:9px padding:0 14px position:relative`
  - [ ] **HeroCard** — “이번 달 소비”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **Card(18)** — “이번 달 소비 기록”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 14px 13px`
  - [ ] **TurnCard** — “다음 안내”
        `display:flex gap:12px background:#FFFFFF border:1px solid #E3E8F1 border-left:3px solid #DE8A2A border-radius:18px padding:13px 14px`
  - [ ] **Card(18)** — “이번 달 한도 오늘 포함 하루 44,700원”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px`
  - [ ] **Card(18)** — “순자산”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:4px 14px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`
- [ ] **div** — “저장했어요”
      `position:absolute left:14px right:14px bottom:78px background:#101828 border-radius:16px padding:13px 14px 12px color:#FFFFFF box-shadow:0 8px 24px rgba(0,0,0,.28)`

## DaySheetConfirm — 참고 · 저장을 한 번 더 물어보는 경우

`canvas/DaySheetConfirm.dc.html` · 1200×1221 · 원본 `components/navi/day-sheet.tsx (plan/v5-calendar.md §4 · record-3 · record-5)`

- [ ] text 11px/600 — “구현 참고 · 앱 화면이 아닙니다”
      `font-size:11px font-weight:600 letter-spacing:0.02em color:#475467 border:1px solid #E3E8F1 background:#FFFFFF border-radius:99px padding:4px 10px`
- [ ] text 20px/700 — “저장을 눌렀는데 한 번 더 물어보는 경우”
      `font-size:20px font-weight:700 letter-spacing:-0.025em color:#101828`
- [ ] **p** — “아래 네 경우에는 바로 저장하지 않고 금액 칸 아래에 안내가 뜹니다. 저장 버튼의 글이 그때의”
      `font-size:13px line-height:1.55 color:#626D88`
- [ ] **div** — “오늘 4건 37,000원”
      `display:flex gap:32px align-items:flex-start`
- [ ] **Card(18)** — “구현 메모”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:10px 18px 8px`

## ClassifySheet — 카테고리 고르기 시트

`canvas/ClassifySheet.dc.html` · 390×844 · 원본 `components/navi/classify-sheet.tsx (plan/v5-calendar.md §5-4 · spending-3)`

- [ ] **div** — “배경을 눌러 닫기”
      `flex:1 min-height:0 display:flex align-items:flex-end justify-content:center padding:0 20px 12px text-align:center`
  - [ ] text 11.5px/500 — “배경을 눌러 닫기”
        `font-size:11.5px font-weight:500 color:rgba(255,255,255,.62)`
- [ ] **BottomSheet** — “카테고리 고르기 · 7건”
      `background:#FFFFFF border:1px solid #E3E8F1 border-bottom:0 border-radius:26px 26px 0 0 display:flex flex-direction:column`

## HeroInsufficient — 홈 · 히어로 이력 부족

`canvas/HeroInsufficient.dc.html` · 390×844 · 원본 `components/navi/home-hero.tsx (plan/v5-calendar.md §3-4 · D9)`

- [ ] **Header** — “NAVI”
      `display:flex flex-direction:column gap:6px padding:12px 16px 10px`
- [ ] **본문(스크롤 영역)** — “이번 달 소비”
      `flex:1 min-height:0 display:flex flex-direction:column gap:9px padding:0 14px`
  - [ ] **HeroCard** — “이번 달 소비”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **Card(18)** — “이번 달 소비 기록”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 14px 13px`
  - [ ] **TurnCard** — “다음 안내”
        `display:flex gap:12px background:#FFFFFF border:1px solid #E3E8F1 border-left:3px solid #DE8A2A border-radius:18px padding:13px 14px`
  - [ ] **Card(18)** — “이번 달 한도 오늘 포함 하루 93,700원”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`

## DaySheet360 — 하루 시트 · 360 × 640 작은 폰

`canvas/DaySheet360.dc.html` · 360×640 · 원본 `components/navi/day-sheet.tsx (plan/v5-calendar.md §4)`

- [ ] **div**
      `height:30px`
- [ ] **BottomSheet** — “9월 8일 소비 기록”
      `height:610px background:#FFFFFF border:1px solid #E3E8F1 border-bottom:0 border-radius:26px 26px 0 0 display:flex flex-direction:column`

## HeroFootnotes — 참고 · 홈 맨 위 카드의 안내 줄

`canvas/HeroFootnotes.dc.html` · 1200×800 · 원본 `components/navi/home-hero.tsx (plan/v5-calendar.md §3-4 · home-8)`

- [ ] text 11px/600 — “구현 참고 · 앱 화면이 아닙니다”
      `font-size:11px font-weight:600 letter-spacing:0.02em color:#475467 border:1px solid #E3E8F1 background:#FFFFFF border-radius:99px padding:4px 10px`
- [ ] text 20px/700 — “홈 맨 위 카드에 붙는 작은 안내 줄”
      `font-size:20px font-weight:700 letter-spacing:-0.025em color:#101828`
- [ ] text 13px/400 — “월말 예상을 계산한 방식에 덧붙일 말이 있을 때만 월급 · 부수입 고치기 줄 아래에 회색 글이”
      `font-size:13px line-height:1.55 color:#626D88`
- [ ] **div** — “이번 달 소비”
      `display:flex gap:32px align-items:flex-start`
- [ ] **p** — “오른쪽 견본은 카드의 아랫부분만 잘라 보여 줍니다. 카드의 나머지는 모든 경우에 같고, 안내 ”
      `font-size:12px line-height:1.6 color:#626D88`

## HomeCalendarStrip — 홈 · 달력 접힘 (7일 줄)

`canvas/HomeCalendarStrip.dc.html` · 390×844 · 원본 `components/navi/calendar-card.tsx · home-hero.tsx (plan/v5-calendar.md §3)`

- [ ] **Header** — “NAVI”
      `display:flex flex-direction:column gap:6px padding:12px 16px 10px`
- [ ] **본문(스크롤 영역)** — “이번 달 소비”
      `flex:1 min-height:0 display:flex flex-direction:column gap:9px padding:0 14px`
  - [ ] **HeroCard** — “이번 달 소비”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **Card(18)** — “이번 달 소비 기록”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 14px 13px`
  - [ ] **TurnCard** — “다음 안내”
        `display:flex gap:12px background:#FFFFFF border:1px solid #E3E8F1 border-left:3px solid #DE8A2A border-radius:18px padding:13px 14px`
  - [ ] **Card(18)** — “이번 달 한도 오늘 포함 하루 45,220원”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px`
  - [ ] **Card(18)** — “순자산”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:4px 14px`
  - [ ] **Card(18)** — “상환 계획”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:4px 14px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`

## HomeCalendar — 홈 · 달력 펼침 (월 달력)

`canvas/HomeCalendar.dc.html` · 390×844 · 원본 `components/navi/calendar-card.tsx (plan/v5-calendar.md §3)`

- [ ] **본문(스크롤 영역)** — “2026년 9월”
      `flex:1 min-height:0 display:flex flex-direction:column gap:9px padding:0 14px`
  - [ ] **div**
        `height:22px background:#FFFFFF border:1px solid #E3E8F1 border-top:none border-radius:0 0 20px 20px opacity:.55`
  - [ ] **Card(18)** — “2026년 9월”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 14px 13px`
  - [ ] **TurnCard** — “다음 안내”
        `display:flex gap:12px background:#FFFFFF border:1px solid #E3E8F1 border-left:3px solid #DE8A2A border-radius:18px padding:13px 14px`
  - [ ] **Card(18)** — “이번 달 한도 오늘 포함 하루 45,220원”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`

## HomeCalendar360 — 홈 · 달력 펼침 · 360px (월 달력 그대로)

`canvas/HomeCalendar360.dc.html` · 360×844 · 원본 `components/navi/calendar-card.tsx (plan/v5-calendar.md §3)`

- [ ] **본문(스크롤 영역)** — “2026년 9월”
      `flex:1 min-height:0 display:flex flex-direction:column gap:9px padding:0 14px`
  - [ ] **div**
        `height:22px background:#FFFFFF border:1px solid #E3E8F1 border-top:none border-radius:0 0 20px 20px opacity:.55`
  - [ ] **Card(18)** — “2026년 9월”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 10px 13px`
  - [ ] **TurnCard** — “다음 안내”
        `display:flex gap:12px background:#FFFFFF border:1px solid #E3E8F1 border-left:3px solid #DE8A2A border-radius:18px padding:13px 14px`
  - [ ] **Card(18)** — “이번 달 한도 오늘 포함 하루 45,220원”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`

## HomeCalendarPrev — 홈 · 달력 펼침 · ‹ 지난달 8월 보기

`canvas/HomeCalendarPrev.dc.html` · 390×844 · 원본 `components/navi/calendar-card.tsx (plan/v5-calendar.md §3 · home-18)`

- [ ] **본문(스크롤 영역)** — “2026년 8월”
      `flex:1 min-height:0 display:flex flex-direction:column gap:9px padding:0 14px`
  - [ ] **div**
        `height:22px background:#FFFFFF border:1px solid #E3E8F1 border-top:none border-radius:0 0 20px 20px opacity:.55`
  - [ ] **Card(18)** — “2026년 8월”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 14px 13px`
  - [ ] **TurnCard** — “다음 안내”
        `display:flex gap:12px background:#FFFFFF border:1px solid #E3E8F1 border-left:3px solid #DE8A2A border-radius:18px padding:13px 14px`
  - [ ] **Card(18)** — “이번 달 한도 오늘 포함 하루 45,220원”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`

## CalendarCells — 참고 · 달력 칸 읽는 법

`canvas/CalendarCells.dc.html` · 1330×880 · 원본 `components/navi/calendar-card.tsx (plan/v5-calendar.md §3 · record-11)`

- [ ] text 11px/600 — “구현 참고 · 앱 화면이 아닙니다”
      `font-size:11px font-weight:600 letter-spacing:0.02em color:#475467 border:1px solid #E3E8F1 background:#FFFFFF border-radius:99px padding:4px 10px`
- [ ] text 20px/700 — “달력 칸 읽는 법”
      `font-size:20px font-weight:700 letter-spacing:-0.025em color:#101828`
- [ ] **p** — “칸의 숫자는 그날 소비 합계입니다(고정비 포함 · 이체 제외). 왼쪽 달력의 번호를 가운데에서”
      `font-size:13px line-height:1.55 color:#626D88`
- [ ] **div** — “2026년 9월”
      `display:flex gap:28px align-items:flex-start`

## CalendarGridSizes — 참고 · 달력을 펼치면 어디서나 월 달력

`canvas/CalendarGridSizes.dc.html` · 1150×1745 · 원본 `components/navi/calendar-card.tsx (plan/v5-calendar.md §3 · home-17)`

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

`canvas/DesktopHomeV5.dc.html` · 1440×1273 · 원본 `v5 · 데스크톱 달력 자리(2026-09-21 결정 · plan/v5-calendar.md §10 10판 메모)`

- [ ] **div** — “NAVI”
      `width:232px background:#FFFFFF display:flex flex-direction:column padding:22px 16px 18px`
- [ ] **div** — “2026년 9월 8일 · 이번 달 오늘 포함 23일 남음”
      `flex:1 display:flex flex-direction:column padding:18px 28px 22px`
  - [ ] **div** — “2026년 9월 8일 · 이번 달 오늘 포함 23일 남음”
        `display:flex align-items:flex-end justify-content:space-between gap:12px margin-top:18px`
  - [ ] **div** — “이번 달 소비”
        `display:grid grid-template-columns:minmax(0, 1.6fr) minmax(0, 1fr) gap:18px margin-top:16px align-items:start`

## HomeSetupStocksOn — 첫 실행 · 홈 구성 · 주식 알림 켬

`canvas/HomeSetupStocksOn.dc.html` · 390×844 · 원본 `components/navi/home-layout-editor.tsx (AMEND 1 · first-run-16 · plan/v4-stocks.md §3)`

- [ ] **div** — “홈 구성”
      `padding:0 20px`
- [ ] **div** — “홈에 무엇을 둘까요?”
      `flex:1 min-height:0 padding:0 20px display:flex flex-direction:column justify-content:flex-end`
  - [ ] **div** — “홈에 무엇을 둘까요?”
        `display:flex flex-direction:column`
- [ ] **div** — “다음”
      `padding:8px 20px 24px display:flex flex-direction:column gap:8px background:#EDF0F7`

## SettingsHomeEntry — 설정

`canvas/SettingsHomeEntry.dc.html` · 390×844 · 원본 `components/navi/settings-sheet.tsx (D5 · home-9)`

- [ ] **div** — “배경을 눌러 닫기”
      `height:60px display:flex align-items:flex-end justify-content:center`
- [ ] **BottomSheet** — “설정”
      `flex:1 min-height:0 background:#FFFFFF border-radius:26px 26px 0 0 display:flex flex-direction:column color:#101828`
  - [ ] **div**
        `display:flex justify-content:center padding:9px 0 0`
  - [ ] **div** — “설정”
        `display:flex align-items:flex-start justify-content:space-between gap:10px padding:12px 18px 14px border-bottom:1px solid #EFF2F8`
  - [ ] **div** — “내 수치”
        `flex:1 min-height:0 padding:14px 18px 14px display:flex flex-direction:column gap:15px`
    - [ ] **Callout(info)** — “내 수치”
          `display:flex align-items:center justify-content:space-between gap:8px min-height:56px padding:10px 13px border-radius:12px background:#F4F6FB`
    - [ ] **div** — “화면”
    - [ ] **div** — “홈 화면”
    - [ ] **div** — “기기 알림”
    - [ ] **div** — “도움말”
    - [ ] **div** — “데이터”
  - [ ] **div** — “닫기”
        `display:flex gap:10px padding:12px 18px 20px border-top:1px solid #EFF2F8`

## HomeLayoutEdit — 설정 › 홈 구성 (처음 실행 뒤에 다시 고칠 때)

`canvas/HomeLayoutEdit.dc.html` · 390×844 · 원본 `components/navi/home-layout-editor.tsx (first-run-15 · plan/v5-calendar.md §12-2)`

- [ ] **div**
      `position:absolute left:0 right:0 bottom:0 height:12px background:#FFFFFF border-top:1px solid #E3E8F1`
- [ ] **div**
      `position:absolute inset:0 background:rgba(0,0,0,.1)`
- [ ] **div** — “홈 구성”
      `position:absolute left:0 top:12px width:390px height:820px background:#EDF0F7 box-shadow:0 0 0 1px rgba(16,24,40,.1) display:flex flex-direction:column`

## DestPayoff — 목적지 · 상환 계획 (5탭)

`canvas/DestPayoff.dc.html` · 390×844 · 원본 `v4 미구현 · plan/v4-stocks.md §4`

- [ ] **div** — “목적지”
      `display:flex flex-direction:column gap:10px padding:14px 16px 12px`
- [ ] **본문(스크롤 영역)** — “저장된 계획”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **Card(18)** — “저장된 계획”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
  - [ ] **Card(18)** — “고금리 우선”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 14px`
  - [ ] **Card(18)** — “저장된 상환 계획이에요”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`

## DaySheetScrolled — 하루 시트 · 키보드를 내린 모습

`canvas/DaySheetScrolled.dc.html` · 390×844 · 원본 `v5 · plan/v5-calendar.md §4`

- [ ] **div**
      `height:30px`
- [ ] **BottomSheet** — “9월 8일 소비 기록”
      `height:814px background:#FFFFFF border:1px solid #E3E8F1 border-bottom:0 border-radius:26px 26px 0 0 display:flex flex-direction:column`

## DaySheetNoSpend — 하루 시트 · 소비 0건인 날 (오늘은 안 썼어요)

`canvas/DaySheetNoSpend.dc.html` · 390×844 · 원본 `v5 · plan/v5-calendar.md §4 · §8`

- [ ] **div** — “배경을 눌러 닫기 · 앱이 다시 시작되면 저장하지 않은 내용은 사라져요”
      `flex:1 min-height:0 display:flex align-items:flex-end justify-content:center padding:0 20px 12px text-align:center`
  - [ ] text 11.5px/500 — “배경을 눌러 닫기 · 앱이 다시 시작되면 저장하지 않은 내용은 사라져요”
        `font-size:11.5px font-weight:500 color:rgba(255,255,255,.62)`
- [ ] **BottomSheet** — “9월 8일 소비 기록”
      `background:#FFFFFF border:1px solid #E3E8F1 border-bottom:0 border-radius:26px 26px 0 0 display:flex flex-direction:column`

## ReviewListSheet — 확인할 내용 목록 시트

`canvas/ReviewListSheet.dc.html` · 390×844 · 원본 `v5 · plan/v5-calendar.md §3-3`

- [ ] **div** — “시안 주석 · 앱에는 보이지 않아요”
      `flex:1 min-height:0 display:flex flex-direction:column justify-content:center`
  - [ ] **div** — “시안 주석 · 앱에는 보이지 않아요”
        `padding:12px 14px border:1px dashed rgba(255,255,255,.32) border-radius:12px display:flex flex-direction:column gap:7px`
- [ ] **div** — “배경을 눌러 닫기”
      `height:60px display:flex align-items:flex-end justify-content:center padding:0 20px 12px text-align:center`
- [ ] **BottomSheet** — “확인할 내용 2개”
      `position:relative background:#FFFFFF border:1px solid #E3E8F1 border-radius:26px 26px 0 0 display:flex flex-direction:column`

## HomeDefaultScroll — 홈 · 기본 카드 4개 전체 스크롤

`canvas/HomeDefaultScroll.dc.html` · 390×1241 · 원본 `v5 · plan/v5-calendar.md §3-1 · §10 2단계`

- [ ] **Header** — “NAVI”
      `display:flex flex-direction:column gap:6px padding:12px 16px 10px`
- [ ] **본문(스크롤 영역)** — “이번 달 소비”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px 14px`
  - [ ] **HeroCard** — “이번 달 소비”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **Card(18)** — “이번 달 소비 기록”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 14px 13px`
  - [ ] **TurnCard** — “다음 안내”
        `display:flex gap:12px background:#FFFFFF border:1px solid #E3E8F1 border-left:3px solid #DE8A2A border-radius:18px padding:13px 14px`
  - [ ] **Card(18)** — “이번 달 한도 오늘 포함 하루 45,220원”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px`
  - [ ] **Card(18)** — “순자산”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:4px 14px`
  - [ ] **Card(18)** — “상환 계획”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:4px 14px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`

## CalendarStatusLines — 참고 · 달력 아래 한 줄이 바뀌는 경우

`canvas/CalendarStatusLines.dc.html` · 1200×2629 · 원본 `v5 · plan/v5-calendar.md §3-3`

- [ ] text 11px/600 — “구현 참고 · 앱 화면이 아닙니다”
      `font-size:11px font-weight:600 letter-spacing:0.02em color:#475467 border:1px solid #E3E8F1 background:#FFFFFF border-radius:99px padding:4px 10px`
- [ ] text 20px/700 — “달력 아래 한 줄이 바뀌는 경우”
      `font-size:20px font-weight:700 letter-spacing:-0.025em color:#101828`
- [ ] **p** — “접어 둔 달력의 날짜 칸 아래에는 오늘 합계를 말하는 한 문장과 적기 알약(오늘 기록이 없으면”
      `font-size:13px line-height:1.55 color:#626D88`
- [ ] **div** — “이번 달 소비 기록”
      `display:flex gap:32px align-items:flex-start`

## DaySheetStates — 참고 · 기록 창의 글이 바뀌는 경우

`canvas/DaySheetStates.dc.html` · 1210×1919 · 원본 `v5 · plan/v5-calendar.md §4 · §8`

- [ ] text 11px/600 — “구현 참고 · 앱 화면이 아닙니다”
      `font-size:11px font-weight:600 letter-spacing:0.02em color:#475467 border:1px solid #E3E8F1 background:#FFFFFF border-radius:99px padding:4px 10px`
- [ ] text 20px/700 — “기록 창의 글이 바뀌는 경우”
      `font-size:20px font-weight:700 letter-spacing:-0.025em color:#101828`
- [ ] text 13px/400 — “기록 창은 하나이고, 날짜 · 시간 · 입력한 값에 따라 아래 다섯 자리의 글과 모양만 바뀝니”
      `font-size:13px line-height:1.55 color:#626D88`
- [ ] **div** — “오늘 4건 37,000원2”
      `display:flex gap:32px align-items:flex-start`
- [ ] **Card(18)** — “구현 메모”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:10px 18px 8px`

## DaySheetNoSpendStates — 참고 · 안 쓴 날을 표시하는 경우

`canvas/DaySheetNoSpendStates.dc.html` · 1200×1252 · 원본 `v5 · plan/v5-calendar.md §4 · §8`

- [ ] text 11px/600 — “구현 참고 · 앱 화면이 아닙니다”
      `font-size:11px font-weight:600 letter-spacing:0.02em color:#475467 border:1px solid #E3E8F1 background:#FFFFFF border-radius:99px padding:4px 10px`
- [ ] text 20px/700 — “안 쓴 날을 표시하는 경우”
      `font-size:20px font-weight:700 letter-spacing:-0.025em color:#101828`
- [ ] text 13px/400 — “소비가 한 건도 없는 날에만 기록 창 맨 아래에 오늘은 안 썼어요가 보입니다. 누르면 달력의 ”
      `font-size:13px line-height:1.55 color:#626D88`
- [ ] **div** — “오늘 소비는 아직 기록이 없어요 · 이체 300,000원(소비율 제외)1”
      `display:flex gap:32px align-items:flex-start`
- [ ] **Card(18)** — “구현 메모”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:10px 18px 8px`

## DoneCardStates — 참고 · 저장 완료 카드의 경우들

`canvas/DoneCardStates.dc.html` · 1200×1534 · 원본 `v5 · plan/v5-calendar.md §4-4`

- [ ] text 11px/600 — “구현 참고 · 앱 화면이 아닙니다”
      `font-size:11px font-weight:600 letter-spacing:0.02em color:#475467 border:1px solid #E3E8F1 background:#FFFFFF border-radius:99px padding:4px 10px`
- [ ] text 20px/700 — “저장 완료 카드의 경우들”
      `font-size:20px font-weight:700 letter-spacing:-0.025em color:#101828`
- [ ] text 13px/400 — “저장이 끝나면 홈 아래쪽에 뜨는 카드 하나가 제목 · 셋째 줄 · 행동만 바꿔 가며 모든 경우”
      `font-size:13px line-height:1.55 color:#626D88`
- [ ] **div** — “저장했어요”
      `display:flex gap:32px align-items:flex-start`

## LedgerV5 — 소비 · 내역 (카테고리 없음 칩 · 날짜별 합계)

`canvas/LedgerV5.dc.html` · 390×844 · 원본 `v5 · plan/v5-calendar.md §9 · components/navi/spending-tab.tsx`

- [ ] **div** — “소비”
      `display:flex flex-direction:column gap:10px padding:14px 16px 12px`
- [ ] **본문(스크롤 영역)** — “메모·카테고리 검색”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **Card(18)** — “메모·카테고리 검색”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
  - [ ] **Card(18)** — “9월 8일 화요일 · 오늘”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:4px 14px 10px`
  - [ ] **div** — “기록 기준”
        `display:flex align-items:center justify-content:space-between height:46px padding:0 14px background:#FFFFFF border:1px solid #E3E8F1 border-radius:16px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`

## MonthlyCloseV5 — 모달 · 8월 첫 마감 (카테고리 없음 안내)

`canvas/MonthlyCloseV5.dc.html` · 390×1099 · 원본 `v5 · plan/v5-calendar.md §9`

- [ ] **div** — “배경을 눌러 닫기”
      `height:40px display:flex align-items:flex-end justify-content:center`
- [ ] **BottomSheet** — “8월 마감”
      `flex:1 min-height:0 background:#FFFFFF border-radius:26px 26px 0 0 display:flex flex-direction:column color:#101828`
  - [ ] **div**
        `display:flex justify-content:center padding:9px 0 0`
  - [ ] **div** — “8월 마감”
        `display:flex align-items:flex-start justify-content:space-between gap:10px padding:12px 18px 14px border-bottom:1px solid #EFF2F8`
  - [ ] **div** — “지금 값으로 채운 칸은 그 달 값으로 고쳐 주세요”
        `flex:1 min-height:0 padding:14px 18px 14px display:flex flex-direction:column gap:12px`
    - [ ] **Callout(warn)** — “지금 값으로 채운 칸은 그 달 값으로 고쳐 주세요”
          `padding:10px 12px background:#FDF1E0 border-radius:12px font-size:12.5px color:#7A3E0A`
    - [ ] **div** — “그 달의 실제 수치”
    - [ ] **div** — “카테고리 없음 3건 · 21,200원이 기타로 들어가요 · 다음 달 한도 배분에도 기타로 들어”
          `padding:11px 13px border:1px solid #E3E8F1 border-radius:12px font-size:12.5px line-height:1.55 color:#475467`
    - [ ] **div** — “자동으로 채워진 값”
    - [ ] **div** — “바뀐 게 있으면 자산 고치기 ›”
          `display:flex align-items:center justify-content:space-between height:46px padding:0 14px border-radius:12px border:1px solid #E3E8F1`
    - [ ] text 12px/400 — “소비 합계는 기록에서 계산해요. 마감 뒤 기록을 고치면 합계를 고치라고 알려 드려요.”
          `font-size:12px line-height:1.5 color:#626D88`
  - [ ] **div** — “월급 칸이 비어 있어요 · 이 달 월급 대비 소비율은 —로 남아요”
        `padding:11px 18px 12px background:#F4F6FB border-top:1px solid #E3E8F1`
  - [ ] **div** — “취소”
        `display:flex gap:10px padding:12px 18px 20px border-top:1px solid #EFF2F8`

## TransactionAddFromDaySheet — 참고 · 기록 추가 — 하루 시트에서 넘어왔을 때

`canvas/TransactionAddFromDaySheet.dc.html` · 960×908 · 원본 `v5 · plan/v5-calendar.md §4`

- [ ] text 11px/600 — “구현 참고 · 앱 화면이 아닙니다”
      `font-size:11px font-weight:600 letter-spacing:0.02em color:#475467 border:1px solid #E3E8F1 background:#FFFFFF border-radius:99px padding:4px 10px white-space:nowrap`
- [ ] text 20px/700 — “기록 추가 — 하루 시트에서 넘어왔을 때”
      `font-size:20px font-weight:700 letter-spacing:-0.025em color:#101828`
- [ ] text 13px/400 — “하루 시트 아래의 링크 「저축·투자로 기록 ›」를 누르면 자세한 기록 추가 창이 이 모습으로 ”
      `font-size:13px line-height:1.55 color:#626D88`
- [ ] **div** — “기록 추가”
      `display:flex gap:28px align-items:flex-start`

## InsufficientElsewhere — 참고 · 월말 예상 기준이 서기 전 — 홈 밖의 화면들

`canvas/InsufficientElsewhere.dc.html` · 1230×1864 · 원본 `v5 · plan/v5-calendar.md §3-4 · §9-22`

- [ ] text 11px/600 — “구현 참고 · 앱 화면이 아닙니다”
      `font-size:11px font-weight:600 letter-spacing:0.02em color:#475467 border:1px solid #E3E8F1 background:#FFFFFF border-radius:99px padding:4px 10px`
- [ ] text 20px/700 — “월말 예상 기준이 서기 전 — 홈 밖의 화면들”
      `font-size:20px font-weight:700 letter-spacing:-0.025em color:#101828`
- [ ] **p** — “홈의 이력 부족 상태(HeroInsufficient)와 같은 사람입니다 — 9월 5일에 처음 ”
      `font-size:13px line-height:1.55 color:#626D88`
- [ ] **div** — “1”
      `display:flex gap:24px align-items:flex-start`
- [ ] **Card(18)** — “구현 메모”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:10px 18px 8px`

## FutureProvisional — 참고 · 미래 · 목적지의 임시 계산 표시

`canvas/FutureProvisional.dc.html` · 1230×1256 · 원본 `v5 · plan/v5-calendar.md §3-4`

- [ ] text 11px/600 — “구현 참고 · 앱 화면이 아닙니다”
      `font-size:11px font-weight:600 letter-spacing:0.02em color:#475467 border:1px solid #E3E8F1 background:#FFFFFF border-radius:99px padding:4px 10px`
- [ ] text 20px/700 — “미래 · 목적지 — 월말 예상 기준이 서기 전의 임시 계산 표시”
      `font-size:20px font-weight:700 letter-spacing:-0.025em color:#101828`
- [ ] text 13px/400 — “8월을 마감하기 전에도 미래 · 목적지 화면의 예상 값은 그대로 보여 주되 임시 계산이라고 표”
      `font-size:13px line-height:1.55 color:#626D88`
- [ ] **div** — “미래”
      `display:flex gap:32px align-items:flex-start`

## LimitCardCases — 참고 · 이번 달 한도 카드의 경우들

`canvas/LimitCardCases.dc.html` · 1200×1462 · 원본 `v5 · plan/v5-calendar.md §10 3단계`

- [ ] text 11px/600 — “구현 참고 · 앱 화면이 아닙니다”
      `font-size:11px font-weight:600 letter-spacing:0.02em color:#475467 border:1px solid #E3E8F1 background:#FFFFFF border-radius:99px padding:4px 10px`
- [ ] text 20px/700 — “이번 달 한도 카드 — 하루 금액 자리의 경우들”
      `font-size:20px font-weight:700 letter-spacing:-0.025em color:#101828`
- [ ] text 13px/400 — “홈 한도 카드의 하루 금액은 늘 오늘 포함 남은 날로 나눈 값입니다. 한도가 없을 때 · 0원”
      `font-size:13px line-height:1.55 color:#626D88`
- [ ] **div** — “평소 — 한도가 남아 있을 때”
      `display:flex gap:32px align-items:flex-start`
- [ ] **Card(18)** — “구현 메모”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:10px 18px 8px`

## RecurringPrefill — 반복 기록 · 방금 저장한 기록으로 미리 채움

`canvas/RecurringPrefill.dc.html` · 390×877 · 원본 `v5 · plan/v5-calendar.md §10 3단계`

- [ ] **div** — “배경을 눌러 닫기”
      `height:40px display:flex align-items:flex-end justify-content:center`
- [ ] **BottomSheet** — “반복 기록”
      `flex:1 min-height:0 background:#FFFFFF border-radius:26px 26px 0 0 display:flex flex-direction:column color:#101828`
  - [ ] **div**
        `display:flex justify-content:center padding:9px 0 0`
  - [ ] **div** — “반복 기록”
        `display:flex align-items:flex-start justify-content:space-between gap:10px padding:12px 18px 14px border-bottom:1px solid #EFF2F8`
  - [ ] **div** — “등록된 규칙”
        `flex:1 min-height:0 padding:14px 18px 0 display:flex flex-direction:column gap:15px`
    - [ ] **div** — “등록된 규칙”
    - [ ] **div** — “새 규칙”
  - [ ] **div** — “닫기”
        `display:flex gap:10px padding:12px 18px 20px border-top:1px solid #EFF2F8`

## EtcSubline — 참고 · 카테고리 없는 소비와 안 쓴 날 — 소비 · 한도 · 코치

`canvas/EtcSubline.dc.html` · 1200×1715 · 원본 `v5 · plan/v5-calendar.md §5-3 · §9`

- [ ] text 11px/600 — “구현 참고 · 앱 화면이 아닙니다”
      `font-size:11px font-weight:600 letter-spacing:0.02em color:#475467 border:1px solid #E3E8F1 background:#FFFFFF border-radius:99px padding:4px 10px`
- [ ] text 20px/700 — “카테고리 없는 소비와 안 쓴 날 — 소비 · 한도 · 코치에서”
      `font-size:20px font-weight:700 letter-spacing:-0.025em color:#101828`
- [ ] text 13px/400 — “하루 시트에서 카테고리 없이 저장한 소비는 기타로 들어가요. 소비 · 한도 화면은 기타 아래에”
      `font-size:13px line-height:1.55 color:#626D88`
- [ ] **div** — “1”
      `display:flex gap:24px align-items:flex-start`
- [ ] **Card(18)** — “구현 메모”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:10px 18px 8px`

## ImportBackupNotes — 참고 · 가져오기 · 백업 안내

`canvas/ImportBackupNotes.dc.html` · 1230×1103 · 원본 `v5 · plan/v5-calendar.md §10 3단계`

- [ ] text 11px/600 — “구현 참고 · 앱 화면이 아닙니다”
      `font-size:11px font-weight:600 letter-spacing:0.02em color:#475467 border:1px solid #E3E8F1 background:#FFFFFF border-radius:99px padding:4px 10px`
- [ ] text 20px/700 — “가져오기 · 백업 — 확인 표시와 카테고리 없음 표시가 어떻게 따라오는지”
      `font-size:20px font-weight:700 letter-spacing:-0.025em color:#101828`
- [ ] **p** — “달력의 확인 표시(다 적었어요 · 안 썼어요)와 카테고리 없음 표시는 백업 파일에 함께 들어갑”
      `font-size:13px line-height:1.55 color:#626D88`
- [ ] **div** — “백업 불러오기”
      `display:flex gap:32px align-items:flex-start`

## TourHome1 — 첫 실행 안내 · 홈 1 / 3 이번 달 소비

`canvas/TourHome1.dc.html` · 390×844 · 원본 `components/navi/first-run-tour.tsx · lib/navi-tour.ts TOUR_STEPS · lib/navi-tour-policy.ts (AMEND 2 · first-run-3/4/21)`

- [ ] **Header** — “NAVI”
      `display:flex flex-direction:column gap:6px padding:12px 16px 10px`
- [ ] **본문(스크롤 영역)** — “이번 달 소비”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px 14px`
  - [ ] **HeroCard** — “이번 달 소비”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **Card(18)** — “이번 달 소비 기록”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 14px 13px`
  - [ ] **TurnCard** — “다음 안내”
        `display:flex gap:12px background:#FFFFFF border:1px solid #E3E8F1 border-left:3px solid #DE8A2A border-radius:18px padding:13px 14px`
  - [ ] **Card(18)** — “이번 달 한도 오늘 포함 하루 45,220원”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px`
  - [ ] **Card(18)** — “순자산”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:4px 14px`
  - [ ] **Card(18)** — “상환 계획”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:4px 14px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`
- [ ] **div** — “처음 안내”
      `position:absolute left:0 top:0 width:390px height:778px`

## TourHome2 — 첫 실행 안내 · 홈 2 / 3 달력으로 기록

`canvas/TourHome2.dc.html` · 390×844 · 원본 `components/navi/first-run-tour.tsx · lib/navi-tour.ts TOUR_STEPS · lib/navi-tour-policy.ts (AMEND 2 · first-run-3/4/21)`

- [ ] **Header** — “NAVI”
      `display:flex flex-direction:column gap:6px padding:12px 16px 10px`
- [ ] **본문(스크롤 영역)** — “이번 달 소비”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px 14px`
  - [ ] **HeroCard** — “이번 달 소비”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **Card(18)** — “이번 달 소비 기록”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 14px 13px`
  - [ ] **TurnCard** — “다음 안내”
        `display:flex gap:12px background:#FFFFFF border:1px solid #E3E8F1 border-left:3px solid #DE8A2A border-radius:18px padding:13px 14px`
  - [ ] **Card(18)** — “이번 달 한도 오늘 포함 하루 45,220원”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px`
  - [ ] **Card(18)** — “순자산”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:4px 14px`
  - [ ] **Card(18)** — “상환 계획”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:4px 14px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`
- [ ] **div** — “처음 안내”
      `position:absolute left:0 top:0 width:390px height:778px`

## TourHome3 — 첫 실행 안내 · 홈 3 / 3 다음 안내

`canvas/TourHome3.dc.html` · 390×844 · 원본 `components/navi/first-run-tour.tsx · lib/navi-tour.ts TOUR_STEPS · lib/navi-tour-policy.ts (AMEND 2 · first-run-3/4/21)`

- [ ] **Header** — “NAVI”
      `margin-top:-397px display:flex flex-direction:column gap:6px padding:12px 16px 10px`
- [ ] **본문(스크롤 영역)** — “이번 달 소비”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px 14px`
  - [ ] **HeroCard** — “이번 달 소비”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **Card(18)** — “이번 달 소비 기록”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 14px 13px`
  - [ ] **TurnCard** — “다음 안내”
        `display:flex gap:12px background:#FFFFFF border:1px solid #E3E8F1 border-left:3px solid #DE8A2A border-radius:18px padding:13px 14px`
  - [ ] **Card(18)** — “이번 달 한도 오늘 포함 하루 45,220원”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px`
  - [ ] **Card(18)** — “순자산”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:4px 14px`
  - [ ] **Card(18)** — “상환 계획”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:4px 14px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`
- [ ] **div** — “처음 안내”
      `position:absolute left:0 top:0 width:390px height:778px`

## TourAssets1 — 첫 실행 안내 · 자산 1 / 3 세 탭

`canvas/TourAssets1.dc.html` · 390×844 · 원본 `components/navi/first-run-tour.tsx · lib/navi-tour.ts TOUR_STEPS · lib/navi-tour-policy.ts (AMEND 2 · first-run-3/4/21)`

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
- [ ] **div** — “처음 안내”
      `position:absolute left:0 top:0 width:390px height:778px`

## TourAssets2 — 첫 실행 안내 · 자산 2 / 3 순자산

`canvas/TourAssets2.dc.html` · 390×844 · 원본 `components/navi/first-run-tour.tsx · lib/navi-tour.ts TOUR_STEPS · lib/navi-tour-policy.ts (AMEND 2 · first-run-3/4/21)`

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
- [ ] **div** — “처음 안내”
      `position:absolute left:0 top:0 width:390px height:778px`

## TourAssets3 — 첫 실행 안내 · 자산 3 / 3 현금성 비상금

`canvas/TourAssets3.dc.html` · 390×844 · 원본 `components/navi/first-run-tour.tsx · lib/navi-tour.ts TOUR_STEPS · lib/navi-tour-policy.ts (AMEND 2 · first-run-3/4/21)`

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
- [ ] **div** — “처음 안내”
      `position:absolute left:0 top:0 width:390px height:778px`

## TourSpending1 — 첫 실행 안내 · 소비 1 / 3 세 탭

`canvas/TourSpending1.dc.html` · 390×844 · 원본 `components/navi/first-run-tour.tsx · lib/navi-tour.ts TOUR_STEPS · lib/navi-tour-policy.ts (AMEND 2 · first-run-3/4/21)`

- [ ] **div** — “소비”
      `display:flex flex-direction:column gap:10px padding:14px 16px 12px`
- [ ] **본문(스크롤 영역)** — “31.1”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **HeroCard** — “31.1”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px 14px 14px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **Card(18)** — “카테고리별 소비”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
  - [ ] **div** — “소비 추이·절감 기회”
        `display:flex align-items:center gap:8px height:46px padding:0 14px background:#FFFFFF border:1px solid #E3E8F1 border-radius:16px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`
- [ ] **div** — “처음 안내”
      `position:absolute left:0 top:0 width:390px height:778px`

## TourSpending2 — 첫 실행 안내 · 소비 2 / 3 속도 그래프

`canvas/TourSpending2.dc.html` · 390×844 · 원본 `components/navi/first-run-tour.tsx · lib/navi-tour.ts TOUR_STEPS · lib/navi-tour-policy.ts (AMEND 2 · first-run-3/4/21)`

- [ ] **div** — “소비”
      `display:flex flex-direction:column gap:10px padding:14px 16px 12px`
- [ ] **본문(스크롤 영역)** — “31.1”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **HeroCard** — “31.1”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px 14px 14px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **Card(18)** — “카테고리별 소비”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
  - [ ] **div** — “소비 추이·절감 기회”
        `display:flex align-items:center gap:8px height:46px padding:0 14px background:#FFFFFF border:1px solid #E3E8F1 border-radius:16px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`
- [ ] **div** — “처음 안내”
      `position:absolute left:0 top:0 width:390px height:778px`

## TourSpending3 — 첫 실행 안내 · 소비 3 / 3 카테고리

`canvas/TourSpending3.dc.html` · 390×844 · 원본 `components/navi/first-run-tour.tsx · lib/navi-tour.ts TOUR_STEPS · lib/navi-tour-policy.ts (AMEND 2 · first-run-3/4/21)`

- [ ] **div** — “소비”
      `margin-top:-151px display:flex flex-direction:column gap:10px padding:14px 16px 12px`
- [ ] **본문(스크롤 영역)** — “31.1”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **HeroCard** — “31.1”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px 14px 14px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **Card(18)** — “카테고리별 소비”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
  - [ ] **div** — “소비 추이·절감 기회”
        `display:flex align-items:center gap:8px height:46px padding:0 14px background:#FFFFFF border:1px solid #E3E8F1 border-radius:16px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`
- [ ] **div** — “처음 안내”
      `position:absolute left:0 top:0 width:390px height:778px`

## TourGoals1 — 첫 실행 안내 · 목적지 1 / 3 매달 모으는 돈

`canvas/TourGoals1.dc.html` · 390×844 · 원본 `components/navi/first-run-tour.tsx · lib/navi-tour.ts TOUR_STEPS · lib/navi-tour-policy.ts (AMEND 2 · first-run-3/4/21)`

- [ ] **div** — “목적지”
      `display:flex flex-direction:column gap:10px padding:14px 16px 12px`
- [ ] **본문(스크롤 영역)** — “매달 모으는 돈”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **HeroCard** — “매달 모으는 돈”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:15px 16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **Card(18)** — “진행 중인 목적지”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px 8px`
  - [ ] **div** — “목적지 추가”
        `display:flex align-items:center justify-content:center gap:6px height:46px border-radius:14px border:1.5px dashed #B9C3D6 background:rgba(255,255,255,.55) color:#3556E6 font-size:14px font-weight:600`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`
- [ ] **div** — “처음 안내”
      `position:absolute left:0 top:0 width:390px height:778px`

## TourGoals2 — 첫 실행 안내 · 목적지 2 / 3 도착 예상

`canvas/TourGoals2.dc.html` · 390×844 · 원본 `components/navi/first-run-tour.tsx · lib/navi-tour.ts TOUR_STEPS · lib/navi-tour-policy.ts (AMEND 2 · first-run-3/4/21)`

- [ ] **div** — “목적지”
      `display:flex flex-direction:column gap:10px padding:14px 16px 12px`
- [ ] **본문(스크롤 영역)** — “매달 모으는 돈”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **HeroCard** — “매달 모으는 돈”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:15px 16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **Card(18)** — “진행 중인 목적지”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px 8px`
  - [ ] **div** — “목적지 추가”
        `display:flex align-items:center justify-content:center gap:6px height:46px border-radius:14px border:1.5px dashed #B9C3D6 background:rgba(255,255,255,.55) color:#3556E6 font-size:14px font-weight:600`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`
- [ ] **div** — “처음 안내”
      `position:absolute left:0 top:0 width:390px height:778px`

## TourGoals3 — 첫 실행 안내 · 목적지 3 / 3 목적지 추가

`canvas/TourGoals3.dc.html` · 390×844 · 원본 `components/navi/first-run-tour.tsx · lib/navi-tour.ts TOUR_STEPS · lib/navi-tour-policy.ts (AMEND 2 · first-run-3/4/21)`

- [ ] **div** — “목적지”
      `margin-top:-186px display:flex flex-direction:column gap:10px padding:14px 16px 12px`
- [ ] **본문(스크롤 영역)** — “매달 모으는 돈”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **HeroCard** — “매달 모으는 돈”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:15px 16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **Card(18)** — “진행 중인 목적지”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px 8px`
  - [ ] **div** — “목적지 추가”
        `display:flex align-items:center justify-content:center gap:6px height:46px border-radius:14px border:1.5px dashed #B9C3D6 background:rgba(255,255,255,.55) color:#3556E6 font-size:14px font-weight:600`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`
- [ ] **div** — “처음 안내”
      `position:absolute left:0 top:0 width:390px height:778px`

## TourFuture1 — 첫 실행 안내 · 미래 1 / 3 자산 경로

`canvas/TourFuture1.dc.html` · 390×844 · 원본 `components/navi/first-run-tour.tsx · lib/navi-tour.ts TOUR_STEPS · lib/navi-tour-policy.ts (AMEND 2 · first-run-3/4/21)`

- [ ] **div** — “미래”
      `display:flex flex-direction:column gap:10px padding:14px 16px 12px`
- [ ] **본문(스크롤 영역)** — “기간”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **HeroCard** — “기간”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:14px 14px 13px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **Card(18)** — “다음 자산 지점”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 14px 5px`
  - [ ] **Card(18)** — “10년 뒤 +0원”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:11px 14px 11px`
  - [ ] **Card(18)** — “투자 환경별 비교 · 전체 경로”
        `display:flex align-items:center justify-content:space-between gap:8px height:70px padding:12px 14px background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px`
  - [ ] **Card(18)** — “계산 방법 자세히”
        `height:86px padding:13px background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px`
  - [ ] **div** — “앞으로의 금액은 100만원 단위로 어림해 「약」을 붙였어요. 지금 금액은 입력한 그대로예요. ”
        `display:flex gap:8px padding:2px 4px 0 margin-top:21px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`
- [ ] **div** — “처음 안내”
      `position:absolute left:0 top:0 width:390px height:778px`

## TourFuture2 — 첫 실행 안내 · 미래 2 / 3 다음 지점

`canvas/TourFuture2.dc.html` · 390×844 · 원본 `components/navi/first-run-tour.tsx · lib/navi-tour.ts TOUR_STEPS · lib/navi-tour-policy.ts (AMEND 2 · first-run-3/4/21)`

- [ ] **div** — “미래”
      `display:flex flex-direction:column gap:10px padding:14px 16px 12px`
- [ ] **본문(스크롤 영역)** — “기간”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **HeroCard** — “기간”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:14px 14px 13px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **Card(18)** — “다음 자산 지점”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 14px 5px`
  - [ ] **Card(18)** — “10년 뒤 +0원”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:11px 14px 11px`
  - [ ] **Card(18)** — “투자 환경별 비교 · 전체 경로”
        `display:flex align-items:center justify-content:space-between gap:8px height:70px padding:12px 14px background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px`
  - [ ] **Card(18)** — “계산 방법 자세히”
        `height:86px padding:13px background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px`
  - [ ] **div** — “앞으로의 금액은 100만원 단위로 어림해 「약」을 붙였어요. 지금 금액은 입력한 그대로예요. ”
        `display:flex gap:8px padding:2px 4px 0 margin-top:21px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`
- [ ] **div** — “처음 안내”
      `position:absolute left:0 top:0 width:390px height:778px`

## TourFuture3 — 첫 실행 안내 · 미래 3 / 3 가정

`canvas/TourFuture3.dc.html` · 390×844 · 원본 `components/navi/first-run-tour.tsx · lib/navi-tour.ts TOUR_STEPS · lib/navi-tour-policy.ts (AMEND 2 · first-run-3/4/21)`

- [ ] **div** — “미래”
      `margin-top:-398px display:flex flex-direction:column gap:10px padding:14px 16px 12px`
- [ ] **본문(스크롤 영역)** — “기간”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **HeroCard** — “기간”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:14px 14px 13px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **Card(18)** — “다음 자산 지점”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 14px 5px`
  - [ ] **Card(18)** — “10년 뒤 +0원”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:11px 14px 11px`
  - [ ] **Card(18)** — “투자 환경별 비교 · 전체 경로”
        `display:flex align-items:center justify-content:space-between gap:8px height:70px padding:12px 14px background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px`
  - [ ] **Card(18)** — “계산 방법 자세히”
        `height:86px padding:13px background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px`
  - [ ] **div** — “앞으로의 금액은 100만원 단위로 어림해 「약」을 붙였어요. 지금 금액은 입력한 그대로예요. ”
        `display:flex gap:8px padding:2px 4px 0 margin-top:21px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`
- [ ] **div** — “처음 안내”
      `position:absolute left:0 top:0 width:390px height:778px`

## TourDebts1 — 첫 실행 안내 · 부채 1 / 3 총부채

`canvas/TourDebts1.dc.html` · 390×844 · 원본 `components/navi/first-run-tour.tsx · lib/navi-tour.ts TOUR_STEPS · lib/navi-tour-policy.ts (AMEND 2 · first-run-3/4/21)`

- [ ] **div** — “자산”
      `display:flex flex-direction:column gap:10px padding:14px 16px 12px`
- [ ] **본문(스크롤 영역)** — “총부채”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **HeroCard** — “총부채”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **TurnCard** — “상환 안내”
        `display:flex gap:12px background:#FFFFFF border:1px solid #E3E8F1 border-left:3px solid #DE8A2A border-radius:18px padding:13px 14px`
  - [ ] **Card(18)** — “부채 4건”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
  - [ ] **Card(18)** — “이번 달 상환 예정”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 14px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`
- [ ] **div** — “처음 안내”
      `position:absolute left:0 top:0 width:390px height:778px`

## TourDebts2 — 첫 실행 안내 · 부채 2 / 3 상환 안내

`canvas/TourDebts2.dc.html` · 390×844 · 원본 `components/navi/first-run-tour.tsx · lib/navi-tour.ts TOUR_STEPS · lib/navi-tour-policy.ts (AMEND 2 · first-run-3/4/21)`

- [ ] **div** — “자산”
      `display:flex flex-direction:column gap:10px padding:14px 16px 12px`
- [ ] **본문(스크롤 영역)** — “총부채”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **HeroCard** — “총부채”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **TurnCard** — “상환 안내”
        `display:flex gap:12px background:#FFFFFF border:1px solid #E3E8F1 border-left:3px solid #DE8A2A border-radius:18px padding:13px 14px`
  - [ ] **Card(18)** — “부채 4건”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
  - [ ] **Card(18)** — “이번 달 상환 예정”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 14px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`
- [ ] **div** — “처음 안내”
      `position:absolute left:0 top:0 width:390px height:778px`

## TourDebts3 — 첫 실행 안내 · 부채 3 / 3 부채 목록

`canvas/TourDebts3.dc.html` · 390×844 · 원본 `components/navi/first-run-tour.tsx · lib/navi-tour.ts TOUR_STEPS · lib/navi-tour-policy.ts (AMEND 2 · first-run-3/4/21)`

- [ ] **div** — “자산”
      `display:flex flex-direction:column gap:10px padding:14px 16px 12px`
- [ ] **본문(스크롤 영역)** — “총부채”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **HeroCard** — “총부채”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **TurnCard** — “상환 안내”
        `display:flex gap:12px background:#FFFFFF border:1px solid #E3E8F1 border-left:3px solid #DE8A2A border-radius:18px padding:13px 14px`
  - [ ] **Card(18)** — “부채 4건”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
  - [ ] **Card(18)** — “이번 달 상환 예정”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 14px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`
- [ ] **div** — “처음 안내”
      `position:absolute left:0 top:0 width:390px height:778px`

## TourStrategy1 — 첫 실행 안내 · 자산 › 상환 계획 1 / 3 저장된 계획

`canvas/TourStrategy1.dc.html` · 390×844 · 원본 `components/navi/first-run-tour.tsx · lib/navi-tour.ts TOUR_STEPS · lib/navi-tour-policy.ts (AMEND 2 · first-run-3/4/21)`

- [ ] **div** — “자산”
      `display:flex flex-direction:column gap:10px padding:14px 16px 12px`
- [ ] **본문(스크롤 영역)** — “저장된 상환 계획”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **HeroCard** — “저장된 상환 계획”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **Card(18)** — “다 갚는 달”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
  - [ ] **Card(18)** — “갚는 순서”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`
- [ ] **div** — “처음 안내”
      `position:absolute left:0 top:0 width:390px height:778px`

## TourStrategy2 — 첫 실행 안내 · 자산 › 상환 계획 2 / 3 다 갚는 달

`canvas/TourStrategy2.dc.html` · 390×844 · 원본 `components/navi/first-run-tour.tsx · lib/navi-tour.ts TOUR_STEPS · lib/navi-tour-policy.ts (AMEND 2 · first-run-3/4/21)`

- [ ] **div** — “자산”
      `display:flex flex-direction:column gap:10px padding:14px 16px 12px`
- [ ] **본문(스크롤 영역)** — “저장된 상환 계획”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **HeroCard** — “저장된 상환 계획”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **Card(18)** — “다 갚는 달”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
  - [ ] **Card(18)** — “갚는 순서”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`
- [ ] **div** — “처음 안내”
      `position:absolute left:0 top:0 width:390px height:778px`

## TourStrategy3 — 첫 실행 안내 · 자산 › 상환 계획 3 / 3 갚는 순서

`canvas/TourStrategy3.dc.html` · 390×844 · 원본 `components/navi/first-run-tour.tsx · lib/navi-tour.ts TOUR_STEPS · lib/navi-tour-policy.ts (AMEND 2 · first-run-3/4/21)`

- [ ] **div** — “자산”
      `display:flex flex-direction:column gap:10px padding:14px 16px 12px`
- [ ] **본문(스크롤 영역)** — “저장된 상환 계획”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **HeroCard** — “저장된 상환 계획”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **Card(18)** — “다 갚는 달”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
  - [ ] **Card(18)** — “갚는 순서”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`
- [ ] **div** — “처음 안내”
      `position:absolute left:0 top:0 width:390px height:778px`

## TourLedger1 — 첫 실행 안내 · 내역 1 / 3 검색 · 칩

`canvas/TourLedger1.dc.html` · 390×844 · 원본 `components/navi/first-run-tour.tsx · lib/navi-tour.ts TOUR_STEPS · lib/navi-tour-policy.ts (AMEND 2 · first-run-3/4/21)`

- [ ] **div** — “소비”
      `display:flex flex-direction:column gap:10px padding:14px 16px 12px`
- [ ] **본문(스크롤 영역)** — “메모·카테고리 검색”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **Card(18)** — “메모·카테고리 검색”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
  - [ ] **Card(18)** — “9월 8일 화요일 · 오늘”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:4px 14px 10px`
  - [ ] **div** — “기록 기준”
        `display:flex align-items:center justify-content:space-between height:46px padding:0 14px background:#FFFFFF border:1px solid #E3E8F1 border-radius:16px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`
- [ ] **div** — “처음 안내”
      `position:absolute left:0 top:0 width:390px height:778px`

## TourLedger2 — 첫 실행 안내 · 내역 2 / 3 날짜 묶음

`canvas/TourLedger2.dc.html` · 390×844 · 원본 `components/navi/first-run-tour.tsx · lib/navi-tour.ts TOUR_STEPS · lib/navi-tour-policy.ts (AMEND 2 · first-run-3/4/21)`

- [ ] **div** — “소비”
      `margin-top:-365px display:flex flex-direction:column gap:10px padding:14px 16px 12px`
- [ ] **본문(스크롤 영역)** — “메모·카테고리 검색”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **Card(18)** — “메모·카테고리 검색”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
  - [ ] **Card(18)** — “9월 8일 화요일 · 오늘”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:4px 14px 10px`
  - [ ] **div** — “기록 기준”
        `display:flex align-items:center justify-content:space-between height:46px padding:0 14px background:#FFFFFF border:1px solid #E3E8F1 border-radius:16px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`
- [ ] **div** — “처음 안내”
      `position:absolute left:0 top:0 width:390px height:778px`

## TourLedger3 — 첫 실행 안내 · 내역 3 / 3 기록 추가

`canvas/TourLedger3.dc.html` · 390×844 · 원본 `components/navi/first-run-tour.tsx · lib/navi-tour.ts TOUR_STEPS · lib/navi-tour-policy.ts (AMEND 2 · first-run-3/4/21)`

- [ ] **div** — “소비”
      `margin-top:-53px display:flex flex-direction:column gap:10px padding:14px 16px 12px`
- [ ] **본문(스크롤 영역)** — “메모·카테고리 검색”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **Card(18)** — “메모·카테고리 검색”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
  - [ ] **Card(18)** — “9월 8일 화요일 · 오늘”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:4px 14px 10px`
  - [ ] **div** — “기록 기준”
        `display:flex align-items:center justify-content:space-between height:46px padding:0 14px background:#FFFFFF border:1px solid #E3E8F1 border-radius:16px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`
- [ ] **div** — “처음 안내”
      `position:absolute left:0 top:0 width:390px height:778px`

## TourLimits1 — 첫 실행 안내 · 한도 1 / 3 총한도

`canvas/TourLimits1.dc.html` · 390×844 · 원본 `components/navi/first-run-tour.tsx · lib/navi-tour.ts TOUR_STEPS · lib/navi-tour-policy.ts (AMEND 2 · first-run-3/4/21)`

- [ ] **div** — “소비”
      `display:flex flex-direction:column gap:10px padding:14px 16px 12px`
- [ ] **본문(스크롤 영역)** — “이번 달 총한도”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **HeroCard** — “이번 달 총한도”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **Card(18)** — “소비 경고”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px 14px 12px`
  - [ ] **Card(18)** — “카테고리 배분”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
  - [ ] **div** — “이 한도는 어떻게 계산했나요?”
        `display:flex align-items:center justify-content:space-between gap:8px background:#FFFFFF border:1px solid #E3E8F1 border-radius:14px padding:0 14px height:50px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`
- [ ] **div** — “처음 안내”
      `position:absolute left:0 top:0 width:390px height:778px`

## TourLimits2 — 첫 실행 안내 · 한도 2 / 3 카테고리 배분

`canvas/TourLimits2.dc.html` · 390×844 · 원본 `components/navi/first-run-tour.tsx · lib/navi-tour.ts TOUR_STEPS · lib/navi-tour-policy.ts (AMEND 2 · first-run-3/4/21)`

- [ ] **div** — “소비”
      `margin-top:-300px display:flex flex-direction:column gap:10px padding:14px 16px 12px`
- [ ] **본문(스크롤 영역)** — “이번 달 총한도”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **HeroCard** — “이번 달 총한도”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **Card(18)** — “소비 경고”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px 14px 12px`
  - [ ] **Card(18)** — “카테고리 배분”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
  - [ ] **div** — “이 한도는 어떻게 계산했나요?”
        `display:flex align-items:center justify-content:space-between gap:8px background:#FFFFFF border:1px solid #E3E8F1 border-radius:14px padding:0 14px height:50px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`
- [ ] **div** — “처음 안내”
      `position:absolute left:0 top:0 width:390px height:778px`

## TourLimits3 — 첫 실행 안내 · 한도 3 / 3 계산 근거

`canvas/TourLimits3.dc.html` · 390×844 · 원본 `components/navi/first-run-tour.tsx · lib/navi-tour.ts TOUR_STEPS · lib/navi-tour-policy.ts (AMEND 2 · first-run-3/4/21)`

- [ ] **div** — “소비”
      `margin-top:-300px display:flex flex-direction:column gap:10px padding:14px 16px 12px`
- [ ] **본문(스크롤 영역)** — “이번 달 총한도”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **HeroCard** — “이번 달 총한도”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **Card(18)** — “소비 경고”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px 14px 12px`
  - [ ] **Card(18)** — “카테고리 배분”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
  - [ ] **div** — “이 한도는 어떻게 계산했나요?”
        `display:flex align-items:center justify-content:space-between gap:8px background:#FFFFFF border:1px solid #E3E8F1 border-radius:14px padding:0 14px height:50px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`
- [ ] **div** — “처음 안내”
      `position:absolute left:0 top:0 width:390px height:778px`

## TourGoalDesign1 — 첫 실행 안내 · 새 목적지 설계 1 / 3 두 탭

`canvas/TourGoalDesign1.dc.html` · 390×844 · 원본 `components/navi/first-run-tour.tsx · lib/navi-tour.ts TOUR_STEPS · lib/navi-tour-policy.ts (AMEND 2 · first-run-3/4/21)`

- [ ] **div** — “목적지”
      `display:flex flex-direction:column gap:10px padding:14px 16px 12px`
- [ ] **본문(스크롤 영역)** — “추천 목적지에서 시작”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **Card(18)** — “추천 목적지에서 시작”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 14px`
  - [ ] **HeroCard** — “이름”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:15px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **Card(18)** — “다른 금액으로 계산해 보기 · 계산 기준”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:15px 14px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`
- [ ] **div** — “처음 안내”
      `position:absolute left:0 top:0 width:390px height:778px`

## TourGoalDesign2 — 첫 실행 안내 · 새 목적지 설계 2 / 3 추천

`canvas/TourGoalDesign2.dc.html` · 390×844 · 원본 `components/navi/first-run-tour.tsx · lib/navi-tour.ts TOUR_STEPS · lib/navi-tour-policy.ts (AMEND 2 · first-run-3/4/21)`

- [ ] **div** — “목적지”
      `display:flex flex-direction:column gap:10px padding:14px 16px 12px`
- [ ] **본문(스크롤 영역)** — “추천 목적지에서 시작”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **Card(18)** — “추천 목적지에서 시작”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 14px`
  - [ ] **HeroCard** — “이름”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:15px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **Card(18)** — “다른 금액으로 계산해 보기 · 계산 기준”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:15px 14px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`
- [ ] **div** — “처음 안내”
      `position:absolute left:0 top:0 width:390px height:778px`

## TourGoalDesign3 — 첫 실행 안내 · 새 목적지 설계 3 / 3 입력

`canvas/TourGoalDesign3.dc.html` · 390×844 · 원본 `components/navi/first-run-tour.tsx · lib/navi-tour.ts TOUR_STEPS · lib/navi-tour-policy.ts (AMEND 2 · first-run-3/4/21)`

- [ ] **div** — “목적지”
      `display:flex flex-direction:column gap:10px padding:14px 16px 12px`
- [ ] **본문(스크롤 영역)** — “추천 목적지에서 시작”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **Card(18)** — “추천 목적지에서 시작”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 14px`
  - [ ] **HeroCard** — “이름”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:15px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **Card(18)** — “다른 금액으로 계산해 보기 · 계산 기준”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:15px 14px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`
- [ ] **div** — “처음 안내”
      `position:absolute left:0 top:0 width:390px height:778px`

## TourPayoff1 — 첫 실행 안내 · 미래 › 상환 계획 1 / 3 추가 상환

`canvas/TourPayoff1.dc.html` · 390×844 · 원본 `components/navi/first-run-tour.tsx · lib/navi-tour.ts TOUR_STEPS · lib/navi-tour-policy.ts (AMEND 2 · first-run-3/4/21)`

- [ ] **div** — “미래”
      `display:flex flex-direction:column gap:10px padding:14px 16px 12px`
- [ ] **본문(스크롤 영역)** — “저장된 계획”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **Card(18)** — “저장된 계획”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
  - [ ] **Card(18)** — “고금리 우선”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 14px`
  - [ ] **Card(18)** — “저장된 상환 계획이에요”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`
- [ ] **div** — “처음 안내”
      `position:absolute left:0 top:0 width:390px height:778px`

## TourPayoff2 — 첫 실행 안내 · 미래 › 상환 계획 2 / 3 비교

`canvas/TourPayoff2.dc.html` · 390×844 · 원본 `components/navi/first-run-tour.tsx · lib/navi-tour.ts TOUR_STEPS · lib/navi-tour-policy.ts (AMEND 2 · first-run-3/4/21)`

- [ ] **div** — “미래”
      `display:flex flex-direction:column gap:10px padding:14px 16px 12px`
- [ ] **본문(스크롤 영역)** — “저장된 계획”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **Card(18)** — “저장된 계획”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
  - [ ] **Card(18)** — “고금리 우선”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 14px`
  - [ ] **Card(18)** — “저장된 상환 계획이에요”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`
- [ ] **div** — “처음 안내”
      `position:absolute left:0 top:0 width:390px height:778px`

## TourPayoff3 — 첫 실행 안내 · 미래 › 상환 계획 3 / 3 저장

`canvas/TourPayoff3.dc.html` · 390×844 · 원본 `components/navi/first-run-tour.tsx · lib/navi-tour.ts TOUR_STEPS · lib/navi-tour-policy.ts (AMEND 2 · first-run-3/4/21)`

- [ ] **div** — “미래”
      `margin-top:-118px display:flex flex-direction:column gap:10px padding:14px 16px 12px`
- [ ] **본문(스크롤 영역)** — “저장된 계획”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **Card(18)** — “저장된 계획”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
  - [ ] **Card(18)** — “고금리 우선”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 14px`
  - [ ] **Card(18)** — “저장된 상환 계획이에요”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`
- [ ] **div** — “처음 안내”
      `position:absolute left:0 top:0 width:390px height:778px`

## SettingsNotify — 모달 · 설정 › 알림 (기기 알림)

`canvas/SettingsNotify.dc.html` · 390×903 · 원본 `components/navi/notify-settings.tsx (plan/v5-calendar.md §14 · tasks-12)`

- [ ] **div**
      `height:24px`
- [ ] **BottomSheet** — “알림”
      `flex:1 min-height:0 background:#FFFFFF border-radius:26px 26px 0 0 display:flex flex-direction:column color:#101828`
  - [ ] **div**
        `display:flex justify-content:center padding:9px 0 0`
  - [ ] **div** — “알림”
        `display:flex align-items:flex-start justify-content:space-between gap:10px padding:12px 18px 14px border-bottom:1px solid #EFF2F8`
  - [ ] **div** — “조용한 시간”
        `flex:1 min-height:0 padding:14px 18px 14px display:flex flex-direction:column gap:15px`
    - [ ] **div** — “조용한 시간”
          `margin-top:0px`
    - [ ] **div** — “알림”
          `margin-top:3px`
    - [ ] **div** — “확인”
          `margin-top:3px`
    - [ ] **div** — “절전 상태와 기기 설정에 따라 늦거나 빠질 수 있어요. 앱을 35일 넘게 안 열면 예약이 멈춰”
          `margin-top:3px`
  - [ ] **div** — “닫기”
        `display:flex gap:10px padding:12px 18px 20px border-top:1px solid #EFF2F8`

## NotifyCases — 참고 · 기기 알림 여섯 가지와 규칙

`canvas/NotifyCases.dc.html` · 1200×1435 · 원본 `lib/navi-notify.ts · components/navi/notify-settings.tsx (plan/v5-calendar.md §14)`

- [ ] text 11px/600 — “구현 참고 · 앱 화면이 아닙니다”
      `font-size:11px font-weight:600 letter-spacing:0.02em color:#475467 border:1px solid #E3E8F1 background:#FFFFFF border-radius:99px padding:4px 10px`
- [ ] text 20px/700 — “기기 알림 — 여섯 가지와 규칙”
      `font-size:20px font-weight:700 letter-spacing:-0.025em color:#101828`
- [ ] **p** — “앱 안 알림 창과 별개로, 앱을 안 켜고 있을 때 시각으로 오는 안드로이드 로컬 알림입니다. ”
      `font-size:13px line-height:1.55 color:#626D88`
- [ ] **div** — “1”
      `display:grid grid-template-columns:repeat(3, 362px) gap:26px 28px align-items:start`
- [ ] **div** — “규칙”
      `margin-top:22px padding:16px 18px background:#FFFFFF border:1px solid #E3E8F1 border-radius:16px`

## SpendingPastOpen — 소비 · 지난 달 (마감 전)

`canvas/SpendingPastOpen.dc.html` · 390×1264 · 원본 `components/navi/spending-overview.tsx 월 마감 카드 (spending-4 · D9)`

- [ ] **div** — “소비”
      `display:flex flex-direction:column gap:10px padding:14px 16px 12px`
- [ ] **div** — “지난 달에는 한도 탭이 없어요 · 기록은 내역에서 고쳐요”
      `display:flex align-items:center gap:7px padding:0 16px 10px`
- [ ] **본문(스크롤 영역)** — “8월은 아직 마감하지 않았어요”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **Card(18)** — “8월은 아직 마감하지 않았어요”
        `background:#FFFFFF border:1.5px solid #DE8A2A border-radius:18px padding:13px 14px`
  - [ ] **HeroCard** — “지난 달 기록”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **Card(18)** — “31일 동안 이렇게 썼어요”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
  - [ ] **Card(18)** — “카테고리”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
  - [ ] **Card(18)** — “소비 추이·절감 기회”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px 16px`
- [ ] **div**
      `height:12px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`

## SpendingPastChanged — 소비 · 지난 달 (마감 뒤 기록이 바뀜)

`canvas/SpendingPastChanged.dc.html` · 390×1212 · 원본 `components/navi/spending-overview.tsx · reclose-spend-dialog.tsx (record-1 · D9)`

- [ ] **div** — “소비”
      `display:flex flex-direction:column gap:10px padding:14px 16px 12px`
- [ ] **div** — “지난 달에는 한도 탭이 없어요 · 기록은 내역에서 고쳐요”
      `display:flex align-items:center gap:7px padding:0 16px 10px`
- [ ] **본문(스크롤 영역)** — “8월 마감 뒤 기록이 바뀌었어요”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **Card(18)** — “8월 마감 뒤 기록이 바뀌었어요”
        `background:#FFFFFF border:1px solid #DE8A2A border-radius:18px padding:13px 15px`
  - [ ] **HeroCard** — “마감한 달”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **Card(18)** — “31일 동안 이렇게 썼어요”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
  - [ ] **Card(18)** — “카테고리”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
  - [ ] **Card(18)** — “소비 추이·절감 기회”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px 16px`
- [ ] **div**
      `height:12px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`

## ProfileDialogNoItems — 모달 · 내 수치 (자산 · 부채를 안 넣었을 때)

`canvas/ProfileDialogNoItems.dc.html` · 390×844 · 원본 `components/navi/numbers-sheet.tsx (D5 · first-run-2)`

- [ ] **div** — “배경을 눌러 닫기”
      `height:60px display:flex align-items:flex-end justify-content:center`
- [ ] **BottomSheet** — “내 수치”
      `flex:1 min-height:0 background:#FFFFFF border-radius:26px 26px 0 0 display:flex flex-direction:column color:#101828`
  - [ ] **div**
        `display:flex justify-content:center padding:9px 0 0`
  - [ ] **div** — “내 수치”
        `display:flex align-items:flex-start justify-content:space-between gap:10px padding:12px 18px 14px border-bottom:1px solid #EFF2F8`
  - [ ] **div** — “기본”
        `flex:1 min-height:0 padding:14px 18px 0 display:flex flex-direction:column gap:15px`
    - [ ] **div** — “기본”
    - [ ] **div** — “소비 목표”
    - [ ] **div** — “추가 설정”
  - [ ] **div** — “취소”
        `display:flex gap:10px padding:12px 18px 20px border-top:1px solid #EFF2F8`

## SalarySheet — 모달 · 월급 입력

`canvas/SalarySheet.dc.html` · 390×844 · 원본 `components/navi/salary-sheet.tsx (D5 · first-run-22)`

- [ ] **div** — “배경을 눌러 닫기”
      `flex:0 1 447px min-height:12px display:flex align-items:flex-end justify-content:center`
- [ ] **BottomSheet** — “월급 입력”
      `flex:1 0 auto background:#FFFFFF border-radius:26px 26px 0 0 display:flex flex-direction:column color:#101828`
  - [ ] **div**
        `display:flex justify-content:center padding:9px 0 0`
  - [ ] **div** — “월급 입력”
        `display:flex align-items:flex-start justify-content:space-between gap:10px padding:12px 18px 14px border-bottom:1px solid #EFF2F8`
  - [ ] **div** — “월급 (실수령)”
        `flex:1 0 auto padding:14px 18px 14px display:flex flex-direction:column gap:15px`
    - [ ] **div** — “월급 (실수령)”
          `flex:0 0 auto`
    - [ ] text 13px/600 — “소비 목표 60% · 월 216만원까지”
          `font-size:13px font-weight:600 line-height:19.5px color:#101828 margin-top:-9px`
    - [ ] text 13px/600 — “다른 수치도 입력하기 ›”
          `display:flex align-items:center height:44px font-size:13px font-weight:600 color:#3556E6`
  - [ ] **div** — “나중에”
        `display:flex gap:10px padding:12px 18px 20px border-top:1px solid #EFF2F8`

## NetWorthRatioSheet — 모달 · 순자산 대비 소비

`canvas/NetWorthRatioSheet.dc.html` · 390×844 · 원본 `components/navi/net-worth-ratio-sheet.tsx (home-8)`

- [ ] **div**
      `height:551px`
- [ ] **BottomSheet** — “순자산 대비 소비”
      `flex:1 min-height:0 position:relative background:#FFFFFF border:1px solid #E3E8F1 border-bottom:0 border-radius:26px 26px 0 0 display:flex flex-direction:column`
  - [ ] **GrabHandle**
        `position:absolute top:8px left:50% width:38px height:4px border-radius:99px background:#D7DEEA`
  - [ ] **div** — “순자산 대비 소비”
        `padding:24px 56px 20px 20px display:flex flex-direction:column gap:8px`
  - [ ] **div** — “자산 탭에서 보기”
        `margin-top:auto display:flex gap:10px padding:14px 20px 15px border-top:1px solid #EFF2F8`

## AssetEditDialog — 모달 · 자산 수정

`canvas/AssetEditDialog.dc.html` · 390×844 · 원본 `components/navi/asset-view.tsx (assets-4)`

- [ ] **Scrim여백** — “배경을 눌러 닫기”
      `height:190px display:flex align-items:flex-end justify-content:center`
- [ ] **BottomSheet** — “자산 수정”
      `flex:1 min-height:0 background:#FFFFFF border-radius:26px 26px 0 0 display:flex flex-direction:column color:#101828`
  - [ ] **div**
        `display:flex justify-content:center padding:9px 0 0`
  - [ ] **div** — “자산 수정”
        `display:flex align-items:flex-start justify-content:space-between gap:10px padding:12px 18px 14px border-bottom:1px solid #EFF2F8`
  - [ ] **div** — “자산 이름 *”
        `flex:1 min-height:0 padding:14px 18px 14px display:flex flex-direction:column gap:15px`
    - [ ] **div** — “자산 이름 *”
          `flex:0 0 auto`
    - [ ] **div** — “유형”
          `display:flex gap:10px align-items:flex-start margin-top:0px`
    - [ ] **div** — “수익률 (연) 선택 사항”
          `flex:0 0 auto`
    - [ ] **div** — “지금 적용 연 2.5% · 직접 입력 마지막 확인 2026년 9월 1일”
          `font-size:11.5px line-height:17.25px color:#475467 margin-top:-9px`
  - [ ] **div** — “취소”
        `display:flex gap:10px padding:12px 18px 20px border-top:1px solid #EFF2F8`

## AssetBalanceCheck — 모달 · 잔액 한 번에 확인 (자산 구성의 주황 띠에서 · 확인 필요 2개)

`canvas/AssetBalanceCheck.dc.html` · 390×844 · 원본 `components/navi/balance-check-sheet.tsx (assets-15)`

- [ ] **Scrim여백** — “배경을 눌러 닫기”
      `height:190px display:flex align-items:flex-end justify-content:center`
- [ ] **BottomSheet** — “잔액 한 번에 확인”
      `flex:1 min-height:0 background:#FFFFFF border-radius:26px 26px 0 0 display:flex flex-direction:column color:#101828`
  - [ ] **div**
        `display:flex justify-content:center padding:9px 0 0`
  - [ ] **div** — “잔액 한 번에 확인”
        `display:flex align-items:flex-start justify-content:space-between gap:10px padding:12px 18px 14px border-bottom:1px solid #EFF2F8`
  - [ ] **div** — “2개 중 0개 확인함”
        `flex:1 min-height:0 padding:14px 18px 0 display:flex flex-direction:column gap:15px`
    - [ ] text 11.5px/600 — “2개 중 0개 확인함”
          `font-size:11.5px font-weight:600 line-height:17px color:#626D88`
    - [ ] **div** — “ETF 계좌”
          `display:flex flex-direction:column gap:10px`
  - [ ] **div** — “닫기”
        `display:flex gap:10px padding:12px 18px 20px border-top:1px solid #EFF2F8`

## RecurringDialogOverlap — 모달 · 반복 기록 (이번 달 겹침 확인)

`canvas/RecurringDialogOverlap.dc.html` · 390×945 · 원본 `components/navi/spending-view.tsx 반복 기록 (record-2)`

- [ ] **div** — “배경을 눌러 닫기”
      `height:40px display:flex align-items:flex-end justify-content:center`
- [ ] **BottomSheet** — “반복 기록”
      `flex:1 min-height:0 background:#FFFFFF border-radius:26px 26px 0 0 display:flex flex-direction:column color:#101828`
  - [ ] **div**
        `display:flex justify-content:center padding:9px 0 0`
  - [ ] **div** — “반복 기록”
        `display:flex align-items:flex-start justify-content:space-between gap:10px padding:12px 18px 14px border-bottom:1px solid #EFF2F8`
  - [ ] **div** — “등록된 규칙”
        `flex:1 min-height:0 padding:14px 18px 0 display:flex flex-direction:column gap:15px`
    - [ ] **div** — “등록된 규칙”
    - [ ] **div** — “새 규칙”
    - [ ] **Callout(info)** — “9월 1일에 같은 금액(주거/관리 320,000원)이 이미 있어요 — 이번 달은 건너뛸까요?”
          `padding:11px 12px margin-top:12px background:#F4F6FB border-radius:12px display:flex flex-direction:column gap:9px`
  - [ ] **div** — “닫기”
        `display:flex gap:10px padding:12px 18px 20px border-top:1px solid #EFF2F8`

## AssetDebtTypes — 참고 · 자산 · 부채 유형 목록 · 새 부채 · 다 갚은 부채

`canvas/AssetDebtTypes.dc.html` · 1400×770 · 원본 `lib/navi-asset-labels.ts · components/navi/asset-view.tsx (assets-6 · assets-7 · assets-14 · assets-23)`

- [ ] text 11px/600 — “구현 참고 · 앱 화면이 아닙니다”
      `font-size:11px font-weight:600 letter-spacing:0.02em color:#475467 border:1px solid #E3E8F1 background:#FFFFFF border-radius:99px padding:4px 10px white-space:nowrap`
- [ ] text 20px/700 — “자산 · 부채 유형 목록 · 새 부채 · 다 갚은 부채”
      `font-size:20px font-weight:700 letter-spacing:-0.025em color:#101828`
- [ ] text 13px/400 — “자산 · 부채 창에서 「유형」을 열었을 때의 목록과, 새 부채를 넣는 창의 처음 모습, 다 갚”
      `font-size:13px line-height:1.55 color:#626D88`
- [ ] **div** — “자산 유형 열기”
      `display:flex gap:22px align-items:flex-start`

## GoalsStates — 참고 · 목적지 상태 7종 (가정 · 펼침 · 도착 · 목표일 없음 · 도착 어려움 · 상환 늦음 · 설계 미리 보기)

`canvas/GoalsStates.dc.html` · 390×4432 · 원본 `components/navi/goals-view.tsx 매달 모으는 돈 가정 · 한 줄 펼침 · 도착한 목적지 (goals-9 · goals-10 · goals-7 · goals-24 · goals-26 · D13)`

- [ ] **div** — “구현 참고 · 앱 화면이 아닙니다”
      `padding:0 2px 6px`
- [ ] text 11px/600 — “A · 「매달 모으는 돈 바꿔 보기 ›」로 110만원을 넣어 본 가정”
      `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
- [ ] **Card(20)** — “매달 모으는 돈”
      `background:#FFFFFF border:1.5px dashed #B79BFF border-radius:20px padding:15px 16px`
- [ ] **Card(20)** — “매달 모으는 돈을 바꾸면?”
      `background:#FFFFFF border:1.5px dashed #B79BFF border-radius:20px padding:15px 16px`
- [ ] **Card(18)** — “진행 중인 목적지”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px 8px`
- [ ] text 11.5px/400 — “바뀐 목적지 줄만 보라 점선 + 「가정」 칩이고, 매달 · 도착 글자도 보라예요. 「가정 종료”
      `font-size:11.5px line-height:1.5 color:#626D88 padding:0 4px`
- [ ] text 11px/600 — “B · 비상금 6개월 한 줄을 펼쳤을 때”
      `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
- [ ] **Card(18)** — “68%”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px 14px`
- [ ] text 11.5px/400 — “「홈에 표시」는 홈 구성에 「대표 목적지」 카드를 켠 사람에게만 뜻이 있어요 — 기본 홈에는 ”
      `font-size:11.5px line-height:1.5 color:#626D88 padding:0 4px`
- [ ] text 11px/600 — “C · 비상금이 도착했을 때(1,500 / 1,500만원)”
      `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
- [ ] **Card(18)** — “매달 모으는 돈”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:15px 16px`
- [ ] **Card(18)** — “진행 중인 목적지”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px 8px`
- [ ] **div** — “목적지 추가”
      `display:flex align-items:center justify-content:center gap:6px height:46px border-radius:14px border:1.5px dashed #B9C3D6 background:rgba(255,255,255,.55) color:#3556E6 font-size:14px font-weight:600`
- [ ] **Card(18)** — “도착한 목적지 1개”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px 8px`
- [ ] text 11.5px/400 — “도착한 목적지는 진행 중 목록과 「모두 도착하려면」에서 빠지고 「목적지 추가」 아래 「도착한 ”
      `font-size:11.5px line-height:1.5 color:#626D88 padding:0 4px`
- [ ] text 11px/600 — “D ① · 목표일이 없는 목적지가 있을 때(투자 계좌의 목표일을 지운 경우)”
      `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
- [ ] **Card(18)** — “매달 모으는 돈”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:15px 16px`
- [ ] **Card(18)** — “진행 중인 목적지”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px 8px`
- [ ] text 11.5px/400 — “그 목적지는 매달 나눠 넣는 계산에서 빠지고(오른쪽 줄 「목표일이 있는 목적지에 80만원」) ”
      `font-size:11.5px line-height:1.5 color:#626D88 padding:0 4px`
- [ ] text 11px/600 — “D ② · 지금 배분으로는 도착하기 어려울 때(목표액 3억원 · 360개월 넘게 걸림)”
      `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
- [ ] **Card(18)** — “7%”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:4px 14px`
- [ ] text 11.5px/400 — “도착 달 대신 빨간 「지금 배분으로는 도착하기 어려워요」 · 날짜 없음. 이때 맨 위는 「모두”
      `font-size:11.5px line-height:1.5 color:#626D88 padding:0 4px`
- [ ] text 11px/600 — “D ③ · 부채 상환 목적지가 목표일보다 늦을 때(목표일 2029년 3월 8일 · 펼친 모습)”
      `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
- [ ] **Card(18)** — “31%”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:4px 14px`
- [ ] text 11.5px/400 — “「상환 계획대로」 대신 빨간 「목표일보다 약 1년 8개월 늦어요」, 펼치면 상태가 「상환 조정”
      `font-size:11.5px line-height:1.5 color:#626D88 padding:0 4px`
- [ ] text 11px/600 — “D ④ · 새 목적지 설계 — 저장하면 새 목적지가 도착하기 어려울 때(목표액 3억원)”
      `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
- [ ] **Card(18)** — “저장하면 이렇게 바뀌어요”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 15px`
- [ ] text 11.5px/400 — “새 목적지 줄이 빨간 「지금 배분으로는 도착하기 어려워요」, 기존 목적지가 360개월을 넘기면”
      `font-size:11.5px line-height:1.5 color:#626D88 padding:0 4px`

## GoalDesignStates — 참고 · 새 목적지 설계 상태 2종 (처음 · 다른 금액 가정)

`canvas/GoalDesignStates.dc.html` · 390×1421 · 원본 `components/navi/goal-tools.tsx 처음 · 다른 금액으로 계산해 보기 (goals-16 · goals-28 · D13)`

- [ ] **div** — “구현 참고 · 앱 화면이 아닙니다”
      `padding:0 2px 6px`
- [ ] text 11px/600 — “A · 처음 들어갔을 때 — 목표액과 기간이 비어 있음”
      `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
- [ ] **HeroCard** — “이름”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:15px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
- [ ] text 11.5px/400 — “빈 칸은 빨간 오류가 아니라 회색 안내 한 줄이에요. 목표액 · 기간을 넣으면 매달 넣어야 할”
      `font-size:11.5px line-height:1.5 color:#626D88 padding:0 4px`
- [ ] text 11px/600 — “B · 「다른 금액으로 계산해 보기」에 매달 30만원을 넣었을 때”
      `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
- [ ] **HeroCard** — “결혼 자금 · 목표액 3,000만원 · 지금 모은 돈 500만원 · 7년 · 수익률 연 4%”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:15px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
- [ ] **Card(18)** — “매달 30만원 넣는 가정 · 계산 기준”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
- [ ] text 11.5px/400 — “보라 점선 · 「가정」은 금액을 넣은 뒤에만 그려요. 넣은 금액은 저장되지 않아요.”
      `font-size:11.5px line-height:1.5 color:#626D88 padding:0 4px`

## HomeTargetEditor — 홈 · 소비 목표 조정 열림

`canvas/HomeTargetEditor.dc.html` · 390×844 · 원본 `components/navi/home-hero.tsx 소비 목표 조정 편집기 (home-1 · D1 · D4)`

- [ ] **Header** — “NAVI”
      `display:flex flex-direction:column gap:6px padding:12px 16px 10px`
- [ ] **본문(스크롤 영역)** — “이번 달 소비”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **HeroCard** — “이번 달 소비”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **Card(18)** — “이번 달 소비 기록”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 14px 13px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`

## HomeMonthStart — 홈 · 달이 바뀐 첫 주 (10월 2일)

`canvas/HomeMonthStart.dc.html` · 390×1118 · 원본 `components/navi/calendar-card.tsx 최근 7일 제목 · home-hero 0건 (home-17 · home-6 · D9 · first-run-5)`

- [ ] **Header** — “NAVI”
      `display:flex flex-direction:column gap:6px padding:12px 16px 10px`
- [ ] **본문(스크롤 영역)** — “이번 달 소비”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px 14px`
  - [ ] **HeroCard** — “이번 달 소비”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **Card(18)** — “최근 7일 소비 기록”
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

## HomeSampleMode — 홈 · 샘플 모드

`canvas/HomeSampleMode.dc.html` · 390×1246 · 원본 `app/page.tsx 샘플 띠 · calendar-card 샘플 문장 (D8 · language-ia-21 · first-run-17 · D9)`

- [ ] **SampleBanner** — “샘플 데이터로 둘러보는 중”
      `display:flex align-items:center justify-content:space-between gap:8px height:32px padding:0 14px background:#E9EDFD`
- [ ] **Header** — “NAVI”
      `display:flex flex-direction:column gap:6px padding:12px 16px 10px`
- [ ] **본문(스크롤 영역)** — “이번 달 소비”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px 14px`
  - [ ] **HeroCard** — “이번 달 소비”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **Card(18)** — “이번 달 소비 기록”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 14px 13px`
  - [ ] **TurnCard** — “다음 안내”
        `display:flex gap:12px background:#FFFFFF border:1px solid #E3E8F1 border-left:3px solid #DE8A2A border-radius:18px padding:13px 14px`
  - [ ] **Card(18)** — “이번 달 한도 오늘 포함 하루 45,220원”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px`
  - [ ] **Card(18)** — “순자산”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:4px 14px`
  - [ ] **Card(18)** — “상환 계획”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:4px 14px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`

## DaySheetPastEmpty — 하루 시트 · 기록 없는 어제

`canvas/DaySheetPastEmpty.dc.html` · 390×844 · 원본 `components/navi/day-sheet.tsx 어제 · 빈 날 (record-11 · record-18)`

- [ ] **div** — “배경을 눌러 닫기 · 앱이 다시 시작되면 저장하지 않은 내용은 사라져요”
      `flex:1 min-height:0 display:flex align-items:flex-end justify-content:center padding:0 20px 12px text-align:center`
  - [ ] text 11.5px/500 — “배경을 눌러 닫기 · 앱이 다시 시작되면 저장하지 않은 내용은 사라져요”
        `font-size:11.5px font-weight:500 color:rgba(255,255,255,.62)`
- [ ] **BottomSheet** — “9월 7일 소비 기록”
      `background:#FFFFFF border:1px solid #E3E8F1 border-bottom:0 border-radius:26px 26px 0 0 display:flex flex-direction:column`

## DaySheetDeleted — 하루 시트 · 지운 뒤 (되돌리기)

`canvas/DaySheetDeleted.dc.html` · 390×844 · 원본 `components/navi/day-sheet.tsx inlineNotice (record-6 · D10)`

- [ ] **div** — “배경을 눌러 닫기 · 앱이 다시 시작되면 저장하지 않은 내용은 사라져요”
      `flex:1 min-height:0 display:flex align-items:flex-end justify-content:center padding:0 20px 12px text-align:center`
  - [ ] text 11.5px/500 — “배경을 눌러 닫기 · 앱이 다시 시작되면 저장하지 않은 내용은 사라져요”
        `font-size:11.5px font-weight:500 color:rgba(255,255,255,.62)`
- [ ] **BottomSheet** — “9월 3일 소비 기록”
      `background:#FFFFFF border:1px solid #E3E8F1 border-bottom:0 border-radius:26px 26px 0 0 display:flex flex-direction:column`

## DaySheetEditMoved — 하루 시트 · 수정 · 날짜를 옮길 때

`canvas/DaySheetEditMoved.dc.html` · 390×844 · 원본 `components/navi/day-sheet.tsx moved (record-15)`

- [ ] **div** — “배경을 눌러 닫기 · 앱이 다시 시작되면 저장하지 않은 내용은 사라져요”
      `flex:1 min-height:0 display:flex align-items:flex-end justify-content:center padding:0 20px 12px text-align:center`
  - [ ] text 11.5px/500 — “배경을 눌러 닫기 · 앱이 다시 시작되면 저장하지 않은 내용은 사라져요”
        `font-size:11.5px font-weight:500 color:rgba(255,255,255,.62)`
- [ ] **BottomSheet** — “9월 3일 기록 수정”
      `background:#FFFFFF border:1px solid #E3E8F1 border-bottom:0 border-radius:26px 26px 0 0 display:flex flex-direction:column`

## ClassifySheetPicker — 카테고리 고르기 시트 · 줄에서 고르기 펼침

`canvas/ClassifySheetPicker.dc.html` · 390×844 · 원본 `components/navi/classify-sheet.tsx 줄 고르기 펼침 (spending-3 · a11y-1)`

- [ ] **div** — “배경을 눌러 닫기”
      `flex:1 min-height:0 display:flex align-items:flex-end justify-content:center padding:0 20px 12px text-align:center`
  - [ ] text 11.5px/500 — “배경을 눌러 닫기”
        `font-size:11.5px font-weight:500 color:rgba(255,255,255,.62)`
- [ ] **BottomSheet** — “카테고리 고르기 · 7건”
      `background:#FFFFFF border:1px solid #E3E8F1 border-bottom:0 border-radius:26px 26px 0 0 display:flex flex-direction:column`

## PayoffStates — 참고 · 미래 › 상환 계획의 경우들

`canvas/PayoffStates.dc.html` · 1230×1501 · 원본 `components/navi/payoff-plan.tsx 초안 · 다 갚지 못함 · 최소 상환만 · 모자람 (future-2/4/6/11/22/25 · D6 · D13 · D15)`

- [ ] text 11px/600 — “구현 참고 · 앱 화면이 아닙니다”
      `font-size:11px font-weight:600 letter-spacing:0.02em color:#475467 border:1px solid #E3E8F1 background:#FFFFFF border-radius:99px padding:4px 10px`
- [ ] text 20px/700 — “미래 › 상환 계획 — 초안 · 다 갚지 못함 · 최소 상환만 · 모자람”
      `font-size:20px font-weight:700 letter-spacing:-0.025em color:#101828`
- [ ] **p** — “저장된 계획(Payoff 장)에서 슬라이더나 방식을 바꾸면 초안이 됩니다. 숫자는 시안 사용자”
      `font-size:13px line-height:1.55 color:#626D88`
- [ ] **div** — “1”
      `display:flex gap:24px align-items:flex-start`
- [ ] **Card(18)** — “구현 메모”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:10px 18px 8px`

## FutureStates — 참고 · 미래 › 자산 경로의 경우들

`canvas/FutureStates.dc.html` · 1230×1749 · 원본 `components/navi/future-view.tsx 절감 가정 · 기록 없음 · 늘어나는 대출 · 초안 · 자세히 (future-1/2/5/11/12/19/21)`

- [ ] text 11px/600 — “구현 참고 · 앱 화면이 아닙니다”
      `font-size:11px font-weight:600 letter-spacing:0.02em color:#475467 border:1px solid #E3E8F1 background:#FFFFFF border-radius:99px padding:4px 10px`
- [ ] text 20px/700 — “미래 › 자산 경로 — 가정 · 기록 없음 · 늘어나는 대출 · 초안 · 자세히”
      `font-size:20px font-weight:700 letter-spacing:-0.025em color:#101828`
- [ ] **p** — “기본(Future 장)은 절감 가정 0원입니다. 숫자는 시안 사용자 9월 8일(보통 5.0% ”
      `font-size:13px line-height:1.55 color:#626D88`
- [ ] **div** — “1”
      `display:flex gap:24px align-items:flex-start`
- [ ] **Card(18)** — “구현 메모”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:10px 18px 8px`

## HomeGlanceRows — 참고 · 홈 자산 한눈에 줄 펼침

`canvas/HomeGlanceRows.dc.html` · 1230×1045 · 원본 `components/navi/home-glance.tsx 자산 한눈에 줄 펼침 (home-12)`

- [ ] text 11px/600 — “구현 참고 · 앱 화면이 아닙니다”
      `font-size:11px font-weight:600 letter-spacing:0.02em color:#475467 border:1px solid #E3E8F1 background:#FFFFFF border-radius:99px padding:4px 10px`
- [ ] text 20px/700 — “홈 · 자산 한눈에 — 줄을 펼쳤을 때”
      `font-size:20px font-weight:700 letter-spacing:-0.025em color:#101828`
- [ ] **p** — “홈 구성에서 「자산 한눈에」를 켠 사람의 카드입니다. 줄을 누르면 그 아래에 풀이가 열립니다.”
      `font-size:13px line-height:1.55 color:#626D88`
- [ ] **div** — “1”
      `display:flex gap:20px align-items:flex-start`
- [ ] **Card(18)** — “구현 메모”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:10px 18px 8px`

## SampleModeTabs — 참고 · 샘플 모드 띠 (모든 탭)

`canvas/SampleModeTabs.dc.html` · 1290×823 · 원본 `app/page.tsx 샘플 띠 (D8 · language-ia-21 · first-run-17)`

- [ ] text 11px/600 — “구현 참고 · 앱 화면이 아닙니다”
      `font-size:11px font-weight:600 letter-spacing:0.02em color:#475467 border:1px solid #E3E8F1 background:#FFFFFF border-radius:99px padding:4px 10px`
- [ ] text 20px/700 — “샘플 모드 — 모든 탭 맨 위 띠”
      `font-size:20px font-weight:700 letter-spacing:-0.025em color:#101828`
- [ ] text 13px/400 — “샘플로 둘러보는 동안 다섯 탭 모두 머리줄 위에 같은 띠가 있습니다.”
      `font-size:13px line-height:1.55 color:#626D88`
- [ ] **div** — “홈”
      `display:flex gap:20px flex-wrap:wrap`
- [ ] **Card(18)** — “구현 메모”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:10px 18px 8px`

## DebtUnpayable — 참고 · 월 최소 상환액을 비운 부채

`canvas/DebtUnpayable.dc.html` · 1230×936 · 원본 `components/navi/asset-view.tsx 부채 · 상환 계획 요약 (tasks-4 · D7 · D11 · D15)`

- [ ] text 11px/600 — “구현 참고 · 앱 화면이 아닙니다”
      `font-size:11px font-weight:600 letter-spacing:0.02em color:#475467 border:1px solid #E3E8F1 background:#FFFFFF border-radius:99px padding:4px 10px`
- [ ] text 20px/700 — “월 최소 상환액을 비워 둔 부채 — 다 갚지 못할 때”
      `font-size:20px font-weight:700 letter-spacing:-0.025em color:#101828`
- [ ] **p** — “예: 전세자금대출 1억 · 연 3.6%만 있고 월 최소 상환액을 비웠습니다(월 추가 20만원)”
      `font-size:13px line-height:1.55 color:#626D88`
- [ ] **div** — “1”
      `display:flex gap:24px align-items:flex-start`
- [ ] **Card(18)** — “구현 메모”
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:10px 18px 8px`

## TourHomeChecklist — 첫 실행 안내 · 홈 3 / 3 시작 순서 (처음 시작한 빈 홈)

`canvas/TourHomeChecklist.dc.html` · 390×844 · 원본 `components/navi/first-run-tour.tsx · lib/navi-tour.ts TOUR_HOME_CHECKLIST_STEP · components/navi/start-checklist.tsx (first-run-5 · AMEND 2)`

- [ ] **Header** — “NAVI”
      `margin-top:-348px display:flex flex-direction:column gap:6px padding:12px 16px 10px`
- [ ] **본문(스크롤 영역)** — “이번 달 소비”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
  - [ ] **HeroCard** — “이번 달 소비”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **Card(18)** — “이번 달 소비 기록”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 14px 13px`
  - [ ] **Card(18)** — “다음 안내”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px 16px 10px`
  - [ ] **Card(18)** — “이번 달 한도 오늘 포함 하루 —”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px`
  - [ ] **Card(18)** — “순자산”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:4px 14px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`
- [ ] **div** — “처음 안내”
      `position:absolute left:0 top:0 width:390px height:778px`

## TourHelpReplay — 첫 실행 안내 · 제목 옆 ?로 다시 연 안내 (화면 안내)

`canvas/TourHelpReplay.dc.html` · 390×844 · 원본 `components/navi/first-run-tour.tsx · lib/navi-tour-policy.ts tourBadge · showTourHelp (first-run-3 · AMEND 2 · D14)`

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
- [ ] **div** — “화면 안내”
      `position:absolute left:0 top:0 width:390px height:778px`

## TourRules — 참고 · 첫 실행 안내 규칙 (빈 화면 · 닫기 · 다시 보기 · 배치)

`canvas/TourRules.dc.html` · 1200×1760 · 원본 `lib/navi-tour.ts · lib/navi-tour-policy.ts isEmptyScreen · components/navi/first-run-tour.tsx · app/first-run-tour.css (AMEND 2 · first-run-3/4/21 · D7 · D8)`

- [ ] text 11px/600 — “구현 참고 · 앱 화면이 아닙니다”
      `font-size:11px font-weight:600 letter-spacing:0.02em color:#475467 border:1px solid #E3E8F1 background:#FFFFFF border-radius:99px padding:4px 10px white-space:nowrap`
- [ ] text 20px/700 — “첫 실행 안내 — 규칙”
      `font-size:20px font-weight:700 letter-spacing:-0.025em color:#101828`
- [ ] **p** — “앱 v5-stage1 a724aac 의 lib/navi-tour.ts · lib/navi-to”
      `font-size:13px line-height:1.55 color:#626D88`
- [ ] **div** — “처음 안내 · 홈 3 / 3”
      `display:flex gap:32px align-items:flex-start`

## HeroOverTarget — 참고 · 홈 맨 위 카드 · 소비 목표를 넘을 때

`canvas/HeroOverTarget.dc.html` · 1230×765 · 원본 `components/navi/home-hero.tsx 배지 · 오른쪽 줄 · 셋째 칸 (D1 · D4 · home-1 · home-8)`

- [ ] text 11px/600 — “구현 참고 · 앱 화면이 아닙니다”
      `font-size:11px font-weight:600 letter-spacing:0.02em color:#475467 border:1px solid #E3E8F1 background:#FFFFFF border-radius:99px padding:4px 10px`
- [ ] text 20px/700 — “홈 맨 위 카드 · 소비 목표를 넘을 때”
      `font-size:20px font-weight:700 letter-spacing:-0.025em color:#101828`
- [ ] **p** — “같은 시안 사용자(9월 8일 · 각주 두 줄)에서 소비 목표나 쓴 돈만 바꾼 세 경우입니다. ”
      `font-size:13px line-height:1.55 color:#626D88`
- [ ] **div** — “1”
      `display:grid grid-template-columns:repeat(3, 362px) gap:24px 28px align-items:start`
- [ ] **p** — “배지는 월말 예상으로만 판정합니다 — 월말 예상 ≤ 소비 목표면 「월말에도 목표 안」(초록 ·”
      `font-size:12px line-height:1.6 color:#626D88`

## TourHomeSample1 — 첫 실행 안내 · 홈 1 / 3 샘플로 둘러보기 (흐려진 샘플 띠 아래)

`canvas/TourHomeSample1.dc.html` · 390×844 · 원본 `components/navi/first-run-tour.tsx · lib/navi-tour.ts TOUR_STEPS · 샘플 띠 app/page.tsx (D8 · language-ia-21 · AMEND 2)`

- [ ] **SampleBanner** — “샘플 데이터로 둘러보는 중”
      `display:flex align-items:center justify-content:space-between gap:8px height:32px padding:0 14px background:#E9EDFD`
- [ ] **Header** — “NAVI”
      `display:flex flex-direction:column gap:6px padding:12px 16px 10px`
- [ ] **본문(스크롤 영역)** — “이번 달 소비”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px 14px`
  - [ ] **HeroCard** — “이번 달 소비”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **Card(18)** — “이번 달 소비 기록”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 14px 13px`
  - [ ] **TurnCard** — “다음 안내”
        `display:flex gap:12px background:#FFFFFF border:1px solid #E3E8F1 border-left:3px solid #DE8A2A border-radius:18px padding:13px 14px`
  - [ ] **Card(18)** — “이번 달 한도 오늘 포함 하루 45,220원”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px`
  - [ ] **Card(18)** — “순자산”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:4px 14px`
  - [ ] **Card(18)** — “상환 계획”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:4px 14px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`
- [ ] **div** — “처음 안내”
      `position:absolute left:0 top:0 width:390px height:778px`

## HomePrimaryGoal — 홈 · 대표 목적지 카드를 켰을 때

`canvas/HomePrimaryGoal.dc.html` · 390×1195 · 원본 `app/page.tsx 홈 카드 primaryGoal · lib/navi-home-layout.ts HOME_CARD_KEYS (goals-14 · first-run-14)`

- [ ] **Header** — “NAVI”
      `display:flex flex-direction:column gap:6px padding:12px 16px 10px`
- [ ] **본문(스크롤 영역)** — “이번 달 소비”
      `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px 14px`
  - [ ] **HeroCard** — “이번 달 소비”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **Card(18)** — “이번 달 소비 기록”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 14px 13px`
  - [ ] **Card(18)** — “68%”
        `display:flex align-items:center gap:12px background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px`
  - [ ] **Card(18)** — “이번 달 한도 오늘 포함 하루 45,220원”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px`
  - [ ] **Card(18)** — “순자산”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:4px 14px`
  - [ ] **Card(18)** — “상환 계획”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:4px 14px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`

## HomeTargetSaved — 홈 · 소비 목표를 저장한 직후 (알림 · 종 배지 3)

`canvas/HomeTargetSaved.dc.html` · 390×844 · 원본 `components/navi/home-hero.tsx 소비 목표 저장 · components/navi/save-notice.tsx (home-1 · D1 · D4 · D10)`

- [ ] **Header** — “NAVI”
      `display:flex flex-direction:column gap:6px padding:12px 16px 10px`
- [ ] **본문(스크롤 영역)** — “이번 달 소비”
      `flex:1 min-height:0 display:flex flex-direction:column gap:9px padding:0 14px position:relative`
  - [ ] **HeroCard** — “이번 달 소비”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - [ ] **Card(18)** — “이번 달 소비 기록”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 14px 13px`
  - [ ] **TurnCard** — “다음 안내”
        `display:flex gap:12px background:#FFFFFF border:1px solid #E3E8F1 border-left:3px solid #DE8A2A border-radius:18px padding:13px 14px`
  - [ ] **Card(18)** — “이번 달 한도 오늘 포함 하루 29,570원”
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px`
- [ ] **BottomNav** — “홈”
      `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`
- [ ] **div** — “소비 목표 50%로 저장했어요 · 한도 180만원”
      `position:absolute left:14px right:14px bottom:78px background:#101828 border-radius:16px padding:13px 14px 12px color:#FFFFFF box-shadow:0 8px 24px rgba(0,0,0,.28)`

## AssetsStale — 자산 · 잔액 확인이 필요한 자산이 있을 때

`canvas/AssetsStale.dc.html` · 390×1033 · 원본 `components/navi/asset-view.tsx 잔액 확인 띠 · lib/navi-asset-freshness.ts (assets-15)`

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

## GoalDialogPreview — 모달 · 목적지 추가 (일반 저축 · 저장 전 미리 보기)

`canvas/GoalDialogPreview.dc.html` · 390×981 · 원본 `components/navi/goal-dialog.tsx 저축 유형 · 저장 전 미리 보기 (goals-15 · goals-3 · D1)`

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
    - [ ] **div** — “이름 *”
          `flex:0 0 auto`
    - [ ] **div** — “표시 아이콘”
          `display:flex align-items:center gap:3px height:23px margin-top:-9px font-size:11.5px color:#626D88`
    - [ ] **div** — “목표액 *”
          `display:flex gap:10px align-items:flex-start margin-top:0px`
    - [ ] **div** — “우선순위”
          `display:flex gap:10px align-items:flex-start margin-top:0px`
    - [ ] **Callout(info)** — “이대로면 매달 25만원씩 모아야 해요 · 2027년 9월에 도착”
          `padding:10px 12px background:#F4F6FB border-radius:12px display:flex flex-direction:column gap:6px font-size:13px line-height:19.5px color:#475467`
    - [ ] **Callout(info)** — “수익 없이 넣은 돈만 계산해요”
          `display:flex gap:8px padding:10px 11px background:#F4F6FB border-radius:12px`
  - [ ] **div** — “취소”
        `display:flex gap:10px padding:12px 18px 20px border-top:1px solid #EFF2F8`

## AlertsPanelInfo — 모달 · 알림 (중요 1 · 참고 1)

`canvas/AlertsPanelInfo.dc.html` · 390×844 · 원본 `lib/navi-alert-rows.ts 참고 줄 · components/navi/coach-panel.tsx 알림 (home-10 · assets-15)`

- [ ] **div** — “배경을 눌러 닫기”
      `height:40px display:flex align-items:flex-end justify-content:center`
- [ ] **BottomSheet** — “알림 2건”
      `flex:1 min-height:0 background:#FFFFFF border-radius:26px 26px 0 0 display:flex flex-direction:column color:#101828`
  - [ ] **div**
        `display:flex justify-content:center padding:9px 0 0`
  - [ ] **div** — “알림 2건”
        `display:flex align-items:flex-start justify-content:space-between gap:10px padding:12px 18px 14px border-bottom:1px solid #EFF2F8`
  - [ ] **div** — “중요 1”
        `flex:1 min-height:0 padding:14px 18px 0 display:flex flex-direction:column gap:15px`
    - [ ] **div** — “중요 1”
          `display:flex flex-direction:column`
    - [ ] **Callout(info)** — “자산의 잔액 확인일이 없거나 35일 넘게 갱신하지 않으면 여기에 알려 드려요.”
          `display:flex gap:8px padding:10px 11px background:#F4F6FB border-radius:12px`
  - [ ] **div** — “닫기”
        `display:flex gap:10px padding:12px 18px 20px border-top:1px solid #EFF2F8`

