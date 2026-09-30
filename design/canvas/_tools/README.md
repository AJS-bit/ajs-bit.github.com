# 아트보드 생성 도구

아트보드 파일 327장(라이트 164 · 다크 163 · 캔버스에는 317장 — 2026-09-27 fix-up 3) 가운데 손으로 쓴 라이트 16종(아래 목록)을 뺀 전부와 다크 전부를 일관된 조각으로 찍어내는 스크립트입니다. **최종 산출물은 상위 폴더의 `.dc.html` 파일**이고, 이 도구는 그것을 처음 만들 때와 다크 버전을 다시 뽑을 때 씁니다.

| 파일 | 역할 |
|---|---|
| `gen_common.py` | 색·아이콘·카드·버튼·입력·시트 등 공통 조각 |
| `gen_calendar.py` | **홈 달력 공용 조각** — 자료(2026년 9월 · 8월 · 달이 바뀐 첫 주 견본의 10월) · 칸 · 접힘 카드(최근 7일 스트립) · 펼침 월 달력(**홈의 기본 — `HOME_EXPANDED` · 2026-09-30**) · 상태 줄 · 적기 버튼 `+ 오늘 쓴 돈 적기` / 알약 `+ 더 적기`(줄 높이 40) · 오늘 칸 테두리와 `+`(2026-09-24 · 최종 점검 후속에서 스트립 수식어 줄 9 · 이체 · ✓와 함께인 `+` 16) · 오늘 0건(`today_empty`) · 처음 쓰는 날(`since`)은 펼침에도 · 그 달 기록 0건의 합계 줄 `9월 기록이 아직 없어요` · 홈 구성 행의 축소 미리보기(`calendar_card` · `calendar_thumb`). `gen_v4.py`(`gen_v4_stocks.py`는 그 `calendar_block`을 받아 씀) · `gen_v5.py` · `gen_v5_sheets.py`가 함께 쓰고, `gen_screens.py`는 `LedgerV5`의 날짜별 합계를 여기 자료와 맞춘다. `gen_common`만 import하고 파일을 쓰지 않는다. **홈에 달력이 나오는 장은 전부 여기서 가져온다 — 달력을 고칠 때는 이 파일 하나만 고친다.** 홈 장은 `calendar_card(HOME_EXPANDED)`(펼친 월 달력)이고, 접은 7일 줄(`False`)은 「접기 ▴」 뒤를 보여 주는 상태 장(`HomeCalendarStrip` · `CalendarCells` ⑨ · `CalendarGridSizes` · `CalendarStatusLines` · `Components` 08)에만 쓴다. 펼친 달력에서 날짜 · ‹ 를 누른 3초 안내는 `tap_note`(안내 줄 자리) · 이체만 있는 날은 합계 글자 `''` |
| `gen_screens.py` | 화면 — 시작 방법 고르기(`Onboarding`) · 저장소 상태 · 부채 · 자산 › 상환 계획(읽기 전용 요약 `Strategy`) · 내역 · 새 목적지 설계 · 미래 › 상환 계획(저장된 계획 `Payoff`) + 내역 `LedgerV5`(카테고리 없음 칩 · 날짜별 합계) + 목적지 · 새 목적지 설계 상태 장(`GoalsStates` · `GoalDesignStates`). v3 기준 그림 `Ledger`는 원본 전용 |
| `gen_modals.py` | 장 23개 — 모달 18종(내 수치(접힌 칸을 연 모습) · 항목 없는 내 수치 `ProfileDialogNoItems` · 월급 입력 `SalarySheet` · 순자산 대비 소비 `NetWorthRatioSheet` · 자산 추가 · 자산 수정 `AssetEditDialog` · 잔액 한 번에 확인 `AssetBalanceCheck` · 부채 · 목적지 · 목적지 저축 미리 보기 `GoalDialogPreview` · 반복 기록 · 반복 기록 겹침 `RecurringDialogOverlap` · 백업 불러오기 · 코칭 · 알림 · 알림 참고 줄 `AlertsPanelInfo` · 알림 없음 `AlertsEmpty` · 또래) · 확인 대화상자 시트 `Confirmations` · 월 마감 `MonthlyCloseV5`(+ 원본 전용 `MonthlyClose`) · 구현 참고 장 `AssetDebtTypes` · `TransactionAddFromDaySheet`(960 × 908 · 손으로 쓴 `TransactionAdd.dc.html`을 읽어 값만 바꾼다 — 그 파일은 고치지 않는다) |
| `gen_errors.py` | 모달 오류·저장 상태 7종 시트 `ModalErrors` (`python3 gen_errors.py <높이>` · 기본 2100 · 쓴 뒤 자연 높이를 알려 준다) |
| `gen_rest.py` | 장 6개 — 적립 모달 · 목적지 유형 5종 시트 · 소비 지난 달 셋(마감함 `SpendingPast` · 마감 전 `SpendingPastOpen` · 마감 뒤 기록이 바뀜 `SpendingPastChanged`) · 코칭 기록 없음 (`python3 gen_rest.py <유형 시트 높이>` · 기본 1920). 옛 `AlertsReview`는 2026-09-22에 거뒀다. `gen_modals`의 조각을 import하므로 모달 장도 같이 다시 쓴다(멱등) |
| `gen_v4.py` | **v4 · 1단계** 아트보드 8종과 다크 짝 — 소개 3장 · 홈 구성(첫 실행 · 버튼 「다음」) `HomeSetup` · 주식 알림을 켠 변형 `HomeSetupStocksOn` · 설정 시트(D5)의 `홈 구성` 행 `SettingsHomeEntry` · 설정에서 들어온 홈 구성 `HomeLayoutEdit` · 구성 반영 홈 `HomeConfigured`. 홈은 `Main.dc.html`을 잘라 쓰고, `Main`에는 달력이 없으므로 `이번 달 달력` 카드와 홈 구성 첫 행의 미리보기는 `gen_calendar`에서 가져온다 |
| `gen_v4_stocks.py` | **v4 · 2~5단계** 아트보드 16종(내비 4 · 주식 뼈대 4 · 카테고리 탐색 6 · 설정 2)과 다크 짝, 스냅숏 표본 JSON. 목적지 탭 본문은 `Goals`·`Future`·`Payoff`를 잘라 쓴다(셋째 세그먼트 `DestPayoff`). 홈 두 장(`HomeStocksOff` · `HomeStocksCard`)은 `gen_v4`의 달력 든 홈을 받아 쓴다. `import gen_v4`라 1단계 8종도 같이 다시 쓴다(멱등) |
| `gen_v5.py` | **v5 · 1 · 2단계** 아트보드 27종과 다크 짝 — 홈 10종(접은 모습 스트립 `HomeCalendarStrip` · 기본 카드 4개 전체 스크롤(펼친 달력 · 2026-09-30) `HomeDefaultScroll` 390 × 1555 · 펼침 월 달력 390/360 · 지난달 보기 · 소비 목표 조정 열림 `HomeTargetEditor` · 달이 바뀐 첫 주 `HomeMonthStart` · 샘플 모드 `HomeSampleMode` · 대표 목적지 카드를 켠 홈 `HomePrimaryGoal` 390 × 1509 · 소비 목표를 저장한 직후 `HomeTargetSaved` 390 × 1510 — 2026-09-27 fix-up 3) + 하루 시트 쪽 12종(시트 기본 · 키보드를 내린 모습 `DaySheetScrolled` · 목록 우선 · 수정 · 날짜 옮기기 `DaySheetEditMoved` · 지운 뒤 `DaySheetDeleted` · 기록 없는 어제 `DaySheetPastEmpty` · 360 × 640 · 완료 카드 · 카테고리 고르기 · 줄에서 고르기 `ClassifySheetPicker` · 이력 부족 히어로 `HeroInsufficient` 390 × 1499) + 구현 참고 장 5종 = 저장을 한 번 더 물어보는 경우 1200 × 1219 · 홈 맨 위 카드의 안내 줄 1200 × 800 · 홈 맨 위 카드 · 소비 목표를 넘을 때 `HeroOverTarget` 1230 × 765(2026-09-27 fix-up 2) · 달력 칸 읽는 법 1330 × 880 · 폭과 글자 크기 1150 × 1745(2026-09-27 fix-up 3) — 앱 화면이 아니라 설명 장이라 `spec_frame`으로 가로로 넓게 그린다. 펼침은 어느 폭에서도 7열 월 달력(계획 7판). 홈은 `Main.dc.html`을 잘라 쓰고 달력은 `gen_calendar`. **`gen_v4` · `gen_v4_stocks`를 import하므로 돌리면 v4 24종도 같이 다시 쓴다(멱등)** |
| `gen_v5_sheets.py` | **v5 · 하루 시트 · 완료 카드 · 상태 줄의 나머지 상태** 6종과 다크 짝 — 앱 화면 2종(소비 0건인 날 `DaySheetNoSpend` · 확인할 내용 목록 시트 `ReviewListSheet`) + 구현 참고 장 4종(`DaySheetNoSpendStates` 1200 × 1252 · `DoneCardStates` 1200 × 1534 · `DaySheetStates` 1210 × 1919 · `CalendarStatusLines` 1200 × 2673 — 2026-09-27 fix-up 5). `gen_v5`의 조각과 `w()`를 쓴다 — `import gen_v5`라 v4 · v5 장을 전부 다시 쓴다(멱등) |
| `gen_v5_screens.py` | **v5 · 달력 밖의 화면들** 11종과 다크 짝 — 구현 참고 장 10종(`InsufficientElsewhere` 1230 × 1864 · `FutureProvisional` 1230 × 1256 · `EtcSubline` 1200 × 1715 · `LimitCardCases` 1200 × 1462 · `ImportBackupNotes` 1230 × 1103 · 2026-09-26 새 장 `PayoffStates` 1230 × 1501 · `FutureStates` 1230 × 1749 · `HomeGlanceRows` 1230 × 1045 · `SampleModeTabs` 1290 × 823 · `DebtUnpayable` 1230 × 936) + 앱 화면 2종(`RecurringPrefill` · 2026-09-27 fix-up 3 `AssetsStale` — `Assets.dc.html`을 잘라 잔액 확인 띠 · 칩을 넣음). 높이는 파일의 `NEW` 표. 손으로 쓴 `Spending` · `Limits` · `PeerStates` · `Future` · `Goals`는 `.dc.html`에서 잘라 쓰고, 모달 조각은 `gen_modals` · `gen_rest`를 import하지 않고 같은 모양으로 옮겨 적었다(import하면 그쪽 장을 다시 쓰므로). 계획에 원문이 없어 지은 문구 · 모양에는 `# 제안` 주석 |
| `gen_canvas.py` | `canvas.json`(페이지 11개 · 좌표 · 주석 · 제목 · 크기 `TALL`/`WIDE`) 생성 |
| `gen_tour.py` | **첫 실행 안내** 37장과 다크 짝 — 11화면 × 3단계(탭 장 위에 막 + 강조 + 카드) · 빈 홈의 3단계 `TourHomeChecklist` · 제목 옆 `?`로 다시 연 안내 `TourHelpReplay` · 규칙 참고 장 `TourRules` · 샘플로 둘러보기로 시작한 홈 1단계 `TourHomeSample1`(흐려진 샘플 띠 아래 · 2026-09-27 fix-up 2). 문구 · 버튼 · 배치 규칙은 앱 `lib/navi-tour.ts` · `first-run-tour.tsx` 그대로이고, 좌표 표 `PLACE`(스크롤 · 대상 자리 · 카드 위 / 아래 / compact)는 실제 웹폰트로 바탕 장을 펼쳐 재고 앱 `placeTourCard`를 흉내 내 얻은 값이다. **바탕 장(탭 장)을 고쳐 카드 자리가 바뀌면 다시 잰다.** 스크롤 끝 = 마지막 내용 아래가 y 716(세그먼트 화면) · y 740(홈) 막은 탭 막대 위(778)까지 · 다크 카드 `#1E2739` / 선 `#39455F` / 막 `rgba(4,7,14,.74)`는 darken 뒤에 이 파일이 채운다. `refresh_components_v5` 뒤 · `gen_notify` 앞. 2026-09-30 홈의 달력이 펼친 월 달력이 되어 홈 · 시작 순서 · 샘플 홈의 표를 다시 쟀다(같은 흉내가 예전 표 9줄을 그대로 다시 만드는 것을 먼저 확인). |
| `gen_notify.py` | 기기 알림 2장(`SettingsNotify` · `NotifyCases`)과 다크 짝. `gen_v5`를 import 하므로 v4 · v5 장도 다시 써진다(멱등) |
| `nobreak.py` | 낱말 중간 꺾임 막기(D14 · a11y-11) — 낫표 · 괄호(앞 낱말부터 닫는 괄호 + 조사까지 통째로 · 띄어쓰기가 든 묶음은 22자까지 · 어느 묶음도 괄호 안에서 끝나거나 시작하지 않음 — 2026-09-27 fix-up 6) · 붙임표 · 숫자 % + 조사(`50%로`) 자리만 `white-space:nowrap`으로 묶는다(글자는 그대로 · 멱등 · 2026-09-27 fix-up 5). `gen_v5.w`(2026-09-26 새로 고친 장) · `gen_notify` · `refresh_components_v5` · `gen_tour`(`TourRules`)가 쓴다 |
| `nocode.py` | 그린 글에서 결정 · 점검 번호(`(D7)` · `(home-8)` · `AMEND 2` · `NUMBERS §4` …)를 찾는다 — `sync_screens.py`가 라이트 장의 글에 번호가 있으면 1로 끝난다(2026-09-27 fix-up 3 · 번호는 CHANGES · SPEC 문서에만) |
| `brand_mark.py` | 앱마크 규격(2026-09-30 「하루가 쌓인 길」 · 네모와 같은 크기 svg · 그림은 **어디서나 네모의 54%** — 같은 날 둘째 결정 · 앱 안 마크 · 런처 · 웹 아이콘과 같은 비율 · viewBox `8.63 8.63 90.74 90.74`) · `fix()`가 옛 종이비행기와 처음 규격(45.4% · viewBox `0 0 108 108` / `18 18 72 72`)이 남은 손편집 장을 고친다(`Main` 은 홈 장 머리줄의 원본이라 먼저 고친다) · 로고 파일 묶음은 `design/brand/gen_brand.py` |
| `refresh_components_v5.py` | `Components.dc.html`의 **08 · v5 절만** 지금의 v5 장(`HomeCalendarStrip` · `HomeCalendar` · `DaySheet` · `DoneCard` · `ClassifySheet` · `HeroInsufficient` · `HeroFootnotes`)에서 다시 잘라 와 채운다. 01~07절과 루트 크기는 건드리지 않는다. `gen_v5.py` 뒤 · `darken.py` 앞 |
| `sync_screens.py` | `gen_canvas.py` **뒤에** 돌린다. `canvas.json`의 제목 · 페이지 · 크기를 `design/screens.json`에 맞추고, `.dc.html` 루트 크기와 등록부가 어긋난 장 · 출처(`SOURCE`)가 없는 새 장을 알려 준다(있으면 종료 코드 1). 새 장을 더하면 이 파일의 `SOURCE`에 출처(앱 파일 또는 계획 절)를 적는다 |
| `seed_doc.py` | 캔버스 페이지 `navi-redesign.html` 안의 `appifact-doc` JSON 블록을 디스크의 아트보드 · `canvas.json`으로 다시 채운다(`gen_canvas.py` 뒤 · publish 앞). design 스킬의 `seed-canvas.mjs`가 없을 때 쓴다 |
| `mkcompare.py` | 라이트/다크를 한 장에 나란히 놓은 비교 시트 HTML 생성 (아트보드가 아니라 검토용) |
| `calc/` | 시안에 적힌 완제일·도착일·총이자를 만들어 낸 상각·복리 계산기 |
| `darken.py` | 라이트 아트보드를 다크 토큰으로 변환(2026-09-26 기준 120장을 씀 · `Tokens` 제외). v4 · v5 생성기와 `gen_tour` · `gen_notify`는 다크 짝을 스스로 쓰지만, v3 생성기와 손편집 산물(`LedgerV5` · `MonthlyCloseV5` · `TransactionAddFromDaySheet` · `DesktopHomeV5` · 2026-09-26 새 모달 · 상태 장 포함)은 여기서만 다크가 만들어진다. 새 장을 더하면 이 파일의 목록에도 넣는다. `<!--dc-keep-->…<!--/dc-keep-->` 구간은 변환하지 않는다(라이트에서도 반전된 토스트 등). **꺼진 토글 손잡이와 세그먼트 선택 칸만은 토큰 표대로 `surface`로 바꾸지 않고** `KNOB_OFF_DARK`(`#8595AE`) · `SEG_ON_DARK`(`#2E3A54`)로 칠한다 — 트랙보다 어두우면 구멍 · 파인 자리처럼 보여서다. 토글 · 세그먼트 마크업을 바꿔 정규식이 못 잡으면 `assert`가 장 이름과 함께 멈춘다. **앱 outline 보조 버튼**(라이트 바탕 `#EDF0F7` + 1px `#E3E8F1` · 모서리 10/13 · 높이 32/44/46 — 확인 창 「취소」 · 미래 「부채 수정 ›」 · 「자산 탭에서 보기」 · 「그대로예요」)은 canvas 가 아니라 앱처럼 `rgba(57,69,95,.3)` + 1px `#39455F`(`_outline` · 2026-09-27 fix-up 6), 버튼 모양인데 바탕이 `#080C16` 으로 남으면 멈춘다 |

