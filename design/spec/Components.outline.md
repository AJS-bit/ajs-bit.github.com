# Components — 블록 개요

원본 `canvas/Components.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div`
  `width:1200px height:4773px background:#FFFFFF color:#101828 padding:40px 44px display:flex flex-direction:column gap:28px`
  - `div`
    `display:flex align-items:flex-end justify-content:space-between gap:20px border-bottom:2px solid #101828`
    - `div`
      - `div` **text 12px/600** — “NAVI DESIGN SYSTEM v3”
        `font-size:12px font-weight:600 letter-spacing:0.14em color:#626D88`
      - `h1` **text 34px/700** — “버튼 · 입력 · 카드 · 폼 상태”
        `font-size:34px font-weight:700 letter-spacing:-0.035em line-height:1.15 color:#101828`
    - `p` — “주 행동 버튼 46–48px, 보조 30–42px. 누를 수 있는 것은 모두 의 누르는 영역을 모양은 그대로 · 가”
      `font-size:13px line-height:1.55 color:#475467`
      - `b` — “44 × 44 이상”
        `font-weight:600 color:#101828`
      - `span` — “가집니다(보이는”
        `white-space:nowrap`
      - `span` — “적용(설정”
        `white-space:nowrap`
      - `span` — “「바로 적용돼요」)과”
        `white-space:nowrap`
  - `div`
    `display:grid grid-template-columns:minmax(0, 1fr) minmax(0, 1.1fr) gap:32px`
    - `div`
      - `div` **text 12px/600** — “01 · 버튼 위계와 상태”
        `font-size:12px font-weight:600 letter-spacing:0.1em color:#626D88 margin-top:0px`
      - `div`
        `display:grid grid-template-columns:repeat(4, minmax(0, 1fr)) gap:10px 10px margin-top:14px align-items:start`
        - `div` **text 11px/400** — “기본”
          `font-size:11px color:#697182`
        - `div` **text 11px/400** — “비활성 — 까닭 줄과 함께”
          `font-size:11px color:#697182`
        - `div` **text 11px/400** — “저장 중”
          `font-size:11px color:#697182`
        - `div` **text 11px/400** — “빠진 칸이 있을 때 누름”
          `font-size:11px color:#697182`
        - `div`
        - `div`
        - `div`
        - `div`
      - `div`
        `display:grid grid-template-columns:repeat(4, minmax(0, 1fr)) gap:10px margin-top:14px`
        - `div` **SecondaryButton(44)** — “취소”
          `height:44px border-radius:12px display:flex align-items:center justify-content:center gap:6px font-size:14px font-weight:600 white-space:nowrap background:#FFFFFF border:1px solid #D7DEEA color:#475467`
        - `div` **text 14px/600** — “총한도 조정”
          `height:44px border-radius:12px display:flex align-items:center justify-content:center gap:6px font-size:14px font-weight:600 white-space:nowrap background:#FFFFFF border:1.5px solid #3556E6 color:#3556E6`
        - `div` **text 14px/600** — “배분 편집”
          `height:44px border-radius:12px display:flex align-items:center justify-content:center gap:6px font-size:14px font-weight:600 white-space:nowrap background:#E9EDFD color:#3556E6`
        - `div` **text 14px/600** — “삭제”
          `height:44px border-radius:12px display:flex align-items:center justify-content:center gap:6px font-size:14px font-weight:600 white-space:nowrap background:#FCEBEA color:#C0342F`
      - `div`
        `display:flex align-items:center gap:10px margin-top:12px`
        - `div` — “목적지 추가”
          `flex:1 height:44px border-radius:12px border:1.5px dashed #B9C3D6 background:#F8FAFD display:flex align-items:center justify-content:center gap:6px font-size:14px font-weight:600 color:#3556E6`
        - `div` **text 14px/600** — “상환 계획 보기 ›”
          `flex:1 height:44px display:flex align-items:center justify-content:center font-size:14px font-weight:600 color:#3556E6`
        - `span` — “자동”
          `display:inline-flex align-items:center gap:2px height:26px background:#E9EDFD color:#3556E6 font-size:12px font-weight:600 border-radius:99px padding:0 8px 0 11px`
      - `div` **Callout(info)**
        `display:flex gap:10px margin-top:14px padding:12px 14px background:#F4F6FB border-radius:12px`
        - `span` — “나머지는 외곽선 · 연한 배경 · 글자 링크로 내립니다. 점선 버튼은 “목록 끝에서 항목을 새로 만드는” 자리에만.”
          `font-size:12px line-height:1.55 color:#475467`
      - `div` **text 12px/600** — “02 · 배지와 칩”
        `font-size:12px font-weight:600 letter-spacing:0.1em color:#626D88 margin-top:28px`
      - `div`
        `display:flex flex-wrap:wrap gap:8px margin-top:14px`
        - `span` — “월말에도 목표 안”
          `display:inline-flex align-items:center gap:5px background:#E4F4EA color:#0F7B47 font-size:12px font-weight:600 border-radius:99px padding:5px 10px white-space:nowrap`
        - `span` **text 12px/600** — “월말엔 목표 초과”
          `display:inline-flex align-items:center gap:5px background:#FDF1E0 color:#B45309 font-size:12px font-weight:600 border-radius:99px padding:5px 10px white-space:nowrap`
        - `span` **text 12px/600** — “월말엔 월급 초과”
          `display:inline-flex align-items:center gap:5px background:#FCEBEA color:#C0342F font-size:12px font-weight:600 border-radius:99px padding:5px 10px white-space:nowrap`
        - `span` **text 12px/600** — “입력하면 보여요”
          `display:inline-flex align-items:center gap:5px background:#F0F2F7 color:#5B6880 font-size:12px font-weight:600 border-radius:99px padding:5px 10px white-space:nowrap`
        - `span` — “저장되지 않는 가정”
          `display:inline-flex align-items:center gap:5px background:#F1EAFD color:#6B32D6 font-size:12px font-weight:600 border-radius:99px padding:5px 10px white-space:nowrap`
        - `span` — “저장된 계획”
          `display:inline-flex align-items:center gap:5px background:#E4F4EA color:#0F7B47 font-size:12px font-weight:600 border-radius:99px padding:5px 10px white-space:nowrap`
        - `span` **text 12px/600** — “확인 필요”
          `display:inline-flex align-items:center gap:5px background:#FDF1E0 color:#7A3E0A font-size:12px font-weight:600 border-radius:99px padding:5px 10px white-space:nowrap`
        - `span` **text 11px/600** — “입력 필요”
          `display:inline-flex align-items:center gap:5px background:#F4F6FB color:#475467 font-size:11px font-weight:600 border-radius:99px padding:3px 8px white-space:nowrap`
        - `span` **text 11px/600** — “임시 계산”
          `display:inline-flex align-items:center gap:5px background:#F0F2F7 color:#5B6880 font-size:11px font-weight:600 border-radius:99px padding:3px 8px white-space:nowrap`
        - `span` **text 10.5px/600** — “가정”
          `display:inline-flex align-items:center gap:5px background:#F1EAFD color:#6B32D6 font-size:10.5px font-weight:600 border-radius:6px padding:3px 6px white-space:nowrap`
        - `span` — “처음 안내”
          `display:inline-flex align-items:center gap:5px min-height:22px padding:2px 9px border-radius:99px background:#E9EDFD color:#3556E6 font-size:11.5px font-weight:700 letter-spacing:0.02em white-space:nowrap`
        - `span` — “화면 안내”
          `display:inline-flex align-items:center gap:5px min-height:22px padding:2px 9px border-radius:99px background:#E9EDFD color:#3556E6 font-size:11.5px font-weight:700 letter-spacing:0.02em white-space:nowrap`
        - `span` **text 10.5px/600** — “홈 대표”
          `display:inline-flex align-items:center gap:5px background:#E9EDFD color:#3556E6 font-size:10.5px font-weight:600 border-radius:6px padding:3px 6px white-space:nowrap`
      - `div` — “월말 배지 셋은 월말 예상 기준이 선 없으면 회색 · 기록이 모자라거나 이번 달 0건이면 배지 없음). = 한 번도”
        `font-size:11px line-height:1.45 color:#626D88 margin-top:10px`
        - `span` — “달에만(월급이”
          `white-space:nowrap`
        - `span` — “「입력하면 보여요」”
          `white-space:nowrap`
        - `span` — “「입력 필요」”
          `white-space:nowrap`
        - `span` — “「임시 계산」”
          `white-space:nowrap`
        - `span` — “「가정」은”
          `white-space:nowrap`
        - `span` — “「매달 모으는 돈 바꿔 보기」로”
          `white-space:nowrap`
        - `span` — “「홈 대표」는”
          `white-space:nowrap`
        - `span` — “「처음 안내」”
          `white-space:nowrap`
        - `span` — “「화면 안내」는”
          `white-space:nowrap`
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
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px 16px 12px margin-top:14px`
        - `div`
          `display:flex justify-content:space-between align-items:baseline`
        - `div`
          `display:flex gap:12px margin-top:6px font-size:11px color:#475467`
      - `div`
        `display:flex flex-direction:column gap:7px margin-top:12px`
        - `div`
          `display:flex gap:8px`
        - `div`
          `display:flex gap:8px`
        - `div`
          `display:flex gap:8px`
        - `div`
          `display:flex gap:8px`
        - `div`
          `display:flex gap:8px`
        - `div`
          `display:flex gap:8px`
    - `div`
      - `div` **text 12px/600** — “04 · 입력 · 단위 · 필수 표시”
        `font-size:12px font-weight:600 letter-spacing:0.1em color:#626D88 margin-top:0px`
      - `div`
        `display:grid grid-template-columns:repeat(2, minmax(0, 1fr)) gap:14px margin-top:14px`
        - `div`
        - `div`
        - `div`
        - `div`
      - `div` — “· 자산 이름, 지금 금액 — 창 아래 버튼 위에 한 번, 첫 칸으로 이동”
        `margin-top:12px padding:10px 12px background:#FCEBEA border-radius:11px font-size:12px color:#7C221E`
        - `b` — “빠진 칸이 있어요”
          `font-weight:600`
      - `div`
        `display:grid grid-template-columns:repeat(2, minmax(0, 1fr)) gap:14px margin-top:16px`
        - `div`
        - `div`
      - `div`
        `margin-top:14px border:1px solid #E3E8F1 border-radius:16px text-align:center`
        - `div`
          `padding:16px`
        - `div`
          `display:flex flex-direction:column gap:8px padding:16px background:#F8FAFD border-top:1px solid #E3E8F1`
      - `div` **Callout(info)**
        `display:flex gap:10px margin-top:14px padding:12px 14px background:#F4F6FB border-radius:12px`
        - `span` — “단위는 늘 입력 칸 오른쪽 안쪽. 만원 칸은 쓰는 동안 쉼표를 넣고 칸 아래에 되읽기 · · 비었거나 0이면 없음)”
          `font-size:12px line-height:1.55 color:#475467`
      - `div` **text 12px/600** — “05 · 긴 폼의 구조 · 추가와 수정”
        `font-size:12px font-weight:600 letter-spacing:0.1em color:#626D88 margin-top:28px`
      - `div`
        `display:grid grid-template-columns:repeat(2, minmax(0, 1fr)) gap:14px margin-top:14px`
        - `div`
          `border:1px solid #E3E8F1 border-radius:16px`
        - `div`
          `border:1px solid #E3E8F1 border-radius:16px`
      - `div` — “추가와 수정은 로만 구분합니다. 본문 구조와 칸 순서는 같게, 오른쪽 위에는 늘 ✕ 닫기. 하단 행동은 고정되고 본”
        `font-size:11.5px line-height:1.55 color:#475467 margin-top:10px`
        - `span` — “제목 · 설명 · 저장 버튼 문구 · 삭제 유무”
          `font-weight:600 color:#101828`
      - `div` **text 12px/600** — “06 · 저장 알림 · 오류”
        `font-size:12px font-weight:600 letter-spacing:0.1em color:#626D88 margin-top:26px`
      - `div`
        `display:flex flex-direction:column gap:9px margin-top:13px`
        - `div`
          `padding:12px 14px border-radius:16px background:#101828 box-shadow:0 12px 30px -14px rgba(16,24,40,.5)`
        - `div`
          `display:flex align-items:center gap:9px height:40px padding:0 14px border-radius:12px background:#101828 color:#FFFFFF font-size:13px`
        - `div`
          `display:flex align-items:flex-start gap:9px padding:12px 14px border-radius:13px background:#9D3346`
        - `div` — “한도를 저장하지 못했습니다. 넣은 값은 그대로 있어요. 다시 저장해 주세요.”
          `padding:10px 12px border:1px solid #E3E8F1 border-radius:12px font-size:12px color:#C0342F`
      - `div` — “알림은 아래 탭 바로 위 어두운 카드 하나 — 6초 동안 · 내용 · 닫기 · 되돌리기) 보이고 40px 띠 「✓ ”
        `font-size:11px line-height:1.45 color:#626D88 margin-top:10px`
        - `span` — “온전히(제목”
          `white-space:nowrap`
        - `span` — “닫기」로”
          `white-space:nowrap`
        - `span` — “사라집니다(되돌리기도”
          `white-space:nowrap`
        - `span` — “「못했습니다」로”
          `white-space:nowrap`
        - `span` — “카드(되돌리기”
          `white-space:nowrap`
  - `div`
    `padding:18px 20px background:#F4F6FB border-radius:16px`
    - `div` **text 12px/600** — “07 · 행동을 어디에 놓는가 — 이번 재설계의 핵심 규칙”
      `font-size:12px font-weight:600 letter-spacing:0.1em color:#626D88 margin-top:0px`
    - `div`
      `display:grid grid-template-columns:repeat(4, minmax(0, 1fr)) gap:18px margin-top:14px`
      - `div`
        - `div` **text 13px/600** — “바꾸는 값 가까이”
          `font-size:13px font-weight:600 color:#101828`
        - `div` — “총한도 조정은 총한도 숫자 아래, 배분 편집은 카테고리 목록 머리, 알약 한도 머리 — 셋 다 같은 한도 조정 창을”
          `font-size:11.5px line-height:1.55 color:#475467 margin-top:4px`
      - `div`
        - `div` **text 13px/600** — “목록 끝에서 추가”
          `font-size:13px font-weight:600 color:#101828`
        - `div` — “목적지 추가는 목록 마지막 점선 버튼. 상환 방식 · 월 추가 상환액은 미래 › 상환 계획 한 곳에서만 › 상환 계”
          `font-size:11.5px line-height:1.55 color:#475467 margin-top:4px`
      - `div`
        - `div` **text 13px/600** — “행 안에서 행 조작”
          `font-size:13px font-weight:600 color:#101828`
        - `div` — “적립은 줄 오른쪽의 연한 수정 · 삭제는 ⋯ 관리 메뉴 안. 적립할 수 없는 순자산 · 부채 상환 목적지에는 버튼이”
          `font-size:11.5px line-height:1.55 color:#475467 margin-top:4px`
      - `div`
        - `div` **text 13px/600** — “기준은 근거 옆에”
          `font-size:13px font-weight:600 color:#101828`
        - `div` — “기준 · 저축 이체와 대출 갚은 돈은 쓴 돈에 넣지 않아요」 문장 오른쪽 — 내 수치 창을 엽니다. 무엇이 바뀌는지”
          `font-size:11.5px line-height:1.55 color:#475467 margin-top:4px`
  - `div`
    - `div` **text 12px/600** — “08 · v5 달력과 하루 시트 — 새 컴포넌트 11종”
      `font-size:12px font-weight:600 letter-spacing:0.1em color:#626D88`
    - `p` — “조각은 v5 달력 · 하루 시트 · 완료 카드 · 카테고리 고르기)에서 그대로 가져왔습니다. 새 색은 없습니다 — ”
      `font-size:12.5px line-height:1.55 color:#475467`
      - `span` — “시안(홈”
        `white-space:nowrap`
      - `span` — “brand-soft”
        `white-space:nowrap`
      - `span` — “ink-2”
        `white-space:nowrap`
      - `span` — “ink-3”
        `white-space:nowrap`
      - `span` — “ink-4”
        `white-space:nowrap`
      - `span` — “씁니다(그날”
        `white-space:nowrap`
      - `span` — “ink-2”
        `white-space:nowrap`
      - `span` — “ink-3”
        `white-space:nowrap`
      - `span` — “ink-4”
        `white-space:nowrap`
      - `span` — “v5-calendar.css”
        `white-space:nowrap`
    - `div`
      `display:flex align-items:flex-start justify-content:space-between gap:18px margin-top:14px background:#EDF0F7 border-radius:18px padding:16px 14px 18px`
      - `div`
        `width:362px display:flex flex-direction:column gap:9px`
        - `div`
          `display:flex gap:8px padding:0 2px`
        - `div`
          `display:flex gap:8px padding:0 2px`
        - `div`
          `display:flex gap:8px padding:0 2px`
        - `div` **Card(18)**
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 14px 13px`
        - `div` **Card(18)**
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:13px 14px 13px`
        - `div`
          `height:8px`
        - `div`
          `display:flex gap:8px padding:0 2px`
        - `div`
          `background:#FFFFFF border:1px solid #E3E8F1 border-top:none border-radius:0 0 20px 20px padding:4px 16px 16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
      - `div`
        `width:362px display:flex flex-direction:column gap:9px`
        - `div`
          `display:flex gap:8px padding:0 2px`
        - `div`
          `display:flex gap:8px padding:0 2px`
        - `div`
          `display:flex gap:8px padding:0 2px`
        - `div`
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:26px display:flex flex-direction:column`
        - `div`
          `height:8px`
        - `div`
          `display:flex gap:8px padding:0 2px`
        - `div` **HeroCard**
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
      - `div`
        `width:324px display:flex flex-direction:column gap:9px`
        - `div`
          `display:flex gap:8px padding:0 2px`
        - `div` **Card(18)**
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 6px 10px display:grid grid-template-columns:repeat(4, 1fr)`
        - `div`
          `height:8px`
        - `div`
          `display:flex gap:8px padding:0 2px`
        - `div`
          `background:#101828 border-radius:16px padding:13px 14px 12px color:#FFFFFF box-shadow:0 8px 24px rgba(0,0,0,.28)`
        - `div`
          `height:8px`
        - `div`
          `display:flex gap:8px padding:0 2px`
        - `div` **Card(18)**
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:2px 16px 4px`
  - `div`
    - `div` — “09 · 탭 머리줄 — 모든 탭이 같은”
      `font-size:12px font-weight:600 letter-spacing:0.1em color:#626D88`
      - `span` — “틀(AppTopbar)”
        `white-space:nowrap`
    - `div`
      `display:grid grid-template-columns:repeat(3, 356px) justify-content:space-between gap:18px 8px margin-top:14px background:#EDF0F7 border-radius:18px padding:16px 14px 18px`
      - `div`
        `display:flex flex-direction:column gap:9px`
        - `div`
        - `div`
          `width:356px background:#EDF0F7 border:1px solid #E3E8F1 border-radius:18px`
        - `div`
        - `div`
          `width:356px background:#EDF0F7 border:1px solid #E3E8F1 border-radius:18px`
      - `div`
        `display:flex flex-direction:column gap:9px`
        - `div`
        - `div`
          `width:356px background:#EDF0F7 border:1px solid #E3E8F1 border-radius:18px`
      - `div`
        `display:flex flex-direction:column gap:9px`
        - `div`
        - `div`
          `width:356px background:#EDF0F7 border:1px solid #E3E8F1 border-radius:18px`
        - `div`
  - `div`
    - `div` **text 12px/600** — “10 · 판정 줄 · 참고 줄 · 비어 있는 값”
      `font-size:12px font-weight:600 letter-spacing:0.1em color:#626D88`
    - `div`
      `display:grid grid-template-columns:repeat(3, 356px) justify-content:space-between gap:18px 8px margin-top:14px background:#EDF0F7 border-radius:18px padding:16px 14px 18px`
      - `div`
        `display:flex flex-direction:column gap:9px`
        - `div`
        - `div` **HeroCard**
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
      - `div`
        `display:flex flex-direction:column gap:9px`
        - `div`
        - `div` **Card(18)**
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px`
        - `div`
        - `div` **Card(18)**
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px`
      - `div`
        `display:flex flex-direction:column gap:9px`
        - `div`
        - `div` **Card(18)**
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:8px 14px 6px`
        - `div`
        - `div` **Card(18)**
          `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px display:flex align-items:center gap:10px`
