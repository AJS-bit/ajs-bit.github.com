# GoalTypes — 블록 개요

원본 `canvas/GoalTypes.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div`
  `width:390px height:1767px background:#EDF0F7 color:#101828 padding:18px 14px 20px display:flex flex-direction:column gap:8px`
  - `div`
    `padding:0 2px 6px`
    - `h2` **text 18px/700** — “목적지 유형 5종”
      `font-size:18px font-weight:700 letter-spacing:-0.025em color:#101828`
    - `p` — “유형이 바꾸는 것은 셋뿐입니다 — . 나머지 화면 구조는 다섯 유형이 똑같습니다.”
      `font-size:12px line-height:1.45 color:#626D88`
      - `b` — “수익률 가정 · 현재값을 어디서 가져오는가 · 적립 버튼의 유무”
        `font-weight:600`
  - `div` **text 11px/600** — “A · 일반 저축 — 수익률을 쓰지 않음”
    `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
  - `div` **Card(18)**
    `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px 15px`
    - `div`
      `display:flex align-items:flex-start gap:10px`
      - `span` **text 20px/400** — “💰”
        `font-size:20px line-height:1 margin-top:1px`
      - `div`
        `flex:1`
        - `div`
          `display:flex align-items:center gap:7px`
        - `div` **text 12px/400** — “수익률을 반영하지 않고 넣은 돈만 더합니다.”
          `font-size:12px line-height:1.45 color:#626D88 margin-top:3px`
    - `div`
      `display:flex gap:6px flex-wrap:wrap margin-top:11px`
      - `span` **text 11.5px/600** — “목표액 *”
        `display:inline-flex align-items:center height:27px padding:0 9px border-radius:8px background:#F4F6FB border:1px solid #D7DEEA color:#475467 font-size:11.5px font-weight:600`
      - `span` **text 11.5px/600** — “현재 적립액”
        `display:inline-flex align-items:center height:27px padding:0 9px border-radius:8px background:#F4F6FB border:1px solid #D7DEEA color:#475467 font-size:11.5px font-weight:600`
      - `span` **text 11.5px/600** — “목표일”
        `display:inline-flex align-items:center height:27px padding:0 9px border-radius:8px background:#F4F6FB border:1px solid #D7DEEA color:#475467 font-size:11.5px font-weight:600`
      - `span` **text 11.5px/600** — “연 수익률”
        `display:inline-flex align-items:center height:27px padding:0 9px border-radius:8px background:#FFFFFF border:1px solid #E3E8F1 color:#B4BECD font-size:11.5px font-weight:600`
    - `div`
      `display:flex gap:8px padding:9px 11px background:#F4F6FB border-radius:11px margin-top:10px`
      - `span`
        `margin-top:1px`
      - `span` **text 11.5px/400** — “남은 금액 ÷ 월 배분. 수익률 칸이 아예 없어 “왜 계산이 다르지”가 생기지 않습니다.”
        `font-size:11.5px line-height:1.5 color:#626D88`
    - `div`
      `margin-top:11px border-top:1px solid #F3F5FA`
      - `div` **text 10.5px/600** — “목록에서는 이렇게”
        `font-size:10.5px font-weight:600 letter-spacing:0.06em color:#697182`
      - `div`
        `display:flex align-items:center gap:11px`
        - `div`
          `width:40px height:40px border-radius:99px background:conic-gradient(#3556E6 0% 20%, #E8ECF5 20% 100%) display:flex align-items:center justify-content:center`
        - `div`
          `flex:1`
        - `div` **text 12.5px/600** — “적립”
          `display:inline-flex align-items:center gap:4px height:30px padding:0 11px border-radius:9px background:#E9EDFD border:none color:#3556E6 font-size:12.5px font-weight:600`
  - `div` **text 11px/600** — “B · 투자 — 수익률이 계산에 들어감”
    `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
  - `div` **Card(18)**
    `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px 15px`
    - `div`
      `display:flex align-items:flex-start gap:10px`
      - `span` **text 20px/400** — “🌱”
        `font-size:20px line-height:1 margin-top:1px`
      - `div`
        `flex:1`
        - `div`
          `display:flex align-items:center gap:7px`
        - `div` **text 12px/400** — “설정한 투자 기대수익률을 반영합니다.”
          `font-size:12px line-height:1.45 color:#626D88 margin-top:3px`
    - `div`
      `display:flex gap:6px flex-wrap:wrap margin-top:11px`
      - `span` **text 11.5px/600** — “목표액 *”
        `display:inline-flex align-items:center height:27px padding:0 9px border-radius:8px background:#F4F6FB border:1px solid #D7DEEA color:#475467 font-size:11.5px font-weight:600`
      - `span` **text 11.5px/600** — “현재 평가액”
        `display:inline-flex align-items:center height:27px padding:0 9px border-radius:8px background:#F4F6FB border:1px solid #D7DEEA color:#475467 font-size:11.5px font-weight:600`
      - `span` **text 11.5px/600** — “목표일”
        `display:inline-flex align-items:center height:27px padding:0 9px border-radius:8px background:#F4F6FB border:1px solid #D7DEEA color:#475467 font-size:11.5px font-weight:600`
      - `span` **text 11.5px/600** — “연 기대수익률 5.0%”
        `display:inline-flex align-items:center height:27px padding:0 9px border-radius:8px background:#F1EAFD border:1px solid #F1EAFD color:#6B32D6 font-size:11.5px font-weight:600`
    - `div`
      `display:flex gap:8px padding:9px 11px background:#F4F6FB border-radius:11px margin-top:10px`
      - `span`
        `margin-top:1px`
      - `span` — “복리로 계산합니다. 수익률은 으로 표시하고, 도착 예상 옆에 “가정”을 붙입니다.”
        `font-size:11.5px line-height:1.5 color:#626D88`
        - `b` — “확정값이 아니므로 보라색”
          `font-weight:600`
    - `div`
      `margin-top:11px border-top:1px solid #F3F5FA`
      - `div` **text 10.5px/600** — “목록에서는 이렇게”
        `font-size:10.5px font-weight:600 letter-spacing:0.06em color:#697182`
      - `div`
        `display:flex align-items:center gap:11px`
        - `div`
          `width:40px height:40px border-radius:99px background:conic-gradient(#6B85EC 0% 42%, #E8ECF5 42% 100%) display:flex align-items:center justify-content:center`
        - `div`
          `flex:1`
        - `div` **text 12.5px/600** — “적립”
          `display:inline-flex align-items:center gap:4px height:30px padding:0 11px border-radius:9px background:#E9EDFD border:none color:#3556E6 font-size:12.5px font-weight:600`
  - `div` **text 11px/600** — “C · 순자산 — 값을 직접 넣지 않음”
    `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
  - `div` **Card(18)**
    `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px 15px`
    - `div`
      `display:flex align-items:flex-start gap:10px`
      - `span` **text 20px/400** — “💎”
        `font-size:20px line-height:1 margin-top:1px`
      - `div`
        `flex:1`
        - `div`
          `display:flex align-items:center gap:7px`
        - `div` **text 12px/400** — “현재 순자산과 자산별 가중 기대수익률을 그대로 씁니다.”
          `font-size:12px line-height:1.45 color:#626D88 margin-top:3px`
    - `div`
      `display:flex gap:6px flex-wrap:wrap margin-top:11px`
      - `span` **text 11.5px/600** — “목표액 *”
        `display:inline-flex align-items:center height:27px padding:0 9px border-radius:8px background:#F4F6FB border:1px solid #D7DEEA color:#475467 font-size:11.5px font-weight:600`
      - `span` **text 11.5px/600** — “현재 순자산 9,350만원 · 자동”
        `display:inline-flex align-items:center height:27px padding:0 9px border-radius:8px background:#E9EDFD border:1px solid #E9EDFD color:#3556E6 font-size:11.5px font-weight:600`
      - `span` **text 11.5px/600** — “현재 적립액”
        `display:inline-flex align-items:center height:27px padding:0 9px border-radius:8px background:#FFFFFF border:1px solid #E3E8F1 color:#B4BECD font-size:11.5px font-weight:600`
    - `div`
      `display:flex gap:8px padding:9px 11px background:#F4F6FB border-radius:11px margin-top:10px`
      - `span`
        `margin-top:1px`
      - `span` — “현재값은 자산 화면에서 자동으로 옵니다. 그래서 — 순자산은 자산·부채를 고치면 따라 움직입니다.”
        `font-size:11.5px line-height:1.5 color:#626D88`
        - `b` — “적립 버튼이 없습니다”
          `font-weight:600`
    - `div`
      `margin-top:11px border-top:1px solid #F3F5FA`
      - `div` **text 10.5px/600** — “목록에서는 이렇게”
        `font-size:10.5px font-weight:600 letter-spacing:0.06em color:#697182`
      - `div`
        `display:flex align-items:center gap:11px`
        - `div`
          `width:40px height:40px border-radius:99px background:conic-gradient(#7A3FE4 0% 47%, #E8ECF5 47% 100%) display:flex align-items:center justify-content:center`
        - `div`
          `flex:1`
        - `span` **text 11px/400** — “적립 없음”
          `font-size:11px color:#697182`
  - `div` **text 11px/600** — “D · 부채 상환 — 상환 계획에서 계산”
    `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
  - `div` **Card(18)**
    `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px 15px`
    - `div`
      `display:flex align-items:flex-start gap:10px`
      - `span` **text 20px/400** — “🏔️”
        `font-size:20px line-height:1 margin-top:1px`
      - `div`
        `flex:1`
        - `div`
          `display:flex align-items:center gap:7px`
        - `div` **text 12px/400** — “실제 부채 잔액과 상환 설정에서 진행률·완제일을 계산합니다.”
          `font-size:12px line-height:1.45 color:#626D88 margin-top:3px`
    - `div`
      `display:flex gap:6px flex-wrap:wrap margin-top:11px`
      - `span` **text 11.5px/600** — “연결할 부채 *”
        `display:inline-flex align-items:center height:27px padding:0 9px border-radius:8px background:#F4F6FB border:1px solid #D7DEEA color:#475467 font-size:11.5px font-weight:600`
      - `span` **text 11.5px/600** — “신용대출 ✓”
        `display:inline-flex align-items:center height:27px padding:0 9px border-radius:8px background:#E9EDFD border:1px solid #E9EDFD color:#3556E6 font-size:11.5px font-weight:600`
      - `span` **text 11.5px/600** — “목표액”
        `display:inline-flex align-items:center height:27px padding:0 9px border-radius:8px background:#FFFFFF border:1px solid #E3E8F1 color:#B4BECD font-size:11.5px font-weight:600`
      - `span` **text 11.5px/600** — “적립액”
        `display:inline-flex align-items:center height:27px padding:0 9px border-radius:8px background:#FFFFFF border:1px solid #E3E8F1 color:#B4BECD font-size:11.5px font-weight:600`
    - `div`
      `display:flex gap:8px padding:9px 11px background:#F4F6FB border-radius:11px margin-top:10px`
      - `span`
        `margin-top:1px`
      - `span` — “목표액을 묻지 않습니다. 연결한 부채의 원금이 목표이고, 완제일은 에서 옵니다. 두 화면이 다른 답을 내지 않게 하”
        `font-size:11.5px line-height:1.5 color:#626D88`
        - `b` — “상환 전략 화면의 계획”
          `font-weight:600`
    - `div`
      `margin-top:11px border-top:1px solid #F3F5FA`
      - `div` **text 10.5px/600** — “목록에서는 이렇게”
        `font-size:10.5px font-weight:600 letter-spacing:0.06em color:#697182`
      - `div`
        `display:flex align-items:center gap:11px`
        - `div`
          `width:40px height:40px border-radius:99px background:conic-gradient(#C0342F 0% 31%, #E8ECF5 31% 100%) display:flex align-items:center justify-content:center`
        - `div`
          `flex:1`
        - `span` **text 11px/400** — “적립 없음”
          `font-size:11px color:#697182`
  - `div` **text 11px/600** — “E · 비상금 — 저축과 같되 수익률 0% 고정”
    `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
  - `div` **Card(18)**
    `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px 15px`
    - `div`
      `display:flex align-items:flex-start gap:10px`
      - `span` **text 20px/400** — “🧯”
        `font-size:20px line-height:1 margin-top:1px`
      - `div`
        `flex:1`
        - `div`
          `display:flex align-items:center gap:7px`
        - `div` **text 12px/400** — “언제든 쓸 수 있는 현금으로 보고 수익률은 0%로 계산합니다.”
          `font-size:12px line-height:1.45 color:#626D88 margin-top:3px`
    - `div`
      `display:flex gap:6px flex-wrap:wrap margin-top:11px`
      - `span` **text 11.5px/600** — “목표액 *”
        `display:inline-flex align-items:center height:27px padding:0 9px border-radius:8px background:#F4F6FB border:1px solid #D7DEEA color:#475467 font-size:11.5px font-weight:600`
      - `span` **text 11.5px/600** — “현재 적립액”
        `display:inline-flex align-items:center height:27px padding:0 9px border-radius:8px background:#F4F6FB border:1px solid #D7DEEA color:#475467 font-size:11.5px font-weight:600`
      - `span` **text 11.5px/600** — “목표 개월 수”
        `display:inline-flex align-items:center height:27px padding:0 9px border-radius:8px background:#F4F6FB border:1px solid #D7DEEA color:#475467 font-size:11.5px font-weight:600`
      - `span` **text 11.5px/600** — “연 수익률 0% 고정”
        `display:inline-flex align-items:center height:27px padding:0 9px border-radius:8px background:#FFFFFF border:1px solid #E3E8F1 color:#B4BECD font-size:11.5px font-weight:600`
    - `div`
      `display:flex gap:8px padding:9px 11px background:#F4F6FB border-radius:11px margin-top:10px`
      - `span`
        `margin-top:1px`
      - `span` — “목표액을 로도 채울 수 있습니다. 수익률은 잠겨 있어 “현금을 굴린다”는 오해가 생기지 않습니다.”
        `font-size:11.5px line-height:1.5 color:#626D88`
        - `b` — “월 고정비 × 개월 수”
          `font-weight:600`
    - `div`
      `margin-top:11px border-top:1px solid #F3F5FA`
      - `div` **text 10.5px/600** — “목록에서는 이렇게”
        `font-size:10.5px font-weight:600 letter-spacing:0.06em color:#697182`
      - `div`
        `display:flex align-items:center gap:11px`
        - `div`
          `width:40px height:40px border-radius:99px background:conic-gradient(#3556E6 0% 68%, #E8ECF5 68% 100%) display:flex align-items:center justify-content:center`
        - `div`
          `flex:1`
        - `div` **text 12.5px/600** — “적립”
          `display:inline-flex align-items:center gap:4px height:30px padding:0 11px border-radius:9px background:#E9EDFD border:none color:#3556E6 font-size:12.5px font-weight:600`
