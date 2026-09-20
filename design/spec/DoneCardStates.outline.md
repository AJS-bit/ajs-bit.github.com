# DoneCardStates — 블록 개요

원본 `canvas/DoneCardStates.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div`
  `width:1200px height:1090px background:#EDF0F7 color:#101828 padding:28px 30px 30px display:flex flex-direction:column gap:10px`
  - `span` **text 11px/600** — “구현 참고 · 앱 화면이 아닙니다”
    `font-size:11px font-weight:600 letter-spacing:0.02em color:#475467 border:1px solid #E3E8F1 background:#FFFFFF border-radius:99px padding:4px 10px`
  - `h2` **text 20px/700** — “저장 완료 카드의 경우들”
    `font-size:20px font-weight:700 letter-spacing:-0.025em color:#101828`
  - `p` **text 13px/400** — “저장이 끝나면 홈 아래쪽에 뜨는 카드 하나가 제목 · 셋째 줄 · 행동만 바꿔 가며 모든 경우를 맡습니다.”
    `font-size:13px line-height:1.55 color:#626D88`
  - `div`
    `display:flex gap:32px align-items:flex-start`
    - `div`
      `width:362px display:flex flex-direction:column gap:12px`
      - `div`
        `position:relative`
        - `div`
          `background:#101828 border-radius:16px padding:13px 14px 12px color:#FFFFFF box-shadow:0 8px 24px rgba(0,0,0,.28)`
        - `span` **text 10.5px/700** — “1”
          `position:absolute left:-8px top:14px width:17px height:17px border-radius:99px background:#101828 color:#FFFFFF font-size:10.5px font-weight:700 display:inline-flex align-items:center justify-content:center box-shadow:0 0 0 2px #FFFFFF`
        - `span` **text 10.5px/700** — “2”
          `position:absolute left:-8px top:63px width:17px height:17px border-radius:99px background:#101828 color:#FFFFFF font-size:10.5px font-weight:700 display:inline-flex align-items:center justify-content:center box-shadow:0 0 0 2px #FFFFFF`
        - `span` **text 10.5px/700** — “3”
          `position:absolute left:-8px top:102px width:17px height:17px border-radius:99px background:#101828 color:#FFFFFF font-size:10.5px font-weight:700 display:inline-flex align-items:center justify-content:center box-shadow:0 0 0 2px #FFFFFF`
      - `p` — “제목 · 셋째 줄 · 행동 두 칸(주 행동 + 취소). 둘째 줄은 언제나 날짜 · 정확한 금액 · 그날 합계입니다.”
        `font-size:12px line-height:1.6 color:#626D88`
        - `b` — “1”
          `font-weight:600 color:#475467`
        - `b` — “2”
          `font-weight:600 color:#475467`
        - `b` — “3”
          `font-weight:600 color:#475467`
      - `div` **Card(18)**
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 16px 4px`
        - `div`
          `display:flex align-items:center gap:7px`
        - `div`
          `display:flex flex-direction:column gap:5px padding:9px 0 border-bottom:1px solid #F3F5FA`
        - `div`
          `display:flex flex-direction:column gap:5px padding:9px 0 border-bottom:1px solid #F3F5FA`
        - `div`
          `display:flex flex-direction:column gap:5px padding:9px 0 border-bottom:1px solid #F3F5FA`
        - `div`
          `display:flex flex-direction:column gap:5px padding:9px 0 border-bottom:1px solid #F3F5FA`
        - `div`
          `display:flex flex-direction:column gap:5px padding:9px 0 border-bottom:1px solid #F3F5FA`
        - `div`
          `display:flex flex-direction:column gap:5px padding:9px 0`
    - `div`
      `flex:1 display:flex flex-direction:column gap:22px`
      - `div`
        `flex:1 display:grid grid-template-columns:repeat(2, 362px) gap:24px 20px align-items:start`
        - `div`
          `display:flex flex-direction:column gap:8px`
        - `div`
          `display:flex flex-direction:column gap:8px`
        - `div`
          `display:flex flex-direction:column gap:8px`
        - `div`
          `display:flex flex-direction:column gap:8px`
        - `div`
          `display:flex flex-direction:column gap:8px`
        - `div`
          `display:flex flex-direction:column gap:8px`
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
