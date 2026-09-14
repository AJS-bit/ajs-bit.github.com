# NAVI 디자인 저장소 — 작업 안내

이 저장소는 NAVI(자산 성장 내비게이션) 앱의 **디자인 산출물과 계획**만 담습니다.
원본 앱 소스는 여기 없습니다 — 사용자의 다른 저장소에 있고 코덱스가 v3 구현을 맡고 있습니다.

## 브랜치

- 작업 브랜치 **`claude/navi-ui-ux-redesign-nzxoxz`** 하나에만 커밋·푸시합니다. 기본 브랜치는 비어 있습니다.
- 다른 브랜치를 만들거나 푸시하지 않습니다. PR은 사용자가 시키기 전엔 만들지 않습니다.
- 커밋 메시지는 한국어로, **왜** 바꿨는지를 씁니다.

## 폴더

| 경로 | 무엇 |
|---|---|
| `design/` | **v3 디자인 인계 묶음(확정본).** 코덱스가 GitHub raw로 읽습니다. 입구 `design/여기부터.md`, 지시서 `design/CODEX-BRIEF.md` |
| `design/canvas/*.dc.html` | 아트보드 75장(라이트 38 · 다크 37). **값의 최종 기준** |
| `design/canvas/_tools/` | 생성기·다크 변환·렌더·계산기. 먼저 `_tools/README.md`를 읽을 것 |
| `design/SPEC-COMPONENTS.md` · `SPEC-SCREENS.md` | 컴포넌트 24개 실측 CSS · 화면별 조립 체크리스트 |
| `plan/v4-stocks.md` | **v4 계획.** §9에 결정 사항. 페이지판은 `plan/_tools/md2page.py`로 생성 |
| `plan/v5-calendar.md` | **v5 계획 — 홈 달력과 빠른 소비 입력.** §12에 결정 30개(1~9가 방향). 페이지판은 `md2page.py v5-calendar.md` |

## 지금 상태 (2026-09-14)

- **v3 완료.** 코덱스에 인계됨. 오류를 발견했을 때만 손댑니다.
- **v4 계획 승인됨** — `plan/v4-stocks.md` §9의 권장안 7개 전부 채택.
- **v4 1단계 시안 승인·커밋 (2026-09-14).** 소개 3장 · 홈 구성 · 구성 반영 홈, 라이트·다크 10장 → 캔버스 페이지 `v4 · 1단계 첫 실행`. 생성기 `gen_v4.py`.
- **v4 2~5단계 시안 승인·커밋 (2026-09-14).** 15장 × 2 = 30장이 캔버스 페이지 7~10(2단계 내비 · 3단계 주식 뼈대 ·
  4단계 카테고리 · 5단계 설정)에 올라가 있다(캔버스 v21). 생성기 `design/canvas/_tools/gen_v4_stocks.py`, 스냅숏 표본
  `design/stocks-snapshot.sample.json`(종목명만 실재, 수치는 전부 가상). 고칠 것이 있으면 생성기를 고쳐 다시 돌린다.
  각 페이지 위 노트에 가정을 적어 두었다. **다음 할 일 = 단계별 구현** (v3 코덱스 구현이 끝난 뒤 그 위에, 1단계부터).
  `preview/*.png`는 이 맥에 크로미움이 없어 v4 40장 모두 아직 못 찍었다.
- **v5 계획 5판 (2026-09-14~15) · 코덱스와 상호 검토 4라운드 완료 · 사용자 §12 결정 대기.** 사용자 피드백 "소비 입력이 불편하다"에서
  출발한 홈 달력 + 하루 시트(날짜 터치 → 숫자만 → 저장) + 나중에 분류 계획. `plan/v5-calendar.md`. 코덱스(herdr 패널 `w9:p2`,
  작업본 `~/Documents/Codex/2026-09-01/ai/work/wealth-navigator`)가 4라운드에 걸쳐 검토했고 기록은 `plan/reviews/v5-round1~4-claude.md`와
  코덱스 쪽 `~/Documents/Codex/2026-09-07/navi-handoff/outputs/NAVI-v5-*.md`. 핵심 합의: 분류 안 한 금액은 이번 달 예상에서 일할로
  늘리지 않음(`finance.ts` `unconfirmed` 옵션) · 예상 소비율 히어로는 '과거 마감 기록 기준' 규칙 통과 시에만(그 전엔 이번 달 기록한
  소비 합계) · 대상 지정 되돌리기 · 달력 칸 = 그날 소비 합계, 하루 기준선 제외 · 초안은 메모리만 · 보호 파일 변경 4건(`finance`·
  `navi-current`·`navi-import`·`navi-goals`)을 §12 절차로. 다음 = 사용자가 §12(37개, 1~18이 방향) 결정 → 1단계 시안. **아직 시안 없음.**

## 사용자가 정한 작업 규칙 — 반드시

