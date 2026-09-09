# CoachEmpty — 블록 개요

원본 `canvas/CoachEmpty.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div` **화면프레임**
  `width:390px height:844px background:#2A3245 color:#101828 display:flex flex-direction:column`
  - `div`
    `height:60px display:flex align-items:flex-end justify-content:center`
    - `span` **text 11.5px/500** — “배경을 눌러 닫기”
      `font-size:11.5px font-weight:500 color:rgba(255,255,255,.62)`
  - `div` **BottomSheet**
    `flex:1 min-height:0 background:#FFFFFF border-radius:26px 26px 0 0 display:flex flex-direction:column color:#101828`
    - `div`
      `display:flex justify-content:center padding:9px 0 0`
      - `span` **GrabHandle**
        `width:38px height:4px border-radius:99px background:#D7DEEA`
    - `div`
      `display:flex align-items:flex-start justify-content:space-between gap:10px padding:12px 18px 14px border-bottom:1px solid #EFF2F8`
      - `div`
        - `h2` **text 18px/700** — “코칭”
          `font-size:18px font-weight:700 letter-spacing:-0.025em color:#101828`
        - `p` **text 12.5px/400** — “기록이 쌓이면 무엇부터 손댈지 순서대로 알려 드려요.”
          `font-size:12.5px line-height:1.45 color:#626D88`
      - `div`
        `width:36px height:36px border-radius:11px background:#F4F6FB display:flex align-items:center justify-content:center`
    - `div`
      `flex:1 min-height:0 padding:14px 18px 0 display:flex flex-direction:column gap:15px`
      - `div` **Card(18)**
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px 15px`
        - `div`
          `display:flex align-items:center gap:13px`
      - `div` **Card(18)**
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px 15px`
        - `div` **text 12.5px/600** — “두 가지만 있으면 시작합니다”
          `font-size:12.5px font-weight:600 color:#475467`
        - `div`
          `display:flex align-items:center gap:11px min-height:52px border-bottom:1px solid #F3F5FA`
        - `div`
          `display:flex align-items:center gap:11px min-height:52px border-bottom:1px solid #F3F5FA`
        - `div`
          `display:flex align-items:center gap:11px min-height:52px`
      - `div` **Card(18)**
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px 15px`
        - `div`
          `display:flex align-items:center justify-content:space-between gap:8px`
        - `div`
          `display:flex flex-direction:column gap:8px margin-top:10px opacity:.5`
        - `div`
          `margin-top:11px`
    - `div`
      `display:flex gap:10px padding:12px 18px 20px border-top:1px solid #EFF2F8`
      - `div` **PrimaryButton(48)** — “소비 기록하기”
        `display:flex align-items:center justify-content:center gap:6px height:48px flex:1.4 border-radius:13px background:#3556E6 border:none color:#FFFFFF font-size:15px font-weight:600`
      - `div` **SecondaryButton(48)** — “닫기”
        `display:flex align-items:center justify-content:center gap:6px height:48px flex:1 border-radius:13px background:#FFFFFF border:1px solid #D7DEEA color:#475467 font-size:15px font-weight:600`
