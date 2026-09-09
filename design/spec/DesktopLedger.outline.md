# DesktopLedger — 블록 개요

원본 `canvas/DesktopLedger.dc.html`. 값이 다르면 **원본이 맞습니다.**

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
        `display:flex align-items:center gap:11px height:42px padding:0 12px border-radius:11px`
        - `span` **text 14px/500** — “홈”
          `font-size:14px font-weight:500 color:#475467`
        - `span` **text 12px/600** — “57.9%”
          `font-size:12px font-weight:600 color:#697182`
      - `div`
        `display:flex align-items:center gap:11px height:42px padding:0 12px border-radius:11px`
        - `span` **text 14px/500** — “자산”
          `font-size:14px font-weight:500 color:#475467`
        - `span` **text 12px/600** — “9,350만”
          `font-size:12px font-weight:600 color:#697182`
      - `div`
        `display:flex align-items:center gap:11px height:42px padding:0 12px border-radius:11px background:#E9EDFD`
        - `span` **text 14px/600** — “소비”
          `font-size:14px font-weight:600 color:#3556E6`
      - `div`
        `display:flex flex-direction:column gap:1px padding:4px 0 4px 40px`
        - `div` **text 13px/500** — “이번 달”
          `display:flex align-items:center height:32px font-size:13px font-weight:500 color:#626D88`
        - `div` **text 13px/600** — “내역”
          `display:flex align-items:center height:32px font-size:13px font-weight:600 color:#3556E6`
        - `div` **text 13px/500** — “한도”
          `display:flex align-items:center height:32px font-size:13px font-weight:500 color:#626D88`
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
    `flex:1 display:flex flex-direction:column padding:22px 28px`
    - `div`
      `display:flex align-items:flex-end justify-content:space-between gap:12px`
      - `div`
        - `div` **text 11.5px/600** — “소비 · 내역”
          `font-size:11.5px font-weight:600 letter-spacing:0.07em color:#626D88`
        - `h1` **text 26px/700** — “2026년 9월 거래”
          `font-size:26px font-weight:700 letter-spacing:-0.03em line-height:1.2 color:#101828`
      - `div`
        `display:flex align-items:center gap:9px`
        - `div`
          `display:flex align-items:center gap:2px height:42px padding:0 6px border-radius:11px background:#FFFFFF border:1px solid #E3E8F1`
        - `div` — “거래 추가”
          `display:inline-flex align-items:center gap:6px height:42px padding:0 16px border-radius:11px background:#3556E6 font-size:14px font-weight:600 color:#FFFFFF`
    - `div`
      `flex:1 min-height:0 display:grid grid-template-columns:minmax(0, 1.75fr) minmax(0, 1fr) gap:18px margin-top:18px`
      - `div` **Card(20)**
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px display:flex flex-direction:column`
        - `div`
          `display:flex align-items:center gap:10px padding:14px 18px border-bottom:1px solid #EFF2F8`
        - `div`
          `display:flex align-items:center justify-content:space-between gap:10px padding:10px 18px background:#F8FAFD border-bottom:1px solid #EFF2F8`
        - `div`
          `flex:1 min-height:0`
      - `div`
        `display:flex flex-direction:column gap:14px`
        - `div` **Card(20)**
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px 18px`
        - `div` **Card(20)**
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px 18px`
        - `div` **Card(20)**
          `flex:1 min-height:0 background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px 18px display:flex flex-direction:column`
        - `div` **Card(20)**
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px 18px`
