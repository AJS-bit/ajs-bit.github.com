# NetWorthRatioSheet — 블록 개요

원본 `canvas/NetWorthRatioSheet.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div` **화면프레임**
  `width:390px height:844px background:#CFD3E1 color:#101828 display:flex flex-direction:column`
  - `div`
    `height:551px`
  - `div` **BottomSheet**
    `flex:1 min-height:0 position:relative background:#FFFFFF border:1px solid #E3E8F1 border-bottom:0 border-radius:26px 26px 0 0 display:flex flex-direction:column`
    - `span` **GrabHandle**
      `position:absolute top:8px left:50% width:38px height:4px border-radius:99px background:#D7DEEA`
    - `div`
      `padding:24px 56px 20px 20px display:flex flex-direction:column gap:8px`
      - `h2` **text 21px/750** — “순자산 대비 소비”
        `font-size:21px font-weight:750 line-height:25.2px letter-spacing:-0.025em color:#101828`
      - `div`
        `margin-top:10px display:flex flex-direction:column gap:8px`
        - `p` **text 15px/400** — “이번 달 지금까지 쓴 112만원은 내 순자산 9,350만원의 1.2%예요.”
          `font-size:15px line-height:24px color:#101828`
        - `p` **text 15px/400** — “월말 예상 208만원으로 치면 2.2%예요.”
          `font-size:15px line-height:24px color:#101828`
        - `p` **text 13px/400** — “순자산은 가진 자산에서 갚을 부채를 뺀 금액이에요. 순자산이 클수록 같은 소비도 작은 비율이 돼요.”
          `font-size:13px line-height:20.8px color:#626D88`
    - `div`
      `margin-top:auto display:flex gap:10px padding:14px 20px 15px border-top:1px solid #EFF2F8`
      - `div` — “자산 탭에서 보기”
        `flex:1 display:flex align-items:center justify-content:center gap:2px height:44px border-radius:10px font-size:14px font-weight:600 white-space:nowrap background:#EDF0F7 border:1px solid #E3E8F1 color:#101828`
      - `div` **PrimaryButton(44)** — “닫기”
        `flex:1 display:flex align-items:center justify-content:center gap:2px height:44px border-radius:10px font-size:14px font-weight:600 white-space:nowrap background:#3556E6 color:#FFFFFF`
