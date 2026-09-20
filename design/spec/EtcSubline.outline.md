# EtcSubline — 블록 개요

원본 `canvas/EtcSubline.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div`
  `width:1200px height:970px background:#EDF0F7 color:#101828 padding:28px 30px 30px display:flex flex-direction:column gap:10px`
  - `span` **text 11px/600** — “구현 참고 · 앱 화면이 아닙니다”
    `font-size:11px font-weight:600 letter-spacing:0.02em color:#475467 border:1px solid #E3E8F1 background:#FFFFFF border-radius:99px padding:4px 10px`
  - `h2` **text 20px/700** — “분류 안 한 소비와 안 쓴 날 — 소비 · 한도 · 코치에서”
    `font-size:20px font-weight:700 letter-spacing:-0.025em color:#101828`
  - `p` **text 13px/400** — “하루 시트에서 분류 없이 저장한 소비는 기타로 들어갑니다. 소비 · 한도 화면은 기타 아래에 그 몫을 따로 적고, ”
    `font-size:13px line-height:1.55 color:#626D88`
  - `div`
    `display:flex gap:24px align-items:flex-start`
    - `div`
      `width:362px display:flex flex-direction:column gap:22px`
      - `div`
        `display:flex flex-direction:column gap:8px`
        - `div`
        - `div` **Card(18)**
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
    - `div`
      `width:362px display:flex flex-direction:column gap:22px`
      - `div`
        `display:flex flex-direction:column gap:8px`
        - `div`
        - `div` **Card(18)**
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
    - `div`
      `width:362px display:flex flex-direction:column gap:22px`
      - `div`
        `display:flex flex-direction:column gap:8px`
        - `div`
        - `div`
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:22px 22px 18px 18px padding:14px 14px 12px display:flex flex-direction:column gap:10px`
      - `div`
        `display:flex flex-direction:column gap:8px`
        - `div`
        - `div` **Card(18)**
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px 15px`
  - `div` **Card(18)**
    `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:10px 18px 8px`
    - `div` **text 12px/700** — “구현 메모”
      `font-size:12px font-weight:700 color:#101828 padding:2px 0 4px`
    - `div`
      `display:flex gap:10px padding:7px 0 border-bottom:1px solid #F3F5FA`
      - `span` **text 10.5px/700** — “1”
        `margin-top:1px width:17px height:17px border-radius:99px background:#101828 color:#FFFFFF font-size:10.5px font-weight:700 display:inline-flex align-items:center justify-content:center box-shadow:0 0 0 2px #FFFFFF`
      - `div` — “소비 · 이번 달의 카테고리별 소비 — ‘ ’ 줄 아래 ‘ ’. 금액 · 막대 · 120%는 엔진 값 그대로(분류 ”
        `font-size:12px line-height:1.55 color:#475467`
        - `b` — “기타”
          `font-weight:600 color:#101828`
        - `b` — “분류 안 함 7건 32,000원”
          `font-weight:600 color:#101828`
    - `div`
      `display:flex gap:10px padding:7px 0 border-bottom:1px solid #F3F5FA`
      - `span` **text 10.5px/700** — “2”
        `margin-top:1px width:17px height:17px border-radius:99px background:#101828 color:#FFFFFF font-size:10.5px font-weight:700 display:inline-flex align-items:center justify-content:center box-shadow:0 0 0 2px #FFFFFF`
      - `div` — “‘ ’ 경고와 코치의 최대 카테고리 비중은 분류 안 한 금액을 뺀 28,000원(56%)으로 다시 판단합니다. 그래”
        `font-size:12px line-height:1.55 color:#475467`
        - `b` — “기타 한도”
          `font-weight:600 color:#101828`
    - `div`
      `display:flex gap:10px padding:7px 0 border-bottom:1px solid #F3F5FA`
      - `span` **text 10.5px/700** — “3”
        `margin-top:1px width:17px height:17px border-radius:99px background:#101828 color:#FFFFFF font-size:10.5px font-weight:700 display:inline-flex align-items:center justify-content:center box-shadow:0 0 0 2px #FFFFFF`
      - `div` **text 12px/400** — “소비 · 한도의 카테고리 배분에도 같은 서브라인. 줄 높이 44는 그대로 두고 그 아래 한 줄을 더합니다.”
        `font-size:12px line-height:1.55 color:#475467`
    - `div`
      `display:flex gap:10px padding:7px 0 border-bottom:1px solid #F3F5FA`
      - `span` **text 10.5px/700** — “4”
        `margin-top:1px width:17px height:17px border-radius:99px background:#101828 color:#FFFFFF font-size:10.5px font-weight:700 display:inline-flex align-items:center justify-content:center box-shadow:0 0 0 2px #FFFFFF`
      - `div` **text 12px/400** — “직접 정한 고정비 한도는 고정비 예상에 반영하지 않는다(계획 §12-15)는 사실을 배분 카드 맨 아래 문장으로 적”
        `font-size:12px line-height:1.55 color:#475467`
    - `div`
      `display:flex gap:10px padding:7px 0 border-bottom:1px solid #F3F5FA`
      - `span` **text 10.5px/700** — “5”
        `margin-top:1px width:17px height:17px border-radius:99px background:#101828 color:#FFFFFF font-size:10.5px font-weight:700 display:inline-flex align-items:center justify-content:center box-shadow:0 0 0 2px #FFFFFF`
      - `div` — “코치 ‘ ’ — 판정은 그대로 두고 본문에 ‘ ’을 함께 적어, 안 썼다고 표시한 날이 미입력처럼 보이지 않게 합니”
        `font-size:12px line-height:1.55 color:#475467`
        - `b` — “소비 기록이 필요합니다”
          `font-weight:600 color:#101828`
        - `b` — “소비 없음 확인 n일”
          `font-weight:600 color:#101828`
    - `div`
      `display:flex gap:10px padding:7px 0`
      - `span` **text 10.5px/700** — “6”
        `margin-top:1px width:17px height:17px border-radius:99px background:#101828 color:#FFFFFF font-size:10.5px font-weight:700 display:inline-flex align-items:center justify-content:center box-shadow:0 0 0 2px #FFFFFF`
      - `div` — “코칭 · 기록 없음(CoachEmpty)의 소비 기록 줄에도 같은 말을 붙입니다. ‘ ’은 그대로 — 안 쓴 날은 ”
        `font-size:12px line-height:1.55 color:#475467`
        - `b` — “0 / 3건”
          `font-weight:600 color:#101828`
