# DebtUnpayable — 블록 개요

원본 `canvas/DebtUnpayable.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div`
  `width:1230px height:936px background:#EDF0F7 color:#101828 padding:28px 30px 30px display:flex flex-direction:column gap:10px`
  - `span` **text 11px/600** — “구현 참고 · 앱 화면이 아닙니다”
    `font-size:11px font-weight:600 letter-spacing:0.02em color:#475467 border:1px solid #E3E8F1 background:#FFFFFF border-radius:99px padding:4px 10px`
  - `h2` **text 20px/700** — “월 최소 상환액을 비워 둔 부채 — 다 갚지 못할 때”
    `font-size:20px font-weight:700 letter-spacing:-0.025em color:#101828`
  - `p` — “예: 전세자금대출 1억 · 연 있고 월 최소 상환액을 추가 20만원). 계산할 수 없는 값은 0원이 아니라 —입니다”
    `font-size:13px line-height:1.55 color:#626D88`
    - `span` — “3.6%만”
      `white-space:nowrap`
    - `span` — “비웠습니다(월”
      `white-space:nowrap`
  - `div`
    `display:flex gap:24px align-items:flex-start`
    - `div`
      `width:362px display:flex flex-direction:column gap:22px`
      - `div`
        `display:flex flex-direction:column gap:8px`
        - `div`
        - `div`
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:22px padding:16px display:flex flex-direction:column gap:12px`
    - `div`
      `width:362px display:flex flex-direction:column gap:22px`
      - `div`
        `display:flex flex-direction:column gap:8px`
        - `div`
        - `div` **Card(18)**
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
      - `div`
        `display:flex flex-direction:column gap:8px`
        - `div`
        - `div` **Card(18)**
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:10px 14px display:flex justify-content:space-between align-items:center gap:8px`
    - `div`
      `width:362px display:flex flex-direction:column gap:22px`
      - `div`
        `display:flex flex-direction:column gap:8px`
        - `div`
        - `div`
          `display:flex flex-direction:column gap:10px`
  - `div` **Card(18)**
    `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:10px 18px 8px`
    - `div` **text 12px/700** — “구현 메모”
      `font-size:12px font-weight:700 color:#101828 padding:2px 0 4px`
    - `div`
      `display:flex gap:10px padding:7px 0 border-bottom:1px solid #F3F5FA`
      - `span` **text 10.5px/700** — “1”
        `margin-top:1px width:17px height:17px border-radius:99px background:#101828 color:#FFFFFF font-size:10.5px font-weight:700 display:inline-flex align-items:center justify-content:center box-shadow:0 0 0 2px #FFFFFF`
      - `div` — “새 부채의 연 금리는 빈칸에서 글자 ‘ ’) 필수입니다. 월 최소 상환액이 비면 두 단계 — 주황 안내가 뜨고 버튼”
        `font-size:12px line-height:1.55 color:#475467`
        - `span` — “시작하고(자리”
          `white-space:nowrap`
        - `b` — “예: 6.5”
          `font-weight:600 color:#101828`
        - `b` — “그대로 저장”
          `font-weight:600 color:#101828`
    - `div`
      `display:flex gap:10px padding:7px 0 border-bottom:1px solid #F3F5FA`
      - `span` **text 10.5px/700** — “2”
        `margin-top:1px width:17px height:17px border-radius:99px background:#101828 color:#FFFFFF font-size:10.5px font-weight:700 display:inline-flex align-items:center justify-content:center box-shadow:0 0 0 2px #FFFFFF`
      - `div` — “저장한 뒤 부채 화면은 ‘ ’ + ‘ ’, 이번 달 상환 예정 ‘ ’ + ‘ ’. 0원이나 좋은 결과로 보이지 않습”
        `font-size:12px line-height:1.55 color:#475467`
        - `b` — “월 최소 상환 —”
          `font-weight:600 color:#101828`
        - `b` — “입력 필요”
          `font-weight:600 color:#101828`
        - `b` — “—”
          `font-weight:600 color:#101828`
        - `b` — “상환액 넣기 ›”
          `font-weight:600 color:#101828`
    - `div`
      `display:flex gap:10px padding:7px 0`
      - `span` **text 10.5px/700** — “3”
        `margin-top:1px width:17px height:17px border-radius:99px background:#101828 color:#FFFFFF font-size:10.5px font-weight:700 display:inline-flex align-items:center justify-content:center box-shadow:0 0 0 2px #FFFFFF`
      - `div` — “자산 › 상환 전용 요약)은 ‘ ’ · 총이자 ‘ ’ · 까닭 한 줄. 미래 › 상환 계획의 같은 경우는 Payof”
        `font-size:12px line-height:1.55 color:#475467`
        - `span` — “계획(읽기”
          `white-space:nowrap`
        - `b` — “다 갚지 못해요”
          `font-weight:600 color:#101828`
        - `b` — “—”
          `font-weight:600 color:#101828`
