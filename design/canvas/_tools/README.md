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
python3 gen_screens.py && python3 gen_modals.py && python3 gen_errors.py 2030 \
  && python3 gen_rest.py 1846 && python3 darken.py && python3 gen_canvas.py
```

`Main` · `Assets` · `Spending` · `Limits` · `Goals` · `Future` · `HomeScroll` · `PeerStates` · `EmptyStates` · `Desktop*` · `Tokens` · `Components`는 손으로 쓴 파일이라 생성 대상이 아닙니다. **캔버스 편집기에서 직접 고친 내용은 스크립트를 다시 돌리면 덮어써집니다.** 한 번 손으로 고치기 시작했다면 `.dc.html`을 원본으로 삼고 스크립트는 `darken.py`만 쓰세요.

## 프레임 높이

아트보드 높이는 `gen_canvas.py`의 `TALL` / `WIDE`와 각 `.dc.html` 루트 div의 `height`가 **같아야** 합니다.
루트에 `overflow: hidden`이 걸려 있어 어긋나면 소리 없이 잘립니다. 새 시트를 만들거나 내용을 늘렸으면
헤드리스로 `scrollHeight`를 재고 그 값을 두 곳에 함께 넣으세요.

## 라이트/다크 비교 시트

`python3 mkcompare.py`를 돌리면 스크래치 폴더에 비교용 HTML이 생깁니다. 브라우저로 열거나 헤드리스로 캡처해서 봅니다.
아트보드가 아니라 검토용 파생물이라 `canvas.json`에는 등록하지 않습니다.

## 페이지 배치

`gen_canvas.py`의 `PAGES`에는 **라이트 아트보드만** 적습니다. 다크 짝(`Dark<이름>`, 홈만 `DarkHome`)은
파일이 있으면 자동으로 **같은 x, 바로 아래 줄**에 놓입니다. 다크 파일이 없는 아트보드(토큰 시트)는
아래 줄을 비웁니다. 줄 간격은 `PAIR_GAP`(라이트→다크 52px)과 `GROUP_GAP`(다음 묶음까지 168px)입니다.
