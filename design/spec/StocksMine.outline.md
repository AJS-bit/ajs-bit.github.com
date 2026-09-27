# StocksMine — 블록 개요

원본 `canvas/StocksMine.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div`
  `width:390px height:912px background:#EDF0F7 color:#101828 display:flex flex-direction:column`
  - `div`
    `display:flex flex-direction:column gap:10px padding:14px 16px 12px`
    - `div`
      `display:flex align-items:flex-start justify-content:space-between gap:8px`
      - `div`
        `display:flex align-items:center gap:4px min-height:36px`
        - `h1` **text 21px/700** — “주식”
          `font-size:21px font-weight:700 letter-spacing:-0.03em line-height:1.25 color:#101828`
        - `span`
          `width:28px height:28px border-radius:99px display:inline-flex align-items:center justify-content:center`
      - `div`
        `display:flex align-items:flex-start gap:0`
        - `div`
          `width:44px display:flex flex-direction:column align-items:center`
        - `div`
          `width:44px display:flex flex-direction:column align-items:center`
        - `div`
          `width:44px display:flex flex-direction:column align-items:center`
  - `div` **본문(스크롤 영역)**
    `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
    - `div`
      `display:flex align-items:flex-start gap:8px padding:9px 12px background:#E9EDFD border-radius:14px`
      - `span`
        `margin-top:1px`
      - `div`
        `display:flex flex-direction:column gap:2px flex:1`
        - `span` **text 12px/600** — “목적지에 나누고 남은 돈”
          `font-size:12px font-weight:600 color:#3B4E8F`
        - `span` **text 12.5px/600** — “목적지에 이미 매달 90만원을 다 나눴어요 · 지금도 매달 57만원이 모자라요”
          `font-size:12.5px font-weight:600 line-height:1.45 color:#101828`
        - `span`
          `font-size:11px line-height:1.45 color:#3B4E8F`
    - `div` **Card(18)**
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px 8px`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:8px`
        - `div`
          `display:flex align-items:baseline gap:7px`
        - `span` **text 12.5px/600** — “보유 추가 ›”
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
