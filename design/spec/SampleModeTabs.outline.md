# SampleModeTabs — 블록 개요

원본 `canvas/SampleModeTabs.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div`
  `width:1290px height:823px background:#EDF0F7 color:#101828 padding:28px 30px 30px display:flex flex-direction:column gap:10px`
  - `span` **text 11px/600** — “구현 참고 · 앱 화면이 아닙니다”
    `font-size:11px font-weight:600 letter-spacing:0.02em color:#475467 border:1px solid #E3E8F1 background:#FFFFFF border-radius:99px padding:4px 10px`
  - `h2` **text 20px/700** — “샘플 모드 — 모든 탭 맨 위 띠”
    `font-size:20px font-weight:700 letter-spacing:-0.025em color:#101828`
  - `p` **text 13px/400** — “샘플로 둘러보는 동안 다섯 탭 모두 머리줄 위에 같은 띠가 있습니다.”
    `font-size:13px line-height:1.55 color:#626D88`
  - `div`
    `display:flex gap:20px flex-wrap:wrap`
    - `div`
      `display:flex flex-direction:column gap:8px`
      - `div` **text 14px/700** — “홈”
        `font-size:14px font-weight:700 color:#101828`
      - `div`
        `width:392px height:196px border-radius:22px border:1px solid #E3E8F1 background:#EDF0F7`
        - `div`
          `width:390px height:1537px background:#EDF0F7 color:#101828 display:flex flex-direction:column`
    - `div`
      `display:flex flex-direction:column gap:8px`
      - `div` **text 14px/700** — “자산”
        `font-size:14px font-weight:700 color:#101828`
      - `div`
        `width:392px height:196px border-radius:22px border:1px solid #E3E8F1 background:#EDF0F7`
        - `div` **SampleBanner**
          `display:flex align-items:center justify-content:space-between gap:8px height:32px padding:0 14px background:#E9EDFD`
        - `div`
          `width:390px height:977px background:#EDF0F7 color:#101828 display:flex flex-direction:column`
    - `div`
      `display:flex flex-direction:column gap:8px`
      - `div` **text 14px/700** — “소비”
        `font-size:14px font-weight:700 color:#101828`
      - `div`
        `width:392px height:196px border-radius:22px border:1px solid #E3E8F1 background:#EDF0F7`
        - `div` **SampleBanner**
          `display:flex align-items:center justify-content:space-between gap:8px height:32px padding:0 14px background:#E9EDFD`
        - `div`
          `width:390px height:957px background:#EDF0F7 color:#101828 display:flex flex-direction:column`
    - `div`
      `display:flex flex-direction:column gap:8px`
      - `div` **text 14px/700** — “목적지”
        `font-size:14px font-weight:700 color:#101828`
      - `div`
        `width:392px height:196px border-radius:22px border:1px solid #E3E8F1 background:#EDF0F7`
        - `div` **SampleBanner**
          `display:flex align-items:center justify-content:space-between gap:8px height:32px padding:0 14px background:#E9EDFD`
        - `div`
          `width:390px height:992px background:#EDF0F7 color:#101828 display:flex flex-direction:column`
    - `div`
      `display:flex flex-direction:column gap:8px`
      - `div` **text 14px/700** — “미래”
        `font-size:14px font-weight:700 color:#101828`
      - `div`
        `width:392px height:196px border-radius:22px border:1px solid #E3E8F1 background:#EDF0F7`
        - `div` **SampleBanner**
          `display:flex align-items:center justify-content:space-between gap:8px height:32px padding:0 14px background:#E9EDFD`
        - `div`
          `width:390px height:1204px background:#EDF0F7 color:#101828 display:flex flex-direction:column`
  - `div` **Card(18)**
    `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:10px 18px 8px`
    - `div` **text 12px/700** — “구현 메모”
      `font-size:12px font-weight:700 color:#101828 padding:2px 0 4px`
    - `div`
      `display:flex gap:10px padding:7px 0 border-bottom:1px solid #F3F5FA`
      - `span` **text 10.5px/700** — “1”
        `margin-top:1px width:17px height:17px border-radius:99px background:#101828 color:#FFFFFF font-size:10.5px font-weight:700 display:inline-flex align-items:center justify-content:center box-shadow:0 0 0 2px #FFFFFF`
      - `div` — “샘플 모드에서는 모든 탭 머리줄 위에 띠 하나 ‘ ’만 둡니다. 다른 샘플 안내 · 저장 안내는 없습니다.”
        `font-size:12px line-height:1.55 color:#475467`
        - `b` — “샘플 데이터로 둘러보는 중 · 내 데이터로 시작 ›”
          `font-weight:600 color:#101828`
    - `div`
      `display:flex gap:10px padding:7px 0 border-bottom:1px solid #F3F5FA`
      - `span` **text 10.5px/700** — “2”
        `margin-top:1px width:17px height:17px border-radius:99px background:#101828 color:#FFFFFF font-size:10.5px font-weight:700 display:inline-flex align-items:center justify-content:center box-shadow:0 0 0 2px #FFFFFF`
      - `div` — “‘ ’을 누르면 파란 확인 창 ‘ ’(상태 페이지 StorageStates D) → 월급 입력 시트가 열립니다.”
        `font-size:12px line-height:1.55 color:#475467`
        - `b` — “내 데이터로 시작 ›”
          `font-weight:600 color:#101828`
        - `b` — “샘플을 치우고 내 데이터로 시작할까요?”
          `font-weight:600 color:#101828`
    - `div`
      `display:flex gap:10px padding:7px 0`
      - `span` **text 10.5px/700** — “3”
        `margin-top:1px width:17px height:17px border-radius:99px background:#101828 color:#FFFFFF font-size:10.5px font-weight:700 display:inline-flex align-items:center justify-content:center box-shadow:0 0 0 2px #FFFFFF`
      - `div` — “그림은 각 탭의 머리줄 · 세그먼트까지만 자리). 샘플 홈 전체는 HomeSampleMode 장 — 샘플은 지난달들”
        `font-size:12px line-height:1.55 color:#475467`
        - `span` — “잘랐습니다(띠의”
          `white-space:nowrap`
