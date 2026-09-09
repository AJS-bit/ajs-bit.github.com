# DesktopHome — 블록 개요

원본 `canvas/DesktopHome.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div`
  `width:1440px height:900px background:#EDF0F7 color:#101828 display:flex`
  - `div`
    `width:232px background:#FFFFFF display:flex flex-direction:column padding:22px 16px 18px`
    - `div`
      `display:flex align-items:center gap:10px padding:0 6px`
      - `div`
        `width:34px height:34px border-radius:11px background:linear-gradient(140deg, #3556E6 0%, #7A3FE4 100%) display:flex align-items:center justify-content:center`
      - `div`
        - `div` **text 16px/700** — “NAVI”
          `font-size:16px font-weight:700 letter-spacing:0.06em color:#101828 line-height:1.2`
        - `div` **text 11px/500** — “자산 성장 내비게이션”
          `font-size:11px font-weight:500 color:#626D88`
    - `div`
      `display:flex flex-direction:column gap:3px margin-top:26px`
      - `div`
        `display:flex align-items:center gap:11px height:42px padding:0 12px border-radius:11px background:#E9EDFD`
        - `span` **text 14px/600** — “홈”
          `font-size:14px font-weight:600 color:#3556E6`
      - `div`
        `display:flex align-items:center gap:11px height:42px padding:0 12px border-radius:11px`
        - `span` **text 14px/500** — “자산”
          `font-size:14px font-weight:500 color:#475467`
        - `span` **text 12px/600** — “9,350만”
          `font-size:12px font-weight:600 color:#697182`
      - `div`
        `display:flex align-items:center gap:11px height:42px padding:0 12px border-radius:11px`
        - `span` **text 14px/500** — “소비”
          `font-size:14px font-weight:500 color:#475467`
        - `span` **text 12px/600** — “57.9%”
          `font-size:12px font-weight:600 color:#697182`
      - `div`
        `display:flex align-items:center gap:11px height:42px padding:0 12px border-radius:11px`
        - `span` **text 14px/500** — “목적지”
          `font-size:14px font-weight:500 color:#475467`
        - `span` **text 12px/600** — “4”
          `font-size:12px font-weight:600 color:#697182`
      - `div`
        `display:flex align-items:center gap:11px height:42px padding:0 12px border-radius:11px`
        - `span` **text 14px/500** — “미래”
          `font-size:14px font-weight:500 color:#475467`
        - `span` **text 12px/600** — “2.0억”
          `font-size:12px font-weight:600 color:#697182`
    - `div`
      `margin-top:22px padding:13px background:#F4F6FB border-radius:14px`
      - `div` **text 11px/600** — “이번 달 남은 여유”
        `font-size:11px font-weight:600 letter-spacing:0.06em color:#626D88`
      - `div`
        `display:flex align-items:baseline gap:3px margin-top:4px`
        - `span` **text 22px/700** — “104”
          `font-size:22px font-weight:700 letter-spacing:-0.03em color:#0F7B47`
        - `span` **text 13px/600** — “만원”
          `font-size:13px font-weight:600 color:#0F7B47`
      - `div` **ProgressTrack**
        `position:relative height:6px border-radius:99px background:#E3E8F1 margin-top:8px`
        - `div`
          `position:absolute inset:0 48.1% 0 0 border-radius:99px background:#3556E6`
      - `div` **text 11px/400** — “22일 · 하루 47,270원”
        `font-size:11px color:#626D88 margin-top:6px`
    - `div`
      `margin-top:auto display:flex flex-direction:column gap:3px`
      - `div`
        `display:flex align-items:center gap:11px height:40px padding:0 12px border-radius:11px`
        - `span` **text 13.5px/500** — “설정 · 내 수치”
          `font-size:13.5px font-weight:500 color:#475467`
      - `div` **Callout(info)**
        `display:flex align-items:center gap:10px height:48px padding:0 10px border-radius:12px background:#F4F6FB`
        - `div` **text 12px/700** — “샘”
          `width:30px height:30px border-radius:9px background:#E9EDFD display:flex align-items:center justify-content:center font-size:12px font-weight:700 color:#3556E6`
        - `div`
  - `div`
    `flex:1 display:flex flex-direction:column padding:18px 28px 22px`
    - `div`
      `display:flex align-items:center justify-content:space-between gap:12px height:38px padding:0 16px background:#E9EDFD border-radius:12px`
      - `span` **text 12.5px/500** — “샘플 데이터로 둘러보는 중 · 표시된 이름과 금액은 실제 정보가 아닙니다”
        `font-size:12.5px font-weight:500 color:#3B4E8F`
      - `span` **text 12.5px/600** — “내 데이터로 시작 ›”
        `font-size:12.5px font-weight:600 color:#3556E6`
    - `div`
      `display:flex align-items:flex-end justify-content:space-between gap:12px margin-top:18px`
      - `div`
        - `div` **text 11.5px/600** — “2026년 9월 8일 · 이번 달 22일 남음”
          `font-size:11.5px font-weight:600 letter-spacing:0.07em color:#626D88`
        - `h1` **text 26px/700** — “오늘의 내비게이션”
          `font-size:26px font-weight:700 letter-spacing:-0.03em line-height:1.2 color:#101828`
      - `div`
        `display:flex align-items:center gap:8px`
        - `div` — “내 수치 입력”
          `display:inline-flex align-items:center gap:6px height:40px padding:0 14px border-radius:11px background:#FFFFFF border:1px solid #E3E8F1 font-size:13.5px font-weight:600 color:#475467`
        - `div`
          `width:40px height:40px border-radius:11px background:#FFFFFF border:1px solid #E3E8F1 display:flex align-items:center justify-content:center`
        - `div`
          `width:40px height:40px border-radius:11px background:#FFFFFF border:1px solid #E3E8F1 display:flex align-items:center justify-content:center position:relative`
    - `div`
      `flex:1 min-height:0 display:grid grid-template-columns:minmax(0, 1.6fr) minmax(0, 1fr) gap:18px margin-top:16px`
      - `div`
        `display:flex flex-direction:column gap:16px`
        - `div`
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:22px padding:20px 22px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 8px 24px -16px rgba(16,24,40,.28)`
        - `div` **Card(20)**
          `flex:1 min-height:0 background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:18px 20px 16px display:flex flex-direction:column`
      - `div`
        `display:flex flex-direction:column gap:14px`
        - `div` **TurnCard**
          `display:flex gap:13px background:#FFFFFF border:1px solid #E3E8F1 border-left:3px solid #DE8A2A border-radius:18px padding:15px 16px`
        - `div` **Card(18)**
          `display:flex align-items:center gap:13px background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:15px 16px`
        - `div` **Card(18)**
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:15px 16px display:flex flex-direction:column`
        - `div` **Card(18)**
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:15px 16px`
