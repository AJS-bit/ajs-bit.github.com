# 소스 적용 계획

**이번 작업에서 NAVI 원본 소스는 수정하지 않았습니다.** 코드 산출물은 `design/canvas/`의 시안(`.dc.html`)뿐입니다. 아래는 이 디자인을 `wealth-navigator`에 적용할 때의 파일별 계획입니다.

> 인계된 `NAVI-2.2-source.zip`을 읽고 작성했습니다. 경로는 원본 체크아웃 기준입니다.

---

## 1. 적용 순서 — 4단계

계산·저장 로직을 건드리지 않고 아래 순서로 나누면 각 단계가 독립적으로 되돌릴 수 있습니다.

### 1단계 · 토큰 교체 (계산 영향 없음)

| 파일 | 작업 |
|---|---|
| `app/globals.css` | `:root` / `.dark` 변수 블록을 [`tokens.v3.json`](tokens.v3.json)의 `color.light` / `color.dark`로 교체. `--type-*` 변수를 9단계로 재정의 |
| `app/layout.tsx` | 서체 로딩 추가 — IBM Plex Sans KR 또는 Pretendard **자체 호스팅 `@font-face`**. 현재는 이름만 지정돼 OS마다 다르게 렌더됩니다 |
| `lib/engine/constants.ts` | **변경 없음** — 카테고리 15색·자산 5색은 그대로 |

이 단계만으로 색과 폰트가 v3가 되고, 레이아웃은 2.2 그대로 유지됩니다.

### 2단계 · 공통 컴포넌트

| 파일 | 작업 |
|---|---|
| `components/navi/shared.tsx` | `MetricTile`(가운데 정렬 타일)을 **`DataRow`**(이름 왼쪽 / 값 오른쪽 tabular / 보조 / 액션)로 대체하고, `MetricTile`은 히어로 내부 3연속 지표 전용으로 축소. `ViewHeader`에 `tabs`·`trailing` 슬롯 추가. **`HeroCard`**, **`AssumptionCard`**(보라 점선 + 가정 배지), **`RouteBar`**(항로 바) 신규 |
| `components/navi/number-input.tsx` | 단위 표기를 칸 오른쪽 안쪽 고정으로. 빈 값(자동)과 `0`(0원 지정)의 표시 분기 유지 |
| `components/ui/button.tsx` | **variant만 추가** — `outline-accent`, `soft`, `dashed-add`. Base UI 프리미티브 자체는 수정하지 않음 |

`RouteBar`가 이 디자인의 핵심 재사용 요소입니다. 홈·소비·한도·목적지가 모두 이걸 씁니다.

```
<RouteBar value={57.9} target={60} max={100} tone="positive" />
```

### 3단계 · 화면별 레이아웃

