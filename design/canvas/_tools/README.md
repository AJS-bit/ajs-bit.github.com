# 아트보드 생성 도구

아트보드 193장(라이트 97 · 다크 96) 가운데 라이트 81종과 다크 96장을 일관된 조각으로 찍어내는 스크립트입니다(나머지 라이트 16종은 손으로 쓴 파일 — 아래 목록). **최종 산출물은 상위 폴더의 `.dc.html` 파일**이고, 이 도구는 그것을 처음 만들 때와 다크 버전을 다시 뽑을 때 씁니다.

| 파일 | 역할 |
|---|---|
| `gen_common.py` | 색·아이콘·카드·버튼·입력·시트 등 공통 조각 |
| `gen_calendar.py` | **홈 달력 공용 조각** — 자료(2026년 9월 · 8월) · 칸 · 접힘 카드(최근 7일 스트립) · 펼침 월 달력 · 상태 줄 · 적기 버튼 `+ 오늘 쓴 돈 적기` / 알약 `+ 더 적기`(줄 높이 40) · 오늘 칸 테두리와 `+`(2026-09-24 · 최종 점검 후속에서 스트립 수식어 줄 9 · 이체 · ✓와 함께인 `+` 16) · 오늘 0건(`today_empty`) · 처음 쓰는 날(`since`)은 펼침에도 · 그 달 기록 0건의 합계 줄 `9월 기록이 아직 없어요` · 홈 구성 행의 축소 미리보기(`calendar_card` · `calendar_thumb`). `gen_v4.py`(`gen_v4_stocks.py`는 그 `calendar_block`을 받아 씀) · `gen_v5.py` · `gen_v5_sheets.py`가 함께 쓰고, `gen_screens.py`는 `LedgerV5`의 날짜별 합계를 여기 자료와 맞춘다. `gen_common`만 import하고 파일을 쓰지 않는다. **홈에 달력이 나오는 장은 전부 여기서 가져온다 — 달력을 고칠 때는 이 파일 하나만 고친다** |
| `gen_screens.py` | 화면 8종 — v3 7종(온보딩·저장소 상태·부채·상환 전략·내역·목적지 설계·상환 계획) + v5 뒤의 내역 `LedgerV5`(분류 안 함 칩 · 날짜별 합계. v3 기준 그림 `Ledger`는 그대로 둔다) |
| `gen_modals.py` | 장 14개 — 모달 11종(알림 없음 `AlertsEmpty` 포함) · 확인 대화상자 시트 `Confirmations` + v5 뒤의 월 마감 `MonthlyCloseV5` · 구현 참고 장 `TransactionAddFromDaySheet`(960 × 850 · 손으로 쓴 `TransactionAdd.dc.html`을 읽어 값만 바꾼다 — 그 파일은 고치지 않는다) |
| `gen_errors.py` | 모달 오류·저장 상태 6종 시트 `ModalErrors` (`python3 gen_errors.py <높이>` · 기본 2100) |
| `gen_rest.py` | 장 5개 — 적립 모달 · 목적지 유형 5종 시트 · 소비 지난 달 · 코칭 기록 없음 + v5 구현 참고 장 `AlertsReview`(1200 × 1040 · 달력이 없을 때 「확인할 내용」이 보이는 곳) (`python3 gen_rest.py <유형 시트 높이>` · 기본 1920). `gen_modals`의 조각을 import하므로 모달 장도 같이 다시 쓴다(멱등) |
| `gen_v4.py` | **v4 · 1단계** 아트보드 8종과 다크 짝 — 소개 3장 · 홈 구성(첫 실행) `HomeSetup` · 주식을 켠 변형 `HomeSetupStocksOn` · 설정 시트의 `홈 구성 ›` 행 `SettingsHomeEntry` · 설정에서 들어온 홈 구성 `HomeLayoutEdit` · 구성 반영 홈 `HomeConfigured`. 홈은 `Main.dc.html`을 잘라 쓰고, `Main`에는 달력이 없으므로 `이번 달 달력` 카드와 홈 구성 첫 행의 미리보기는 `gen_calendar`에서 가져온다 |
| `gen_v4_stocks.py` | **v4 · 2~5단계** 아트보드 16종(내비 4 · 주식 뼈대 4 · 카테고리 탐색 6 · 설정 2)과 다크 짝, 스냅숏 표본 JSON. 목적지 탭 본문은 `Goals`·`Future`·`Payoff`를 잘라 쓴다(셋째 세그먼트 `DestPayoff`). 홈 두 장(`HomeStocksOff` · `HomeStocksCard`)은 `gen_v4`의 달력 든 홈을 받아 쓴다. `import gen_v4`라 1단계 8종도 같이 다시 쓴다(멱등) |
| `gen_v5.py` | **v5 · 1 · 2단계** 아트보드 17종과 다크 짝 — 홈 달력 5종(접힘 스트립 · 기본 5카드 전체 스크롤 `HomeDefaultScroll` 390 × 1360 · 펼침 월 달력 390/360 · 지난달 보기) + 하루 시트 쪽 8종(시트 기본 · 키보드를 내린 모습 `DaySheetScrolled` · 목록 우선 · 수정 · 360 × 640 · 완료 카드 · 분류하기 · 이력 부족 히어로) + 구현 참고 장 4종 = 저장을 한 번 더 물어보는 경우 1200 × 900 · 홈 맨 위 카드의 안내 줄 1200 × 640 · 달력 칸 읽는 법 1330 × 830 · 폭과 글자 크기 1150 × 1670 — 앱 화면이 아니라 설명 장이라 `spec_frame`으로 가로로 넓게 그린다. 펼침은 어느 폭에서도 7열 월 달력(계획 7판). 홈은 `Main.dc.html`을 잘라 쓰고 달력은 `gen_calendar`. **`gen_v4` · `gen_v4_stocks`를 import하므로 돌리면 v4 24종도 같이 다시 쓴다(멱등)** |
| `gen_v5_sheets.py` | **v5 · 하루 시트 · 완료 카드 · 상태 줄의 나머지 상태** 6종과 다크 짝 — 앱 화면 2종(소비 0건인 날 `DaySheetNoSpend` · 확인할 내용 목록 시트 `ReviewListSheet`) + 구현 참고 장 4종(`DaySheetNoSpendStates` 1200 × 1190 · `DoneCardStates` 1200 × 1100 · `DaySheetStates` 1210 × 1660 · `CalendarStatusLines` 1200 × 1570). `gen_v5`의 조각과 `w()`를 쓴다 — `import gen_v5`라 v4 · v5 장을 전부 다시 쓴다(멱등) |
| `gen_v5_screens.py` | **v5 · 달력 밖의 화면들** 6종과 다크 짝 — 구현 참고 장 5종(`InsufficientElsewhere` 1230 × 1390 · `FutureProvisional` 1230 × 1080 · `EtcSubline` 1200 × 970 · `LimitCardCases` 1200 × 960 · `ImportBackupNotes` 1230 × 1060) + 앱 화면 1종(`RecurringPrefill`). 손으로 쓴 `Spending` · `Limits` · `PeerStates` · `Future` · `Goals`는 `.dc.html`에서 잘라 쓰고, 모달 조각은 `gen_modals` · `gen_rest`를 import하지 않고 같은 모양으로 옮겨 적었다(import하면 그쪽 장을 다시 쓰므로). 계획에 원문이 없어 지은 문구 · 모양에는 `# 제안` 주석 |
| `gen_canvas.py` | `canvas.json`(페이지 14개 · 좌표 · 주석) 생성 |
| `refresh_components_v5.py` | `Components.dc.html`의 **08 · v5 절만** 지금의 v5 장(`HomeCalendarStrip` · `HomeCalendar` · `DaySheet` · `DoneCard` · `ClassifySheet` · `HeroInsufficient` · `HeroFootnotes`)에서 다시 잘라 와 채운다. 01~07절과 루트 크기는 건드리지 않는다. `gen_v5.py` 뒤 · `darken.py` 앞 |
| `sync_screens.py` | `gen_canvas.py` **뒤에** 돌린다. `canvas.json`의 제목 · 페이지 · 크기를 `design/screens.json`에 맞추고, `.dc.html` 루트 크기와 등록부가 어긋난 장 · 출처(`SOURCE`)가 없는 새 장을 알려 준다(있으면 종료 코드 1). 새 장을 더하면 이 파일의 `SOURCE`에 출처(앱 파일 또는 계획 절)를 적는다 |
| `seed_doc.py` | 캔버스 페이지 `navi-redesign.html` 안의 `appifact-doc` JSON 블록을 디스크의 아트보드 · `canvas.json`으로 다시 채운다(`gen_canvas.py` 뒤 · publish 앞). design 스킬의 `seed-canvas.mjs`가 없을 때 쓴다 |
| `mkcompare.py` | 라이트/다크를 한 장에 나란히 놓은 비교 시트 HTML 생성 (아트보드가 아니라 검토용) |
| `calc/` | 시안에 적힌 완제일·도착일·총이자를 만들어 낸 상각·복리 계산기 |
| `darken.py` | 라이트 아트보드 96종(`Tokens` 제외 전부)을 다크 토큰으로 변환. v4 · v5 생성기는 다크 짝을 스스로 쓰지만, v3 생성기와 손편집 산물(`LedgerV5` · `MonthlyCloseV5` · `AlertsReview` · `TransactionAddFromDaySheet` · `DesktopHomeV5` 포함)은 여기서만 다크가 만들어진다. 새 장을 더하면 이 파일의 목록에도 넣는다. `<!--dc-keep-->…<!--/dc-keep-->` 구간은 변환하지 않는다(라이트에서도 반전된 토스트 등). **꺼진 토글 손잡이와 세그먼트 선택 칸만은 토큰 표대로 `surface`로 바꾸지 않고** `KNOB_OFF_DARK`(`#8595AE`) · `SEG_ON_DARK`(`#2E3A54`)로 칠한다 — 트랙보다 어두우면 구멍 · 파인 자리처럼 보여서다. 토글 · 세그먼트 마크업을 바꿔 정규식이 못 잡으면 `assert`가 장 이름과 함께 멈춘다 |

