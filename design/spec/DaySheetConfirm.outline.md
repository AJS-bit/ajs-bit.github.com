# DaySheetConfirm — 블록 개요

원본 `canvas/DaySheetConfirm.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div`
  `width:1200px height:900px background:#EDF0F7 color:#101828 padding:28px 30px 30px display:flex flex-direction:column gap:10px`
  - `span` **text 11px/600** — “구현 참고 · 앱 화면이 아닙니다”
    `font-size:11px font-weight:600 letter-spacing:0.02em color:#475467 border:1px solid #E3E8F1 background:#FFFFFF border-radius:99px padding:4px 10px`
  - `h2` **text 20px/700** — “저장을 눌렀는데 한 번 더 물어보는 경우”
    `font-size:20px font-weight:700 letter-spacing:-0.025em color:#101828`
  - `p` **text 13px/400** — “아래 네 경우에는 바로 저장하지 않고 금액 칸 아래에 안내가 한 줄 뜹니다. 저장을 한 번 더 누르면 그대로 저장됩”
    `font-size:13px line-height:1.55 color:#626D88`
  - `div`
    `display:flex gap:32px align-items:flex-start`
    - `div`
      `width:362px display:flex flex-direction:column gap:8px`
      - `div`
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:26px 26px 18px 18px display:flex flex-direction:column`
        - `div`
          `display:flex justify-content:center padding:9px 0 0`
        - `div`
          `display:flex align-items:flex-start justify-content:space-between gap:10px padding:12px 18px 12px border-bottom:1px solid #EFF2F8`
        - `div`
          `padding:12px 18px 18px display:flex flex-direction:column gap:10px`
      - `p` — “네 안내 모두 이 자리에 뜹니다. 그림은 1번의 경우입니다.”
        `font-size:12px line-height:1.5 color:#626D88`
        - `b` — “금액 칸 바로 아래”
          `font-weight:600 color:#475467`
    - `div`
      `flex:1 display:grid grid-template-columns:repeat(2, 362px) gap:24px 20px align-items:start`
      - `div`
        `display:flex flex-direction:column gap:8px`
        - `div`
        - `div` **Card(18)**
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px display:flex flex-direction:column gap:10px`
      - `div`
        `display:flex flex-direction:column gap:8px`
        - `div`
        - `div` **Card(18)**
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px display:flex flex-direction:column gap:10px`
      - `div`
        `display:flex flex-direction:column gap:8px`
        - `div`
        - `div` **Card(18)**
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px display:flex flex-direction:column gap:10px`
      - `div`
        `display:flex flex-direction:column gap:8px`
        - `div`
        - `div` **Card(18)**
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px display:flex flex-direction:column gap:10px`
  - `div` **Card(18)**
    `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:10px 18px 8px`
    - `div` **text 12px/700** — “구현 메모”
      `font-size:12px font-weight:700 color:#101828 padding:2px 0 4px`
    - `div`
      `display:flex gap:10px padding:7px 0 border-bottom:1px solid #F3F5FA`
      - `span` **text 10.5px/700** — “1”
        `margin-top:1px width:17px height:17px border-radius:99px background:#101828 color:#FFFFFF font-size:10.5px font-weight:700 display:inline-flex align-items:center justify-content:center box-shadow:0 0 0 2px #FFFFFF`
      - `div` **text 12px/400** — “적은 금액이 월급(실수령)의 10% 이상일 때 뜹니다. 그림은 월급 360만원이라 36만원부터입니다. 그대로 저장해”
        `font-size:12px line-height:1.55 color:#475467`
    - `div`
      `display:flex gap:10px padding:7px 0 border-bottom:1px solid #F3F5FA`
      - `span` **text 10.5px/700** — “2”
        `margin-top:1px width:17px height:17px border-radius:99px background:#101828 color:#FFFFFF font-size:10.5px font-weight:700 display:inline-flex align-items:center justify-content:center box-shadow:0 0 0 2px #FFFFFF`
      - `div` **text 12px/400** — “켜져 있는 반복 지출과 금액 차이가 5% 안이거나 메모가 같고, 아직 결제일 전일 때 뜹니다.”
        `font-size:12px line-height:1.55 color:#475467`
    - `div`
      `display:flex gap:10px padding:7px 0 border-bottom:1px solid #F3F5FA`
      - `span` **text 10.5px/700** — “3”
        `margin-top:1px width:17px height:17px border-radius:99px background:#101828 color:#FFFFFF font-size:10.5px font-weight:700 display:inline-flex align-items:center justify-content:center box-shadow:0 0 0 2px #FFFFFF`
      - `div` **text 12px/400** — “같은 날 자동으로 기록된 반복 지출이 이미 있을 때 뜹니다. 금액이 비슷하다는 이유만으로 지우거나 자동 기록을 건너”
        `font-size:12px line-height:1.55 color:#475467`
    - `div`
      `display:flex gap:10px padding:7px 0`
      - `span` **text 10.5px/700** — “4”
        `margin-top:1px width:17px height:17px border-radius:99px background:#101828 color:#FFFFFF font-size:10.5px font-weight:700 display:inline-flex align-items:center justify-content:center box-shadow:0 0 0 2px #FFFFFF`
      - `div` **text 12px/400** — “안내는 금액 칸 아래에 그대로 남습니다. 저장 완료 카드는 뜨지 않습니다.”
        `font-size:12px line-height:1.55 color:#475467`
