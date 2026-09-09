# MonthlyClose — 블록 개요

원본 `canvas/MonthlyClose.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div` **화면프레임**
  `width:390px height:844px background:#2A3245 color:#101828 display:flex flex-direction:column`
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
        - `h2` **text 18px/700** — “2026년 8월 마감”
          `font-size:18px font-weight:700 letter-spacing:-0.025em color:#101828`
        - `p` **text 12.5px/400** — “그 달의 실제 수치를 확정합니다. 저장한 값으로만 과거 소비율을 계산해요.”
          `font-size:12.5px line-height:1.45 color:#626D88`
      - `div`
        `width:36px height:36px border-radius:11px background:#F4F6FB display:flex align-items:center justify-content:center`
    - `div`
      `flex:1 min-height:0 padding:14px 18px 0 display:flex flex-direction:column gap:15px`
      - `div` **Callout(warn)**
        `display:flex gap:8px padding:10px 11px background:#FDF1E0 border-radius:12px`
        - `span`
          `margin-top:1px`
        - `span` — “이미 에 마감한 달입니다. 다시 저장하면 기존 마감값을 덮어씁니다.”
          `font-size:11.5px line-height:1.5 color:#7A3E0A`
      - `div`
        - `div`
          `display:flex align-items:baseline justify-content:space-between gap:8px`
        - `div`
          `display:flex gap:10px`
        - `div`
          `display:flex gap:10px margin-top:12px`
      - `div`
        - `div`
          `display:flex align-items:baseline justify-content:space-between gap:8px`
        - `div`
          `padding:2px 13px background:#F4F6FB border-radius:14px`
      - `div` **Callout(info)**
        `display:flex gap:8px padding:10px 11px background:#F4F6FB border-radius:12px`
        - `span`
          `margin-top:1px`
        - `span` — “급여를 비워 두면 그 달은 로 남습니다. 지금 급여로 과거를 채우지 않아요.”
          `font-size:11.5px line-height:1.5 color:#626D88`
    - `div`
      `padding:12px 18px background:#F4F6FB border-top:1px solid #E3E8F1`
      - `div`
        `display:flex align-items:flex-start gap:9px`
        - `span`
          `width:20px height:20px border-radius:6px background:#3556E6 display:flex align-items:center justify-content:center`
        - `span` **text 12.5px/400** — “위 수치가 실제와 같음을 확인했습니다.”
          `font-size:12.5px line-height:1.5 color:#475467`
    - `div`
      `display:flex gap:10px padding:12px 18px 20px border-top:1px solid #EFF2F8`
      - `div` **SecondaryButton(48)** — “취소”
        `display:flex align-items:center justify-content:center gap:6px height:48px flex:1 border-radius:13px background:#FFFFFF border:1px solid #D7DEEA color:#475467 font-size:15px font-weight:600`
      - `div` **PrimaryButton(48)** — “마감 저장”
        `display:flex align-items:center justify-content:center gap:6px height:48px flex:1.4 border-radius:13px background:#3556E6 border:none color:#FFFFFF font-size:15px font-weight:600`
