# Tokens — 블록 개요

원본 `canvas/Tokens.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div`
  `width:1200px height:1684px background:#FFFFFF color:#101828 padding:40px 44px display:flex flex-direction:column gap:30px`
  - `div`
    `display:flex align-items:flex-end justify-content:space-between gap:20px border-bottom:2px solid #101828`
    - `div`
      - `div`
        `display:flex align-items:center gap:10px`
        - `div`
          `width:30px height:30px border-radius:10px background:linear-gradient(140deg, #3556E6 0%, #7A3FE4 100%) display:flex align-items:center justify-content:center`
        - `span` **text 12px/600** — “NAVI DESIGN SYSTEM v3”
          `font-size:12px font-weight:600 letter-spacing:0.14em color:#626D88`
      - `h1` **text 34px/700** — “색 · 타이포 · 간격 토큰”
        `font-size:34px font-weight:700 letter-spacing:-0.035em line-height:1.15 color:#101828`
    - `p` **text 13px/400** — “2.2 구현에서 뽑아낸 값을 대체하는 새 토큰입니다. 카테고리·자산 고정 팔레트만 데이터 정체성으로 그대로 두고, ”
      `font-size:13px line-height:1.55 color:#475467`
  - `div`
    `display:grid grid-template-columns:repeat(2, minmax(0, 1fr)) gap:26px`
    - `div`
      - `div` **text 12px/600** — “01 · 표면과 잉크 — LIGHT”
        `font-size:12px font-weight:600 letter-spacing:0.1em color:#626D88`
      - `div`
        `display:grid grid-template-columns:repeat(5, minmax(0, 1fr)) gap:8px margin-top:12px`
        - `div`
        - `div`
        - `div`
        - `div`
        - `div`
      - `div`
        `display:grid grid-template-columns:repeat(5, minmax(0, 1fr)) gap:8px margin-top:12px`
        - `div`
        - `div`
        - `div`
        - `div`
        - `div`
    - `div`
      - `div` **text 12px/600** — “02 · 표면과 잉크 — DARK”
        `font-size:12px font-weight:600 letter-spacing:0.1em color:#626D88`
      - `div`
        `background:#080C16 border-radius:14px padding:14px margin-top:12px`
        - `div`
          `display:grid grid-template-columns:repeat(5, minmax(0, 1fr)) gap:8px`
        - `div`
          `display:grid grid-template-columns:repeat(5, minmax(0, 1fr)) gap:8px margin-top:10px`
  - `div`
    - `div` **text 12px/600** — “03 · 브랜드와 상태색 — 의미가 고정된 색 · 라이트/다크 대응”
      `font-size:12px font-weight:600 letter-spacing:0.1em color:#626D88`
    - `div`
      `display:grid grid-template-columns:repeat(6, minmax(0, 1fr)) gap:12px margin-top:12px`
      - `div`
        `border:1px solid #E3E8F1 border-radius:14px`
        - `div`
          `height:62px background:linear-gradient(140deg, #3556E6 0%, #7A3FE4 100%)`
        - `div`
          `padding:10px 12px`
      - `div`
        `border:1px solid #E3E8F1 border-radius:14px`
        - `div`
          `height:62px background:#3556E6`
        - `div`
          `padding:10px 12px`
      - `div`
        `border:1px solid #E3E8F1 border-radius:14px`
        - `div`
          `height:62px background:#0F7B47`
        - `div`
          `padding:10px 12px`
      - `div`
        `border:1px solid #E3E8F1 border-radius:14px`
        - `div`
          `height:62px background:#B45309`
        - `div`
          `padding:10px 12px`
      - `div`
        `border:1px solid #E3E8F1 border-radius:14px`
        - `div`
          `height:62px background:#C0342F`
        - `div`
          `padding:10px 12px`
      - `div`
        `border:1px solid #E3E8F1 border-radius:14px`
        - `div`
          `height:62px background:#7A3FE4`
        - `div`
          `padding:10px 12px`
    - `div` **Callout(info)**
      `display:flex gap:10px margin-top:12px padding:12px 14px background:#F4F6FB border-radius:12px`
      - `span` — “홈 소비 가정, 미저장 상환 계획, 목표 계산기 결과처럼 저장 전 시뮬레이션은 모두 보라 + 점선 테두리 + “저장”
        `font-size:12px line-height:1.55 color:#475467`
        - `span` — “보라 = 확정되지 않은 값.”
          `font-weight:600 color:#101828`
        - `span` — “회색(ink-4) = 미측정·미입력”
          `font-weight:600 color:#101828`
  - `div`
    - `div`
      `display:flex align-items:baseline gap:12px`
      - `span` **text 12px/600** — “04 · 데이터 팔레트 — 2.2에서 그대로 유지”
        `font-size:12px font-weight:600 letter-spacing:0.1em color:#626D88`
      - `span` **text 11.5px/400** — “거래·차트·범례가 이 색으로 식별되므로 변경하지 않습니다”
        `font-size:11.5px color:#697182`
    - `div`
      `display:flex flex-wrap:wrap gap:7px margin-top:12px`
      - `div`
        `display:inline-flex align-items:center gap:6px height:30px padding:0 11px border-radius:99px border:1px solid #E3E8F1`
        - `span`
          `width:10px height:10px border-radius:3px background:#f97316`
        - `span` **text 12px/400** — “식비”
          `font-size:12px color:#475467`
      - `div`
        `display:inline-flex align-items:center gap:6px height:30px padding:0 11px border-radius:99px border:1px solid #E3E8F1`
        - `span`
          `width:10px height:10px border-radius:3px background:#d97706`
        - `span` **text 12px/400** — “카페/간식”
          `font-size:12px color:#475467`
      - `div`
        `display:inline-flex align-items:center gap:6px height:30px padding:0 11px border-radius:99px border:1px solid #E3E8F1`
        - `span`
          `width:10px height:10px border-radius:3px background:#0ea5e9`
        - `span` **text 12px/400** — “교통”
          `font-size:12px color:#475467`
      - `div`
        `display:inline-flex align-items:center gap:6px height:30px padding:0 11px border-radius:99px border:1px solid #E3E8F1`
        - `span`
          `width:10px height:10px border-radius:3px background:#8b5cf6`
        - `span` **text 12px/400** — “주거/관리”
          `font-size:12px color:#475467`
      - `div`
        `display:inline-flex align-items:center gap:6px height:30px padding:0 11px border-radius:99px border:1px solid #E3E8F1`
        - `span`
          `width:10px height:10px border-radius:3px background:#6366f1`
        - `span` **text 12px/400** — “통신”
          `font-size:12px color:#475467`
      - `div`
        `display:inline-flex align-items:center gap:6px height:30px padding:0 11px border-radius:99px border:1px solid #E3E8F1`
        - `span`
          `width:10px height:10px border-radius:3px background:#0d9488`
        - `span` **text 12px/400** — “보험”
          `font-size:12px color:#475467`
      - `div`
        `display:inline-flex align-items:center gap:6px height:30px padding:0 11px border-radius:99px border:1px solid #E3E8F1`
        - `span`
          `width:10px height:10px border-radius:3px background:#a855f7`
        - `span` **text 12px/400** — “구독”
          `font-size:12px color:#475467`
      - `div`
        `display:inline-flex align-items:center gap:6px height:30px padding:0 11px border-radius:99px border:1px solid #E3E8F1`
        - `span`
          `width:10px height:10px border-radius:3px background:#ec4899`
        - `span` **text 12px/400** — “쇼핑”
          `font-size:12px color:#475467`
      - `div`
        `display:inline-flex align-items:center gap:6px height:30px padding:0 11px border-radius:99px border:1px solid #E3E8F1`
        - `span`
          `width:10px height:10px border-radius:3px background:#14b8a6`
        - `span` **text 12px/400** — “문화/여가”
          `font-size:12px color:#475467`
      - `div`
        `display:inline-flex align-items:center gap:6px height:30px padding:0 11px border-radius:99px border:1px solid #E3E8F1`
        - `span`
          `width:10px height:10px border-radius:3px background:#22c55e`
        - `span` **text 12px/400** — “의료/건강”
          `font-size:12px color:#475467`
      - `div`
        `display:inline-flex align-items:center gap:6px height:30px padding:0 11px border-radius:99px border:1px solid #E3E8F1`
        - `span`
          `width:10px height:10px border-radius:3px background:#3b82f6`
        - `span` **text 12px/400** — “교육”
          `font-size:12px color:#475467`
      - `div`
        `display:inline-flex align-items:center gap:6px height:30px padding:0 11px border-radius:99px border:1px solid #E3E8F1`
        - `span`
          `width:10px height:10px border-radius:3px background:#f43f5e`
        - `span` **text 12px/400** — “경조사”
          `font-size:12px color:#475467`
      - `div`
        `display:inline-flex align-items:center gap:6px height:30px padding:0 11px border-radius:99px border:1px solid #E3E8F1`
        - `span`
          `width:10px height:10px border-radius:3px background:#64748b`
        - `span` **text 12px/400** — “기타”
          `font-size:12px color:#475467`
      - `div`
        `display:inline-flex align-items:center gap:6px height:30px padding:0 11px border-radius:99px border:1px dashed #CFD7E6`
        - `span`
          `width:10px height:10px border-radius:3px background:#34d17e`
        - `span` **text 12px/400** — “저축/투자 · 소비 제외”
          `font-size:12px color:#475467`
      - `div`
        `display:inline-flex align-items:center gap:6px height:30px padding:0 11px border-radius:99px border:1px dashed #CFD7E6`
        - `span`
          `width:10px height:10px border-radius:3px background:#94a3b8`
        - `span` **text 12px/400** — “대출상환 · 소비 제외”
          `font-size:12px color:#475467`
      - `div`
        `width:1px height:30px background:#E3E8F1`
      - `div`
        `display:inline-flex align-items:center gap:6px height:30px padding:0 11px border-radius:99px border:1px solid #E3E8F1`
        - `span`
          `width:10px height:10px border-radius:3px background:#38bdf8`
        - `span` **text 12px/400** — “현금성”
          `font-size:12px color:#475467`
      - `div`
        `display:inline-flex align-items:center gap:6px height:30px padding:0 11px border-radius:99px border:1px solid #E3E8F1`
        - `span`
          `width:10px height:10px border-radius:3px background:#5b8dff`
        - `span` **text 12px/400** — “투자”
          `font-size:12px color:#475467`
      - `div`
        `display:inline-flex align-items:center gap:6px height:30px padding:0 11px border-radius:99px border:1px solid #E3E8F1`
        - `span`
          `width:10px height:10px border-radius:3px background:#8b5cf6`
        - `span` **text 12px/400** — “연금”
          `font-size:12px color:#475467`
      - `div`
        `display:inline-flex align-items:center gap:6px height:30px padding:0 11px border-radius:99px border:1px solid #E3E8F1`
        - `span`
          `width:10px height:10px border-radius:3px background:#f59e0b`
        - `span` **text 12px/400** — “부동산”
          `font-size:12px color:#475467`
  - `div`
    `display:grid grid-template-columns:minmax(0, 1.35fr) minmax(0, 1fr) gap:30px`
    - `div`
      - `div`
        `display:flex align-items:baseline gap:12px`
        - `span` **text 12px/600** — “05 · 타이포 위계”
          `font-size:12px font-weight:600 letter-spacing:0.1em color:#626D88`
        - `span` **text 11.5px/400** — “IBM Plex Sans KR · 숫자는 항상 tabular-nums”
          `font-size:11.5px color:#697182`
      - `div`
        `display:flex flex-direction:column margin-top:12px border-top:1px solid #E3E8F1`
        - `div`
          `display:flex align-items:baseline gap:20px padding:13px 0 border-bottom:1px solid #EFF2F8`
        - `div`
          `display:flex align-items:baseline gap:20px padding:13px 0 border-bottom:1px solid #EFF2F8`
        - `div`
          `display:flex align-items:baseline gap:20px padding:13px 0 border-bottom:1px solid #EFF2F8`
        - `div`
          `display:flex align-items:baseline gap:20px padding:13px 0 border-bottom:1px solid #EFF2F8`
        - `div`
          `display:flex align-items:baseline gap:20px padding:13px 0 border-bottom:1px solid #EFF2F8`
        - `div`
          `display:flex align-items:baseline gap:20px padding:13px 0 border-bottom:1px solid #EFF2F8`
        - `div`
          `display:flex align-items:baseline gap:20px padding:13px 0 border-bottom:1px solid #EFF2F8`
        - `div`
          `display:flex align-items:baseline gap:20px padding:13px 0 border-bottom:1px solid #EFF2F8`
        - `div`
          `display:flex align-items:baseline gap:20px padding:13px 0 border-bottom:1px solid #EFF2F8`
      - `div` **Callout(info)**
        `display:flex gap:10px margin-top:12px padding:12px 14px background:#F4F6FB border-radius:12px`
        - `span` — “2.2에는 17·18·20·21·23·26·32px가 뒤섞여 있었습니다. v3는 본문 역할을 로 고정하고, 여기에 ”
          `font-size:12px line-height:1.55 color:#475467`
    - `div`
      - `div` **text 12px/600** — “06 · 간격 · 모서리 · 그림자”
        `font-size:12px font-weight:600 letter-spacing:0.1em color:#626D88`
      - `div`
        `margin-top:12px border:1px solid #E3E8F1 border-radius:14px`
        - `div`
          `display:flex align-items:center gap:14px padding:11px 14px border-bottom:1px solid #EFF2F8`
        - `div`
          `display:flex align-items:center gap:14px padding:11px 14px border-bottom:1px solid #EFF2F8`
        - `div`
          `display:flex align-items:center gap:14px padding:14px background:#EDF0F7`
      - `div` **text 12px/600** — “07 · 그래프 규칙”
        `font-size:12px font-weight:600 letter-spacing:0.1em color:#626D88 margin-top:24px`
      - `div`
        `margin-top:12px border:1px solid #E3E8F1 border-radius:14px padding:14px`
        - `div`
          `display:flex gap:9px border-bottom:1px solid #EFF2F8`
        - `div`
          `display:flex gap:9px padding:11px 0 border-bottom:1px solid #EFF2F8`
        - `div`
          `display:flex gap:9px padding:11px 0 border-bottom:1px solid #EFF2F8`
        - `div`
          `display:flex gap:9px padding:11px 0 border-bottom:1px solid #EFF2F8`
        - `div`
          `display:flex gap:9px`
