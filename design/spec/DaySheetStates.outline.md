# DaySheetStates — 블록 개요

원본 `canvas/DaySheetStates.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div`
  `width:1210px height:1660px background:#EDF0F7 color:#101828 padding:28px 30px 30px display:flex flex-direction:column gap:10px`
  - `span` **text 11px/600** — “구현 참고 · 앱 화면이 아닙니다”
    `font-size:11px font-weight:600 letter-spacing:0.02em color:#475467 border:1px solid #E3E8F1 background:#FFFFFF border-radius:99px padding:4px 10px`
  - `h2` **text 20px/700** — “기록 창의 글이 바뀌는 경우”
    `font-size:20px font-weight:700 letter-spacing:-0.025em color:#101828`
  - `p` **text 13px/400** — “기록 창은 하나이고, 날짜 · 시간 · 입력한 값에 따라 아래 다섯 자리의 글과 모양만 바뀝니다.”
    `font-size:13px line-height:1.55 color:#626D88`
  - `div`
    `display:flex gap:32px align-items:flex-start`
    - `div`
      `width:362px display:flex flex-direction:column gap:22px`
      - `div`
        `display:flex flex-direction:column gap:8px`
        - `div`
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:26px 26px 18px 18px display:flex flex-direction:column`
        - `p` — “번호는 글이 바뀌는 자리입니다. 그림은 의 기록 창입니다.”
          `font-size:12px line-height:1.5 color:#626D88`
      - `div`
        `display:flex flex-direction:column gap:8px`
        - `div`
        - `div`
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:26px 26px 18px 18px display:flex flex-direction:column`
    - `div`
      `width:362px display:flex flex-direction:column gap:22px`
      - `div`
        `display:flex flex-direction:column gap:8px`
        - `div`
        - `div` **BottomSheet**
          `background:#FFFFFF border:1px solid #E3E8F1 border-bottom:none border-radius:26px 26px 0 0 display:flex flex-direction:column`
      - `div`
        `display:flex flex-direction:column gap:8px`
        - `div`
        - `div` **BottomSheet**
          `background:#FFFFFF border:1px solid #E3E8F1 border-bottom:none border-radius:26px 26px 0 0 display:flex flex-direction:column`
      - `div`
        `display:flex flex-direction:column gap:8px`
        - `div`
        - `div` **BottomSheet**
          `background:#FFFFFF border:1px solid #E3E8F1 border-bottom:none border-radius:26px 26px 0 0 display:flex flex-direction:column`
      - `div`
        `display:flex flex-direction:column gap:8px`
        - `div`
        - `div` **BottomSheet**
          `background:#FFFFFF border:1px solid #E3E8F1 border-bottom:none border-radius:26px 26px 0 0 display:flex flex-direction:column`
      - `div`
        `display:flex flex-direction:column gap:8px`
        - `div`
        - `div` **Card(18)**
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px display:flex flex-direction:column gap:10px`
      - `div`
        `display:flex flex-direction:column gap:8px`
        - `div`
        - `div` **Card(18)**
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px display:flex flex-direction:column gap:10px`
    - `div`
      `width:362px display:flex flex-direction:column gap:22px`
      - `div`
        `display:flex flex-direction:column gap:8px`
        - `div`
        - `div` **Card(18)**
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px display:flex flex-direction:column gap:10px`
      - `div`
        `display:flex flex-direction:column gap:8px`
        - `div`
        - `div` **Card(18)**
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px display:flex flex-direction:column gap:10px`
      - `div`
        `display:flex flex-direction:column gap:8px`
        - `div`
        - `div`
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:26px 26px 18px 18px display:flex flex-direction:column`
  - `div` **Card(18)**
    `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:10px 18px 8px`
    - `div` **text 12px/700** — “구현 메모”
      `font-size:12px font-weight:700 color:#101828 padding:2px 0 4px`
    - `div`
      `display:flex gap:10px padding:7px 0 border-bottom:1px solid #F3F5FA`
      - `span` **text 10.5px/700** — “1”
        `margin-top:1px width:17px height:17px border-radius:99px background:#101828 color:#FFFFFF font-size:10.5px font-weight:700 display:inline-flex align-items:center justify-content:center box-shadow:0 0 0 2px #FFFFFF`
      - `div` **text 12px/400** — “날짜 선택기는 이번 달과 지난달 전체를 주 단위로 보여 줍니다. 그보다 앞선 달은 소비 탭의 거래 추가에서 남깁니다”
        `font-size:12px line-height:1.55 color:#475467`
    - `div`
      `display:flex gap:10px padding:7px 0 border-bottom:1px solid #F3F5FA`
      - `span` **text 10.5px/700** — “2”
        `margin-top:1px width:17px height:17px border-radius:99px background:#101828 color:#FFFFFF font-size:10.5px font-weight:700 display:inline-flex align-items:center justify-content:center box-shadow:0 0 0 2px #FFFFFF`
      - `div` **text 12px/400** — “둘째 줄은 평소에 그날 합계(오늘 4건 37,000원)입니다. 위 네 경우에는 그 자리에 안내 문장이 옵니다. 마감”
        `font-size:12px line-height:1.55 color:#475467`
    - `div`
      `display:flex gap:10px padding:7px 0 border-bottom:1px solid #F3F5FA`
      - `span` **text 10.5px/700** — “3”
        `margin-top:1px width:17px height:17px border-radius:99px background:#101828 color:#FFFFFF font-size:10.5px font-weight:700 display:inline-flex align-items:center justify-content:center box-shadow:0 0 0 2px #FFFFFF`
      - `div` **text 12px/400** — “금액 아래 한 줄은 저장을 한 번 더 물어보는 경우 장의 네 안내와 같은 자리입니다.”
        `font-size:12px line-height:1.55 color:#475467`
    - `div`
      `display:flex gap:10px padding:7px 0 border-bottom:1px solid #F3F5FA`
      - `span` **text 10.5px/700** — “4”
        `margin-top:1px width:17px height:17px border-radius:99px background:#101828 color:#FFFFFF font-size:10.5px font-weight:700 display:inline-flex align-items:center justify-content:center box-shadow:0 0 0 2px #FFFFFF`
      - `div` **text 12px/400** — “예전에 60자를 넘겨 적은 메모는 그대로 열리고 저장도 됩니다. 글자를 더 넣는 것만 막습니다.”
        `font-size:12px line-height:1.55 color:#475467`
    - `div`
      `display:flex gap:10px padding:7px 0`
      - `span` **text 10.5px/700** — “5”
        `margin-top:1px width:17px height:17px border-radius:99px background:#101828 color:#FFFFFF font-size:10.5px font-weight:700 display:inline-flex align-items:center justify-content:center box-shadow:0 0 0 2px #FFFFFF`
      - `div` **text 12px/400** — “순서는 식비 · 카페/간식 · 교통 · 쇼핑 · 문화/여가 · 의료/건강 · 교육 · 경조사 · 기타, 선 아래 주”
        `font-size:12px line-height:1.55 color:#475467`
