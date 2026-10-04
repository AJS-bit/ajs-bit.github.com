# InsufficientElsewhere — 블록 개요

원본 `canvas/InsufficientElsewhere.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div`
  `width:1230px height:1864px background:#EDF0F7 color:#101828 padding:28px 30px 30px display:flex flex-direction:column gap:10px`
  - `span` **text 11px/600** — “구현 참고 · 앱 화면이 아닙니다”
    `font-size:11px font-weight:600 letter-spacing:0.02em color:#475467 border:1px solid #E3E8F1 background:#FFFFFF border-radius:99px padding:4px 10px`
  - `h2` **text 20px/700** — “월말 예상 기준이 서기 전 — 홈 밖의 화면들”
    `font-size:20px font-weight:700 letter-spacing:-0.025em color:#101828`
  - `p` — “홈의 이력 부족 같은 사람입니다 — 9월 5일에 처음 열었고 오늘 커피 5,000원 한 건을 적었습니다. 지난달을 ”
    `font-size:13px line-height:1.55 color:#626D88`
    - `span` — “상태(HeroInsufficient)와”
      `white-space:nowrap`
  - `div`
    `display:flex gap:24px align-items:flex-start`
    - `div`
      `width:390px display:flex flex-direction:column gap:22px`
      - `div`
        `display:flex flex-direction:column gap:8px`
        - `div`
        - `div`
          `width:390px background:#EDF0F7 border:1px solid #E3E8F1 border-radius:24px`
      - `div`
        `display:flex flex-direction:column gap:8px`
        - `div`
        - `div`
          `display:flex flex-direction:column gap:8px`
    - `div`
      `width:362px display:flex flex-direction:column gap:22px`
      - `div`
        `display:flex flex-direction:column gap:8px`
        - `div`
        - `div` **HeroCard**
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
        - `div` **Card(18)**
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px 14px 12px`
      - `div`
        `display:flex flex-direction:column gap:8px`
        - `div`
        - `div`
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:22px 22px 18px 18px padding:14px 14px 12px display:flex flex-direction:column gap:10px`
    - `div`
      `width:362px display:flex flex-direction:column gap:22px`
      - `div`
        `display:flex flex-direction:column gap:8px`
        - `div`
        - `div` **Card(18)**
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
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
      - `div` — “소비 · 이번 달 — 큰 숫자는 지금까지 쓴 돈 ÷ 기준과 상관없이 그대로입니다. 월말 배지 ‘ ’ · ‘ ’ · ”
        `font-size:12px line-height:1.55 color:#475467`
        - `span` — “월급(0.1%)이라”
          `white-space:nowrap`
        - `b` — “월말에도 목표 안”
          `font-weight:600 color:#101828`
        - `b` — “월말엔 목표 초과”
          `font-weight:600 color:#101828`
        - `b` — “월말엔 월급 초과”
          `font-weight:600 color:#101828`
        - `span` — “‘ ’을”
          `white-space:nowrap`
        - `b` — “9월 기록이 아직 없어요”
          `font-weight:600 color:#101828`
        - `b` — “월말 예상 —”
          `font-weight:600 color:#101828`
    - `div`
      `display:flex gap:10px padding:7px 0 border-bottom:1px solid #F3F5FA`
      - `span` **text 10.5px/700** — “2”
        `margin-top:1px width:17px height:17px border-radius:99px background:#101828 color:#FFFFFF font-size:10.5px font-weight:700 display:inline-flex align-items:center justify-content:center box-shadow:0 0 0 2px #FFFFFF`
      - `div` — “그 자리에 사실 문구 ‘ ’가 옵니다. 마감하지 않은 지난달이 있을 때만 그 아래에 ‘ ’(한 달이면 ‘ ’)가 붙”
        `font-size:12px line-height:1.55 color:#475467`
        - `b` — “기록한 소비 N원 · 아직 기록하지 않은 소비는 포함하지 않았어요”
          `font-weight:600 color:#101828`
        - `b` — “월말 예상을 보려면 … 마감해 주세요 · …부터 마감하기 ›”
          `font-weight:600 color:#101828`
        - `b` — “8월을 마감하면 월말 예상을 볼 수 있어요 · 8월 마감하기 ›”
          `font-weight:600 color:#101828`
        - `span` — “문구뿐입니다(홈”
          `white-space:nowrap`
        - `b` — “9월을 마감하면 10월부터 월말 예상을 보여 드려요”
          `font-weight:600 color:#101828`
    - `div`
      `display:flex gap:10px padding:7px 0 border-bottom:1px solid #F3F5FA`
      - `span` **text 10.5px/700** — “3”
        `margin-top:1px width:17px height:17px border-radius:99px background:#101828 color:#FFFFFF font-size:10.5px font-weight:700 display:inline-flex align-items:center justify-content:center box-shadow:0 0 0 2px #FFFFFF`
      - `div` — “한도 탭 — 알약 ‘ ’ · 남은 일수는 오늘 포함 · 달 중간에 시작한 사람은 남은 한도를 초록 대신 기본 글자색”
        `font-size:12px line-height:1.55 color:#475467`
        - `b` — “자동 ›”
          `font-weight:600 color:#101828`
        - `b` — “9월 5일부터 기록 · 그 전 소비는 빠져 있어요”
          `font-weight:600 color:#101828`
        - `b` — “저축 · 상환 계획까지 지키려면 152만원 안에서 쓰면 돼요”
          `font-weight:600 color:#101828`
        - `b` — “초과 예상”
          `font-weight:600 color:#101828`
    - `div`
      `display:flex gap:10px padding:7px 0 border-bottom:1px solid #F3F5FA`
      - `span` **text 10.5px/700** — “4”
        `margin-top:1px width:17px height:17px border-radius:99px background:#101828 color:#FFFFFF font-size:10.5px font-weight:700 display:inline-flex align-items:center justify-content:center box-shadow:0 0 0 2px #FFFFFF`
      - `div` — “코치 — 예상에서 나오는 예상 · 매달 모을 수 있는 돈 · 모든 목적지가 제때 도착해요)가 없습니다. 카테고리 비”
        `font-size:12px line-height:1.55 color:#475467`
        - `span` — “안내(월말”
          `white-space:nowrap`
    - `div`
      `display:flex gap:10px padding:7px 0 border-bottom:1px solid #F3F5FA`
      - `span` **text 10.5px/700** — “5”
        `margin-top:1px width:17px height:17px border-radius:99px background:#101828 color:#FFFFFF font-size:10.5px font-weight:700 display:inline-flex align-items:center justify-content:center box-shadow:0 0 0 2px #FFFFFF`
      - `div` — “다음 안내 — 늘 있는 안내가 있으면 할부 금리 · 상환 계획 보기 ›), 없으면 빠진 날 안내 ‘ ’. 같은 카드”
        `font-size:12px line-height:1.55 color:#475467`
        - `span` — “그것(카드”
          `white-space:nowrap`
        - `b` — “어제 쓴 돈도 적어 볼까요? · 7일 적기 ›”
          `font-weight:600 color:#101828`
        - `span` — “홈(HeroInsufficient)과”
          `white-space:nowrap`
    - `div`
      `display:flex gap:10px padding:7px 0 border-bottom:1px solid #F3F5FA`
      - `span` **text 10.5px/700** — “6”
        `margin-top:1px width:17px height:17px border-radius:99px background:#101828 color:#FFFFFF font-size:10.5px font-weight:700 display:inline-flex align-items:center justify-content:center box-shadow:0 0 0 2px #FFFFFF`
      - `div` — “또래 카드 — 월말 예상으로 판단하는 ‘ ’ 줄 대신 ‘ ’. · 기준 등록 · 자세히 접힘)는 그대로입니다. 월급”
        `font-size:12px line-height:1.55 color:#475467`
        - `b` — “월말에도 소비 목표 60% 안이에요”
          `font-weight:600 color:#101828`
        - `b` — “이번 달 기록 · 기록한 소비 5,000원”
          `font-weight:600 color:#101828`
        - `span` — “나머지(나이대”
          `white-space:nowrap`
        - `b` — “이번 달 기록이 아직 없어요”
          `font-weight:600 color:#101828`
        - `b` — “소비 기록하기”
          `font-weight:600 color:#101828`
        - `span` — “하나입니다(월급”
          `white-space:nowrap`
    - `div`
      `display:flex gap:10px padding:7px 0`
      - `span` **text 10.5px/700** — “7”
        `margin-top:1px width:17px height:17px border-radius:99px background:#101828 color:#FFFFFF font-size:10.5px font-weight:700 display:inline-flex align-items:center justify-content:center box-shadow:0 0 0 2px #FFFFFF`
      - `div` — “알림 — 예상으로 만든 알림은 목록과 · 머리줄 종 배지)에서 모두 빠집니다. 목록은 중요 · 참고로 묶고, 종 배”
        `font-size:12px line-height:1.55 color:#475467`
        - `span` — “개수(제목”
          `white-space:nowrap`
        - `span` — “수(1)입니다”
          `white-space:nowrap`
    - `div` — “판정은 하나입니다 — 월말 예상 마감)이 서기 전이면 위 일곱 곳이 전부 이 모양이고, 서면 전부 원래 화면으로 돌”
      `font-size:12px line-height:1.55 color:#626D88 padding:8px 0 4px border-top:1px solid #F3F5FA`
      - `span` — “기준(지난달”
        `white-space:nowrap`
      - `b` — “월말에도 목표 안”
        `font-weight:600 color:#101828`
      - `span` — “선(소비”
        `white-space:nowrap`
      - `span` — “비율(홈”
        `white-space:nowrap`
      - `b` — “이번 달 기록이 아직 없어요”
        `font-weight:600 color:#101828`
      - `span` — “씁니다(판정”
        `white-space:nowrap`
