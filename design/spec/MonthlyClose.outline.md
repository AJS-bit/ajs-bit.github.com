# MonthlyClose — 블록 개요

원본 `canvas/MonthlyClose.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div`
  `width:390px height:982px background:#2A3245 color:#101828 display:flex flex-direction:column`
  - `div`
    `height:40px display:flex align-items:flex-end justify-content:center`
    - `span` **text 11.5px/500** — “배경을 눌러 닫기”
      `font-size:11.5px font-weight:500 color:rgba(255,255,255,.62)`
  - `div` **BottomSheet**
    `flex:1 min-height:0 background:#FFFFFF border-radius:26px 26px 0 0 display:flex flex-direction:column color:#101828`
    - `div`
      `display:flex justify-content:center padding:9px 0 0`
      - `span` **GrabHandle**
        `width:38px height:4px border-radius:99px background:#D7DEEA`
    - `div`
      `display:flex align-items:flex-start justify-content:space-between gap:10px padding:12px 18px 14px border-bottom:1px solid #EFF2F8`
      - `div`
        - `h2` **text 18px/700** — “8월 마감”
          `font-size:18px font-weight:700 letter-spacing:-0.025em color:#101828`
        - `p` **text 12.5px/400** — “그 달의 실제 수치를 확정해요. 저장한 값으로만 그 달 소비율을 계산해요.”
          `font-size:12.5px line-height:1.45 color:#626D88`
      - `div`
        `width:36px height:36px border-radius:11px background:#F4F6FB display:flex align-items:center justify-content:center`
    - `div`
      `flex:1 min-height:0 padding:14px 18px 14px display:flex flex-direction:column gap:12px`
      - `div` **Callout(warn)**
        `display:flex gap:8px padding:10px 12px background:#FDF1E0 border-radius:12px font-size:12.5px line-height:1.5 color:#7A3E0A`
        - `span`
          `margin-top:1px`
        - `span` — “이미 9월 2일에 마감한 달이에요. 다시 저장하면 전에 저장한 값을 덮어써요.”
      - `div`
        - `div`
          `display:flex align-items:baseline justify-content:space-between gap:8px`
        - `div`
          `flex:0 0 auto`
        - `div`
          `margin-top:12px`
        - `div`
          `margin-top:12px`
      - `div` — “· 다음 달 한도 배분에도 기타로 들어가요 ·”
        `padding:11px 13px border:1px solid #E3E8F1 border-radius:12px font-size:12.5px line-height:1.55 color:#475467`
        - `span` — “카테고리 없음 3건 · 21,200원이 기타로 들어가요”
          `font-weight:600 color:#101828`
        - `span` — “카테고리 고르기 ›”
          `font-weight:600 color:#3556E6 white-space:nowrap`
      - `div`
        - `div`
          `display:flex align-items:baseline justify-content:space-between gap:8px`
        - `div`
          `padding:2px 13px background:#F4F6FB border-radius:14px`
    - `div`
      `padding:11px 18px 12px background:#F4F6FB border-top:1px solid #E3E8F1`
      - `div`
        `display:flex align-items:flex-start gap:9px`
        - `span`
          `width:20px height:20px border-radius:6px border:1.5px solid #CFD7E6`
        - `span` **text 12.5px/400** — “이 달의 수입·상환·잔액을 확인했고, 빠진 소비 기록이 없는지 살펴봤어요”
          `font-size:12.5px line-height:1.5 color:#475467`
    - `div`
      `display:flex gap:10px padding:12px 18px 20px border-top:1px solid #EFF2F8`
      - `div` **SecondaryButton(48)** — “취소”
        `display:flex align-items:center justify-content:center gap:6px height:48px flex:1 border-radius:13px background:#FFFFFF border:1px solid #D7DEEA color:#475467 font-size:15px font-weight:600`
      - `div` **text 15px/600** — “마감 저장”
        `display:flex align-items:center justify-content:center gap:6px height:48px flex:1.4 border-radius:13px background:#E8ECF5 border:none color:#B4BECD font-size:15px font-weight:600`
