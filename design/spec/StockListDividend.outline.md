# StockListDividend — 블록 개요

원본 `canvas/StockListDividend.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div` **화면프레임**
  `width:390px height:844px background:#EDF0F7 color:#101828 display:flex flex-direction:column`
  - `div`
    `display:flex align-items:center gap:6px padding:12px 12px 12px`
    - `div`
      `width:36px height:36px border-radius:11px display:flex align-items:center justify-content:center`
    - `div`
      `display:flex align-items:baseline gap:8px flex:1`
      - `h1` **text 19px/700** — “배당주”
        `font-size:19px font-weight:700 letter-spacing:-0.03em line-height:1.2 color:#101828 white-space:nowrap`
      - `span` **text 12px/500** — “기준 3개”
        `font-size:12px font-weight:500 color:#626D88`
    - `span` **StatusPill** — “9/4 종가”
      `display:inline-flex align-items:center gap:4px background:#F0F2F7 color:#5B6880 font-size:11.5px font-weight:600 border-radius:99px padding:4px 9px`
  - `div` **본문(스크롤 영역)**
    `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
    - `div`
      `display:flex flex-direction:column gap:9px`
      - `div`
        `display:flex flex-wrap:wrap gap:6px`
        - `span` — “높은 배당수익률”
          `display:inline-flex align-items:center gap:5px height:30px padding:0 10px 0 8px border-radius:99px background:#3556E6 color:#FFFFFF font-size:12px font-weight:600 white-space:nowrap`
        - `span` — “연속 배당”
          `display:inline-flex align-items:center gap:5px height:30px padding:0 10px 0 8px border-radius:99px background:#3556E6 color:#FFFFFF font-size:12px font-weight:600 white-space:nowrap`
        - `span` **text 12px/500** — “무리 없는 배당”
          `display:inline-flex align-items:center height:30px padding:0 11px border-radius:99px background:#FFFFFF border:1px solid #D7DEEA color:#475467 font-size:12px font-weight:500 white-space:nowrap`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:8px padding:0 2px`
        - `span` **text 12px/400** — “27종목 · 기준을 끄면 목록이 달라져요”
          `font-size:12px color:#626D88`
        - `span` — “충족 기준 수”
          `display:inline-flex align-items:center gap:3px font-size:12px font-weight:600 color:#475467`
    - `div` **Card(18)**
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:2px 14px 0`
      - `div`
        `display:flex align-items:center gap:10px padding:11px 0 border-bottom:1px solid #F3F5FA`
        - `div`
          `display:flex flex-direction:column gap:2px flex:1`
        - `div`
          `display:flex flex-direction:column align-items:flex-end gap:4px`
      - `div`
        `display:flex align-items:center gap:10px padding:11px 0 border-bottom:1px solid #F3F5FA`
        - `div`
          `display:flex flex-direction:column gap:2px flex:1`
        - `div`
          `display:flex flex-direction:column align-items:flex-end gap:4px`
      - `div`
        `display:flex align-items:center gap:10px padding:11px 0 border-bottom:1px solid #F3F5FA`
        - `div`
          `display:flex flex-direction:column gap:2px flex:1`
        - `div`
          `display:flex flex-direction:column align-items:flex-end gap:4px`
      - `div`
        `display:flex align-items:center gap:10px padding:11px 0 border-bottom:1px solid #F3F5FA`
        - `div`
          `display:flex flex-direction:column gap:2px flex:1`
        - `div`
          `display:flex flex-direction:column align-items:flex-end gap:4px`
      - `div`
        `display:flex align-items:center gap:10px padding:11px 0 border-bottom:1px solid #F3F5FA`
        - `div`
          `display:flex flex-direction:column gap:2px flex:1`
        - `div`
          `display:flex flex-direction:column align-items:flex-end gap:4px`
      - `div`
        `display:flex align-items:center gap:10px padding:11px 0`
        - `div`
          `display:flex flex-direction:column gap:2px flex:1`
        - `div`
          `display:flex flex-direction:column align-items:flex-end gap:4px`
      - `div` — “아래로 21종목 더”
        `display:flex align-items:center justify-content:center gap:4px height:42px border-top:1px solid #F3F5FA font-size:12.5px font-weight:600 color:#3556E6`
    - `p` — “데이터 기준일 2026-09-04 종가 · 설정에서 새로 받기 기준에 맞는 종목을 보여주는 것이지 투자 권유가 아니”
      `font-size:11px line-height:1.5 color:#626D88`
      - `br`
