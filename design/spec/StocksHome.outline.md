# StocksHome — 블록 개요

원본 `canvas/StocksHome.dc.html`. 값이 다르면 **원본이 맞습니다.**

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
        - `span` **text 12px/500** — “기준일 9/4”
          `font-size:12px font-weight:500 color:#626D88`
      - `div`
        `display:flex align-items:center gap:2px`
        - `div`
          `width:36px height:36px border-radius:11px display:flex align-items:center justify-content:center`
        - `div`
          `width:36px height:36px border-radius:11px display:flex align-items:center justify-content:center position:relative`
    - `div`
      `display:flex gap:4px background:#E3E8F1 border-radius:12px padding:3px`
      - `div` **SegmentedItem** — “둘러보기”
        `flex:1 height:36px border-radius:9px background:#FFFFFF display:flex align-items:center justify-content:center font-size:13.5px font-weight:600 color:#101828 box-shadow:0 1px 2px rgba(16,24,40,.06)`
      - `div` **SegmentedItem** — “내 종목”
        `flex:1 height:36px border-radius:9px display:flex align-items:center justify-content:center font-size:13.5px font-weight:500 color:#5B6880`
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
    - `div` **Callout(warn)**
      `display:flex align-items:center gap:8px padding:9px 12px background:#FDF1E0 border-radius:12px`
      - `span` **text 12px/400** — “비상금이 68%예요. 투자보다 비상금을 먼저 채우는 걸 권해요.”
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
      `display:grid grid-template-columns:repeat(2, minmax(0, 1fr)) gap:10px`
      - `div` **Card(18)**
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 13px 12px display:flex flex-direction:column gap:9px`
        - `div`
          `display:flex align-items:center justify-content:space-between gap:6px`
        - `div`
          `display:flex flex-direction:column gap:2px`
        - `div`
          `display:flex flex-wrap:wrap gap:4px`
      - `div` **Card(18)**
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 13px 12px display:flex flex-direction:column gap:9px`
        - `div`
          `display:flex align-items:center justify-content:space-between gap:6px`
        - `div`
          `display:flex flex-direction:column gap:2px`
        - `div`
          `display:flex flex-wrap:wrap gap:4px`
      - `div` **Card(18)**
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 13px 12px display:flex flex-direction:column gap:9px`
        - `div`
          `display:flex align-items:center justify-content:space-between gap:6px`
        - `div`
          `display:flex flex-direction:column gap:2px`
        - `div`
          `display:flex flex-wrap:wrap gap:4px`
      - `div` **Card(18)**
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 13px 12px display:flex flex-direction:column gap:9px`
        - `div`
          `display:flex align-items:center justify-content:space-between gap:6px`
        - `div`
          `display:flex flex-direction:column gap:2px`
        - `div`
          `display:flex flex-wrap:wrap gap:4px`
    - `p` — “데이터 기준일 2026-09-04 종가 · 설정에서 새로 받기 기준에 맞는 종목을 보여주는 것이지 투자 권유가 아니”
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
