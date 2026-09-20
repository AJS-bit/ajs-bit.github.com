# 컴포넌트 사양서 — 이 파일을 먼저 구현하세요

v3 아트보드 77장에 나오는 모든 블록은 **아래 24개 컴포넌트의 조합**입니다.
화면마다 div를 새로 짜면 시안과 달라집니다. 여기 있는 것을 먼저 공통 컴포넌트로 만들고,
화면은 그 컴포넌트를 배치하는 일만 하세요.

**v5(홈 달력 · 하루 시트)에서 11종이 늘었습니다 — §27.** 컴포넌트 장(`Components`) 08절에 같은 조각이 있습니다.

- 값은 **아트보드에서 그대로 뽑은 실측치**입니다. 반올림하거나 "비슷한 Tailwind 클래스"로 바꾸지 마세요.
  `13.5px`는 `text-sm`(14px)이 아닙니다. `border-radius: 18px`는 `rounded-2xl`(16px)이 아닙니다.
- 다크 값은 `canvas/_tools/darken.py`의 `MAP`이 유일한 기준입니다. 여기 적힌 다크 값도 거기서 나왔습니다.
- 표에 없는 색을 새로 만들지 마세요. 필요하면 `tokens.v3.json`에서 고릅니다.

---

## 0. 화면 프레임

```
width 390 · height 844 · background #EDF0F7 (dark #080C16)
color #101828 (dark #EAEFF8) · display flex · flex-direction column
overflow hidden · font-variant-numeric tabular-nums
```

`font-variant-numeric: tabular-nums`는 **루트에 한 번** 겁니다. 숫자 열이 흔들리지 않게 하는 장치라
빠뜨리면 자산·거래 리스트가 시안과 다르게 보입니다.

폰트: `IBM Plex Sans KR` (300/400/500/600/700), 폴백 `Apple SD Gothic Neo, Noto Sans KR, system-ui, sans-serif`.

세로 구성은 항상 이 순서입니다:

| 순서 | 블록 | 높이 |
|---|---|---|
| 1 | SampleBanner (샘플 데이터일 때만) | 32px |
| 2 | Header + PageTitle | 내용에 따라 |
| 3 | 본문 `flex:1; min-height:0; overflow:hidden; padding: 0 14px` | 나머지 |
| 4 | BottomNav | 66px |

본문 `min-height: 0`이 없으면 flex 자식이 넘쳐서 그래프가 잘립니다. 2.2에서 그래프가 잘리던 원인 중 하나입니다.

---

## 1. SampleBanner

```
height 32 · padding 0 14 · background #E9EDFD (dark #1B2748)
display flex · align-items center · justify-content space-between · gap 8 · flex-shrink 0
좌: 12px/500 #3B4E8F (dark #A8BCF5)
우: 12px/600 #3556E6 (dark #7FA0FF)   ← "내 데이터로 시작 ›"
```

샘플 데이터를 보고 있을 때만 붙습니다. 실제 데이터에서는 이 32px가 없어지고 본문이 그만큼 늘어납니다.

## 2. Header

```
컨테이너: display flex · flex-direction column · gap 6 · padding 12 16 10 · flex-shrink 0
1행: 좌 [앱마크 + "NAVI"] / 우 [아이콘 버튼 n개]  (space-between)
  앱마크: 28×28 · border-radius 9 · background linear-gradient(140deg, #3556E6 0%, #7A3FE4 100%)
          안에 흰 화살표 svg 15×15
  워드마크: 15px/700 · letter-spacing 0.06em · #101828
  아이콘 버튼: 36×36 · border-radius 11 · svg 19×19 · stroke #475467 · stroke-width 1.7
  알림 배지: position absolute · top 4 · right 4 · min-width 15 · height 15 · radius 99
             background #C0342F · color #FFFFFF · 10px/700 · padding 0 4 · border 2px solid #EDF0F7
```

