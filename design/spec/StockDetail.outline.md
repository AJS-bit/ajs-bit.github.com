# StockDetail — 블록 개요

원본 `canvas/StockDetail.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div` **화면프레임**
  `width:390px height:844px background:#EDF0F7 color:#101828 display:flex flex-direction:column`
  - `div`
    `display:flex align-items:center gap:6px padding:12px 12px 12px`
    - `div`
      `width:36px height:36px border-radius:11px display:flex align-items:center justify-content:center`
    - `div`
      `display:flex align-items:baseline gap:8px flex:1`
      - `h1` **text 19px/700** — “삼성전자”
        `font-size:19px font-weight:700 letter-spacing:-0.03em line-height:1.2 color:#101828 white-space:nowrap`
      - `span` **text 12px/500** — “005930 · KOSPI”
        `font-size:12px font-weight:500 color:#626D88`
  - `div` **본문(스크롤 영역)**
    `flex:1 min-height:0 display:flex flex-direction:column gap:8px padding:0 14px 12px`
    - `div` **HeroCard**
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:12px 14px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
      - `div`
        `display:flex align-items:flex-end justify-content:space-between gap:10px`
        - `div`
          `display:flex align-items:baseline gap:3px`
        - `span` **StatusPill** — “9/4 종가”
          `display:inline-flex align-items:center gap:4px background:#F0F2F7 color:#5B6880 font-size:11.5px font-weight:600 border-radius:99px padding:4px 9px`
      - `div`
        `display:flex align-items:center gap:6px margin-top:8px`
        - `span` **StatusPill** — “성장”
          `display:inline-flex align-items:center gap:4px background:#E9EDFD color:#3556E6 font-size:11.5px font-weight:600 border-radius:99px padding:4px 9px`
        - `span` **StatusPill** — “배당”
          `display:inline-flex align-items:center gap:4px background:#E4F4EA color:#0F7B47 font-size:11.5px font-weight:600 border-radius:99px padding:4px 9px`
        - `span` **text 11.5px/400** — “성장·배당 두 목록에 있어요”
          `font-size:11.5px color:#626D88`
      - `div`
        `margin-top:10px`
        - `div`
          `display:flex justify-content:space-between font-size:11px color:#626D88`
        - `div`
          `position:relative height:8px border-radius:99px background:#E8ECF5 margin-top:5px`
        - `div` **text 11px/400** — “52주 저점과 고점 사이 52% 지점”
          `font-size:11px color:#626D88 margin-top:7px text-align:center`
    - `div` **Card(18)**
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px 4px`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:8px`
        - `div`
          `display:flex align-items:baseline gap:7px`
      - `div`
        `margin-top:2px`
        - `div`
          `display:flex align-items:center gap:10px padding:7px 0 border-bottom:1px solid #F3F5FA`
        - `div`
          `display:flex align-items:center gap:10px padding:7px 0 border-bottom:1px solid #F3F5FA`
        - `div`
          `display:flex align-items:center gap:10px padding:7px 0`
    - `div` **Card(18)**
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:11px 14px`
      - `div`
        `display:grid grid-template-columns:repeat(3, minmax(0, 1fr)) gap:0`
        - `div`
          `display:flex flex-direction:column gap:3px`
        - `div`
          `display:flex flex-direction:column gap:3px border-left:1px solid #EFF2F8`
        - `div`
          `display:flex flex-direction:column gap:3px border-left:1px solid #EFF2F8`
    - `div` **Card(18)**
      `background:#FFFFFF border:1px dashed #B79BFF border-radius:18px padding:12px 14px`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:8px`
        - `span` **StatusPill** — “저장되지 않는 가정”
          `display:inline-flex align-items:center gap:4px background:#F1EAFD color:#6B32D6 font-size:11.5px font-weight:600 border-radius:99px padding:4px 9px`
        - `span` **text 12px/600** — “되돌리기”
          `font-size:12px font-weight:600 color:#626D88`
      - `p` **text 15px/600** — “내 항로에 넣어보기”
        `font-size:15px font-weight:600 letter-spacing:-0.015em color:#101828`
      - `div`
        `display:flex align-items:baseline justify-content:space-between gap:8px margin-top:6px`
        - `span` **text 12.5px/400** — “이 종목에 매달”
          `font-size:12.5px color:#475467`
        - `span` — “15”
          `font-size:22px font-weight:700 letter-spacing:-0.03em color:#6B32D6`
      - `div`
        `margin-top:4px`
        - `div`
          `position:relative height:22px`
      - `div` **text 12px/400** — “투자 계좌 5,000만원 도착”
        `margin-top:8px font-size:12px color:#626D88 white-space:nowrap`
      - `div`
        `display:flex align-items:center gap:6px margin-top:5px font-size:13px color:#475467 white-space:nowrap`
        - `span` — “2032년 6월”
          `font-weight:500 color:#697182`
        - `span` **text 14px/700** — “2030년 12월”
          `font-size:14px font-weight:700 color:#6B32D6`
        - `span` **StatusPill** — “1년 6개월 빨라져요”
          `display:inline-flex align-items:center background:#F1EAFD color:#6B32D6 font-size:11.5px font-weight:600 border-radius:99px padding:4px 9px white-space:nowrap`
      - `p` — “이번 달 여력 27만원 안에서 넣어 본 가정이에요. 수익률은 이 종목이 아니라 투자 계좌 목표의 연 5.0%로 봤어”
        `font-size:11px line-height:1.45 color:#626D88`
        - `br`
  - `div`
    `display:flex gap:8px padding:10px 14px 20px background:#FFFFFF border-top:1px solid #E3E8F1`
    - `div` **SecondaryButton(48)** — “관심 추가”
      `display:flex align-items:center justify-content:center gap:6px height:48px flex:1 border-radius:13px background:#FFFFFF border:1px solid #D7DEEA color:#475467 font-size:15px font-weight:600`
    - `div` **PrimaryButton(48)** — “보유 기록”
      `display:flex align-items:center justify-content:center gap:6px height:48px flex:1.3 border-radius:13px background:#3556E6 border:none color:#FFFFFF font-size:15px font-weight:600`
