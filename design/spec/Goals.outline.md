# Goals — 블록 개요

원본 `canvas/Goals.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div` **화면프레임**
  `width:390px height:844px background:#EDF0F7 color:#101828 display:flex flex-direction:column`
  - `div`
    `display:flex flex-direction:column gap:10px padding:14px 16px 12px`
    - `div`
      `display:flex align-items:center justify-content:space-between gap:8px`
      - `div`
        `display:flex align-items:baseline gap:8px`
        - `h1` **text 21px/700** — “목적지”
          `font-size:21px font-weight:700 letter-spacing:-0.03em line-height:1.2 color:#101828`
        - `span` **text 12px/500** — “4개 진행 중”
          `font-size:12px font-weight:500 color:#626D88`
      - `div`
        `display:flex align-items:center gap:2px`
        - `div`
          `width:36px height:36px border-radius:11px display:flex align-items:center justify-content:center`
        - `div`
          `width:36px height:36px border-radius:11px display:flex align-items:center justify-content:center position:relative`
    - `div`
      `display:flex gap:4px background:#E3E8F1 border-radius:12px padding:3px`
      - `div` **SegmentedItem** — “내 목적지”
        `flex:1 height:36px border-radius:9px background:#FFFFFF display:flex align-items:center justify-content:center font-size:13.5px font-weight:600 color:#101828 box-shadow:0 1px 2px rgba(16,24,40,.06)`
      - `div` **SegmentedItem** — “새 목적지 설계”
        `flex:1 height:36px border-radius:9px display:flex align-items:center justify-content:center font-size:13.5px font-weight:500 color:#5B6880`
  - `div` **본문(스크롤 영역)**
    `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
    - `div` **HeroCard**
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:15px 16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:8px`
        - `span` **text 11px/600** — “월 저축 배분”
          `font-size:11px font-weight:600 letter-spacing:0.07em color:#626D88`
        - `span` **text 12.5px/600** — “배분 조정 ›”
          `font-size:12.5px font-weight:600 color:#3556E6`
      - `div`
        `display:flex align-items:flex-end justify-content:space-between gap:10px margin-top:7px`
        - `div`
          `display:flex align-items:baseline gap:2px`
        - `span` — “모두 도착하려면”
          `font-size:12.5px font-weight:500 color:#626D88`
      - `div` **ProgressTrack**
        `position:relative height:9px border-radius:99px background:#E8ECF5 margin-top:11px`
        - `div`
          `position:absolute inset:0 54.3% 0 0 border-radius:99px background:linear-gradient(90deg, #3556E6 0%, #7A3FE4 100%)`
      - `div` **Callout(warn)**
        `display:flex gap:8px margin-top:11px padding:10px 11px background:#FDF1E0 border-radius:12px`
        - `span` — “월 이 부족해요. 기한을 늦추거나 우선순위가 낮은 목적지의 배분을 줄여보세요.”
          `font-size:12.5px line-height:1.45 color:#7A3E0A`
    - `div` **Card(18)**
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px 8px`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:8px`
        - `span` **text 14px/600** — “진행 중인 목적지”
          `font-size:14px font-weight:600 color:#101828`
        - `span` — “우선순위 순”
          `display:inline-flex align-items:center gap:4px font-size:12px font-weight:500 color:#5B6880`
      - `div`
        `display:flex align-items:center gap:11px padding:11px 0 border-top:1px solid #F3F5FA`
        - `div`
          `width:44px height:44px border-radius:99px background:conic-gradient(#38bdf8 0% 68%, #E8ECF5 68% 100%) display:flex align-items:center justify-content:center`
        - `div`
          `flex:1`
        - `div` — “적립”
          `display:inline-flex align-items:center gap:3px height:32px padding:0 10px border-radius:9px background:#E4F2FB color:#0A72AC font-size:12.5px font-weight:600`
      - `div`
        `display:flex align-items:center gap:11px padding:11px 0 border-top:1px solid #F3F5FA`
        - `div`
          `width:44px height:44px border-radius:99px background:conic-gradient(#7A3FE4 0% 42%, #E8ECF5 42% 100%) display:flex align-items:center justify-content:center`
        - `div`
          `flex:1`
        - `div` — “적립”
          `display:inline-flex align-items:center gap:3px height:32px padding:0 10px border-radius:9px background:#F1EAFD color:#6B32D6 font-size:12.5px font-weight:600`
      - `div`
        `display:flex align-items:center gap:11px padding:11px 0 border-top:1px solid #F3F5FA`
        - `div`
          `width:44px height:44px border-radius:99px background:conic-gradient(#B45309 0% 31%, #E8ECF5 31% 100%) display:flex align-items:center justify-content:center`
        - `div`
          `flex:1`
      - `div`
        `display:flex align-items:center gap:11px padding:11px 0 border-top:1px solid #F3F5FA`
        - `div`
          `width:44px height:44px border-radius:99px background:conic-gradient(#3556E6 0% 47%, #E8ECF5 47% 100%) display:flex align-items:center justify-content:center`
        - `div`
          `flex:1`
    - `div` — “목적지 추가”
      `display:flex align-items:center justify-content:center gap:6px height:46px border-radius:14px border:1.5px dashed #B9C3D6 background:rgba(255,255,255,.55) color:#3556E6 font-size:14px font-weight:600`
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
      - `span` **text 11px/600** — “목표”
        `font-size:11px font-weight:600 color:#3556E6`
    - `div`
      `display:flex flex-direction:column align-items:center gap:3px flex:1`
      - `div`
        `width:40px height:24px display:flex align-items:center justify-content:center`
      - `span` **text 11px/500** — “미래”
        `font-size:11px font-weight:500 color:#606B7D`
