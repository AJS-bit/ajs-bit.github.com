# Payoff — 블록 개요

원본 `canvas/Payoff.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div`
  `width:390px height:924px background:#EDF0F7 color:#101828 display:flex flex-direction:column`
  - `div`
    `display:flex flex-direction:column gap:10px padding:14px 16px 12px`
    - `div`
      `display:flex align-items:flex-start justify-content:space-between gap:8px`
      - `div`
        `display:flex align-items:center gap:4px min-height:36px`
        - `h1` **text 21px/700** — “미래”
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
      - `div` **SegmentedItem** — “자산 경로”
        `flex:1 height:36px border-radius:9px display:flex align-items:center justify-content:center font-size:13.5px font-weight:500 color:#5B6880`
      - `div` **SegmentedItem** — “상환 계획”
        `flex:1 height:36px border-radius:9px background:#FFFFFF display:flex align-items:center justify-content:center font-size:13.5px font-weight:600 color:#101828 box-shadow:0 1px 2px rgba(16,24,40,.06)`
  - `div` **본문(스크롤 영역)**
    `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
    - `div` **Card(18)**
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
      - `div`
        `display:flex align-items:center gap:8px`
        - `span` **StatusPill** — “저장된 계획”
          `display:inline-flex align-items:center gap:4px background:#E4F4EA color:#0F7B47 font-size:11.5px font-weight:600 border-radius:99px padding:4px 9px`
      - `p` **text 15px/600** — “월 추가 상환을 얼마나 할까요?”
        `font-size:15px font-weight:600 letter-spacing:-0.015em color:#101828`
      - `div`
        `display:flex align-items:baseline gap:2px margin-top:8px`
        - `span` **text 25px/700** — “15”
          `font-size:25px font-weight:700 letter-spacing:-0.03em color:#101828`
        - `span` **text 15px/600** — “만원”
          `font-size:15px font-weight:600 color:#475467`
      - `div` **text 12.5px/600** — “최소 77만원 + 추가 15만원 = 매월 92만원”
        `font-size:12.5px font-weight:600 color:#475467 margin-top:4px`
      - `div` **text 12.5px/400** — “지금 계획에서 매달 남는 돈 약 90만원”
        `font-size:12.5px color:#475467 margin-top:10px`
      - `div`
        `margin-top:8px`
        - `div`
          `position:relative height:22px`
      - `div`
        `display:flex align-items:center justify-content:space-between margin-top:5px`
        - `span` **text 11px/400** — “최소 상환만”
          `font-size:11px color:#697182`
        - `span` **text 11px/400** — “월 200만원”
          `font-size:11px color:#697182`
      - `div` **text 12px/400** — “저축 · 상환 계획까지 지키려면 이번 달 152만원 안에서 쓰면 돼요”
        `font-size:12px line-height:1.45 color:#626D88 margin-top:8px`
      - `div`
        `margin-top:10px`
        - `div` **Callout(info)**
          `display:flex gap:8px padding:10px 11px background:#F4F6FB border-radius:12px`
    - `div` **Card(18)**
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 14px`
      - `div`
        `display:flex gap:8px`
        - `div`
          `flex:1 padding:13px border-radius:14px border:1.5px solid #3556E6 background:#E9EDFD`
        - `div`
          `flex:1 padding:13px border-radius:14px border:1px solid #E3E8F1 background:#FFFFFF`
      - `div`
        `margin-top:11px`
        - `div` **Callout(info)**
          `display:flex gap:8px padding:10px 11px background:#F4F6FB border-radius:12px`
    - `div` **Card(18)**
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
      - `div` **text 13.5px/600** — “저장된 상환 계획이에요”
        `font-size:13.5px font-weight:600 color:#101828`
      - `div` **text 11.5px/400** — “슬라이더나 방식을 바꾸면 보라 점선으로 바뀌고, 저장해야 홈 · 자산 경로 · 목적지 계산에 반영돼요.”
        `font-size:11.5px line-height:1.5 color:#626D88 margin-top:3px`
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
        `width:40px height:24px display:flex align-items:center justify-content:center`
      - `span` **text 11px/500** — “목적지”
        `font-size:11px font-weight:500 color:#606B7D`
    - `div`
      `display:flex flex-direction:column align-items:center gap:3px flex:1`
      - `div`
        `width:40px height:24px border-radius:99px background:#E9EDFD display:flex align-items:center justify-content:center`
      - `span` **text 11px/600** — “미래”
        `font-size:11px font-weight:600 color:#3556E6`
