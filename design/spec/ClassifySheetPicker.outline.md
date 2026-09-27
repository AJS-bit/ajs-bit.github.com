# ClassifySheetPicker — 블록 개요

원본 `canvas/ClassifySheetPicker.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div` **화면프레임**
  `width:390px height:844px background:#2A3245 color:#101828 display:flex flex-direction:column position:relative`
  - `div`
    `flex:1 min-height:0 display:flex align-items:flex-end justify-content:center padding:0 20px 12px text-align:center`
    - `span` **text 11.5px/500** — “배경을 눌러 닫기”
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
          `display:flex align-items:center gap:4px`
        - `span` **text 12.5px/400** — “같은 메모끼리 묶고, 메모 없는 기록은 한 건씩 보여요. 추천은 눌러야 정해지고, 정한 것만 저장돼요.”
          `font-size:12.5px line-height:18.125px color:#626D88`
      - `span` **text 13px/600** — “닫기”
        `font-size:13px font-weight:600 line-height:18.57px color:#475467 white-space:nowrap`
    - `div`
      `padding:6px 18px 20px display:flex flex-direction:column`
      - `div`
        `border-bottom:1px solid #F3F5FA`
        - `div`
          `display:flex align-items:center gap:10px min-height:52px padding:6px 0`
      - `div`
        `border-bottom:1px solid #F3F5FA`
        - `div`
          `display:flex align-items:center gap:10px min-height:52px padding:6px 0`
        - `div`
          `display:flex flex-wrap:wrap gap:6px padding:8px 0 10px`
      - `div`
        `border-bottom:1px solid #F3F5FA`
        - `div`
          `display:flex align-items:center gap:10px min-height:52px padding:6px 0`
      - `div`
        `border-bottom:1px solid #F3F5FA`
        - `div`
          `display:flex align-items:center gap:10px min-height:52px padding:6px 0`
      - `div`
        - `div`
          `display:flex align-items:center gap:10px min-height:52px padding:6px 0`
    - `div`
      `padding:12px 18px 21px border-top:1px solid #EFF2F8 display:flex flex-direction:column gap:8px`
      - `div` **text 16px/600** — “0건 저장”
        `display:flex align-items:center justify-content:center gap:6px height:52px width:100% border-radius:14px background:#E8ECF5 border:none color:#B4BECD font-size:16px font-weight:600`
      - `p` **text 11.5px/400** — “카테고리를 골라 주세요 · 추천도 눌러야 정해져요”
        `text-align:center font-size:11.5px line-height:17.25px color:#626D88`
