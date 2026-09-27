# PayoffStates — 블록 개요

원본 `canvas/PayoffStates.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div`
  `width:1230px height:1501px background:#EDF0F7 color:#101828 padding:28px 30px 30px display:flex flex-direction:column gap:10px`
  - `span` **text 11px/600** — “구현 참고 · 앱 화면이 아닙니다”
    `font-size:11px font-weight:600 letter-spacing:0.02em color:#475467 border:1px solid #E3E8F1 background:#FFFFFF border-radius:99px padding:4px 10px`
  - `h2` **text 20px/700** — “미래 › 상환 계획 — 초안 · 다 갚지 못함 · 최소 상환만 · 모자람”
    `font-size:20px font-weight:700 letter-spacing:-0.025em color:#101828`
  - `p` — “저장된 장)에서 슬라이더나 방식을 바꾸면 초안이 됩니다. 숫자는 시안 사용자의 저장된 우선 · 월 추가 15만원)에”
    `font-size:13px line-height:1.55 color:#626D88`
    - `span` — “계획(Payoff”
      `white-space:nowrap`
    - `span` — “계획(고금리”
      `white-space:nowrap`
  - `div`
    `display:flex gap:24px align-items:flex-start`
    - `div`
      `width:362px display:flex flex-direction:column gap:22px`
      - `div`
        `display:flex flex-direction:column gap:8px`
        - `div`
        - `div`
          `display:flex flex-direction:column gap:10px`
    - `div`
      `width:362px display:flex flex-direction:column gap:22px`
      - `div`
        `display:flex flex-direction:column gap:8px`
        - `div`
        - `div`
          `display:flex flex-direction:column gap:10px`
      - `div`
        `display:flex flex-direction:column gap:8px`
        - `div`
        - `div` **Card(18)**
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
    - `div`
      `width:362px display:flex flex-direction:column gap:22px`
      - `div`
        `display:flex flex-direction:column gap:8px`
        - `div`
        - `div` **Card(18)**
          `background:#FFFFFF border:1.5px dashed #B79BFF border-radius:18px padding:14px`
      - `div`
        `display:flex flex-direction:column gap:8px`
        - `div`
        - `div` **Card(18)**
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:6px 14px`
      - `div`
        `display:flex flex-direction:column gap:8px`
        - `div`
        - `div` **Card(18)**
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 14px`
  - `div` **Card(18)**
    `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:10px 18px 8px`
    - `div` **text 12px/700** — “구현 메모”
      `font-size:12px font-weight:700 color:#101828 padding:2px 0 4px`
    - `div`
      `display:flex gap:10px padding:7px 0 border-bottom:1px solid #F3F5FA`
      - `span` **text 10.5px/700** — “1”
        `margin-top:1px width:17px height:17px border-radius:99px background:#101828 color:#FFFFFF font-size:10.5px font-weight:700 display:inline-flex align-items:center justify-content:center box-shadow:0 0 0 2px #FFFFFF`
      - `div` — “초안 — 슬라이더나 방식을 저장된 계획과 다르게 바꾼 동안만 보라 점선 + ‘ ’. 예전 값은 회색 작게 · 새 값”
        `font-size:12px line-height:1.55 color:#475467`
        - `b` — “저장되지 않는 가정”
          `font-weight:600 color:#101828`
        - `b` — “되돌리기”
          `font-weight:600 color:#101828`
        - `b` — “가정 종료”
          `font-weight:600 color:#101828`
        - `b` — “상환 계획 저장”
          `font-weight:600 color:#101828`
    - `div`
      `display:flex gap:10px padding:7px 0 border-bottom:1px solid #F3F5FA`
      - `span` **text 10.5px/700** — “2”
        `margin-top:1px width:17px height:17px border-radius:99px background:#101828 color:#FFFFFF font-size:10.5px font-weight:700 display:inline-flex align-items:center justify-content:center box-shadow:0 0 0 2px #FFFFFF`
      - `div` — “다 갚지 못할 최소 상환액을 넣지 않은 부채) — 다 갚는 달 ‘ ’ · 총이자 ‘ ’ · ‘ ’ 없음 · 이자)과”
        `font-size:12px line-height:1.55 color:#475467`
        - `span` — “때(월”
          `white-space:nowrap`
        - `b` — “다 갚지 못해요”
          `font-weight:600 color:#101828`
        - `b` — “—”
          `font-weight:600 color:#101828`
        - `b` — “추천”
          `font-weight:600 color:#101828`
        - `span` — “까닭(매달”
          `white-space:nowrap`
        - `b` — “부채 수정 ›”
          `font-weight:600 color:#101828`
    - `div`
      `display:flex gap:10px padding:7px 0 border-bottom:1px solid #F3F5FA`
      - `span` **text 10.5px/700** — “3”
        `margin-top:1px width:17px height:17px border-radius:99px background:#101828 color:#FFFFFF font-size:10.5px font-weight:700 display:inline-flex align-items:center justify-content:center box-shadow:0 0 0 2px #FFFFFF`
      - `div` — “예전 버전의 ‘ ’을 고른 사람 — 셋째 카드로 골라 두고 ‘ ’. 기준선이 아니라 저장된 방식입니다.”
        `font-size:12px line-height:1.55 color:#475467`
        - `b` — “최소 상환만”
          `font-weight:600 color:#101828`
        - `b` — “예전 버전에서 고른 설정이에요 …”
          `font-weight:600 color:#101828`
    - `div`
      `display:flex gap:10px padding:7px 0 border-bottom:1px solid #F3F5FA`
      - `span` **text 10.5px/700** — “4”
        `margin-top:1px width:17px height:17px border-radius:99px background:#101828 color:#FFFFFF font-size:10.5px font-weight:700 display:inline-flex align-items:center justify-content:center box-shadow:0 0 0 2px #FFFFFF`
      - `div` — “매달 남는 돈이 모자라면 슬라이더 위에 주황 한 줄. 참고 줄은 늘 회색이고 판정이 아닙니다 — 목적지 필요액이 가”
        `font-size:12px line-height:1.55 color:#475467`
        - `span` — “70%로”
          `white-space:nowrap`
    - `div`
      `display:flex gap:10px padding:7px 0`
      - `span` **text 10.5px/700** — “5”
        `margin-top:1px width:17px height:17px border-radius:99px background:#101828 color:#FFFFFF font-size:10.5px font-weight:700 display:inline-flex align-items:center justify-content:center box-shadow:0 0 0 2px #FFFFFF`
      - `div` — “두 방식의 다 갚는 달이 같고 이자 차이가 1만원 안이면 ‘ ’ 없이 순서를 샘플 부채 예). 저장된 계획은 파란 ”
        `font-size:12px line-height:1.55 color:#475467`
        - `b` — “추천”
          `font-weight:600 color:#101828`
        - `span` — “말합니다(앱”
          `white-space:nowrap`
        - `b` — “저장된 계획”
          `font-weight:600 color:#101828`
        - `span` — “배지(보라”
          `white-space:nowrap`
