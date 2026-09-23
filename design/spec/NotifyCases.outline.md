# NotifyCases — 블록 개요

원본 `canvas/NotifyCases.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div`
  `width:1200px height:830px background:#EDF0F7 color:#101828 padding:28px 30px 30px display:flex flex-direction:column gap:10px`
  - `span` **text 11px/600** — “구현 참고 · 앱 화면이 아닙니다”
    `font-size:11px font-weight:600 letter-spacing:0.02em color:#475467 border:1px solid #E3E8F1 background:#FFFFFF border-radius:99px padding:4px 10px`
  - `h2` **text 20px/700** — “기기 알림 — 여섯 가지와 규칙”
    `font-size:20px font-weight:700 letter-spacing:-0.025em color:#101828`
  - `p` **text 13px/400** — “앱 안 알림 창과 별개로, 앱을 안 켜고 있을 때 시각으로 오는 안드로이드 로컬 알림입니다. 기본 켬 셋 · 설정에”
    `font-size:13px line-height:1.55 color:#626D88`
  - `div`
    `display:grid grid-template-columns:repeat(3, 362px) gap:26px 28px align-items:start`
    - `div`
      `display:flex flex-direction:column gap:8px width:362px`
      - `div`
        `display:flex align-items:center gap:7px`
        - `span` **text 10.5px/700** — “1”
          `width:17px height:17px border-radius:99px background:#101828 color:#FFFFFF font-size:10.5px font-weight:700 display:inline-flex align-items:center justify-content:center box-shadow:0 0 0 2px #FFFFFF`
        - `span` **text 14px/700** — “오늘 소비 기록 확인”
          `font-size:14px font-weight:700 color:#101828`
        - `span` **text 10.5px/700** — “기본 켬”
          `font-size:10.5px font-weight:700 padding:2px 7px border-radius:99px background:#E9EDFD color:#3556E6`
      - `div` **text 12px/400** — “매일 21:00 · 안 적은 날만”
        `font-size:12px color:#626D88 margin-top:-4px`
      - `div`
        `width:362px background:#FFFFFF border:1px solid #E3E8F1 border-radius:16px padding:12px 14px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
        - `div`
          `display:flex align-items:center gap:7px`
        - `div` **text 14px/700** — “오늘 소비 기록을 확인해 주세요”
          `font-size:14px font-weight:700 letter-spacing:-0.01em color:#101828 margin-top:7px`
        - `div` **text 12.5px/400** — “날짜를 눌러 숫자만 넣으면 돼요”
          `font-size:12.5px line-height:1.45 color:#475467 margin-top:2px`
      - `div` — “누르면 →”
        `font-size:12px color:#626D88`
        - `b` — “홈 · 오늘 하루 시트”
          `font-weight:600 color:#475467`
    - `div`
      `display:flex flex-direction:column gap:8px width:362px`
      - `div`
        `display:flex align-items:center gap:7px`
        - `span` **text 10.5px/700** — “2”
          `width:17px height:17px border-radius:99px background:#101828 color:#FFFFFF font-size:10.5px font-weight:700 display:inline-flex align-items:center justify-content:center box-shadow:0 0 0 2px #FFFFFF`
        - `span` **text 14px/700** — “지난달 마감”
          `font-size:14px font-weight:700 color:#101828`
        - `span` **text 10.5px/700** — “기본 켬”
          `font-size:10.5px font-weight:700 padding:2px 7px border-radius:99px background:#E9EDFD color:#3556E6`
      - `div` **text 12px/400** — “매월 1일 10:00 · 마감할 기록이 있을 때”
        `font-size:12px color:#626D88 margin-top:-4px`
      - `div`
        `width:362px background:#FFFFFF border:1px solid #E3E8F1 border-radius:16px padding:12px 14px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
        - `div`
          `display:flex align-items:center gap:7px`
        - `div` **text 14px/700** — “지난달 기록을 확인하고 마감해 주세요”
          `font-size:14px font-weight:700 letter-spacing:-0.01em color:#101828 margin-top:7px`
        - `div` **text 12.5px/400** — “마감한 달이 예상의 기준이 돼요”
          `font-size:12.5px line-height:1.45 color:#475467 margin-top:2px`
      - `div` — “누르면 →”
        `font-size:12px color:#626D88`
        - `b` — “소비 · 지난달 마감”
          `font-weight:600 color:#475467`
    - `div`
      `display:flex flex-direction:column gap:8px width:362px`
      - `div`
        `display:flex align-items:center gap:7px`
        - `span` **text 10.5px/700** — “3”
          `width:17px height:17px border-radius:99px background:#101828 color:#FFFFFF font-size:10.5px font-weight:700 display:inline-flex align-items:center justify-content:center box-shadow:0 0 0 2px #FFFFFF`
        - `span` **text 14px/700** — “자산 잔액 · 백업 확인”
          `font-size:14px font-weight:700 color:#101828`
        - `span` **text 10.5px/700** — “기본 켬”
          `font-size:10.5px font-weight:700 padding:2px 7px border-radius:99px background:#E9EDFD color:#3556E6`
      - `div` **text 12px/400** — “매월 1일 · 마감 알림과 한 건”
        `font-size:12px color:#626D88 margin-top:-4px`
      - `div`
        `width:362px background:#FFFFFF border:1px solid #E3E8F1 border-radius:16px padding:12px 14px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
        - `div`
          `display:flex align-items:center gap:7px`
        - `div` **text 14px/700** — “자산 잔액과 백업을 확인해 주세요”
          `font-size:14px font-weight:700 letter-spacing:-0.01em color:#101828 margin-top:7px`
        - `div` **text 12.5px/400** — “오래된 잔액은 순자산과 미래 예측에 영향을 줘요”
          `font-size:12.5px line-height:1.45 color:#475467 margin-top:2px`
      - `div` — “누르면 →”
        `font-size:12px color:#626D88`
        - `b` — “자산 · 구성”
          `font-weight:600 color:#475467`
    - `div`
      `display:flex flex-direction:column gap:8px width:362px`
      - `div`
        `display:flex align-items:center gap:7px`
        - `span` **text 10.5px/700** — “4”
          `width:17px height:17px border-radius:99px background:#101828 color:#FFFFFF font-size:10.5px font-weight:700 display:inline-flex align-items:center justify-content:center box-shadow:0 0 0 2px #FFFFFF`
        - `span` **text 14px/700** — “미마감 재안내”
          `font-size:14px font-weight:700 color:#101828`
        - `span` **text 10.5px/700** — “설정에서 켬”
          `font-size:10.5px font-weight:700 padding:2px 7px border-radius:99px background:#F4F6FB color:#626D88`
      - `div` **text 12px/400** — “매월 8일 10:00 · 아직 안 했을 때”
        `font-size:12px color:#626D88 margin-top:-4px`
      - `div`
        `width:362px background:#FFFFFF border:1px solid #E3E8F1 border-radius:16px padding:12px 14px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
        - `div`
          `display:flex align-items:center gap:7px`
        - `div` **text 14px/700** — “지난달이 아직 마감되지 않았어요”
          `font-size:14px font-weight:700 letter-spacing:-0.01em color:#101828 margin-top:7px`
        - `div` **text 12.5px/400** — “기록을 확인하고 마감해 주세요”
          `font-size:12.5px line-height:1.45 color:#475467 margin-top:2px`
      - `div` — “누르면 →”
        `font-size:12px color:#626D88`
        - `b` — “소비 · 지난달 마감”
          `font-weight:600 color:#475467`
    - `div`
      `display:flex flex-direction:column gap:8px width:362px`
      - `div`
        `display:flex align-items:center gap:7px`
        - `span` **text 10.5px/700** — “5”
          `width:17px height:17px border-radius:99px background:#101828 color:#FFFFFF font-size:10.5px font-weight:700 display:inline-flex align-items:center justify-content:center box-shadow:0 0 0 2px #FFFFFF`
        - `span` **text 14px/700** — “월 중간 점검”
          `font-size:14px font-weight:700 color:#101828`
        - `span` **text 10.5px/700** — “설정에서 켬”
          `font-size:10.5px font-weight:700 padding:2px 7px border-radius:99px background:#F4F6FB color:#626D88`
      - `div` **text 12px/400** — “매월 15일 10:00”
        `font-size:12px color:#626D88 margin-top:-4px`
      - `div`
        `width:362px background:#FFFFFF border:1px solid #E3E8F1 border-radius:16px padding:12px 14px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
        - `div`
          `display:flex align-items:center gap:7px`
        - `div` **text 14px/700** — “이번 달 소비와 남은 한도를 확인해 주세요”
          `font-size:14px font-weight:700 letter-spacing:-0.01em color:#101828 margin-top:7px`
        - `div` **text 12.5px/400** — “지금 속도로 월말까지 괜찮은지 봐요”
          `font-size:12.5px line-height:1.45 color:#475467 margin-top:2px`
      - `div` — “누르면 →”
        `font-size:12px color:#626D88`
        - `b` — “소비 · 이번 달”
          `font-weight:600 color:#475467`
    - `div`
      `display:flex flex-direction:column gap:8px width:362px`
      - `div`
        `display:flex align-items:center gap:7px`
        - `span` **text 10.5px/700** — “6”
          `width:17px height:17px border-radius:99px background:#101828 color:#FFFFFF font-size:10.5px font-weight:700 display:inline-flex align-items:center justify-content:center box-shadow:0 0 0 2px #FFFFFF`
        - `span` **text 14px/700** — “반복 거래 예정일 전날”
          `font-size:14px font-weight:700 color:#101828`
        - `span` **text 10.5px/700** — “설정에서 켬”
          `font-size:10.5px font-weight:700 padding:2px 7px border-radius:99px background:#F4F6FB color:#626D88`
      - `div` **text 12px/400** — “예정일 전날 09:00”
        `font-size:12px color:#626D88 margin-top:-4px`
      - `div`
        `width:362px background:#FFFFFF border:1px solid #E3E8F1 border-radius:16px padding:12px 14px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
        - `div`
          `display:flex align-items:center gap:7px`
        - `div` **text 14px/700** — “내일은 등록한 반복 거래 예정일이에요”
          `font-size:14px font-weight:700 letter-spacing:-0.01em color:#101828 margin-top:7px`
        - `div` **text 12.5px/400** — “휴대폰 요금 · 매월 25일”
          `font-size:12.5px line-height:1.45 color:#475467 margin-top:2px`
      - `div` — “누르면 →”
        `font-size:12px color:#626D88`
        - `b` — “소비 · 내역 · 반복 거래”
          `font-weight:600 color:#475467`
  - `div`
    `margin-top:22px padding:16px 18px background:#FFFFFF border:1px solid #E3E8F1 border-radius:16px`
    - `div` **text 13px/700** — “규칙”
      `font-size:13px font-weight:700 color:#101828`
    - `ol`
      `font-size:12.5px line-height:1.55 color:#475467`
      - `li` — “기기 알림은 뿐입니다. 한도 초과 · 목적지 도착 · 부채 완제 · 다시 마감 · 자동 기록처럼 저장 순간 생기는 ”
        - `b` — “앱을 안 켜고 있을 때 시각으로 오는 것”
          `font-weight:600`
      - `li` — “문구에 금액 · 목표 이름을 넣지 않습니다 — 예약 시점 값이라 틀릴 수 있고, 알림 내용은 앱의 암호화 저장 밖에”
      - `li` — “같은 종류는 하루 1번. 기록 알림은 이틀째부터 「어제 것도 같이 적을 수 있어요」, 일주일째부터는 주 1회로 줄입”
      - `li` — “누르면 그 화면 · 그 날짜로 갑니다. 알림으로 들어온 동안은 첫 실행 안내를 띄우지 않되, 본 것으로 저장하지는 ”
      - `li` — “권한(안드로이드 13+)은 홈 안내가 끝난 뒤 개인 데이터일 때, 설명 카드에서 「켜기」를 누를 때 묻습니다. 샘플”
      - `li` — “앱이 열릴 때마다 앞으로 35일치를 다시 예약하고 지난 예약은 지웁니다. 35일 넘게 안 열면 알림이 멈추고, 재부”
