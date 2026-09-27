# DaySheet360 — 블록 개요

원본 `canvas/DaySheet360.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div`
  `width:360px height:640px background:#2A3245 color:#101828 display:flex flex-direction:column position:relative`
  - `div`
    `height:30px`
  - `div` **BottomSheet**
    `height:610px background:#FFFFFF border:1px solid #E3E8F1 border-bottom:0 border-radius:26px 26px 0 0 display:flex flex-direction:column`
    - `div`
      `position:relative display:flex align-items:flex-start justify-content:space-between gap:10px padding:20px 18px 12px border-bottom:1px solid #EFF2F8`
      - `span` **GrabHandle**
        `position:absolute top:8px left:50% width:38px height:4px border-radius:99px background:#D7DEEA`
      - `div`
        `display:flex flex-direction:column gap:3px`
        - `div`
          `display:flex align-items:center gap:4px min-height:28px`
        - `span` **text 12.5px/400** — “오늘 4건 37,000원”
          `font-size:12.5px line-height:18.125px color:#626D88`
      - `span` **text 13px/600** — “닫기”
        `font-size:13px font-weight:600 line-height:18.57px color:#475467 white-space:nowrap`
    - `div`
      `flex:1 min-height:0 padding:12px 18px 20px display:flex flex-direction:column gap:10px justify-content:flex-end`
      - `div`
        `display:flex flex-direction:column`
        - `div`
          `display:flex align-items:center height:18px`
        - `div`
          `display:flex align-items:center justify-content:flex-end gap:6px height:48px padding:0 16px border-radius:12px background:#FFFFFF border:1px solid #CFD7E6`
      - `div` — “· 저장을 눌러야 기록돼요”
        `font-size:11.5px line-height:16.675px color:#626D88 padding:0 2px`
        - `span` — “1.2만원”
          `font-weight:600 color:#475467`
      - `div`
        `display:flex flex-direction:column`
        - `div`
          `display:flex align-items:center height:18px`
        - `div`
          `display:flex align-items:center gap:10px height:44px padding:0 14px border-radius:12px background:#FFFFFF border:1px solid #CFD7E6`
      - `div`
        `display:flex flex-direction:column gap:8px`
        - `div`
          `display:flex align-items:center justify-content:space-between gap:8px min-height:24px`
        - `div`
          `display:flex align-items:center gap:6px`
      - `div`
        `display:flex flex-direction:column gap:8px`
        - `span` **text 12px/600** — “최근 기록”
          `font-size:12px font-weight:600 line-height:17px color:#475467`
        - `div`
          `display:flex gap:6px padding:0 18px`
      - `div`
        - `div`
          `display:flex flex-direction:column gap:4px`
      - `div`
        `display:flex flex-direction:column gap:8px`
        - `span` **text 12px/600** — “오늘 기록”
          `font-size:12px font-weight:600 line-height:17px color:#475467`
        - `div`
          `display:flex flex-direction:column`
        - `div` — “1건 더 보기”
          `display:flex align-items:center gap:4px height:28px padding:0 2px font-size:12.5px font-weight:600 color:#3556E6 white-space:nowrap`
      - `div`
        `display:flex flex-direction:column gap:4px`
        - `div` **SecondaryButton(44)** — “9월 8일 다 적었어요”
          `display:flex align-items:center justify-content:center gap:6px height:44px width:100% border-radius:12px background:#FFFFFF border:1px solid #D7DEEA color:#475467 font-size:12.5px font-weight:600 white-space:nowrap`
        - `div` **text 12px/400** — “누르면 달력에 ✓가 남고 오늘 저녁엔 더 묻지 않아요”
          `font-size:12px line-height:17.4px color:#626D88 padding:0 2px`
    - `div`
      `padding:12px 18px 12px border-top:1px solid #EFF2F8 background:#FFFFFF`
      - `div`
        `margin-top:2px`
        - `div` **text 16px/600** — “저장”
          `display:flex align-items:center justify-content:center gap:6px height:52px width:100% border-radius:14px background:#3556E6 border:none color:#FFFFFF font-size:16px font-weight:600`
