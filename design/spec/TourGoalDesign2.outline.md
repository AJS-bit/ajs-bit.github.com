# TourGoalDesign2 — 블록 개요

원본 `canvas/TourGoalDesign2.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div` **화면프레임**
  `width:390px height:844px background:#EDF0F7 color:#101828 display:flex flex-direction:column position:relative`
  - `div`
    `display:flex flex-direction:column gap:10px padding:14px 16px 12px`
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
        `flex:1 height:36px border-radius:9px display:flex align-items:center justify-content:center font-size:13.5px font-weight:500 color:#5B6880`
      - `div` **SegmentedItem** — “새 목적지 설계”
        `flex:1 height:36px border-radius:9px background:#FFFFFF display:flex align-items:center justify-content:center font-size:13.5px font-weight:600 color:#101828 box-shadow:0 1px 2px rgba(16,24,40,.06)`
  - `div` **본문(스크롤 영역)**
    `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
    - `div` **Card(18)**
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 14px`
      - `div` **text 11px/600** — “추천 목적지에서 시작”
        `font-size:11px font-weight:600 letter-spacing:0.07em color:#626D88`
      - `div`
        `display:flex gap:8px margin-top:9px`
        - `div`
          `flex:0 0 120px width:120px min-height:126px padding:11px 10px border-radius:14px border:1px solid #E3E8F1 background:#FFFFFF`
        - `div`
          `flex:0 0 120px width:120px min-height:126px padding:11px 10px border-radius:14px border:1px solid #E3E8F1 background:#FFFFFF`
        - `div`
          `flex:0 0 120px width:120px min-height:126px padding:11px 10px border-radius:14px border:1px solid #E3E8F1 background:#FFFFFF`
        - `div`
          `flex:0 0 120px width:120px min-height:126px padding:11px 10px border-radius:14px border:1px solid #E3E8F1 background:#FFFFFF`
    - `div` **HeroCard**
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:15px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
      - `div`
        `display:flex gap:10px align-items:flex-start`
        - `div`
          `flex:1`
        - `div`
          `width:124px`
      - `div`
        `display:flex gap:10px margin-top:12px align-items:flex-start`
        - `div`
          `flex:1`
        - `div`
          `flex:1`
        - `div`
          `flex:1`
      - `div` **text 11.5px/400** — “수익률을 비워 두면 일반 저축(수익률 0%)으로 계산해요.”
        `font-size:11.5px line-height:1.45 color:#626D88 margin-top:10px`
      - `div` **text 12px/400** — “목표액과 기간을 넣으면 매달 필요한 돈을 계산해요.”
        `margin-top:10px font-size:12px line-height:1.45 color:#626D88`
      - `div`
        `margin-top:14px`
        - `div` **text 15px/600** — “목적지로 저장”
          `display:flex align-items:center justify-content:center gap:6px height:46px width:100% border-radius:13px background:#3556E6 border:none color:#FFFFFF font-size:15px font-weight:600`
    - `div` **Card(18)**
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:15px 14px`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:8px`
        - `span` **text 13.5px/500** — “다른 금액으로 계산해 보기 · 계산 기준”
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
      `position:absolute left:14px top:127px width:362px height:180px border-radius:18px box-shadow:0 0 0 2px rgba(255,255,255,.95), 0 0 0 4px #3556E6, 0 0 0 9999px rgba(16,24,40,.62)`
    - `div`
      `position:absolute left:44px top:313px width:13px height:13px background:#FFFFFF border-left:1px solid #E3E8F1 border-top:1px solid #E3E8F1 transform:rotate(45deg)`
    - `div` **Card(18)**
      `position:absolute left:14px top:319px width:362px background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:16px box-shadow:0 12px 32px -12px rgba(16,24,40,.45) font-size:13px line-height:1.55 color:#101828`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:8px flex-wrap:wrap font-size:11.5px font-weight:600 color:#626D88`
        - `span` — “처음 안내”
          `display:inline-flex align-items:center gap:5px min-height:22px padding:2px 9px border-radius:99px background:#E9EDFD color:#3556E6 font-weight:700 letter-spacing:0.02em white-space:nowrap`
        - `span` — “새 목적지 설계 2 / 3”
          `white-space:nowrap`
      - `div` **text 16px/700** — “추천에서 시작해도 돼요”
        `margin-top:8px font-size:16px font-weight:700 letter-spacing:-0.02em line-height:1.35 color:#101828`
      - `div` **text 13px/400** — “추천 카드를 누르면 이름 · 목표액 · 목표일이 채워져요. 골라서 고치기만 하면 돼요.”
        `margin-top:8px font-size:13px line-height:1.55 color:#475467`
      - `div`
        `display:flex align-items:center justify-content:space-between flex-wrap:wrap gap:4px 8px margin-top:14px`
        - `div`
          `display:flex align-items:center flex-wrap:wrap gap:0 12px`
        - `span` **text 14px/600** — “다음”
          `display:inline-flex align-items:center justify-content:center min-height:40px padding:8px 20px border-radius:12px background:#3556E6 color:#FFFFFF font-size:14px font-weight:600 line-height:1.4 white-space:nowrap`
