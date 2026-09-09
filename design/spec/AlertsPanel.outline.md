# AlertsPanel — 블록 개요

원본 `canvas/AlertsPanel.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div` **화면프레임**
  `width:390px height:844px background:#2A3245 color:#101828 display:flex flex-direction:column`
  - `div`
    `height:40px display:flex align-items:flex-end justify-content:center`
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
        - `h2` **text 18px/700** — “알림 3건”
          `font-size:18px font-weight:700 letter-spacing:-0.025em color:#101828`
        - `p` **text 12.5px/400** — “저장된 기록을 기준으로 만든 알림이에요. 읽어도 기록은 바뀌지 않습니다.”
          `font-size:12.5px line-height:1.45 color:#626D88`
      - `div`
        `width:36px height:36px border-radius:11px background:#F4F6FB display:flex align-items:center justify-content:center`
    - `div`
      `flex:1 min-height:0 padding:14px 18px 0 display:flex flex-direction:column gap:15px`
      - `div`
        `display:flex flex-direction:column`
        - `div`
          `display:flex gap:11px min-height:60px padding:13px 0 border-bottom:1px solid #F3F5FA`
        - `div`
          `display:flex gap:11px min-height:60px padding:13px 0 border-bottom:1px solid #F3F5FA`
        - `div`
          `display:flex gap:11px min-height:60px padding:13px 0 border-bottom:1px solid #F3F5FA`
      - `div` **Callout(info)**
        `display:flex gap:8px padding:10px 11px background:#F4F6FB border-radius:12px`
        - `span`
          `margin-top:1px`
        - `span` — “자산을 넘게 갱신하지 않으면 여기에 알려드려요. 지금은 갱신이 필요한 자산이 없습니다.”
          `font-size:11.5px line-height:1.5 color:#626D88`
      - `div`
        - `div`
          `display:flex align-items:baseline justify-content:space-between gap:8px`
        - `div`
          `display:flex flex-direction:column align-items:center text-align:center padding:20px 10px background:#F4F6FB border-radius:14px`
    - `div`
      `display:flex gap:10px padding:12px 18px 20px border-top:1px solid #EFF2F8`
      - `div` **SecondaryButton(48)** — “닫기”
        `display:flex align-items:center justify-content:center gap:6px height:48px width:100% border-radius:13px background:#FFFFFF border:1px solid #D7DEEA color:#475467 font-size:15px font-weight:600`