```bash
# 순서대로 — gen_v4_stocks가 gen_screens의 Payoff를 잘라 쓰므로 v3 생성기가 먼저
python3 gen_screens.py && python3 gen_modals.py && python3 gen_errors.py 2100 && python3 gen_rest.py 1920
# gen_v5.py가 gen_v4 · gen_v4_stocks를 import해서 v4 장도 같이 다시 쓴다. 뒤의 둘은 gen_v5의 조각을 쓴다
python3 gen_v5.py && python3 gen_v5_sheets.py && python3 gen_v5_screens.py
# Components 08절을 지금의 v5 장에서 다시 잘라 온다
python3 refresh_components_v5.py
# 첫 실행 안내(탭 장이 다시 써진 뒤) → 기기 알림
python3 gen_tour.py && python3 gen_notify.py
# 다크 → canvas.json → screens.json(0으로 끝나야 한다)
python3 darken.py && python3 gen_canvas.py && python3 sync_screens.py
```

v4 · v5 생성기는 `if __name__` 가드 없이 **import되는 순간 장을 씁니다.** 그래서 `gen_v5_screens.py` 하나만 돌려도 `gen_v5` → `gen_v4_stocks` → `gen_v4`가 차례로 다시 쓰입니다. 결과가 같으므로(멱등) 해는 없지만, v4 장만 고치고 싶을 때도 v5 장의 수정 시각이 바뀝니다.

