# GoalTypes — 블록 개요

원본 `canvas/GoalTypes.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div`
  `width:390px height:1920px background:#EDF0F7 color:#101828 padding:18px 14px 20px display:flex flex-direction:column gap:8px`
  - `div`
    `padding:0 2px 6px`
    - `span` **text 11px/600** — “구현 참고 · 앱 화면이 아닙니다”
      `display:inline-block font-size:11px font-weight:600 letter-spacing:0.02em color:#475467 border:1px solid #E3E8F1 background:#FFFFFF border-radius:99px padding:4px 10px white-space:nowrap`
    - `h2` **text 18px/700** — “목적지 유형 5종”
      `font-size:18px font-weight:700 letter-spacing:-0.025em color:#101828`
    - `p` **text 12px/400** — “목적지 유형마다 입력하는 칸과 계산 방식이 어떻게 다른지 보여 줍니다.”
      `font-size:12px line-height:1.45 color:#626D88`
    - `div`
      `display:flex flex-wrap:wrap gap:5px 12px margin-top:9px font-size:11px color:#626D88`
      - `span` — “진한 칸 = 직접 입력”
        `display:inline-flex align-items:center gap:5px white-space:nowrap`
        - `span` **text 10px/600** — “가”
          `display:inline-flex align-items:center height:16px padding:0 5px border-radius:5px background:#F4F6FB border:1px solid #CFD7E6 color:#475467 font-size:10px font-weight:600 line-height:1`
      - `span` — “파란 칸 = 자동으로 채워짐”
        `display:inline-flex align-items:center gap:5px white-space:nowrap`
        - `span` **text 10px/600** — “가”
          `display:inline-flex align-items:center height:16px padding:0 5px border-radius:5px background:#E9EDFD border:1px solid #3556E6 color:#3556E6 font-size:10px font-weight:600 line-height:1`
      - `span` — “보라 칸 = 가정값”
        `display:inline-flex align-items:center gap:5px white-space:nowrap`
        - `span` **text 10px/600** — “가”
          `display:inline-flex align-items:center height:16px padding:0 5px border-radius:5px background:#F1EAFD border:1px solid #B79BFF color:#6B32D6 font-size:10px font-weight:600 line-height:1`
      - `span` — “흐린 칸 = 이 유형에는 없음”
        `display:inline-flex align-items:center gap:5px white-space:nowrap`
        - `span` **text 10px/600** — “가”
          `display:inline-flex align-items:center height:16px padding:0 5px border-radius:5px background:#FFFFFF border:1px dashed #B4BECD color:#B4BECD font-size:10px font-weight:600 line-height:1`
  - `div` **text 11px/600** — “A · 일반 저축”
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
    - `div` **text 10.5px/600** — “입력하는 칸”
      `font-size:10.5px font-weight:600 letter-spacing:0.06em color:#697182 margin-top:12px`
    - `div`
      `display:flex gap:6px flex-wrap:wrap margin-top:6px`
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
      - `span` **text 11.5px/400** — “남은 금액을 월 적립액으로 나눠 도착 예상일을 계산합니다.”
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
  - `div` **text 11px/600** — “B · 투자”
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
    - `div` **text 10.5px/600** — “입력하는 칸”
      `font-size:10.5px font-weight:600 letter-spacing:0.06em color:#697182 margin-top:12px`
    - `div`
      `display:flex gap:6px flex-wrap:wrap margin-top:6px`
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
      - `span` **text 11.5px/400** — “복리로 계산합니다. 수익률은 가정값이라 도착 예상 옆에 “가정”이 붙습니다.”
        `font-size:11.5px line-height:1.5 color:#626D88`
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
  - `div` **text 11px/600** — “C · 순자산”
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
    - `div` **text 10.5px/600** — “입력하는 칸”
      `font-size:10.5px font-weight:600 letter-spacing:0.06em color:#697182 margin-top:12px`
    - `div`
      `display:flex gap:6px flex-wrap:wrap margin-top:6px`
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
      - `span` **text 11.5px/400** — “현재 순자산은 자산 화면에서 자동으로 가져옵니다. 직접 넣는 값이 아니어서 적립 버튼이 없습니다.”
        `font-size:11.5px line-height:1.5 color:#626D88`
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
  - `div` **text 11px/600** — “D · 부채 상환”
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
    - `div` **text 10.5px/600** — “입력하는 칸”
      `font-size:10.5px font-weight:600 letter-spacing:0.06em color:#697182 margin-top:12px`
    - `div`
      `display:flex gap:6px flex-wrap:wrap margin-top:6px`
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
      - `span` **text 11.5px/400** — “연결한 부채의 남은 원금이 목표가 됩니다. 완제 예상일은 상환 전략 화면의 계획을 그대로 씁니다.”
        `font-size:11.5px line-height:1.5 color:#626D88`
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
  - `div` **text 11px/600** — “E · 비상금”
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
    - `div` **text 10.5px/600** — “입력하는 칸”
      `font-size:10.5px font-weight:600 letter-spacing:0.06em color:#697182 margin-top:12px`
    - `div`
      `display:flex gap:6px flex-wrap:wrap margin-top:6px`
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
      - `span` **text 11.5px/400** — “목표액은 월 고정비 × 개월 수로도 정할 수 있습니다. 수익률은 0%로 고정됩니다.”
        `font-size:11.5px line-height:1.5 color:#626D88`
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
