# TourDebts1 — 블록 개요

원본 `canvas/TourDebts1.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div` **화면프레임**
  `width:390px height:844px background:#EDF0F7 color:#101828 display:flex flex-direction:column position:relative`
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
        `flex:1 height:36px border-radius:9px display:flex align-items:center justify-content:center font-size:13.5px font-weight:500 color:#5B6880`
      - `div` **SegmentedItem** — “부채”
        `flex:1 height:36px border-radius:9px background:#FFFFFF display:flex align-items:center justify-content:center font-size:13.5px font-weight:600 color:#101828 box-shadow:0 1px 2px rgba(16,24,40,.06)`
      - `div` **SegmentedItem** — “상환 전략”
        `flex:1 height:36px border-radius:9px display:flex align-items:center justify-content:center font-size:13.5px font-weight:500 color:#5B6880`
  - `div` **본문(스크롤 영역)**
    `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
    - `div` **HeroCard**
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:8px`
        - `span` **text 11px/600** — “총부채”
          `font-size:11px font-weight:600 letter-spacing:0.07em color:#626D88`
        - `span` **StatusPill** — “가중 평균 연 4.44%”
          `display:inline-flex align-items:center gap:4px background:#F0F2F7 color:#5B6880 font-size:11.5px font-weight:600 border-radius:99px padding:4px 9px`
      - `div`
        `display:flex align-items:flex-end justify-content:space-between gap:10px margin-top:6px`
        - `div`
          `display:flex align-items:baseline gap:2px`
        - `div`
          `display:flex flex-direction:column align-items:flex-end gap:1px`
      - `div` **ProgressTrack**
        `display:flex height:10px border-radius:99px margin-top:14px gap:2px`
        - `div`
          `width:70% background:#94a3b8`
        - `div`
          `width:25% background:#f59e0b`
        - `div`
          `width:3% background:#64748b`
        - `div`
          `width:2% background:#C0342F`
      - `div`
        `display:flex align-items:center justify-content:space-between margin-top:8px`
        - `span` **text 11px/400** — “담보 70% · 신용 25% · 학자금 3% · 할부 2%”
          `font-size:11px color:#626D88`
        - `span` **text 11px/400** — “총자산의 48.7%”
          `font-size:11px color:#626D88`
    - `div` **TurnCard**
      `display:flex gap:12px background:#FFFFFF border:1px solid #E3E8F1 border-left:3px solid #DE8A2A border-radius:18px padding:13px 14px`
      - `div`
        `width:34px height:34px border-radius:11px background:#FDF1E0 display:flex align-items:center justify-content:center`
      - `div`
        `display:flex flex-direction:column gap:3px`
        - `span` **text 11px/600** — “고금리 경고”
          `font-size:11px font-weight:600 letter-spacing:0.06em color:#B45309`
        - `span` **text 15px/600** — “카드 할부 연 14.5%부터 갚으세요”
          `font-size:15px font-weight:600 letter-spacing:-0.015em line-height:1.35 color:#101828`
        - `span` **text 12.5px/400** — “잔액은 전체의 2%지만 금리는 신용대출의 2.1배예요.”
          `font-size:12.5px line-height:1.45 color:#475467`
        - `span` **text 12.5px/600** — “상환 전략 보기 ›”
          `font-size:12.5px font-weight:600 color:#3556E6 margin-top:5px`
    - `div` **Card(18)**
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:8px`
        - `div`
          `display:flex align-items:baseline gap:7px`
        - `div` — “추가”
          `display:inline-flex align-items:center gap:4px height:30px padding:0 11px border-radius:9px background:#E9EDFD border:none color:#3556E6 font-size:12.5px font-weight:600`
      - `div`
        `display:flex flex-direction:column margin-top:6px`
        - `div`
          `display:flex align-items:center gap:10px min-height:52px border-bottom:1px solid #EFF2F8`
        - `div`
          `display:flex align-items:center gap:10px min-height:52px border-bottom:1px solid #EFF2F8`
        - `div`
          `display:flex align-items:center gap:10px min-height:52px border-bottom:1px solid #EFF2F8`
        - `div`
          `display:flex align-items:center gap:10px min-height:52px`
    - `div` **Card(18)**
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 14px`
      - `div`
        `display:flex align-items:baseline justify-content:space-between gap:8px`
        - `span` — “이번 달 상환 예정”
          `font-size:13.5px font-weight:600 color:#101828`
        - `span` **text 15px/600** — “92만원”
          `font-size:15px font-weight:600 letter-spacing:-0.02em color:#101828`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:8px margin-top:6px`
        - `span` **text 11.5px/400** — “최소 77만원 + 추가 15만원”
          `font-size:11.5px color:#626D88`
        - `span` **text 11.5px/400** — “소비율에는 포함되지 않아요”
          `font-size:11.5px color:#626D88`
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
  - `div`
    `position:absolute inset:0`
    - `div` **HeroCard**
      `position:absolute left:14px top:114px width:362px height:160px border-radius:20px box-shadow:0 0 0 2px rgba(255,255,255,.95), 0 0 0 4px #3556E6, 0 0 0 9999px rgba(16,24,40,.62)`
    - `div` **Card(18)**
      `position:absolute left:14px width:362px top:286px background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:16px display:flex flex-direction:column gap:8px box-shadow:0 12px 32px -12px rgba(16,24,40,.45)`
      - `div`
        `position:absolute top:-7px left:30px width:13px height:13px background:#FFFFFF transform:rotate(45deg) border-left:1px solid #E3E8F1 border-top:1px solid #E3E8F1`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:8px`
        - `span` — “처음 안내”
          `display:inline-flex align-items:center gap:5px height:22px padding:0 9px border-radius:99px background:#E9EDFD color:#3556E6 font-size:11.5px font-weight:700 letter-spacing:0.02em`
        - `span` **text 11.5px/600** — “부채 1 / 3”
          `font-size:11.5px font-weight:600 color:#626D88 white-space:nowrap`
      - `span` **text 16px/700** — “갚을 것 전체”
        `font-size:16px font-weight:700 letter-spacing:-0.02em line-height:1.35 color:#101828`
      - `span` **text 13px/400** — “총부채와 가중 평균 금리, 월 최소 상환액이에요. 담보 비중이 크면 급하지 않은 빚이 많다는 뜻이에요.”
        `font-size:13px line-height:1.55 color:#475467`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:8px margin-top:6px`
        - `span` **text 13px/600** — “건너뛰기”
          `font-size:13px font-weight:600 color:#626D88 padding:8px 4px`
        - `span` **text 14px/600** — “다음”
          `display:inline-flex align-items:center justify-content:center height:40px padding:0 20px border-radius:12px background:#3556E6 color:#FFFFFF font-size:14px font-weight:600 white-space:nowrap`
