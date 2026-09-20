# CalendarCells — 블록 개요

원본 `canvas/CalendarCells.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div`
  `width:1330px height:820px background:#EDF0F7 color:#101828 padding:28px 30px 30px display:flex flex-direction:column gap:10px`
  - `span` **text 11px/600** — “구현 참고 · 앱 화면이 아닙니다”
    `font-size:11px font-weight:600 letter-spacing:0.02em color:#475467 border:1px solid #E3E8F1 background:#FFFFFF border-radius:99px padding:4px 10px`
  - `h2` **text 20px/700** — “달력 칸 읽는 법”
    `font-size:20px font-weight:700 letter-spacing:-0.025em color:#101828`
  - `p` **text 13px/400** — “칸의 숫자는 그날 소비 합계입니다(고정비 포함 · 이체 제외). 왼쪽 달력의 번호를 가운데에서 찾으세요.”
    `font-size:13px line-height:1.55 color:#626D88`
  - `div`
    `display:flex gap:28px align-items:flex-start`
    - `div`
      `width:362px`
      - `div` **Card(18)**
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 14px 13px`
        - `div`
          `display:flex align-items:center justify-content:space-between gap:6px min-height:32px`
        - `div`
          `display:grid grid-template-columns:repeat(7, minmax(0, 1fr)) margin-top:8px`
        - `div`
          `display:flex flex-direction:column border-bottom:1px solid #EFF2F8`
        - `div` **text 11px/400** — “9월 기록한 소비 124,000원 · 오늘 4건 37,000원”
          `font-size:11px line-height:1.5 color:#475467 margin-top:8px`
        - `div`
          `display:flex align-items:center justify-content:space-between height:32px margin-top:2px border-top:1px solid #EFF2F8`
    - `div`
      `width:490px`
      - `div` **Card(18)**
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:4px 16px`
        - `div`
          `display:flex gap:11px padding:10px 0 border-bottom:1px solid #F3F5FA`
        - `div`
          `display:flex gap:11px padding:10px 0 border-bottom:1px solid #F3F5FA`
        - `div`
          `display:flex gap:11px padding:10px 0 border-bottom:1px solid #F3F5FA`
        - `div`
          `display:flex gap:11px padding:10px 0 border-bottom:1px solid #F3F5FA`
        - `div`
          `display:flex gap:11px padding:10px 0 border-bottom:1px solid #F3F5FA`
        - `div`
          `display:flex gap:11px padding:10px 0 border-bottom:1px solid #F3F5FA`
        - `div`
          `display:flex gap:11px padding:10px 0 border-bottom:1px solid #F3F5FA`
        - `div`
          `display:flex gap:11px padding:10px 0 border-bottom:1px solid #F3F5FA`
        - `div`
          `display:flex gap:11px padding:10px 0`
      - `p` — “접힌 최근 7일 줄에는 달 제목이 없어서 지난달 날짜를 처럼 달을 붙여 씁니다. 6일 칸은 안 쓴 날로 표시했고 이”
        `font-size:12px line-height:1.6 color:#626D88`
        - `b` — “8/31”
          `font-weight:600 color:#475467`
    - `div`
      `width:362px display:flex flex-direction:column gap:22px`
      - `div`
        `width:362px display:flex flex-direction:column gap:8px`
        - `div`
        - `div`
          `position:relative`
      - `div` **Card(18)**
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 16px`
        - `div` **text 13.5px/700** — “칸에 금액을 쓰는 법”
          `font-size:13.5px font-weight:700 color:#101828`
        - `div`
          `display:flex align-items:center gap:12px padding:9px 0 border-bottom:1px solid #F3F5FA`
        - `div`
          `display:flex align-items:center gap:12px padding:9px 0 border-bottom:1px solid #F3F5FA`
        - `div`
          `display:flex align-items:center gap:12px padding:9px 0 border-bottom:1px solid #F3F5FA`
        - `div`
          `display:flex align-items:center gap:12px padding:9px 0 border-bottom:1px solid #F3F5FA`
        - `div`
          `display:flex align-items:center gap:12px padding:9px 0`
        - `div` **text 12px/400** — “상태 줄 · 기록 창 · 저장 완료 카드의 합계는 줄이지 않고 원 단위 그대로 씁니다(오늘 4건 37,000원).”
          `font-size:12px line-height:1.5 color:#626D88 border-top:1px solid #F3F5FA`
