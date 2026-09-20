# StockStates — 블록 개요

원본 `canvas/StockStates.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div`
  `width:1180px height:880px background:#EDF0F7 color:#101828 padding:28px 30px 30px display:flex flex-direction:column gap:10px`
  - `span` **text 11px/600** — “구현 참고 · 앱 화면이 아닙니다”
    `font-size:11px font-weight:600 letter-spacing:0.02em color:#475467 border:1px solid #E3E8F1 background:#FFFFFF border-radius:99px padding:4px 10px`
  - `h2` **text 20px/700** — “주식 탭 · 특수한 상황 6가지”
    `font-size:20px font-weight:700 letter-spacing:-0.025em color:#101828`
  - `p` **text 13px/400** — “경고 띠는 알려주기만 하고 아무것도 막지 않아요. 자료가 없는 기준은 —로 두고 충족 수에서 빼요. 왼쪽 화면의 번”
    `font-size:13px line-height:1.55 color:#626D88`
  - `div`
    `display:flex gap:28px align-items:flex-start`
    - `div`
      `width:362px display:flex flex-direction:column`
      - `div` **text 11px/600** — “주식 홈 · 위쪽”
        `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:0 2px 6px`
      - `div`
        `border:1px solid #CFD7E6 border-radius:22px background:#EDF0F7`
        - `div`
          `display:flex flex-direction:column gap:10px padding:14px 14px 12px`
        - `div`
          `display:flex flex-direction:column gap:10px padding:0 14px 14px`
      - `div`
        `height:16px`
      - `div` **text 11px/600** — “종목 목록 · 한 줄”
        `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:0 2px 6px`
      - `div`
        `position:relative`
        - `div` **Card(18)**
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:2px 14px`
        - `span` **text 10.5px/700** — “2”
          `position:absolute top:-6px right:-6px width:17px height:17px border-radius:99px background:#101828 color:#FFFFFF font-size:10.5px font-weight:700 display:inline-flex align-items:center justify-content:center box-shadow:0 0 0 2px #FFFFFF`
      - `div`
        `height:16px`
      - `div` **text 11px/600** — “종목 상세 · 맨 위”
        `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:0 2px 6px`
      - `div`
        `display:flex align-items:baseline gap:8px padding:0 2px 8px`
        - `span` **text 19px/700** — “삼성전자”
          `font-size:19px font-weight:700 letter-spacing:-0.03em line-height:1.2 color:#101828 white-space:nowrap`
        - `span` **text 12px/500** — “005930 · KOSPI”
          `font-size:12px font-weight:500 color:#626D88`
      - `div`
        `position:relative`
        - `div` **HeroCard**
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:12px 14px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
        - `span` **text 10.5px/700** — “3”
          `position:absolute top:-6px right:-6px width:17px height:17px border-radius:99px background:#101828 color:#FFFFFF font-size:10.5px font-weight:700 display:inline-flex align-items:center justify-content:center box-shadow:0 0 0 2px #FFFFFF`
    - `div`
      `flex:1`
      - `div`
        `display:grid grid-template-columns:repeat(2, minmax(0, 1fr)) gap:22px 24px align-items:start`
        - `div`
          `display:flex flex-direction:column gap:9px`
        - `div`
          `display:flex flex-direction:column gap:9px`
        - `div`
          `display:flex flex-direction:column gap:9px`
        - `div`
          `display:flex flex-direction:column gap:9px`
        - `div`
          `display:flex flex-direction:column gap:9px`
        - `div`
          `display:flex flex-direction:column gap:9px`
      - `p` — “—는 0점이 아니라 이라는 뜻이에요. 레인보우로보틱스는 성장 기준 3개 중 자료가 있는 1개만 세어 으로 보여요.”
        `font-size:12px line-height:1.6 color:#626D88`
        - `b` — “자료 없음”
          `font-weight:600 color:#475467`
        - `b` — “1/1 충족”
          `font-weight:600 color:#475467`