`Main` · `HomeScroll` · `Assets` · `Spending` · `Limits` · `Goals` · `Future` · `LimitEditor` · `TransactionAdd` · `PeerStates` · `EmptyStates` · `DesktopHome` · `DesktopLedger` · `DesktopHomeV5`(v5 달력이 들어간 데스크톱 홈 · 1440 × 1273) · `Tokens` · `Components` 16종은 손으로 쓴 파일이라 생성 대상이 아닙니다(2026-09-26 앱 따라잡기에서 몇 장은 작업 폴더의 일회성 스크립트로 다시 썼고, 그 뒤로도 원본은 `.dc.html`). 다만 `Main` · `Goals` · `Future` · `Spending` · `Limits` · `PeerStates`(v4 · v5 생성기)와 `TransactionAdd`(`gen_modals.py`)는 생성기가 **잘라 쓰는 원본**이라, 고치면 그 생성기를 다시 돌려야 따라옵니다(잘라 올 마커가 바뀌면 생성기의 `assert`가 먼저 멈춥니다). **캔버스 편집기에서 직접 고친 내용은 스크립트를 다시 돌리면 덮어써집니다.** 한 번 손으로 고치기 시작했다면 `.dc.html`을 원본으로 삼고 스크립트는 `darken.py`만 쓰세요.

