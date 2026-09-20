# ClassifySheet — 블록 개요

원본 `canvas/ClassifySheet.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div` **화면프레임**
  `width:390px height:844px background:#2A3245 color:#101828 display:flex flex-direction:column position:relative`
  - `div`
    `height:60px display:flex align-items:flex-end justify-content:center padding:0 20px 12px text-align:center`
    - `span` **text 11px/500** — “배경을 눌러 닫기”
      `font-size:11px line-height:1.4 font-weight:500 color:rgba(255,255,255,.62)`
  - `div` **BottomSheet**
    `flex:1 min-height:0 background:#FFFFFF border-radius:26px 26px 0 0 display:flex flex-direction:column`
    - `div`
      `display:flex justify-content:center padding:9px 0 0`
      - `span` **GrabHandle**
        `width:38px height:4px border-radius:99px background:#D7DEEA`
    - `div`
      `display:flex align-items:flex-start justify-content:space-between gap:10px padding:12px 18px 14px border-bottom:1px solid #EFF2F8`
      - `div`
        - `h2` **text 18px/700** — “분류하기 · 7건”
          `font-size:18px font-weight:700 letter-spacing:-0.025em color:#101828`
        - `p` **text 12.5px/400** — “같은 메모끼리 묶었어요. 추천은 눌러야 정해지고, 정한 것만 저장돼요.”
          `font-size:12.5px line-height:1.45 color:#626D88`
      - `span` **text 13px/600** — “닫기”
        `font-size:13px font-weight:600 color:#475467 white-space:nowrap`
    - `div`
      `flex:1 min-height:0 padding:6px 18px 0 display:flex flex-direction:column`
      - `div`
        `display:flex align-items:center gap:10px height:52px border-bottom:1px solid #F3F5FA`
        - `div`
          `display:flex flex-direction:column gap:2px flex:1`
        - `span` — “카페/간식”
          `display:inline-flex align-items:center gap:5px height:30px padding:0 10px border-radius:8px background:#E9EDFD border:1.5px solid #3556E6 font-size:12px font-weight:600 color:#101828 white-space:nowrap`
      - `div`
        `background:#F4F6FB border-radius:0 0 12px 12px padding:0 10px 2px`
        - `div`
          `display:flex align-items:center gap:10px height:40px border-bottom:1px solid #F3F5FA`
        - `div`
          `display:flex align-items:center gap:10px height:40px border-bottom:1px solid #F3F5FA`
        - `div`
          `display:flex align-items:center gap:10px height:40px border-bottom:1px solid #F3F5FA`
        - `div`
          `display:flex align-items:center gap:10px height:40px`
      - `div`
        `display:flex align-items:center gap:10px height:52px border-bottom:1px solid #F3F5FA`
        - `div`
          `display:flex flex-direction:column gap:2px flex:1`
        - `span` — “식비”
          `display:inline-flex align-items:center gap:5px height:30px padding:0 10px border-radius:8px background:#FFFFFF border:1px solid #D7DEEA font-size:12px font-weight:600 color:#101828 white-space:nowrap`
      - `div`
        `display:flex align-items:center gap:10px height:52px border-bottom:1px solid #F3F5FA`
        - `div`
          `display:flex flex-direction:column gap:2px flex:1`
        - `span` **text 12.5px/600** — “분류 고르기 ›”
          `font-size:12.5px font-weight:600 color:#3556E6 white-space:nowrap`
      - `div`
        `display:flex align-items:center gap:10px height:52px`
        - `div`
          `display:flex flex-direction:column gap:2px flex:1`
        - `span` **text 12.5px/600** — “분류 고르기 ›”
          `font-size:12.5px font-weight:600 color:#3556E6 white-space:nowrap`
    - `div`
      `padding:12px 18px 20px border-top:1px solid #EFF2F8 display:flex flex-direction:column gap:8px`
      - `div` **text 16px/600** — “3건 저장”
        `display:flex align-items:center justify-content:center gap:6px height:52px width:100% border-radius:14px background:#3556E6 border:none color:#FFFFFF font-size:16px font-weight:600`
      - `p` **text 11.5px/400** — “나머지 4건은 분류 안 함으로 남아요”
        `text-align:center font-size:11.5px line-height:1.5 color:#626D88`
