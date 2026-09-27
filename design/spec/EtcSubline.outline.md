# EtcSubline — 블록 개요

원본 `canvas/EtcSubline.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div`
  `width:1200px height:1715px background:#EDF0F7 color:#101828 padding:28px 30px 30px display:flex flex-direction:column gap:10px`
  - `span` **text 11px/600** — “구현 참고 · 앱 화면이 아닙니다”
    `font-size:11px font-weight:600 letter-spacing:0.02em color:#475467 border:1px solid #E3E8F1 background:#FFFFFF border-radius:99px padding:4px 10px`
  - `h2` **text 20px/700** — “카테고리 없는 소비와 안 쓴 날 — 소비 · 한도 · 코치에서”
    `font-size:20px font-weight:700 letter-spacing:-0.025em color:#101828`
  - `p` **text 13px/400** — “하루 시트에서 카테고리 없이 저장한 소비는 기타로 들어가요. 소비 · 한도 화면은 기타 아래에 그 몫을 따로 적고,”
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
        - `div`
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:22px 22px 18px 18px padding:14px 14px 12px display:flex flex-direction:column gap:10px`
  - `div` **Card(18)**
    `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:10px 18px 8px`
    - `div` **text 12px/700** — “구현 메모”
      `font-size:12px font-weight:700 color:#101828 padding:2px 0 4px`
    - `div`
      `display:flex gap:10px padding:7px 0 border-bottom:1px solid #F3F5FA`
      - `span` **text 10.5px/700** — “1”
        `margin-top:1px width:17px height:17px border-radius:99px background:#101828 color:#FFFFFF font-size:10.5px font-weight:700 display:inline-flex align-items:center justify-content:center box-shadow:0 0 0 2px #FFFFFF`
      - `div` — “소비 · 이번 달의 카테고리별 소비 — 기타가 쓴 돈 위 다섯에 들 때만 그 이름 · 금액 줄 아래 ‘ ’(링크 없”
        `font-size:12px line-height:1.55 color:#475467`
        - `b` — “카테고리 없음 N건 N원”
          `font-weight:600 color:#101828`
        - `b` — “한도의 N%”
          `font-weight:600 color:#101828`
        - `span` — “그대로(카테고리”
          `white-space:nowrap`
        - `b` — “한도의 141%”
          `font-weight:600 color:#101828`
        - `span` — “보입니다(‘”
          `white-space:nowrap`
        - `b` — “카테고리 없음 7건 32,000원”
          `font-weight:600 color:#101828`
    - `div`
      `display:flex gap:10px padding:7px 0 border-bottom:1px solid #F3F5FA`
      - `span` **text 10.5px/700** — “2”
        `margin-top:1px width:17px height:17px border-radius:99px background:#101828 color:#FFFFFF font-size:10.5px font-weight:700 display:inline-flex align-items:center justify-content:center box-shadow:0 0 0 2px #FFFFFF`
      - `div` — “‘ ’ 경고와 코치의 가장 큰 카테고리 비중은 카테고리 없는 금액을 빼고 다시 판단합니다. 화면에 따로 문장을 두지”
        `font-size:12px line-height:1.55 color:#475467`
        - `b` — “기타 한도”
          `font-weight:600 color:#101828`
        - `span` — “않습니다(카테고리를”
          `white-space:nowrap`
    - `div`
      `display:flex gap:10px padding:7px 0 border-bottom:1px solid #F3F5FA`
      - `span` **text 10.5px/700** — “3”
        `margin-top:1px width:17px height:17px border-radius:99px background:#101828 color:#FFFFFF font-size:10.5px font-weight:700 display:inline-flex align-items:center justify-content:center box-shadow:0 0 0 2px #FFFFFF`
      - `div` — “소비 · 한도의 카테고리 배분에도 같은 부줄 — 이름 안 아래 11px 두 왼쪽 · 줄 높이가 그만큼 늘어요). 머”
        `font-size:12px line-height:1.55 color:#475467`
        - `span` — “칸(68)”
          `white-space:nowrap`
        - `span` — “「기타」”
          `white-space:nowrap`
        - `span` — “줄(막대”
          `white-space:nowrap`
        - `b` — “13개 · 직접 1개”
          `font-weight:600 color:#101828`
    - `div`
      `display:flex gap:10px padding:7px 0 border-bottom:1px solid #F3F5FA`
      - `span` **text 10.5px/700** — “4”
        `margin-top:1px width:17px height:17px border-radius:99px background:#101828 color:#FFFFFF font-size:10.5px font-weight:700 display:inline-flex align-items:center justify-content:center box-shadow:0 0 0 2px #FFFFFF`
      - `div` — “직접 정한 고정비 한도는 고정비 예상에 반영하지 §12-15)는 규칙은 그대로이지만 화면 문장은 두지 않습니다.”
        `font-size:12px line-height:1.55 color:#475467`
        - `span` — “않는다(계획”
          `white-space:nowrap`
    - `div`
      `display:flex gap:10px padding:7px 0 border-bottom:1px solid #F3F5FA`
      - `span` **text 10.5px/700** — “5”
        `margin-top:1px width:17px height:17px border-radius:99px background:#101828 color:#FFFFFF font-size:10.5px font-weight:700 display:inline-flex align-items:center justify-content:center box-shadow:0 0 0 2px #FFFFFF`
      - `div` — “코치 — 이번 달 기록이 0건이면 판정하지 않고 ‘ ’. 안 썼어요로 표시한 날은 기록 건수에 들지 ‘ ’은 쓰지 ”
        `font-size:12px line-height:1.55 color:#475467`
        - `b` — “이번 달 기록이 아직 없어요 · 달력에서 날짜를 눌러 쓴 돈을 적어 보세요 · 오늘 쓴 돈 적기 ›”
          `font-weight:600 color:#101828`
        - `span` — “않습니다(예전”
          `white-space:nowrap`
        - `b` — “소비 없음 확인 n일”
          `font-weight:600 color:#101828`
        - `b` — “안 썼어요”
          `font-weight:600 color:#101828`
    - `div`
      `display:flex gap:10px padding:7px 0`
      - `span` **text 10.5px/700** — “6”
        `margin-top:1px width:17px height:17px border-radius:99px background:#101828 color:#FFFFFF font-size:10.5px font-weight:700 display:inline-flex align-items:center justify-content:center box-shadow:0 0 0 2px #FFFFFF`
      - `div` — “코칭 · 월급만 넣은 첫날도 같은 카드 하나 + 카테고리 절감 ’). 월급도 없으면 코칭 · 기록 ‘ ’입니다.”
        `font-size:12px line-height:1.55 color:#475467`
        - `span` — “가정(‘”
          `white-space:nowrap`
        - `b` — “이번 달 변동비 기록이 있으면 줄였을 때의 효과를 비교해요.”
          `font-weight:600 color:#101828`
        - `span` — “없음(CoachEmpty)의”
          `white-space:nowrap`
        - `b` — “이렇게 시작해 보세요”
          `font-weight:600 color:#101828`
