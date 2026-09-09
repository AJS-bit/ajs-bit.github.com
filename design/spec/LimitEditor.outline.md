# LimitEditor — 블록 개요

원본 `canvas/LimitEditor.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div` **화면프레임**
  `width:390px height:844px background:#2A3245 display:flex flex-direction:column justify-content:flex-end`
  - `div`
    `height:74px display:flex align-items:flex-end justify-content:center`
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
        - `h2` **text 18px/700** — “한도 조정”
          `font-size:18px font-weight:700 letter-spacing:-0.025em color:#101828`
        - `p` — “총한도를 정하고 카테고리로 나눠 주세요. 저장하기 전에는 현재 한도가 바뀌지 않아요.”
          `font-size:12.5px line-height:1.45 color:#626D88`
      - `div`
        `width:36px height:36px border-radius:11px background:#F4F6FB display:flex align-items:center justify-content:center`
    - `div`
      `flex:1 min-height:0 padding:14px 18px 0`
      - `div`
        `background:#F4F6FB border-radius:16px padding:13px`
        - `div`
          `display:flex align-items:center justify-content:space-between gap:8px`
        - `div`
          `display:flex align-items:baseline gap:3px margin-top:9px`
        - `p` **text 11.5px/400** — “실수령 급여 360만원 × 소비 목표 60%. 총수입에서 저축 이체·대출상환을 뺀 금액보다 작아 이 값이 적용됐어요”
          `font-size:11.5px line-height:1.45 color:#626D88`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:8px margin-top:17px`
        - `div`
          `display:flex align-items:baseline gap:7px`
        - `div` — “자동으로 되돌리기”
          `display:inline-flex align-items:center gap:4px height:30px padding:0 11px border-radius:9px background:#F4F6FB border:1px solid #E3E8F1 color:#475467 font-size:12px font-weight:600`
      - `div`
        `display:flex flex-direction:column margin-top:6px`
        - `div`
          `display:flex align-items:center gap:10px height:56px border-bottom:1px solid #F3F5FA`
        - `div`
          `display:flex align-items:center gap:10px height:56px border-bottom:1px solid #F3F5FA`
        - `div`
          `display:flex align-items:center gap:10px height:56px border-bottom:1px solid #F3F5FA`
        - `div`
          `display:flex align-items:center gap:10px height:56px`
    - `div`
      `display:flex align-items:center justify-content:space-between gap:8px padding:11px 18px background:#E4F4EA border-top:1px solid #C9E5D5`
      - `span` — “배분 합계가 총한도와 같아요”
        `display:inline-flex align-items:center gap:6px font-size:12.5px font-weight:600 color:#0F7B47`
      - `span` **text 13px/600** — “216 / 216만원”
        `font-size:13px font-weight:600 color:#0F7B47`
    - `div`
      `display:flex gap:10px padding:12px 18px 20px border-top:1px solid #EFF2F8`
      - `div` **SecondaryButton(48)** — “취소”
        `flex:1 height:48px border-radius:13px border:1px solid #D7DEEA background:#FFFFFF display:flex align-items:center justify-content:center font-size:15px font-weight:600 color:#475467`
      - `div` **PrimaryButton(48)** — “한도 저장”
        `flex:1.4 height:48px border-radius:13px background:#3556E6 display:flex align-items:center justify-content:center font-size:15px font-weight:600 color:#FFFFFF`
