# 아트보드 생성 도구

아트보드 59개를 일관된 조각으로 찍어내는 스크립트입니다. **최종 산출물은 상위 폴더의 `.dc.html` 파일**이고, 이 도구는 그것을 처음 만들 때와 다크 버전을 다시 뽑을 때 씁니다.

| 파일 | 역할 |
|---|---|
| `gen_common.py` | 색·아이콘·카드·버튼·입력·시트 등 공통 조각 |
| `gen_screens.py` | 새로 추가한 화면 7종 (온보딩·저장소 상태·부채·상환 전략·내역·목적지 설계·상환 계획) |
| `gen_modals.py` | 모달 11종 |
| `gen_canvas.py` | `canvas.json`(페이지·좌표·주석) 생성 |
| `darken.py` | 라이트 아트보드 26종을 다크 토큰으로 변환 |

```bash
python3 gen_screens.py && python3 gen_modals.py && python3 darken.py && python3 gen_canvas.py
```

`Main` · `Assets` · `Spending` · `Limits` · `Goals` · `Future` · `HomeScroll` · `PeerStates` · `EmptyStates` · `Desktop*` · `Tokens` · `Components`는 손으로 쓴 파일이라 생성 대상이 아닙니다. **캔버스 편집기에서 직접 고친 내용은 스크립트를 다시 돌리면 덮어써집니다.** 한 번 손으로 고치기 시작했다면 `.dc.html`을 원본으로 삼고 스크립트는 `darken.py`만 쓰세요.
