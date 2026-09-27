# HeroOverTarget — 블록 개요

원본 `canvas/HeroOverTarget.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div`
  `width:1230px height:765px background:#EDF0F7 color:#101828 padding:28px 30px 30px display:flex flex-direction:column gap:10px`
  - `span` **text 11px/600** — “구현 참고 · 앱 화면이 아닙니다”
    `font-size:11px font-weight:600 letter-spacing:0.02em color:#475467 border:1px solid #E3E8F1 background:#FFFFFF border-radius:99px padding:4px 10px`
  - `h2` **text 20px/700** — “홈 맨 위 카드 · 소비 목표를 넘을 때”
    `font-size:20px font-weight:700 letter-spacing:-0.025em color:#101828`
  - `p` — “같은 시안 8일 · 각주 두 줄)에서 소비 목표나 쓴 돈만 바꾼 세 경우입니다. 카드의 틀은 그대로이고 글과 색만 ”
    `font-size:13px line-height:1.55 color:#626D88`
    - `span` — “사용자(9월”
      `white-space:nowrap`
  - `div`
    `display:grid grid-template-columns:repeat(3, 362px) gap:24px 28px align-items:start`
    - `div`
      `display:flex flex-direction:column gap:8px`
      - `div`
        - `div`
          `display:flex align-items:center gap:7px`
        - `div` — “소비 목표 저장하면 선 · 오른쪽 줄 · 배지 · 셋째 칸이 새 소비 목표 180만원으로 바로 바뀝니다. 쓴 돈 월”
          `font-size:12px line-height:1.5 color:#626D88 margin-top:3px`
      - `div` **HeroCard**
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
        - `div`
          `display:flex align-items:center justify-content:space-between gap:8px min-height:28px`
        - `div`
          `display:flex align-items:flex-end justify-content:space-between gap:10px margin-top:8px`
        - `div`
          `display:flex align-items:baseline justify-content:space-between gap:10px margin-top:5px`
        - `div`
          `margin-top:15px`
        - `div`
          `display:grid grid-template-columns:repeat(3, minmax(0, 1fr)) gap:0 margin-top:14px border-top:1px solid #EFF2F8`
        - `div`
          `display:flex align-items:center justify-content:space-between gap:10px margin-top:12px`
        - `p` **text 11px/400** — “카테고리 없는 32,000원은 적은 금액 그대로 예상에 더했어요”
          `font-size:11px line-height:1.4 color:#626D88`
        - `p` **text 11px/400** — “지난 고정비 기록을 보고 앞으로 나갈 돈도 예상했어요”
          `font-size:11px line-height:1.4 color:#626D88`
    - `div`
      `display:flex flex-direction:column gap:8px`
      - `div`
        - `div`
          `display:flex align-items:center gap:7px`
        - `div` — “이번 달 쓴 돈이 목표 216만원 + 32,000원)이 된 날. 오른쪽 줄은 주황, 이번 달 한도 카드는”
          `font-size:12px line-height:1.5 color:#626D88 margin-top:3px`
      - `div` **HeroCard**
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
        - `div`
          `display:flex align-items:center justify-content:space-between gap:8px min-height:28px`
        - `div`
          `display:flex align-items:flex-end justify-content:space-between gap:10px margin-top:8px`
        - `div`
          `display:flex align-items:baseline justify-content:space-between gap:10px margin-top:5px`
        - `div`
          `margin-top:15px`
        - `div`
          `display:grid grid-template-columns:repeat(3, minmax(0, 1fr)) gap:0 margin-top:14px border-top:1px solid #EFF2F8`
        - `div`
          `display:flex align-items:center justify-content:space-between gap:10px margin-top:12px`
        - `p` **text 11px/400** — “카테고리 없는 32,000원은 적은 금액 그대로 예상에 더했어요”
          `font-size:11px line-height:1.4 color:#626D88`
        - `p` **text 11px/400** — “지난 고정비 기록을 보고 앞으로 나갈 돈도 예상했어요”
          `font-size:11px line-height:1.4 color:#626D88`
    - `div`
      `display:flex flex-direction:column gap:8px`
      - `div`
        - `div`
          `display:flex align-items:center gap:7px`
        - `div` — “쓴 돈이 216만원 = 소비 목표인 날. 오른쪽 줄 주황 · 한도 카드는 ·”
          `font-size:12px line-height:1.5 color:#626D88 margin-top:3px`
      - `div` **HeroCard**
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
        - `div`
          `display:flex align-items:center justify-content:space-between gap:8px min-height:28px`
        - `div`
          `display:flex align-items:flex-end justify-content:space-between gap:10px margin-top:8px`
        - `div`
          `display:flex align-items:baseline justify-content:space-between gap:10px margin-top:5px`
        - `div`
          `margin-top:15px`
        - `div`
          `display:grid grid-template-columns:repeat(3, minmax(0, 1fr)) gap:0 margin-top:14px border-top:1px solid #EFF2F8`
        - `div`
          `display:flex align-items:center justify-content:space-between gap:10px margin-top:12px`
        - `p` **text 11px/400** — “카테고리 없는 32,000원은 적은 금액 그대로 예상에 더했어요”
          `font-size:11px line-height:1.4 color:#626D88`
        - `p` **text 11px/400** — “지난 고정비 기록을 보고 앞으로 나갈 돈도 예상했어요”
          `font-size:11px line-height:1.4 color:#626D88`
  - `p` — “배지는 월말 예상으로만 판정합니다 — 월말 예상 ≤ 소비 목표면 · 시안 사용자 홈), 넘으면 월급마저 넘으면 · ”
    `font-size:12px line-height:1.6 color:#626D88`
    - `span` — “「월말에도 목표 안」(초록”
      `white-space:nowrap`
    - `span` — “「월말엔 목표 초과」(주황),”
      `white-space:nowrap`
    - `span` — “「월말엔 월급 초과」(빨강”
      `white-space:nowrap`
    - `span` — “「월말 예상 여유」”
      `white-space:nowrap`
    - `span` — “「월말 예상 초과」”
      `white-space:nowrap`
    - `span` — “「한도」라는”
      `white-space:nowrap`
