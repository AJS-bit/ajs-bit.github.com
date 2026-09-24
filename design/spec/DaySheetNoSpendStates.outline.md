# DaySheetNoSpendStates — 블록 개요

원본 `canvas/DaySheetNoSpendStates.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div`
  `width:1200px height:1190px background:#EDF0F7 color:#101828 padding:28px 30px 30px display:flex flex-direction:column gap:10px`
  - `span` **text 11px/600** — “구현 참고 · 앱 화면이 아닙니다”
    `font-size:11px font-weight:600 letter-spacing:0.02em color:#475467 border:1px solid #E3E8F1 background:#FFFFFF border-radius:99px padding:4px 10px`
  - `h2` **text 20px/700** — “안 쓴 날을 표시하는 경우”
    `font-size:20px font-weight:700 letter-spacing:-0.025em color:#101828`
  - `p` **text 13px/400** — “소비가 한 건도 없는 날에만 기록 창 맨 아래에 오늘은 안 썼어요가 보입니다. 누르면 달력의 오늘 칸이 파란 +에서”
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
          `padding:12px 18px 6px display:flex flex-direction:column gap:10px`
      - `p` — “그림은 입니다. 바뀌는 자리는 둘째 줄 · 목록 · 맨 아래 버튼 세 곳입니다.”
        `font-size:12px line-height:1.5 color:#626D88`
        - `b` — “소비는 없고 적금 이체만 있는 오늘”
          `font-weight:600 color:#475467`
    - `div`
      `flex:1 display:grid grid-template-columns:repeat(2, 362px) gap:24px 20px align-items:start`
      - `div`
        `display:flex flex-direction:column gap:8px`
        - `div`
        - `div`
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:26px 26px 18px 18px display:flex flex-direction:column`
      - `div`
        `display:flex flex-direction:column gap:8px`
        - `div`
        - `div`
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:26px 26px 18px 18px display:flex flex-direction:column`
      - `div`
        `display:flex flex-direction:column gap:8px`
        - `div`
        - `div`
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:26px 26px 18px 18px display:flex flex-direction:column`
      - `div`
        `display:flex flex-direction:column gap:8px`
        - `div`
        - `div`
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:26px 26px 18px 18px display:flex flex-direction:column`
  - `div` **Card(18)**
    `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:10px 18px 8px`
    - `div` **text 12px/700** — “구현 메모”
      `font-size:12px font-weight:700 color:#101828 padding:2px 0 4px`
    - `div`
      `display:flex gap:10px padding:7px 0 border-bottom:1px solid #F3F5FA`
      - `span` **text 10.5px/700** — “1”
        `margin-top:1px width:17px height:17px border-radius:99px background:#101828 color:#FFFFFF font-size:10.5px font-weight:700 display:inline-flex align-items:center justify-content:center box-shadow:0 0 0 2px #FFFFFF`
      - `div` **text 12px/400** — “둘째 줄은 그날 소비 합계 자리입니다. 소비가 0건이면 합계 대신 이 문장이 오고, 이체가 있으면 이체 금액을 (소”
        `font-size:12px line-height:1.55 color:#475467`
    - `div`
      `display:flex gap:10px padding:7px 0 border-bottom:1px solid #F3F5FA`
      - `span` **text 10.5px/700** — “2”
        `margin-top:1px width:17px height:17px border-radius:99px background:#101828 color:#FFFFFF font-size:10.5px font-weight:700 display:inline-flex align-items:center justify-content:center box-shadow:0 0 0 2px #FFFFFF`
      - `div` **text 12px/400** — “이체 · 상환 행은 소비율 제외 배지와 회색 금액으로 그립니다. 칸 숫자에도 소비 합계에도 들어가지 않습니다.”
        `font-size:12px line-height:1.55 color:#475467`
    - `div`
      `display:flex gap:10px padding:7px 0`
      - `span` **text 10.5px/700** — “3”
        `margin-top:1px width:17px height:17px border-radius:99px background:#101828 color:#FFFFFF font-size:10.5px font-weight:700 display:inline-flex align-items:center justify-content:center box-shadow:0 0 0 2px #FFFFFF`
      - `div` **text 12px/400** — “오늘은 안 썼어요는 그 날짜 소비 거래가 0건일 때만 보입니다. 0원 거래를 만들지 않고 그 날짜에 표시만 남깁니다”
        `font-size:12px line-height:1.55 color:#475467`
