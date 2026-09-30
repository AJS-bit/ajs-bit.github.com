# HomeTargetSaved — 블록 개요

원본 `canvas/HomeTargetSaved.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div`
  `width:390px height:1510px background:#EDF0F7 color:#101828 display:flex flex-direction:column position:relative`
  - `div` **Header**
    `display:flex flex-direction:column gap:6px padding:12px 16px 10px`
    - `div`
      `display:flex align-items:flex-start justify-content:space-between gap:8px`
      - `div`
        `display:flex align-items:center gap:8px height:36px`
        - `div`
          `width:32px height:32px border-radius:10px background:linear-gradient(140deg, #3556E6 0%, #7A3FE4 100%) display:flex align-items:center justify-content:center`
        - `span` **text 15px/700** — “NAVI”
          `font-size:15px font-weight:700 letter-spacing:0.06em color:#101828`
      - `div`
        `display:flex align-items:flex-start gap:0`
        - `div`
          `width:44px display:flex flex-direction:column align-items:center`
        - `div`
          `width:44px display:flex flex-direction:column align-items:center`
        - `div`
          `width:44px display:flex flex-direction:column align-items:center`
    - `div`
      `display:flex align-items:baseline justify-content:space-between gap:8px`
      - `h1` **text 21px/700** — “오늘의 내비게이션”
        `font-size:21px font-weight:700 letter-spacing:-0.03em line-height:1.25 color:#101828 white-space:nowrap`
      - `span` **text 12px/500** — “9월 8일 · 오늘 포함 23일 남음”
        `font-size:12px font-weight:500 color:#626D88 white-space:nowrap`
  - `div` **본문(스크롤 영역)**
    `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px 14px`
    - `div` **HeroCard**
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:8px min-height:28px`
        - `span` **text 11px/600** — “이번 달 소비”
          `font-size:11px font-weight:600 letter-spacing:0.07em color:#626D88 white-space:nowrap`
        - `div`
          `display:flex align-items:center justify-content:flex-end gap:6px`
      - `div`
        `display:flex align-items:flex-end justify-content:space-between gap:10px margin-top:8px`
        - `div`
          `display:flex align-items:baseline gap:2px`
        - `div`
          `display:flex flex-direction:column align-items:flex-end gap:1px`
      - `div`
        `display:flex align-items:baseline justify-content:space-between gap:10px margin-top:5px`
        - `span` **text 13px/500** — “월급 360만원 중 112만원 썼어요”
          `font-size:13px font-weight:500 color:#475467`
        - `span`
          `display:inline-flex align-items:baseline gap:4px`
      - `div`
        `margin-top:15px`
        - `div` **ProgressTrack**
          `position:relative height:10px border-radius:99px background:#E8ECF5`
        - `div`
          `position:relative height:15px margin-top:5px`
      - `div`
        `display:grid grid-template-columns:repeat(3, minmax(0, 1fr)) gap:0 margin-top:14px border-top:1px solid #EFF2F8`
        - `div`
          `display:flex flex-direction:column gap:3px`
        - `div`
          `display:flex flex-direction:column gap:3px padding:0 10px border-left:1px solid #EFF2F8`
        - `div`
          `display:flex flex-direction:column gap:3px border-left:1px solid #EFF2F8`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:10px margin-top:12px`
        - `span` — “기준 · 저축 이체와 대출 갚은 돈은 쓴 돈에 넣지 않아요”
          `font-size:11px line-height:1.4 color:#626D88`
        - `span` — “월급 · 부수입 고치기”
          `display:inline-flex align-items:center font-size:11.5px font-weight:600 color:#3556E6 white-space:nowrap`
      - `p` **text 11px/400** — “카테고리 없는 32,000원은 적은 금액 그대로 예상에 더했어요”
        `font-size:11px line-height:1.4 color:#626D88`
      - `p` **text 11px/400** — “지난 고정비 기록을 보고 앞으로 나갈 돈도 예상했어요”
        `font-size:11px line-height:1.4 color:#626D88`
    - `div` **Card(18)**
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 14px 13px`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:6px min-height:32px`
        - `div`
          `display:flex align-items:center gap:4px`
        - `div`
          `display:flex align-items:center gap:6px`
      - `div` **text 12px/400** — “날짜를 누르면 그날 쓴 돈을 적어요”
        `font-size:12px line-height:1.45 color:#626D88 margin-top:6px`
      - `div`
        `display:grid grid-template-columns:repeat(7, minmax(0, 1fr)) margin-top:8px`
        - `span` **text 11px/500** — “일”
          `text-align:center font-size:11px font-weight:500 color:#626D88`
        - `span` **text 11px/500** — “월”
          `text-align:center font-size:11px font-weight:500 color:#626D88`
        - `span` **text 11px/500** — “화”
          `text-align:center font-size:11px font-weight:500 color:#626D88`
        - `span` **text 11px/500** — “수”
          `text-align:center font-size:11px font-weight:500 color:#626D88`
        - `span` **text 11px/500** — “목”
          `text-align:center font-size:11px font-weight:500 color:#626D88`
        - `span` **text 11px/500** — “금”
          `text-align:center font-size:11px font-weight:500 color:#626D88`
        - `span` **text 11px/500** — “토”
          `text-align:center font-size:11px font-weight:500 color:#626D88`
      - `div`
        `display:flex flex-direction:column border-bottom:1px solid #EFF2F8`
        - `div`
          `display:grid grid-template-columns:repeat(7, minmax(0, 1fr)) border-top:1px solid #EFF2F8 padding:2px 0`
        - `div`
          `display:grid grid-template-columns:repeat(7, minmax(0, 1fr)) border-top:1px solid #EFF2F8 padding:2px 0`
        - `div`
          `display:grid grid-template-columns:repeat(7, minmax(0, 1fr)) border-top:1px solid #EFF2F8 padding:2px 0`
        - `div`
          `display:grid grid-template-columns:repeat(7, minmax(0, 1fr)) border-top:1px solid #EFF2F8 padding:2px 0`
        - `div`
          `display:grid grid-template-columns:repeat(7, minmax(0, 1fr)) border-top:1px solid #EFF2F8 padding:2px 0`
      - `div` — “· ·”
        `font-size:11.5px line-height:1.45 color:#626D88 margin-top:6px`
        - `span` — “기록 없음”
          `white-space:nowrap`
        - `span` — “안 썼어요”
          `white-space:nowrap`
        - `span` — “다 적었어요”
          `white-space:nowrap`
      - `div` **text 12.5px/400** — “9월 기록한 소비 1,120,000원”
        `font-size:12.5px line-height:1.5 color:#475467 margin-top:8px`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:10px min-height:40px margin-top:10px`
        - `span` **text 12.5px/400** — “오늘 4건 37,000원”
          `flex:1 font-size:12.5px line-height:1.5 color:#475467`
        - `span` **SampleBanner** — “더 적기”
          `display:inline-flex align-items:center gap:4px height:32px padding:0 12px border-radius:99px background:#E9EDFD color:#3556E6 font-size:13px font-weight:700 white-space:nowrap`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:8px min-height:32px margin-top:6px border-top:1px solid #EFF2F8`
        - `span` **text 12.5px/600** — “카테고리 없는 기록 7건 · 카테고리 고르기”
          `font-size:12.5px line-height:1.4 font-weight:600 color:#101828`
    - `div` **TurnCard**
      `display:flex gap:12px background:#FFFFFF border:1px solid #E3E8F1 border-left:3px solid #DE8A2A border-radius:18px padding:13px 14px`
      - `div`
        `width:34px height:34px border-radius:11px background:#FDF1E0 display:flex align-items:center justify-content:center`
      - `div`
        `display:flex flex-direction:column gap:3px`
        - `span` **text 11px/600** — “다음 안내”
          `font-size:11px font-weight:600 letter-spacing:0.06em color:#B45309`
        - `span` — “월말엔 소비 목표 넘어요”
          `font-size:15px font-weight:600 letter-spacing:-0.015em line-height:1.35 color:#101828`
        - `span` — “월말 예상 월급의 . 월 28만원 줄이면 소비 목표 안이에요.”
          `font-size:12.5px line-height:1.45 color:#475467`
        - `span` **text 12.5px/600** — “줄일 소비 찾기 ›”
          `font-size:12.5px font-weight:600 color:#3556E6 margin-top:5px`
    - `div` **Card(18)**
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px`
      - `div`
        `display:flex flex-wrap:wrap align-items:center justify-content:space-between gap:4px 8px`
        - `span` — “이번 달 한도”
          `font-size:13.5px font-weight:600 color:#101828 white-space:nowrap`
        - `div`
          `display:flex align-items:center gap:4px`
      - `div` **text 13px/400** — “180만원 중 112만원 썼어요”
        `font-size:13px line-height:1.45 color:#475467 margin-top:4px`
      - `div`
        `position:relative height:8px border-radius:99px background:#E8ECF5 margin-top:9px`
        - `div`
          `position:absolute inset:0 37.8% 0 0 border-radius:99px background:linear-gradient(90deg, #6E6BEE 0%, #7A3FE4 100%)`
    - `div` **Card(18)**
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:4px 14px`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:10px min-height:46px`
        - `div`
          `display:flex flex-direction:column gap:2px`
        - `div`
          `display:flex align-items:center gap:8px`
    - `div` **Card(18)**
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:4px 14px`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:10px min-height:46px`
        - `div`
          `display:flex flex-direction:column gap:2px`
        - `div`
          `display:flex align-items:center gap:8px`
  - `div` **BottomNav**
    `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`
    - `div`
      `display:flex flex-direction:column align-items:center gap:3px flex:1`
      - `div`
        `width:40px height:24px border-radius:99px background:#E9EDFD display:flex align-items:center justify-content:center`
      - `span` **text 11px/600** — “홈”
        `font-size:11px font-weight:600 color:#3556E6`
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
    `position:absolute left:14px right:14px bottom:78px background:#101828 border-radius:16px padding:13px 14px 12px color:#FFFFFF box-shadow:0 8px 24px rgba(0,0,0,.28)`
    - `div`
      `display:flex align-items:flex-start justify-content:space-between gap:8px`
      - `span`
        `display:inline-flex align-items:flex-start gap:7px font-size:14px line-height:1.45 font-weight:500`
        - `span` — “· 한도 180만원”
      - `span` **text 12px/600** — “닫기”
        `font-size:12px font-weight:600 color:rgba(255,255,255,.72) white-space:nowrap`
    - `div`
      `display:flex gap:8px margin-top:11px`
      - `span` **text 13px/700** — “되돌리기”
        `display:inline-flex align-items:center justify-content:center height:36px border-radius:10px font-size:13px white-space:nowrap padding:0 14px border:1px solid rgba(255,255,255,.55) color:#FFFFFF font-weight:700`
