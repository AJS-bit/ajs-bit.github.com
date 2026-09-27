# HomeLayoutEdit — 블록 개요

원본 `canvas/HomeLayoutEdit.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div` **화면프레임**
  `width:390px height:844px position:relative background:#E9EDFD color:#101828`
  - `div`
    `position:absolute left:0 right:0 bottom:0 height:12px background:#FFFFFF border-top:1px solid #E3E8F1`
  - `div`
    `position:absolute inset:0 background:rgba(0,0,0,.1)`
  - `div`
    `position:absolute left:0 top:12px width:390px height:820px background:#EDF0F7 box-shadow:0 0 0 1px rgba(16,24,40,.1) display:flex flex-direction:column`
    - `div`
      `padding:0 20px`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:8px height:56px margin-top:8px`
        - `h1` **text 20px/700** — “홈 구성”
          `font-size:20px font-weight:700 letter-spacing:-0.03em color:#101828`
        - `div`
          `width:36px height:36px border-radius:11px background:#F4F6FB display:flex align-items:center justify-content:center`
    - `div`
      `flex:1 min-height:0 padding:0 20px display:flex flex-direction:column`
      - `div`
        `display:flex flex-direction:column`
        - `p` — “이번 달 소비와 소비 기록 달력은 늘 맨 위에 있어요. 그 아래에 둘 카드를 4개까지 골라 주세요.”
          `font-size:13.5px line-height:1.5 color:#475467`
        - `div`
          `margin-top:12px`
        - `div`
          `margin-top:12px`
        - `div`
          `margin-top:8px`
        - `div`
          `margin-top:10px`
    - `div`
      `padding:8px 20px 24px display:flex flex-direction:column gap:8px background:#EDF0F7`
      - `div` **text 16px/600** — “저장”
        `display:flex align-items:center justify-content:center gap:6px height:52px width:100% border-radius:14px background:#3556E6 border:none color:#FFFFFF font-size:16px font-weight:600`