## 인계용 산출물 도구

인계용 산출물을 만드는 도구는 따로입니다. 아트보드를 바꾸지 않고 읽기만 합니다.

| 파일 | 역할 |
|---|---|
| `outline.py` | 아트보드 → `design/spec/<이름>.outline.md` 블록 개요. 400줄짜리 마크업을 150줄 구조로 줄인다 |
| `gen_spec_screens.py` | 아트보드 → `design/SPEC-SCREENS.md` 화면별 조립 체크리스트 |
| `render_png.py` | 아트보드 → PNG(기본 출력은 임시 폴더 `navi-preview/` · `--out`으로 바꿈 — 렌더는 저장소에 두지 않는다). 만든 앱을 같은 방식으로 캡처해 비교할 때도 쓴다 |

```bash
python3 outline.py && python3 gen_spec_screens.py && python3 render_png.py
```

`SPEC-COMPONENTS.md`는 손으로 쓴 문서라 생성 대상이 아닙니다.


## 프레임 높이

아트보드 높이는 `gen_canvas.py`의 `TALL` / `WIDE`, `screens.json`, 각 `.dc.html` 루트 div의 `height`
**세 곳이 같아야** 합니다. 루트에 `overflow: hidden`이 걸려 있어 어긋나면 소리 없이 잘립니다.
`sync_screens.py`가 `screens.json`을 `canvas.json`에 맞추고 `.dc.html` 루트와 크기가 어긋난 장을 알려 줍니다. 내용이 프레임을 넘쳐 잘리는지는
알려 주지 않으므로 높이는 여전히 아래 방법으로 직접 재야 합니다.

