# TourHome1 — 블록 개요

원본 `canvas/TourHome1.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div` **화면프레임**
  `width:390px height:844px background:#EDF0F7 color:#101828 display:flex flex-direction:column position:relative`
  - `div` **Header**
    `display:flex flex-direction:column gap:6px padding:12px 16px 10px`
    - `div`
      `display:flex align-items:center justify-content:space-between gap:8px`
      - `div`
        `display:flex align-items:center gap:8px`
        - `div`
          `width:32px height:32px border-radius:10px background:linear-gradient(140deg, #3556E6 0%, #7A3FE4 100%) display:flex align-items:center justify-content:center`
        - `span` **text 15px/700** — “NAVI”
          `font-size:15px font-weight:700 letter-spacing:0.06em color:#101828`
      - `div`
        `display:flex align-items:center gap:2px`
        - `div`
          `width:36px height:36px border-radius:11px display:flex align-items:center justify-content:center`
        - `div`
          `width:36px height:36px border-radius:11px display:flex align-items:center justify-content:center`
        - `div`
          `width:36px height:36px border-radius:11px display:flex align-items:center justify-content:center position:relative`
    - `div`
      `display:flex align-items:baseline justify-content:space-between gap:8px`
      - `h1` **text 21px/700** — “오늘의 내비게이션”
        `font-size:21px font-weight:700 letter-spacing:-0.03em line-height:1.25 color:#101828`
      - `span` **text 12px/500** — “9월 8일 · 22일 남음”
        `font-size:12px font-weight:500 color:#626D88`
  - `div` **본문(스크롤 영역)**
    `flex:1 min-height:0 display:flex flex-direction:column gap:9px padding:0 14px`
    - `div` **HeroCard**
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:8px`
        - `span` **text 11px/600** — “현재 위치”
          `font-size:11px font-weight:600 letter-spacing:0.07em color:#626D88`
        - `span` **StatusPill** — “월말에도 목표 안”
          `display:inline-flex align-items:center gap:4px background:#E4F4EA color:#0F7B47 font-size:11.5px font-weight:600 border-radius:99px padding:4px 9px`
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
          `display:inline-flex align-items:center gap:4px`
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
        - `span` **text 11px/400** — “실수령 급여 기준 · 부수입·저축 이체·대출상환 제외”
          `font-size:11px line-height:1.4 color:#626D88`
        - `span` **text 11.5px/600** — “기준 조정 ›”
          `font-size:11.5px font-weight:600 color:#3556E6 white-space:nowrap`
    - `div` **Card(18)**
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 14px 13px`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:8px`
        - `span` **text 14px/600** — “이번 달 소비 기록”
          `font-size:14px font-weight:600 color:#101828`
        - `span` — “펼치기”
          `display:inline-flex align-items:center gap:2px font-size:12px font-weight:600 color:#475467`
      - `div` **text 12px/400** — “날짜를 누르면 그날 쓴 돈을 적어요”
        `font-size:12px line-height:1.45 color:#626D88 margin-top:2px`
      - `div`
        `display:flex justify-content:space-between margin-top:10px`
        - `div`
          `width:44px height:56px border-radius:10px background:transparent display:flex flex-direction:column align-items:center justify-content:center gap:2px`
        - `div`
          `width:44px height:56px border-radius:10px background:transparent display:flex flex-direction:column align-items:center justify-content:center gap:2px`
        - `div`
          `width:44px height:56px border-radius:10px background:transparent display:flex flex-direction:column align-items:center justify-content:center gap:2px`
        - `div`
          `width:44px height:56px border-radius:10px background:transparent display:flex flex-direction:column align-items:center justify-content:center gap:2px`
        - `div`
          `width:44px height:56px border-radius:10px background:transparent display:flex flex-direction:column align-items:center justify-content:center gap:2px`
        - `div`
          `width:44px height:56px border-radius:10px background:transparent display:flex flex-direction:column align-items:center justify-content:center gap:2px`
        - `div`
          `width:44px height:56px border-radius:10px background:#E9EDFD box-shadow:inset 0 0 0 1.5px #3556E6 display:flex flex-direction:column align-items:center justify-content:center gap:2px`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:10px min-height:40px margin-top:10px`
        - `span` **text 12.5px/400** — “오늘 4건 37,000원”
          `flex:1 font-size:12.5px line-height:1.5 color:#475467`
        - `span` **SampleBanner** — “더 적기”
          `display:inline-flex align-items:center gap:4px height:32px padding:0 12px border-radius:99px background:#E9EDFD color:#3556E6 font-size:13px font-weight:700 white-space:nowrap`
      - `div`
        `display:flex align-items:center justify-content:space-between height:32px margin-top:6px border-top:1px solid #EFF2F8`
        - `span` **text 12.5px/600** — “확인할 내용 2개”
          `font-size:12.5px font-weight:600 color:#101828`
    - `div` **TurnCard**
      `display:flex gap:12px background:#FFFFFF border:1px solid #E3E8F1 border-left:3px solid #DE8A2A border-radius:18px padding:13px 14px`
      - `div`
        `width:34px height:34px border-radius:11px background:#FDF1E0 display:flex align-items:center justify-content:center`
      - `div`
        `display:flex flex-direction:column gap:3px`
        - `span` **text 11px/600** — “다음 안내”
          `font-size:11px font-weight:600 letter-spacing:0.06em color:#B45309`
        - `span` **text 15px/600** — “카드 할부 금리 14.5%부터 줄여보세요”
          `font-size:15px font-weight:600 letter-spacing:-0.015em line-height:1.35 color:#101828`
        - `span` **text 12.5px/400** — “고금리 부채는 자산이 자라는 속도를 가장 크게 낮춰요.”
          `font-size:12.5px line-height:1.45 color:#475467`
        - `span` **text 12.5px/600** — “상환 전략 보기 ›”
          `font-size:12.5px font-weight:600 color:#3556E6 margin-top:5px`
    - `div` **Card(18)**
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:8px`
        - `span` — “이번 달 한도”
          `font-size:13.5px font-weight:600 color:#101828 white-space:nowrap`
        - `div`
          `display:flex align-items:center gap:4px`
      - `div`
        `position:relative height:8px border-radius:99px background:#E8ECF5 margin-top:9px`
        - `div`
          `position:absolute inset:0 48.1% 0 0 border-radius:99px background:linear-gradient(90deg, #6E6BEE 0%, #7A3FE4 100%)`
    - `div` **Card(18)**
      `display:flex align-items:center gap:12px background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px`
      - `div`
        `width:52px height:52px border-radius:99px background:conic-gradient(#7A3FE4 0% 68%, #E8ECF5 68% 100%) display:flex align-items:center justify-content:center`
        - `div` **text 13px/700** — “68%”
          `width:40px height:40px border-radius:99px background:#FFFFFF display:flex align-items:center justify-content:center font-size:13px font-weight:700 letter-spacing:-0.02em color:#7A3FE4`
      - `div`
        `display:flex flex-direction:column gap:2px flex:1`
        - `span` **text 11px/600** — “대표 목적지”
          `font-size:11px font-weight:600 letter-spacing:0.06em color:#626D88`
        - `span` **text 15px/600** — “비상금 6개월”
          `font-size:15px font-weight:600 letter-spacing:-0.015em color:#101828`
        - `span` **text 12.5px/400** — “1,020 / 1,500만원 · 월 35만원 적립”
          `font-size:12.5px color:#475467`
        - `span` **text 11.5px/400** — “예상 도착 2027년 11월”
          `font-size:11.5px color:#626D88`
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
      - `span` **text 11px/500** — “목표”
        `font-size:11px font-weight:500 color:#606B7D`
    - `div`
      `display:flex flex-direction:column align-items:center gap:3px flex:1`
      - `div`
        `width:40px height:24px display:flex align-items:center justify-content:center`
      - `span` **text 11px/500** — “미래”
        `font-size:11px font-weight:500 color:#606B7D`
  - `div`
    `position:absolute inset:0`
    - `div` **HeroCard**
      `position:absolute left:14px top:90px width:362px height:296px border-radius:20px box-shadow:0 0 0 2px rgba(255,255,255,.95), 0 0 0 4px #3556E6, 0 0 0 9999px rgba(16,24,40,.62)`
    - `div` **Card(18)**
      `position:absolute left:14px width:362px top:398px background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:16px display:flex flex-direction:column gap:8px box-shadow:0 12px 32px -12px rgba(16,24,40,.45)`
      - `div`
        `position:absolute top:-7px left:30px width:13px height:13px background:#FFFFFF transform:rotate(45deg) border-left:1px solid #E3E8F1 border-top:1px solid #E3E8F1`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:8px`
        - `span` — “처음 안내”
          `display:inline-flex align-items:center gap:5px height:22px padding:0 9px border-radius:99px background:#E9EDFD color:#3556E6 font-size:11.5px font-weight:700 letter-spacing:0.02em`
        - `span` **text 11.5px/600** — “홈 1 / 3”
          `font-size:11.5px font-weight:600 color:#626D88 white-space:nowrap`
      - `span` **text 16px/700** — “여기가 현재 위치예요”
        `font-size:16px font-weight:700 letter-spacing:-0.02em line-height:1.35 color:#101828`
      - `span` **text 13px/400** — “이번 달 월급에서 지금까지 쓴 비율이에요. 막대가 내 목표 선을 넘지 않게 써 보세요. 월말 예상은 아래 칸에 있어”
        `font-size:13px line-height:1.55 color:#475467`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:8px margin-top:6px`
        - `span` **text 13px/600** — “건너뛰기”
          `font-size:13px font-weight:600 color:#626D88 padding:8px 4px`
        - `span` **text 14px/600** — “다음”
          `display:inline-flex align-items:center justify-content:center height:40px padding:0 20px border-radius:12px background:#3556E6 color:#FFFFFF font-size:14px font-weight:600 white-space:nowrap`
