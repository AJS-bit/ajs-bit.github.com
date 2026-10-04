# AssetBalanceCheck — 블록 개요

원본 `canvas/AssetBalanceCheck.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div` **화면프레임**
  `width:390px height:844px background:#2A3245 color:#101828 display:flex flex-direction:column`
  - `div` **Scrim여백**
    `height:190px display:flex align-items:flex-end justify-content:center`
    - `span` **text 11.5px/500** — “배경을 눌러 닫기”
      `font-size:11.5px font-weight:500 color:rgba(255,255,255,.62)`
  - `div` **BottomSheet**
    `flex:1 min-height:0 background:#FFFFFF border-radius:26px 26px 0 0 display:flex flex-direction:column color:#101828`
    - `div`
      `display:flex justify-content:center padding:9px 0 0`
      - `span` **GrabHandle**
        `width:38px height:4px border-radius:99px background:#D7DEEA`
    - `div`
      `display:flex align-items:flex-start justify-content:space-between gap:10px padding:12px 18px 14px border-bottom:1px solid #EFF2F8`
      - `div`
        - `h2` **text 18px/700** — “잔액 한 번에 확인”
          `font-size:18px font-weight:700 letter-spacing:-0.025em color:#101828`
        - `p` **text 12.5px/400** — “통장·증권 앱에서 지금 금액을 보고, 같으면 「그대로예요」를 누르세요.”
          `font-size:12.5px line-height:1.45 color:#626D88`
    - `div`
      `flex:1 min-height:0 padding:14px 18px 0 display:flex flex-direction:column gap:15px`
      - `div` **text 11.5px/600** — “2개 중 0개 확인함”
        `font-size:11.5px font-weight:600 line-height:17px color:#626D88`
      - `div`
        `display:flex flex-direction:column gap:10px`
        - `div`
          `padding:12px border-radius:14px background:#FFFFFF border:1px solid #E3E8F1`
        - `div`
          `padding:12px border-radius:14px background:#FFFFFF border:1px solid #E3E8F1`
    - `div`
      `display:flex gap:10px padding:12px 18px 20px border-top:1px solid #EFF2F8`
      - `div` **SecondaryButton(48)** — “닫기”
        `display:flex align-items:center justify-content:center gap:6px height:48px width:100% border-radius:13px background:#FFFFFF border:1px solid #D7DEEA color:#475467 font-size:15px font-weight:600`
