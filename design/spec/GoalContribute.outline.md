# GoalContribute — 블록 개요

원본 `canvas/GoalContribute.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div` **화면프레임**
  `width:390px height:844px background:#2A3245 color:#101828 display:flex flex-direction:column`
  - `div`
    `height:60px display:flex align-items:flex-end justify-content:center`
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
        - `h2` **text 18px/700** — “비상금 6개월 적립액 추가”
          `font-size:18px font-weight:700 letter-spacing:-0.025em color:#101828`
        - `p` **text 12.5px/400** — “이 목적지의 적립 기록만 갱신합니다.”
          `font-size:12.5px line-height:1.45 color:#626D88`
      - `div`
        `width:36px height:36px border-radius:11px background:#F4F6FB display:flex align-items:center justify-content:center`
    - `div`
      `flex:1 min-height:0 padding:14px 18px 0 display:flex flex-direction:column gap:15px`
      - `div` **Card(18)**
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px 15px`
        - `div`
          `display:flex align-items:center gap:13px`
      - `div`
        - `div`
          `flex:1`
        - `div`
          `display:flex gap:7px margin-top:10px flex-wrap:wrap`
      - `div` **Card(18)**
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 15px`
        - `div`
          `display:flex align-items:center justify-content:space-between gap:8px`
        - `div`
          `margin-top:4px`
      - `div` **Callout(info)**
        `display:flex gap:8px padding:10px 11px background:#F4F6FB border-radius:12px`
        - `span`
          `margin-top:1px`
        - `span` — “이 기록은 바꿉니다. 통장 잔액이나 소비 거래에 중복 반영되지 않아요.”
          `font-size:11.5px line-height:1.5 color:#626D88`
      - `div` **Card(18)**
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 15px`
        - `div`
          `display:flex align-items:center justify-content:space-between gap:8px`
        - `div`
          `margin-top:6px`
    - `div`
      `display:flex gap:10px padding:12px 18px 20px border-top:1px solid #EFF2F8`
      - `div` **SecondaryButton(48)** — “취소”
        `display:flex align-items:center justify-content:center gap:6px height:48px flex:1 border-radius:13px background:#FFFFFF border:1px solid #D7DEEA color:#475467 font-size:15px font-weight:600`
      - `div` **PrimaryButton(48)** — “적립액 추가”
        `display:flex align-items:center justify-content:center gap:6px height:48px flex:1.4 border-radius:13px background:#3556E6 border:none color:#FFFFFF font-size:15px font-weight:600`