| 파일 | 작업 | 대응 아트보드 |
|---|---|---|
| `app/page.tsx` | 홈 히어로 재구성(숫자 왼쪽 + 증감 오른쪽 + RouteBar + 3지표 + 근거줄/기준 조정 + 단일 CTA). 캡션 줄 오른쪽에 **순자산 대비 보조 지표**(`예상 소비 ÷ 순자산`, 13px) — 순자산 0이거나 자산 미입력이면 이 조각만 숨기고 주 지표는 그대로. 다음 안내 턴 카드. 보조 지표 3개 → `더 깊이 보기` 아코디언 3행. 데스크톱 1.6fr/1fr 그리드 | `Main`, `HomeScroll`, `DesktopHome`, `EmptyStates` |
| `components/navi/asset-view.tsx` | 요약 타일 5개 → 히어로(순자산 + 스파크라인 + 구성 막대) + 칩 2개 + 계좌 `DataRow` 목록. `+ 추가`를 섹션 헤더로. 부채 탭은 총부채 히어로 + 고금리 경고 + 부채 행 목록, 상환 전략 탭은 방식 카드 2장 + 추가 상환 입력 + 상환 순서 | `Assets`, `Debts`, `Strategy`, `AssetDialog`, `DebtDialog` |
| `components/navi/spending-view.tsx` | 이번 달 탭: 타일 4개 → 히어로 1개(소비율 + 계획 대비 그래프). 내역 탭: 검색줄 + 반복 거래 버튼 + 날짜 그룹 목록. 한도 탭: **총한도 조정 / 배분 편집 버튼 분리**. 과거 달은 탭 2개 + 예상 말투 제거 + 점선 예상선 제거 | `Spending`, `Limits`, `SpendingPast`, `DesktopLedger` |
| `components/navi/goals-view.tsx` | 요약 타일 4개 → 월 저축 배분 카드 1개. `목표 추가`를 목록 끝 점선 버튼으로 이동. 행 안쪽 `+ 적립`(순자산·부채 목표는 미표시). 유형별로 **쓰지 않는 입력 칸을 렌더하지 않음**. 적립 모달에 저장 전 변화 3줄(적립액·진행률·도착 예상) | `Goals`, `GoalDialog`, `GoalTypes`, `GoalContribute` |
| `components/navi/future-view.tsx` | 기간·투자 환경 칩을 그래프 위로. 타일 4개 → 그래프 히어로 + `다음 자산 지점` 카드. 상환 계획 탭은 `AssumptionCard`(보라 점선) + 전략 비교 2장 + 명시 저장 카드 | `Future`, `Payoff` |
| `components/navi/peer-card.tsx` | 가운데 %p 숫자 → 위아래 두 막대 비교. 5가지 상태 분기. 출처 블록 상시 표시 | `PeerStates` |
| `components/navi/spending-analysis.tsx` | `CategoryLimitEditor`: 바텀시트 구조 + 총한도 세그먼트 + 카테고리 입력 + **고정 합계 바(배분 합계 / 총한도)**. `MonthlyClosePanel`: 재마감 경고 + 원 단위 입력 + 자동 계산값 + 고정 확인 줄 | `LimitEditor`, `MonthlyClose` |
| `components/navi/journey-card.tsx` | 링 + 왼쪽 정렬 텍스트 + 오른쪽 chevron 한 줄 | `Main` |
| `components/navi/transaction-link-fields.tsx` · 거래 모달 | 거래 종류 세그먼트 → 날짜/금액 → 카테고리 칩 → 메모 → 잔액 반영 토글 순서. 소비율 제외 안내 고정 | `TransactionAdd` |
| `components/navi/coach-panel.tsx` (기록 없음: `CoachEmpty`) | 조언 3개에 우선순위 번호 + `guidance` 스타일(왼쪽 3px 상태색). 절감 가정은 보라 점선 블록. 알림 패널은 아이콘+CTA 행 목록과 “조치 없음” 상태 | `CoachPanel`, `AlertsPanel` |
| `components/navi/goal-tools.tsx` | 추천 목적지 카드 3장 + 계산 폼 + 보라 “저장되지 않는 계산” 결과 + 원금/원금+수익 두 곡선 | `GoalDesign` |
| `components/navi/import-review.tsx` | 적용 방식 세그먼트 + 신규/중복/충돌/검토 건수 행 + 현재→적용 후 비교 + 고정 확인 줄 | `ImportReview` |
| `app/page.tsx` (첫 실행·저장소) | 온보딩 화면, 로딩·불러오기 실패·복구 파일 오류·샘플→내 데이터 전환 | `Onboarding`, `StorageStates` |
| `components/ui/alert-dialog.tsx` 사용처 | 삭제·초기화 확인 5종. 대상 이름과 **무엇이 함께 사라지는지**를 본문에 명시 | `Confirmations` |
| 모달 공통(폼 검증·저장 경로) | 오류 6종: 필수 값 미입력 시 저장 비활성, 규칙 위반 시 해결 선택지 2개, 저장 중 입력 잠금, 실패 시 입력값 보존, 완료 시 변경 요약 + 되돌리기, 저장 없이 닫기 확인 | `ModalErrors` |

### 4단계 · 그래프 (Recharts)

`components/navi/spending-analysis.tsx`, `future-view.tsx`, `goal-tools.tsx`

| 적용 | Recharts 설정 |
|---|---|
| Y축 눈금 제거 | `<YAxis hide />` + 필요한 지점에 `<ReferenceLine>` + `label` |
| 가로 폭 전체 | `<ResponsiveContainer>` margin `{top:12,right:12,bottom:0,left:12}` (기본 left 여백 제거) |
| 도메인 헤드룸 | `domain={[0, (max) => max * 1.1]}` |
| 예상선 | 같은 `<Line>`을 두 개로 — 실측 구간(`strokeDasharray` 없음)과 예측 구간(`strokeDasharray="5 4"`, 옅은 색). 데이터에 `actual` / `projected` 두 키를 두고 오늘 지점에서 둘 다 값을 갖게 함 |
| 끝점 라벨 | `<LabelList dataKey position="top">` 또는 마지막 점에만 커스텀 `<Label>` |
| X축 눈금 | `ticks={[1, today, 15, 22, lastDay]}` 최대 5개 |
| 높이 | 부모 CSS 높이와 `ResponsiveContainer minHeight`를 **같은 값**으로 통일 (현재 모바일 280 vs 300 충돌) |
| 범위 밴드 | `<Area dataKey="range" fill="violet" fillOpacity={0.13} stroke="none" />` |