```bash
# 순서대로 — gen_v4_stocks가 gen_screens의 Payoff를 잘라 쓰므로 v3 생성기가 먼저
python3 gen_screens.py && python3 gen_modals.py && python3 gen_errors.py 2100 && python3 gen_rest.py 1920
# gen_v5.py가 gen_v4 · gen_v4_stocks를 import해서 v4 장도 같이 다시 쓴다. 뒤의 둘은 gen_v5의 조각을 쓴다
python3 gen_v5.py && python3 gen_v5_sheets.py && python3 gen_v5_screens.py
# Components 08절을 지금의 v5 장에서 다시 잘라 온다
python3 refresh_components_v5.py
# 다크 96장 → canvas.json → screens.json
python3 darken.py && python3 gen_canvas.py && python3 sync_screens.py
```

v4 · v5 생성기는 `if __name__` 가드 없이 **import되는 순간 장을 씁니다.** 그래서 `gen_v5_screens.py` 하나만 돌려도 `gen_v5` → `gen_v4_stocks` → `gen_v4`가 차례로 다시 쓰입니다. 결과가 같으므로(멱등) 해는 없지만, v4 장만 고치고 싶을 때도 v5 장의 수정 시각이 바뀝니다.

`Main` · `HomeScroll` · `Assets` · `Spending` · `Limits` · `Goals` · `Future` · `LimitEditor` · `TransactionAdd` · `PeerStates` · `EmptyStates` · `DesktopHome` · `DesktopLedger` · `DesktopHomeV5`(v5 달력이 들어간 데스크톱 홈 제안 · 1440 × 1000) · `Tokens` · `Components` 16종은 손으로 쓴 파일이라 생성 대상이 아닙니다. 다만 `Main` · `Goals` · `Future` · `Spending` · `Limits` · `PeerStates`(v4 · v5 생성기)와 `TransactionAdd`(`gen_modals.py`)는 생성기가 **잘라 쓰는 원본**이라, 고치면 그 생성기를 다시 돌려야 따라옵니다(잘라 올 마커가 바뀌면 생성기의 `assert`가 먼저 멈춥니다). **캔버스 편집기에서 직접 고친 내용은 스크립트를 다시 돌리면 덮어써집니다.** 한 번 손으로 고치기 시작했다면 `.dc.html`을 원본으로 삼고 스크립트는 `darken.py`만 쓰세요.

