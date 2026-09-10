# SpendingPast — 블록 개요

원본 `canvas/SpendingPast.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div` **화면프레임**
  `width:390px height:844px background:#EDF0F7 color:#101828 display:flex flex-direction:column`
  - `div`
    `display:flex flex-direction:column gap:10px padding:14px 16px 12px`
    - `div`
      `display:flex align-items:center justify-content:space-between gap:8px`
      - `div`
        `display:flex align-items:baseline gap:8px`
        - `h1` **text 21px/700** — “소비”
          `font-size:21px font-weight:700 letter-spacing:-0.03em line-height:1.2 color:#101828`
        - `span` **text 12px/500** — “지난 달 · 마감됨”
          `font-size:12px font-weight:500 color:#626D88`
      - `div`
        `display:flex align-items:center gap:2px height:34px padding:0 4px border-radius:10px background:#FFFFFF border:1px solid #E3E8F1`
        - `span` **text 13px/600** — “2026년 7월”
          `font-size:13px font-weight:600 color:#101828 padding:0 4px`
    - `div`
      `display:flex gap:4px background:#E3E8F1 border-radius:12px padding:3px`
      - `div` **SegmentedItem** — “월 요약”
        `flex:1 height:36px border-radius:9px background:#FFFFFF display:flex align-items:center justify-content:center font-size:13.5px font-weight:600 color:#101828 box-shadow:0 1px 2px rgba(16,24,40,.06)`
      - `div` **SegmentedItem** — “내역”
        `flex:1 height:36px border-radius:9px display:flex align-items:center justify-content:center font-size:13.5px font-weight:500 color:#5B6880`
  - `div`
    `display:flex align-items:center gap:7px padding:0 16px 10px`
    - `span` — “마감한 달이라 · 기록은 내역에서 수정”
      `font-size:11.5px color:#626D88`
      - `b` — “한도 탭이 없어요”
        `font-weight:600`
  - `div` **본문(스크롤 영역)**
    `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
    - `div` **HeroCard**
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:10px`
        - `span` **text 11.5px/600** — “마감한 달”
          `font-size:11.5px font-weight:600 letter-spacing:0.07em color:#626D88`
        - `span` **StatusPill** — “7월 마감 완료 · 확정”
          `display:inline-flex align-items:center gap:4px background:#E4F4EA color:#0F7B47 font-size:11.5px font-weight:600 border-radius:99px padding:4px 9px`
      - `div`
        `display:flex align-items:flex-end justify-content:space-between gap:10px margin-top:9px`
        - `div`
          `display:flex align-items:baseline gap:2px`
        - `div`
          `text-align:right`
      - `div`
        `display:flex align-items:baseline justify-content:space-between gap:10px margin-top:5px`
        - `span` — “월급 대비 소비”
          `font-size:13px font-weight:500 color:#475467`
        - `span`
          `display:inline-flex align-items:center gap:4px`
      - `div`
        `display:grid grid-template-columns:repeat(3, minmax(0, 1fr)) gap:0 margin-top:14px border-top:1px solid #EFF2F8`
        - `div`
          `display:flex flex-direction:column gap:3px`
        - `div`
          `display:flex flex-direction:column gap:3px padding:0 10px border-left:1px solid #EFF2F8`
        - `div`
          `display:flex flex-direction:column gap:3px border-left:1px solid #EFF2F8`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:10px margin-top:12px border-top:1px solid #EFF2F8`
        - `span` **text 11.5px/400** — “7월 마감값 기준 · 예상치 아님”
          `font-size:11.5px color:#626D88`
        - `span` **text 12.5px/600** — “마감 내역 ›”
          `font-size:12.5px font-weight:600 color:#3556E6`
    - `div` **Card(18)**
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
      - `div`
        `display:flex align-items:baseline justify-content:space-between gap:8px`
        - `span` **text 14px/600** — “31일 동안 이렇게 썼어요”
          `font-size:14px font-weight:600 color:#101828`
        - `span` **text 11.5px/400** — “확정 누적 191만원”
          `font-size:11.5px color:#626D88`
      - `div`
        `position:relative height:108px margin-top:12px`
        - `span` **text 10.5px/600** — “한도 211만”
          `position:absolute left:0 top:0 font-size:10.5px font-weight:600 color:#626D88`
        - `div`
          `position:absolute left:0 right:0 top:14px border-top:1px dashed #D7DEEA`
        - `span` **text 12px/700** — “191만”
          `position:absolute right:0 top:36px font-size:12px font-weight:700 color:#101828`
      - `div`
        `position:relative height:26px border-top:1px solid #EFF2F8 margin-top:6px`
        - `span` **text 11px/400** — “1일”
          `position:absolute left:0 top:8px font-size:11px color:#697182`
        - `span` **text 11px/400** — “15일”
          `position:absolute left:46.7% transform:translateX(-50%) top:8px font-size:11px color:#697182 white-space:nowrap`
        - `span` **text 11px/600** — “31일 마감”
          `position:absolute right:0 top:8px font-size:11px font-weight:600 color:#101828`
    - `div` **Card(18)**
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:8px`
        - `div`
          `display:flex align-items:baseline gap:7px`
        - `span` **text 12.5px/600** — “내역 보기 ›”
          `font-size:12.5px font-weight:600 color:#3556E6`
      - `div`
        `margin-top:11px display:flex flex-direction:column gap:10px`
        - `div`
        - `div`
        - `div`
  - `div`
    `height:12px`
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
