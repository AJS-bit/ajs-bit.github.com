# ImportBackupNotes — 블록 개요

원본 `canvas/ImportBackupNotes.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div`
  `width:1230px height:1060px background:#EDF0F7 color:#101828 padding:28px 30px 30px display:flex flex-direction:column gap:10px`
  - `span` **text 11px/600** — “구현 참고 · 앱 화면이 아닙니다”
    `font-size:11px font-weight:600 letter-spacing:0.02em color:#475467 border:1px solid #E3E8F1 background:#FFFFFF border-radius:99px padding:4px 10px`
  - `h2` **text 20px/700** — “가져오기 · 백업 — 확인 표시와 분류 안 함 표시가 어떻게 따라오는지”
    `font-size:20px font-weight:700 letter-spacing:-0.025em color:#101828`
  - `p` **text 13px/400** — “달력의 확인 표시(다 적었어요 · 안 썼어요)와 분류 안 함 표시는 백업 파일에 함께 들어갑니다. 전체 복원과 골라”
    `font-size:13px line-height:1.55 color:#626D88`
  - `div`
    `display:flex gap:32px align-items:flex-start`
    - `div`
      `width:390px border-radius:24px`
      - `div` **화면프레임**
        `width:390px height:844px background:#2A3245 color:#101828 display:flex flex-direction:column`
        - `div`
          `height:40px display:flex align-items:flex-end justify-content:center`
        - `div` **BottomSheet**
          `flex:1 min-height:0 background:#FFFFFF border-radius:26px 26px 0 0 display:flex flex-direction:column color:#101828`
    - `div`
      `flex:1 display:flex flex-direction:column gap:22px`
      - `div`
        `display:grid grid-template-columns:repeat(2, 362px) gap:22px 20px align-items:start`
        - `div`
          `display:flex flex-direction:column gap:8px`
        - `div`
          `display:flex flex-direction:column gap:8px`
      - `div`
        `display:flex flex-direction:column gap:8px`
        - `div` **text 14px/700** — “경로마다 돌아오는 것”
          `font-size:14px font-weight:700 letter-spacing:-0.01em color:#101828`
        - `div` **Card(18)**
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:10px 18px 6px`
      - `div` **Card(18)**
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:10px 18px 8px`
        - `div` **text 12px/700** — “구현 메모”
          `font-size:12px font-weight:700 color:#101828 padding:2px 0 4px`
        - `div`
          `display:flex gap:10px padding:7px 0 border-bottom:1px solid #F3F5FA`
        - `div`
          `display:flex gap:10px padding:7px 0 border-bottom:1px solid #F3F5FA`
        - `div`
          `display:flex gap:10px padding:7px 0`