**월말 예상 소비는 이미 앱이 계산합니다**(`lib/navi-current.ts`). 새 계산이 아니라 기존 값을 그래프에 옮기는 것뿐입니다.

---

## 2. 절대 바꾸지 않을 것

디자인 때문에 건드리면 안 되는 파일과 규칙입니다.

- `lib/engine/**` — 계산 엔진
- `lib/navi-salary.ts` · `navi-current.ts` · `navi-monthly.ts` · `navi-goals.ts` · `navi-readiness.ts` · `navi-spending-scenario.ts` — 계산식
- `lib/navi-storage.ts` · `navi-persistence.ts` · `navi-import.ts` — 저장·백업 형식, 거래 ID
- `lib/navi-recurring.ts` · `navi-ledger.ts` — 반복 거래, 계좌 연결
- `components/ui/**` — Base UI 프리미티브 (variant 추가만, 구조 수정 금지)
- 자동 한도 계산식 `min(실수령 × 소비 목표, 총수입 − 저축 − 상환)`
- 실수령 급여와 총수입의 구분, 저축 이체·대출상환의 소비율 제외
- 기본 소비 목표 60%가 "수정 가능한 계획 시작값"이라는 성격, 목표 0%도 임의로 바꾸지 않음
- 과거 급여는 그 달 마감에 저장된 값만 사용
- 저장 방식의 차이 — 상환 방식 **즉시 반영** / 금액 일부 **포커스 해제 시 반영** / 미래 상환 계획 **명시 저장** / 홈 시나리오 **가정** / 가져오기 **미리보기 확인 후 적용**

새 요구사항으로 만들지 않는 것: 로그인, 클라우드 계정, 외부 서버, 실시간 API, 네트워크에서 내려받아야만 쓸 수 있는 필수 자산. **유일한 외부 의존은 웹폰트이며 자체 호스팅으로 오프라인 동작이 가능합니다.**

---

## 3. 확인한 동작 / 검증하지 않은 것

### 확인한 것 (이 세션에서 실제로 측정·렌더)

| 항목 | 방법 | 결과 |
|---|---|---|
| 75개 아트보드 렌더 | Chromium 헤드리스로 각 프레임 크기에서 실제 렌더 | 전부 렌더됨 |
| 전체 잘림 | 프레임 높이 대비 콘텐츠 높이를 DOM에서 측정 | **75개 모두 오버플로 0**. 상태 카탈로그 3종은 이 측정에서 잘림이 드러나 프레임 높이를 늘렸습니다(저장소 1180→1264, 또래 1360→1552, 미입력 1400→1718) |
| 하단 여백 | 마지막 카드 하단 ~ 콘텐츠 영역 하단 간격 | 모달 0 · 미래 5 · 자산 7 · 한도 15 · 내역 20 · 상환 계획 21 · 소비 35 · 부채 62 · 목적지 71 |
| 그래프 라벨 충돌 | 렌더 결과 육안 확인 후 좌표 재배치 | 소비·데스크톱 홈의 `한도`/`월말 예상` 겹침, 목적지 설계 곡선의 끝 구간 급변, 상환 계획 비교 카드의 배지 줄바꿈 해소 |
| 다크 변환 | 라이트 26종을 토큰 매핑으로 변환 후 렌더 | 브랜드 그라디언트·마크 화살표·카테고리 팔레트가 라이트와 동일하게 유지됨을 확인 |
| 샘플 수치 정합성 | 손계산 | 360만 × 60% = 216만 한도 / 216 − 208 = 8만 여유 / 112 + 104 = 216 / 자산 5건 = 1억 8,210만 / 부채 3건 = 8,860만 (6,200+2,480+180) / 월 최소 상환 55만 (32+21+2) / 18,210 − 8,860 = 9,350만 / 가중 평균 금리 4.58% |
| 캔버스 파일 무결성 | `seed-canvas.mjs --check` | ok, 76 files (75 아트보드 + canvas.json) · 5페이지, 배치 안 된 파일 0 |
| 완제일·도착일·총이자 | `_tools/calc/`의 월 단위 상각·복리 시뮬레이션 | 화면 수치가 계산 결과와 일치 |

