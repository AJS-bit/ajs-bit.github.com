# FutureProvisional — 블록 개요

원본 `canvas/FutureProvisional.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div`
  `width:1230px height:1080px background:#EDF0F7 color:#101828 padding:28px 30px 30px display:flex flex-direction:column gap:10px`
  - `span` **text 11px/600** — “구현 참고 · 앱 화면이 아닙니다”
    `font-size:11px font-weight:600 letter-spacing:0.02em color:#475467 border:1px solid #E3E8F1 background:#FFFFFF border-radius:99px padding:4px 10px`
  - `h2` **text 20px/700** — “미래 · 자산 경로 — 예상 기준을 확인하기 전의 잠정 표시”
    `font-size:20px font-weight:700 letter-spacing:-0.025em color:#101828`
  - `p` **text 13px/400** — “지난 소비 기록을 확인하기 전에도 미래 · 목표 화면의 예상 값은 그대로 보여 주되 잠정이라고 표시합니다. 왼쪽이 ”
    `font-size:13px line-height:1.55 color:#626D88`
  - `div`
    `display:flex gap:32px align-items:flex-start`
    - `div`
      `width:392px border-radius:24px border:1px solid #E3E8F1`
      - `div`
        `width:390px height:860px background:#EDF0F7 color:#101828 display:flex flex-direction:column`
        - `div`
          `display:flex flex-direction:column gap:10px padding:14px 16px 12px`
        - `div` **본문(스크롤 영역)**
          `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
        - `div` **BottomNav**
          `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`
    - `div`
      `flex:1 display:flex flex-direction:column gap:22px`
      - `div`
        `display:grid grid-template-columns:repeat(2, 362px) gap:22px 20px align-items:start`
        - `div`
          `display:flex flex-direction:column gap:8px`
        - `div`
          `display:flex flex-direction:column gap:22px`
      - `div` **Card(18)**
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:10px 18px 8px`
        - `div` **text 12px/700** — “구현 메모”
          `font-size:12px font-weight:700 color:#101828 padding:2px 0 4px`
        - `div`
          `display:flex gap:10px padding:7px 0 border-bottom:1px solid #F3F5FA`
        - `div`
          `display:flex gap:10px padding:7px 0 border-bottom:1px solid #F3F5FA`
        - `div`
          `display:flex gap:10px padding:7px 0 border-bottom:1px solid #F3F5FA`
        - `div`
          `display:flex gap:10px padding:7px 0 border-bottom:1px solid #F3F5FA`
        - `div`
          `display:flex gap:10px padding:7px 0`
