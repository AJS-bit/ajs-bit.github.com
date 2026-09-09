# CoachPanel — 블록 개요

원본 `canvas/CoachPanel.dc.html`. 값이 다르면 **원본이 맞습니다.**

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
        - `h2` **text 18px/700** — “코칭”
          `font-size:18px font-weight:700 letter-spacing:-0.025em color:#101828`
        - `p` **text 12.5px/400** — “저장된 기록만 보고 드리는 조언이에요. 우선순위가 높은 순서입니다.”
          `font-size:12.5px line-height:1.45 color:#626D88`
      - `div`
        `width:36px height:36px border-radius:11px background:#F4F6FB display:flex align-items:center justify-content:center`
    - `div`
      `flex:1 min-height:0 padding:14px 18px 0 display:flex flex-direction:column gap:15px`
      - `div`
        `display:flex flex-direction:column gap:9px`
        - `div`
          `display:flex gap:11px padding:13px border-radius:14px background:#FFFFFF border:1px solid #E3E8F1 border-left:3px solid #C0342F`
        - `div`
          `display:flex gap:11px padding:13px border-radius:14px background:#FFFFFF border:1px solid #E3E8F1 border-left:3px solid #B45309`
        - `div`
          `display:flex gap:11px padding:13px border-radius:14px background:#FFFFFF border:1px solid #E3E8F1 border-left:3px solid #0F7B47`
      - `div` **Callout(info)**
        `display:flex align-items:center justify-content:space-between gap:8px height:48px padding:0 13px border-radius:12px background:#F4F6FB`
        - `span` **text 13.5px/600** — “다른 안내 4개 더 보기”
          `font-size:13.5px font-weight:600 color:#101828`
        - `div`
          `display:flex align-items:center gap:8px`
      - `div`
        - `div`
          `display:flex align-items:baseline justify-content:space-between gap:8px`
        - `div`
          `padding:13px background:#F1EAFD border-radius:14px border:1px dashed #B79BFF`
    - `div`
      `display:flex gap:10px padding:12px 18px 20px border-top:1px solid #EFF2F8`
      - `div` **SecondaryButton(48)** — “닫기”
        `display:flex align-items:center justify-content:center gap:6px height:48px width:100% border-radius:13px background:#FFFFFF border:1px solid #D7DEEA color:#475467 font-size:15px font-weight:600`
