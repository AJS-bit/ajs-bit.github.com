# CalendarStatusLines — 블록 개요

원본 `canvas/CalendarStatusLines.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div`
  `width:1200px height:1050px background:#EDF0F7 color:#101828 padding:28px 30px 30px display:flex flex-direction:column gap:10px`
  - `span` **text 11px/600** — “구현 참고 · 앱 화면이 아닙니다”
    `font-size:11px font-weight:600 letter-spacing:0.02em color:#475467 border:1px solid #E3E8F1 background:#FFFFFF border-radius:99px padding:4px 10px`
  - `h2` **text 20px/700** — “달력 아래 한 줄이 바뀌는 경우”
    `font-size:20px font-weight:700 letter-spacing:-0.025em color:#101828`
  - `p` **text 13px/400** — “접어 둔 달력의 날짜 칸 아래에는 오늘 합계를 말하는 한 문장이 있습니다. 아래 경우에는 그 문장이 바뀝니다.”
    `font-size:13px line-height:1.55 color:#626D88`
  - `div`
    `display:flex gap:32px align-items:flex-start`
    - `div`
      `width:362px display:flex flex-direction:column gap:8px`
      - `div` **Card(18)**
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 14px 13px`
        - `div`
          `display:flex align-items:center justify-content:space-between gap:8px`
        - `div`
          `display:flex justify-content:space-between margin-top:8px`
        - `div`
          `position:relative`
        - `div`
          `display:flex align-items:center justify-content:space-between height:32px margin-top:2px border-top:1px solid #EFF2F8`
      - `p` — “상태 줄은 입니다. 그림은 평소(오늘 기록이 있고 저녁 6시 전)입니다.”
        `font-size:12px line-height:1.5 color:#626D88`
        - `b` — “날짜 칸 아래 한 줄”
          `font-weight:600 color:#475467`
      - `div` **Card(18)**
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:10px 18px 8px`
        - `div` **text 12px/700** — “구현 메모”
          `font-size:12px font-weight:700 color:#101828 padding:2px 0 4px`
        - `div`
          `display:flex gap:10px padding:7px 0 border-bottom:1px solid #F3F5FA`
        - `div`
          `display:flex gap:10px padding:7px 0 border-bottom:1px solid #F3F5FA`
        - `div`
          `display:flex gap:10px padding:7px 0`
    - `div`
      `flex:1 display:grid grid-template-columns:repeat(2, 362px) gap:24px 20px align-items:start`
      - `div`
        `display:flex flex-direction:column gap:8px`
        - `div`
        - `div` **Card(18)**
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 14px 13px`
      - `div`
        `display:flex flex-direction:column gap:8px`
        - `div`
        - `div` **Card(18)**
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 14px 13px`
      - `div`
        `display:flex flex-direction:column gap:8px`
        - `div`
        - `div` **Card(18)**
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 14px 13px`
      - `div`
        `display:flex flex-direction:column gap:8px`
        - `div`
        - `div` **Card(18)**
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 14px 13px`
      - `div`
        `display:flex flex-direction:column gap:8px`
        - `div`
        - `div` **Card(18)**
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 14px 13px`
      - `div`
        `display:flex flex-direction:column gap:8px`
        - `div`
        - `div` **Card(18)**
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 14px 13px`
