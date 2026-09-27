# DaySheetDeleted — 블록 개요

원본 `canvas/DaySheetDeleted.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div` **화면프레임**
  `width:390px height:844px background:#2A3245 color:#101828 display:flex flex-direction:column position:relative`
  - `div`
    `flex:1 min-height:0 display:flex align-items:flex-end justify-content:center padding:0 20px 12px text-align:center`
    - `span` **text 11.5px/500** — “배경을 눌러 닫기 · 앱이 다시 시작되면 저장하지 않은 내용은 사라져요”
      `font-size:11.5px font-weight:500 color:rgba(255,255,255,.62)`
  - `div` **BottomSheet**
    `background:#FFFFFF border:1px solid #E3E8F1 border-bottom:0 border-radius:26px 26px 0 0 display:flex flex-direction:column`
    - `div`
      `position:relative display:flex align-items:flex-start justify-content:space-between gap:10px padding:20px 18px 12px border-bottom:1px solid #EFF2F8`
      - `span` **GrabHandle**
        `position:absolute top:8px left:50% width:38px height:4px border-radius:99px background:#D7DEEA`
      - `div`
        `display:flex flex-direction:column gap:3px`
        - `div`
          `display:flex align-items:center gap:4px min-height:28px`
        - `span` **text 12.5px/400** — “2건 13,500원”
          `font-size:12.5px line-height:18.125px color:#626D88`
      - `span` **text 13px/600** — “닫기”
        `font-size:13px font-weight:600 line-height:18.57px color:#475467 white-space:nowrap`
    - `div` — “지웠어요 · 택시 45,000원 ·”
      `padding:8px 18px border-bottom:1px solid #EFF2F8 background:#F4F6FB font-size:11.5px font-weight:500 line-height:16.675px color:#475467`
      - `span` — “되돌리기”
        `font-weight:600 color:#3556E6`
    - `div`
      `flex:1 min-height:0 padding:12px 18px 21px display:flex flex-direction:column gap:10px`
      - `div`
        `display:flex flex-direction:column gap:8px`
        - `span` **text 12px/600** — “9월 3일 기록”
          `font-size:12px font-weight:600 line-height:17px color:#475467`
        - `div` **Card(18)**
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:2px 14px`
      - `div` — “추가”
        `display:flex align-items:center justify-content:center gap:6px height:46px border-radius:14px border:1.5px dashed #B9C3D6 background:rgba(255,255,255,.55) color:#3556E6 font-size:14px font-weight:600`
      - `div`
        - `div`
          `display:flex flex-direction:column gap:4px`
      - `div`
        `display:flex flex-direction:column gap:4px`
        - `div` **SecondaryButton(44)** — “9월 3일 다 적었어요”
          `display:flex align-items:center justify-content:center gap:6px height:44px width:100% border-radius:12px background:#FFFFFF border:1px solid #D7DEEA color:#475467 font-size:12.5px font-weight:600 white-space:nowrap`
        - `div` **text 12px/400** — “누르면 달력에 ✓가 남아요 · 안 눌러도 기록은 그대로예요”
          `font-size:12px line-height:17.4px color:#626D88 padding:0 2px`
