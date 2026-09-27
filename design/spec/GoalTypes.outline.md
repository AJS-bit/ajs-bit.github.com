# GoalTypes — 블록 개요

원본 `canvas/GoalTypes.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div`
  `width:390px height:2170px background:#EDF0F7 color:#101828 padding:18px 14px 20px display:flex flex-direction:column gap:8px`
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
        - `div` **text 12px/400** — “수익 없이 넣은 돈만 계산해요”
          `font-size:12px line-height:1.45 color:#626D88 margin-top:3px`
    - `div` **text 10.5px/600** — “입력하는 칸”
      `font-size:10.5px font-weight:600 letter-spacing:0.06em color:#697182 margin-top:12px`
    - `div`
      `display:flex gap:6px flex-wrap:wrap margin-top:6px`
      - `span` **text 11.5px/600** — “이름 *”
        `display:inline-flex align-items:center height:27px padding:0 9px border-radius:8px background:#F4F6FB border:1px solid #D7DEEA color:#475467 font-size:11.5px font-weight:600`
      - `span` **text 11.5px/600** — “표시 아이콘”
        `display:inline-flex align-items:center height:27px padding:0 9px border-radius:8px background:#F4F6FB border:1px solid #D7DEEA color:#475467 font-size:11.5px font-weight:600`
      - `span` **text 11.5px/600** — “목표액 *”
        `display:inline-flex align-items:center height:27px padding:0 9px border-radius:8px background:#F4F6FB border:1px solid #D7DEEA color:#475467 font-size:11.5px font-weight:600`
      - `span` **text 11.5px/600** — “지금 모은 돈”
        `display:inline-flex align-items:center height:27px padding:0 9px border-radius:8px background:#F4F6FB border:1px solid #D7DEEA color:#475467 font-size:11.5px font-weight:600`
      - `span` **text 11.5px/600** — “우선순위”
        `display:inline-flex align-items:center height:27px padding:0 9px border-radius:8px background:#F4F6FB border:1px solid #D7DEEA color:#475467 font-size:11.5px font-weight:600`
      - `span` **text 11.5px/600** — “목표일 *”
        `display:inline-flex align-items:center height:27px padding:0 9px border-radius:8px background:#F4F6FB border:1px solid #D7DEEA color:#475467 font-size:11.5px font-weight:600`
      - `span` **text 11.5px/600** — “6개월 · 1년 · 2년”
        `display:inline-flex align-items:center height:27px padding:0 9px border-radius:8px background:#F4F6FB border:1px solid #D7DEEA color:#475467 font-size:11.5px font-weight:600`
    - `div`
      `display:flex gap:8px padding:9px 11px background:#F4F6FB border-radius:11px margin-top:10px`
      - `span`
        `margin-top:1px`
      - `span` **text 11.5px/400** — “남은 금액을 매달 넣을 돈으로 나눠 도착 예상 달을 계산해요.”
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
        - `div` **text 12.5px/600** — “+ 적립”
          `display:inline-flex align-items:center height:30px padding:0 11px border-radius:9px background:#E9EDFD color:#3556E6 font-size:12.5px font-weight:600 white-space:nowrap`
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
        - `div` **text 12px/400** — “설정의 투자 자산 기본 수익률로 계산해요”
          `font-size:12px line-height:1.45 color:#626D88 margin-top:3px`
    - `div` **text 10.5px/600** — “입력하는 칸”
      `font-size:10.5px font-weight:600 letter-spacing:0.06em color:#697182 margin-top:12px`
    - `div`
      `display:flex gap:6px flex-wrap:wrap margin-top:6px`
      - `span` **text 11.5px/600** — “이름 *”
        `display:inline-flex align-items:center height:27px padding:0 9px border-radius:8px background:#F4F6FB border:1px solid #D7DEEA color:#475467 font-size:11.5px font-weight:600`
      - `span` **text 11.5px/600** — “표시 아이콘”
        `display:inline-flex align-items:center height:27px padding:0 9px border-radius:8px background:#F4F6FB border:1px solid #D7DEEA color:#475467 font-size:11.5px font-weight:600`
      - `span` **text 11.5px/600** — “목표액 *”
        `display:inline-flex align-items:center height:27px padding:0 9px border-radius:8px background:#F4F6FB border:1px solid #D7DEEA color:#475467 font-size:11.5px font-weight:600`
      - `span` **text 11.5px/600** — “지금 금액”
        `display:inline-flex align-items:center height:27px padding:0 9px border-radius:8px background:#F4F6FB border:1px solid #D7DEEA color:#475467 font-size:11.5px font-weight:600`
      - `span` **text 11.5px/600** — “수익률 (연)”
        `display:inline-flex align-items:center height:27px padding:0 9px border-radius:8px background:#F4F6FB border:1px solid #D7DEEA color:#475467 font-size:11.5px font-weight:600`
      - `span` **text 11.5px/600** — “우선순위”
        `display:inline-flex align-items:center height:27px padding:0 9px border-radius:8px background:#F4F6FB border:1px solid #D7DEEA color:#475467 font-size:11.5px font-weight:600`
      - `span` **text 11.5px/600** — “목표일 *”
        `display:inline-flex align-items:center height:27px padding:0 9px border-radius:8px background:#F4F6FB border:1px solid #D7DEEA color:#475467 font-size:11.5px font-weight:600`
      - `span` **text 11.5px/600** — “6개월 · 1년 · 2년”
        `display:inline-flex align-items:center height:27px padding:0 9px border-radius:8px background:#F4F6FB border:1px solid #D7DEEA color:#475467 font-size:11.5px font-weight:600`
    - `div`
      `display:flex gap:8px padding:9px 11px background:#F4F6FB border-radius:11px margin-top:10px`
      - `span`
        `margin-top:1px`
      - `span` **text 11.5px/400** — “복리로 계산해요. 수익률을 비우면 설정의 투자 자산 기본 수익률(연 5.0%)을 써요.”
        `font-size:11.5px line-height:1.5 color:#626D88`
    - `div`
      `margin-top:11px border-top:1px solid #F3F5FA`
      - `div` **text 10.5px/600** — “목록에서는 이렇게”
        `font-size:10.5px font-weight:600 letter-spacing:0.06em color:#697182`
      - `div`
        `display:flex align-items:center gap:11px`
        - `div`
          `width:40px height:40px border-radius:99px background:conic-gradient(#7A3FE4 0% 42%, #E8ECF5 42% 100%) display:flex align-items:center justify-content:center`
        - `div`
          `flex:1`
        - `div` **text 12.5px/600** — “+ 적립”
          `display:inline-flex align-items:center height:30px padding:0 11px border-radius:9px background:#F1EAFD color:#6B32D6 font-size:12.5px font-weight:600 white-space:nowrap`
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
        - `div` **text 12px/400** — “지금 순자산과 가진 자산들의 평균 수익률로 계산해요”
          `font-size:12px line-height:1.45 color:#626D88 margin-top:3px`
    - `div` **text 10.5px/600** — “입력하는 칸”
      `font-size:10.5px font-weight:600 letter-spacing:0.06em color:#697182 margin-top:12px`
    - `div`
      `display:flex gap:6px flex-wrap:wrap margin-top:6px`
      - `span` **text 11.5px/600** — “이름 *”
        `display:inline-flex align-items:center height:27px padding:0 9px border-radius:8px background:#F4F6FB border:1px solid #D7DEEA color:#475467 font-size:11.5px font-weight:600`
      - `span` **text 11.5px/600** — “표시 아이콘”
        `display:inline-flex align-items:center height:27px padding:0 9px border-radius:8px background:#F4F6FB border:1px solid #D7DEEA color:#475467 font-size:11.5px font-weight:600`
      - `span` **text 11.5px/600** — “목표액 *”
        `display:inline-flex align-items:center height:27px padding:0 9px border-radius:8px background:#F4F6FB border:1px solid #D7DEEA color:#475467 font-size:11.5px font-weight:600`
      - `span` **text 11.5px/600** — “지금 순자산 · 자동 9,350만원”
        `display:inline-flex align-items:center height:27px padding:0 9px border-radius:8px background:#E9EDFD border:1px solid #E9EDFD color:#3556E6 font-size:11.5px font-weight:600`
      - `span` **text 11.5px/600** — “우선순위”
        `display:inline-flex align-items:center height:27px padding:0 9px border-radius:8px background:#F4F6FB border:1px solid #D7DEEA color:#475467 font-size:11.5px font-weight:600`
      - `span` **text 11.5px/600** — “목표일 *”
        `display:inline-flex align-items:center height:27px padding:0 9px border-radius:8px background:#F4F6FB border:1px solid #D7DEEA color:#475467 font-size:11.5px font-weight:600`
      - `span` **text 11.5px/600** — “지금 모은 돈”
        `display:inline-flex align-items:center height:27px padding:0 9px border-radius:8px background:#FFFFFF border:1px solid #E3E8F1 color:#B4BECD font-size:11.5px font-weight:600`
    - `div`
      `display:flex gap:8px padding:9px 11px background:#F4F6FB border-radius:11px margin-top:10px`
      - `span`
        `margin-top:1px`
      - `span` **text 11.5px/400** — “지금 순자산은 자산 탭에서 자동으로 가져와요 · 적립 버튼이 없어요”
        `font-size:11.5px line-height:1.5 color:#626D88`
    - `div`
      `margin-top:11px border-top:1px solid #F3F5FA`
      - `div` **text 10.5px/600** — “목록에서는 이렇게”
        `font-size:10.5px font-weight:600 letter-spacing:0.06em color:#697182`
      - `div`
        `display:flex align-items:center gap:11px`
        - `div`
          `width:40px height:40px border-radius:99px background:conic-gradient(#3556E6 0% 47%, #E8ECF5 47% 100%) display:flex align-items:center justify-content:center`
        - `div`
          `flex:1`
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
        - `div` **text 12px/400** — “남은 빚과 상환 계획으로 다 갚는 달을 계산해요”
          `font-size:12px line-height:1.45 color:#626D88 margin-top:3px`
    - `div` **text 10.5px/600** — “입력하는 칸”
      `font-size:10.5px font-weight:600 letter-spacing:0.06em color:#697182 margin-top:12px`
    - `div`
      `display:flex gap:6px flex-wrap:wrap margin-top:6px`
      - `span` **text 11.5px/600** — “이름 *”
        `display:inline-flex align-items:center height:27px padding:0 9px border-radius:8px background:#F4F6FB border:1px solid #D7DEEA color:#475467 font-size:11.5px font-weight:600`
      - `span` **text 11.5px/600** — “표시 아이콘”
        `display:inline-flex align-items:center height:27px padding:0 9px border-radius:8px background:#F4F6FB border:1px solid #D7DEEA color:#475467 font-size:11.5px font-weight:600`
      - `span` **text 11.5px/600** — “갚을 부채 · 1개 골랐어요 · 2,200만원”
        `display:inline-flex align-items:center height:27px padding:0 9px border-radius:8px background:#E9EDFD border:1px solid #E9EDFD color:#3556E6 font-size:11.5px font-weight:600`
      - `span` **text 11.5px/600** — “우선순위”
        `display:inline-flex align-items:center height:27px padding:0 9px border-radius:8px background:#F4F6FB border:1px solid #D7DEEA color:#475467 font-size:11.5px font-weight:600`
      - `span` **text 11.5px/600** — “목표일 *”
        `display:inline-flex align-items:center height:27px padding:0 9px border-radius:8px background:#F4F6FB border:1px solid #D7DEEA color:#475467 font-size:11.5px font-weight:600`
      - `span` **text 11.5px/600** — “목표액”
        `display:inline-flex align-items:center height:27px padding:0 9px border-radius:8px background:#FFFFFF border:1px solid #E3E8F1 color:#B4BECD font-size:11.5px font-weight:600`
      - `span` **text 11.5px/600** — “지금 모은 돈”
        `display:inline-flex align-items:center height:27px padding:0 9px border-radius:8px background:#FFFFFF border:1px solid #E3E8F1 color:#B4BECD font-size:11.5px font-weight:600`
    - `div`
      `display:flex gap:8px padding:9px 11px background:#F4F6FB border-radius:11px margin-top:10px`
      - `span`
        `margin-top:1px`
      - `span` **text 11.5px/400** — “목표액과 진행률은 실제 남은 원금에서 자동으로 계산해요. 매달 모으는 돈에서 따로 나눠 넣지 않아요.”
        `font-size:11.5px line-height:1.5 color:#626D88`
    - `div`
      `margin-top:11px border-top:1px solid #F3F5FA`
      - `div` **text 10.5px/600** — “목록에서는 이렇게”
        `font-size:10.5px font-weight:600 letter-spacing:0.06em color:#697182`
      - `div`
        `display:flex align-items:center gap:11px`
        - `div`
          `width:40px height:40px border-radius:99px background:conic-gradient(#B45309 0% 31%, #E8ECF5 31% 100%) display:flex align-items:center justify-content:center`
        - `div`
          `flex:1`
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
        - `div` **text 12px/400** — “언제든 쓸 수 있는 현금이라 수익률 0%로 계산해요”
          `font-size:12px line-height:1.45 color:#626D88 margin-top:3px`
    - `div` **text 10.5px/600** — “입력하는 칸”
      `font-size:10.5px font-weight:600 letter-spacing:0.06em color:#697182 margin-top:12px`
    - `div`
      `display:flex gap:6px flex-wrap:wrap margin-top:6px`
      - `span` **text 11.5px/600** — “이름 *”
        `display:inline-flex align-items:center height:27px padding:0 9px border-radius:8px background:#F4F6FB border:1px solid #D7DEEA color:#475467 font-size:11.5px font-weight:600`
      - `span` **text 11.5px/600** — “표시 아이콘”
        `display:inline-flex align-items:center height:27px padding:0 9px border-radius:8px background:#F4F6FB border:1px solid #D7DEEA color:#475467 font-size:11.5px font-weight:600`
      - `span` **text 11.5px/600** — “목표액 *”
        `display:inline-flex align-items:center height:27px padding:0 9px border-radius:8px background:#F4F6FB border:1px solid #D7DEEA color:#475467 font-size:11.5px font-weight:600`
      - `span` **text 11.5px/600** — “지금 모은 돈”
        `display:inline-flex align-items:center height:27px padding:0 9px border-radius:8px background:#F4F6FB border:1px solid #D7DEEA color:#475467 font-size:11.5px font-weight:600`
      - `span` **text 11.5px/600** — “지금 현금성 자산 1,460만원 넣기”
        `display:inline-flex align-items:center height:27px padding:0 9px border-radius:8px background:#E9EDFD border:1px solid #E9EDFD color:#3556E6 font-size:11.5px font-weight:600`
      - `span` **text 11.5px/600** — “우선순위”
        `display:inline-flex align-items:center height:27px padding:0 9px border-radius:8px background:#F4F6FB border:1px solid #D7DEEA color:#475467 font-size:11.5px font-weight:600`
      - `span` **text 11.5px/600** — “목표일 *”
        `display:inline-flex align-items:center height:27px padding:0 9px border-radius:8px background:#F4F6FB border:1px solid #D7DEEA color:#475467 font-size:11.5px font-weight:600`
      - `span` **text 11.5px/600** — “6개월 · 1년 · 2년”
        `display:inline-flex align-items:center height:27px padding:0 9px border-radius:8px background:#F4F6FB border:1px solid #D7DEEA color:#475467 font-size:11.5px font-weight:600`
    - `div`
      `display:flex gap:8px padding:9px 11px background:#F4F6FB border-radius:11px margin-top:10px`
      - `span`
        `margin-top:1px`
      - `span` **text 11.5px/400** — “수익률은 0%로 계산해요. 지금 모은 돈 칸 아래 버튼으로 자산 탭의 현금성 자산 금액을 넣을 수 있어요.”
        `font-size:11.5px line-height:1.5 color:#626D88`
    - `div`
      `margin-top:11px border-top:1px solid #F3F5FA`
      - `div` **text 10.5px/600** — “목록에서는 이렇게”
        `font-size:10.5px font-weight:600 letter-spacing:0.06em color:#697182`
      - `div`
        `display:flex align-items:center gap:11px`
        - `div`
          `width:40px height:40px border-radius:99px background:conic-gradient(#38bdf8 0% 68%, #E8ECF5 68% 100%) display:flex align-items:center justify-content:center`
        - `div`
          `flex:1`
        - `div` **text 12.5px/600** — “+ 적립”
          `display:inline-flex align-items:center height:30px padding:0 11px border-radius:9px background:#E4F2FB color:#0A72AC font-size:12.5px font-weight:600 white-space:nowrap`