### 검증하지 않은 것

- **실제 Android 기기 렌더**와 safe-area(`--navi-top/bottom`) 반영. 시안은 브라우저 렌더입니다.
- **터치 표적 크기.** 실제 기기에서 30~42px 보조 버튼의 히트 영역을 확인해 주세요. 시안은 시각 크기만 정의하고 히트 영역 확장은 구현에 맡깁니다.
- **실제 데이터 볼륨** — 거래 수백 건의 목록 성능, 긴 계좌명, 억 단위 금액의 줄바꿈. 시안은 짧은 가상 이름만 씁니다.
- **Recharts 이식 세부** — 축 숨김 + `ReferenceLine` 라벨 + 실측/예측 이중 라인의 실제 동작. 시안은 손으로 그린 SVG입니다.
- 토큰 시트는 라이트/다크 값을 한 장에 함께 적은 명세라 다크 사본을 두지 않습니다.
- **화면 안의 세부 분기** — 자산·부채·목적지 모달의 오류 상태(모두 정상 입력 상태로 그림), 목적지 적립 모달, 목적지 유형 5종 중 부채 상환만 그림, 소비 과거 월 보기, 코칭의 “기록 없음” 상태.

### 기능상 차이가 생기는 부분

디자인만으로 끝나지 않고 **동작 결정이 필요한 것**들입니다.

1. **홈 한도 카드에서 총한도·하루 예산 표시를 줄였습니다.** 세로 공간 때문에 `이번 달 한도 / 하루 47,270원 / 남은 104만원 / 진행바`만 남겼습니다. 총한도 금액은 소비 › 한도 화면에 있습니다. 홈에서 총한도를 꼭 봐야 한다면 알려주세요.
2. **소비 › 이번 달의 `총수입 대비 예상 소비`와 `소비·상환 후 남는 비율`을 홈의 `더 깊이 보기`와 내역 요약으로 옮겼습니다.** 이번 달 탭 첫 화면에서는 보이지 않습니다.
3. **소비율 기준 스위치(현재 38px)를 44px 기준으로 올렸습니다.** 2.2 계약에서 "주요 조작으로 다룰지 디자인 결정 필요"로 남아 있던 항목입니다. v3는 주요 조작으로 봅니다.
4. **화면 이름을 `목표` → `목적지`로 바꿨습니다.** 하단 탭 라벨은 `목표`를 유지했습니다(4글자 이내). 둘 중 하나로 통일할지는 결정이 필요합니다.
5. **월별 실제 소비 막대 차트를 없앴습니다.** 자산 화면의 순자산 스파크라인과 소비의 누적선으로 역할을 나눴습니다. 월별 비교가 꼭 필요하면 내역 탭에 되살릴 수 있습니다.
6. **부채 화면의 `이번 달 상환 예정`은 새로 만든 요약입니다.** 2.2에는 없던 카드로, 최소 상환 + 추가 상환 합계와 결제일을 보여줍니다. 계산은 기존 값의 합이라 새 로직이 필요 없지만 표시 항목은 추가입니다.
7. **상환 전략 화면에 “선택 즉시 저장됨” 배지를 넣었습니다.** 방식 선택은 즉시 반영, 추가 상환액은 포커스 해제 시 반영이라는 2.2의 서로 다른 저장 방식을 화면에서 구분해 알립니다.
8. **서체를 바꾸면 모든 화면의 줄바꿈이 달라집니다.** Pretendard를 유지하기로 하면 시안의 크기·굵기 램프는 그대로 쓸 수 있지만, 카드 안 문구의 줄 수는 다시 확인해야 합니다.

---

## 4. 시안 파일을 다시 만들려면

```bash
cd design/canvas
node <design-skill>/seed-canvas.mjs \
  --template <design-skill>/payload.template.html \
  --out navi-redesign.html --title "NAVI 자산 성장 내비게이션" \
  --artboard Main.dc.html --artboard HomeScroll.dc.html ... \
  --canvas canvas.json
```

`.dc.html`은 정적 HTML + 인라인 스타일입니다. 브라우저에서 바로 열어도 되고, `navi-redesign.html` 하나만 열면 75개 아트보드를 한 캔버스에서 볼 수 있습니다.
