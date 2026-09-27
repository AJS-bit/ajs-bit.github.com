# GoalDesign — 블록 개요

원본 `canvas/GoalDesign.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div`
  `width:390px height:1231px background:#EDF0F7 color:#101828 display:flex flex-direction:column`
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
      - `div`
        `margin-top:13px padding:13px background:#F1EAFD border-radius:14px`
        - `div`
          `display:flex align-items:flex-end justify-content:space-between gap:10px`
        - `div` **text 11.5px/400** — “다른 목적지에 이미 매달 90만원을 다 나눴어요 · 지금도 매달 57만원이 모자라요. 저장하면 기존 목적지 몫이 줄”
          `font-size:11.5px line-height:1.5 color:#4E2496 margin-top:6px`
      - `div`
        `margin-top:12px`
      - `div`
        `margin-top:12px`
        - `div` **text 13px/700** — “저장하면 이렇게 바뀌어요”
          `font-size:13px font-weight:700 color:#101828`
        - `div`
          `display:flex flex-direction:column gap:4px margin-top:6px font-size:12px line-height:1.5 color:#475467`
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
