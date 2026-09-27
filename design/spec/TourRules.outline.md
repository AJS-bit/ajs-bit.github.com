# TourRules — 블록 개요

원본 `canvas/TourRules.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div`
  `width:1200px height:1760px background:#EDF0F7 color:#101828 padding:28px 30px 30px display:flex flex-direction:column gap:10px`
  - `span` **text 11px/600** — “구현 참고 · 앱 화면이 아닙니다”
    `font-size:11px font-weight:600 letter-spacing:0.02em color:#475467 border:1px solid #E3E8F1 background:#FFFFFF border-radius:99px padding:4px 10px white-space:nowrap`
  - `h2` **text 20px/700** — “첫 실행 안내 — 규칙”
    `font-size:20px font-weight:700 letter-spacing:-0.025em color:#101828`
  - `p` — “앱 a724aac 의 lib/ · lib/ · components/navi/ 그대로. 화면마다의 안내 이 규칙을 시”
    `font-size:13px line-height:1.55 color:#626D88`
    - `span` — “v5-stage1”
      `white-space:nowrap`
    - `span` — “navi-tour.ts”
      `white-space:nowrap`
    - `span` — “navi-tour-policy.ts”
      `white-space:nowrap`
    - `span` — “first-run-tour.tsx”
      `white-space:nowrap`
    - `span` — “장(33장)은”
      `white-space:nowrap`
    - `span` — “사용자(9월”
      `white-space:nowrap`
  - `div`
    `display:flex gap:32px align-items:flex-start`
    - `div`
      `width:362px display:flex flex-direction:column gap:10px`
      - `div`
        - `div` **text 13.5px/700** — “처음 안내 · 홈 3 / 3”
          `font-size:13.5px font-weight:700 color:#101828`
        - `div` **text 12px/400** — “저절로 뜬 안내. 홈 마지막 단계만 각주 한 줄이 붙는다.”
          `font-size:12px line-height:1.5 color:#626D88 margin-top:2px`
      - `div` **Card(18)**
        `position:relative width:362px background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:16px box-shadow:0 12px 32px -12px rgba(16,24,40,.45) font-size:13px line-height:1.55 color:#101828`
        - `div`
          `display:flex align-items:center justify-content:space-between gap:8px flex-wrap:wrap font-size:11.5px font-weight:600 color:#626D88`
        - `div` **text 16px/700** — “지금 할 일 한 가지”
          `margin-top:8px font-size:16px font-weight:700 letter-spacing:-0.02em line-height:1.35 color:#101828`
        - `div` **text 13px/400** — “기록이 쌓이면 가장 효과가 큰 일 하나를 골라 알려 줘요. 누르면 그 화면으로 바로 가요.”
          `margin-top:8px font-size:13px line-height:1.55 color:#475467`
        - `div` — “다른 화면도 처음 들어갈 때 짧은 안내가 떠요. 필요 없으면 누르세요.”
          `margin-top:6px font-size:12.5px line-height:1.5 color:#626D88`
        - `div`
          `display:flex align-items:center justify-content:space-between flex-wrap:wrap gap:4px 8px margin-top:14px`
      - `div`
        `height:6px`
      - `div`
        - `div` **text 13.5px/700** — “화면 안내 · 제목 옆 ?로 다시 연 안내”
          `font-size:13.5px font-weight:700 color:#101828`
        - `div` — “단계 · 문구 · 버튼은 같고 알약만”
          `font-size:12px line-height:1.5 color:#626D88 margin-top:2px`
      - `div` **Card(18)**
        `position:relative width:362px background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:16px box-shadow:0 12px 32px -12px rgba(16,24,40,.45) font-size:13px line-height:1.55 color:#101828`
        - `div`
          `display:flex align-items:center justify-content:space-between gap:8px flex-wrap:wrap font-size:11.5px font-weight:600 color:#626D88`
        - `div` **text 16px/700** — “가진 것과 갚을 것”
          `margin-top:8px font-size:16px font-weight:700 letter-spacing:-0.02em line-height:1.35 color:#101828`
        - `div` **text 13px/400** — “자산 구성 · 부채 · 상환 계획 세 탭이에요. 부채가 있으면 상환 계획에서 언제 다 갚는지 봐요.”
          `margin-top:8px font-size:13px line-height:1.55 color:#475467`
        - `div`
          `display:flex align-items:center justify-content:space-between flex-wrap:wrap gap:4px 8px margin-top:14px`
      - `div`
        `height:6px`
      - `div`
        - `div` **text 13.5px/700** — “다크”
          `font-size:13.5px font-weight:700 color:#101828`
        - `div` **text 12px/400** — “카드 · 꼬리 #1E2739 · 선 #39455F · 막 rgba(4,7,14,.74).”
          `font-size:12px line-height:1.5 color:#626D88 margin-top:2px`
      - `div`
        `background:#080C16 border-radius:18px padding:16px`
        - `div`
          `position:relative width:330px background:#1E2739 border:1px solid #39455F border-radius:18px padding:16px box-shadow:0 12px 32px -12px rgba(0,0,0,.6) font-size:13px line-height:1.55 color:#EAEFF8`
      - `div`
        `height:6px`
      - `div`
        - `div` **text 13.5px/700** — “빈 화면 — 안내도 ?도 없음”
          `font-size:13.5px font-weight:700 color:#101828`
        - `div` **text 12px/400** — “빈 카드 한 장 + 버튼 하나. 본 것으로 기록하지 않아 내용이 생긴 뒤 처음 들어갈 때 안내가 뜬다.”
          `font-size:12px line-height:1.5 color:#626D88 margin-top:2px`
      - `div` **Card(18)**
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:22px 16px text-align:center`
        - `div`
          `width:48px height:48px border-radius:14px background:#E9EDFD display:flex align-items:center justify-content:center`
        - `div` **text 17px/700** — “등록된 자산이 없어요”
          `font-size:17px font-weight:700 letter-spacing:-0.02em color:#101828 margin-top:12px`
        - `div` **text 13.5px/400** — “첫 자산을 추가하면 순자산이 보여요.”
          `font-size:13.5px color:#626D88 margin-top:6px`
        - `div` **PrimaryButton(44)** — “자산 추가”
          `display:inline-flex gap:6px margin-top:16px height:44px padding:0 20px border-radius:13px background:#3556E6 color:#FFFFFF font-size:14px font-weight:600 align-items:center`
    - `div`
      `flex:1 display:flex flex-direction:column gap:22px`
      - `div`
        `display:flex flex-direction:column gap:8px`
        - `div` **text 14px/700** — “언제 뜨나 — 11화면 모두 처음 들어갈 때 저절로”
          `font-size:14px font-weight:700 letter-spacing:-0.01em color:#101828`
        - `ul`
          `font-size:12.5px line-height:1.55 color:#475467`
        - `div`
          `display:grid grid-template-columns:150px 1fr 170px background:#FFFFFF border:1px solid #E3E8F1 border-radius:14px`
      - `div`
        `display:flex flex-direction:column gap:8px`
        - `div` — “닫는 방법 — 버튼 줄 = 왼쪽 · + 오른쪽”
          `font-size:14px font-weight:700 letter-spacing:-0.01em color:#101828`
        - `div`
          `display:grid grid-template-columns:190px 1fr background:#FFFFFF border:1px solid #E3E8F1 border-radius:14px`
        - `ul`
          `font-size:12.5px line-height:1.55 color:#475467`
      - `div`
        `display:flex flex-direction:column gap:8px`
        - `div` **text 14px/700** — “다시 보기”
          `font-size:14px font-weight:700 letter-spacing:-0.01em color:#101828`
        - `ul`
          `font-size:12.5px line-height:1.55 color:#475467`
      - `div`
        `display:flex flex-direction:column gap:8px`
        - `div` **text 14px/700** — “단계 수 — 대상이 있는 단계만 센다”
          `font-size:14px font-weight:700 letter-spacing:-0.01em color:#101828`
        - `ul`
          `font-size:12.5px line-height:1.55 color:#475467`
      - `div`
        `display:flex flex-direction:column gap:8px`
        - `div` — “배치 — 앱 placeTourCard 저장하지 않고 그 자리에서 잰다)”
          `font-size:14px font-weight:700 letter-spacing:-0.01em color:#101828`
        - `ul`
          `font-size:12.5px line-height:1.55 color:#475467`
      - `div`
        `display:flex flex-direction:column gap:8px`
        - `div` **text 14px/700** — “색 · 저장”
          `font-size:14px font-weight:700 letter-spacing:-0.01em color:#101828`
        - `ul`
          `font-size:12.5px line-height:1.55 color:#475467`
