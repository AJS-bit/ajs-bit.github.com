# AlertsReview — 블록 개요

원본 `canvas/AlertsReview.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div`
  `width:1200px height:1040px background:#EDF0F7 color:#101828 padding:28px 30px 30px display:flex flex-direction:column gap:10px`
  - `span` **text 11px/600** — “구현 참고 · 앱 화면이 아닙니다”
    `font-size:11px font-weight:600 letter-spacing:0.02em color:#475467 border:1px solid #E3E8F1 background:#FFFFFF border-radius:99px padding:4px 10px white-space:nowrap`
  - `h2` **text 20px/700** — “달력이 없을 때 「확인할 내용」이 보이는 곳”
    `font-size:20px font-weight:700 letter-spacing:-0.025em color:#101828`
  - `p` **text 13px/400** — “홈에 달력 카드가 없으면(껐거나 달력이 나오기 전 단계) 같은 목록을 소비 탭의 알림이 보여 줍니다. 왼쪽이 알림 ”
    `font-size:13px line-height:1.55 color:#626D88`
  - `div`
    `display:flex gap:28px align-items:flex-start`
    - `div`
      `width:390px border-radius:18px`
      - `div` **화면프레임**
        `width:390px height:844px background:#2A3245 color:#101828 display:flex flex-direction:column`
        - `div`
          `height:40px display:flex align-items:flex-end justify-content:center`
        - `div` **BottomSheet**
          `flex:1 min-height:0 background:#FFFFFF border-radius:26px 26px 0 0 display:flex flex-direction:column color:#101828`
    - `div`
      `flex:1 display:flex flex-direction:column gap:18px`
      - `div` **Card(18)**
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:4px 16px`
        - `div`
          `display:flex gap:11px padding:10px 0 border-bottom:1px solid #F3F5FA`
        - `div`
          `display:flex gap:11px padding:10px 0 border-bottom:1px solid #F3F5FA`
        - `div`
          `display:flex gap:11px padding:10px 0 border-bottom:1px solid #F3F5FA`
        - `div`
          `display:flex gap:11px padding:10px 0`
      - `div`
        `display:flex gap:20px align-items:flex-start`
        - `div`
          `width:362px display:flex flex-direction:column gap:8px`
        - `div`
          `flex:1 display:flex flex-direction:column gap:8px`
      - `p` — “달력을 끈 홈에서도 히어로의 는 그대로 오늘 하루 시트를 엽니다. 홈에는 이 목록을 따로 두지 않습니다.”
        `font-size:12px line-height:1.6 color:#626D88`
        - `b` — “소비 기록하기”
          `font-weight:600 color:#475467`
