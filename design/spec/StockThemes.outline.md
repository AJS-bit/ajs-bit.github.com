# StockThemes — 블록 개요

원본 `canvas/StockThemes.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div` **화면프레임**
  `width:390px height:844px background:#EDF0F7 color:#101828 display:flex flex-direction:column`
  - `div`
    `display:flex align-items:center gap:6px padding:12px 12px 12px`
    - `div`
      `width:36px height:36px border-radius:11px display:flex align-items:center justify-content:center`
    - `div`
      `display:flex align-items:baseline gap:8px flex:1`
      - `h1` **text 19px/700** — “테마”
        `font-size:19px font-weight:700 letter-spacing:-0.03em line-height:1.2 color:#101828 white-space:nowrap`
      - `span` **text 12px/500** — “14개 테마”
        `font-size:12px font-weight:500 color:#626D88`
    - `span` **StatusPill** — “9/4 종가”
      `display:inline-flex align-items:center gap:4px background:#F0F2F7 color:#5B6880 font-size:11.5px font-weight:600 border-radius:99px padding:4px 9px`
  - `div` **본문(스크롤 영역)**
    `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
    - `div` **Callout(info)**
      `display:flex gap:8px padding:10px 11px background:#F4F6FB border-radius:12px`
      - `span`
        `margin-top:1px`
      - `span` — “테마는 기준으로 거른 목록이 아니라 예요. 한 종목이 여러 테마에 들어갈 수 있어요.”
        `font-size:11.5px line-height:1.5 color:#626D88`
        - `b` — “업종별로 묶어 둔 이름표”
          `font-weight:600`
    - `div`
      `display:grid grid-template-columns:repeat(2, minmax(0, 1fr)) gap:8px`
      - `div`
        `display:flex align-items:center gap:8px height:46px padding:0 12px background:#FFFFFF border:1px solid #E3E8F1 border-radius:14px`
        - `span` **text 13.5px/600** — “반도체”
          `flex:1 font-size:13.5px font-weight:600 color:#101828 white-space:nowrap`
        - `span` **text 11.5px/400** — “24”
          `font-size:11.5px color:#626D88 white-space:nowrap`
      - `div`
        `display:flex align-items:center gap:8px height:46px padding:0 12px background:#FFFFFF border:1px solid #E3E8F1 border-radius:14px`
        - `span` **text 13.5px/600** — “2차전지”
          `flex:1 font-size:13.5px font-weight:600 color:#101828 white-space:nowrap`
        - `span` **text 11.5px/400** — “18”
          `font-size:11.5px color:#626D88 white-space:nowrap`
      - `div`
        `display:flex align-items:center gap:8px height:46px padding:0 12px background:#FFFFFF border:1px solid #E3E8F1 border-radius:14px`
        - `span` **text 13.5px/600** — “바이오”
          `flex:1 font-size:13.5px font-weight:600 color:#101828 white-space:nowrap`
        - `span` **text 11.5px/400** — “31”
          `font-size:11.5px color:#626D88 white-space:nowrap`
      - `div`
        `display:flex align-items:center gap:8px height:46px padding:0 12px background:#FFFFFF border:1px solid #E3E8F1 border-radius:14px`
        - `span` **text 13.5px/600** — “AI”
          `flex:1 font-size:13.5px font-weight:600 color:#101828 white-space:nowrap`
        - `span` **text 11.5px/400** — “15”
          `font-size:11.5px color:#626D88 white-space:nowrap`
      - `div`
        `display:flex align-items:center gap:8px height:46px padding:0 12px background:#FFFFFF border:1px solid #E3E8F1 border-radius:14px`
        - `span` **text 13.5px/600** — “방산”
          `flex:1 font-size:13.5px font-weight:600 color:#101828 white-space:nowrap`
        - `span` **text 11.5px/400** — “9”
          `font-size:11.5px color:#626D88 white-space:nowrap`
      - `div`
        `display:flex align-items:center gap:8px height:46px padding:0 12px background:#FFFFFF border:1px solid #E3E8F1 border-radius:14px`
        - `span` **text 13.5px/600** — “조선”
          `flex:1 font-size:13.5px font-weight:600 color:#101828 white-space:nowrap`
        - `span` **text 11.5px/400** — “7”
          `font-size:11.5px color:#626D88 white-space:nowrap`
      - `div`
        `display:flex align-items:center gap:8px height:46px padding:0 12px background:#FFFFFF border:1px solid #E3E8F1 border-radius:14px`
        - `span` **text 13.5px/600** — “로봇”
          `flex:1 font-size:13.5px font-weight:600 color:#101828 white-space:nowrap`
        - `span` **text 11.5px/400** — “11”
          `font-size:11.5px color:#626D88 white-space:nowrap`
      - `div`
        `display:flex align-items:center gap:8px height:46px padding:0 12px background:#FFFFFF border:1px solid #E3E8F1 border-radius:14px`
        - `span` **text 13.5px/600** — “자동차”
          `flex:1 font-size:13.5px font-weight:600 color:#101828 white-space:nowrap`
        - `span` **text 11.5px/400** — “12”
          `font-size:11.5px color:#626D88 white-space:nowrap`
      - `div`
        `display:flex align-items:center gap:8px height:46px padding:0 12px background:#FFFFFF border:1px solid #E3E8F1 border-radius:14px`
        - `span` **text 13.5px/600** — “금융”
          `flex:1 font-size:13.5px font-weight:600 color:#101828 white-space:nowrap`
        - `span` **text 11.5px/400** — “20”
          `font-size:11.5px color:#626D88 white-space:nowrap`
      - `div`
        `display:flex align-items:center gap:8px height:46px padding:0 12px background:#FFFFFF border:1px solid #E3E8F1 border-radius:14px`
        - `span` **text 13.5px/600** — “엔터”
          `flex:1 font-size:13.5px font-weight:600 color:#101828 white-space:nowrap`
        - `span` **text 11.5px/400** — “8”
          `font-size:11.5px color:#626D88 white-space:nowrap`
      - `div`
        `display:flex align-items:center gap:8px height:46px padding:0 12px background:#FFFFFF border:1px solid #E3E8F1 border-radius:14px`
        - `span` **text 13.5px/600** — “건설”
          `flex:1 font-size:13.5px font-weight:600 color:#101828 white-space:nowrap`
        - `span` **text 11.5px/400** — “10”
          `font-size:11.5px color:#626D88 white-space:nowrap`
      - `div`
        `display:flex align-items:center gap:8px height:46px padding:0 12px background:#FFFFFF border:1px solid #E3E8F1 border-radius:14px`
        - `span` **text 13.5px/600** — “유틸리티”
          `flex:1 font-size:13.5px font-weight:600 color:#101828 white-space:nowrap`
        - `span` **text 11.5px/400** — “6”
          `font-size:11.5px color:#626D88 white-space:nowrap`
      - `div`
        `display:flex align-items:center gap:8px height:46px padding:0 12px background:#FFFFFF border:1px solid #E3E8F1 border-radius:14px`
        - `span` **text 13.5px/600** — “화장품”
          `flex:1 font-size:13.5px font-weight:600 color:#101828 white-space:nowrap`
        - `span` **text 11.5px/400** — “9”
          `font-size:11.5px color:#626D88 white-space:nowrap`
      - `div`
        `display:flex align-items:center gap:8px height:46px padding:0 12px background:#FFFFFF border:1px solid #E3E8F1 border-radius:14px`
        - `span` **text 13.5px/600** — “게임”
          `flex:1 font-size:13.5px font-weight:600 color:#101828 white-space:nowrap`
        - `span` **text 11.5px/400** — “7”
          `font-size:11.5px color:#626D88 white-space:nowrap`
    - `p` — “데이터 기준일 2026-09-04 종가 · 설정에서 새로 받기 기준에 맞는 종목을 보여주는 것이지 투자 권유가 아니”
      `font-size:11px line-height:1.5 color:#626D88`
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
