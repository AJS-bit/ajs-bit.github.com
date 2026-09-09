# Limits — 블록 개요

원본 `canvas/Limits.dc.html`. 값이 다르면 **원본이 맞습니다.**

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
        `flex:1 height:36px border-radius:9px display:flex align-items:center justify-content:center font-size:13.5px font-weight:500 color:#5B6880`
      - `div` **SegmentedItem** — “한도”
        `flex:1 height:36px border-radius:9px background:#FFFFFF display:flex align-items:center justify-content:center font-size:13.5px font-weight:600 color:#101828 box-shadow:0 1px 2px rgba(16,24,40,.06)`
  - `div` **본문(스크롤 영역)**
    `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
    - `div` **HeroCard**
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:8px`
        - `span` **text 11px/600** — “이번 달 총한도”
          `font-size:11px font-weight:600 letter-spacing:0.07em color:#626D88`
        - `span` **StatusPill** — “자동 계산”
          `display:inline-flex align-items:center gap:4px background:#E9EDFD color:#3556E6 font-size:11.5px font-weight:600 border-radius:99px padding:4px 9px`
      - `div`
        `display:flex align-items:flex-end justify-content:space-between gap:10px margin-top:6px`
        - `div`
          `display:flex align-items:baseline gap:2px`
        - `div`
          `display:flex flex-direction:column align-items:flex-end gap:1px`
      - `div` **ProgressTrack**
        `position:relative height:10px border-radius:99px background:#E8ECF5 margin-top:13px`
        - `div`
          `position:absolute inset:0 48.1% 0 0 border-radius:99px background:linear-gradient(90deg, #3556E6 0%, #6E6BEE 100%)`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:8px margin-top:7px`
        - `span` **text 11.5px/400** — “사용 112만원 · 52%”
          `font-size:11.5px color:#626D88`
        - `span` **text 11.5px/400** — “22일 남음 · 하루 47,270원”
          `font-size:11.5px color:#626D88`
      - `div` — “총한도 조정”
        `display:flex align-items:center justify-content:center gap:6px height:44px margin-top:13px border-radius:12px background:#FFFFFF border:1.5px solid #3556E6 color:#3556E6 font-size:14px font-weight:600`
    - `div` **Card(18)**
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:8px`
        - `div`
          `display:flex align-items:baseline gap:7px`
        - `div` — “배분 편집”
          `display:inline-flex align-items:center gap:4px height:30px padding:0 11px border-radius:9px background:#E9EDFD color:#3556E6 font-size:12.5px font-weight:600`
      - `div`
        `display:flex flex-direction:column margin-top:6px`
        - `div`
          `display:flex align-items:center gap:10px height:44px border-bottom:1px solid #F3F5FA`
        - `div`
          `display:flex align-items:center gap:10px height:44px border-bottom:1px solid #F3F5FA`
        - `div`
          `display:flex align-items:center gap:10px height:44px border-bottom:1px solid #F3F5FA`
        - `div`
          `display:flex align-items:center gap:10px height:44px border-bottom:1px solid #F3F5FA`
        - `div`
          `display:flex align-items:center gap:10px height:44px border-bottom:1px solid #F3F5FA`
        - `div`
          `display:flex align-items:center gap:10px height:44px`
      - `div` — “나머지 7개 카테고리 보기”
        `display:flex align-items:center justify-content:center gap:5px height:38px margin-top:6px border-top:1px solid #F3F5FA font-size:12.5px font-weight:600 color:#5B6880`
    - `div`
      `display:flex align-items:center justify-content:space-between gap:8px background:#FFFFFF border:1px solid #E3E8F1 border-radius:14px padding:0 14px height:50px`
      - `div`
        `display:flex align-items:center gap:8px`
        - `span` **text 13.5px/500** — “이 한도는 어떻게 계산했나요?”
          `font-size:13.5px font-weight:500 color:#475467`
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
