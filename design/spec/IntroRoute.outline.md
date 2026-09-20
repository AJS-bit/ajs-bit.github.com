# IntroRoute — 블록 개요

원본 `canvas/IntroRoute.dc.html`. 값이 다르면 **원본이 맞습니다.**

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
        - `span` **text 12px/500** — “소개 2 / 3”
          `font-size:12px font-weight:500 color:#626D88`
      - `span` **text 13px/600** — “건너뛰기”
        `font-size:13px font-weight:600 color:#3556E6`
    - `div`
      `margin-top:36px display:flex flex-direction:column gap:10px`
      - `div` **Card(18)**
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
        - `div`
          `display:flex align-items:center justify-content:space-between gap:8px`
        - `div`
          `margin-top:16px`
      - `div` **TurnCard**
        `display:flex gap:12px background:#FFFFFF border:1px solid #E3E8F1 border-left:3px solid #DE8A2A border-radius:18px padding:13px 14px`
        - `div`
          `width:34px height:34px border-radius:11px background:#FDF1E0 display:flex align-items:center justify-content:center`
        - `div`
          `display:flex flex-direction:column gap:3px`
    - `span` **text 11px/600** — “항로”
      `display:block margin-top:30px font-size:11px font-weight:600 letter-spacing:0.07em color:#3556E6`
    - `h1` — “목표까지 얼마나 남았는지, 지금 무엇을 하면 되는지 알려줍니다.”
      `font-size:23px font-weight:700 letter-spacing:-0.03em line-height:1.4 color:#101828`
      - `br`
    - `div`
      `margin-top:auto display:flex flex-direction:column gap:16px`
      - `div`
        `display:flex align-items:center justify-content:center gap:6px`
        - `span` **ProgressTrack**
          `width:6px height:6px border-radius:99px background:#CFD7E6`
        - `span` **ProgressTrack**
          `width:18px height:6px border-radius:99px background:#3556E6`
        - `span` **ProgressTrack**
          `width:6px height:6px border-radius:99px background:#CFD7E6`
      - `div` **text 16px/600** — “다음”
        `display:flex align-items:center justify-content:center gap:6px height:52px width:100% border-radius:14px background:#3556E6 border:none color:#FFFFFF font-size:16px font-weight:600`
