# Future — 블록 개요

원본 `canvas/Future.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div`
  `width:390px height:1204px background:#EDF0F7 color:#101828 display:flex flex-direction:column`
  - `div`
    `display:flex flex-direction:column gap:10px padding:14px 16px 12px`
    - `div`
      `display:flex align-items:flex-start justify-content:space-between gap:8px`
      - `div`
        `display:flex align-items:center gap:4px min-height:36px`
        - `h1` **text 21px/700** — “미래”
          `font-size:21px font-weight:700 letter-spacing:-0.03em line-height:1.25 color:#101828`
        - `span`
          `width:28px height:28px border-radius:99px display:inline-flex align-items:center justify-content:center`
      - `div`
        `display:flex align-items:flex-start gap:0`
        - `div`
          `width:44px display:flex flex-direction:column align-items:center`
        - `div`
          `width:44px display:flex flex-direction:column align-items:center`
        - `div`
          `width:44px display:flex flex-direction:column align-items:center`
    - `div`
      `display:flex gap:4px background:#E3E8F1 border-radius:12px padding:3px`
      - `div` **SegmentedItem** — “자산 경로”
        `flex:1 height:36px border-radius:9px background:#FFFFFF display:flex align-items:center justify-content:center font-size:13.5px font-weight:600 color:#101828 box-shadow:0 1px 2px rgba(16,24,40,.06)`
      - `div` **SegmentedItem** — “상환 계획”
        `flex:1 height:36px border-radius:9px display:flex align-items:center justify-content:center font-size:13.5px font-weight:500 color:#5B6880`
  - `div` **본문(스크롤 영역)**
    `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
    - `div` **HeroCard**
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:14px 14px 13px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
      - `div`
        `display:flex align-items:center gap:8px padding:0 2px`
        - `span` **text 11px/500** — “기간”
          `font-size:11px font-weight:500 color:#626D88 width:52px`
        - `div`
          `display:flex gap:5px flex:1`
      - `div`
        `display:flex align-items:center gap:8px margin-top:6px padding:0 2px`
        - `span` **text 11px/500** — “투자 환경”
          `font-size:11px font-weight:500 color:#626D88 width:52px`
        - `div`
          `display:flex gap:5px flex:1`
      - `div` — “앞으로 모을 돈에만 붙는 연 수익률이에요 · 보통 5.0%는 설정의 투자 자산 기본 수익률 ·”
        `font-size:11.5px line-height:1.5 color:#626D88 margin-top:7px padding:0 2px`
        - `span` — “바꾸기 ›”
          `font-weight:600 color:#3556E6 white-space:nowrap`
      - `div`
        `display:flex align-items:flex-end justify-content:space-between gap:10px margin-top:14px padding:0 2px`
        - `div`
        - `div`
          `display:flex flex-direction:column align-items:flex-end gap:1px`
      - `div`
        `margin-top:10px`
      - `div`
        `display:flex align-items:center gap:12px margin-top:6px padding:0 2px`
        - `span` — “보통 3.82억”
          `display:inline-flex align-items:center gap:5px font-size:11px color:#475467`
        - `span` — “범위 2.8억 ~ 5.47억”
          `display:inline-flex align-items:center gap:5px font-size:11px color:#475467`
      - `p` — “물가 · 세금은 빼고 계산했어요 ·”
        `padding:0 2px font-size:11.5px line-height:1.45 color:#626D88`
        - `span` — “자세히 ›”
          `font-weight:600 color:#3556E6`
    - `div` **Card(18)**
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 14px 5px`
      - `div`
        `display:flex align-items:center gap:6px`
        - `span` **text 14px/600** — “다음 자산 지점”
          `font-size:14px font-weight:600 color:#101828`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:8px height:40px border-top:1px solid #F3F5FA`
        - `span` **text 13.5px/600** — “1억원”
          `font-size:13.5px font-weight:600 color:#101828`
        - `div`
          `display:flex align-items:baseline gap:8px`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:8px height:40px border-top:1px solid #F3F5FA`
        - `span` **text 13.5px/600** — “1억 5,000만원”
          `font-size:13.5px font-weight:600 color:#101828`
        - `div`
          `display:flex align-items:baseline gap:8px`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:8px height:40px border-top:1px solid #F3F5FA`
        - `span` **text 13.5px/600** — “2억원”
          `font-size:13.5px font-weight:600 color:#101828`
        - `div`
          `display:flex align-items:baseline gap:8px`
    - `div` **Card(18)**
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:11px 14px 11px`
      - `div`
        `display:flex align-items:center justify-content:flex-end gap:8px min-height:25px`
        - `span` **text 13px/600** — “10년 뒤 +0원”
          `font-size:13px font-weight:600 color:#475467 white-space:nowrap`
      - `p` **text 13.5px/600** — “한 달에 얼마를 아끼면? 밀어서 시험해 보세요”
        `font-size:13.5px font-weight:600 letter-spacing:-0.015em color:#101828`
      - `div`
        `display:flex align-items:center gap:9px margin-top:6px`
        - `span` **text 11px/400** — “0원”
          `font-size:11px color:#697182 white-space:nowrap`
        - `div`
          `position:relative height:20px flex:1`
        - `span` **text 11px/400** — “45만원”
          `font-size:11px color:#697182 white-space:nowrap`
      - `div` **text 11.5px/400** — “줄인 만큼은 모두 매달 모으는 돈에 더한다고 봐요.”
        `font-size:11.5px line-height:1.45 color:#626D88 margin-top:7px`
    - `div` **Card(18)**
      `display:flex align-items:center justify-content:space-between gap:8px height:70px padding:12px 14px background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px`
      - `span` **text 12.5px/600** — “투자 환경별 비교 · 전체 경로”
        `font-size:12.5px font-weight:600 color:#475467`
    - `div` **Card(18)**
      `height:86px padding:13px background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:8px height:58px padding:0 18px`
        - `span` **text 15px/650** — “계산 방법 자세히”
          `font-size:15px font-weight:650 color:#101828`
    - `div`
      `display:flex gap:8px padding:2px 4px 0 margin-top:21px`
      - `span` **text 11px/400** — “앞으로의 금액은 100만원 단위로 어림해 「약」을 붙였어요. 지금 금액은 입력한 그대로예요. 지금 넣은 값으로 그린”
        `font-size:11px line-height:1.65 color:#626D88`
  - `div` **BottomNav**
    `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`
    - `div`
      `display:flex flex-direction:column align-items:center gap:3px flex:1`
      - `div`
        `width:40px height:24px display:flex align-items:center justify-content:center`
      - `span` **text 11px/500** — “홈”
        `font-size:11px font-weight:500 color:#606B7D`
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
      - `span` **text 11px/500** — “목적지”
        `font-size:11px font-weight:500 color:#606B7D`
    - `div`
      `display:flex flex-direction:column align-items:center gap:3px flex:1`
      - `div`
        `width:40px height:24px border-radius:99px background:#E9EDFD display:flex align-items:center justify-content:center`
      - `span` **text 11px/600** — “미래”
        `font-size:11px font-weight:600 color:#3556E6`
