# CalendarGridSizes — 블록 개요

원본 `canvas/CalendarGridSizes.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div`
  `width:1150px height:1490px background:#EDF0F7 color:#101828 padding:28px 30px 30px display:flex flex-direction:column gap:10px`
  - `span` **text 11px/600** — “구현 참고 · 앱 화면이 아닙니다”
    `font-size:11px font-weight:600 letter-spacing:0.02em color:#475467 border:1px solid #E3E8F1 background:#FFFFFF border-radius:99px padding:4px 10px`
  - `h2` **text 20px/700** — “달력을 펼치면 어디서나 월 달력”
    `font-size:20px font-weight:700 letter-spacing:-0.025em color:#101828`
  - `p` **text 13px/400** — “화면이 좁아도, 글자를 크게 써도 날짜를 세로로 늘어놓은 목록으로 바뀌지 않습니다. 접어 둔 최근 7일 줄도 칸 그”
    `font-size:13px line-height:1.55 color:#626D88`
  - `div`
    `display:flex gap:36px align-items:flex-start`
    - `div`
      `width:292px display:flex flex-direction:column gap:8px`
      - `div`
        - `div` **text 14px/700** — “가장 좁은 폰”
          `font-size:14px font-weight:700 letter-spacing:-0.01em color:#101828`
        - `div` **text 12px/400** — “달력 그대로. 제목은 9월만 적어요”
          `font-size:12px line-height:1.5 color:#626D88 margin-top:2px`
      - `div` **Card(18)**
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 8px 13px`
        - `div`
          `display:flex align-items:center justify-content:space-between gap:6px min-height:32px`
        - `div`
          `display:grid grid-template-columns:repeat(7, minmax(0, 1fr)) margin-top:8px`
        - `div`
          `display:flex flex-direction:column border-bottom:1px solid #EFF2F8`
        - `div` **text 11px/400** — “9월 기록한 소비 124,000원 · 오늘 4건 37,000원”
          `font-size:11px line-height:1.5 color:#475467 margin-top:8px`
        - `div`
          `display:flex align-items:center justify-content:space-between height:32px margin-top:2px border-top:1px solid #EFF2F8`
    - `div`
      `width:362px display:flex flex-direction:column gap:8px`
      - `div`
        - `div` **text 14px/700** — “글자를 크게 쓰는 사람”
          `font-size:14px font-weight:700 letter-spacing:-0.01em color:#101828`
        - `div` **text 12px/400** — “달력 그대로. 칸이 높아지고 글자가 커져요”
          `font-size:12px line-height:1.5 color:#626D88 margin-top:2px`
      - `div` **Card(18)**
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 14px 4px`
        - `div`
          `display:flex align-items:center justify-content:space-between gap:6px min-height:40px`
        - `div`
          `display:grid grid-template-columns:repeat(7, minmax(0, 1fr)) margin-top:10px`
        - `div`
          `display:flex flex-direction:column border-bottom:1px solid #EFF2F8`
        - `div` **text 14.5px/400** — “9월 기록한 소비 124,000원 · 오늘 4건 37,000원”
          `font-size:14.5px line-height:1.5 color:#475467 margin-top:8px`
        - `div`
          `display:flex align-items:center justify-content:space-between height:44px margin-top:2px border-top:1px solid #EFF2F8`
        - `div`
          `display:flex align-items:center justify-content:space-between height:44px margin-top:2px border-top:1px solid #EFF2F8`
    - `div`
      `width:362px display:flex flex-direction:column gap:8px`
      - `div`
        - `div` **text 14px/700** — “목록으로 보기를 고르면”
          `font-size:14px font-weight:700 letter-spacing:-0.01em color:#101828`
        - `div` **text 12px/400** — “스스로 고른 사람에게만. 저절로 바뀌지 않아요”
          `font-size:12px line-height:1.5 color:#626D88 margin-top:2px`
      - `div` **Card(18)**
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 14px 4px`
        - `div`
          `display:flex align-items:center justify-content:space-between gap:6px min-height:40px`
        - `div`
          `margin-top:8px`
        - `div`
          `display:flex align-items:center justify-content:space-between height:44px margin-top:2px border-top:1px solid #EFF2F8`
  - `div`
    `display:flex gap:36px align-items:flex-start margin-top:26px`
    - `div`
      `width:292px display:flex flex-direction:column gap:24px`
      - `div`
        `width:292px display:flex flex-direction:column gap:8px`
        - `div`
        - `div` **Card(18)**
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 8px 13px`
      - `div`
        `width:292px display:flex flex-direction:column gap:8px`
        - `div`
        - `div` **Card(18)**
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 8px 13px`
    - `div`
      `width:292px display:flex flex-direction:column gap:8px`
      - `div`
        - `div` **text 14px/700** — “좁은 폰 + 큰 글자”
          `font-size:14px font-weight:700 letter-spacing:-0.01em color:#101828`
        - `div` **text 12px/400** — “금액 글자를 조금 줄여 71.2만도 잘리지 않아요”
          `font-size:12px line-height:1.5 color:#626D88 margin-top:2px`
      - `div` **Card(18)**
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 8px 13px`
        - `div`
          `display:flex align-items:center justify-content:space-between gap:6px min-height:40px`
        - `div`
          `display:flex justify-content:flex-end margin-top:6px`
        - `div`
          `display:grid grid-template-columns:repeat(7, minmax(0, 1fr)) margin-top:10px`
        - `div`
          `display:flex flex-direction:column border-bottom:1px solid #EFF2F8`
    - `div`
      `width:362px display:flex flex-direction:column gap:8px`
      - `div`
        - `div` **text 14px/700** — “글자를 크게 쓰는 사람 · 접어 둔 달력”
          `font-size:14px font-weight:700 letter-spacing:-0.01em color:#101828`
        - `div` **text 12px/400** — “칸이 높아지고 글자가 커져요. 금액은 숨기지 않아요”
          `font-size:12px line-height:1.5 color:#626D88 margin-top:2px`
      - `div` **Card(18)**
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 14px 13px`
        - `div`
          `display:flex align-items:center justify-content:space-between gap:8px`
        - `div`
          `display:flex justify-content:space-between margin-top:8px`
        - `div` **text 14.5px/400** — “오늘 4건 37,000원”
          `font-size:14.5px line-height:1.5 color:#475467 margin-top:8px`
        - `div`
          `display:flex align-items:center justify-content:space-between height:44px margin-top:2px border-top:1px solid #EFF2F8`
  - `div`
    `margin-top:24px display:flex flex-direction:column gap:4px`
    - `div` **text 12px/600** — “구현 메모”
      `font-size:12px font-weight:600 color:#475467`
    - `p` **text 12px/400** — “가장 좁은 폰은 화면 너비 320px, 달력 칸은 39 × 56입니다. 큰 글자에서는 칸 높이가 72가 됩니다. 좁”
      `font-size:12px line-height:1.6 color:#626D88`
