# DaySheetNoSpend — 블록 개요

원본 `canvas/DaySheetNoSpend.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div` **화면프레임**
  `width:390px height:844px background:#2A3245 color:#101828 display:flex flex-direction:column position:relative`
  - `div`
    `height:60px display:flex align-items:flex-end justify-content:center padding:0 20px 12px text-align:center`
    - `span` **text 11px/500** — “배경을 눌러 닫기 · 앱이 다시 시작되면 저장하지 않은 내용은 사라져요”
      `font-size:11px line-height:1.4 font-weight:500 color:rgba(255,255,255,.62)`
  - `div` **BottomSheet**
    `flex:1 min-height:0 background:#FFFFFF border-radius:26px 26px 0 0 display:flex flex-direction:column`
    - `div`
      `display:flex justify-content:center padding:9px 0 0`
      - `span` **GrabHandle**
        `width:38px height:4px border-radius:99px background:#D7DEEA`
    - `div`
      `display:flex align-items:flex-start justify-content:space-between gap:10px padding:12px 18px 12px border-bottom:1px solid #EFF2F8`
      - `div`
        `display:flex flex-direction:column gap:3px`
        - `div`
          `display:flex align-items:center gap:4px`
        - `span` **text 12.5px/400** — “오늘 소비는 아직 기록이 없어요 · 이체 300,000원(소비율 제외)”
          `font-size:12.5px color:#626D88`
      - `span` **text 13px/600** — “닫기”
        `font-size:13px font-weight:600 color:#475467`
    - `div`
      `flex:1 min-height:0 padding:12px 18px 0 display:flex flex-direction:column gap:10px`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:10px height:48px padding:0 14px border-radius:12px background:#FFFFFF border:1px solid #CFD7E6`
        - `span` **text 12px/600** — “금액”
          `font-size:12px font-weight:600 color:#475467`
        - `span`
          `display:inline-flex align-items:baseline gap:4px`
      - `div` **text 11.5px/400** — “금액을 넣거나, 안 썼으면 「오늘은 안 썼어요」로 표시해요”
        `font-size:11.5px line-height:1.45 color:#626D88 padding:0 2px`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:10px height:44px padding:0 14px border-radius:12px background:#FFFFFF border:1px solid #CFD7E6`
        - `span`
          `display:inline-flex align-items:center gap:12px`
      - `div`
        `display:flex flex-direction:column gap:8px`
        - `div`
          `display:flex align-items:center gap:8px`
        - `div`
          `display:flex align-items:center gap:6px`
      - `div`
        `display:flex flex-direction:column gap:8px`
        - `span` **text 12px/600** — “최근 기록”
          `font-size:12px font-weight:600 color:#475467`
        - `div`
          `display:flex gap:6px padding:0 18px`
      - `div`
        `margin-top:2px`
        - `div` **text 16px/600** — “저장”
          `display:flex align-items:center justify-content:center gap:6px height:52px width:100% border-radius:14px background:#E8ECF5 border:none color:#B4BECD font-size:16px font-weight:600`
      - `div`
        - `div`
          `display:flex flex-direction:column gap:5px`
      - `div`
        `position:relative margin-top:4px`
        - `div`
          `display:flex flex-direction:column`
      - `div`
        `position:relative margin-top:auto`
        - `div` **SecondaryButton(44)** — “오늘은 안 썼어요”
          `display:flex align-items:center justify-content:center gap:6px height:44px width:100% border-radius:12px background:#FFFFFF border:1px solid #D7DEEA color:#475467 font-size:14.5px font-weight:600 white-space:nowrap`
