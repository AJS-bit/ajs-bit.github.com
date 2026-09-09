# EmptyStates — 블록 개요

원본 `canvas/EmptyStates.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div`
  `width:390px height:1718px background:#EDF0F7 color:#101828 padding:18px 14px 20px display:flex flex-direction:column gap:8px`
  - `div`
    `padding:0 2px 6px`
    - `h2` **text 18px/700** — “미입력 · 빈 상태”
      `font-size:18px font-weight:700 letter-spacing:-0.025em color:#101828`
    - `p` — “미입력은 로만 표시하고, 0원·0%·좋은 성과로 바꾸지 않습니다. 자산이 없어도 급여와 소비 기록만으로 시작할 수 ”
      `font-size:12px line-height:1.45 color:#626D88`
      - `span` — “—”
        `font-weight:600 color:#475467`
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
  - `div` **text 11px/600** — “B · 급여 미입력 · 소비 기록만 있음”
    `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
  - `div` **Card(20)**
    `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px`
    - `div`
      `display:flex align-items:center justify-content:space-between gap:8px`
      - `span` **text 11px/600** — “현재 위치”
        `font-size:11px font-weight:600 letter-spacing:0.07em color:#626D88`
      - `span` **StatusPill** — “기준 없음”
        `background:#F0F2F7 color:#5B6880 font-size:11.5px font-weight:600 border-radius:99px padding:4px 9px`
    - `div`
      `display:flex align-items:baseline gap:10px margin-top:8px`
      - `span` **text 48px/700** — “—”
        `font-size:48px font-weight:700 letter-spacing:-0.04em line-height:1 color:#B4BECD`
      - `span` **text 13px/500** — “월급 대비 이번 달 예상 소비”
        `font-size:13px font-weight:500 color:#475467`
    - `div`
      `display:flex align-items:center justify-content:space-between gap:10px margin-top:9px padding:9px 11px background:#F4F6FB border-radius:11px`
      - `span` — “급여가 없어도 는 계산돼요”
        `font-size:12px color:#626D88`
        - `b` — “순자산 대비”
          `font-weight:600`
      - `span`
        `display:inline-flex align-items:center gap:4px`
        - `span` **text 15px/600** — “2.2%”
          `font-size:15px font-weight:600 letter-spacing:-0.02em color:#101828`
    - `div` **ProgressTrack**
      `height:10px border-radius:99px background:#EFF2F8 border:1px dashed #CFD7E6 margin-top:14px`
    - `p` — “실수령 급여를 입력하면 이 비율을 계산할 수 있어요.”
      `font-size:12.5px line-height:1.5 color:#475467`
      - `span` — “미입력은 0%가 아닙니다.”
        `font-weight:600 color:#101828`
    - `div`
      `display:grid grid-template-columns:repeat(3, minmax(0, 1fr)) margin-top:13px border-top:1px solid #EFF2F8`
      - `div`
        - `div` **text 11.5px/500** — “월 실수령”
          `font-size:11.5px font-weight:500 color:#626D88`
        - `div` **text 18px/600** — “—”
          `font-size:18px font-weight:600 color:#B4BECD margin-top:3px`
      - `div`
        `padding:0 10px border-left:1px solid #EFF2F8`
        - `div` **text 11.5px/500** — “월말 예상”
          `font-size:11.5px font-weight:500 color:#626D88`
        - `div` — “208”
          `font-size:18px font-weight:600 color:#101828 margin-top:3px`
      - `div`
        `border-left:1px solid #EFF2F8`
        - `div` **text 11.5px/500** — “남은 여유”
          `font-size:11.5px font-weight:500 color:#626D88`
        - `div` **text 18px/600** — “—”
          `font-size:18px font-weight:600 color:#B4BECD margin-top:3px`
    - `div` **text 15px/600** — “실수령 급여 입력하기”
      `display:flex align-items:center justify-content:center height:46px margin-top:12px border-radius:13px background:#3556E6 color:#FFFFFF font-size:15px font-weight:600`
  - `div` **text 11px/600** — “C · 급여 0원 · 부수입만 있음”
    `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
  - `div` **Card(20)**
    `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px`
    - `div`
      `display:flex align-items:center justify-content:space-between gap:8px`
      - `span` **text 11px/600** — “현재 위치”
        `font-size:11px font-weight:600 letter-spacing:0.07em color:#626D88`
      - `span` **StatusPill** — “급여 기준 없음”
        `background:#F0F2F7 color:#5B6880 font-size:11.5px font-weight:600 border-radius:99px padding:4px 9px`
    - `div`
      `display:flex align-items:baseline gap:10px margin-top:8px`
      - `span` **text 48px/700** — “—”
        `font-size:48px font-weight:700 letter-spacing:-0.04em line-height:1 color:#B4BECD`
      - `span` **text 13px/500** — “월급 대비 소비율”
        `font-size:13px font-weight:500 color:#475467`
    - `p` — “이번 달 실수령 급여가 이에요. 부수입 120만원은 총수입에는 들어가지만, 급여 대비 소비율의 기준으로는 쓰지 않습”
      `font-size:12.5px line-height:1.5 color:#475467`
      - `span` — “0원”
        `font-weight:600 color:#101828`
    - `div`
      `margin-top:12px padding:12px background:#FDF1E0 border-radius:14px`
      - `div` **text 11px/600** — “대신 볼 수 있는 지표”
        `font-size:11px font-weight:600 letter-spacing:0.06em color:#7A3E0A`
      - `div`
        `display:flex align-items:flex-end justify-content:space-between gap:8px margin-top:6px`
        - `div`
          `display:flex align-items:baseline gap:2px`
        - `span` **text 12px/600** — “총수입 대비 예상 소비”
          `font-size:12px font-weight:600 color:#7A3E0A`
      - `div` **text 11.5px/400** — “총수입 120만원 · 월말 예상 소비 208만원 · 총수입을 넘고 있어요”
        `font-size:11.5px color:#7A3E0A margin-top:5px`
    - `div`
      `display:flex gap:8px margin-top:12px`
      - `div` **PrimaryButton(44)** — “급여 입력”
        `flex:1 height:44px border-radius:12px background:#3556E6 display:flex align-items:center justify-content:center font-size:14px font-weight:600 color:#FFFFFF`
      - `div` **SecondaryButton(44)** — “총수입 기준으로 보기”
        `flex:1 height:44px border-radius:12px background:#FFFFFF border:1px solid #D7DEEA display:flex align-items:center justify-content:center font-size:14px font-weight:600 color:#475467`
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
