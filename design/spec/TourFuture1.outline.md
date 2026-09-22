# TourFuture1 — 블록 개요

원본 `canvas/TourFuture1.dc.html`. 값이 다르면 **원본이 맞습니다.**

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
        `flex:1 height:36px border-radius:9px background:#FFFFFF display:flex align-items:center justify-content:center font-size:13.5px font-weight:600 color:#101828 box-shadow:0 1px 2px rgba(16,24,40,.06)`
      - `div` **SegmentedItem** — “상환 계획”
        `flex:1 height:36px border-radius:9px display:flex align-items:center justify-content:center font-size:13.5px font-weight:500 color:#5B6880`
  - `div` **본문(스크롤 영역)**
    `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
    - `div` **HeroCard**
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:14px 14px 13px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
      - `div`
        `display:flex align-items:center gap:8px padding:0 2px`
        - `span` **text 11px/500** — “기간”
          `font-size:11px font-weight:500 color:#626D88 width:52px`
        - `div`
          `display:flex gap:5px flex:1`
      - `div`
        `display:flex align-items:center gap:8px margin-top:6px padding:0 2px`
        - `span` **text 11px/500** — “투자 환경”
          `font-size:11px font-weight:500 color:#626D88 width:52px`
        - `div`
          `display:flex gap:5px flex:1`
      - `div`
        `display:flex align-items:flex-end justify-content:space-between gap:10px margin-top:14px padding:0 2px`
        - `div`
        - `div`
          `display:flex flex-direction:column align-items:flex-end gap:1px`
      - `div`
        `margin-top:10px`
      - `div`
        `display:flex align-items:center gap:12px margin-top:6px padding:0 2px`
        - `span` — “기준 3.21억”
          `display:inline-flex align-items:center gap:5px font-size:11px color:#475467`
        - `span` — “보수 2.85억 ~ 낙관 4.02억”
          `display:inline-flex align-items:center gap:5px font-size:11px color:#475467`
      - `p` **text 11px/400** — “명목금액 기준이며 물가·세금·수수료는 반영하지 않았어요. 월 63만원 적립과 현재 자산 구성이 유지된다고 가정합니다”
        `padding:0 2px font-size:11px line-height:1.45 color:#626D88`
    - `div` **Card(18)**
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px 4px`
      - `div`
        `display:flex align-items:center gap:6px`
        - `span` **text 14px/600** — “다음 자산 지점”
          `font-size:14px font-weight:600 color:#101828`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:8px height:36px border-top:1px solid #F3F5FA`
        - `span` **text 13.5px/600** — “1억원”
          `font-size:13.5px font-weight:600 color:#101828`
        - `div`
          `display:flex align-items:baseline gap:8px`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:8px height:36px border-top:1px solid #F3F5FA`
        - `span` **text 13.5px/600** — “1억 5,000만원”
          `font-size:13.5px font-weight:600 color:#101828`
        - `div`
          `display:flex align-items:baseline gap:8px`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:8px height:36px border-top:1px solid #F3F5FA`
        - `span` **text 13.5px/600** — “2억원”
          `font-size:13.5px font-weight:600 color:#101828`
        - `div`
          `display:flex align-items:baseline gap:8px`
    - `div` **Card(18)**
      `background:#FFFFFF border:1px dashed #B79BFF border-radius:18px padding:11px 14px 11px`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:8px`
        - `span` **StatusPill** — “저장되지 않는 가정”
          `display:inline-flex align-items:center gap:5px background:#F1EAFD color:#6B32D6 font-size:11px font-weight:600 border-radius:99px padding:4px 9px white-space:nowrap`
        - `span` **text 13px/600** — “10년 뒤 +2,032만원”
          `font-size:13px font-weight:600 color:#6B32D6 white-space:nowrap`
      - `p` — “월 소비를 줄이면 얼마나 달라질까요?”
        `font-size:13.5px font-weight:600 letter-spacing:-0.015em color:#101828 white-space:nowrap`
        - `span` — “15만원”
          `color:#6B32D6`
      - `div`
        `display:flex align-items:center gap:9px margin-top:6px`
        - `span` **text 11px/400** — “0원”
          `font-size:11px color:#697182 white-space:nowrap`
        - `div`
          `position:relative height:20px flex:1`
        - `span` **text 11px/400** — “45만원”
          `font-size:11px color:#697182 white-space:nowrap`
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
      `position:absolute left:14px top:114px width:362px height:386px border-radius:20px box-shadow:0 0 0 2px rgba(255,255,255,.95), 0 0 0 4px #3556E6, 0 0 0 9999px rgba(16,24,40,.62)`
    - `div` **Card(18)**
      `position:absolute left:14px width:362px top:512px background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:16px display:flex flex-direction:column gap:8px box-shadow:0 12px 32px -12px rgba(16,24,40,.45)`
      - `div`
        `position:absolute top:-7px left:30px width:13px height:13px background:#FFFFFF transform:rotate(45deg) border-left:1px solid #E3E8F1 border-top:1px solid #E3E8F1`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:8px`
        - `span` — “처음 안내”
          `display:inline-flex align-items:center gap:5px height:22px padding:0 9px border-radius:99px background:#E9EDFD color:#3556E6 font-size:11.5px font-weight:700 letter-spacing:0.02em`
        - `span` **text 11.5px/600** — “미래 1 / 3”
          `font-size:11.5px font-weight:600 color:#626D88 white-space:nowrap`
      - `span` **text 16px/700** — “앞으로의 자산 경로”
        `font-size:16px font-weight:700 letter-spacing:-0.02em line-height:1.35 color:#101828`
      - `span` **text 13px/400** — “기간과 투자 환경을 고르면 지금 속도로 자산이 어떻게 자라는지 그려요. 실제 기록은 바뀌지 않아요.”
        `font-size:13px line-height:1.55 color:#475467`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:8px margin-top:6px`
        - `span` **text 13px/600** — “건너뛰기”
          `font-size:13px font-weight:600 color:#626D88 padding:8px 4px`
        - `span` **text 14px/600** — “다음”
          `display:inline-flex align-items:center justify-content:center height:40px padding:0 20px border-radius:12px background:#3556E6 color:#FFFFFF font-size:14px font-weight:600 white-space:nowrap`
