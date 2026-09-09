# Ledger — 블록 개요

원본 `canvas/Ledger.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div` **화면프레임**
  `width:390px height:844px background:#EDF0F7 color:#101828 display:flex flex-direction:column`
  - `div`
    `display:flex flex-direction:column gap:10px padding:14px 16px 12px`
    - `div`
      `display:flex align-items:center justify-content:space-between gap:8px`
      - `h1` **text 21px/700** — “소비”
        `font-size:21px font-weight:700 letter-spacing:-0.03em line-height:1.2 color:#101828`
      - `div`
        `display:flex align-items:center gap:8px`
        - `div`
          `display:flex align-items:center gap:2px height:34px padding:0 4px border-radius:10px background:#FFFFFF border:1px solid #E3E8F1`
        - `div` — “거래”
          `display:inline-flex align-items:center gap:3px height:34px padding:0 11px border-radius:10px background:#3556E6 color:#FFFFFF font-size:13px font-weight:600`
    - `div`
      `display:flex gap:4px background:#E3E8F1 border-radius:12px padding:3px`
      - `div` **SegmentedItem** — “이번 달”
        `flex:1 height:36px border-radius:9px display:flex align-items:center justify-content:center font-size:13.5px font-weight:500 color:#5B6880`
      - `div` **SegmentedItem** — “내역”
        `flex:1 height:36px border-radius:9px background:#FFFFFF display:flex align-items:center justify-content:center font-size:13.5px font-weight:600 color:#101828 box-shadow:0 1px 2px rgba(16,24,40,.06)`
      - `div` **SegmentedItem** — “한도”
        `flex:1 height:36px border-radius:9px display:flex align-items:center justify-content:center font-size:13.5px font-weight:500 color:#5B6880`
  - `div` **본문(스크롤 영역)**
    `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
    - `div` **Card(18)**
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
      - `div`
        `display:flex align-items:center gap:8px`
        - `div`
          `flex:1 display:flex align-items:center gap:9px height:40px padding:0 12px border-radius:11px background:#F4F6FB`
        - `div`
          `width:40px height:40px border-radius:11px border:1px solid #E3E8F1 display:flex align-items:center justify-content:center`
      - `div`
        `display:flex gap:6px margin-top:10px`
        - `div` **SampleBanner** — “전체 32건”
          `display:inline-flex align-items:center gap:4px height:32px padding:0 12px border-radius:99px background:#E9EDFD color:#3556E6 font-size:12.5px font-weight:600`
        - `div` — “식비”
          `display:inline-flex align-items:center gap:5px height:32px padding:0 12px border-radius:99px border:1px solid #E3E8F1 color:#475467 font-size:12.5px font-weight:500`
        - `div` — “주거”
          `display:inline-flex align-items:center gap:5px height:32px padding:0 12px border-radius:99px border:1px solid #E3E8F1 color:#475467 font-size:12.5px font-weight:500`
        - `div` **text 12.5px/500** — “더보기”
          `display:inline-flex align-items:center height:32px padding:0 12px border-radius:99px border:1px solid #E3E8F1 color:#626D88 font-size:12.5px font-weight:500`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:8px margin-top:11px border-top:1px solid #EFF2F8`
        - `span` — “일반 소비”
          `font-size:12px color:#475467`
        - `span` **text 11.5px/400** — “이체 63만 · 상환 92만은 제외”
          `font-size:11.5px color:#626D88`
    - `div` **Card(18)**
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:4px 14px 10px`
      - `div`
        `display:flex align-items:baseline justify-content:space-between gap:10px padding:12px 0 6px`
        - `span` — “9월 8일”
          `font-size:13px font-weight:600 color:#101828`
        - `span` **text 12.5px/600** — “32,000원”
          `font-size:12.5px font-weight:600 color:#475467`
      - `div`
        `display:flex align-items:center gap:11px min-height:54px border-top:1px solid #F3F5FA`
        - `div`
          `width:34px height:34px border-radius:10px background:#f9731618 display:flex align-items:center justify-content:center`
        - `div`
          `flex:1`
        - `span` **text 14.5px/600** — “−32,000”
          `font-size:14.5px font-weight:600 letter-spacing:-0.02em color:#101828`
      - `div`
        `display:flex align-items:baseline justify-content:space-between gap:10px padding:12px 0 6px`
        - `span` — “9월 7일”
          `font-size:13px font-weight:600 color:#101828`
        - `span` **text 12.5px/600** — “118,400원”
          `font-size:12.5px font-weight:600 color:#475467`
      - `div`
        `display:flex align-items:center gap:11px min-height:54px border-top:1px solid #F3F5FA`
        - `div`
          `width:34px height:34px border-radius:10px background:#0ea5e918 display:flex align-items:center justify-content:center`
        - `div`
          `flex:1`
        - `span` **text 14.5px/600** — “−50,000”
          `font-size:14.5px font-weight:600 letter-spacing:-0.02em color:#101828`
      - `div`
        `display:flex align-items:center gap:11px min-height:54px border-top:1px solid #F3F5FA`
        - `div`
          `width:34px height:34px border-radius:10px background:#ec489918 display:flex align-items:center justify-content:center`
        - `div`
          `flex:1`
        - `span` **text 14.5px/600** — “−62,000”
          `font-size:14.5px font-weight:600 letter-spacing:-0.02em color:#101828`
      - `div`
        `display:flex align-items:center gap:11px min-height:54px border-top:1px solid #F3F5FA`
        - `div`
          `width:34px height:34px border-radius:10px background:#d9770618 display:flex align-items:center justify-content:center`
        - `div`
          `flex:1`
        - `span` **text 14.5px/600** — “−6,400”
          `font-size:14.5px font-weight:600 letter-spacing:-0.02em color:#101828`
      - `div`
        `display:flex align-items:baseline justify-content:space-between gap:10px padding:12px 0 6px`
        - `span` — “9월 5일”
          `font-size:13px font-weight:600 color:#101828`
        - `span` **text 12.5px/600** — “320,000원”
          `font-size:12.5px font-weight:600 color:#475467`
      - `div`
        `display:flex align-items:center gap:11px min-height:54px border-top:1px solid #F3F5FA`
        - `div`
          `width:34px height:34px border-radius:10px background:#34d17e18 display:flex align-items:center justify-content:center`
        - `div`
          `flex:1`
        - `span` **text 14.5px/600** — “−300,000”
          `font-size:14.5px font-weight:600 letter-spacing:-0.02em color:#475467`
      - `div`
        `display:flex align-items:baseline justify-content:space-between gap:10px padding:12px 0 6px`
        - `span` — “9월 3일”
          `font-size:13px font-weight:600 color:#101828`
        - `span` **text 12.5px/600** — “470,000원”
          `font-size:12.5px font-weight:600 color:#475467`
      - `div`
        `display:flex align-items:center gap:11px min-height:54px border-top:1px solid #F3F5FA`
        - `div`
          `width:34px height:34px border-radius:10px background:#8b5cf618 display:flex align-items:center justify-content:center`
        - `div`
          `flex:1`
        - `span` **text 14.5px/600** — “−470,000”
          `font-size:14.5px font-weight:600 letter-spacing:-0.02em color:#101828`
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
        `width:40px height:24px border-radius:99px background:#E9EDFD display:flex align-items:center justify-content:center`
      - `span` **text 11px/600** — “소비”
        `font-size:11px font-weight:600 color:#3556E6`
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
