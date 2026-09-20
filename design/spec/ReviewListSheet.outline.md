# ReviewListSheet — 블록 개요

원본 `canvas/ReviewListSheet.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div` **화면프레임**
  `width:390px height:844px background:#2A3245 color:#101828 display:flex flex-direction:column position:relative`
  - `div`
    `flex:1 min-height:0 display:flex flex-direction:column justify-content:center`
    - `div`
      `padding:12px 14px border:1px dashed rgba(255,255,255,.32) border-radius:12px display:flex flex-direction:column gap:7px`
      - `span` **text 11px/600** — “시안 주석 · 앱에는 보이지 않아요”
        `font-size:11px font-weight:600 letter-spacing:0.02em color:rgba(255,255,255,.62)`
      - `div`
        `display:flex gap:8px font-size:11.5px line-height:1.5`
        - `span` — “항목은 셋뿐”
          `width:96px color:rgba(255,255,255,.55)`
        - `span` — “8월 다시 마감 필요 › · 통신 반복 건이 두 번 잡혔을 수 있어요 › · 분류 안 함 7건 · 분류하기 ›”
          `flex:1 color:rgba(255,255,255,.86)`
      - `div`
        `display:flex gap:8px font-size:11.5px line-height:1.5`
        - `span` — “이 화면”
          `width:96px color:rgba(255,255,255,.55)`
        - `span` — “홈의 확인할 내용 2개 = 아래 두 항목. 통신 항목은 자동 기록일(25일) 뒤에만 생겨요”
          `flex:1 color:rgba(255,255,255,.86)`
      - `div`
        `display:flex gap:8px font-size:11.5px line-height:1.5`
        - `span` — “28일~다음 달 3일”
          `width:96px color:rgba(255,255,255,.55)`
        - `span` — “분류 안 함 4건 · 월말 전에 정리 ›”
          `flex:1 color:rgba(255,255,255,.86)`
      - `div`
        `display:flex gap:8px font-size:11.5px line-height:1.5`
        - `span` — “달이 바뀌면”
          `width:96px color:rgba(255,255,255,.55)`
        - `span` — “9월 분류 안 함 4건 · 마감 전에 정리 ›”
          `flex:1 color:rgba(255,255,255,.86)`
      - `div`
        `display:flex gap:8px font-size:11.5px line-height:1.5`
        - `span` — “누르면”
          `width:96px color:rgba(255,255,255,.55)`
        - `span` — “다시 마감 → 8월 마감 · 통신 → 그 날짜 기록 창(두 행) · 분류 → 분류하기 창”
          `flex:1 color:rgba(255,255,255,.86)`
  - `div`
    `height:60px display:flex align-items:flex-end justify-content:center padding:0 20px 12px text-align:center`
    - `span` **text 11px/500** — “배경을 눌러 닫기”
      `font-size:11px line-height:1.4 font-weight:500 color:rgba(255,255,255,.62)`
  - `div` **BottomSheet**
    `background:#FFFFFF border-radius:26px 26px 0 0 display:flex flex-direction:column`
    - `div`
      `display:flex justify-content:center padding:9px 0 0`
      - `span` **GrabHandle**
        `width:38px height:4px border-radius:99px background:#D7DEEA`
    - `div`
      `display:flex align-items:center justify-content:space-between gap:10px padding:12px 18px 12px border-bottom:1px solid #EFF2F8`
      - `h2` **text 18px/700** — “확인할 내용 2개”
        `font-size:18px font-weight:700 letter-spacing:-0.025em color:#101828`
      - `span` **text 13px/600** — “닫기”
        `font-size:13px font-weight:600 color:#475467 white-space:nowrap`
    - `div`
      `padding:4px 18px 28px display:flex flex-direction:column`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:10px min-height:52px border-bottom:1px solid #F3F5FA`
        - `span` **text 14.5px/600** — “8월 다시 마감 필요”
          `font-size:14.5px font-weight:600 color:#101828`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:10px min-height:52px`
        - `span` **text 14.5px/600** — “분류 안 함 7건 · 분류하기”
          `font-size:14.5px font-weight:600 color:#101828`
