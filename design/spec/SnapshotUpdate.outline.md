# SnapshotUpdate — 블록 개요

원본 `canvas/SnapshotUpdate.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div`
  `width:1180px height:762px background:#EDF0F7 color:#101828 padding:28px 30px 30px display:flex flex-direction:column gap:10px`
  - `span` **text 11px/600** — “구현 참고 · 앱 화면이 아닙니다”
    `font-size:11px font-weight:600 letter-spacing:0.02em color:#475467 border:1px solid #E3E8F1 background:#FFFFFF border-radius:99px padding:4px 10px`
  - `h2` **text 20px/700** — “종목 데이터 새로 받기 · 순서대로”
    `font-size:20px font-weight:700 letter-spacing:-0.025em color:#101828`
  - `p` **text 13px/400** — “주식 설정에서 [새로 받기]를 누르면 이 순서로 바뀌어요. 받다가 실패해도 지금 데이터로 그대로 쓸 수 있어요.”
    `font-size:13px line-height:1.55 color:#626D88`
  - `div`
    `display:flex gap:28px align-items:flex-start`
    - `div`
      `width:362px display:flex flex-direction:column`
      - `div` **text 11px/600** — “시작 · 주식 설정에서 [새로 받기]를 누르면”
        `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:0 2px 6px`
      - `div`
        `border-radius:22px background:#2A3245`
        - `div`
          `height:40px display:flex align-items:flex-end justify-content:center`
        - `div` **BottomSheet**
          `background:#FFFFFF border-radius:26px 26px 0 0 color:#101828`
      - `div`
        `height:22px`
      - `div`
        `display:flex flex-direction:column gap:9px`
        - `div`
          `display:flex gap:9px align-items:flex-start`
        - `div`
          `display:flex align-items:center gap:9px padding:11px 14px background:#101828 border-radius:14px color:#FFFFFF font-size:13px font-weight:500`
    - `div`
      `flex:1`
      - `div`
        `display:grid grid-template-columns:repeat(2, minmax(0, 1fr)) gap:22px 24px align-items:start`
        - `div`
          `display:flex flex-direction:column gap:9px`
        - `div`
          `display:flex flex-direction:column gap:9px`
        - `div`
          `display:flex flex-direction:column gap:9px`
        - `div`
          `display:flex flex-direction:column gap:9px`
      - `p` — “어느 단계에서도 실시간 시세는 받지 않아요. 받는 것은 하나뿐이고, 가격 옆에는 늘 기준일을 함께 보여줘요.”
        `font-size:12px line-height:1.6 color:#626D88`
        - `b` — “기준일 종가가 담긴 파일”
          `font-weight:600 color:#475467`
