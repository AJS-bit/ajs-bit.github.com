# TourPayoff3 — 블록 개요

원본 `canvas/TourPayoff3.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div` **화면프레임**
  `width:390px height:844px background:#EDF0F7 color:#101828 display:flex flex-direction:column position:relative`
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
          `font-size:12px font-weight:600 color:#626D88 white-space:nowrap`
      - `p` **text 15px/600** — “월 추가 상환을 얼마나 할까요?”
        `font-size:15px font-weight:600 letter-spacing:-0.015em color:#101828`
      - `div`
        `display:flex align-items:baseline gap:7px margin-top:9px`
        - `span` **text 14px/500** — “15만원”
          `font-size:14px font-weight:500 color:#697182`
        - `span`
        - `span` — “20”
          `font-size:25px font-weight:700 letter-spacing:-0.03em color:#6B32D6`
        - `span` **text 12.5px/600** — “매월 97만원 상환”
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
        - `div` **SecondaryButton(44)** — “가정 종료”
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
  - `div`
    `position:absolute inset:0`
    - `div` **HeroCard**
      `position:absolute left:14px top:635px width:362px height:126px border-radius:20px box-shadow:0 0 0 2px rgba(255,255,255,.95), 0 0 0 4px #3556E6, 0 0 0 9999px rgba(16,24,40,.62)`
    - `div` **Card(18)**
      `position:absolute left:14px width:362px bottom:221px background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:16px display:flex flex-direction:column gap:8px box-shadow:0 12px 32px -12px rgba(16,24,40,.45)`
      - `div`
        `position:absolute bottom:-7px left:30px width:13px height:13px background:#FFFFFF transform:rotate(45deg) border-bottom:1px solid #E3E8F1`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:8px`
        - `span` — “처음 안내”
          `display:inline-flex align-items:center gap:5px height:22px padding:0 9px border-radius:99px background:#E9EDFD color:#3556E6 font-size:11.5px font-weight:700 letter-spacing:0.02em`
        - `span` **text 11.5px/600** — “상환 계획 3 / 3”
          `font-size:11.5px font-weight:600 color:#626D88 white-space:nowrap`
      - `span` **text 16px/700** — “마음에 들면 저장”
        `font-size:16px font-weight:700 letter-spacing:-0.02em line-height:1.35 color:#101828`
      - `span` **text 13px/400** — “저장해야 자산 경로와 목적지 계산에 반영돼요. 저장 전까지는 어디에도 영향이 없어요.”
        `font-size:13px line-height:1.55 color:#475467`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:8px margin-top:6px`
        - `span` **text 13px/600** — “건너뛰기”
          `font-size:13px font-weight:600 color:#626D88 padding:8px 4px`
        - `span` **text 14px/600** — “알겠어요”
          `display:inline-flex align-items:center justify-content:center height:40px padding:0 20px border-radius:12px background:#3556E6 color:#FFFFFF font-size:14px font-weight:600 white-space:nowrap`
