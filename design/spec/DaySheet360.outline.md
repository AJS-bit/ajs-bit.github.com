# DaySheet360 — 블록 개요

원본 `canvas/DaySheet360.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div`
  `width:360px height:640px background:#2A3245 color:#101828 display:flex flex-direction:column position:relative`
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
        - `span` **text 12.5px/400** — “오늘 4건 37,000원”
          `font-size:12.5px color:#626D88`
      - `span` **text 13px/600** — “닫기”
        `font-size:13px font-weight:600 color:#475467`
    - `div`
      `flex:1 min-height:0 padding:12px 14px 0 display:flex flex-direction:column gap:10px`
      - `div`
        - `div`
          `display:flex flex-direction:column gap:8px`
      - `div`
        - `div`
          `display:flex flex-direction:column gap:5px`
      - `div`
        `display:flex flex-direction:column`
        - `div`
          `height:18px display:flex align-items:center`
        - `div`
          `display:flex align-items:center gap:10px height:44px border-bottom:1px solid #F3F5FA`
        - `div`
          `display:flex align-items:center gap:10px height:44px border-bottom:1px solid #F3F5FA`
        - `div`
          `display:flex align-items:center gap:10px height:44px`
        - `div` — “1건 더 보기”
          `display:flex align-items:center gap:5px height:32px font-size:12.5px font-weight:600 color:#3556E6 white-space:nowrap`
      - `div`
        - `div` **SecondaryButton(44)** — “9월 8일 다 적었어요”
          `display:flex align-items:center justify-content:center gap:6px height:44px width:100% border-radius:12px background:#FFFFFF border:1px solid #D7DEEA color:#475467 font-size:14.5px font-weight:600 white-space:nowrap`
    - `div`
      `padding:10px 14px 14px border-top:1px solid #EFF2F8 background:#FFFFFF`
      - `div` **text 16px/600** — “저장”
        `display:flex align-items:center justify-content:center gap:6px height:52px width:100% border-radius:14px background:#3556E6 border:none color:#FFFFFF font-size:16px font-weight:600`
