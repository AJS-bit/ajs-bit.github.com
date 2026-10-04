# GoalDesignStates — 블록 개요

원본 `canvas/GoalDesignStates.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div`
  `width:390px height:1421px background:#EDF0F7 color:#101828 padding:18px 14px 20px display:flex flex-direction:column gap:8px`
  - `div`
    `padding:0 2px 6px`
    - `span` **text 11px/600** — “구현 참고 · 앱 화면이 아닙니다”
      `display:inline-block font-size:11px font-weight:600 letter-spacing:0.02em color:#475467 border:1px solid #E3E8F1 background:#FFFFFF border-radius:99px padding:4px 10px white-space:nowrap`
    - `h2` **text 18px/700** — “새 목적지 설계 · 상태 2종”
      `font-size:18px font-weight:700 letter-spacing:-0.025em color:#101828`
    - `p` **text 12px/400** — “처음 들어갔을 때(빈 칸)와 「다른 금액으로 계산해 보기」에 매달 넣을 돈을 넣어 본 가정입니다.”
      `font-size:12px line-height:1.45 color:#626D88`
  - `div` **text 11px/600** — “A · 처음 들어갔을 때 — 목표액과 기간이 비어 있음”
    `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
  - `div` **HeroCard**
    `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:15px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
    - `div`
      `display:flex gap:10px align-items:flex-start`
      - `div`
        `flex:1`
        - `div` **text 12px/600** — “이름”
          `font-size:12px font-weight:600 color:#475467`
        - `div` **InputField**
          `display:flex align-items:center gap:5px height:46px padding:0 12px border-radius:11px border:1px solid #CFD7E6 background:#FFFFFF`
      - `div`
        `width:124px`
        - `div` — “목표액”
          `font-size:12px font-weight:600 color:#475467`
        - `div` **InputField**
          `display:flex align-items:center gap:5px height:46px padding:0 12px border-radius:11px border:1px solid #CFD7E6 background:#FFFFFF`
    - `div`
      `display:flex gap:10px margin-top:12px align-items:flex-start`
      - `div`
        `flex:1`
        - `div` **text 12px/600** — “지금 모은 돈”
          `font-size:12px font-weight:600 color:#475467`
        - `div` **InputField**
          `display:flex align-items:center gap:5px height:46px padding:0 12px border-radius:11px border:1px solid #CFD7E6 background:#FFFFFF`
      - `div`
        `flex:1`
        - `div` — “기간”
          `font-size:12px font-weight:600 color:#475467`
        - `div` **InputField**
          `display:flex align-items:center gap:5px height:46px padding:0 12px border-radius:11px border:1px solid #CFD7E6 background:#FFFFFF`
        - `div`
          `display:flex gap:4px margin-top:6px`
      - `div`
        `flex:1`
        - `div` **text 12px/600** — “수익률 (연)”
          `font-size:12px font-weight:600 color:#475467`
        - `div` **InputField**
          `display:flex align-items:center gap:5px height:46px padding:0 12px border-radius:11px border:1px solid #CFD7E6 background:#FFFFFF`
    - `div` **text 11.5px/400** — “수익률을 비워 두면 일반 저축(수익률 0%)으로 계산해요.”
      `font-size:11.5px line-height:1.45 color:#626D88 margin-top:10px`
    - `div` **text 12px/400** — “목표액과 기간을 넣으면 매달 필요한 돈을 계산해요.”
      `margin-top:10px font-size:12px line-height:1.45 color:#626D88`
    - `div`
      `margin-top:14px`
      - `div` **text 15px/600** — “목적지로 저장”
        `display:flex align-items:center justify-content:center gap:6px height:46px width:100% border-radius:13px background:#3556E6 border:none color:#FFFFFF font-size:15px font-weight:600`
  - `div` **text 11.5px/400** — “빈 칸은 빨간 오류가 아니라 회색 안내 한 줄이에요. 목표액 · 기간을 넣으면 매달 넣어야 할 돈과 「저장하면 이렇”
    `font-size:11.5px line-height:1.5 color:#626D88 padding:0 4px`
  - `div` **text 11px/600** — “B · 「다른 금액으로 계산해 보기」에 매달 30만원을 넣었을 때”
    `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
  - `div` **HeroCard**
    `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:15px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
    - `div` **text 13px/600** — “결혼 자금 · 목표액 3,000만원 · 지금 모은 돈 500만원 · 7년 · 수익률 연 4%”
      `font-size:13px font-weight:600 color:#101828`
    - `div`
      `margin-top:10px`
    - `div` — “가정 매달 30만원 · 7년 뒤 3,553만”
      `display:flex align-items:center gap:6px margin-top:6px font-size:12px font-weight:600 color:#6B32D6`
      - `span`
        `width:16px height:0 border-top:2px dashed #7A3FE4`
    - `div` **text 12px/400** — “위의 「저장하면 이렇게 바뀌어요」는 매달 넣어야 할 돈(24만원) 기준 그대로예요.”
      `font-size:12px line-height:1.5 color:#626D88 margin-top:8px`
  - `div` **Card(18)**
    `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
    - `div`
      `display:flex align-items:center justify-content:space-between gap:8px`
      - `span` **text 13.5px/600** — “매달 30만원 넣는 가정 · 계산 기준”
        `font-size:13.5px font-weight:600 color:#101828`
    - `div` **text 12px/400** — “매달 넣을 돈을 적어 보면 그 돈으로 모았을 때를 보라 점선으로 보여 줘요. 이 목적지 하나만 본 가정이에요. 목적”
      `font-size:12px line-height:1.55 color:#475467 margin-top:8px`
    - `div`
      `margin-top:12px`
      - `div`
        `flex:0 0 auto`
        - `div` **text 12px/600** — “매달 넣을 돈 (가정)”
          `font-size:12px font-weight:600 color:#475467`
        - `div` **InputField**
          `display:flex align-items:center gap:5px height:46px padding:0 12px border-radius:11px border:1px solid #CFD7E6 background:#FFFFFF`
        - `div` **text 12px/500** — “= 30만원”
          `font-size:12px font-weight:500 line-height:16px color:#626D88 margin-top:4px white-space:nowrap`
    - `div`
      `display:flex align-items:flex-end justify-content:space-between gap:8px margin-top:12px padding:12px background:#F1EAFD border-radius:14px`
      - `div`
        - `div` **text 11.5px/600** — “가정대로 7년 뒤”
          `font-size:11.5px font-weight:600 color:#6B32D6`
        - `div` — “3,553”
          `font-size:22px font-weight:700 letter-spacing:-0.03em color:#6B32D6 margin-top:2px`
      - `span` **text 12px/600** — “목표액에 닿아요”
        `font-size:12px font-weight:600 color:#6B32D6`
    - `div` **text 11.5px/400** — “보라 실선: 매달 넣어야 할 돈으로 모은 금액 · 회색 점선: 원금만(수익 없이 넣은 돈) · 보라 점선: 매달 넣”
      `font-size:11.5px line-height:1.55 color:#626D88 margin-top:10px`
    - `div` **text 11.5px/400** — “추천 목적지는 필요한 것만 고르세요. 비상금은 자산 탭의 현금성 자산으로 채워 드려요 · 비상금으로 따로 둔 돈만 ”
      `font-size:11.5px line-height:1.55 color:#626D88 margin-top:8px`
  - `div` **text 11.5px/400** — “보라 점선 · 「가정」은 금액을 넣은 뒤에만 그려요. 넣은 금액은 저장되지 않아요.”
    `font-size:11.5px line-height:1.5 color:#626D88 padding:0 4px`
