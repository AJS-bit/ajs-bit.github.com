# DaySheetEdit — 블록 개요

원본 `canvas/DaySheetEdit.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div` **화면프레임**
  `width:390px height:844px background:#2A3245 color:#101828 display:flex flex-direction:column position:relative`
  - `div`
    `height:60px display:flex align-items:flex-end justify-content:center padding:0 20px 12px text-align:center`
    - `span` **text 11px/500** — “배경을 눌러 닫기 · 저장 전 내용은 앱 재시작 시 사라져요”
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
        - `span` **text 12.5px/400** — “9월 3일 3건 58,500원”
          `font-size:12.5px color:#626D88`
      - `span` **text 13px/600** — “닫기”
        `font-size:13px font-weight:600 color:#475467`
    - `div`
      `flex:1 min-height:0 padding:14px 18px 0 display:flex flex-direction:column gap:12px`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:10px height:48px padding:0 14px border-radius:12px background:#FFFFFF border:1.5px solid #3556E6 box-shadow:0 0 0 3px rgba(53,86,230,.16)`
        - `span` **text 12px/600** — “금액”
          `font-size:12px font-weight:600 color:#475467`
        - `span`
          `display:inline-flex align-items:baseline gap:4px`
      - `div`
        `font-size:11.5px line-height:1.45 color:#626D88 padding:0 2px`
        - `span` — “4.5만원”
          `font-weight:600 color:#475467`
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
        `display:flex gap:8px margin-top:2px`
        - `div` **text 16px/600** — “저장”
          `display:flex align-items:center justify-content:center gap:6px height:52px flex:1.6 border-radius:14px background:#3556E6 border:none color:#FFFFFF font-size:16px font-weight:600`
        - `div` **text 15px/600** — “삭제”
          `display:flex align-items:center justify-content:center gap:6px height:52px flex:1 border-radius:14px background:#FFFFFF border:1px solid #D7DEEA color:#475467 font-size:15px font-weight:600`
  - `div`
    `position:absolute left:0 right:0 bottom:0 height:280px background:#E8ECF5 border-top:1px solid #D7DEEA display:flex align-items:center justify-content:center flex-direction:column gap:4px`
    - `span` **text 12px/600** — “시스템 숫자 키보드 자리”
      `font-size:12px font-weight:600 color:#626D88`
    - `span` **text 11px/400** — “기기가 그립니다 · 약 280px · 이 위로 날짜·금액·저장이 보여야 해요”
      `font-size:11px color:#697182`
