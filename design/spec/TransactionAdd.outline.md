# TransactionAdd — 블록 개요

원본 `canvas/TransactionAdd.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div` **화면프레임**
  `width:390px height:844px background:#2A3245 display:flex flex-direction:column justify-content:flex-end`
  - `div`
    `height:60px display:flex align-items:flex-end justify-content:center`
    - `span` **text 11.5px/500** — “배경을 눌러 닫기”
      `font-size:11.5px font-weight:500 color:rgba(255,255,255,.62)`
  - `div` **BottomSheet**
    `flex:1 min-height:0 background:#FFFFFF border-radius:26px 26px 0 0 display:flex flex-direction:column color:#101828`
    - `div`
      `display:flex justify-content:center padding:9px 0 0`
      - `span` **GrabHandle**
        `width:38px height:4px border-radius:99px background:#D7DEEA`
    - `div`
      `display:flex align-items:center justify-content:space-between gap:10px padding:12px 18px 13px border-bottom:1px solid #EFF2F8`
      - `h2` **text 18px/700** — “거래 추가”
        `font-size:18px font-weight:700 letter-spacing:-0.025em color:#101828`
      - `div`
        `width:36px height:36px border-radius:11px background:#F4F6FB display:flex align-items:center justify-content:center`
    - `div`
      `flex:1 min-height:0 padding:14px 18px 0 display:flex flex-direction:column gap:15px`
      - `div`
        - `div` **text 12px/600** — “거래 종류”
          `font-size:12px font-weight:600 color:#475467`
        - `div`
          `display:flex gap:4px background:#F4F6FB border-radius:11px padding:3px`
      - `div`
        `display:flex gap:10px`
        - `div`
          `flex:1`
        - `div`
          `width:148px`
      - `div`
        - `div`
          `display:flex align-items:baseline justify-content:space-between`
        - `div`
          `display:flex gap:7px`
      - `div`
        - `div` — “메모”
          `font-size:12px font-weight:600 color:#475467`
        - `div` **InputField**
          `display:flex align-items:center height:46px padding:0 12px border-radius:11px border:1px solid #CFD7E6 background:#FFFFFF`
      - `div`
        `background:#F4F6FB border-radius:14px padding:13px`
        - `div`
          `display:flex align-items:center justify-content:space-between gap:10px`
        - `div`
          `display:flex align-items:center justify-content:space-between gap:10px height:44px margin-top:10px padding:0 12px border-radius:11px border:1px solid #CFD7E6 background:#FFFFFF`
      - `div`
        `display:flex gap:7px padding:0 2px`
        - `span` **text 11.5px/400** — “일반 소비는 월급 대비 소비율과 카테고리 한도에 함께 반영됩니다. 저축·투자 이체와 대출상환은 소비율에서 제외돼요.”
          `font-size:11.5px line-height:1.45 color:#626D88`
    - `div`
      `display:flex gap:10px padding:12px 18px 20px border-top:1px solid #EFF2F8`
      - `div` **SecondaryButton(48)** — “취소”
        `flex:1 height:48px border-radius:13px border:1px solid #D7DEEA background:#FFFFFF display:flex align-items:center justify-content:center font-size:15px font-weight:600 color:#475467`
      - `div` **PrimaryButton(48)** — “거래 저장”
        `flex:1.4 height:48px border-radius:13px background:#3556E6 display:flex align-items:center justify-content:center font-size:15px font-weight:600 color:#FFFFFF`
