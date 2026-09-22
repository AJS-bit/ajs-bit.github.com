# TourSpending1 — 블록 개요

원본 `canvas/TourSpending1.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div` **화면프레임**
  `width:390px height:844px background:#EDF0F7 color:#101828 display:flex flex-direction:column position:relative`
  - `div`
    `display:flex flex-direction:column gap:10px padding:14px 16px 12px`
    - `div`
      `display:flex align-items:center justify-content:space-between gap:8px`
      - `h1` **text 21px/700** — “소비”
        `font-size:21px font-weight:700 letter-spacing:-0.03em line-height:1.2 color:#101828`
      - `div`
        `display:flex align-items:center gap:8px`
        - `div`
          `display:flex align-items:center gap:2px height:34px padding:0 4px border-radius:10px background:#FFFFFF border:1px solid #E3E8F1`
        - `div` — “거래”
          `display:inline-flex align-items:center gap:3px height:34px padding:0 11px border-radius:10px background:#3556E6 color:#FFFFFF font-size:13px font-weight:600`
    - `div`
      `display:flex gap:4px background:#E3E8F1 border-radius:12px padding:3px`
      - `div` **SegmentedItem** — “이번 달”
        `flex:1 height:36px border-radius:9px background:#FFFFFF display:flex align-items:center justify-content:center font-size:13.5px font-weight:600 color:#101828 box-shadow:0 1px 2px rgba(16,24,40,.06)`
      - `div` **SegmentedItem** — “내역”
        `flex:1 height:36px border-radius:9px display:flex align-items:center justify-content:center font-size:13.5px font-weight:500 color:#5B6880`
      - `div` **SegmentedItem** — “한도”
        `flex:1 height:36px border-radius:9px display:flex align-items:center justify-content:center font-size:13.5px font-weight:500 color:#5B6880`
  - `div` **본문(스크롤 영역)**
    `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
    - `div` **HeroCard**
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px 14px 14px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
      - `div`
        `display:flex align-items:flex-start justify-content:space-between gap:10px padding:0 2px`
        - `div`
        - `div`
          `display:flex flex-direction:column align-items:flex-end gap:5px`
      - `div`
        `display:flex align-items:baseline justify-content:space-between gap:8px margin-top:13px padding:0 2px`
        - `span` **text 13.5px/600** — “계획한 속도로 쓰고 있나요?”
          `font-size:13.5px font-weight:600 color:#101828`
      - `div`
        `margin-top:8px`
      - `div`
        `display:flex align-items:center gap:12px margin-top:4px padding:0 2px`
        - `span` — “실제 누적”
          `display:inline-flex align-items:center gap:5px font-size:11px color:#475467`
        - `span` — “월말 예상”
          `display:inline-flex align-items:center gap:5px font-size:11px color:#475467`
        - `span` — “계획선”
          `display:inline-flex align-items:center gap:5px font-size:11px color:#475467`
      - `p` **text 11px/400** — “계획선은 한도를 일수로 나눈 속도예요. 주거·통신·보험처럼 초반에 빠져나가는 고정비 때문에 실제 선이 먼저 올라가요”
        `padding:0 2px font-size:11px line-height:1.45 color:#626D88`
    - `div` **Card(18)**
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:8px`
        - `div`
          `display:flex align-items:baseline gap:7px`
        - `span` **text 12px/600** — “전체 보기 ›”
          `font-size:12px font-weight:600 color:#3556E6`
      - `div`
        `display:flex flex-direction:column margin-top:8px`
        - `div`
          `display:flex align-items:center gap:10px height:46px`
        - `div`
          `display:flex align-items:center gap:10px height:46px`
        - `div`
          `display:flex align-items:center gap:10px height:46px`
        - `div`
          `display:flex align-items:center gap:10px height:46px`
        - `div`
          `display:flex align-items:center gap:10px height:46px`
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
  - `div`
    `position:absolute inset:0`
    - `div`
      `position:absolute left:16px top:58px width:358px height:42px border-radius:14px box-shadow:0 0 0 2px rgba(255,255,255,.95), 0 0 0 4px #3556E6, 0 0 0 9999px rgba(16,24,40,.62)`
    - `div` **Card(18)**
      `position:absolute left:14px width:362px top:112px background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:16px display:flex flex-direction:column gap:8px box-shadow:0 12px 32px -12px rgba(16,24,40,.45)`
      - `div`
        `position:absolute top:-7px left:30px width:13px height:13px background:#FFFFFF transform:rotate(45deg) border-left:1px solid #E3E8F1 border-top:1px solid #E3E8F1`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:8px`
        - `span` — “처음 안내”
          `display:inline-flex align-items:center gap:5px height:22px padding:0 9px border-radius:99px background:#E9EDFD color:#3556E6 font-size:11.5px font-weight:700 letter-spacing:0.02em`
        - `span` **text 11.5px/600** — “소비 1 / 3”
          `font-size:11.5px font-weight:600 color:#626D88 white-space:nowrap`
      - `span` **text 16px/700** — “이번 달 · 내역 · 한도”
        `font-size:16px font-weight:700 letter-spacing:-0.02em line-height:1.35 color:#101828`
      - `span` **text 13px/400** — “이번 달은 쓰는 속도, 내역은 기록 정리, 한도는 카테고리별 상한이에요. 달력에서 저장한 기록은 내역에서 분류해요.”
        `font-size:13px line-height:1.55 color:#475467`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:8px margin-top:6px`
        - `span` **text 13px/600** — “건너뛰기”
          `font-size:13px font-weight:600 color:#626D88 padding:8px 4px`
        - `span` **text 14px/600** — “다음”
          `display:inline-flex align-items:center justify-content:center height:40px padding:0 20px border-radius:12px background:#3556E6 color:#FFFFFF font-size:14px font-weight:600 white-space:nowrap`
