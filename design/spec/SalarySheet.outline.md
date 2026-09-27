# SalarySheet — 블록 개요

원본 `canvas/SalarySheet.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div` **화면프레임**
  `width:390px height:844px background:#2A3245 color:#101828 display:flex flex-direction:column`
  - `div`
    `flex:0 1 447px min-height:12px display:flex align-items:flex-end justify-content:center`
    - `span` **text 11.5px/500** — “배경을 눌러 닫기”
      `font-size:11.5px font-weight:500 color:rgba(255,255,255,.62)`
  - `div` **BottomSheet**
    `flex:1 0 auto background:#FFFFFF border-radius:26px 26px 0 0 display:flex flex-direction:column color:#101828`
    - `div`
      `display:flex justify-content:center padding:9px 0 0`
      - `span` **GrabHandle**
        `width:38px height:4px border-radius:99px background:#D7DEEA`
    - `div`
      `display:flex align-items:flex-start justify-content:space-between gap:10px padding:12px 18px 14px border-bottom:1px solid #EFF2F8`
      - `div`
        - `h2` **text 18px/700** — “월급 입력”
          `font-size:18px font-weight:700 letter-spacing:-0.025em color:#101828`
        - `p` **text 12.5px/400** — “월급의 몇 %를 썼는지 계산하는 기준이에요.”
          `font-size:12.5px line-height:1.45 color:#626D88`
      - `div`
        `width:36px height:36px border-radius:11px background:#F4F6FB display:flex align-items:center justify-content:center`
    - `div`
      `flex:1 0 auto padding:14px 18px 14px display:flex flex-direction:column gap:15px`
      - `div`
        `flex:0 0 auto`
        - `div` **text 12px/600** — “월급 (실수령)”
          `font-size:12px font-weight:600 color:#475467`
        - `div` **InputField**
          `display:flex align-items:center gap:5px height:46px padding:0 12px border-radius:11px border:1px solid #CFD7E6 background:#FFFFFF`
        - `div` **text 12px/500** — “= 360만원”
          `font-size:12px font-weight:500 line-height:16px color:#626D88 margin-top:4px white-space:nowrap`
        - `div`
          `display:flex align-items:center gap:5px margin-top:6px`
      - `div` **text 13px/600** — “소비 목표 60% · 월 216만원까지”
        `font-size:13px font-weight:600 line-height:19.5px color:#101828 margin-top:-9px`
      - `div` **text 13px/600** — “다른 수치도 입력하기 ›”
        `display:flex align-items:center height:44px font-size:13px font-weight:600 color:#3556E6`
    - `div`
      `display:flex gap:10px padding:12px 18px 20px border-top:1px solid #EFF2F8`
      - `div` **SecondaryButton(48)** — “나중에”
        `display:flex align-items:center justify-content:center gap:6px height:48px flex:1 border-radius:13px background:#FFFFFF border:1px solid #D7DEEA color:#475467 font-size:15px font-weight:600`
      - `div` **PrimaryButton(48)** — “저장”
        `display:flex align-items:center justify-content:center gap:6px height:48px flex:1.4 border-radius:13px background:#3556E6 border:none color:#FFFFFF font-size:15px font-weight:600`
