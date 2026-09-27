# TourGoals3 — 블록 개요

원본 `canvas/TourGoals3.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div` **화면프레임**
  `width:390px height:844px background:#EDF0F7 color:#101828 display:flex flex-direction:column position:relative`
  - `div`
    `margin-top:-186px display:flex flex-direction:column gap:10px padding:14px 16px 12px`
    - `div`
      `display:flex align-items:flex-start justify-content:space-between gap:8px`
      - `div`
        `display:flex align-items:center gap:4px min-height:36px`
        - `h1` **text 21px/700** — “목적지”
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
        - `span` **text 11px/600** — “매달 모으는 돈”
          `font-size:11px font-weight:600 letter-spacing:0.07em color:#626D88`
        - `span` **text 12.5px/600** — “매달 모으는 돈 바꿔 보기 ›”
          `font-size:12.5px font-weight:600 color:#3556E6 white-space:nowrap`
      - `div`
        `display:flex align-items:flex-end justify-content:space-between gap:10px margin-top:7px`
        - `div`
          `display:flex align-items:baseline gap:2px`
        - `span` — “모두 도착하려면”
          `font-size:12.5px font-weight:500 color:#626D88 white-space:nowrap`
      - `div` — “월급 + 부수입 390만 − 월말 예상 소비 208만 − 대출상환 92만 =”
        `font-size:11.5px line-height:1.5 color:#475467 margin-top:6px letter-spacing:-0.02em white-space:nowrap`
        - `span` — “90만원”
          `white-space:nowrap`
      - `div` **text 11.5px/400** — “홈의 '월말 예상 여유 8만원'은 소비 목표(월급의 60%)에서 월말 예상 소비를 뺀 돈이라 이 금액과 달라요.”
        `font-size:11.5px line-height:1.5 color:#626D88 margin-top:4px`
      - `div` **ProgressTrack**
        `position:relative height:9px border-radius:99px background:#E8ECF5 margin-top:11px`
        - `div`
          `position:absolute inset:0 38.4% 0 0 border-radius:99px background:linear-gradient(90deg, #3556E6 0%, #7A3FE4 100%)`
      - `div` **Callout(warn)**
        `margin-top:11px padding:10px 11px 11px background:#FDF1E0 border-radius:12px`
        - `div`
          `display:flex gap:8px`
        - `div`
          `display:flex gap:8px flex-wrap:wrap margin-top:9px`
    - `div` **Card(18)**
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px 8px`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:8px`
        - `span` **text 14px/600** — “진행 중인 목적지”
          `font-size:14px font-weight:600 color:#101828`
        - `span` **text 12px/500** — “우선순위 순으로 보여요”
          `font-size:12px font-weight:500 color:#626D88`
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
      - `span` **text 11px/600** — “목적지”
        `font-size:11px font-weight:600 color:#3556E6`
    - `div`
      `display:flex flex-direction:column align-items:center gap:3px flex:1`
      - `div`
        `width:40px height:24px display:flex align-items:center justify-content:center`
      - `span` **text 11px/500** — “미래”
        `font-size:11px font-weight:500 color:#606B7D`
  - `div`
    `position:absolute left:0 top:0 width:390px height:778px`
    - `div`
      `position:absolute left:14px top:670px width:362px height:46px border-radius:14px box-shadow:0 0 0 2px rgba(255,255,255,.95), 0 0 0 4px #3556E6, 0 0 0 9999px rgba(16,24,40,.62)`
    - `div`
      `position:absolute left:44px top:651px width:13px height:13px background:#FFFFFF border-left:1px solid #E3E8F1 border-top:1px solid #E3E8F1 transform:rotate(225deg)`
    - `div` **Card(18)**
      `position:absolute left:14px bottom:120px width:362px background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:16px box-shadow:0 12px 32px -12px rgba(16,24,40,.45) font-size:13px line-height:1.55 color:#101828`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:8px flex-wrap:wrap font-size:11.5px font-weight:600 color:#626D88`
        - `span` — “처음 안내”
          `display:inline-flex align-items:center gap:5px min-height:22px padding:2px 9px border-radius:99px background:#E9EDFD color:#3556E6 font-weight:700 letter-spacing:0.02em white-space:nowrap`
        - `span` — “목적지 3 / 3”
          `white-space:nowrap`
      - `div` **text 16px/700** — “목적지를 정해 보세요”
        `margin-top:8px font-size:16px font-weight:700 letter-spacing:-0.02em line-height:1.35 color:#101828`
      - `div` **text 13px/400** — “비상금 · 여행 · 전세금처럼 돈을 모으는 목적지예요. 새 목적지 설계 탭에서는 매달 필요한 돈을 먼저 계산해 볼 ”
        `margin-top:8px font-size:13px line-height:1.55 color:#475467`
      - `div`
        `display:flex align-items:center justify-content:space-between flex-wrap:wrap gap:4px 8px margin-top:14px`
        - `div`
          `display:flex align-items:center flex-wrap:wrap gap:0 12px`
        - `span` **text 14px/600** — “알겠어요”
          `display:inline-flex align-items:center justify-content:center min-height:40px padding:8px 20px border-radius:12px background:#3556E6 color:#FFFFFF font-size:14px font-weight:600 line-height:1.4 white-space:nowrap`
