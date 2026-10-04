# HomeGlanceRows — 블록 개요

원본 `canvas/HomeGlanceRows.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div`
  `width:1230px height:1045px background:#EDF0F7 color:#101828 padding:28px 30px 30px display:flex flex-direction:column gap:10px`
  - `span` **text 11px/600** — “구현 참고 · 앱 화면이 아닙니다”
    `font-size:11px font-weight:600 letter-spacing:0.02em color:#475467 border:1px solid #E3E8F1 background:#FFFFFF border-radius:99px padding:4px 10px`
  - `h2` **text 20px/700** — “홈 · 자산 한눈에 — 줄을 펼쳤을 때”
    `font-size:20px font-weight:700 letter-spacing:-0.025em color:#101828`
  - `p` — “홈 구성에서 켠 사람의 카드입니다. 줄을 누르면 그 아래에 풀이가 열립니다.”
    `font-size:13px line-height:1.55 color:#626D88`
    - `span` — “「자산 한눈에」를”
      `white-space:nowrap`
  - `div`
    `display:flex gap:20px align-items:flex-start`
    - `div`
      `width:270px display:flex flex-direction:column gap:22px`
      - `div`
        `display:flex flex-direction:column gap:8px`
        - `div`
        - `div` **Card(18)**
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:10px 14px 4px`
    - `div`
      `width:270px display:flex flex-direction:column gap:22px`
      - `div`
        `display:flex flex-direction:column gap:8px`
        - `div`
        - `div` **Card(18)**
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:10px 14px 4px`
    - `div`
      `width:270px display:flex flex-direction:column gap:22px`
      - `div`
        `display:flex flex-direction:column gap:8px`
        - `div`
        - `div` **Card(18)**
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:10px 14px 4px`
    - `div`
      `width:270px display:flex flex-direction:column gap:22px`
      - `div`
        `display:flex flex-direction:column gap:8px`
        - `div`
        - `div` **Card(18)**
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:10px 14px 4px`
      - `div`
        `display:flex flex-direction:column gap:8px`
        - `div`
        - `div` **Card(18)**
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:6px 14px`
  - `div` **Card(18)**
    `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:10px 18px 8px`
    - `div` **text 12px/700** — “구현 메모”
      `font-size:12px font-weight:700 color:#101828 padding:2px 0 4px`
    - `div`
      `display:flex gap:10px padding:7px 0 border-bottom:1px solid #F3F5FA`
      - `span` **text 10.5px/700** — “1”
        `margin-top:1px width:17px height:17px border-radius:99px background:#101828 color:#FFFFFF font-size:10.5px font-weight:700 display:inline-flex align-items:center justify-content:center box-shadow:0 0 0 2px #FFFFFF`
      - `div` — “한 번에 한 줄만 펼칩니다. 펼친 칸은 그 줄 바로 아래. 금액 쓰는 법은 미래 탭과 같은 ‘ ’ + 100만원 단”
        `font-size:12px line-height:1.55 color:#475467`
        - `b` — “약”
          `font-weight:600 color:#101828`
    - `div`
      `display:flex gap:10px padding:7px 0`
      - `span` **text 10.5px/700** — “2”
        `margin-top:1px width:17px height:17px border-radius:99px background:#101828 color:#FFFFFF font-size:10.5px font-weight:700 display:inline-flex align-items:center justify-content:center box-shadow:0 0 0 2px #FFFFFF`
      - `div` — “자산 종합 점수 = 순자산 대비 소비 40 + 매달 모을 수 있는 돈 30 + 부채 건전성 15 + 비상금 15(시”
        `font-size:12px line-height:1.55 color:#475467`
        - `b` — “지난달을 마감한 뒤 점수를 보여 드려요.”
          `font-weight:600 color:#101828`
