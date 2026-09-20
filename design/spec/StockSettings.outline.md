# StockSettings — 블록 개요

원본 `canvas/StockSettings.dc.html`. 값이 다르면 **원본이 맞습니다.**

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
        - `h2` **text 18px/700** — “주식”
          `font-size:18px font-weight:700 letter-spacing:-0.025em color:#101828`
        - `p` **text 12.5px/400** — “기준값은 처음에 넣어 둔 값일 뿐이에요. 바꿔도 앱이 좋다 나쁘다를 말하지 않아요.”
          `font-size:12.5px line-height:1.45 color:#626D88`
      - `div`
        `width:36px height:36px border-radius:11px background:#F4F6FB display:flex align-items:center justify-content:center`
    - `div`
      `flex:1 min-height:0 padding:14px 18px 0 display:flex flex-direction:column gap:15px`
      - `div`
        - `div`
          `display:flex align-items:baseline justify-content:space-between gap:8px`
        - `div`
          `display:flex align-items:center justify-content:space-between gap:10px padding:12px 13px background:#F4F6FB border-radius:14px`
      - `div`
        - `div`
          `display:flex align-items:baseline justify-content:space-between gap:8px`
        - `div` **Callout(info)**
          `display:flex align-items:center justify-content:space-between gap:8px height:48px padding:0 13px border-radius:12px background:#F4F6FB`
        - `div`
          `padding:0 13px 4px background:#F4F6FB border-radius:0 0 12px 12px margin-top:-8px`
        - `div`
          `margin-top:8px`
        - `div`
          `margin-top:8px`
      - `div`
        - `div`
          `display:flex align-items:baseline justify-content:space-between gap:8px`
        - `div` **text 15px/600** — “주식 기능 끄기”
          `display:flex align-items:center justify-content:center gap:6px height:44px width:100% border-radius:13px background:#FCEBEA border:none color:#C0342F font-size:15px font-weight:600`
        - `p` **text 11.5px/400** — “탭·홈 카드·설정 항목이 사라지고 보유·관심 기록은 남아요.”
          `font-size:11.5px line-height:1.5 color:#626D88`
    - `div`
      `display:flex gap:10px padding:12px 18px 20px border-top:1px solid #EFF2F8`
      - `div` **SecondaryButton(48)** — “취소”
        `display:flex align-items:center justify-content:center gap:6px height:48px flex:1 border-radius:13px background:#FFFFFF border:1px solid #D7DEEA color:#475467 font-size:15px font-weight:600`
      - `div` **PrimaryButton(48)** — “저장”
        `display:flex align-items:center justify-content:center gap:6px height:48px flex:1.4 border-radius:13px background:#3556E6 border:none color:#FFFFFF font-size:15px font-weight:600`
