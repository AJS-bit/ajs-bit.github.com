# TourSpending3 — 블록 개요

원본 `canvas/TourSpending3.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div` **화면프레임**
  `width:390px height:844px background:#EDF0F7 color:#101828 display:flex flex-direction:column position:relative`
  - `div`
    `margin-top:-151px display:flex flex-direction:column gap:10px padding:14px 16px 12px`
    - `div`
      `display:flex align-items:flex-start justify-content:space-between gap:8px`
      - `div`
        `display:flex align-items:center gap:4px min-height:36px`
        - `h1` **text 21px/700** — “소비”
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
      `display:flex align-items:center justify-content:space-between gap:8px`
      - `div`
        `display:flex align-items:center gap:2px height:34px padding:0 4px border-radius:10px background:#FFFFFF border:1px solid #E3E8F1`
        - `span` **text 13px/600** — “2026년 9월”
          `font-size:13px font-weight:600 color:#101828 padding:0 4px`
      - `div` — “기록”
        `display:inline-flex align-items:center gap:3px height:34px padding:0 11px border-radius:10px background:#3556E6 color:#FFFFFF font-size:13px font-weight:600`
    - `div`
      `display:flex gap:4px background:#E3E8F1 border-radius:12px padding:3px`
      - `div` **SegmentedItem** — “이번 달”
        `flex:1 height:36px border-radius:9px background:#FFFFFF display:flex align-items:center justify-content:center font-size:13.5px font-weight:600 color:#101828 box-shadow:0 1px 2px rgba(16,24,40,.06)`
      - `div` **SegmentedItem** — “내역”
        `flex:1 height:36px border-radius:9px display:flex align-items:center justify-content:center font-size:13.5px font-weight:500 color:#5B6880`
      - `div` **SegmentedItem** — “한도”
        `flex:1 height:36px border-radius:9px display:flex align-items:center justify-content:center font-size:13.5px font-weight:500 color:#5B6880`
  - `div` **본문(스크롤 영역)**
    `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
    - `div` **HeroCard**
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px 14px 14px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
      - `div`
        `display:flex align-items:flex-start justify-content:space-between gap:10px padding:0 2px`
        - `div`
        - `div`
          `display:flex flex-direction:column align-items:flex-end gap:5px`
      - `div`
        `display:flex align-items:baseline justify-content:space-between gap:8px margin-top:13px padding:0 2px`
        - `span` **text 13.5px/600** — “계획한 속도로 쓰고 있나요?”
          `font-size:13.5px font-weight:600 color:#101828`
        - `span` **text 12px/600** — “누적 112만원”
          `font-size:12px font-weight:600 color:#475467 white-space:nowrap`
      - `div`
        `margin-top:8px`
      - `div`
        `display:flex align-items:center gap:12px margin-top:4px padding:0 2px`
        - `span` — “실제 누적”
          `display:inline-flex align-items:center gap:5px font-size:11px color:#475467`
        - `span` — “월말 예상”
          `display:inline-flex align-items:center gap:5px font-size:11px color:#475467`
        - `span` — “계획선”
          `display:inline-flex align-items:center gap:5px font-size:11px color:#475467`
      - `p` **text 11px/400** — “계획선은 한도를 일수로 나눈 속도예요. 초반에 나가는 고정비가 있으면 실제 선이 먼저 올라갈 수 있어요.”
        `padding:0 2px font-size:11px line-height:1.45 color:#626D88`
    - `div` **Card(18)**
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:8px`
        - `div`
          `display:flex align-items:baseline gap:7px`
        - `span` **text 12px/600** — “한도 보기 ›”
          `font-size:12px font-weight:600 color:#3556E6 white-space:nowrap`
      - `div`
        `display:flex flex-direction:column margin-top:8px`
        - `div`
          `display:flex align-items:center gap:10px height:46px`
        - `div`
          `display:flex align-items:center gap:10px height:46px`
        - `div`
          `display:flex align-items:center gap:10px height:46px`
        - `div`
          `display:flex align-items:center gap:10px height:46px`
        - `div`
          `display:flex align-items:center gap:10px height:46px`
    - `div`
      `display:flex align-items:center gap:8px height:46px padding:0 14px background:#FFFFFF border:1px solid #E3E8F1 border-radius:16px`
      - `span` **text 13.5px/600** — “소비 추이·절감 기회”
        `font-size:13.5px font-weight:600 color:#101828`
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
      - `span` **text 11px/500** — “목적지”
        `font-size:11px font-weight:500 color:#606B7D`
    - `div`
      `display:flex flex-direction:column align-items:center gap:3px flex:1`
      - `div`
        `width:40px height:24px display:flex align-items:center justify-content:center`
      - `span` **text 11px/500** — “미래”
        `font-size:11px font-weight:500 color:#606B7D`
  - `div`
    `position:absolute left:0 top:0 width:390px height:778px`
    - `div`
      `position:absolute left:14px top:371px width:362px height:289px border-radius:18px box-shadow:0 0 0 2px rgba(255,255,255,.95), 0 0 0 4px #3556E6, 0 0 0 9999px rgba(16,24,40,.62)`
    - `div`
      `position:absolute left:44px top:352px width:13px height:13px background:#FFFFFF border-left:1px solid #E3E8F1 border-top:1px solid #E3E8F1 transform:rotate(225deg)`
    - `div` **Card(18)**
      `position:absolute left:14px bottom:419px width:362px background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:16px box-shadow:0 12px 32px -12px rgba(16,24,40,.45) font-size:13px line-height:1.55 color:#101828`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:8px flex-wrap:wrap font-size:11.5px font-weight:600 color:#626D88`
        - `span` — “처음 안내”
          `display:inline-flex align-items:center gap:5px min-height:22px padding:2px 9px border-radius:99px background:#E9EDFD color:#3556E6 font-weight:700 letter-spacing:0.02em white-space:nowrap`
        - `span` — “소비 3 / 3”
          `white-space:nowrap`
      - `div` **text 16px/700** — “카테고리마다 얼마 썼는지”
        `margin-top:8px font-size:16px font-weight:700 letter-spacing:-0.02em line-height:1.35 color:#101828`
      - `div` **text 13px/400** — “한도의 몇 %를 썼는지예요. 100%를 넘으면 빨갛게 보이고, 누르면 그 카테고리 내역이 열려요.”
        `margin-top:8px font-size:13px line-height:1.55 color:#475467`
      - `div`
        `display:flex align-items:center justify-content:space-between flex-wrap:wrap gap:4px 8px margin-top:14px`
        - `div`
          `display:flex align-items:center flex-wrap:wrap gap:0 12px`
        - `span` **text 14px/600** — “알겠어요”
          `display:inline-flex align-items:center justify-content:center min-height:40px padding:8px 20px border-radius:12px background:#3556E6 color:#FFFFFF font-size:14px font-weight:600 line-height:1.4 white-space:nowrap`
