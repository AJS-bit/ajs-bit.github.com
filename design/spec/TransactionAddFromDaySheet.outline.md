# TransactionAddFromDaySheet — 블록 개요

원본 `canvas/TransactionAddFromDaySheet.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div`
  `width:960px height:850px background:#EDF0F7 color:#101828 padding:28px 30px 30px display:flex flex-direction:column gap:10px`
  - `span` **text 11px/600** — “구현 참고 · 앱 화면이 아닙니다”
    `font-size:11px font-weight:600 letter-spacing:0.02em color:#475467 border:1px solid #E3E8F1 background:#FFFFFF border-radius:99px padding:4px 10px white-space:nowrap`
  - `h2` **text 20px/700** — “거래 추가 — 하루 시트에서 넘어왔을 때”
    `font-size:20px font-weight:700 letter-spacing:-0.025em color:#101828`
  - `p` **text 13px/400** — “하루 시트 아래의 링크 「저축·투자로 기록 ›」를 누르면 소비 탭의 거래 추가 창이 이 모습으로 열립니다. 왼쪽 창”
    `font-size:13px line-height:1.55 color:#626D88`
  - `div`
    `display:flex gap:28px align-items:flex-start`
    - `div`
      `width:390px`
      - `div`
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:26px 26px 18px 18px display:flex flex-direction:column color:#101828`
        - `div`
          `display:flex justify-content:center padding:9px 0 0`
        - `div`
          `display:flex align-items:center justify-content:space-between gap:10px padding:12px 18px 13px border-bottom:1px solid #EFF2F8`
        - `div`
          `padding:14px 18px 14px display:flex flex-direction:column gap:15px`
        - `div`
          `display:flex gap:10px padding:12px 18px 20px border-top:1px solid #EFF2F8`
    - `div`
      `flex:1 display:flex flex-direction:column gap:12px`
      - `div` **Card(18)**
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:4px 16px`
        - `div`
          `display:flex gap:11px padding:10px 0 border-bottom:1px solid #F3F5FA`
        - `div`
          `display:flex gap:11px padding:10px 0 border-bottom:1px solid #F3F5FA`
        - `div`
          `display:flex gap:11px padding:10px 0 border-bottom:1px solid #F3F5FA`
        - `div`
          `display:flex gap:11px padding:10px 0`
      - `div` **Card(18)**
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 16px`
        - `div` **text 12px/700** — “어디서 와서 어디로 가나”
          `font-size:12px font-weight:700 color:#101828`
        - `div`
          `display:flex align-items:center flex-wrap:wrap gap:6px margin-top:9px`
        - `p` **text 12px/400** — “하루 시트에는 거래 종류 · 잔액 반영 · 계좌 선택이 없어서, 저축·투자와 대출상환은 이 창에서 남깁니다. 소비율”
          `font-size:12px line-height:1.55 color:#626D88`
