# GoalsStates — 블록 개요

원본 `canvas/GoalsStates.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div`
  `width:390px height:4432px background:#EDF0F7 color:#101828 padding:18px 14px 20px display:flex flex-direction:column gap:8px`
  - `div`
    `padding:0 2px 6px`
    - `span` **text 11px/600** — “구현 참고 · 앱 화면이 아닙니다”
      `display:inline-block font-size:11px font-weight:600 letter-spacing:0.02em color:#475467 border:1px solid #E3E8F1 background:#FFFFFF border-radius:99px padding:4px 10px white-space:nowrap`
    - `h2` **text 18px/700** — “목적지 · 상태 7종”
      `font-size:18px font-weight:700 letter-spacing:-0.025em color:#101828`
    - `p` — “내 목적지 화면에서 모양이 바뀌는 경우들입니다. 값은 앱에 넣어 나온 그대로입니다.”
      `font-size:12px line-height:1.45 color:#626D88`
      - `span` — “시안 사용자(9월 8일)를”
        `white-space:nowrap`
  - `div` **text 11px/600** — “A · 「매달 모으는 돈 바꿔 보기 ›」로 110만원을 넣어 본 가정”
    `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
  - `div` **Card(20)**
    `background:#FFFFFF border:1.5px dashed #B79BFF border-radius:20px padding:15px 16px`
    - `div`
      `display:flex align-items:center justify-content:space-between gap:8px`
      - `span` **text 11px/600** — “매달 모으는 돈”
        `font-size:11px font-weight:600 letter-spacing:0.07em color:#626D88`
      - `span` **text 12.5px/600** — “매달 모으는 돈 바꿔 보기 ›”
        `font-size:12.5px font-weight:600 color:#3556E6 white-space:nowrap`
    - `div`
      `margin-top:8px`
      - `span` **StatusPill** — “저장되지 않는 가정”
        `display:inline-flex align-items:center gap:4px background:#F1EAFD color:#6B32D6 font-size:11.5px font-weight:600 border-radius:99px padding:4px 9px`
    - `div`
      `display:flex align-items:flex-end justify-content:space-between gap:10px margin-top:7px`
      - `div`
        `display:flex align-items:baseline gap:2px`
        - `span` **text 30px/700** — “110”
          `font-size:30px font-weight:700 letter-spacing:-0.035em line-height:1.05 color:#101828`
        - `span` **text 16px/600** — “만원”
          `font-size:16px font-weight:600 color:#475467`
        - `span` **text 12.5px/500** — “가정”
          `font-size:12.5px font-weight:500 color:#626D88 white-space:nowrap`
      - `span` — “모두 도착하려면”
        `font-size:12.5px font-weight:500 color:#626D88 white-space:nowrap`
        - `span` — “146만원”
          `font-weight:600 color:#101828`
    - `div` **text 12px/400** — “저장되지 않는 가정 금액이에요”
      `font-size:12px color:#626D88 margin-top:5px`
    - `div` **ProgressTrack**
      `position:relative height:9px border-radius:99px background:#E8ECF5 margin-top:11px`
      - `div`
        `position:absolute inset:0 24.7% 0 0 border-radius:99px background:linear-gradient(90deg, #3556E6 0%, #7A3FE4 100%)`
    - `div` **Callout(warn)**
      `margin-top:11px padding:10px 11px 11px background:#FDF1E0 border-radius:12px`
      - `div`
        `display:flex gap:8px`
        - `span`
          `margin-top:2px`
        - `span` — “목적지에 매달 이 더 필요해요. 늦어지는 목적지: 투자 계좌 5,000만원. 목표일을 늦추거나 우선순위를 바꾸면 앱”
          `font-size:12.5px line-height:1.5 color:#7A3E0A`
      - `div`
        `display:flex gap:8px flex-wrap:wrap margin-top:9px`
        - `span` **text 11px/600** — “목표일 늦추기 ›”
          `display:inline-flex align-items:center height:30px padding:0 10px border-radius:99px border:1px solid #DE8A2A background:#FFFFFF color:#7A3E0A font-size:11px font-weight:600 white-space:nowrap`
        - `span` **text 11px/600** — “우선순위 바꾸기 ›”
          `display:inline-flex align-items:center height:30px padding:0 10px border-radius:99px border:1px solid #DE8A2A background:#FFFFFF color:#7A3E0A font-size:11px font-weight:600 white-space:nowrap`
  - `div` **Card(20)**
    `background:#FFFFFF border:1.5px dashed #B79BFF border-radius:20px padding:15px 16px`
    - `div`
      `display:flex align-items:center justify-content:space-between gap:8px`
      - `span` **text 15px/700** — “매달 모으는 돈을 바꾸면?”
        `font-size:15px font-weight:700 color:#101828`
      - `span` **text 18px/500** — “−”
        `font-size:18px font-weight:500 line-height:1 color:#3556E6`
    - `div`
      `margin-top:8px`
      - `span` **StatusPill** — “저장되지 않는 가정”
        `display:inline-flex align-items:center gap:4px background:#F1EAFD color:#6B32D6 font-size:11.5px font-weight:600 border-radius:99px padding:4px 9px`
    - `div` **text 13px/600** — “매달 모으는 돈을 바꿔 보세요”
      `font-size:13px font-weight:600 color:#101828 margin-top:10px`
    - `div` **text 12px/400** — “바꿔 본 금액으로 목적지 결과만 미리 보고 있어요. 실제 월급 · 소비나 저장된 계획은 바뀌지 않아요.”
      `font-size:12px line-height:1.5 color:#3556E6 margin-top:6px padding:9px 11px background:#E9EDFD border-radius:12px`
    - `div`
      `display:flex align-items:baseline gap:6px margin-top:10px`
      - `span` **text 24px/700** — “110만원”
        `font-size:24px font-weight:700 letter-spacing:-0.03em color:#101828`
      - `span` **text 12px/400** — “가정한 매달 모으는 돈”
        `font-size:12px color:#626D88`
    - `div`
      `margin-top:8px`
      - `div`
        `position:relative height:22px`
        - `div`
          `position:absolute left:0 right:0 top:9px height:5px border-radius:99px background:#E8ECF5`
        - `div`
          `position:absolute left:0 width:50% top:9px height:5px border-radius:99px background:#3556E6`
        - `div`
          `position:absolute left:50% top:0 width:20px height:20px border-radius:99px background:#FFFFFF border:2.5px solid #3556E6 box-shadow:0 2px 6px rgba(16,24,40,.2)`
    - `div`
      `display:flex align-items:center justify-content:space-between margin-top:5px`
      - `span` **text 11px/400** — “0만원”
        `font-size:11px color:#697182`
      - `span` — “가정 종료”
        `display:inline-flex align-items:center gap:4px font-size:12.5px font-weight:600 color:#3556E6`
      - `span` **text 11px/400** — “220만원”
        `font-size:11px color:#697182`
    - `div` **text 11.5px/400** — “부채 상환 목적지는 월 최소 상환액과 추가 상환에 이미 들어 있어 매달 모으는 돈에서 빠져요.”
      `font-size:11.5px line-height:1.5 color:#626D88 margin-top:8px`
  - `div` **Card(18)**
    `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px 8px`
    - `div`
      `display:flex align-items:center justify-content:space-between gap:8px`
      - `span` **text 14px/600** — “진행 중인 목적지”
        `font-size:14px font-weight:600 color:#101828`
      - `span` **text 12px/500** — “우선순위 순으로 보여요”
        `font-size:12px font-weight:500 color:#626D88`
    - `div`
      `display:flex align-items:center gap:11px border:1px dashed #B79BFF border-radius:13px padding:11px 6px`
      - `div`
        `width:44px height:44px border-radius:99px background:conic-gradient(#38bdf8 0% 68%, #E8ECF5 68% 100%) display:flex align-items:center justify-content:center`
        - `div` — “68”
          `width:33px height:33px border-radius:99px background:#FFFFFF display:flex align-items:center justify-content:center font-size:11.5px font-weight:700 color:#0A72AC`
      - `div`
        `flex:1`
        - `div`
          `display:flex align-items:center gap:5px`
        - `div` — “1,020 / 1,500만원 ·”
          `font-size:12px color:#475467 margin-top:2px`
        - `div`
          `font-size:11.5px line-height:1.45 color:#626D88 margin-top:1px`
      - `div` — “적립”
        `display:inline-flex align-items:center gap:3px height:32px padding:0 10px border-radius:9px background:#E4F2FB color:#0A72AC font-size:12.5px font-weight:600`
    - `div`
      `display:flex align-items:center gap:11px border:1px dashed #B79BFF border-radius:13px padding:11px 6px`
      - `div`
        `width:44px height:44px border-radius:99px background:conic-gradient(#7A3FE4 0% 42%, #E8ECF5 42% 100%) display:flex align-items:center justify-content:center`
        - `div` — “42”
          `width:33px height:33px border-radius:99px background:#FFFFFF display:flex align-items:center justify-content:center font-size:11.5px font-weight:700 color:#7A3FE4`
      - `div`
        `flex:1`
        - `div`
          `display:flex align-items:center gap:5px`
        - `div` — “2,100 / 5,000만원 ·”
          `font-size:12px color:#475467 margin-top:2px`
        - `div` — “· ·”
          `font-size:11.5px line-height:1.45 color:#626D88 margin-top:1px`
      - `div` — “적립”
        `display:inline-flex align-items:center gap:3px height:32px padding:0 10px border-radius:9px background:#F1EAFD color:#6B32D6 font-size:12.5px font-weight:600`
    - `div`
      `display:flex align-items:center gap:11px padding:11px 0 border-top:1px solid #F3F5FA`
      - `div`
        `width:44px height:44px border-radius:99px background:conic-gradient(#B45309 0% 31%, #E8ECF5 31% 100%) display:flex align-items:center justify-content:center`
        - `div` — “31”
          `width:33px height:33px border-radius:99px background:#FFFFFF display:flex align-items:center justify-content:center font-size:11.5px font-weight:700 color:#B45309`
      - `div`
        `flex:1`
        - `div`
          `display:flex align-items:center gap:5px`
        - `div` **text 12px/400** — “남은 원금 2,200만원 · 연 6.8%”
          `font-size:12px color:#475467 margin-top:2px`
        - `div` **text 11.5px/400** — “다 갚는 달 2030년 11월 · 상환 계획대로”
          `font-size:11.5px line-height:1.45 color:#626D88 margin-top:1px`
    - `div`
      `display:flex align-items:center gap:11px padding:11px 0 border-top:1px solid #F3F5FA`
      - `div`
        `width:44px height:44px border-radius:99px background:conic-gradient(#3556E6 0% 47%, #E8ECF5 47% 100%) display:flex align-items:center justify-content:center`
        - `div` — “47”
          `width:33px height:33px border-radius:99px background:#FFFFFF display:flex align-items:center justify-content:center font-size:11.5px font-weight:700 color:#3556E6`
      - `div`
        `flex:1`
        - `div`
          `display:flex align-items:center gap:5px`
        - `div` **text 12px/400** — “9,350만 / 2억원 · 자산에서 자동으로 계산”
          `font-size:12px color:#475467 margin-top:2px`
        - `div` **text 11.5px/400** — “도착 예상 2031년 1월 · 미래 탭 계산”
          `font-size:11.5px line-height:1.45 color:#626D88 margin-top:1px`
  - `div` **text 11.5px/400** — “바뀐 목적지 줄만 보라 점선 + 「가정」 칩이고, 매달 · 도착 글자도 보라예요. 「가정 종료」를 누르거나 탭을 떠”
    `font-size:11.5px line-height:1.5 color:#626D88 padding:0 4px`
  - `div` **text 11px/600** — “B · 비상금 6개월 한 줄을 펼쳤을 때”
    `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
  - `div` **Card(18)**
    `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px 14px`
    - `div`
      `display:flex align-items:center gap:11px padding:11px 0`
      - `div`
        `width:44px height:44px border-radius:99px background:conic-gradient(#38bdf8 0% 68%, #E8ECF5 68% 100%) display:flex align-items:center justify-content:center`
        - `div` — “68”
          `width:33px height:33px border-radius:99px background:#FFFFFF display:flex align-items:center justify-content:center font-size:11.5px font-weight:700 color:#0A72AC`
      - `div`
        `flex:1`
        - `div`
          `display:flex align-items:center gap:5px`
        - `div` **text 12px/400** — “1,020 / 1,500만원 · 매달 70만원”
          `font-size:12px color:#475467 margin-top:2px`
        - `div` — “도착 예상 2027년 4월 ·”
          `font-size:11.5px line-height:1.45 color:#626D88 margin-top:1px`
      - `div` — “적립”
        `display:inline-flex align-items:center gap:3px height:32px padding:0 10px border-radius:9px background:#E4F2FB color:#0A72AC font-size:12.5px font-weight:600`
    - `div`
      `display:flex align-items:center justify-content:space-between gap:8px margin-top:4px font-size:12px color:#626D88`
      - `span` — “조정 필요 · 비상금 · 우선순위 1”
      - `span` — “목표일 2027년 3월 8일”
        `white-space:nowrap`
    - `div` **Callout(info)**
      `margin-top:9px padding:11px 12px background:#F4F6FB border-radius:12px`
      - `div` — “자산 탭의 현금성 자산은 이에요.”
        `font-size:12.5px color:#475467`
        - `b` — “1,460만원”
          `font-weight:700`
      - `div` **text 12.5px/600** — “이 금액으로 맞추기”
        `display:inline-flex align-items:center height:34px padding:0 12px margin-top:8px border-radius:10px border:1px solid #E3E8F1 background:#FFFFFF font-size:12.5px font-weight:600 color:#101828`
    - `div`
      `display:flex align-items:center justify-content:space-between margin-top:11px font-size:12px color:#626D88`
      - `span` — “자세히”
      - `span` — “접기 ⌃”
        `font-weight:600 color:#3556E6`
    - `div`
      `display:grid grid-template-columns:repeat(2, minmax(0, 1fr)) gap:8px margin-top:8px`
      - `div` **Callout(info)**
        `padding:10px 11px background:#F4F6FB border-radius:12px`
        - `div` **text 11.5px/400** — “매달 필요한 돈”
          `font-size:11.5px color:#626D88`
        - `div` **text 14px/700** — “80만원”
          `font-size:14px font-weight:700 color:#101828 margin-top:3px`
      - `div` **Callout(info)**
        `padding:10px 11px background:#F4F6FB border-radius:12px`
        - `div` **text 11.5px/400** — “이 목적지에 매달 넣을 돈”
          `font-size:11.5px color:#626D88`
        - `div` **text 14px/700** — “70만원”
          `font-size:14px font-weight:700 color:#101828 margin-top:3px`
      - `div` **Callout(info)**
        `padding:10px 11px background:#F4F6FB border-radius:12px`
        - `div` **text 11.5px/400** — “목표일 대비”
          `font-size:11.5px color:#626D88`
        - `div` **text 12px/700** — “목표일보다 약 1개월 늦어요”
          `font-size:12px font-weight:700 color:#C0342F margin-top:3px`
      - `div` **Callout(info)**
        `padding:10px 11px background:#F4F6FB border-radius:12px`
        - `div` **text 11.5px/400** — “도착 예상”
          `font-size:11.5px color:#626D88`
        - `div` **text 14px/700** — “2027년 4월”
          `font-size:14px font-weight:700 color:#101828 margin-top:3px`
    - `div` **Callout(info)**
      `margin-top:8px padding:10px 11px background:#F4F6FB border-radius:12px`
      - `div` **text 11.5px/400** — “소비 계획에서 빼는 몫”
        `font-size:11.5px color:#626D88`
      - `div` **text 14px/700** — “매달 80만원”
        `font-size:14px font-weight:700 color:#101828 margin-top:3px`
      - `div` **text 11px/400** — “이 몫은 '저축 · 상환 계획까지 지키려면' 금액에서만 빠져요. 이번 달 한도는 소비 목표로만 판단해요.”
        `font-size:11px line-height:1.5 color:#626D88 margin-top:3px`
    - `div` **text 12px/400** — “이 목적지에 쓰는 수익률 연 0.0% · 언제든 쓸 수 있는 현금이라 수익률 0%로 계산해요”
      `font-size:12px line-height:1.5 color:#475467 margin-top:8px`
    - `div` **text 12.5px/600** — “홈에 표시”
      `display:inline-flex align-items:center height:34px padding:0 12px margin-top:8px border-radius:10px border:1px solid #E3E8F1 background:#F4F6FB font-size:12.5px font-weight:600 color:#101828`
  - `div` **text 11.5px/400** — “「홈에 표시」는 홈 구성에 「대표 목적지」 카드를 켠 사람에게만 뜻이 있어요 — 기본 홈에는 대표 목적지 카드가 없”
    `font-size:11.5px line-height:1.5 color:#626D88 padding:0 4px`
  - `div` **text 11px/600** — “C · 비상금이 도착했을 때(1,500 / 1,500만원)”
    `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
  - `div` **Card(18)**
    `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:15px 16px`
    - `div`
      `display:flex align-items:center justify-content:space-between gap:8px`
      - `span` **text 11px/600** — “매달 모으는 돈”
        `font-size:11px font-weight:600 letter-spacing:0.07em color:#626D88`
      - `span` **text 12.5px/600** — “매달 모으는 돈 바꿔 보기 ›”
        `font-size:12.5px font-weight:600 color:#3556E6 white-space:nowrap`
    - `div`
      `display:flex align-items:flex-end justify-content:space-between gap:10px margin-top:7px`
      - `div`
        `display:flex align-items:baseline gap:2px`
        - `span` **text 30px/700** — “90”
          `font-size:30px font-weight:700 letter-spacing:-0.035em line-height:1.05 color:#101828`
        - `span` **text 16px/600** — “만원”
          `font-size:16px font-weight:600 color:#475467`
        - `span` **text 12.5px/500** — “목적지에 나눠 넣는 중”
          `font-size:12.5px font-weight:500 color:#626D88 white-space:nowrap`
      - `span` — “모두 도착하려면”
        `font-size:12.5px font-weight:500 color:#626D88 white-space:nowrap`
        - `span` — “66만원”
          `font-weight:600 color:#101828`
    - `div` **text 11.5px/400** — “월급 + 부수입 390만 − 월말 예상 소비 208만 − 대출상환 92만 = 90만원”
      `font-size:11.5px line-height:1.5 color:#475467 margin-top:6px letter-spacing:-0.02em white-space:nowrap`
    - `div` **text 11.5px/400** — “홈의 '월말 예상 여유 8만원'은 소비 목표(월급의 60%)에서 월말 예상 소비를 뺀 돈이라 이 금액과 달라요.”
      `font-size:11.5px line-height:1.5 color:#626D88 margin-top:4px`
    - `div` **ProgressTrack**
      `position:relative height:9px border-radius:99px background:#E8ECF5 margin-top:11px`
      - `div`
        `position:absolute inset:0 0.0% 0 0 border-radius:99px background:linear-gradient(90deg, #3556E6 0%, #7A3FE4 100%)`
    - `div` **Callout(info)**
      `display:flex gap:8px margin-top:11px padding:10px 11px background:#F4F6FB border-radius:12px`
      - `span`
        `margin-top:1px`
      - `span` — “나눠 넣고도 매달 이 남아요. 목표일과 나눠 넣는 돈을 확인해 주세요.”
        `font-size:12.5px line-height:1.5 color:#475467`
        - `b` — “23만원”
          `font-weight:700`
  - `div` **Card(18)**
    `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px 8px`
    - `div`
      `display:flex align-items:center justify-content:space-between gap:8px`
      - `span` **text 14px/600** — “진행 중인 목적지”
        `font-size:14px font-weight:600 color:#101828`
      - `span` **text 12px/500** — “우선순위 순으로 보여요”
        `font-size:12px font-weight:500 color:#626D88`
    - `div`
      `display:flex align-items:center gap:11px padding:11px 0 border-top:1px solid #F3F5FA`
      - `div`
        `width:44px height:44px border-radius:99px background:conic-gradient(#7A3FE4 0% 42%, #E8ECF5 42% 100%) display:flex align-items:center justify-content:center`
        - `div` — “42”
          `width:33px height:33px border-radius:99px background:#FFFFFF display:flex align-items:center justify-content:center font-size:11.5px font-weight:700 color:#7A3FE4`
      - `div`
        `flex:1`
        - `div`
          `display:flex align-items:center gap:5px`
        - `div` **text 12px/400** — “2,100 / 5,000만원 · 매달 66만원”
          `font-size:12px color:#475467 margin-top:2px`
        - `div` — “도착 예상 2029년 9월 ·”
          `font-size:11.5px line-height:1.45 color:#626D88 margin-top:1px`
      - `div` — “적립”
        `display:inline-flex align-items:center gap:3px height:32px padding:0 10px border-radius:9px background:#F1EAFD color:#6B32D6 font-size:12.5px font-weight:600`
    - `div`
      `display:flex align-items:center gap:11px padding:11px 0 border-top:1px solid #F3F5FA`
      - `div`
        `width:44px height:44px border-radius:99px background:conic-gradient(#B45309 0% 31%, #E8ECF5 31% 100%) display:flex align-items:center justify-content:center`
        - `div` — “31”
          `width:33px height:33px border-radius:99px background:#FFFFFF display:flex align-items:center justify-content:center font-size:11.5px font-weight:700 color:#B45309`
      - `div`
        `flex:1`
        - `div`
          `display:flex align-items:center gap:5px`
        - `div` **text 12px/400** — “남은 원금 2,200만원 · 연 6.8%”
          `font-size:12px color:#475467 margin-top:2px`
        - `div` **text 11.5px/400** — “다 갚는 달 2030년 11월 · 상환 계획대로”
          `font-size:11.5px line-height:1.45 color:#626D88 margin-top:1px`
    - `div`
      `display:flex align-items:center gap:11px padding:11px 0 border-top:1px solid #F3F5FA`
      - `div`
        `width:44px height:44px border-radius:99px background:conic-gradient(#3556E6 0% 47%, #E8ECF5 47% 100%) display:flex align-items:center justify-content:center`
        - `div` — “47”
          `width:33px height:33px border-radius:99px background:#FFFFFF display:flex align-items:center justify-content:center font-size:11.5px font-weight:700 color:#3556E6`
      - `div`
        `flex:1`
        - `div`
          `display:flex align-items:center gap:5px`
        - `div` **text 12px/400** — “9,350만 / 2억원 · 자산에서 자동으로 계산”
          `font-size:12px color:#475467 margin-top:2px`
        - `div` **text 11.5px/400** — “도착 예상 2031년 1월 · 미래 탭 계산”
          `font-size:11.5px line-height:1.45 color:#626D88 margin-top:1px`
  - `div` — “목적지 추가”
    `display:flex align-items:center justify-content:center gap:6px height:46px border-radius:14px border:1.5px dashed #B9C3D6 background:rgba(255,255,255,.55) color:#3556E6 font-size:14px font-weight:600`
  - `div` **Card(18)**
    `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px 8px`
    - `div` **text 14px/600** — “도착한 목적지 1개”
      `font-size:14px font-weight:600 color:#101828`
    - `div`
      `display:flex align-items:center gap:11px padding:11px 0 border-top:1px solid #F3F5FA`
      - `div`
        `width:44px height:44px border-radius:99px background:conic-gradient(#0F7B47 0% 100%, #E8ECF5 100% 100%) display:flex align-items:center justify-content:center`
        - `div` — “100”
          `width:33px height:33px border-radius:99px background:#FFFFFF display:flex align-items:center justify-content:center font-size:11.5px font-weight:700 color:#0F7B47`
      - `div`
        `flex:1`
        - `div`
          `display:flex align-items:center gap:5px`
        - `div` **text 12px/400** — “1,500 / 1,500만원”
          `font-size:12px color:#475467 margin-top:2px`
        - `div` **text 11.5px/400**
          `font-size:11.5px line-height:1.45 color:#626D88 margin-top:1px`
  - `div` **text 11.5px/400** — “도착한 목적지는 진행 중 목록과 「모두 도착하려면」에서 빠지고 「목적지 추가」 아래 「도착한 목적지」로 옮겨 가요.”
    `font-size:11.5px line-height:1.5 color:#626D88 padding:0 4px`
  - `div` **text 11px/600** — “D ① · 목표일이 없는 목적지가 있을 때(투자 계좌의 목표일을 지운 경우)”
    `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
  - `div` **Card(18)**
    `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:15px 16px`
    - `div`
      `display:flex align-items:center justify-content:space-between gap:8px`
      - `span` **text 11px/600** — “매달 모으는 돈”
        `font-size:11px font-weight:600 letter-spacing:0.07em color:#626D88`
      - `span` **text 12.5px/600** — “매달 모으는 돈 바꿔 보기 ›”
        `font-size:12.5px font-weight:600 color:#3556E6 white-space:nowrap`
    - `div`
      `display:flex align-items:baseline gap:2px margin-top:7px`
      - `span` **text 30px/700** — “90”
        `font-size:30px font-weight:700 letter-spacing:-0.035em line-height:1.05 color:#101828`
      - `span` **text 16px/600** — “만원”
        `font-size:16px font-weight:600 color:#475467`
      - `span` **text 12.5px/500** — “목적지에 나눠 넣는 중”
        `font-size:12.5px font-weight:500 color:#626D88 white-space:nowrap`
    - `div` — “목표일이 있는 목적지에”
      `text-align:right font-size:12.5px font-weight:500 color:#626D88 margin-top:4px`
      - `span` — “80만원”
        `font-weight:600 color:#101828`
    - `div` **text 11.5px/400** — “월급 + 부수입 390만 − 월말 예상 소비 208만 − 대출상환 92만 = 90만원”
      `font-size:11.5px line-height:1.5 color:#475467 margin-top:6px letter-spacing:-0.02em white-space:nowrap`
    - `div` **text 11.5px/400** — “홈의 '월말 예상 여유 8만원'은 소비 목표(월급의 60%)에서 월말 예상 소비를 뺀 돈이라 이 금액과 달라요.”
      `font-size:11.5px line-height:1.5 color:#626D88 margin-top:4px`
    - `div` **ProgressTrack**
      `position:relative height:9px border-radius:99px background:#E8ECF5 margin-top:11px`
      - `div`
        `position:absolute inset:0 0.0% 0 0 border-radius:99px background:linear-gradient(90deg, #3556E6 0%, #7A3FE4 100%)`
    - `div` **Callout(warn)**
      `display:flex gap:8px margin-top:11px padding:10px 11px background:#FDF1E0 border-radius:12px`
      - `span`
        `margin-top:2px`
      - `span` **text 12.5px/400** — “1개 목적지의 목표일을 다시 정해 주세요. 그동안 그 목적지는 매달 나눠 넣는 계산에서 빠져요.”
        `font-size:12.5px line-height:1.5 color:#7A3E0A`
  - `div` **Card(18)**
    `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px 8px`
    - `div`
      `display:flex align-items:center justify-content:space-between gap:8px`
      - `span` **text 14px/600** — “진행 중인 목적지”
        `font-size:14px font-weight:600 color:#101828`
      - `span` **text 12px/500** — “우선순위 순으로 보여요”
        `font-size:12px font-weight:500 color:#626D88`
    - `div`
      `display:flex align-items:center gap:11px padding:11px 0 border-top:1px solid #F3F5FA`
      - `div`
        `width:44px height:44px border-radius:99px background:conic-gradient(#38bdf8 0% 68%, #E8ECF5 68% 100%) display:flex align-items:center justify-content:center`
        - `div` — “68”
          `width:33px height:33px border-radius:99px background:#FFFFFF display:flex align-items:center justify-content:center font-size:11.5px font-weight:700 color:#0A72AC`
      - `div`
        `flex:1`
        - `div`
          `display:flex align-items:center gap:5px`
        - `div` **text 12px/400** — “1,020 / 1,500만원 · 매달 80만원”
          `font-size:12px color:#475467 margin-top:2px`
        - `div` **text 11.5px/400** — “도착 예상 2027년 3월”
          `font-size:11.5px line-height:1.45 color:#626D88 margin-top:1px`
      - `div` — “적립”
        `display:inline-flex align-items:center gap:3px height:32px padding:0 10px border-radius:9px background:#E4F2FB color:#0A72AC font-size:12.5px font-weight:600`
    - `div`
      `display:flex align-items:center gap:11px padding:11px 0 border-top:1px solid #F3F5FA`
      - `div`
        `width:44px height:44px border-radius:99px background:conic-gradient(#7A3FE4 0% 42%, #E8ECF5 42% 100%) display:flex align-items:center justify-content:center`
        - `div` — “42”
          `width:33px height:33px border-radius:99px background:#FFFFFF display:flex align-items:center justify-content:center font-size:11.5px font-weight:700 color:#7A3FE4`
      - `div`
        `flex:1`
        - `div`
          `display:flex align-items:center gap:5px`
        - `div` **text 12px/400** — “2,100 / 5,000만원 · 목표일을 정하면 나눠 넣어요”
          `font-size:12px color:#475467 margin-top:2px`
        - `div` **text 11.5px/400** — “목표일을 다시 정해 주세요”
          `font-size:11.5px line-height:1.45 color:#626D88 margin-top:1px`
      - `div` — “적립”
        `display:inline-flex align-items:center gap:3px height:32px padding:0 10px border-radius:9px background:#F1EAFD color:#6B32D6 font-size:12.5px font-weight:600`
  - `div` **text 11.5px/400** — “그 목적지는 매달 나눠 넣는 계산에서 빠지고(오른쪽 줄 「목표일이 있는 목적지에 80만원」) 줄은 회색 「목표일을 ”
    `font-size:11.5px line-height:1.5 color:#626D88 padding:0 4px`
  - `div` **text 11px/600** — “D ② · 지금 배분으로는 도착하기 어려울 때(목표액 3억원 · 360개월 넘게 걸림)”
    `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
  - `div` **Card(18)**
    `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:4px 14px`
    - `div`
      `display:flex align-items:center gap:11px padding:11px 0`
      - `div`
        `width:44px height:44px border-radius:99px background:conic-gradient(#7A3FE4 0% 7%, #E8ECF5 7% 100%) display:flex align-items:center justify-content:center`
        - `div` — “7”
          `width:33px height:33px border-radius:99px background:#FFFFFF display:flex align-items:center justify-content:center font-size:11.5px font-weight:700 color:#7A3FE4`
      - `div`
        `flex:1`
        - `div`
          `display:flex align-items:center gap:5px`
        - `div` **text 12px/400** — “2,100만 / 3억원 · 매달 19만원”
          `font-size:12px color:#475467 margin-top:2px`
        - `div` — “·”
          `font-size:11.5px line-height:1.45 color:#626D88 margin-top:1px`
      - `div` — “적립”
        `display:inline-flex align-items:center gap:3px height:32px padding:0 10px border-radius:9px background:#F1EAFD color:#6B32D6 font-size:12.5px font-weight:600`
  - `div` **text 11.5px/400** — “도착 달 대신 빨간 「지금 배분으로는 도착하기 어려워요」 · 날짜 없음. 이때 맨 위는 「모두 도착하려면 793만원”
    `font-size:11.5px line-height:1.5 color:#626D88 padding:0 4px`
  - `div` **text 11px/600** — “D ③ · 부채 상환 목적지가 목표일보다 늦을 때(목표일 2029년 3월 8일 · 펼친 모습)”
    `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
  - `div` **Card(18)**
    `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:4px 14px`
    - `div`
      `display:flex align-items:center gap:11px padding:11px 0`
      - `div`
        `width:44px height:44px border-radius:99px background:conic-gradient(#B45309 0% 31%, #E8ECF5 31% 100%) display:flex align-items:center justify-content:center`
        - `div` — “31”
          `width:33px height:33px border-radius:99px background:#FFFFFF display:flex align-items:center justify-content:center font-size:11.5px font-weight:700 color:#B45309`
      - `div`
        `flex:1`
        - `div`
          `display:flex align-items:center gap:5px`
        - `div` **text 12px/400** — “남은 원금 2,200만원 · 연 6.8%”
          `font-size:12px color:#475467 margin-top:2px`
        - `div` — “다 갚는 달 2030년 11월 ·”
          `font-size:11.5px line-height:1.45 color:#626D88 margin-top:1px`
    - `div`
      `display:flex align-items:center justify-content:space-between gap:8px font-size:12px color:#626D88`
      - `span` — “상환 조정 필요 · 부채 상환 · 우선순위 2”
      - `span` — “목표일 2029년 3월 8일”
        `white-space:nowrap`
    - `div`
      `display:flex align-items:center justify-content:space-between margin-top:11px font-size:12px color:#626D88`
      - `span` — “자세히”
      - `span` — “접기 ⌃”
        `font-weight:600 color:#B45309`
    - `div`
      `display:grid grid-template-columns:repeat(2, minmax(0, 1fr)) gap:8px margin-top:8px`
      - `div` **Callout(info)**
        `padding:10px 11px background:#F4F6FB border-radius:12px`
        - `div` **text 11.5px/400** — “매달 갚는 돈”
          `font-size:11.5px color:#626D88`
        - `div` **text 14px/700** — “35만원”
          `font-size:14px font-weight:700 color:#101828 margin-top:3px`
      - `div` **Callout(info)**
        `padding:10px 11px background:#F4F6FB border-radius:12px`
        - `div` **text 11.5px/400** — “매달 모으는 돈에서”
          `font-size:11.5px color:#626D88`
        - `div` **text 14px/700** — “빠져요”
          `font-size:14px font-weight:700 color:#101828 margin-top:3px`
      - `div` **Callout(info)**
        `padding:10px 11px background:#F4F6FB border-radius:12px`
        - `div` **text 11.5px/400** — “목표일 대비”
          `font-size:11.5px color:#626D88`
        - `div` **text 12px/700** — “목표일보다 약 1년 8개월 늦어요”
          `font-size:12px font-weight:700 color:#C0342F margin-top:3px`
      - `div` **Callout(info)**
        `padding:10px 11px background:#F4F6FB border-radius:12px`
        - `div` **text 11.5px/400** — “다 갚는 달”
          `font-size:11.5px color:#626D88`
        - `div` **text 14px/700** — “2030년 11월”
          `font-size:14px font-weight:700 color:#101828 margin-top:3px`
    - `div` **text 12px/400** — “남은 빚과 상환 계획으로 다 갚는 달을 계산해요”
      `font-size:12px line-height:1.5 color:#475467 margin-top:8px`
    - `div` **text 12.5px/600** — “홈에 표시”
      `display:inline-flex align-items:center height:34px padding:0 12px border-radius:10px border:1px solid #E3E8F1 background:#F4F6FB font-size:12.5px font-weight:600 color:#101828`
  - `div` **text 11.5px/400** — “「상환 계획대로」 대신 빨간 「목표일보다 약 1년 8개월 늦어요」, 펼치면 상태가 「상환 조정 필요」 — 다 갚는 ”
    `font-size:11.5px line-height:1.5 color:#626D88 padding:0 4px`
  - `div` **text 11px/600** — “D ④ · 새 목적지 설계 — 저장하면 새 목적지가 도착하기 어려울 때(목표액 3억원)”
    `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
  - `div` **Card(18)**
    `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 15px`
    - `div` **text 13px/700** — “저장하면 이렇게 바뀌어요”
      `font-size:13px font-weight:700 color:#101828`
    - `div`
      `display:flex flex-direction:column gap:4px margin-top:6px font-size:12px line-height:1.5 color:#475467`
      - `div` — “결혼 자금 매달 13만원 ·”
        - `span` — “지금 배분으로는 도착하기 어려워요”
          `color:#C0342F`
      - `div` — “비상금 6개월 매달 70만 → 60만원 ·”
        - `span` — “도착 2027년 4월 →”
          `color:#C0342F`
      - `div` — “투자 계좌 5,000만원 매달 19만 → 17만원 ·”
        - `span` — “도착 2033년 12월 →”
          `color:#C0342F`
  - `div` **text 11.5px/400** — “새 목적지 줄이 빨간 「지금 배분으로는 도착하기 어려워요」, 기존 목적지가 360개월을 넘기면 「도착 … → 도착하”
    `font-size:11.5px line-height:1.5 color:#626D88 padding:0 4px`
