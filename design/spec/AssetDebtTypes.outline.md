# AssetDebtTypes — 블록 개요

원본 `canvas/AssetDebtTypes.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div`
  `width:1400px height:770px background:#EDF0F7 color:#101828 padding:28px 30px 30px display:flex flex-direction:column gap:10px`
  - `span` **text 11px/600** — “구현 참고 · 앱 화면이 아닙니다”
    `font-size:11px font-weight:600 letter-spacing:0.02em color:#475467 border:1px solid #E3E8F1 background:#FFFFFF border-radius:99px padding:4px 10px white-space:nowrap`
  - `h2` **text 20px/700** — “자산 · 부채 유형 목록 · 새 부채 · 다 갚은 부채”
    `font-size:20px font-weight:700 letter-spacing:-0.025em color:#101828`
  - `p` **text 13px/400** — “자산 · 부채 창에서 「유형」을 열었을 때의 목록과, 새 부채를 넣는 창의 처음 모습, 다 갚은 부채가 목록 끝에 ”
    `font-size:13px line-height:1.55 color:#626D88`
  - `div`
    `display:flex gap:22px align-items:flex-start`
    - `div`
      `width:290px`
      - `div` **text 12.5px/700** — “자산 유형 열기”
        `font-size:12.5px font-weight:700 color:#101828`
      - `div`
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:14px padding:5px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 8px 24px -16px rgba(16,24,40,.28)`
        - `div`
          `display:flex align-items:center gap:8px padding:10px 12px border-radius:10px background:#E9EDFD`
        - `div`
          `display:flex align-items:center gap:8px padding:10px 12px border-radius:10px`
        - `div`
          `display:flex align-items:center gap:8px padding:10px 12px border-radius:10px`
        - `div`
          `display:flex align-items:center gap:8px padding:10px 12px border-radius:10px`
        - `div`
          `display:flex align-items:center gap:8px padding:10px 12px border-radius:10px`
      - `p` — “유형 아래 한 줄: 현금성 「비상금(생활비 몇 달 치)과 들어가요」 · 투자 「 들어가요 · 비상금에는 안 들어가요”
        `font-size:12px line-height:1.55 color:#626D88`
        - `span` — “현금+투자자산에”
          `white-space:nowrap`
        - `span` — “현금+투자자산에”
          `white-space:nowrap`
        - `span` — “현금+투자자산에는”
          `white-space:nowrap`
    - `div`
      `width:290px`
      - `div` **text 12.5px/700** — “부채 유형 열기”
        `font-size:12.5px font-weight:700 color:#101828`
      - `div`
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:14px padding:5px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 8px 24px -16px rgba(16,24,40,.28)`
        - `div`
          `display:flex align-items:center gap:8px padding:10px 12px border-radius:10px`
        - `div`
          `display:flex align-items:center gap:8px padding:10px 12px border-radius:10px background:#E9EDFD`
        - `div`
          `display:flex align-items:center gap:8px padding:10px 12px border-radius:10px`
        - `div`
          `display:flex align-items:center gap:8px padding:10px 12px border-radius:10px`
        - `div`
          `display:flex align-items:center gap:8px padding:10px 12px border-radius:10px`
      - `p` **text 12px/400** — “부채 줄의 부제도 이 이름을 씁니다 — 「주택담보 · 전세대출 · 월 최소 32만원」.”
        `font-size:12px line-height:1.55 color:#626D88`
    - `div`
      `width:370px`
      - `div` **text 12.5px/700** — “새 부채 — 연 금리는 비어서 시작”
        `font-size:12.5px font-weight:700 color:#101828`
      - `div` **Card(18)**
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px`
        - `div`
          `display:flex align-items:flex-start justify-content:space-between gap:10px padding:14px 16px 12px border-bottom:1px solid #EFF2F8`
        - `div`
          `display:flex flex-direction:column gap:13px padding:13px 16px 16px`
        - `div`
          `display:flex gap:10px padding:12px 16px 14px border-top:1px solid #EFF2F8`
      - `p` — “연 금리는 유형 기본값을 자리 글자(예: 6.5)로만 보여 주고 채우지 월 최소 상환액을 비우고 저장하면 한 번 더”
        `font-size:12px line-height:1.55 color:#626D88`
        - `span` — “않습니다(필수 *).”
          `white-space:nowrap`
        - `span` — “「그대로 저장」으로”
          `white-space:nowrap`
    - `div`
      `flex:1`
      - `div` **text 12.5px/700** — “다 갚은 부채 — 부채 목록 맨 아래”
        `font-size:12.5px font-weight:700 color:#101828`
      - `div`
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:16px padding:12px 14px`
        - `div` **text 12px/600** — “다 갚은 부채 1건”
          `font-size:12px font-weight:600 color:#626D88`
        - `div`
          `display:flex align-items:center gap:10px margin-top:10px`
      - `p` **text 12px/400** — “남은 원금을 0으로 저장한 부채는 지우지 않고 「다 갚음」으로 남습니다. 연결된 부채 상환 목적지는 「다 갚았어요」”
        `font-size:12px line-height:1.55 color:#626D88`
