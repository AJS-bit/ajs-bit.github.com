# HomeCalendarPrev — 블록 개요

원본 `canvas/HomeCalendarPrev.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div` **화면프레임**
  `width:390px height:844px background:#EDF0F7 color:#101828 display:flex flex-direction:column`
  - `div` **본문(스크롤 영역)**
    `flex:1 min-height:0 display:flex flex-direction:column gap:9px padding:0 14px`
    - `div`
      `height:22px background:#FFFFFF border:1px solid #E3E8F1 border-top:none border-radius:0 0 20px 20px opacity:.55`
    - `div` **Card(18)**
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 14px 13px`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:6px min-height:32px`
        - `div`
          `display:flex align-items:center gap:4px`
        - `div`
          `display:flex align-items:center gap:8px`
      - `div` **text 12px/400** — “날짜를 누르면 그날 쓴 돈을 적어요”
        `font-size:12px line-height:1.45 color:#626D88 margin-top:6px`
      - `div`
        `display:grid grid-template-columns:repeat(7, minmax(0, 1fr)) margin-top:8px`
        - `span` **text 11px/500** — “일”
          `text-align:center font-size:11px font-weight:500 color:#626D88`
        - `span` **text 11px/500** — “월”
          `text-align:center font-size:11px font-weight:500 color:#626D88`
        - `span` **text 11px/500** — “화”
          `text-align:center font-size:11px font-weight:500 color:#626D88`
        - `span` **text 11px/500** — “수”
          `text-align:center font-size:11px font-weight:500 color:#626D88`
        - `span` **text 11px/500** — “목”
          `text-align:center font-size:11px font-weight:500 color:#626D88`
        - `span` **text 11px/500** — “금”
          `text-align:center font-size:11px font-weight:500 color:#626D88`
        - `span` **text 11px/500** — “토”
          `text-align:center font-size:11px font-weight:500 color:#626D88`
      - `div`
        `display:flex flex-direction:column border-bottom:1px solid #EFF2F8`
        - `div`
          `display:grid grid-template-columns:repeat(7, minmax(0, 1fr)) border-top:1px solid #EFF2F8 padding:2px 0`
        - `div`
          `display:grid grid-template-columns:repeat(7, minmax(0, 1fr)) border-top:1px solid #EFF2F8 padding:2px 0`
        - `div`
          `display:grid grid-template-columns:repeat(7, minmax(0, 1fr)) border-top:1px solid #EFF2F8 padding:2px 0`
        - `div`
          `display:grid grid-template-columns:repeat(7, minmax(0, 1fr)) border-top:1px solid #EFF2F8 padding:2px 0`
        - `div`
          `display:grid grid-template-columns:repeat(7, minmax(0, 1fr)) border-top:1px solid #EFF2F8 padding:2px 0`
        - `div`
          `display:grid grid-template-columns:repeat(7, minmax(0, 1fr)) border-top:1px solid #EFF2F8 padding:2px 0`
      - `div` **text 12.5px/400** — “8월 기록한 소비 1,715,200원”
        `font-size:12.5px line-height:1.5 color:#475467 margin-top:8px`
      - `div`
        `display:flex align-items:center justify-content:space-between height:32px margin-top:6px border-top:1px solid #EFF2F8`
        - `span` **text 12.5px/600** — “확인할 내용 2개”
          `font-size:12.5px font-weight:600 color:#101828`
    - `div` **TurnCard**
      `display:flex gap:12px background:#FFFFFF border:1px solid #E3E8F1 border-left:3px solid #DE8A2A border-radius:18px padding:13px 14px`
      - `div`
        `width:34px height:34px border-radius:11px background:#FDF1E0 display:flex align-items:center justify-content:center`
      - `div`
        `display:flex flex-direction:column gap:3px`
        - `span` **text 11px/600** — “다음 안내”
          `font-size:11px font-weight:600 letter-spacing:0.06em color:#B45309`
        - `span` **text 15px/600** — “카드 할부 금리 14.5%부터 줄여보세요”
          `font-size:15px font-weight:600 letter-spacing:-0.015em line-height:1.35 color:#101828`
        - `span` **text 12.5px/400** — “고금리 부채는 자산이 자라는 속도를 가장 크게 낮춰요.”
          `font-size:12.5px line-height:1.45 color:#475467`
        - `span` **text 12.5px/600** — “상환 전략 보기 ›”
          `font-size:12.5px font-weight:600 color:#3556E6 margin-top:5px`
  - `div` **BottomNav**
    `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`
    - `div`
      `display:flex flex-direction:column align-items:center gap:3px flex:1`
      - `div`
        `width:40px height:24px border-radius:99px background:#E9EDFD display:flex align-items:center justify-content:center`
      - `span` **text 11px/600** — “홈”
        `font-size:11px font-weight:600 color:#3556E6`
    - `div`
      `display:flex flex-direction:column align-items:center gap:3px flex:1`
      - `div`
        `width:40px height:24px display:flex align-items:center justify-content:center`
      - `span` **text 11px/500** — “자산”
        `font-size:11px font-weight:500 color:#606B7D`
    - `div`
      `display:flex flex-direction:column align-items:center gap:3px flex:1`
      - `div`
        `width:40px height:24px display:flex align-items:center justify-content:center`
      - `span` **text 11px/500** — “소비”
        `font-size:11px font-weight:500 color:#606B7D`
    - `div`
      `display:flex flex-direction:column align-items:center gap:3px flex:1`
      - `div`
        `width:40px height:24px display:flex align-items:center justify-content:center`
      - `span` **text 11px/500** — “목표”
        `font-size:11px font-weight:500 color:#606B7D`
    - `div`
      `display:flex flex-direction:column align-items:center gap:3px flex:1`
      - `div`
        `width:40px height:24px display:flex align-items:center justify-content:center`
      - `span` **text 11px/500** — “미래”
        `font-size:11px font-weight:500 color:#606B7D`
