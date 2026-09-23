# SettingsNotify — 블록 개요

원본 `canvas/SettingsNotify.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div` **화면프레임**
  `width:390px height:844px background:#2A3245 color:#101828 display:flex flex-direction:column`
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
      `display:flex align-items:flex-start justify-content:space-between gap:10px padding:12px 18px 14px border-bottom:1px solid #EFF2F8`
      - `div`
        - `h2` **text 18px/700** — “알림”
          `font-size:18px font-weight:700 letter-spacing:-0.025em color:#101828`
        - `p` **text 12.5px/400** — “앱 안의 알림 창(종)과는 별개예요. 앱을 안 켜고 있을 때만 기기로 알려 드려요.”
          `font-size:12.5px line-height:1.45 color:#626D88`
      - `div`
        `display:flex align-items:center gap:8px`
        - `span` **text 12px/600** — “기기 알림”
          `font-size:12px font-weight:600 color:#475467`
        - `div`
          `width:46px height:27px border-radius:99px background:#3556E6 padding:3px display:flex justify-content:flex-end`
    - `div`
      `flex:1 min-height:0 padding:14px 18px 14px display:flex flex-direction:column gap:15px`
      - `div`
        `margin-top:0px`
        - `div` **text 11px/600** — “조용한 시간”
          `font-size:11px font-weight:600 letter-spacing:0.07em color:#626D88`
        - `div`
          `background:#F4F6FB border-radius:14px padding:0 13px`
      - `div`
        `margin-top:8px`
        - `div` **text 11px/600** — “알림”
          `font-size:11px font-weight:600 letter-spacing:0.07em color:#626D88`
        - `div`
          `background:#F4F6FB border-radius:14px padding:0 13px`
      - `div`
        `margin-top:8px`
        - `div` **text 11px/600** — “확인”
          `font-size:11px font-weight:600 letter-spacing:0.07em color:#626D88`
        - `div`
          `background:#F4F6FB border-radius:14px padding:0 13px`
      - `div`
        `margin-top:8px`
        - `div` **Callout(info)**
          `display:flex gap:8px padding:10px 11px background:#F4F6FB border-radius:12px`
    - `div`
      `display:flex gap:10px padding:12px 18px 20px border-top:1px solid #EFF2F8`
      - `div` **SecondaryButton(48)** — “닫기”
        `display:flex align-items:center justify-content:center gap:6px height:48px flex:1 border-radius:13px background:#FFFFFF border:1px solid #D7DEEA color:#475467 font-size:15px font-weight:600`
      - `div` **PrimaryButton(48)** — “저장”
        `display:flex align-items:center justify-content:center gap:6px height:48px flex:1.4 border-radius:13px background:#3556E6 border:none color:#FFFFFF font-size:15px font-weight:600`
