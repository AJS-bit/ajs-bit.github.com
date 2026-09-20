# HomeSetup — 블록 개요

원본 `canvas/HomeSetup.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div` **화면프레임**
  `width:390px height:844px background:#EDF0F7 color:#101828 display:flex flex-direction:column`
  - `div`
    `flex:1 min-height:0 display:flex flex-direction:column padding:0 20px`
    - `div`
      `display:flex align-items:center justify-content:space-between gap:8px height:56px margin-top:8px`
      - `div`
        `display:flex align-items:center gap:8px`
        - `div`
          `width:28px height:28px border-radius:9px background:linear-gradient(140deg, #3556E6 0%, #7A3FE4 100%) display:flex align-items:center justify-content:center`
        - `span` **text 12px/500** — “홈 구성”
          `font-size:12px font-weight:500 color:#626D88`
      - `span` **text 13px/600** — “건너뛰기”
        `font-size:13px font-weight:600 color:#3556E6`
    - `h1` **text 22px/700** — “홈에 무엇을 둘까요?”
      `font-size:22px font-weight:700 letter-spacing:-0.03em line-height:1.35 color:#101828`
    - `p` — “소비율은 늘 맨 위에 있어요. 그 아래에 둘 카드를 5개까지 골라 주세요.”
      `font-size:13.5px line-height:1.5 color:#475467`
      - `br`
    - `div`
      `margin-top:12px`
      - `div` **Card(18)**
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:0 14px`
        - `div`
          `display:flex align-items:center gap:10px height:48px`
    - `div`
      `margin-top:12px`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:8px`
        - `div`
          `display:flex align-items:baseline gap:7px`
        - `span` **text 12px/600** — “4 / 5 선택”
          `font-size:12px font-weight:600 color:#626D88`
    - `div`
      `margin-top:8px`
      - `div` **Card(18)**
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:0 14px`
        - `div`
          `display:flex align-items:center gap:12px height:52px border-bottom:1px solid #F3F5FA`
        - `div`
          `display:flex align-items:center gap:12px height:52px border-bottom:1px solid #F3F5FA`
        - `div`
          `display:flex align-items:center gap:12px height:52px border-bottom:1px solid #F3F5FA`
        - `div`
          `display:flex align-items:center gap:12px height:52px border-bottom:1px solid #F3F5FA`
        - `div`
          `display:flex align-items:center gap:12px height:52px border-bottom:1px solid #F3F5FA`
        - `div`
          `display:flex align-items:center gap:12px height:52px border-bottom:1px solid #F3F5FA`
        - `div`
          `display:flex align-items:center gap:12px height:52px`
    - `div`
      `margin-top:10px`
      - `div` **Card(18)**
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
        - `div`
          `display:flex align-items:flex-start gap:12px`
    - `div`
      `margin-top:auto display:flex flex-direction:column gap:8px`
      - `div` **text 16px/600** — “이 구성으로 시작”
        `display:flex align-items:center justify-content:center gap:6px height:52px width:100% border-radius:14px background:#3556E6 border:none color:#FFFFFF font-size:16px font-weight:600`
      - `p` **text 11.5px/400** — “언제든 설정 › 홈 구성에서 바꿀 수 있어요.”
        `text-align:center font-size:11.5px line-height:1.5 color:#626D88`
