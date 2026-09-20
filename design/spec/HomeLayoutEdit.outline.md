# HomeLayoutEdit — 블록 개요

원본 `canvas/HomeLayoutEdit.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div` **화면프레임**
  `width:390px height:844px background:#EDF0F7 color:#101828 display:flex flex-direction:column`
  - `div`
    `padding:0 20px`
    - `div`
      `display:flex align-items:center justify-content:space-between gap:8px height:56px margin-top:8px`
      - `h1` **text 20px/700** — “홈 구성”
        `font-size:20px font-weight:700 letter-spacing:-0.03em color:#101828`
      - `div`
        `width:36px height:36px border-radius:11px background:#F4F6FB display:flex align-items:center justify-content:center`
  - `div`
    `flex:1 min-height:0 padding:0 20px`
    - `div`
      `display:flex flex-direction:column margin-top:0px`
      - `p` — “소비율은 늘 맨 위에 있어요. 그 아래에 둘 카드를 5개까지 골라 주세요.”
        `font-size:13.5px line-height:1.5 color:#475467`
        - `br`
      - `div`
        `margin-top:12px`
        - `div` **Card(18)**
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:0 14px`
      - `div`
        `margin-top:12px`
        - `div`
          `display:flex align-items:center justify-content:space-between gap:8px`
      - `div`
        `margin-top:8px`
        - `div` **Card(18)**
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:0 14px`
      - `p` **text 11.5px/400** — “달력을 꺼도 소비 기록하기는 오늘 기록을 열어요. 확인할 내용은 소비 탭 알림에서 볼 수 있어요.”
        `font-size:11.5px line-height:1.5 color:#626D88`
      - `div`
        `margin-top:10px`
        - `div` **Card(18)**
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
  - `div`
    `padding:8px 20px 24px display:flex flex-direction:column gap:8px`
    - `div` **text 16px/600** — “저장”
      `display:flex align-items:center justify-content:center gap:6px height:52px width:100% border-radius:14px background:#3556E6 border:none color:#FFFFFF font-size:16px font-weight:600`
