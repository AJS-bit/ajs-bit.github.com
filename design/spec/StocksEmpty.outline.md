# StocksEmpty — 블록 개요

원본 `canvas/StocksEmpty.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div` **화면프레임**
  `width:390px height:844px background:#EDF0F7 color:#101828 display:flex flex-direction:column`
  - `div`
    `display:flex flex-direction:column gap:10px padding:14px 16px 12px`
    - `div`
      `display:flex align-items:center justify-content:space-between gap:8px`
      - `div`
        `display:flex align-items:baseline gap:8px`
        - `h1` **text 21px/700** — “주식”
          `font-size:21px font-weight:700 letter-spacing:-0.03em line-height:1.2 color:#101828`
        - `span` **text 12px/500** — “아직 기록 없음”
          `font-size:12px font-weight:500 color:#626D88`
      - `div`
        `display:flex align-items:center gap:2px`
        - `div`
          `width:36px height:36px border-radius:11px display:flex align-items:center justify-content:center`
        - `div`
          `width:36px height:36px border-radius:11px display:flex align-items:center justify-content:center position:relative`
  - `div` **본문(스크롤 영역)**
    `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
    - `div`
      `display:flex align-items:center gap:10px padding:10px 14px background:#E9EDFD border-radius:14px`
      - `div`
        `display:flex flex-direction:column gap:1px flex:1`
        - `span` **text 12px/500** — “이번 달 저축·투자 여력”
          `font-size:12px font-weight:500 color:#3B4E8F`
        - `span` **text 11px/400** — “총수입 390만원 − 소비 예상·저축·상환”
          `font-size:11px color:#3B4E8F`
      - `span` — “27”
        `font-size:17px font-weight:700 letter-spacing:-0.02em color:#3556E6 white-space:nowrap`
        - `span` **text 12.5px/600** — “만원”
          `font-size:12.5px font-weight:600`
    - `div` **Card(18)**
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:4px 14px`
      - `div`
        `display:flex flex-direction:column align-items:center text-align:center padding:22px 8px 18px`
        - `div`
          `width:52px height:52px border-radius:16px background:#F4F6FB display:flex align-items:center justify-content:center`
        - `span` **text 16px/700** — “아직 기록한 종목이 없어요”
          `margin-top:14px font-size:16px font-weight:700 letter-spacing:-0.02em color:#101828`
        - `span` — “보유 종목은 수량과 평단을, 관심 종목은 이름만 적으면 돼요. 종가는 직접 넣고, 비워 두면 —로 남아요.”
          `margin-top:6px font-size:12.5px line-height:1.5 color:#475467`
        - `div`
          `display:flex gap:8px width:100% margin-top:18px`
    - `div` **Card(18)**
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
      - `span` **text 11px/600** — “이 화면에 없는 것”
        `font-size:11px font-weight:600 letter-spacing:0.07em color:#626D88`
      - `p` — “실시간 시세 · 주문 · 호가 · 뉴스 · 커뮤니티 · 시세 알림은 없어요. 내 기록을 정리해 보는 화면이라, 주문”
        `font-size:12.5px line-height:1.55 color:#475467`
        - `br`
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
        `width:40px height:24px border-radius:99px background:#E9EDFD display:flex align-items:center justify-content:center`
      - `span` **text 11px/600** — “주식”
        `font-size:11px font-weight:600 color:#3556E6`
    - `div`
      `display:flex flex-direction:column align-items:center gap:3px flex:1`
      - `div`
        `width:40px height:24px display:flex align-items:center justify-content:center`
      - `span` **text 11px/500** — “목적지”
        `font-size:11px font-weight:500 color:#606B7D`
