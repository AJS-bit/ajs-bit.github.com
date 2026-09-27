# LimitCardCases — 블록 개요

원본 `canvas/LimitCardCases.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div`
  `width:1200px height:1462px background:#EDF0F7 color:#101828 padding:28px 30px 30px display:flex flex-direction:column gap:10px`
  - `span` **text 11px/600** — “구현 참고 · 앱 화면이 아닙니다”
    `font-size:11px font-weight:600 letter-spacing:0.02em color:#475467 border:1px solid #E3E8F1 background:#FFFFFF border-radius:99px padding:4px 10px`
  - `h2` **text 20px/700** — “이번 달 한도 카드 — 하루 금액 자리의 경우들”
    `font-size:20px font-weight:700 letter-spacing:-0.025em color:#101828`
  - `p` **text 13px/400** — “홈 한도 카드의 하루 금액은 늘 오늘 포함 남은 날로 나눈 값입니다. 한도가 없을 때 · 0원일 때 · 넘었을 때 ”
    `font-size:13px line-height:1.55 color:#626D88`
  - `div`
    `display:flex gap:32px align-items:flex-start`
    - `div`
      `width:362px display:flex flex-direction:column gap:8px`
      - `div`
        - `div` **text 14px/700** — “평소 — 한도가 남아 있을 때”
          `font-size:14px font-weight:700 letter-spacing:-0.01em color:#101828`
        - `div` — “남은 한도 ÷ 오늘 포함 남은 · 10원 단위. 홈의 하루 숫자는 이것 하나입니다.”
          `font-size:12px line-height:1.5 color:#626D88 margin-top:3px`
      - `div` **Card(18)**
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px`
        - `div`
          `display:flex flex-wrap:wrap align-items:center justify-content:space-between gap:4px 8px`
        - `div` **text 13px/400** — “216만원 중 112만원 썼어요”
          `font-size:13px line-height:1.45 color:#475467 margin-top:4px`
        - `div`
          `position:relative height:8px border-radius:99px background:#E8ECF5 margin-top:9px`
      - `p` — “오른쪽 경우들은 이 바뀌는 것입니다. 넘었을 때는 하루 금액 대신 넘은 금액을 빨갛게, 하루 0원이라고 쓰지 않습니”
        `font-size:12px line-height:1.5 color:#626D88`
        - `b` — “제목 옆 회색 글 · 오른쪽 값 · 둘째 줄”
          `font-weight:600 color:#475467`
      - `div`
        `margin-top:14px display:flex flex-direction:column gap:8px`
        - `div`
        - `div` **HeroCard**
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
      - `div`
        `margin-top:14px display:flex flex-direction:column gap:8px`
        - `div`
        - `div` **HeroCard**
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
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
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:6px 14px`
      - `div`
        `display:flex flex-direction:column gap:8px`
        - `div`
        - `div`
          `display:flex gap:11px padding:13px border-radius:14px background:#FFFFFF border:1px solid #E3E8F1 border-left:3px solid #0F7B47`
      - `div`
        `display:flex flex-direction:column gap:8px`
        - `div`
        - `div`
          `display:flex gap:11px padding:13px border-radius:14px background:#FFFFFF border:1px solid #E3E8F1 border-left:3px solid #B45309`
      - `div`
        `display:flex flex-direction:column gap:8px`
        - `div`
        - `div`
          `display:flex gap:11px padding:13px border-radius:14px background:#FFFFFF border:1px solid #E3E8F1 border-left:3px solid #0F7B47`
  - `div` **Card(18)**
    `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:10px 18px 8px`
    - `div` **text 12px/700** — “구현 메모”
      `font-size:12px font-weight:700 color:#101828 padding:2px 0 4px`
    - `div`
      `display:flex gap:10px padding:7px 0 border-bottom:1px solid #F3F5FA`
      - `span` **text 10.5px/700** — “1”
        `margin-top:1px width:17px height:17px border-radius:99px background:#101828 color:#FFFFFF font-size:10.5px font-weight:700 display:inline-flex align-items:center justify-content:center box-shadow:0 0 0 2px #FFFFFF`
      - `div` — “‘ ’ · 오른쪽 ‘ ’ · ‘ ’ — 판정 선이 없을 직접 한도도 없음). 0원과 합치지 않습니다.”
        `font-size:12px line-height:1.55 color:#475467`
        - `b` — “오늘 포함 하루 —”
          `font-weight:600 color:#101828`
        - `b` — “—”
          `font-weight:600 color:#101828`
        - `b` — “한도를 아직 안 정했어요”
          `font-weight:600 color:#101828`
        - `span` — “때(월급도”
          `white-space:nowrap`
    - `div`
      `display:flex gap:10px padding:7px 0 border-bottom:1px solid #F3F5FA`
      - `span` **text 10.5px/700** — “2”
        `margin-top:1px width:17px height:17px border-radius:99px background:#101828 color:#FFFFFF font-size:10.5px font-weight:700 display:inline-flex align-items:center justify-content:center box-shadow:0 0 0 2px #FFFFFF`
      - `div` — “‘ ’ — 남은 한도가 실제로 0원일 때만.”
        `font-size:12px line-height:1.55 color:#475467`
        - `b` — “오늘 포함 하루 0원”
          `font-weight:600 color:#101828`
    - `div`
      `display:flex gap:10px padding:7px 0 border-bottom:1px solid #F3F5FA`
      - `span` **text 10.5px/700** — “3”
        `margin-top:1px width:17px height:17px border-radius:99px background:#101828 color:#FFFFFF font-size:10.5px font-weight:700 display:inline-flex align-items:center justify-content:center box-shadow:0 0 0 2px #FFFFFF`
      - `div` — “넘음 — 오른쪽 ‘ ’(빨강) · 둘째 줄 ‘ ’ · 빨간 막대. ‘ ’이라고 쓰지 않습니다. 카드 · 줄은 ‘ ’”
        `font-size:12px line-height:1.55 color:#475467`
        - `b` — “3만원 넘음”
          `font-weight:600 color:#101828`
        - `b` — “이번 달 한도는 이미 넘었어요 · 216만원 중 219만원 썼어요”
          `font-weight:600 color:#101828`
        - `b` — “하루 0원”
          `font-weight:600 color:#101828`
        - `b` — “N 넘음”
          `font-weight:600 color:#101828`
        - `b` — “한도를 N 넘었어요”
          `font-weight:600 color:#101828`
    - `div`
      `display:flex gap:10px padding:7px 0 border-bottom:1px solid #F3F5FA`
      - `span` **text 10.5px/700** — “4”
        `margin-top:1px width:17px height:17px border-radius:99px background:#101828 color:#FFFFFF font-size:10.5px font-weight:700 display:inline-flex align-items:center justify-content:center box-shadow:0 0 0 2px #FFFFFF`
      - `div` — “‘ ’ — 남은 날이 오늘 하루뿐이면 하루 금액 대신 ‘ ’.”
        `font-size:12px line-height:1.55 color:#475467`
        - `b` — “이번 달 마지막 날”
          `font-weight:600 color:#101828`
        - `b` — “이번 달 남은 한도 9만원”
          `font-weight:600 color:#101828`
    - `div`
      `display:flex gap:10px padding:7px 0 border-bottom:1px solid #F3F5FA`
      - `span` **text 10.5px/700** — “5”
        `margin-top:1px width:17px height:17px border-radius:99px background:#101828 color:#FFFFFF font-size:10.5px font-weight:700 display:inline-flex align-items:center justify-content:center box-shadow:0 0 0 2px #FFFFFF`
      - `div` — “소비 · 한도 맨 위 카드도 같은 규칙 — ‘ ’ / ‘ ’ / ‘ ’. 참고 줄 ‘ ’은 회색 12px(판정 아님”
        `font-size:12px line-height:1.55 color:#475467`
        - `b` — “오늘 포함 23일 남음 · 하루 45,220원”
          `font-weight:600 color:#101828`
        - `b` — “남은 한도 없음”
          `font-weight:600 color:#101828`
        - `b` — “이번 달 마지막 날 · 남은 한도 9만원”
          `font-weight:600 color:#101828`
        - `b` — “저축 · 상환 계획까지 지키려면 152만원 …”
          `font-weight:600 color:#101828`
        - `b` — “이번 달 한도를 3만원 넘었어요 · 한도 216만원 중 219만원 썼어요. · 이번 달 한도 ›”
          `font-weight:600 color:#101828`
        - `b` — “직접 ›”
          `font-weight:600 color:#101828`
    - `div`
      `display:flex gap:10px padding:7px 0 border-bottom:1px solid #F3F5FA`
      - `span` **text 10.5px/700** — “6”
        `margin-top:1px width:17px height:17px border-radius:99px background:#101828 color:#FFFFFF font-size:10.5px font-weight:700 display:inline-flex align-items:center justify-content:center box-shadow:0 0 0 2px #FFFFFF`
      - `div` — “코치 본문의 하루 금액도 ‘ ’으로 한도 카드와 같게 씁니다. 넘었으면 ‘ ’ + ‘ ’ — 코치 목록에서는 ‘ ’”
        `font-size:12px line-height:1.55 color:#475467`
        - `b` — “오늘 포함 하루 45,220원씩”
          `font-weight:600 color:#101828`
        - `b` — “이번 달 한도를 3만원 넘었어요”
          `font-weight:600 color:#101828`
        - `b` — “이번 달 한도 ›”
          `font-weight:600 color:#101828`
        - `span` — “그날(219만원)”
          `white-space:nowrap`
        - `b` — “이대로면 이번 달 18만원 적자예요”
          `font-weight:600 color:#101828`
        - `b` — “월말엔 소비 목표 넘어요”
          `font-weight:600 color:#101828`
    - `div`
      `display:flex gap:10px padding:7px 0 border-bottom:1px solid #F3F5FA`
      - `span` **text 10.5px/700** — “7”
        `margin-top:1px width:17px height:17px border-radius:99px background:#101828 color:#FFFFFF font-size:10.5px font-weight:700 display:inline-flex align-items:center justify-content:center box-shadow:0 0 0 2px #FFFFFF`
      - `div` — “코치 — 마지막 날이면 본문이 ‘ ’(9월 30일 · 207만원 · 목록 일곱째).”
        `font-size:12px line-height:1.55 color:#475467`
        - `b` — “오늘이 이번 달 마지막 날이에요. 이번 달 남은 한도 9만원”
          `font-weight:600 color:#101828`
    - `div`
      `display:flex gap:10px padding:7px 0`
      - `span` **text 10.5px/700** — “8”
        `margin-top:1px width:17px height:17px border-radius:99px background:#101828 color:#FFFFFF font-size:10.5px font-weight:700 display:inline-flex align-items:center justify-content:center box-shadow:0 0 0 2px #FFFFFF`
      - `div` — “남은 날은 오늘을 포함해 날 = 1일 · max(1, 30 − 8 + 1) = 23). 첫 기록 전은 ‘ ’ + ‘”
        `font-size:12px line-height:1.55 color:#475467`
        - `span` — “셉니다(마지막”
          `white-space:nowrap`
        - `b` — “총 216만원”
          `font-weight:600 color:#101828`
        - `b` — “소비를 기록하면 남은 한도가 보여요”
          `font-weight:600 color:#101828`
        - `b` — “9월 5일부터 기록 · 그 전 소비는 빠져 있어요”
          `font-weight:600 color:#101828`
