# DebtDialog — 블록 개요

원본 `canvas/DebtDialog.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div` **화면프레임**
  `width:390px height:844px background:#2A3245 color:#101828 display:flex flex-direction:column`
  - `div`
    `height:110px display:flex align-items:flex-end justify-content:center`
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
        - `h2` **text 18px/700** — “카드 할부 수정”
          `font-size:18px font-weight:700 letter-spacing:-0.025em color:#101828`
        - `p` **text 12.5px/400** — “거래에서 대출상환으로 연결된 부채예요.”
          `font-size:12.5px line-height:1.45 color:#626D88`
      - `div`
        `display:flex align-items:center gap:8px`
        - `div` — “삭제”
          `display:inline-flex align-items:center gap:4px height:32px padding:0 11px border-radius:9px background:#FCEBEA border:none color:#C0342F font-size:12.5px font-weight:600`
        - `div`
          `width:36px height:36px border-radius:11px background:#F4F6FB display:flex align-items:center justify-content:center`
    - `div`
      `flex:1 min-height:0 padding:14px 18px 0 display:flex flex-direction:column gap:15px`
      - `div`
        `flex:1`
        - `div` — “부채 이름”
          `font-size:12px font-weight:600 color:#475467`
        - `div` **InputField**
          `display:flex align-items:center gap:5px height:46px padding:0 12px border-radius:11px border:1px solid #CFD7E6 background:#FFFFFF`
      - `div`
        `display:flex gap:10px`
        - `div`
          `flex:1`
        - `div`
          `width:142px`
      - `div`
        `display:flex gap:10px`
        - `div`
          `flex:1`
        - `div`
          `width:142px`
      - `div` **Callout(warn)**
        `display:flex gap:8px padding:10px 11px background:#FDF1E0 border-radius:12px`
        - `span`
          `margin-top:1px`
        - `span` **text 11.5px/400** — “연 14.5%는 보유한 부채 중 가장 높아요. 고금리 우선 전략에서 1순위로 상환됩니다.”
          `font-size:11.5px line-height:1.5 color:#7A3E0A`
      - `div` **Callout(info)**
        `display:flex gap:8px padding:10px 11px background:#F4F6FB border-radius:12px`
        - `span`
          `margin-top:1px`
        - `span` **text 11.5px/400** — “남은 원금을 0으로 두면 완납으로 기록되고 목록에는 남습니다. 삭제하면 연결된 거래의 부채 연결이 끊깁니다.”
          `font-size:11.5px line-height:1.5 color:#626D88`
    - `div`
      `display:flex gap:10px padding:12px 18px 20px border-top:1px solid #EFF2F8`
      - `div` **SecondaryButton(48)** — “취소”
        `display:flex align-items:center justify-content:center gap:6px height:48px flex:1 border-radius:13px background:#FFFFFF border:1px solid #D7DEEA color:#475467 font-size:15px font-weight:600`
      - `div` **PrimaryButton(48)** — “변경 저장”
        `display:flex align-items:center justify-content:center gap:6px height:48px flex:1.4 border-radius:13px background:#3556E6 border:none color:#FFFFFF font-size:15px font-weight:600`
