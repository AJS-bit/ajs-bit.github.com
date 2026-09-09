# 아트보드 생성 도구

아트보드 75개를 일관된 조각으로 찍어내는 스크립트입니다. **최종 산출물은 상위 폴더의 `.dc.html` 파일**이고, 이 도구는 그것을 처음 만들 때와 다크 버전을 다시 뽑을 때 씁니다.

| 파일 | 역할 |
|---|---|
| `gen_common.py` | 색·아이콘·카드·버튼·입력·시트 등 공통 조각 |
| `gen_screens.py` | 새로 추가한 화면 7종 (온보딩·저장소 상태·부채·상환 전략·내역·목적지 설계·상환 계획) |
| `gen_modals.py` | 모달 11종 |
| `gen_errors.py` | 모달 오류·저장 상태 6종 시트 (`python3 gen_errors.py <높이>`) |
| `gen_rest.py` | 적립 모달 · 목적지 유형 5종 · 소비 지난 달 · 코칭 기록 없음 (`python3 gen_rest.py <유형 시트 높이>`) |
| `gen_canvas.py` | `canvas.json`(페이지·좌표·주석) 생성 |
| `mkcompare.py` | 라이트/다크를 한 장에 나란히 놓은 비교 시트 HTML 생성 (아트보드가 아니라 검토용) |
| `calc/` | 시안에 적힌 완제일·도착일·총이자를 만들어 낸 상각·복리 계산기 |
| `darken.py` | 라이트 아트보드 37종을 다크 토큰으로 변환. `<!--dc-keep-->…<!--/dc-keep-->` 구간은 변환하지 않는다(라이트에서도 반전된 토스트 등) |

```bash
python3 gen_screens.py && python3 gen_modals.py && python3 gen_errors.py 2061 \
  && python3 gen_rest.py 1767 && python3 darken.py && python3 gen_canvas.py
```

`Main` · `Assets` · `Spending` · `Limits` · `Goals` · `Future` · `HomeScroll` · `PeerStates` · `EmptyStates` · `Desktop*` · `Tokens` · `Components`는 손으로 쓴 파일이라 생성 대상이 아닙니다. **캔버스 편집기에서 직접 고친 내용은 스크립트를 다시 돌리면 덮어써집니다.** 한 번 손으로 고치기 시작했다면 `.dc.html`을 원본으로 삼고 스크립트는 `darken.py`만 쓰세요.

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
