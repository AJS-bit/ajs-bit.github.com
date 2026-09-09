# HomeScroll — 블록 개요

원본 `canvas/HomeScroll.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div` **화면프레임**
  `width:390px height:844px background:#EDF0F7 color:#101828 display:flex flex-direction:column`
  - `div` **본문(스크롤 영역)**
    `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px 0`
    - `div`
      `height:20px background:#FFFFFF border:1px solid #E3E8F1 border-top:none border-radius:0 0 18px 18px opacity:.55`
    - `div` **Card(18)**
      `background:#FFFFFF border:1px dashed #B79BFF border-radius:18px padding:14px`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:8px`
        - `span` **StatusPill** — “저장되지 않는 가정”
          `display:inline-flex align-items:center gap:5px background:#F1EAFD color:#6B32D6 font-size:11px font-weight:600 border-radius:99px padding:4px 9px`
        - `span` **text 12px/600** — “가정 종료”
          `font-size:12px font-weight:600 color:#626D88`
      - `p` **text 15px/600** — “소비를 줄이면 얼마나 달라질까요?”
        `font-size:15px font-weight:600 letter-spacing:-0.015em color:#101828`
      - `div`
        `display:flex align-items:baseline gap:7px margin-top:9px`
        - `span` **text 14px/500** — “208만원”
          `font-size:14px font-weight:500 color:#697182`
        - `span` — “188”
          `font-size:25px font-weight:700 letter-spacing:-0.03em color:#6B32D6`
        - `span` **text 12.5px/600** — “−20만원”
          `font-size:12.5px font-weight:600 color:#6B32D6`
      - `div`
        `position:relative height:22px margin-top:8px`
        - `div`
          `position:absolute left:0 right:0 top:9px height:5px border-radius:99px background:#E8ECF5`
        - `div`
          `position:absolute left:0 width:62% top:9px height:5px border-radius:99px background:#7A3FE4`
        - `div`
          `position:absolute left:62% top:0 width:22px height:22px border-radius:99px background:#FFFFFF border:2.5px solid #7A3FE4 box-shadow:0 2px 6px rgba(122,63,228,.28)`
      - `div`
        `display:grid grid-template-columns:repeat(2, minmax(0, 1fr)) gap:8px margin-top:10px`
        - `div`
          `background:#F7F4FE border-radius:12px padding:10px 11px`
        - `div`
          `background:#F7F4FE border-radius:12px padding:10px 11px`
      - `p` **text 11px/400** — “가정일 뿐이며 저장되지 않아요. 실제 기록·한도·목표는 그대로입니다.”
        `font-size:11px line-height:1.45 color:#626D88`
    - `div` **Card(18)**
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:8px`
        - `div`
          `display:flex align-items:center gap:6px`
        - `span` **text 12px/600** — “기준 수정 ›”
          `font-size:12px font-weight:600 color:#3556E6`
      - `div`
        `display:flex align-items:baseline gap:7px margin-top:10px`
        - `span` **text 19px/700** — “20대 후반”
          `font-size:19px font-weight:700 letter-spacing:-0.025em color:#101828`
        - `span` **text 11.5px/400** — “만 27~29세 · 입력한 나이 28세”
          `font-size:11.5px color:#626D88`
      - `div`
        `display:flex flex-direction:column gap:9px margin-top:13px`
        - `div`
        - `div`
      - `p` — “기준보다 4.1%p 적게 쓰고 있어요”
        `font-size:13.5px font-weight:600 letter-spacing:-0.01em color:#0F7B47`
        - `span` — “· 월 15만원 차이”
          `font-weight:500 color:#475467`
      - `div`
        `display:flex gap:7px margin-top:10px padding:9px 10px background:#F4F6FB border-radius:11px`
        - `span` — “내가 직접 등록한 기준입니다. 앱에 내장된 통계나 순위가 아니에요. 출처 · 2025년 · 표본 1,200명”
          `font-size:11px line-height:1.45 color:#626D88`
    - `div` **Card(18)**
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:4px 14px`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:8px height:48px`
        - `span` **text 13.5px/500** — “순자산 대비 소비”
          `font-size:13.5px font-weight:500 color:#475467`
        - `div`
          `display:flex align-items:center gap:8px`
      - `div`
        `height:1px background:#EFF2F8`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:8px height:48px`
        - `span` **text 13.5px/500** — “자산 종합 점수”
          `font-size:13.5px font-weight:500 color:#475467`
        - `div`
          `display:flex align-items:center gap:8px`
      - `div`
        `height:1px background:#EFF2F8`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:8px height:48px`
        - `span` **text 13.5px/500** — “10년 뒤 순자산”
          `font-size:13.5px font-weight:500 color:#475467`
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
      - `span` **text 11px/500** — “목표”
        `font-size:11px font-weight:500 color:#606B7D`
    - `div`
      `display:flex flex-direction:column align-items:center gap:3px flex:1`
      - `div`
        `width:40px height:24px display:flex align-items:center justify-content:center`
      - `span` **text 11px/500** — “미래”
        `font-size:11px font-weight:500 color:#606B7D`
