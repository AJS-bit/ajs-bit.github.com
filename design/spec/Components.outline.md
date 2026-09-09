# Components — 블록 개요

원본 `canvas/Components.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div`
  `width:1200px height:1471px background:#FFFFFF color:#101828 padding:40px 44px display:flex flex-direction:column gap:28px`
  - `div`
    `display:flex align-items:flex-end justify-content:space-between gap:20px border-bottom:2px solid #101828`
    - `div`
      - `div` **text 12px/600** — “NAVI DESIGN SYSTEM v3”
        `font-size:12px font-weight:600 letter-spacing:0.14em color:#626D88`
      - `h1` **text 34px/700** — “버튼 · 입력 · 카드 · 폼 상태”
        `font-size:34px font-weight:700 letter-spacing:-0.035em line-height:1.15 color:#101828`
    - `p` **text 13px/400** — “주 행동 버튼 46–48px, 보조 30–42px(히트 영역은 44px 권장). 금액 입력은 16px 이상(모바일 ”
      `font-size:13px line-height:1.55 color:#475467`
  - `div`
    `display:grid grid-template-columns:minmax(0, 1fr) minmax(0, 1.1fr) gap:32px`
    - `div`
      - `div` **text 12px/600** — “01 · 버튼 위계와 상태”
        `font-size:12px font-weight:600 letter-spacing:0.1em color:#626D88`
      - `div`
        `display:grid grid-template-columns:repeat(4, minmax(0, 1fr)) gap:10px margin-top:14px`
        - `div` **text 11px/400** — “기본”
          `font-size:11px color:#697182`
        - `div` **text 11px/400** — “비활성”
          `font-size:11px color:#697182`
        - `div` **text 11px/400** — “저장 중”
          `font-size:11px color:#697182`
        - `div` **text 11px/400** — “완료”
          `font-size:11px color:#697182`
        - `div` **PrimaryButton(44)** — “저장”
          `height:44px border-radius:12px background:#3556E6 display:flex align-items:center justify-content:center font-size:14px font-weight:600 color:#FFFFFF`
        - `div` **text 14px/600** — “저장”
          `height:44px border-radius:12px background:#E8ECF5 display:flex align-items:center justify-content:center font-size:14px font-weight:600 color:#B4BECD`
        - `div` — “저장 중”
          `height:44px border-radius:12px background:#6B85EC display:flex align-items:center justify-content:center gap:7px font-size:14px font-weight:600 color:#FFFFFF`
        - `div` — “저장됨”
          `height:44px border-radius:12px background:#0F7B47 display:flex align-items:center justify-content:center gap:6px font-size:14px font-weight:600 color:#FFFFFF`
      - `div`
        `display:grid grid-template-columns:repeat(4, minmax(0, 1fr)) gap:10px margin-top:14px`
        - `div` **SecondaryButton(44)** — “취소”
          `height:44px border-radius:12px background:#FFFFFF border:1px solid #D7DEEA display:flex align-items:center justify-content:center font-size:14px font-weight:600 color:#475467`
        - `div` **text 14px/600** — “총한도 조정”
          `height:44px border-radius:12px background:#FFFFFF border:1.5px solid #3556E6 display:flex align-items:center justify-content:center font-size:14px font-weight:600 color:#3556E6`
        - `div` **text 14px/600** — “배분 편집”
          `height:44px border-radius:12px background:#E9EDFD display:flex align-items:center justify-content:center font-size:14px font-weight:600 color:#3556E6`
        - `div` **text 14px/600** — “삭제”
          `height:44px border-radius:12px background:#FCEBEA display:flex align-items:center justify-content:center font-size:14px font-weight:600 color:#C0342F`
      - `div`
        `display:flex gap:10px margin-top:12px`
        - `div` — “목적지 추가”
          `flex:1 height:44px border-radius:12px border:1.5px dashed #B9C3D6 background:#F8FAFD display:flex align-items:center justify-content:center gap:6px font-size:14px font-weight:600 color:#3556E6`
        - `div` **text 14px/600** — “상환 전략 보기 ›”
          `flex:1 height:44px display:flex align-items:center justify-content:center font-size:14px font-weight:600 color:#3556E6`
      - `div` **Callout(info)**
        `display:flex gap:10px margin-top:14px padding:12px 14px background:#F4F6FB border-radius:12px`
        - `span` — “나머지는 외곽선·연한 배경·텍스트 링크로 내립니다. 점선 버튼은 “목록 끝에서 항목을 새로 만드는” 자리에만 씁니다”
          `font-size:12px line-height:1.55 color:#475467`
      - `div` **text 12px/600** — “02 · 배지와 칩”
        `font-size:12px font-weight:600 letter-spacing:0.1em color:#626D88 margin-top:28px`
      - `div`
        `display:flex flex-wrap:wrap gap:8px margin-top:14px`
        - `span` — “목표 안에서 순항 중”
          `display:inline-flex align-items:center gap:5px background:#E4F4EA color:#0F7B47 font-size:12px font-weight:600 border-radius:99px padding:5px 10px`
        - `span` **text 12px/600** — “목표 초과”
          `display:inline-flex align-items:center gap:5px background:#FDF1E0 color:#B45309 font-size:12px font-weight:600 border-radius:99px padding:5px 10px`
        - `span` **text 12px/600** — “급여의 100% 초과”
          `display:inline-flex align-items:center gap:5px background:#FCEBEA color:#C0342F font-size:12px font-weight:600 border-radius:99px padding:5px 10px`
        - `span` **text 12px/600** — “기준 없음”
          `display:inline-flex align-items:center gap:5px background:#F0F2F7 color:#5B6880 font-size:12px font-weight:600 border-radius:99px padding:5px 10px`
        - `span` **text 12px/600** — “자동 계산”
          `display:inline-flex align-items:center gap:5px background:#E9EDFD color:#3556E6 font-size:12px font-weight:600 border-radius:99px padding:5px 10px`
        - `span` — “저장되지 않는 가정”
          `display:inline-flex align-items:center gap:5px background:#F1EAFD color:#6B32D6 font-size:12px font-weight:600 border-radius:99px padding:5px 10px`
        - `span` **text 12px/600** — “확인 필요”
          `display:inline-flex align-items:center gap:5px background:#E4F2FB color:#0A72AC font-size:12px font-weight:600 border-radius:99px padding:5px 10px`
        - `span` **text 10.5px/600** — “홈 대표”
          `display:inline-flex align-items:center gap:5px background:#E9EDFD color:#3556E6 font-size:10.5px font-weight:600 border-radius:6px padding:3px 6px`
      - `div` **text 12px/600** — “03 · 카드 위계”
        `font-size:12px font-weight:600 letter-spacing:0.1em color:#626D88 margin-top:28px`
      - `div`
        `display:flex flex-direction:column gap:10px margin-top:14px`
        - `div`
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:22px padding:14px 16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
        - `div` **Card(18)**
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px 16px`
        - `div`
          `background:#F4F6FB border-radius:14px padding:14px 16px`
        - `div` **TurnCard**
          `background:#FFFFFF border:1px solid #E3E8F1 border-left:3px solid #DE8A2A border-radius:18px padding:14px 16px`
      - `div` **text 12px/600** — “03b · 그래프 규칙”
        `font-size:12px font-weight:600 letter-spacing:0.1em color:#626D88 margin-top:26px`
      - `div` **Card(18)**
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:15px 16px 13px margin-top:14px`
        - `div`
          `position:relative height:92px`
        - `div`
          `display:flex justify-content:space-between border-top:1px solid #EFF2F8 margin-top:4px`
      - `div`
        `display:flex flex-direction:column gap:7px margin-top:12px`
        - `div`
          `display:flex gap:8px`
        - `div`
          `display:flex gap:8px`
        - `div`
          `display:flex gap:8px`
    - `div`
      - `div` **text 12px/600** — “04 · 입력 · 단위 · 필수 표시”
        `font-size:12px font-weight:600 letter-spacing:0.1em color:#626D88`
      - `div`
        `display:grid grid-template-columns:repeat(2, minmax(0, 1fr)) gap:14px margin-top:14px`
        - `div`
        - `div`
        - `div`
        - `div`
      - `div`
        `display:grid grid-template-columns:repeat(2, minmax(0, 1fr)) gap:14px margin-top:16px`
        - `div`
        - `div`
      - `div` **Callout(info)**
        `display:flex gap:10px margin-top:14px padding:12px 14px background:#F4F6FB border-radius:12px`
        - `span` — “단위는 항상 입력 칸 오른쪽 안쪽에 고정합니다. — 비우면 자동 계산(연한 회색 자동값 표시), 0을 넣으면 “0원”
          `font-size:12px line-height:1.55 color:#475467`
      - `div` **text 12px/600** — “05 · 긴 폼의 구조 · 추가와 수정”
        `font-size:12px font-weight:600 letter-spacing:0.1em color:#626D88 margin-top:28px`
      - `div`
        `display:grid grid-template-columns:repeat(2, minmax(0, 1fr)) gap:14px margin-top:14px`
        - `div`
          `border:1px solid #E3E8F1 border-radius:16px`
        - `div`
          `border:1px solid #E3E8F1 border-radius:16px`
      - `div` — “추가와 수정은 로만 구분합니다. 본문 구조와 필드 순서는 동일하게 유지해 근육 기억을 지킵니다. 하단 행동은 항상 ”
        `font-size:11.5px line-height:1.55 color:#475467 margin-top:10px`
        - `span` — “제목·저장 버튼 문구·삭제 버튼 유무”
          `font-weight:600 color:#101828`
      - `div` **text 12px/600** — “06 · 저장 알림”
        `font-size:12px font-weight:600 letter-spacing:0.1em color:#626D88 margin-top:26px`
      - `div`
        `display:flex flex-direction:column gap:9px margin-top:13px`
        - `div`
          `display:flex align-items:center gap:10px padding:12px 14px border-radius:13px background:#101828 box-shadow:0 12px 30px -14px rgba(16,24,40,.5)`
        - `div`
          `display:flex align-items:center gap:10px padding:12px 14px border-radius:13px background:#7A1F1B box-shadow:0 12px 30px -14px rgba(16,24,40,.5)`
  - `div`
    `margin-top:auto padding:18px 20px background:#F4F6FB border-radius:16px`
    - `div` **text 12px/600** — “07 · 행동을 어디에 놓는가 — 이번 재설계의 핵심 규칙”
      `font-size:12px font-weight:600 letter-spacing:0.1em color:#626D88`
    - `div`
      `display:grid grid-template-columns:repeat(4, minmax(0, 1fr)) gap:18px margin-top:14px`
      - `div`
        - `div` **text 13px/600** — “바꾸는 값 바로 아래”
          `font-size:13px font-weight:600 color:#101828`
        - `div` **text 11.5px/400** — “총한도 조정 버튼은 총한도 숫자 아래, 배분 편집은 카테고리 목록 헤더. 하나의 버튼이 두 종류의 값을 바꾸지 않습”
          `font-size:11.5px line-height:1.55 color:#475467 margin-top:4px`
      - `div`
        - `div` **text 13px/600** — “목록 끝에서 추가”
          `font-size:13px font-weight:600 color:#101828`
        - `div` **text 11.5px/400** — “목적지 추가는 목록 마지막 점선 버튼. 탭 위에 떠 있던 버튼을 없앴습니다.”
          `font-size:11.5px line-height:1.55 color:#475467 margin-top:4px`
      - `div`
        - `div` **text 13px/600** — “행 안에서 행 조작”
          `font-size:13px font-weight:600 color:#101828`
        - `div` **text 11.5px/400** — “적립·수정·삭제는 해당 행 오른쪽 끝. 적립이 불가능한 순자산·부채 목표에는 버튼 자체를 두지 않습니다.”
          `font-size:11.5px line-height:1.55 color:#475467 margin-top:4px`
      - `div`
        - `div` **text 13px/600** — “기준은 근거 옆에”
          `font-size:13px font-weight:600 color:#101828`
        - `div` **text 11.5px/400** — ““기준 조정”은 “실수령 급여 기준…” 문장 오른쪽. 무엇이 바뀌는지 읽은 자리에서 바로 누릅니다.”
          `font-size:11.5px line-height:1.55 color:#475467 margin-top:4px`
