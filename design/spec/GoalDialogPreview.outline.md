# GoalDialogPreview — 블록 개요

원본 `canvas/GoalDialogPreview.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div`
  `width:390px height:981px background:#2A3245 color:#101828 display:flex flex-direction:column`
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
        - `h2` **text 18px/700** — “목적지 추가”
          `font-size:18px font-weight:700 letter-spacing:-0.025em color:#101828`
        - `p` **text 12.5px/400** — “유형에 따라 필요한 값이 달라져요.”
          `font-size:12.5px line-height:1.45 color:#626D88`
      - `div`
        `width:36px height:36px border-radius:11px background:#F4F6FB display:flex align-items:center justify-content:center`
    - `div`
      `flex:1 min-height:0 padding:14px 18px 14px display:flex flex-direction:column gap:15px`
      - `div`
        - `div`
          `display:flex align-items:baseline justify-content:space-between gap:8px`
        - `div`
          `display:flex gap:6px`
      - `div`
        `flex:0 0 auto`
        - `div` — “이름”
          `font-size:12px font-weight:600 color:#475467`
        - `div` **InputField**
          `display:flex align-items:center gap:5px height:46px padding:0 12px border-radius:11px border:1px solid #CFD7E6 background:#FFFFFF`
      - `div`
        `display:flex align-items:center gap:3px height:23px margin-top:-9px font-size:11.5px color:#626D88`
        - `span` — “표시 아이콘”
        - `span` **text 11.5px/400** — “🎯”
          `font-size:11.5px`
      - `div`
        `display:flex gap:10px align-items:flex-start margin-top:0px`
        - `div`
          `flex:1`
        - `div`
          `flex:1`
      - `div`
        `display:flex gap:10px align-items:flex-start margin-top:0px`
        - `div`
          `flex:1`
        - `div`
          `width:160px`
      - `div` **Callout(info)**
        `padding:10px 12px background:#F4F6FB border-radius:12px display:flex flex-direction:column gap:6px font-size:13px line-height:19.5px color:#475467`
        - `div` — “이대로면 매달 씩 모아야 해요 · 에 도착”
        - `div`
          `display:flex flex-direction:column gap:4px`
        - `div` **text 12px/400** — “저장하면 '저축 · 상환 계획까지 지키려면' 금액이 152만원 → 127만원으로 바뀌어요. 이번 달 한도는 그대로예”
          `font-size:12px line-height:18px color:#626D88`
      - `div` **Callout(info)**
        `display:flex gap:8px padding:10px 11px background:#F4F6FB border-radius:12px`
        - `span`
          `margin-top:1px`
        - `span` **text 11.5px/400** — “수익 없이 넣은 돈만 계산해요”
          `font-size:11.5px line-height:1.5 color:#626D88`
    - `div`
      `display:flex gap:10px padding:12px 18px 20px border-top:1px solid #EFF2F8`
      - `div` **SecondaryButton(48)** — “취소”
        `display:flex align-items:center justify-content:center gap:6px height:48px flex:1 border-radius:13px background:#FFFFFF border:1px solid #D7DEEA color:#475467 font-size:15px font-weight:600`
      - `div` **PrimaryButton(48)** — “목적지 추가”
        `display:flex align-items:center justify-content:center gap:6px height:48px flex:1.4 border-radius:13px background:#3556E6 border:none color:#FFFFFF font-size:15px font-weight:600`
