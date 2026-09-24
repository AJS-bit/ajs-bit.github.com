# EmptyStates — 블록 개요

원본 `canvas/EmptyStates.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div`
  `width:390px height:2800px background:#EDF0F7 color:#101828 padding:18px 14px 20px display:flex flex-direction:column gap:8px`
  - `div`
    `padding:0 2px 6px`
    - `span` **text 11px/600** — “구현 참고 · 앱 화면이 아닙니다”
      `display:inline-block font-size:11px font-weight:600 letter-spacing:0.02em color:#475467 border:1px solid #E3E8F1 background:#FFFFFF border-radius:99px padding:4px 10px white-space:nowrap`
    - `h2` **text 18px/700** — “미입력 · 빈 상태”
      `font-size:18px font-weight:700 letter-spacing:-0.025em color:#101828`
    - `p` **text 12px/400** — “아직 입력하지 않은 값이 있을 때 화면이 어떻게 보이는지 여섯 가지 경우입니다. 실제로는 한 번에 하나만 보입니다.”
      `font-size:12px line-height:1.45 color:#626D88`
  - `div` **text 11px/600** — “A · 첫 시작 · 홈”
    `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
  - `div` **Card(20)**
    `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px`
    - `div`
      `display:flex align-items:center gap:9px`
      - `div`
        `width:32px height:32px border-radius:10px background:linear-gradient(140deg, #3556E6 0%, #7A3FE4 100%) display:flex align-items:center justify-content:center`
      - `div`
        - `div` **text 11px/600** — “출발 준비”
          `font-size:11px font-weight:600 letter-spacing:0.06em color:#626D88`
        - `div` **text 16px/700** — “실수령 급여 하나면 시작돼요”
          `font-size:16px font-weight:700 letter-spacing:-0.02em color:#101828`
    - `p` **text 12.5px/400** — “자산을 입력하지 않아도 급여와 소비 기록만으로 소비율·한도·목적지를 계산합니다. 자산 분석은 나중에 채워도 괜찮아요”
      `font-size:12.5px line-height:1.5 color:#475467`
    - `div`
      `display:flex flex-direction:column margin-top:13px`
      - `div`
        `display:flex align-items:center gap:10px height:50px border-top:1px solid #EFF2F8`
        - `span` **text 11.5px/700** — “1”
          `width:22px height:22px border-radius:99px background:#3556E6 color:#FFFFFF font-size:11.5px font-weight:700 display:flex align-items:center justify-content:center`
        - `span` **text 13.5px/600** — “월 실수령 급여 입력”
          `flex:1 font-size:13.5px font-weight:600 color:#101828`
        - `div` **text 13px/600** — “입력하기”
          `height:34px padding:0 14px border-radius:10px background:#3556E6 color:#FFFFFF font-size:13px font-weight:600 display:flex align-items:center`
      - `div`
        `display:flex align-items:center gap:10px height:50px border-top:1px solid #EFF2F8`
        - `span` **text 11.5px/700** — “2”
          `width:22px height:22px border-radius:99px background:#E8ECF5 color:#606B7D font-size:11.5px font-weight:700 display:flex align-items:center justify-content:center`
        - `span` **text 13.5px/500** — “이번 달 소비 기록”
          `flex:1 font-size:13.5px font-weight:500 color:#606B7D`
        - `span` **text 12px/400** — “급여 입력 후”
          `font-size:12px color:#697182`
      - `div`
        `display:flex align-items:center gap:10px height:50px border-top:1px solid #EFF2F8`
        - `span` **text 11.5px/700** — “3”
          `width:22px height:22px border-radius:99px background:#E8ECF5 color:#606B7D font-size:11.5px font-weight:700 display:flex align-items:center justify-content:center`
        - `span` — “목적지 추가”
          `flex:1 font-size:13.5px font-weight:500 color:#606B7D`
        - `span` **text 12px/400** — “언제든지”
          `font-size:12px color:#697182`
  - `div` **text 11px/600** — “B · 급여 미입력 · 소비 기록만 있음 · 예상 기준 확인 전”
    `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
  - `div` **Card(20)**
    `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px`
    - `div`
      `display:flex align-items:center justify-content:space-between gap:8px`
      - `span` **text 11px/600** — “현재 위치”
        `font-size:11px font-weight:600 letter-spacing:0.07em color:#626D88`
    - `div`
      `display:flex align-items:flex-end justify-content:space-between gap:10px margin-top:8px`
      - `div`
        `display:flex align-items:baseline gap:2px`
        - `span` **text 54px/700** — “1,120,000”
          `font-size:54px font-weight:700 letter-spacing:-0.045em line-height:1 color:#101828`
        - `span` **text 25px/600** — “원”
          `font-size:25px font-weight:600 letter-spacing:-0.02em color:#475467`
    - `div`
      `display:flex align-items:baseline justify-content:space-between gap:10px margin-top:5px`
      - `span` **text 13px/500** — “월급을 넣으면 월급의 몇 %를 썼는지 보여요”
        `font-size:13px font-weight:500 color:#475467`
    - `div` **text 12px/400** — “아직 기록하지 않은 소비는 포함되지 않았어요”
      `font-size:12px line-height:1.45 color:#626D88 margin-top:3px`
    - `div` **text 12px/400** — “월말 예상에 쓸 지난 소비 기록이 아직 없어요”
      `font-size:12px line-height:1.45 color:#626D88 margin-top:3px`
    - `div`
      `margin-top:15px`
      - `div` **ProgressTrack**
        `position:relative height:10px border-radius:99px background:#E8ECF5`
        - `div`
          `position:absolute left:60% top:-5px width:2px height:20px border-radius:2px background:#101828`
      - `div`
        `position:relative height:15px margin-top:5px`
        - `span` **text 11px/400** — “0%”
          `position:absolute left:0 font-size:11px color:#626D88`
        - `span` **text 11px/600** — “내 목표 60%”
          `position:absolute left:60% transform:translateX(-50%) font-size:11px font-weight:600 color:#101828 white-space:nowrap`
        - `span` **text 11px/400** — “100%”
          `position:absolute right:0 font-size:11px color:#626D88`
    - `div`
      `display:grid grid-template-columns:repeat(3, minmax(0, 1fr)) gap:0 margin-top:14px border-top:1px solid #EFF2F8`
      - `div`
        `display:flex flex-direction:column gap:3px`
        - `span` **text 11.5px/500** — “월 실수령”
          `font-size:11.5px font-weight:500 color:#626D88`
        - `span` **text 18px/600** — “—”
          `font-size:18px font-weight:600 letter-spacing:-0.02em color:#697182`
      - `div`
        `display:flex flex-direction:column gap:3px padding:0 10px border-left:1px solid #EFF2F8`
        - `span` **text 11.5px/500** — “월말 예상”
          `font-size:11.5px font-weight:500 color:#626D88`
        - `span` — “—”
          `font-size:18px font-weight:600 letter-spacing:-0.02em color:#697182`
      - `div`
        `display:flex flex-direction:column gap:3px border-left:1px solid #EFF2F8`
        - `span` **text 11.5px/500** — “월말 예상 여유”
          `font-size:11.5px font-weight:500 color:#626D88`
        - `span` — “—”
          `font-size:18px font-weight:600 letter-spacing:-0.02em color:#697182`
    - `div` **text 15px/600** — “월급 입력하고 시작”
      `display:flex align-items:center justify-content:center height:46px margin-top:12px border-radius:13px background:#3556E6 color:#FFFFFF font-size:15px font-weight:600 white-space:nowrap`
  - `div` **text 11px/600** — “C · 급여 0원 · 부수입만 있음 · 예상 기준 통과”
    `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
  - `div` **Card(20)**
    `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px`
    - `div`
      `display:flex align-items:center justify-content:space-between gap:8px`
      - `span` **text 11px/600** — “현재 위치”
        `font-size:11px font-weight:600 letter-spacing:0.07em color:#626D88`
      - `span` **StatusPill** — “입력하면 보여요”
        `background:#F0F2F7 color:#5B6880 font-size:11.5px font-weight:600 border-radius:99px padding:4px 9px white-space:nowrap`
    - `div`
      `display:flex align-items:flex-end justify-content:space-between gap:10px margin-top:8px`
      - `div`
        `display:flex align-items:baseline gap:2px`
        - `span` **text 54px/700** — “1,120,000”
          `font-size:54px font-weight:700 letter-spacing:-0.045em line-height:1 color:#101828`
        - `span` **text 25px/600** — “원”
          `font-size:25px font-weight:600 letter-spacing:-0.02em color:#475467`
    - `div`
      `display:flex align-items:baseline justify-content:space-between gap:10px margin-top:5px`
      - `span` **text 13px/500** — “월급을 넣으면 월급의 몇 %를 썼는지 보여요”
        `font-size:13px font-weight:500 color:#475467`
    - `div`
      `margin-top:15px`
      - `div` **ProgressTrack**
        `position:relative height:10px border-radius:99px background:#E8ECF5`
        - `div`
          `position:absolute left:60% top:-5px width:2px height:20px border-radius:2px background:#101828`
      - `div`
        `position:relative height:15px margin-top:5px`
        - `span` **text 11px/400** — “0%”
          `position:absolute left:0 font-size:11px color:#626D88`
        - `span` **text 11px/600** — “내 목표 60%”
          `position:absolute left:60% transform:translateX(-50%) font-size:11px font-weight:600 color:#101828 white-space:nowrap`
        - `span` **text 11px/400** — “100%”
          `position:absolute right:0 font-size:11px color:#626D88`
    - `div`
      `display:grid grid-template-columns:repeat(3, minmax(0, 1fr)) gap:0 margin-top:14px border-top:1px solid #EFF2F8`
      - `div`
        `display:flex flex-direction:column gap:3px`
        - `span` **text 11.5px/500** — “월 실수령”
          `font-size:11.5px font-weight:500 color:#626D88`
        - `span` **text 18px/600** — “—”
          `font-size:18px font-weight:600 letter-spacing:-0.02em color:#697182`
      - `div`
        `display:flex flex-direction:column gap:3px padding:0 10px border-left:1px solid #EFF2F8`
        - `span` **text 11.5px/500** — “월말 예상”
          `font-size:11.5px font-weight:500 color:#626D88`
        - `span` — “208”
          `font-size:18px font-weight:600 letter-spacing:-0.02em color:#101828`
      - `div`
        `display:flex flex-direction:column gap:3px border-left:1px solid #EFF2F8`
        - `span` **text 11.5px/500** — “월말 예상 여유”
          `font-size:11.5px font-weight:500 color:#626D88 white-space:nowrap`
        - `span` **text 18px/600** — “—”
          `font-size:18px font-weight:600 letter-spacing:-0.02em color:#697182`
    - `p` — “이번 달 실수령 급여가 이에요. 부수입 120만원은 총수입에는 들어가지만 월급의 몇 %인지 셀 때는 쓰지 않아요. ”
      `font-size:12.5px line-height:1.5 color:#475467`
      - `span` — “0원”
        `font-weight:600 color:#101828`
    - `div`
      `margin-top:12px padding:12px background:#FDF1E0 border-radius:14px`
      - `div` **text 11px/600** — “대신 볼 수 있는 지표 · 월급이 아니라 총수입 기준”
        `font-size:11px font-weight:600 letter-spacing:0.06em color:#7A3E0A`
      - `div`
        `display:flex align-items:flex-end justify-content:space-between gap:8px margin-top:6px`
        - `div`
          `display:flex align-items:baseline gap:2px`
        - `span` **text 12px/600** — “총수입 대비 지금까지 쓴 돈”
          `font-size:12px font-weight:600 color:#7A3E0A`
      - `div` **text 11.5px/400** — “총수입 120만원 중 112만원 썼어요 · 월말 예상 208만원은 총수입을 넘어요”
        `font-size:11.5px line-height:1.45 color:#7A3E0A margin-top:5px`
    - `div`
      `display:flex gap:8px margin-top:12px`
      - `div` **PrimaryButton(44)** — “월급 입력하고 시작”
        `flex:1 height:44px border-radius:12px background:#3556E6 display:flex align-items:center justify-content:center font-size:14px font-weight:600 color:#FFFFFF white-space:nowrap`
      - `div` **SecondaryButton(44)** — “총수입 기준으로 보기”
        `flex:1 height:44px border-radius:12px background:#FFFFFF border:1px solid #D7DEEA display:flex align-items:center justify-content:center font-size:14px font-weight:600 color:#475467 white-space:nowrap`
  - `div` **text 11px/600** — “D · 자산 미입력”
    `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
  - `div` **Card(20)**
    `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px`
    - `div`
      `display:flex gap:11px`
      - `div` **Callout(info)**
        `width:36px height:36px border-radius:12px background:#F4F6FB display:flex align-items:center justify-content:center`
      - `div`
        - `div` **text 15px/600** — “아직 자산을 입력하지 않았어요”
          `font-size:15px font-weight:600 letter-spacing:-0.015em color:#101828`
        - `p` **text 12.5px/400** — “순자산·자산 점수·미래 예측은 자산을 입력한 뒤 계산됩니다. 홈의 소비율과 한도는 지금도 그대로 작동해요.”
          `font-size:12.5px line-height:1.5 color:#475467`
    - `div`
      `display:grid grid-template-columns:repeat(3, minmax(0, 1fr)) margin-top:14px padding:12px 0 border-top:1px solid #EFF2F8 border-bottom:1px solid #EFF2F8`
      - `div`
        - `div` **text 11.5px/500** — “순자산”
          `font-size:11.5px font-weight:500 color:#626D88`
        - `div` **text 18px/600** — “—”
          `font-size:18px font-weight:600 color:#B4BECD margin-top:2px`
      - `div`
        `padding:0 10px border-left:1px solid #EFF2F8`
        - `div` **text 11.5px/500** — “총자산”
          `font-size:11.5px font-weight:500 color:#626D88`
        - `div` **text 18px/600** — “—”
          `font-size:18px font-weight:600 color:#B4BECD margin-top:2px`
      - `div`
        `border-left:1px solid #EFF2F8`
        - `div` **text 11.5px/500** — “총부채”
          `font-size:11.5px font-weight:500 color:#626D88`
        - `div` **text 18px/600** — “—”
          `font-size:18px font-weight:600 color:#B4BECD margin-top:2px`
    - `div`
      `display:flex gap:8px margin-top:12px`
      - `div` **PrimaryButton(44)** — “자산 추가”
        `flex:1 height:44px border-radius:12px background:#3556E6 display:flex align-items:center justify-content:center gap:5px font-size:14px font-weight:600 color:#FFFFFF`
      - `div` **SecondaryButton(44)** — “부채 추가”
        `flex:1 height:44px border-radius:12px background:#FFFFFF border:1px solid #D7DEEA display:flex align-items:center justify-content:center gap:5px font-size:14px font-weight:600 color:#475467`
  - `div` **text 11px/600** — “E · 거래 없음 vs 검색 결과 없음”
    `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
  - `div` **Card(20)**
    `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px`
    - `div`
      `display:flex align-items:center gap:11px`
      - `div`
        `width:34px height:34px border-radius:11px background:#F4F6FB display:flex align-items:center justify-content:center`
      - `div`
        `flex:1`
        - `div` **text 13.5px/600** — “9월에 기록한 거래가 없어요”
          `font-size:13.5px font-weight:600 color:#101828`
        - `div` **text 11.5px/400** — “거래를 추가하면 한도·소비율이 함께 갱신됩니다”
          `font-size:11.5px color:#626D88 margin-top:1px`
      - `div` **text 13px/600** — “거래 추가”
        `height:34px padding:0 13px border-radius:10px background:#3556E6 color:#FFFFFF font-size:13px font-weight:600 display:flex align-items:center`
    - `div`
      `height:1px background:#EFF2F8`
    - `div`
      `display:flex align-items:center gap:11px`
      - `div`
        `width:34px height:34px border-radius:11px background:#F4F6FB display:flex align-items:center justify-content:center`
      - `div`
        `flex:1`
        - `div` **text 13.5px/600** — “‘커피’와 일치하는 거래가 없어요”
          `font-size:13.5px font-weight:600 color:#101828`
        - `div` **text 11.5px/400** — “9월에는 32건의 거래가 있어요”
          `font-size:11.5px color:#626D88 margin-top:1px`
      - `div` **text 13px/600** — “검색 지우기”
        `height:34px padding:0 13px border-radius:10px background:#FFFFFF border:1px solid #D7DEEA color:#475467 font-size:13px font-weight:600 display:flex align-items:center`
  - `div` **text 11px/600** — “F · 히어로 이력 부족 · 월말 예상을 아직 보여 주지 않을 때”
    `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
  - `div` **Card(20)**
    `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px`
    - `div`
      `display:flex align-items:center justify-content:space-between gap:8px`
      - `span` **text 11px/600** — “현재 위치”
        `font-size:11px font-weight:600 letter-spacing:0.07em color:#626D88`
    - `div`
      `display:flex align-items:flex-end justify-content:space-between gap:10px margin-top:8px`
      - `div`
        `display:flex align-items:baseline gap:2px`
        - `span` **text 54px/700** — “0.1”
          `font-size:54px font-weight:700 letter-spacing:-0.045em line-height:1 color:#101828`
        - `span` **text 25px/600** — “%”
          `font-size:25px font-weight:600 letter-spacing:-0.02em color:#475467`
      - `div`
        `display:flex flex-direction:column align-items:flex-end gap:1px`
        - `span` **text 11px/500** — “목표까지”
          `font-size:11px font-weight:500 color:#626D88`
        - `span` **text 14px/600** — “59.9%p 남음”
          `font-size:14px font-weight:600 color:#101828`
    - `div`
      `display:flex align-items:baseline justify-content:space-between gap:10px margin-top:5px`
      - `span` **text 13px/500** — “월급 360만원 중 5,000원 썼어요”
        `font-size:13px font-weight:500 color:#475467`
      - `span`
        `display:inline-flex align-items:center gap:4px`
        - `span` **text 11px/500** — “순자산 대비”
          `font-size:11px font-weight:500 color:#697182`
        - `span` **text 13px/600** — “0.1% 미만”
          `font-size:13px font-weight:600 letter-spacing:-0.02em color:#475467`
    - `div` **text 12px/400** — “아직 기록하지 않은 소비는 포함되지 않았어요”
      `font-size:12px line-height:1.45 color:#626D88 margin-top:3px`
    - `div` **text 12px/400** — “월말 예상에 쓸 지난 소비 기록이 아직 없어요”
      `font-size:12px line-height:1.45 color:#626D88 margin-top:3px`
    - `div`
      `margin-top:15px`
      - `div` **ProgressTrack**
        `position:relative height:10px border-radius:99px background:#E8ECF5`
        - `div`
          `position:absolute inset:0 99.9% 0 0 border-radius:99px background:linear-gradient(90deg, #3556E6 0%, #6E6BEE 100%)`
        - `div`
          `position:absolute left:60% top:-5px width:2px height:20px border-radius:2px background:#101828`
      - `div`
        `position:relative height:15px margin-top:5px`
        - `span` **text 11px/400** — “0%”
          `position:absolute left:0 font-size:11px color:#626D88`
        - `span` **text 11px/600** — “내 목표 60%”
          `position:absolute left:60% transform:translateX(-50%) font-size:11px font-weight:600 color:#101828 white-space:nowrap`
        - `span` **text 11px/400** — “100%”
          `position:absolute right:0 font-size:11px color:#626D88`
    - `div`
      `display:grid grid-template-columns:repeat(3, minmax(0, 1fr)) gap:0 margin-top:14px border-top:1px solid #EFF2F8`
      - `div`
        `display:flex flex-direction:column gap:3px`
        - `span` **text 11.5px/500** — “월 실수령”
          `font-size:11.5px font-weight:500 color:#626D88`
        - `span` — “360”
          `font-size:18px font-weight:600 letter-spacing:-0.02em color:#101828`
      - `div`
        `display:flex flex-direction:column gap:3px padding:0 10px border-left:1px solid #EFF2F8`
        - `span` **text 11.5px/500** — “월말 예상”
          `font-size:11.5px font-weight:500 color:#626D88`
        - `span` **text 18px/600** — “—”
          `font-size:18px font-weight:600 letter-spacing:-0.02em color:#697182`
      - `div`
        `display:flex flex-direction:column gap:3px border-left:1px solid #EFF2F8`
        - `span` **text 11.5px/500** — “월말 예상 여유”
          `font-size:11.5px font-weight:500 color:#626D88 white-space:nowrap`
        - `span` **text 18px/600** — “—”
          `font-size:18px font-weight:600 letter-spacing:-0.02em color:#697182`
    - `div`
      `display:flex align-items:center justify-content:space-between gap:10px margin-top:12px`
      - `span` **text 11px/400** — “실수령 급여 기준 · 부수입·저축 이체·대출상환 제외”
        `font-size:11px line-height:1.4 color:#626D88`
      - `span` **text 11.5px/600** — “기준 조정 ›”
        `font-size:11.5px font-weight:600 color:#3556E6 white-space:nowrap`
  - `div` **Card(20)**
    `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:12px 16px 6px`
    - `div` **text 11px/600** — “각주 둘째 줄 · 부족한 것에 따라 셋 중 하나”
      `font-size:11px font-weight:600 letter-spacing:0.06em color:#626D88`
    - `div`
      `padding:10px 0`
      - `div` **text 11.5px/600** — “지난 소비 기록이 없을 때 · 위 카드”
        `font-size:11.5px font-weight:600 color:#475467`
      - `div` **text 12px/400** — “월말 예상에 쓸 지난 소비 기록이 아직 없어요”
        `font-size:12px line-height:1.45 color:#626D88 margin-top:3px`
    - `div`
      `padding:10px 0 border-top:1px solid #EFF2F8`
      - `div` **text 11.5px/600** — “확인하지 않은 달이 하나일 때”
        `font-size:11.5px font-weight:600 color:#475467`
      - `div` — “7월 기록도 확인하면 월말 예상을 볼 수 있어요 ·”
        `font-size:12px line-height:1.45 color:#626D88 margin-top:3px`
        - `span` — “확인하기 ›”
          `font-weight:600 color:#3556E6 white-space:nowrap`
    - `div`
      `padding:10px 0 border-top:1px solid #EFF2F8`
      - `div` **text 11.5px/600** — “확인하지 않은 달이 여러 개일 때”
        `font-size:11.5px font-weight:600 color:#475467`
      - `div` — “월말 예상에 쓸 이전 기록을 확인해 주세요 ·”
        `font-size:12px line-height:1.45 color:#626D88 margin-top:3px`
        - `span` — “확인할 달 보기 ›”
          `font-weight:600 color:#3556E6 white-space:nowrap`
    - `div`
      `padding:10px 0 border-top:1px solid #EFF2F8`
      - `div` **text 11.5px/600** — “이번 달 소비가 0건일 때 · 큰 숫자 · 설명 줄”
        `font-size:11.5px font-weight:600 color:#475467`
      - `div`
        `font-size:12px line-height:1.45 color:#626D88 margin-top:3px`
        - `span` **text 15px/600** — “아직 기록이 없어요”
          `font-size:15px font-weight:600 letter-spacing:-0.015em color:#101828`
      - `div` **text 13px/500** — “달력에서 날짜를 눌러 쓴 돈을 적어 보세요”
        `font-size:13px font-weight:500 color:#475467 margin-top:3px`
      - `div` — “목표까지 · 순자산 대비 · 배지는 숨기고 게이지는 빈 트랙과 목표 선만 · 0%로 보이지 않아요 안 썼어요 표시만”
        `font-size:12px line-height:1.45 color:#626D88 margin-top:3px`
        - `br`
    - `div`
      `padding:10px 0 border-top:1px solid #EFF2F8`
      - `div` **text 11.5px/600** — “월급을 넣지 않았을 때”
        `font-size:11.5px font-weight:600 color:#475467`
      - `div` — “비율 대신 쓴 돈 금액을 크게 쓰고 목표까지 · 순자산 대비를 비웁니다 · 위 B · C와 같아요 기록 부족이면 B”
        `font-size:12px line-height:1.45 color:#626D88 margin-top:3px`
        - `br`