## 인계용 산출물 도구

인계용 산출물을 만드는 도구는 따로입니다. 아트보드를 바꾸지 않고 읽기만 합니다.

| 파일 | 역할 |
|---|---|
| `outline.py` | 아트보드 → `design/spec/<이름>.outline.md` 블록 개요. 400줄짜리 마크업을 150줄 구조로 줄인다 |
| `gen_spec_screens.py` | 아트보드 → `design/SPEC-SCREENS.md` 화면별 조립 체크리스트 |
| `render_png.py` | 아트보드 → `design/preview/*.png`. 만든 앱을 같은 방식으로 캡처해 비교할 때도 쓴다 |

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

지금 페이지는 14개이고 라이트는 97장입니다(2026-09-21 최신화 반영 뒤). 12~14는 그때 새로 생긴 페이지이고, `CalendarCells` · `CalendarGridSizes` · `HeroFootnotes` · `DaySheetConfirm`은 11에서 12로 옮겼습니다.

| 페이지 | 이름 | 라이트 |
|---|---|---|
| `page-1` | 모바일 · 화면 | 14 |
| `page-2` | 모바일 · 모달 | 15 |
| `page-3` | 상태 카탈로그 | 6 |
| `page-4` | 데스크톱 | 3 |
| `page-5` | 디자인 시스템 | 2 |
| `page-6` | v4 · 1단계 첫 실행 | 8 |
| `page-7` | v4 · 2단계 내비 | 4 |
| `page-8` | v4 · 3단계 주식 뼈대 | 4 |
| `page-9` | v4 · 4단계 카테고리 | 6 |
| `page-10` | v4 · 5단계 설정 | 2 |
| `page-11` | v5 · 달력과 하루 시트 (1 · 2단계) | 15 |
| `page-12` | v5 · 구현 참고 장 | 8 |
| `page-13` | v5 · 다른 화면에 닿는 곳 | 6 |
| `page-14` | v5 · 3단계 한도 라벨 · 반복 거래 · 백업 | 4 |
