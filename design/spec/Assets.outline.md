# Assets — 블록 개요

원본 `canvas/Assets.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div` **화면프레임**
  `width:390px height:844px background:#EDF0F7 color:#101828 display:flex flex-direction:column`
  - `div`
    `display:flex flex-direction:column gap:10px padding:14px 16px 12px`
    - `div`
      `display:flex align-items:center justify-content:space-between gap:8px`
      - `div`
        `display:flex align-items:baseline gap:8px`
        - `h1` **text 21px/700** — “자산”
          `font-size:21px font-weight:700 letter-spacing:-0.03em line-height:1.2 color:#101828`
        - `span` **text 12px/500** — “가진 것과 갚을 것”
          `font-size:12px font-weight:500 color:#626D88`
      - `div`
        `display:flex align-items:center gap:2px`
        - `div`
          `width:36px height:36px border-radius:11px display:flex align-items:center justify-content:center`
        - `div`
          `width:36px height:36px border-radius:11px display:flex align-items:center justify-content:center position:relative`
    - `div`
      `display:flex gap:4px background:#E3E8F1 border-radius:12px padding:3px`
      - `div` **SegmentedItem** — “자산 구성”
        `flex:1 height:36px border-radius:9px background:#FFFFFF display:flex align-items:center justify-content:center font-size:13.5px font-weight:600 color:#101828 box-shadow:0 1px 2px rgba(16,24,40,.06)`
      - `div` **SegmentedItem** — “부채”
        `flex:1 height:36px border-radius:9px display:flex align-items:center justify-content:center font-size:13.5px font-weight:500 color:#5B6880`
      - `div` **SegmentedItem** — “상환 전략”
        `flex:1 height:36px border-radius:9px display:flex align-items:center justify-content:center font-size:13.5px font-weight:500 color:#5B6880`
  - `div` **본문(스크롤 영역)**
    `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
    - `div` **HeroCard**
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:8px`
        - `span` **text 11px/600** — “순자산”
          `font-size:11px font-weight:600 letter-spacing:0.07em color:#626D88`
        - `span` — “6개월 420만원”
          `display:inline-flex align-items:center gap:3px font-size:12px font-weight:600 color:#0F7B47`
      - `div`
        `display:flex align-items:baseline gap:2px margin-top:6px`
        - `span` **text 38px/700** — “9,350”
          `font-size:38px font-weight:700 letter-spacing:-0.04em line-height:1.05 color:#101828`
        - `span` **text 19px/600** — “만원”
          `font-size:19px font-weight:600 color:#475467`
      - `div`
        `margin-top:12px`
        - `div`
          `display:flex align-items:center justify-content:space-between margin-top:2px`
      - `div`
        `margin-top:14px border-top:1px solid #EFF2F8`
        - `div`
          `display:flex align-items:baseline justify-content:space-between gap:8px`
        - `div` **ProgressTrack**
          `display:flex height:9px border-radius:99px margin-top:8px background:#E8ECF5`
        - `div`
          `display:flex align-items:center justify-content:space-between margin-top:7px`
    - `div`
      `display:flex gap:8px`
      - `div`
        `flex:1 background:#FFFFFF border:1px solid #E3E8F1 border-radius:14px padding:11px 12px`
        - `div` **text 11.5px/500** — “현금성 비상금”
          `font-size:11.5px font-weight:500 color:#626D88`
        - `div`
          `display:flex align-items:baseline gap:4px margin-top:3px`
      - `div`
        `flex:1 background:#FFFFFF border:1px solid #E3E8F1 border-radius:14px padding:11px 12px`
        - `div` **text 11.5px/500** — “현금+투자자산”
          `font-size:11.5px font-weight:500 color:#626D88`
        - `div`
          `display:flex align-items:baseline gap:4px margin-top:3px`
    - `div` **Card(18)**
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:8px`
        - `div`
          `display:flex align-items:baseline gap:7px`
        - `div` — “추가”
          `display:inline-flex align-items:center gap:4px height:30px padding:0 11px border-radius:9px background:#E9EDFD color:#3556E6 font-size:12.5px font-weight:600`
      - `div` **ProgressTrack**
        `display:flex height:10px border-radius:99px margin-top:12px gap:2px`
        - `div`
          `width:52.2% background:#f59e0b`
        - `div`
          `width:26.8% background:#5b8dff`
        - `div`
          `width:10.2% background:#8b5cf6`
        - `div`
          `width:8.0% background:#38bdf8`
        - `div`
          `width:2.8% background:#64748b`
      - `div`
        `display:flex flex-direction:column margin-top:6px`
        - `div`
          `display:flex align-items:center gap:9px height:44px border-bottom:1px solid #EFF2F8`
        - `div`
          `display:flex align-items:center gap:9px height:44px border-bottom:1px solid #EFF2F8`
        - `div`
          `display:flex align-items:center gap:9px height:44px border-bottom:1px solid #EFF2F8`
        - `div`
          `display:flex align-items:center gap:9px height:44px border-bottom:1px solid #EFF2F8`
        - `div`
          `display:flex align-items:center gap:9px height:44px`
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
        `width:40px height:24px border-radius:99px background:#E9EDFD display:flex align-items:center justify-content:center`
      - `span` **text 11px/600** — “자산”
        `font-size:11px font-weight:600 color:#3556E6`
    - `div`
      `display:flex flex-direction:column align-items:center gap:3px flex:1`
      - `div`
        `width:40px height:24px display:flex align-items:center justify-content:center`
      - `span` **text 11px/500** — “소비”
        `font-size:11px font-weight:500 color:#606B7D`
    - `div`
      `display:flex flex-direction:column align-items:center gap:3px flex:1`
      - `div`
        `width:40px height:24px display:flex align-items:center justify-content:center`
      - `span` **text 11px/500** — “목표”
        `font-size:11px font-weight:500 color:#606B7D`
    - `div`
      `display:flex flex-direction:column align-items:center gap:3px flex:1`
      - `div`
        `width:40px height:24px display:flex align-items:center justify-content:center`
      - `span` **text 11px/500** — “미래”
        `font-size:11px font-weight:500 color:#606B7D`