높이를 잴 때 주의할 것이 두 가지 있습니다. 둘 다 실제로 걸려서 카탈로그 시트 5장이 잘린 채로 있었습니다.

1. **반드시 실제 웹폰트(IBM Plex Sans KR)를 띄운 채로 재세요.** 네트워크가 막힌 환경에서 폴백 폰트로 재면
   한글 줄 높이가 짧게 나와 실제보다 20~70px 작은 값이 나옵니다. 웹폰트 CSS를 자체 호스팅해서 재는 것이 안전합니다.
2. **루트의 `scrollHeight`만 믿지 마세요.** 안쪽에 `overflow: hidden` 컨테이너가 있으면 잘린 만큼이
   `scrollHeight`에 안 잡힙니다. 루트 높이를 `auto`로 풀고 잰 **자연 높이**를 쓰세요.

현재 값은 전부 `자연 높이 + 아래 여백 24px`입니다.

## 라이트/다크 비교 시트

`python3 mkcompare.py`를 돌리면 스크래치 폴더에 비교용 HTML이 생깁니다. 브라우저로 열거나 헤드리스로 캡처해서 봅니다.
아트보드가 아니라 검토용 파생물이라 `canvas.json`에는 등록하지 않습니다.

## 페이지 배치

`gen_canvas.py`의 `PAGES`에는 **라이트 아트보드만** 적습니다. 다크 짝(`Dark<이름>`, 홈만 `DarkHome`)은
파일이 있으면 자동으로 **같은 x, 바로 아래 줄**에 놓입니다. 다크 파일이 없는 아트보드(토큰 시트)는
아래 줄을 비웁니다. 줄 간격은 `PAIR_GAP`(라이트→다크 52px)과 `GROUP_GAP`(다음 묶음까지 168px)입니다.

지금 페이지는 11개(화면 종류별 · 2026-09-22)이고 라이트는 159장입니다(2026-09-27 fix-up 3 뒤). 캔버스에 올리지 않는 원본 전용 장(`SOURCE_ONLY`)은 `Main` · `HomeScroll` · `Ledger` · `MonthlyClose` · `DesktopHome`(+다크)입니다.

| 페이지 id | 이름 | 라이트 |
|---|---|---|
| `home` | 홈 | 13 |
| `daysheet` | 하루 시트 · 기록 | 14 |
| `assets-spending` | 자산 · 소비 | 10 |
| `dest-future` | 목적지 · 미래 (지금 5탭 → 탭 합친 뒤) | 10 |
| `first-run` | 첫 실행 | 8 |
| `tour` | 첫 실행 안내 · 화면마다 3단계 | 37 |
| `stocks` | 주식 | 10 |
| `modals` | 모달 · 설정 | 22 |
| `desktop` | 데스크톱 | 2 |
| `states` | 상태 · 구현 참고 | 26 |
| `system` | 디자인 시스템 | 2 |
