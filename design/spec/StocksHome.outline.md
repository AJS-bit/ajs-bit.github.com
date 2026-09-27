# StocksHome — 블록 개요

원본 `canvas/StocksHome.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div` **화면프레임**
  `width:390px height:844px background:#EDF0F7 color:#101828 display:flex flex-direction:column`
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
    - `div`
      `display:flex gap:4px background:#E3E8F1 border-radius:12px padding:3px`
      - `div` **SegmentedItem** — “둘러보기”
        `flex:1 height:36px border-radius:9px background:#FFFFFF display:flex align-items:center justify-content:center font-size:13.5px font-weight:600 color:#101828 box-shadow:0 1px 2px rgba(16,24,40,.06)`
      - `div` **SegmentedItem** — “내 종목”
        `flex:1 height:36px border-radius:9px display:flex align-items:center justify-content:center font-size:13.5px font-weight:500 color:#5B6880`
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
    - `div` **Callout(warn)**
      `display:flex align-items:center gap:8px padding:9px 12px background:#FDF1E0 border-radius:12px`
      - `span`
        `display:inline-flex`
      - `span` **text 12px/400** — “비상금 6개월 목적지가 68%예요 · 비상금을 먼저 채워 보세요”
        `flex:1 font-size:12px line-height:1.4 color:#7A3E0A`
      - `span` **text 12px/600** — “목적지 보기 ›”
        `font-size:12px font-weight:600 color:#B45309 white-space:nowrap`
    - `div` **Card(18)**
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:4px 14px`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:10px height:46px`
        - `div`
          `display:flex flex-direction:column gap:2px`
        - `div`
          `display:flex align-items:center gap:8px`
    - `div`
      `display:grid grid-template-columns:repeat(2, minmax(0, 1fr)) gap:10px align-items:start`
      - `div` **Card(18)**
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 12px 12px display:flex flex-direction:column gap:9px`
        - `div`
          `display:flex align-items:center gap:8px`
        - `div`
          `display:flex flex-wrap:wrap gap:4px`
      - `div` **Card(18)**
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 12px 12px display:flex flex-direction:column gap:9px`
        - `div`
          `display:flex align-items:center gap:8px`
        - `div`
          `display:flex flex-wrap:wrap gap:4px`
      - `div` **Card(18)**
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 12px 12px display:flex flex-direction:column gap:9px`
        - `div`
          `display:flex align-items:center gap:8px`
        - `div`
          `display:flex flex-wrap:wrap gap:4px`
      - `div` **Card(18)**
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 12px 12px display:flex flex-direction:column gap:9px`
        - `div`
          `display:flex align-items:center gap:8px`
        - `div`
          `display:flex flex-wrap:wrap gap:4px`
    - `p` — “데이터 기준일 2026년 9월 4일 종가 · 설정 › 주식에서 새로 받기 기준에 맞는 종목을 보여주는 것이지 투자 ”
      `font-size:11px line-height:1.5 color:#626D88`
      - `br`
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
