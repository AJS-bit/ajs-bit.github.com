# LimitCardCases — 블록 개요

원본 `canvas/LimitCardCases.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div`
  `width:1200px height:960px background:#EDF0F7 color:#101828 padding:28px 30px 30px display:flex flex-direction:column gap:10px`
  - `span` **text 11px/600** — “구현 참고 · 앱 화면이 아닙니다”
    `font-size:11px font-weight:600 letter-spacing:0.02em color:#475467 border:1px solid #E3E8F1 background:#FFFFFF border-radius:99px padding:4px 10px`
  - `h2` **text 20px/700** — “이번 달 한도 카드 — 하루 금액 자리의 네 가지 경우”
    `font-size:20px font-weight:700 letter-spacing:-0.025em color:#101828`
  - `p` **text 13px/400** — “3단계에서 홈 한도 카드의 하루 47,270원이 앞으로 하루 47,270원으로 바뀝니다. 한도가 없을 때 · 0원일”
    `font-size:13px line-height:1.55 color:#626D88`
  - `div`
    `display:flex gap:32px align-items:flex-start`
    - `div`
      `width:362px display:flex flex-direction:column gap:8px`
      - `div`
        - `div` **text 14px/700** — “평소 — 한도가 남아 있을 때”
          `font-size:14px font-weight:700 letter-spacing:-0.01em color:#101828`
        - `div` **text 12px/400** — “남은 한도 ÷ 남은 일수. 홈의 하루 숫자는 이것 하나입니다.”
          `font-size:12px line-height:1.5 color:#626D88 margin-top:3px`
      - `div` **Card(18)**
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px`
        - `div`
          `display:flex align-items:center justify-content:space-between gap:8px`
        - `div`
          `position:relative height:8px border-radius:99px background:#E8ECF5 margin-top:9px`
      - `p` — “오른쪽 네 경우는 모두 가 바뀌는 것입니다. 글이 길어 한 줄에 안 들어가면 줄이지 않고 둘째 줄로 내립니다.”
        `font-size:12px line-height:1.5 color:#626D88`
        - `b` — “제목 옆 회색 글 자리”
          `font-weight:600 color:#475467`
      - `div`
        `margin-top:14px display:flex flex-direction:column gap:8px`
        - `div`
        - `div`
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:14px padding:11px 14px display:flex align-items:center justify-content:space-between gap:8px`
    - `div`
      `flex:1 display:grid grid-template-columns:repeat(2, 362px) gap:24px 20px align-items:start`
      - `div`
        `display:flex flex-direction:column gap:8px`
        - `div`
        - `div` **Card(18)**
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px`
      - `div`
        `display:flex flex-direction:column gap:8px`
        - `div`
        - `div` **Card(18)**
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px`
      - `div`
        `display:flex flex-direction:column gap:8px`
        - `div`
        - `div` **Card(18)**
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px`
      - `div`
        `display:flex flex-direction:column gap:8px`
        - `div`
        - `div` **Card(18)**
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px`
      - `div`
        `display:flex flex-direction:column gap:8px`
        - `div`
        - `div`
          `display:flex gap:11px padding:13px border-radius:14px background:#FFFFFF border:1px solid #E3E8F1 border-left:3px solid #B45309`
      - `div`
        `display:flex flex-direction:column gap:8px`
        - `div`
        - `div`
          `display:flex gap:11px padding:13px border-radius:14px background:#FFFFFF border:1px solid #E3E8F1 border-left:3px solid #B45309`
  - `div` **Card(18)**
    `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:10px 18px 8px`
    - `div` **text 12px/700** — “구현 메모”
      `font-size:12px font-weight:700 color:#101828 padding:2px 0 4px`
    - `div`
      `display:flex gap:10px padding:7px 0 border-bottom:1px solid #F3F5FA`
      - `span` **text 10.5px/700** — “1”
        `margin-top:1px width:17px height:17px border-radius:99px background:#101828 color:#FFFFFF font-size:10.5px font-weight:700 display:inline-flex align-items:center justify-content:center box-shadow:0 0 0 2px #FFFFFF`
      - `div` — “‘ ’ — 한도 미입력. 0원과 합치지 않습니다.”
        `font-size:12px line-height:1.55 color:#475467`
        - `b` — “앞으로 하루 — · 한도를 아직 안 정했어요”
          `font-weight:600 color:#101828`
    - `div`
      `display:flex gap:10px padding:7px 0 border-bottom:1px solid #F3F5FA`
      - `span` **text 10.5px/700** — “2”
        `margin-top:1px width:17px height:17px border-radius:99px background:#101828 color:#FFFFFF font-size:10.5px font-weight:700 display:inline-flex align-items:center justify-content:center box-shadow:0 0 0 2px #FFFFFF`
      - `div` — “‘ ’ — 남은 일수가 있고 남은 한도가 실제 0원일 때만.”
        `font-size:12px line-height:1.55 color:#475467`
        - `b` — “앞으로 하루 0원”
          `font-weight:600 color:#101828`
    - `div`
      `display:flex gap:10px padding:7px 0 border-bottom:1px solid #F3F5FA`
      - `span` **text 10.5px/700** — “3”
        `margin-top:1px width:17px height:17px border-radius:99px background:#101828 color:#FFFFFF font-size:10.5px font-weight:700 display:inline-flex align-items:center justify-content:center box-shadow:0 0 0 2px #FFFFFF`
      - `div` — “‘ ’ — 초과. 넘은 금액을 같은 줄에 적습니다.”
        `font-size:12px line-height:1.55 color:#475467`
        - `b` — “앞으로 하루 0원 · 한도보다 32,000원 많아요”
          `font-weight:600 color:#101828`
    - `div`
      `display:flex gap:10px padding:7px 0 border-bottom:1px solid #F3F5FA`
      - `span` **text 10.5px/700** — “4”
        `margin-top:1px width:17px height:17px border-radius:99px background:#101828 color:#FFFFFF font-size:10.5px font-weight:700 display:inline-flex align-items:center justify-content:center box-shadow:0 0 0 2px #FFFFFF`
      - `div` — “‘ ’ — 남은 일수 0. 지금 계산은 이날 하루 금액을 0으로 돌려주므로 한도가 남아도 0원이 됩니다. 분모는 그”
        `font-size:12px line-height:1.55 color:#475467`
        - `b` — “이번 달 남은 한도 90,000원”
          `font-weight:600 color:#101828`
    - `div`
      `display:flex gap:10px padding:7px 0 border-bottom:1px solid #F3F5FA`
      - `span` **text 10.5px/700** — “5”
        `margin-top:1px width:17px height:17px border-radius:99px background:#101828 color:#FFFFFF font-size:10.5px font-weight:700 display:inline-flex align-items:center justify-content:center box-shadow:0 0 0 2px #FFFFFF`
      - `div` — “‘ ’ — 소비 · 한도 맨 위 카드의 남은 일수 옆 하루 금액도 같은 라벨입니다.”
        `font-size:12px line-height:1.55 color:#475467`
        - `b` — “22일 남음 · 앞으로 하루 47,270원”
          `font-weight:600 color:#101828`
    - `div`
      `display:flex gap:10px padding:7px 0 border-bottom:1px solid #F3F5FA`
      - `span` **text 10.5px/700** — “6”
        `margin-top:1px width:17px height:17px border-radius:99px background:#101828 color:#FFFFFF font-size:10.5px font-weight:700 display:inline-flex align-items:center justify-content:center box-shadow:0 0 0 2px #FFFFFF`
      - `div` — “코치 본문의 ‘ ’은 ‘ ’으로 한도 카드와 같게 씁니다.”
        `font-size:12px line-height:1.55 color:#475467`
        - `b` — “하루 X씩”
          `font-weight:600 color:#101828`
        - `b` — “앞으로 하루 47,270원씩”
          `font-weight:600 color:#101828`
    - `div`
      `display:flex gap:10px padding:7px 0`
      - `span` **text 10.5px/700** — “7”
        `margin-top:1px width:17px height:17px border-radius:99px background:#101828 color:#FFFFFF font-size:10.5px font-weight:700 display:inline-flex align-items:center justify-content:center box-shadow:0 0 0 2px #FFFFFF`
      - `div` — “코치 — 남은 일수 0이면 본문도 ‘ ’으로, 한도 카드의 마지막 날과 같은 문구로 씁니다.”
        `font-size:12px line-height:1.55 color:#475467`
        - `b` — “이번 달 남은 한도 90,000원”
          `font-weight:600 color:#101828`