**앱마크 path는 이 값을 그대로 쓰세요** (viewBox 0 0 24 24, fill #FFFFFF):

```
M20.28 2.32 2.88 9.62c-.9.4-.8 1.7.1 2l6.6 2.2c.3.1.5.3.6.6l2.2 6.6c.3.9 1.6 1 2 .1L21.68 3.72c.3-.8-.6-1.7-1.4-1.4Z
```

이전 path는 광학 중심이 오른쪽 아래로 0.7px 밀려 있었습니다. 고친 값이라 되돌리지 마세요.

## 3. PageTitle

```
display flex · align-items baseline · justify-content space-between · gap 8
제목 h1: margin 0 · 21px/700 · letter-spacing -0.03em · line-height 1.25 · #101828
우측 캡션: 12px/500 · #626D88 (dark #8595AE)
```

모달·시트의 제목은 `18px/700 · letter-spacing -0.025em`입니다(§14).

## 4. HeroCard — 화면당 **최대 1개**

```
background #FFFFFF (dark #121A2B) · border 1px solid #E3E8F1 (dark #232D45)
border-radius 20 · padding 16 · flex-shrink 0
box-shadow: 0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)
```

그림자가 있는 카드는 화면에서 이것 하나뿐입니다. 나머지 카드는 §5. 그림자를 여기저기 붙이면
"다 비슷해 보인다"는 원래 문제로 돌아갑니다.

내부 순서(홈 기준):

1. SectionLabel `현재 위치` + StatusPill (space-between)
2. display 숫자 줄 — `margin-top: 8`
3. 설명 줄 + 보조 지표 — `margin-top: 5`
4. RouteBar — `margin-top: 15`
5. StatTriple — `margin-top: 14`
6. 각주 + 인라인 링크 — `margin-top: 12`
7. PrimaryButton — `margin-top: 10`

## 5. Card

세 가지 크기만 씁니다. 그림자 없음.

| 이름 | radius | padding | 쓰는 곳 |
|---|---|---|---|
| `Card(20)` | 20 | 16 | 섹션 대표 카드 |
| `Card(18)` | 18 | 14 또는 14 15 또는 16 | 기본. 가장 많이 나옴 |
| `Card(18) 조밀` | 18 | 13 14 | 아이콘+2줄짜리 얇은 카드 |

```
background #FFFFFF (dark #121A2B) · border 1px solid #E3E8F1 (dark #232D45) · flex-shrink 0
```

## 6. SectionLabel

```
11px/600 · letter-spacing 0.07em · color #626D88 (dark #8595AE)
```

리스트 위 구분 라벨은 `11px/600 · letter-spacing 0.06em · #606B7D (dark #8A95AB) · padding 6px 2px 0`.

## 7. StatusPill

```
display inline-flex · align-items center · gap 4 · border-radius 99 · padding 4px 9px · 11.5px/600
안에 svg 11×11 (stroke-width 3)을 넣을 수 있음
```

| 변형 | background | color | dark bg | dark color |
|---|---|---|---|---|
| positive | `#E4F4EA` | `#0F7B47` | `#0F2C22` | `#3DD489` |
| violet | `#F1EAFD` | `#6B32D6` | `#241D3D` | `#C4A9FF` |
| warning | `#FDF1E0` | `#B45309` | `#2E2617` | `#F5B544` |
| negative | `#FCEBEA` | `#C0342F` | `#331C1F` | `#E8635F` |
| sky | `#E4F2FB` | `#0A72AC` | `#12293C` | `#5CC3F5` |

## 8. RouteBar — 제품의 서명 요소

```
트랙:  position relative · height 10 · border-radius 99 · background #E8ECF5 (dark #232D45) · overflow visible
진행:  position absolute · inset 0 {100-p}% 0 0 · border-radius 99
       background linear-gradient(90deg, #3556E6 0%, #6E6BEE 100%)   (dark #7FA0FF → #9AA0FF)
깃발:  position absolute · left {목표}% · top -5 · width 2 · height 20 · border-radius 2
       background #101828 (dark #EAEFF8)
라벨줄: position relative · height 15 · margin-top 5
       좌 "0%" 11px #626D88 / 중앙 "내 목표 60%" 11px/600 #101828 (left {목표}%, transform translateX(-50%), white-space nowrap) / 우 "100%" 11px #626D88
```

`overflow: visible`이어야 깃발이 트랙 위아래로 나옵니다. `hidden`으로 두면 깃발이 잘려서 사라집니다.

일반 진행바(목표·한도 등)는 깃발 없이:
```
position relative · height 6 (또는 8, 9) · border-radius 99 · background #EFF2F8 (dark #1E2739) · overflow hidden
```

## 9. StatTriple

```
display grid · grid-template-columns repeat(3, minmax(0, 1fr)) · gap 0
margin-top 14 · padding-top 13 · border-top 1px solid #EFF2F8 (dark #1E2739)

1열: padding-right 10
2열: padding 0 10 · border-left 1px solid #EFF2F8
3열: padding-left 10 · border-left 1px solid #EFF2F8

각 칸: display flex · flex-direction column · gap 3
  라벨 11.5px/500 #626D88
  값   18px/600 · letter-spacing -0.02em · #101828
  단위 13px/500 #475467  ← 값 span 안에 중첩
```

칸 사이는 `gap`이 아니라 **border-left**로 가릅니다. gap을 쓰면 선이 안 생깁니다.

## 10. DataRow — 가운데 정렬 타일을 대체하는 기본형

```
display flex · align-items center · justify-content space-between · gap 8
왼쪽: 이름 13.5px/600 #101828 + 보조 11.5px/500 #626D88 (아래줄)
오른쪽: 금액 우측 정렬 · tabular · 14px/600 #101828 + 비중 11.5px #626D88
행 구분: border-bottom 1px solid #F3F5FA (dark #1E2739) — 마지막 행은 없음
```

금액은 **반드시 오른쪽 정렬**입니다. 자릿수를 눈으로 비교하게 만드는 것이 이 화면들의 목적입니다.

## 11. TurnCard — "다음 안내"

```
display flex · gap 12 · padding 13px 14px · border-radius 18
background #FFFFFF (dark #121A2B) · border 1px solid #E3E8F1 (dark #232D45)
border-left 3px solid #DE8A2A (dark #A9772C)      ← 왼쪽 세로 액센트가 이 카드의 표식
아이콘 타일: 34×34 · border-radius 11 · background #FDF1E0 (dark #2E2617)
            svg 18×18 · stroke #B45309 (dark #F5B544) · stroke-width 2
본문: display flex · flex-direction column · gap 3 · min-width 0
  라벨 11px/600 · letter-spacing 0.06em · #B45309 (dark #F5B544)
  지시 15px/600 · letter-spacing -0.015em · line-height 1.35 · #101828
  근거 12.5px/400 · line-height 1.45 · #475467
  링크 12.5px/600 · #3556E6 · margin-top 5
```

`border-left: 3px`가 이 카드를 다른 카드와 가르는 유일한 신호입니다. 빼면 평범한 Card(18)가 됩니다.

## 12. GoalRing

```
52×52 · border-radius 99
background conic-gradient(#7A3FE4 0% {p}%, #E8ECF5 {p}% 100%)
  dark: conic-gradient(#B79BFF 0% {p}%, #232D45 {p}% 100%)
안쪽 구멍: 40×40 · border-radius 99 · background #FFFFFF (dark #121A2B)
가운데 텍스트: 13px/700 · letter-spacing -0.02em · #7A3FE4 (dark #B79BFF)
```

SVG 대신 conic-gradient입니다. 라이브러리 쓰지 마세요.

## 13. 버튼

```
공통: display flex · align-items center · justify-content center · gap 6 · border-radius 13 · 15px/600
```

| 이름 | height | background | border | color |
|---|---|---|---|---|
| Primary | 48 (히어로 안에서는 46) | `#3556E6` | none | `#FFFFFF` |
| Secondary | 48 / 46 / 44 | `#FFFFFF` | `1px solid #D7DEEA` | `#475467` |
| Danger | 44 | `#FCEBEA` | none | `#C0342F` |
| Disabled | 48 | `#F0F2F7` (dark `#1E2739`) | none | `#B4BECD` (dark `#5D6B85`) |

다크: Primary `#7FA0FF` 위에 글자 `#080C16`, Secondary 배경 `#121A2B` · 테두리 `#2E3A54` · 글자 `#A5B2C9`.

두 개를 나란히 둘 때는 **취소 `flex: 1` / 실행 `flex: 1.4`**입니다. 1:1이 아닙니다.

**화면당 Primary는 하나.** 두 개가 나란히 경쟁하던 것이 2.2의 문제였습니다.

## 14. InputField

```
라벨: 12px/600 #475467 · margin-bottom 7   (필수 표시는 뒤에 <span color #C0342F>*</span>, 필수가 아닌 칸은 11px/500 #697182 "선택 사항")
필드: display flex · align-items center · gap 5 · height 46 · padding 0 12
      border-radius 11 · border 1px solid #CFD7E6 (dark #39455F) · background #FFFFFF (dark #121A2B)
텍스트 입력: flex 1 · 15px/400 · #101828 · overflow hidden · white-space nowrap
숫자 입력:  flex 1 · text-align right · 17px/600 · #101828   + 단위 13px/500 #626D88
셀렉트:     justify-content space-between · 값 15px/500 + 아래화살표 svg 16×16 stroke #697182
도움말: 11.5px #626D88 · margin-top 6
```

숫자는 오른쪽 정렬 17px, 글자는 왼쪽 정렬 15px입니다. 섞지 마세요.

## 15. Callout

```
display flex · gap 8 · padding 10px 11px · border-radius 12
아이콘: svg 14×14 · flex-shrink 0 · margin-top 1
본문: 11.5px · line-height 1.5
```

| 변형 | background | 아이콘·글자 | dark bg |
|---|---|---|---|
| info | `#F4F6FB` | `#626D88` | `#1A2337` |
| warn | `#FDF1E0` | `#B45309` | `#2E2617` |
| danger | `#FCEBEA` | `#C0342F` | `#331C1F` |

강조는 본문 안에서 `<b style="font-weight:600">`로만 합니다. 색을 또 바꾸지 않습니다.

## 16. Segmented (탭)

```
컨테이너: display flex · gap 4 · padding 3 · border-radius 12 · background #E3E8F1 (dark #232D45)
활성:   flex 1 · height 36 · border-radius 9 · background #FFFFFF (dark #2E3A54 — surface #121A2B 가 아니다. 트랙보다 밝아야 떠 보인다) · 13.5px/600 #101828
        box-shadow 0 1px 2px rgba(16,24,40,.06)
비활성: flex 1 · height 36 · border-radius 9 · 13.5px/500 #5B6880 (dark #8595AE) · background 없음
```

## 17. BottomNav

```
컨테이너: display flex · align-items flex-start · justify-content space-between · gap 2
          height 66 · padding 8px 10px 0 · background #FFFFFF (dark #121A2B)
          border-top 1px solid #E3E8F1 (dark #232D45) · flex-shrink 0
칸: display flex · flex-direction column · align-items center · gap 3 · flex 1 · padding-top 4
활성:   아이콘틀 40×24 · border-radius 99 · background #E9EDFD (dark #1B2748) · svg stroke #3556E6 stroke-width 2
        라벨 11px/600 #3556E6
비활성: 아이콘틀 40×24 (배경 없음) · svg stroke #606B7D stroke-width 1.9
        라벨 11px/500 #606B7D (dark #8A95AB)
아이콘 svg는 18×18
```

5칸 순서: 홈 · 자산 · 소비 · 목표 · 미래. (화면 제목은 "목적지"지만 **탭 라벨은 "목표"**입니다 — 아트보드 그대로 두세요)

**v4 2단계(내비 재편)부터** 칸 구성이 바뀝니다. 치수 · 색은 위 그대로이고 칸 수와 라벨만 다릅니다(`plan/v4-stocks.md` §4).

| 사용자 | 칸 | 아이콘 |
|---|---|---|
| 주식을 켠 사용자 | 홈 · 자산 · 소비 · 주식 · 목적지 (5칸) | home · wallet · card · candle · flag |
| 주식을 끈 사용자 | 홈 · 자산 · 소비 · 목적지 (4칸) | home · wallet · card · flag |

`목표` · `미래` 탭은 없어지고 `목적지` 한 탭 안의 세그먼트(`내 목적지 / 자산 경로 / 상환 계획`)가 됩니다. 6칸이나 자산 탭 아래 주식 세그먼트는 쓰지 않습니다.
출시 순서가 v3 → v4-1 → v5-1 → v5-2 → v4-2 이므로 **v5 1 · 2단계 화면의 하단 탭은 아직 `홈 · 자산 · 소비 · 목표 · 미래`**입니다.

## 18. BottomSheet (모달)

```
스크림: 화면 전체 background #2A3245 (dark #04070E)
        상단 여백 190 · 맨 아래 가운데에 "배경을 눌러 닫기" 11.5px/500 rgba(255,255,255,.62)
시트:   flex 1 · min-height 0 · background #FFFFFF (dark #121A2B)
        border-radius 26px 26px 0 0 · display flex · flex-direction column · overflow hidden
손잡이: 38×4 · border-radius 99 · background #D7DEEA (dark #2E3A54) · padding 9px 0 0 가운데
헤더:   display flex · align-items flex-start · justify-content space-between · gap 10
        padding 12px 18px 14px · border-bottom 1px solid #EFF2F8
        h2 18px/700 letter-spacing -0.025em / p margin 4px 0 0 · 12.5px · line-height 1.45 · #626D88
        닫기 36×36 · border-radius 11 · background #F4F6FB · svg 17×17 stroke #475467
본문:   flex 1 · min-height 0 · overflow hidden · padding 14px 18px 0 · display flex · flex-direction column · gap 15
푸터:   display flex · gap 10 · padding 12px 18px 20px · border-top 1px solid #EFF2F8 · flex-shrink 0
```

### 하루 시트 변형 (v5 · `DaySheet` · `DaySheetList` · `DaySheetEdit` · `ClassifySheet`)

```
스크림: 상단 여백 60(키보드가 열린 기본 상태) · 맨 아래 가운데 11px/500 line-height 1.4 rgba(255,255,255,.62)
        "배경을 눌러 닫기 · 앱이 다시 시작되면 저장하지 않은 내용은 사라져요"
시트:   위와 같음(border-radius 26px 26px 0 0 · 손잡이 38×4)
헤더:   padding 12px 18px 12px · border-bottom 1px solid #EFF2F8 · 높이 약 44 + 둘째 줄
        왼쪽 ‹ 18×18 stroke #475467 · h2 18px/700 -0.025em nowrap · "오늘" 12.5px/500 #626D88 margin-left 6
        오른쪽 › 18×18 (갈 수 없으면 stroke #C4CCDA) · 둘째 줄 12.5px #626D88 · 닫기는 글자 13px/600 #475467
본문:   padding 12px 18px 0 · gap 10
        금액 칸 height 48 · radius 12 · 포커스 1.5px #3556E6 + 0 0 0 3px rgba(53,86,230,.16)
                라벨 12px/600 #475467 · 값 20px/600 -0.02em · 단위 13px/500 #626D88
        메모 칸 height 44 · radius 12 · border 1px solid #CFD7E6 · 값 15px
저장:   height 52 · radius 14 · 16px/600 · background #3556E6 — 시트의 유일한 채운 버튼
키보드: 기기가 그림 · 약 280px · 그 위로 날짜 · 금액 · 저장이 보여야 함
```

확인 없이 닫히고 초안은 메모리에만 둡니다(앱을 다시 켜면 사라짐 — 오류 F 의 하루 시트 예외).

## 19. Toast

**다크 모드에서 반전하지 않는 유일한 요소입니다.** 라이트에서도 어두운 배경입니다.

```
display flex · align-items center · gap 10 · padding 12px 14px · border-radius 13
background #101828 · box-shadow 0 12px 30px -14px rgba(16,24,40,.5)
글자 #FFFFFF
```

아트보드에서는 `<!--dc-keep-->…<!--/dc-keep-->`로 감싸 다크 변환에서 제외했습니다.
구현할 때도 다크 토큰을 적용하지 마세요.

## 20. EmptyState

**가운데 정렬이 아닙니다.** Card(20) 안의 왼쪽 정렬 2단 구성입니다.

```
Card(20) · padding 16
윗줄: display flex · gap 11
  아이콘틀 36×36 · border-radius 12 · background #F4F6FB (dark #1A2337)
           svg 19×19 · stroke #626D88 · stroke-width 1.8
  제목 15px/600 · letter-spacing -0.015em · #101828
  설명 p · margin 5px 0 0 · 12.5px · line-height 1.5 · #475467
아랫줄: 3열 grid · margin-top 14 · 어떤 값이 왜 비는지 설명
```

**빈 상태를 0원이나 좋은 성과로 표시하지 마세요.** "아직 없음"과 "0원"은 다릅니다.

## 21. 차트

라이브러리 기본 스타일을 그대로 쓰면 시안과 달라집니다. 규칙:

- **Y축 눈금 없음.** 필요한 지점에만 옅은 기준선(`1px dashed #E3E8F1`) + 인라인 라벨 11px #626D88.
- **높이 고정**: 소비 추이 150 · 미래 150 · 스파크라인 58. 부모 높이와 충돌시키지 마세요.
- **폭을 끝까지**: 좌우 패딩 안에서 `width: 100%`. 오른쪽 여백을 남기지 않습니다.
- **끝점 값 라벨**: 12px/600 #101828. 툴팁 없이 읽혀야 합니다.
- 실측 구간은 실선, 예상 구간은 점선. 쓰이는 값은 `4 4`(기본) · `5 5` · `6 5` · `5 4` 뿐입니다.
- 밴드(낙관/보수 범위)는 `fill` + `opacity 0.14`.
- 색은 `tokens.v3.json`의 데이터 팔레트에서만.
- **x·y 좌표를 아트보드에서 베끼지 마세요.** 아트보드는 "9월 8일, 순자산 9,350만원"이라는 하루치
  스냅숏입니다. 좌표는 §26의 식으로 **매번 계산**해야 합니다.

### 소비 추이 차트의 좌표

`viewBox="0 0 362 150"` · 그림 영역 x는 **12 ~ 350**(좌우 12씩 여백).

```
D = 그 달의 일수 (28·29·30·31)      d = 날짜 (1 ~ D)
x(d) = 12 + (d - 1) / (D - 1) * 338
```

오늘(d=today)에 붙는 요소는 **전부 같은 x(today)**입니다. 하나라도 다른 x를 쓰면 어긋납니다.

| 요소 | 아트보드 값 (오늘 = 8일, 30일 달) |
|---|---|
| 세로 강조선 `<line>` | `x1=x2=93.6` · y 60→118 · stroke `#DCE2EC` |
| 오늘 점 `<circle r="4">` | `cx=93.6` |
| 점 후광 `<circle r="7.5" fill-opacity=".15">` | `cx=93.6` |
| 누적 값 라벨 `<text text-anchor="middle">` | `x=93.6` · y = 점 y − 10.5 |
| x축 "오늘" 눈금 | `x=93.6` · y=133 |

검산: `12 + 7/29 * 338 = 93.6` ✓

실선은 `x(1) → x(today)`, 점선 예상은 `x(today) → x(D)`입니다.

x축 눈금은 **1일**(왼쪽 끝, `text-anchor="start"`)과 **말일**(오른쪽 끝, `text-anchor="end"`)이 고정이고,
그 사이 눈금은 7일 간격입니다. **"오늘" 라벨은 눈금과 별개 요소**로 `x(today)`에 붙입니다.
아트보드는 오늘이 마침 8일이라 눈금과 겹쳐 한 덩어리로 보이지만, 겹치지 않는 날이 대부분입니다.
오늘 라벨이 다른 눈금과 12px 안으로 가까워지면 **그 눈금을 지우세요.** 둘 다 그리면 글자가 겹칩니다.

### 미래 차트의 좌표

`viewBox="0 0 362 150"` · x는 **10 ~ 352**, 0년~10년.

```
x(년) = 10 + 년 / 10 * 342
y(원) = 103.9 - (원 / 1억 - 1) * 28.1        // 기준선 1억 y=103.9, 1억당 28.1px
```

기준선은 1억 `y=103.9` · 2억 `75.8` · 3억 `47.7` · 4억 `19.6`.
검산: 시작 9,350만 → `103.9 + 0.065*28.1 = 105.7` ✓ · 10년 뒤 3억 2,126만 → `41.7` ✓

## 22. 아이콘

전부 인라인 SVG, `viewBox="0 0 24 24"`, `fill="none"`, `stroke-linecap="round"`, `stroke-linejoin="round"`.

| 자리 | size | stroke-width |
|---|---|---|
| 헤더 | 19 | 1.7 |
| 바텀 네비 활성 | 18 | 2 |
| 바텀 네비 비활성 | 18 | 1.9 |
| 카드 타일 | 16 | 1.9 |
| 인라인 셰브론 | 13 | 2.2 |
| Callout | 14 | 1.9 |
| 체크(필) | 11 | 3 |

path는 `canvas/_tools/gen_common.py`의 `_P` 딕셔너리에 전부 있습니다. **거기서 복사하세요.**
lucide/heroicons에서 비슷한 걸 가져오면 획 두께와 광학 크기가 달라집니다.

## 23. 셰브론 링크

값 옆에 붙는 인라인 이동:

```
display inline-flex · align-items center · gap 4 · flex-shrink 0
라벨 11px/500 #697182 · 값 13px/600 letter-spacing -0.02em #475467
셰브론 svg 13×13 stroke #697182 stroke-width 2.2 · align-self center
```

행 오른쪽 끝의 "더 보기"류는 `11.5px/600 #3556E6` + `›`(`&rsaquo;`).

## 24. 구분선

| 쓰임 | 값 |
|---|---|
| 카드 안 섹션 구분 | `1px solid #EFF2F8` (dark `#1E2739`) |
| 리스트 행 구분 | `1px solid #F3F5FA` (dark `#1E2739`) |
| 카드 테두리 | `1px solid #E3E8F1` (dark `#232D45`) |
| 입력 테두리 | `1px solid #CFD7E6` (dark `#39455F`) |

## 25. Slider

```
트랙: position relative · height 20 (또는 22)
  바닥  position absolute · left 0 · right 0 · top 8 · height 5 · border-radius 99
        background #E8ECF5 (dark #232D45)
  채움  position absolute · left 0 · width {p}% · top 8 · height 5 · border-radius 99
        background {강조색}
  손잡이 position absolute · left {p}% · top 0 · width 20 · height 20 · margin-left -10
        border-radius 99 · background #FFFFFF (dark #121A2B) · border 2.5px solid {강조색}
        box-shadow 0 2px 6px rgba(16,24,40,.2)
라벨 줄: display flex · align-items center · margin-top 4 (미래 5)
  <span style="flex: 1">           최솟값 11px #697182
  <span>                           현재 값 11.5px/600 · white-space nowrap
  <span style="flex: 1; text-align: right">  최댓값 11px #697182
```

강조색은 화면에 따라 다릅니다: 미래 `#0F7B47` · 코칭·상환 계획 `#7A3FE4` · 내 수치 입력 `#3556E6`.

**채움 `width`와 손잡이 `left`는 항상 같은 %입니다.** 하나만 고치면 손잡이가 채움 끝에서 떨어집니다.

**현재 값 라벨은 손잡이를 따라가지 않고 줄 한가운데에 고정합니다.**
양끝에 `flex: 1`을 주는 것이 그 방법입니다. `justify-content: space-between`을 쓰면
양끝 라벨 폭이 다를 때 가운데 라벨이 `(왼폭 − 오른폭) ÷ 2` 만큼 밀려납니다
(`0원` vs `45만원`이면 8px). 손잡이 위치로 옮기는 것도 안 됩니다 —
값이 양 끝으로 가면 최솟값·최댓값 라벨과 겹칩니다.

---

## 26. 값에 따라 움직이는 것 — 좌표를 고정하지 마세요

**아트보드는 "2026년 9월 8일, 순자산 9,350만원"이라는 하루치 스냅숏입니다.**
거기 적힌 `33%`, `x=93.6`, `left: 60%` 같은 값은 **그날 계산된 결과**이지 상수가 아닙니다.
그대로 박아 넣으면 날짜가 바뀌어도 그림이 그대로인 화면이 됩니다.

아래는 반드시 **계산해서** 넣어야 하는 자리 전부입니다.

| 어디 | 무엇이 움직이나 | 식 |
|---|---|---|
| 홈 항로 바 | 진행 채움 | `inset: 0 {100 − 소비율}% 0 0` |
| 홈 항로 바 | 목적지 깃발 · 목표 라벨 | `left: {소비 목표}%` (라벨은 `translateX(-50%)`) |
| 슬라이더 | 채움 폭 · 손잡이 | `(값 − 최소) ÷ (최대 − 최소) × 100`% — 둘 다 같은 값 |
| 목적지 링 | 진행 | `conic-gradient(색 0% {달성률}%, 트랙 {달성률}% 100%)` · 가운데 숫자도 같은 값 |
| 한도 진행바 | 채움 | `inset: 0 {100 − 사용액 ÷ 한도 × 100}% 0 0` (검산: 47/50 → `inset: 0 6% 0 0`) |
| 한도 초과 막대 | 초과분 빗금 · 한도 마커 | 아래 참조 |
| 자산·부채 구성 막대 | 조각 폭 | `각 항목 ÷ 합계 × 100`% (합이 100%가 되게) |
| 소비 추이 차트 | 오늘 선·점·후광·값 라벨·오늘 눈금 | `x(today) = 12 + (today − 1) ÷ (그달 일수 − 1) × 338` — **다섯 개가 전부 같은 x** |
| 소비 추이 차트 | 실선/점선 경계 | 실선 `x(1) → x(today)` · 점선 `x(today) → x(말일)` |
| 미래 차트 | 연도 x · 금액 y | `x = 10 + 년 ÷ 10 × 342` · `y = 103.9 − (원 ÷ 1억 − 1) × 28.1` |
| 부채 목록 | 금리 색 | 고금리만 `#C0342F`, 나머지 `#101828` — 기준은 원본 엔진을 따르세요 |

### 한도를 넘겼을 때

막대를 100% 이상으로 늘리지 않습니다. 트랙 전체가 **배분 합**이 되고, 한도까지가 파랑,
넘긴 만큼이 빨간 빗금입니다. 한도 지점에 세로 마커를 세웁니다. (`ModalErrors` 아트보드)

```
r = 한도 ÷ 배분 합 × 100                      // 216 ÷ 236 = 91.5%
파랑   position absolute · inset 0 {100−r}% 0 0 · border-radius 99px 0 0 99px · background #3556E6
빗금   position absolute · right 0 · top 0 · bottom 0 · width {100−r}% · border-radius 0 99px 99px 0
       background repeating-linear-gradient(135deg, #C0342F 0 4px, #E0908C 4px 8px)
마커   position absolute · left {r}% · top -5 · width 2 · height 20 · border-radius 2 · background #101828
```

아래 줄은 좌우 두 칸입니다 — 왼쪽 `배분 합 236만원`, 오른쪽 `총한도 216만원 · 20만원 초과`(11px/600 `#C0342F`).

### 날짜가 바뀌면 생기는 일

한 달의 일수는 28·29·30·31로 달라지고 오늘은 1일부터 말일까지 움직입니다.
아트보드 한 장으로는 안 보이는 경계들이 있습니다.

- **오늘 = 1일** — 오늘 라벨이 `1일` 눈금과 겹칩니다. 눈금을 지우고 오늘 라벨만 남기세요.
  실선 구간이 점 하나라 선이 그려지지 않습니다.
- **오늘 = 말일** — 오른쪽 끝. 점선 예상 구간이 없어집니다. `30일` 눈금과 겹치니 마찬가지로 정리하세요.
- **오늘 라벨이 다른 눈금과 12px 안** — 그 눈금을 지웁니다.
- **2월(28·29일)** — `D − 1`이 27·28이라 하루 간격이 넓어집니다. 상수 `9.86px/일`을 쓰면 틀립니다.
- **슬라이더 값이 최소·최대** — 손잡이가 트랙 끝을 넘지 않게 하세요. `margin-left: -10`이 있어
  0%에서 왼쪽으로 10px 삐져나옵니다.

---

---

## 27. v5 — 홈 달력과 하루 시트 (11종)

`plan/v5-calendar.md` §6 의 등록 표를 아트보드(`HomeCalendarStrip` · `HomeCalendar` · `DaySheet` · `DoneCard` · `ClassifySheet` ·
`HeroInsufficient` · `HeroFootnotes`)에서 잰 값으로 옮긴 것입니다. **새 hex 는 없습니다.** 달력 칸은 `brand-soft #E9EDFD` ·
`ink-2 #475467` · `ink-3 #626D88` · `disabled #B4BECD` 만 조합하고, 달력 · 하루 시트 · 완료 카드에는 의미색(주황 · 빨강 · 가정 보라)을 쓰지 않습니다.

### 27-1. CalendarCell

```
스트립 칸: width 44 · height 56 · border-radius 10 · display flex · column · align/justify center · gap 3 · flex-shrink 0
           요일 10px/500 line-height 1 #626D88 · 날짜 11px/500 line-height 1 #475467 (오늘 600 #101828)
           합계 11px/600 line-height 13px tabular-nums #101828
           수식어 줄 height 12 · inline-flex · gap 3 — 비어 있어도 자리를 둔다(모든 칸의 날짜 줄이 같은 높이)
월 달력 칸: min-width 0 · height 56(큰 글자 72) · border-radius 10 · gap 2
           폭 = 카드 안쪽 ÷ 7 (390 = 47.7 · 360 = 44.6 · 320 = 39.4)
           날짜 12px/500 line-height 1.2 (오늘 700) · 합계 11px/600 line-height 1.2 nowrap
           큰 글자: 날짜 14.5 · 합계 13(칸 폭 47 미만은 12)
```

| 상태 | 표시 |
|---|---|
| 합계 | `4,500` · `1.2만` — `#101828` |
| 미입력 | `—` `#626D88`(ink-3). 회색이지만 누를 수 있음 |
| 안 썼어요 | `0` `#475467`(ink-2). ✓ 를 붙이지 않음 |
| 다 적었어요 | 합계 + ✓ 11×11 stroke `#475467` stroke-width 2.8 |
| 이체 | 수식어 줄에 글자 `이체` 10px/500 `#475467`. 카테고리색 점을 쓰지 않음 |
| 오늘 | background `#E9EDFD` |
| 누름 | box-shadow inset 0 0 0 2px `#3556E6` |
| 미래 | 날짜 `#697182`, 숫자 자리 빈 칸(height 13) · 누를 수 없음 |
| 시작일 이전 | 미래 칸과 같은 모양(날짜 `#697182` · `—` 없이 합계 · 수식어 자리를 비움)이되 **누르면 그 날짜 시트가 열림** — `CalendarCells` 9번 · `HeroInsufficient` |
| 이웃 달 | 지난달 · 이번 달 이웃 칸 opacity .7(합계만) · 범위 밖 opacity .45(숫자만 · 버튼 아님) |
| 포커스 | focus ring 3px (`accessibility.focusVisible`) |

칸 숫자 형식은 `tokens.v3.json` `typography.rules.calendarCellSum` — `4,500` · `1.2만` · `12.5만` · `120만` · `1,200만` · `1.2억`. 소수 첫 자리가 0이면 뗍니다(`3만` · `30만`) — `3.0만` · `100.0만`은 없습니다. 내역 날짜 머리글(`이체 30만`)도 같은 함수입니다.

### 27-2. RecentStrip · MonthCalendar · DayList

```
카드:     Card(18) · padding 13px 14px 13px
접힘 머리: 제목 "이번 달 달력" 14px/600 · 오른쪽 토글 "펼치기 ▾" 12px/600 #475467 + 셰브론 14×14
스트립:   display flex · justify-content space-between · margin-top 8 · 7칸(간격 0 · 오늘이 오른쪽 끝)
          지난달 날짜는 "8/31" 처럼 씀
펼침 머리: min-height 32 · ‹ › 버튼 32×32 radius 10 border 1px #E3E8F1 (갈 수 없으면 아이콘 opacity .5)
          달 이름 "2026년 9월" min-width 94 · 15px/700 -0.015em nowrap · 오른쪽 "접기 ▴" 12px/600
요일 줄:   grid repeat(7, minmax(0, 1fr)) · margin-top 8 · padding-bottom 5 · 11px/500 #626D88 (약 21)
월 그리드: 주마다 grid repeat(7, minmax(0, 1fr)) · border-top 1px solid #EFF2F8 · padding 2px 0 · 맨 아래 border-bottom 같은 선
```

MonthCalendar 는 **모든 폭 · 글자 크기의 펼침 기본**입니다. DayList(날짜 목록 · 원 단위 그대로)는 큰 글자에서 `목록으로 보기 ›`를 고른 때만(`CalendarGridSizes`).

### 27-3. StatusLine

`font-size 11 · line-height 1.5 · #475467 · margin-top 8` — 항상 한 문장, 평가어 없음. 접힘 `오늘 4건 37,000원`, 펼침 `9월 기록한 소비 124,000원 · 오늘 4건 37,000원`.

### 27-4. ReviewRow (DataRow §10 변형)

`display flex · space-between · height 32 (= 24 + 간격 8) · margin-top 2 · border-top 1px solid #EFF2F8` · 라벨 `확인할 내용 2개` 12.5px/600 `#101828` · 셰브론 15×15 stroke `#697182`. 주황을 쓰지 않습니다. 누르는 영역은 44.

### 27-5. DaySheet

§18 의 「하루 시트 변형」. radius 26 · 헤더 44 · 저장 버튼 52 · 키보드가 열린 상태가 기본 아트보드입니다.

### 27-6. ColorChipRow

```
줄: display flex · gap 6 · overflow hidden — 자주 쓴 3개 + "전체 ›" 12.5px/600 #3556E6 (펼치면 가로 스크롤 13개)
칩: height 32 · padding 0 11px 0 9px · border-radius 8 · background #FFFFFF · border 1px solid #D7DEEA
    색 점 8×8 radius 99 (dataPalette) + 이름 12.5px/500 #101828 · gap 6 · nowrap
선택(분류하기의 추천 칩): height 30 · background #E9EDFD · border 1.5px solid #3556E6 · 12px/600
```

색만으로 뜻을 전하지 않습니다(점 + 이름). `저축/투자` · `대출상환`은 칩 줄에 없고 `저장`(목록 우선 시트는 `추가`) 바로 아래의 링크 `저축·투자로 기록 ›` · `대출상환으로 기록 ›`입니다. 링크 아래에 11.5px `#626D88` 한 줄 `저축·투자와 대출상환은 거래 추가에서 남겨요 · 소비율에는 안 들어가요`가 붙고, 시트 맨 아래는 확인 버튼(`9월 8일 다 적었어요` · `오늘은 안 썼어요` — 흰 바탕 + 1px `#D7DEEA` 테두리 · 높이 44) 자리입니다.

### 27-7. RecentEntryChip

`height 32 · padding 0 11px · border-radius 8 · background #F4F6FB · 12px/500 #101828 · gap 7 · nowrap` — 메모(8자 + …) + 금액 600 + 분류(색 점 7×7 + 카테고리 이름 11px/500 `#475467` · gap 4), 분류가 없으면 점 없이 `분류 안 함` 11px/500 `#626D88`. 색만으로 분류를 전하지 않습니다 — 점 뒤에 이름이 꼭 붙습니다(`DaySheet` 기준 · 2026-09-21 · `Components` 08절의 조각도 같은 모습 — `_tools/refresh_components_v5.py`로 다시 잘라 옵니다).

### 27-8. DoneCard (Toast §19 변형)

```
background #101828 · border-radius 16 · padding 13px 14px 12px · box-shadow 0 8px 24px rgba(0,0,0,.28)
위치: left 14 · right 14 · bottom 78 (하단 탭 위) — dc-keep, 라이트 · 다크 동일
제목 14px/700 #FFFFFF + 체크 15×15 stroke #3DD489 · 오른쪽 "닫기" 12px/600 rgba(255,255,255,.72)
둘째 줄 13.5px/500 margin-top 7 · 셋째 줄(조건부 · 계획 §4-4 우선순위로 하나만 — 시안은 분류 안 함 저장의 4순위 문장, 소비율 줄은 6순위) 12.5px rgba(255,255,255,.72) margin-top 3
버튼 줄 margin-top 11 · gap 8 · height 36 · radius 10
  주 행동 "한 건 더" padding 0 14 · border 1px rgba(255,255,255,.55) · 13px/700
  "방금 기록한 12,000원 취소" padding 0 12 · border 1px rgba(255,255,255,.28) · 13px/600
```

### 27-9. ClassifyGroupRow (DataRow §10 변형)

```
묶음 행: height 52 · gap 10 · border-bottom 1px solid #F3F5FA
         제목 14px/600 + "×3" 500 #626D88 · 둘째 줄 12px #475467 · 오른쪽 추천 칩(27-6 선택형) · 셰브론 16×16 #697182
건별 행: 묶음 아래 background #F4F6FB · radius 0 0 12px 12px · padding 0 10px 2px
         height 40 · padding-left 8 · 체크 22×22 radius 7 (#3556E6 / 빈 칸 border 1.5px #CFD7E6)
         날짜 13px #475467 · 금액 13px/600 · 제외한 건은 금액 #B4BECD + "· 제외"
푸터:    "2건 저장" height 52 radius 14 · 아래 11.5px #626D88 "나머지 5건은 분류 안 함으로 남아요"
```

계획 표의 높이 46 과 달리 아트보드 실측은 52 입니다 — 아트보드가 기준입니다.

### 27-10. HeroInsufficient (HomeHero 상태)

자리 · 모양은 HeroCard §4 그대로이고 내용만 바뀝니다.

| 자리 | 값 |
|---|---|
| eyebrow | `이번 달 기록한 소비` · 오른쪽 배지 없음(`순항 중` 없음) |
| display | `5,000` 54px/700 + `원` 25px/600 `#475467` · 소비 0건이면 `아직 기록이 없어요` |
| 보조(오른쪽) | `월급의` 11px/500 `#626D88` + `0.1%` 14px/600 — 월급이 없으면 없음(`총수입의 N%`로 바꾸지 않음) |
| 각주 | `아직 기록하지 않은 소비는 포함되지 않았어요` 13px/500 `#475467` · 둘째 줄 12px line-height 1.45 `#626D88` — 3종 |
| RouteBar | 트랙 + 목표 눈금만. 채움 · 현재 위치 없음 |
| StatTriple | 월 실수령 값 · `월말 예상 —` · `월말 예상 여유 —`(`#697182`) |
| 버튼 | `소비 기록하기`(월급 미입력이면 `월급 입력하고 시작` → 월급 입력으로) |

둘째 줄 3종: `7월 기록도 확인하면 예상을 볼 수 있어요 · 확인하기 ›` · `예상에 쓸 이전 기록을 확인해 주세요 · 확인할 달 보기 ›` · `예상에 사용할 지난 소비 기록이 아직 없어요`(링크 없음). 상태 카탈로그 `EmptyStates` F.

### 27-11. HomeHero 조건부 각주

기준 줄(`실수령 급여 기준 · …` + `기준 조정 ›`)과 버튼 사이에 `font-size 11 · line-height 1.4 · #626D88 · margin-top 4`로 한 줄씩 붙습니다.
기존 요소의 치수는 그대로이고 카드 높이만 줄 수만큼 늡니다. 문구 4종과 조합은 `HeroFootnotes`.

---

## 실제로 쓰이는 값 목록 — 자가 점검용

아트보드에서 기계로 뽑은 실측 목록입니다. **여기에 없는 값을 새로 만들면 시안과 다른 화면입니다.**
만든 화면의 `font-size` · `border-radius`를 전부 모아 이 목록과 대조하세요.

### font-size

| 화면군 | 쓰이는 크기 |
|---|---|
| 모바일 화면·모달 (28장) | `10 · 10.5 · 11 · 11.5 · 12 · 12.5 · 13 · 13.5 · 14 · 14.5 · 15 · 16 · 17 · 18 · 19 · 21 · 22 · 25 · 26 · 27 · 30 · 33 · 34 · 54` |
| 상태 카탈로그 (6장) | 위와 같고 `15.5 · 20 · 48` 추가 |
| v5 달력 · 하루 시트 | 모바일과 같고 `20` 추가(하루 시트 금액 칸의 값) |
| 데스크톱 (2장) | `10.5`~`17` 동일 + `20 · 21 · 22 · 26 · 28 · 34 · 62` |
| 토큰·컴포넌트 시트 (2장) | 참조용 시트라 구현 대상이 아닙니다 |

25px 이상은 히어로의 display 숫자와 그 단위(%·만원)뿐입니다. **화면당 한 곳에만** 나옵니다.

굵기는 `400 · 500 · 600 · 700`만 씁니다. 300은 폰트에는 있지만 화면에서 쓰지 않습니다.

`letter-spacing`은 큰 글자에만 겁니다: 54px `-0.045em` · 21px `-0.03em` ·
18~20px `-0.025em` · 14~17px `-0.02em` · 15px 제목 `-0.015em`.
11~13px에는 걸지 않습니다(워드마크 `0.06em`, SectionLabel `0.06~0.07em` 제외).

### border-radius

| 값 | 쓰는 곳 |
|---|---|
| `99` | 필 · 진행 트랙 · 원형 |
| `26` | BottomSheet 상단 |
| `20` | HeroCard · Card(20) |
| `18` | Card(18) |
| `16` `14` | 큰 아이콘 타일 · 이미지 자리 |
| `13` | 버튼 |
| `12` | Callout · 탭 바깥틀 · 아이콘 타일 |
| `11` | 입력 · 헤더 아이콘 버튼 · 카드 안 아이콘 타일 |
| `10` `9` `8` | 작은 칩 · 앱마크 · 탭 안쪽 |
| `7` `6` `5` `3` `2` | 그래프 조각 · 마커 · 막대 끝 |

모바일 화면에서 실제로 나오는 값은 `2 · 3 · 5 · 6 · 7 · 8 · 9 · 10 · 11 · 12 · 13 · 14 · 16 · 18 · 20 · 26 · 99` 뿐입니다.
