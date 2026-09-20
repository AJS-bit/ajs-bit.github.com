# StocksMine — 블록 개요

원본 `canvas/StocksMine.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div` **화면프레임**
  `width:390px height:844px background:#EDF0F7 color:#101828 display:flex flex-direction:column`
  - `div`
    `display:flex flex-direction:column gap:10px padding:14px 16px 12px`
    - `div`
      `display:flex align-items:center justify-content:space-between gap:8px`
      - `div`
        `display:flex align-items:baseline gap:8px`
        - `h1` **text 21px/700** — “주식”
          `font-size:21px font-weight:700 letter-spacing:-0.03em line-height:1.2 color:#101828`
        - `span` **text 12px/500** — “보유 3 · 관심 5”
          `font-size:12px font-weight:500 color:#626D88`
      - `div`
        `display:flex align-items:center gap:2px`
        - `div`
          `width:36px height:36px border-radius:11px display:flex align-items:center justify-content:center`
        - `div`
          `width:36px height:36px border-radius:11px display:flex align-items:center justify-content:center position:relative`
  - `div` **본문(스크롤 영역)**
    `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
    - `div`
      `display:flex align-items:center gap:10px padding:10px 14px background:#E9EDFD border-radius:14px`
      - `div`
        `display:flex flex-direction:column gap:1px flex:1`
        - `span` **text 12px/500** — “이번 달 저축·투자 여력”
          `font-size:12px font-weight:500 color:#3B4E8F`
        - `span` **text 11px/400** — “총수입 390만원 − 소비 예상·저축·상환”
          `font-size:11px color:#3B4E8F`
      - `span` — “27”
        `font-size:17px font-weight:700 letter-spacing:-0.02em color:#3556E6 white-space:nowrap`
        - `span` **text 12.5px/600** — “만원”
          `font-size:12.5px font-weight:600`
    - `div` **Card(18)**
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px 8px`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:8px`
        - `div`
          `display:flex align-items:baseline gap:7px`
        - `span` **text 12.5px/600** — “보유 기록 ›”
          `font-size:12.5px font-weight:600 color:#3556E6 white-space:nowrap`
      - `div`
        `margin-top:2px`
        - `div`
          `display:flex align-items:center gap:10px padding:9px 0 border-bottom:1px solid #F3F5FA`
        - `div`
          `display:flex align-items:center gap:10px padding:9px 0 border-bottom:1px solid #F3F5FA`
        - `div`
          `display:flex align-items:center gap:10px padding:9px 0`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:8px padding:10px 0 4px border-top:1px solid #EFF2F8`
        - `div`
          `display:flex flex-direction:column gap:1px`
        - `span` — “1,244”
          `font-size:17px font-weight:700 letter-spacing:-0.02em color:#101828`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:8px padding:8px 0 2px`
        - `div`
          `display:flex flex-direction:column gap:1px`
        - `div`
          `width:46px height:27px border-radius:99px background:#E3E8F1 padding:3px display:flex justify-content:flex-start`
    - `div` **Card(18)**
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px 6px`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:8px`
        - `div`
          `display:flex align-items:baseline gap:7px`
        - `span` **text 12.5px/600** — “관심 추가 ›”
          `font-size:12.5px font-weight:600 color:#3556E6`
      - `div`
        `margin-top:2px`
        - `div`
          `display:flex align-items:center gap:10px padding:6px 0 border-bottom:1px solid #F3F5FA`
        - `div`
          `display:flex align-items:center gap:10px padding:6px 0 border-bottom:1px solid #F3F5FA`
        - `div`
          `display:flex align-items:center gap:10px padding:6px 0 border-bottom:1px solid #F3F5FA`
        - `div`
          `display:flex align-items:center gap:10px padding:6px 0 border-bottom:1px solid #F3F5FA`
        - `div`
          `display:flex align-items:center gap:10px padding:6px 0`
  - `div` **BottomNav**
    `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`
    - `div`
      `display:flex flex-direction:column align-items:center gap:3px flex:1`
      - `div`
        `width:40px height:24px display:flex align-items:center justify-content:center`
      - `span` **text 11px/500** — “홈”
        `font-size:11px font-weight:500 color:#606B7D`
    - `div`
      `display:flex flex-direction:column align-items:center gap:3px flex:1`
      - `div`
        `width:40px height:24px display:flex align-items:center justify-content:center`
      - `span` **text 11px/500** — “자산”
        `font-size:11px font-weight:500 color:#606B7D`
    - `div`
      `display:flex flex-direction:column align-items:center gap:3px flex:1`
      - `div`
        `width:40px height:24px display:flex align-items:center justify-content:center`
      - `span` **text 11px/500** — “소비”
        `font-size:11px font-weight:500 color:#606B7D`
    - `div`
      `display:flex flex-direction:column align-items:center gap:3px flex:1`
      - `div`
        `width:40px height:24px border-radius:99px background:#E9EDFD display:flex align-items:center justify-content:center`
      - `span` **text 11px/600** — “주식”
        `font-size:11px font-weight:600 color:#3556E6`
    - `div`
      `display:flex flex-direction:column align-items:center gap:3px flex:1`
      - `div`
        `width:40px height:24px display:flex align-items:center justify-content:center`
      - `span` **text 11px/500** — “목적지”
        `font-size:11px font-weight:500 color:#606B7D`
