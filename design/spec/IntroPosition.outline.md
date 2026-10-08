# IntroPosition — 블록 개요

원본 `canvas/IntroPosition.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div` **화면프레임**
  `width:390px height:844px background:#EDF0F7 color:#101828 display:flex flex-direction:column`
  - `div`
    `flex:1 min-height:0 display:flex flex-direction:column padding:0 20px`
    - `div`
      `display:flex align-items:center justify-content:space-between gap:8px height:56px margin-top:8px`
      - `div`
        `display:flex align-items:center gap:8px`
        - `div`
          `width:32px height:32px border-radius:10px`
        - `span` **text 12px/500** — “소개 1 / 3”
          `font-size:12px font-weight:500 color:#626D88`
      - `span` **text 13px/600** — “건너뛰기”
        `font-size:13px font-weight:600 color:#3556E6`
    - `div`
      `margin-top:36px display:flex flex-direction:column gap:10px`
      - `div` **Card(18)**
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px 10px`
        - `span` **text 14px/600** — “이번 달 소비 기록”
          `display:block font-size:14px font-weight:600 line-height:1.4 color:#101828`
        - `div`
          `display:flex justify-content:space-between margin-top:8px`
      - `div` **HeroCard**
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:14px 16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
        - `div`
          `display:flex align-items:center justify-content:space-between gap:8px`
        - `div`
          `margin-top:8px`
        - `div` **text 13px/500** — “월급 360만원 중 112만원 썼어요”
          `font-size:13px font-weight:500 color:#475467 margin-top:5px`
        - `div`
          `margin-top:12px`
    - `span` **text 11px/600** — “현재 위치”
      `display:block margin-top:30px font-size:11px font-weight:600 letter-spacing:0.07em color:#3556E6`
    - `h1` — “쓴 돈을 달력에 숫자만 적으면 월급의 썼는지 바로 보여요”
      `font-size:23px font-weight:700 letter-spacing:-0.03em line-height:1.4 color:#101828`
      - `br`
      - `span` — “몇 %를”
        `white-space:nowrap`
    - `p`
      `display:flex align-items:flex-start gap:6px font-size:13.5px line-height:1.5 color:#475467`
      - `span`
        `margin-top:2px`
      - `span` — “은행 · 카드 연결 없이 직접 적고, 이 폰에만 저장돼요.”
    - `div`
      `margin-top:auto display:flex flex-direction:column gap:16px`
      - `div`
        `display:flex align-items:center justify-content:center gap:6px`
        - `span` **ProgressTrack**
          `width:18px height:6px border-radius:99px background:#3556E6`
        - `span` **ProgressTrack**
          `width:6px height:6px border-radius:99px background:#CFD7E6`
        - `span` **ProgressTrack**
          `width:6px height:6px border-radius:99px background:#CFD7E6`
      - `div` **text 16px/600** — “다음”
        `display:flex align-items:center justify-content:center gap:6px height:52px width:100% border-radius:14px background:#3556E6 border:none color:#FFFFFF font-size:16px font-weight:600`