1. **시안을 바꾸기 전에 before/after 렌더를 보여주고 검사받습니다.** 승인 전에 원본을 고치지 않습니다. 새 시안도 그려서 보여준 뒤 반영합니다.
2. 디자인 때문에 **계산식·거래 ID·백업 형식·반복 거래·계좌 연결·기존 기록**을 바꾸지 않습니다.
3. **로그인·클라우드 계정·실시간 외부 API·네트워크 필수 자산**을 새 요구사항으로 만들지 않습니다. 외부 서비스 없이 동작해야 합니다.
4. **미입력을 0원·0%·좋은 성과로 표시하지 않습니다.** 회색 `—`입니다. 또래 통계(평균·백분위·상위 %)를 지어내지 않습니다.
5. 시안의 숫자(완제일·도착일·총이자)는 `design/canvas/_tools/calc/`로 계산하고 `crosscheck.py`로 원본 엔진 포팅본과 대조합니다. **어긋나면 엔진이 맞습니다.** 확정값: 상환 총이자 1,734만원 · 완제 2036년 4월 · 소비율 57.9%(spendProjected 2,084,000).
6. 시뮬레이션은 저장 기록과 구분합니다 — 보라 `#7A3FE4` + 점선 테두리 + "저장되지 않는 가정" 배지.
7. 주식 화면에는 추천·매수·매도라는 말을 쓰지 않습니다. 가격 옆에는 항상 기준일을 붙입니다.

## 도구와 함정 — 지난 작업에서 실제로 걸린 것

- **아트보드 절반은 생성기 산물입니다.** `.dc.html`만 고치면 생성기를 다시 돌릴 때 되돌아갑니다. 생성기와 파일을 **둘 다** 고치세요. 손으로 쓴 파일 목록은 `_tools/README.md`에 있습니다.
- 다크 아트보드는 `darken.py`가 라이트에서 만듭니다. 라이트를 고친 뒤 `darken.py`를 다시 돌리세요. `<!--dc-keep-->` 구간은 변환에서 제외됩니다(토스트).
- 아트보드 높이는 **세 곳**이 같아야 합니다 — `.dc.html` 루트 `height` · `gen_canvas.py`의 `TALL/WIDE` · `screens.json`. 어긋나면 소리 없이 잘립니다.
- 높이·위치 측정은 **실제 웹폰트(IBM Plex Sans KR)를 띄운 채로** 하세요. 폴백 폰트로 재면 한글 줄 높이가 짧아 20~70px 작게 나옵니다. 루트 `scrollHeight`만 믿지 말고 자연 높이를 재세요.
- 아트보드는 `* { box-sizing: border-box }`입니다. `height`에 글자 높이만 넣으면 `padding`·`border`만큼 줄이 짧아집니다.
- 헤드리스 크로미움 `--window-size`는 창 크롬 높이를 포함해 **아래 87px이 잘립니다.** `render_png.py`는 이미 넉넉히 찍고 잘라냅니다. 직접 찍을 땐 같은 처리를 하세요.
- `justify-content: space-between` 3칸 줄은 양끝 폭이 다르면 가운데 라벨이 `(왼폭 − 오른폭) ÷ 2` 밀립니다. 양끝에 `flex: 1`을 주세요.
- 값에 따라 움직이는 좌표(항로 바, 슬라이더, 차트의 오늘 위치)는 `SPEC-COMPONENTS.md` §26의 식으로 계산해서 넣습니다. 손으로 찍지 않습니다.

```bash
# 렌더 · 개요 · 체크리스트 재생성
cd design/canvas/_tools && python3 outline.py && python3 gen_spec_screens.py && python3 render_png.py
# 생성기 전체 (손편집 파일은 건드리지 않음)
python3 gen_screens.py && python3 gen_modals.py && python3 gen_errors.py 2061 && python3 gen_rest.py 1767 && python3 darken.py && python3 gen_canvas.py
# 계산 검산
cd calc && python3 crosscheck.py
# v4 · v5 계획 페이지
python3 plan/_tools/md2page.py                  # v4-stocks.md → v4-stocks.html
python3 plan/_tools/md2page.py v5-calendar.md   # v5-calendar.md → v5-calendar.html
```

## 아트팩트 (같은 claude.ai 계정이면 `/artifacts`에 보입니다)

- **디자인 캔버스 (v3, 75장)** — https://claude.ai/code/artifact/986cf3e1-d0c7-4c28-94cb-c12c50ca7b46
  contract `0.1.31` 고정. 갱신은 `design/canvas/`를 design 스킬의 `seed-canvas.mjs`로 `navi-redesign.html`에 시드한 뒤 **이 URL을 `url`로 넘겨** publish. 새 캔버스를 만들지 마세요. v4 시안도 이 캔버스에 페이지를 추가합니다.
- **v4 계획 페이지** — https://claude.ai/code/artifact/26eb99d3-9719-407e-bd5d-345b1ab54fe1
  `plan/v4-stocks.md`가 원본. 고치면 `md2page.py`로 다시 만들어 이 URL로 publish.
- **v5 계획 페이지** — https://claude.ai/code/artifact/7000d83c-1af3-458a-a0e9-e4b82b461ef1
  `plan/v5-calendar.md`가 원본. 고치면 `md2page.py v5-calendar.md`로 다시 만들어 이 URL로 publish.
