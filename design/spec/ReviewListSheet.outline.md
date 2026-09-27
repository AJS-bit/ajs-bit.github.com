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
        - `span` — “8월에 새 기록이 있어요 · 8월 합계 고치기 › · 통신 반복 기록이 두 번 들어갔을 수 있어요 › · 카테고리 ”
          `flex:1 color:rgba(255,255,255,.86)`
      - `div`
        `display:flex gap:8px font-size:11.5px line-height:1.5`
        - `span` — “이 화면”
          `width:96px color:rgba(255,255,255,.55)`
        - `span` — “마감한 8월에 기록을 더한 30일 식비 55,000원 · 지난 달 소비 같은 장면)의 두 항목. 기본 장면 9월 8”
          `flex:1 color:rgba(255,255,255,.86)`
      - `div`
        `display:flex gap:8px font-size:11.5px line-height:1.5`
        - `span` — “28일~다음 달 3일”
          `width:96px color:rgba(255,255,255,.55)`
        - `span` — “카테고리 없는 기록 7건 · 월말 전에 정리 ›”
          `flex:1 color:rgba(255,255,255,.86)`
      - `div`
        `display:flex gap:8px font-size:11.5px line-height:1.5`
        - `span` — “달이 바뀌면”
          `width:96px color:rgba(255,255,255,.55)`
        - `span` — “9월 카테고리 없는 기록 7건 · 마감 전에 정리 ›(10월 2일 홈)”
          `flex:1 color:rgba(255,255,255,.86)`
      - `div`
        `display:flex gap:8px font-size:11.5px line-height:1.5`
        - `span` — “누르면”
          `width:96px color:rgba(255,255,255,.55)`
        - `span` — “합계 고치기 → 한 단계 확인 「8월 소비 합계만 새 금액으로 · 합계 고치기 · 마감 창이 아님) · 반복 중복 ”
          `flex:1 color:rgba(255,255,255,.86)`
      - `div`
        `display:flex gap:8px font-size:11.5px line-height:1.5`
        - `span` — “항목이 하나면”
          `width:96px color:rgba(255,255,255,.55)`
        - `span` — “홈 달력의 행이 그 항목 카테고리 없는 기록 7건 · 카테고리 고르기 ›)이 되고 누르면 바로 열려요 · 샘플 모드”
          `flex:1 color:rgba(255,255,255,.86)`
  - `div`
    `height:60px display:flex align-items:flex-end justify-content:center padding:0 20px 12px text-align:center`
    - `span` **text 11px/500** — “배경을 눌러 닫기”
      `font-size:11px line-height:1.4 font-weight:500 color:rgba(255,255,255,.62)`
  - `div` **BottomSheet**
    `position:relative background:#FFFFFF border:1px solid #E3E8F1 border-radius:26px 26px 0 0 display:flex flex-direction:column`
    - `span` **GrabHandle**
      `position:absolute top:8px left:50% width:38px height:4px border-radius:99px background:#D7DEEA`
    - `div`
      `display:flex align-items:flex-start justify-content:space-between gap:8px padding:20px 18px 12px`
      - `h2` **text 18px/700** — “확인할 내용 2개”
        `font-size:18px font-weight:700 line-height:23.4px letter-spacing:-0.025em color:#101828`
      - `span` **text 13px/600** — “닫기”
        `display:inline-flex align-items:center height:28px padding:0 4px font-size:13px font-weight:600 color:#475467 white-space:nowrap`
    - `div`
      `padding:4px 18px 28px display:flex flex-direction:column`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:10px min-height:53px border-top:1px solid #EFF2F8`
        - `span` **text 14.5px/600** — “8월에 새 기록이 있어요 · 8월 합계 고치기”
          `font-size:14.5px font-weight:600 color:#101828`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:10px min-height:53px border-top:1px solid #EFF2F8`
        - `span` **text 14.5px/600** — “카테고리 없는 기록 7건 · 카테고리 고르기”
          `font-size:14.5px font-weight:600 color:#101828`
