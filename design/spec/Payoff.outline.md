# Payoff — 블록 개요

원본 `canvas/Payoff.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div` **화면프레임**
  `width:390px height:844px background:#EDF0F7 color:#101828 display:flex flex-direction:column`
  - `div`
    `display:flex flex-direction:column gap:10px padding:14px 16px 12px`
    - `div`
      `display:flex align-items:center justify-content:space-between gap:8px`
      - `div`
        `display:flex align-items:baseline gap:8px`
        - `h1` **text 21px/700** — “미래”
          `font-size:21px font-weight:700 letter-spacing:-0.03em line-height:1.2 color:#101828`
        - `span` **text 12px/500** — “앞으로의 항로”
          `font-size:12px font-weight:500 color:#626D88`
      - `div`
        `display:flex align-items:center gap:2px`
        - `div`
          `width:36px height:36px border-radius:11px display:flex align-items:center justify-content:center`
        - `div`
          `width:36px height:36px border-radius:11px display:flex align-items:center justify-content:center position:relative`
    - `div`
      `display:flex gap:4px background:#E3E8F1 border-radius:12px padding:3px`
      - `div` **SegmentedItem** — “자산 경로”
        `flex:1 height:36px border-radius:9px display:flex align-items:center justify-content:center font-size:13.5px font-weight:500 color:#5B6880`
      - `div` **SegmentedItem** — “상환 계획”
        `flex:1 height:36px border-radius:9px background:#FFFFFF display:flex align-items:center justify-content:center font-size:13.5px font-weight:600 color:#101828 box-shadow:0 1px 2px rgba(16,24,40,.06)`
  - `div` **본문(스크롤 영역)**
    `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
    - `div` **Card(18)**
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px border:1px dashed #B79BFF`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:8px`
        - `span` **StatusPill** — “저장되지 않는 가정”
          `display:inline-flex align-items:center gap:4px background:#F1EAFD color:#6B32D6 font-size:11.5px font-weight:600 border-radius:99px padding:4px 9px`
        - `span` **text 12px/600** — “되돌리기”
          `font-size:12px font-weight:600 color:#626D88`
      - `p` **text 15px/600** — “월 추가 상환을 얼마나 할까요?”
        `font-size:15px font-weight:600 letter-spacing:-0.015em color:#101828`
      - `div`
        `display:flex align-items:baseline gap:7px margin-top:9px`
        - `span` **text 14px/500** — “0원”
          `font-size:14px font-weight:500 color:#697182`
        - `span`
        - `span` — “15”
          `font-size:25px font-weight:700 letter-spacing:-0.03em color:#6B32D6`
        - `span` **text 12.5px/600** — “매월 92만원 상환”
          `font-size:12.5px font-weight:600 color:#6B32D6`
      - `div`
        `margin-top:8px`
        - `div`
          `position:relative height:22px`
      - `div`
        `display:flex align-items:center justify-content:space-between margin-top:5px`
        - `span` **text 11px/400** — “최소 상환만”
          `font-size:11px color:#697182`
        - `span` **text 11px/400** — “월 27만원”
          `font-size:11px color:#697182`
      - `div`
        `margin-top:11px`
        - `div` **Callout(info)**
          `display:flex gap:8px padding:10px 11px background:#F4F6FB border-radius:12px`
    - `div` **Card(18)**
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 14px`
      - `div`
        `display:flex gap:8px`
        - `div`
          `flex:1 padding:13px border-radius:14px border:1.5px solid #7A3FE4 background:#F1EAFD`
        - `div`
          `flex:1 padding:13px border-radius:14px border:1px solid #E3E8F1 background:#FFFFFF`
      - `div`
        `margin-top:11px`
        - `div` **Callout(info)**
          `display:flex gap:8px padding:10px 11px background:#F4F6FB border-radius:12px`
    - `div` **Card(18)**
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:10px`
        - `div`
      - `div`
        `display:flex gap:8px margin-top:12px`
        - `div` **SecondaryButton(44)** — “가정 취소”
          `display:flex align-items:center justify-content:center gap:6px height:44px flex:1 border-radius:13px background:#FFFFFF border:1px solid #D7DEEA color:#475467 font-size:15px font-weight:600`
        - `div` **PrimaryButton(44)** — “상환 계획 저장”
          `display:flex align-items:center justify-content:center gap:6px height:44px flex:1.4 border-radius:13px background:#3556E6 border:none color:#FFFFFF font-size:15px font-weight:600`
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
      - `span` **text 11px/500** — “목표”
        `font-size:11px font-weight:500 color:#606B7D`
    - `div`
      `display:flex flex-direction:column align-items:center gap:3px flex:1`
      - `div`
        `width:40px height:24px border-radius:99px background:#E9EDFD display:flex align-items:center justify-content:center`
      - `span` **text 11px/600** — “미래”
        `font-size:11px font-weight:600 color:#3556E6`
