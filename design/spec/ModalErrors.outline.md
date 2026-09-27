# ModalErrors — 블록 개요

원본 `canvas/ModalErrors.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div`
  `width:390px height:3290px background:#EDF0F7 color:#101828 padding:18px 14px 20px display:flex flex-direction:column gap:8px`
  - `div`
    `padding:0 2px 6px`
    - `span` **text 11px/600** — “구현 참고 · 앱 화면이 아닙니다”
      `display:inline-block font-size:11px font-weight:600 letter-spacing:0.02em color:#475467 border:1px solid #E3E8F1 background:#FFFFFF border-radius:99px padding:4px 10px white-space:nowrap`
    - `h2` **text 18px/700** — “모달 오류 · 저장 상태 7종”
      `font-size:18px font-weight:700 letter-spacing:-0.025em color:#101828`
    - `p` **text 12px/400** — “저장이 막히거나 실패했을 때 보이는 창 일곱 가지입니다. 실제로는 한 번에 하나만 보입니다.”
      `font-size:12px line-height:1.45 color:#626D88`
  - `div` **text 11px/600** — “A · 필수 값 미입력 — 저장을 누르면 빠진 칸을 알려 줌”
    `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
  - `div`
    `display:flex flex-direction:column gap:8px`
    - `div` **Card(18)**
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:16px`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:8px border-bottom:1px solid #EFF2F8`
        - `div`
          `display:flex align-items:baseline gap:7px`
        - `div`
          `width:28px height:28px border-radius:9px background:#F4F6FB display:flex align-items:center justify-content:center`
      - `div` **text 12px/600** — “기록 종류”
        `font-size:12px font-weight:600 color:#475467`
      - `div`
        `display:flex gap:4px background:#F4F6FB border-radius:11px padding:3px`
        - `div` **text 12.5px/500** — “소비”
          `flex:1 height:34px border-radius:8px display:flex align-items:center justify-content:center font-size:12.5px font-weight:500 color:#5B6880`
        - `div` **text 12.5px/600** — “저축·투자”
          `flex:1 height:34px border-radius:8px background:#FFFFFF display:flex align-items:center justify-content:center font-size:12.5px font-weight:600 color:#101828 box-shadow:0 1px 2px rgba(16,24,40,.08)`
        - `div` **text 12.5px/500** — “대출상환”
          `flex:1 height:34px border-radius:8px display:flex align-items:center justify-content:center font-size:12.5px font-weight:500 color:#5B6880`
      - `div`
        `display:flex flex-direction:column margin-top:12px`
        - `div`
      - `div`
        `display:flex flex-direction:column margin-top:12px`
        - `div`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:12px margin-top:12px`
        - `span` **text 13px/400** — “카테고리”
          `font-size:13px color:#475467`
        - `div`
          `text-align:right`
      - `div` **text 12.5px/400** — “빠진 칸이 있어요 · 금액”
        `margin-top:12px padding:10px 12px border-radius:11px background:#FCEBEA font-size:12.5px line-height:1.5 color:#C0342F`
      - `div`
        `display:flex gap:9px margin-top:14px border-top:1px solid #EFF2F8`
        - `div` **text 15px/600** — “취소”
          `display:flex align-items:center justify-content:center gap:6px height:46px flex:1 border-radius:13px background:#FFFFFF border:1px solid #D7DEEA color:#475467 font-size:15px font-weight:600`
        - `div` **text 15px/600** — “저장”
          `display:flex align-items:center justify-content:center gap:6px height:46px flex:1.4 border-radius:13px background:#3556E6 border:none color:#FFFFFF font-size:15px font-weight:600`
    - `div` **Callout(info)**
      `display:flex gap:8px padding:10px 11px background:#F4F6FB border-radius:12px`
      - `span`
        `margin-top:1px`
      - `span` **text 11.5px/400** — “하루 시트만 예외 — 금액이 비면 「저장」은 회색으로 누를 수 없고 아래에 「금액을 넣으면 저장할 수 있어요」가 붙”
        `font-size:11.5px line-height:1.5 color:#626D88`
  - `div` **text 11px/600** — “B · 직접 정한 카테고리 합계가 총한도보다 큼”
    `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
  - `div` **Card(18)**
    `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:16px`
    - `div`
      `display:flex align-items:center justify-content:space-between gap:8px border-bottom:1px solid #EFF2F8`
      - `div`
        `display:flex align-items:baseline gap:7px`
        - `span` **text 15px/700** — “한도 조정”
          `font-size:15px font-weight:700 letter-spacing:-0.02em color:#101828`
      - `div`
        `width:28px height:28px border-radius:9px background:#F4F6FB display:flex align-items:center justify-content:center`
    - `div`
      `display:flex align-items:baseline gap:7px`
      - `span` **text 13.5px/600** — “카테고리 배분”
        `font-size:13.5px font-weight:600 color:#101828`
      - `span` **text 11.5px/400** — “단위 만원 · 비우면 자동”
        `font-size:11.5px color:#626D88`
    - `div`
      `display:flex align-items:center gap:10px min-height:52px border-bottom:1px solid #F3F5FA`
      - `div`
        `width:30px height:30px border-radius:9px background:#f9731620 display:flex align-items:center justify-content:center`
      - `div`
        `flex:1`
        - `div` **text 13.5px/600** — “식비”
          `font-size:13.5px font-weight:600 color:#101828`
        - `div` **text 11px/400** — “직접 180만원”
          `font-size:11px color:#626D88`
      - `div`
        `display:flex align-items:center gap:3px width:96px height:40px padding:0 10px border-radius:11px border:1.5px solid #3556E6 background:#FFFFFF`
        - `span` **text 15px/600** — “180”
          `flex:1 text-align:right font-size:15px font-weight:600 color:#101828`
        - `span` **text 12px/400** — “만원”
          `font-size:12px color:#626D88`
    - `div`
      `display:flex align-items:center gap:10px min-height:52px border-bottom:1px solid #F3F5FA`
      - `div`
        `width:30px height:30px border-radius:9px background:#8b5cf620 display:flex align-items:center justify-content:center`
      - `div`
        `flex:1`
        - `div` **text 13.5px/600** — “주거/관리”
          `font-size:13.5px font-weight:600 color:#101828`
        - `div` **text 11px/400** — “직접 56만원”
          `font-size:11px color:#626D88`
      - `div`
        `display:flex align-items:center gap:3px width:96px height:40px padding:0 10px border-radius:11px border:1px solid #CFD7E6 background:#FFFFFF`
        - `span` **text 15px/600** — “56”
          `flex:1 text-align:right font-size:15px font-weight:600 color:#101828`
        - `span` **text 12px/400** — “만원”
          `font-size:12px color:#626D88`
    - `div`
      `display:flex align-items:center gap:10px min-height:52px`
      - `div`
        `width:30px height:30px border-radius:9px background:#d9770620 display:flex align-items:center justify-content:center`
      - `div`
        `flex:1`
        - `div` **text 13.5px/600** — “카페/간식”
          `font-size:13.5px font-weight:600 color:#101828`
        - `div` **text 11px/400** — “자동 0원”
          `font-size:11px color:#626D88`
      - `div`
        `display:flex align-items:center gap:3px width:96px height:40px padding:0 10px border-radius:11px border:1px solid #CFD7E6 background:#FFFFFF`
        - `span` **text 15px/500** — “0”
          `flex:1 text-align:right font-size:15px font-weight:500 color:#B4BECD`
        - `span` **text 12px/400** — “만원”
          `font-size:12px color:#626D88`
    - `div` **Callout(warn)**
      `margin-top:12px padding:11px 12px border-radius:12px background:#FDF1E0 border:1px solid #DE8A2A`
      - `div` — “직접 정한 카테고리 합계가 총한도보다 커요”
        `display:flex align-items:center gap:6px font-size:12.5px font-weight:600 color:#7A3E0A`
      - `div` **text 13px/700** — “236만원 / 216만원”
        `text-align:right font-size:13px font-weight:700 color:#7A3E0A margin-top:4px`
      - `div` **text 11.5px/400** — “직접 정한 금액을 줄이거나 총한도를 늘려 주세요.”
        `font-size:11.5px color:#7A3E0A margin-top:3px`
    - `div`
      `display:flex gap:9px margin-top:14px border-top:1px solid #EFF2F8`
      - `div` **text 15px/600** — “취소”
        `display:flex align-items:center justify-content:center gap:6px height:46px flex:1 border-radius:13px background:#FFFFFF border:1px solid #D7DEEA color:#475467 font-size:15px font-weight:600`
      - `div` **text 15px/600** — “한도 저장”
        `display:flex align-items:center justify-content:center gap:6px height:46px flex:1.4 border-radius:13px background:#3556E6 border:none color:#FFFFFF font-size:15px font-weight:600`
  - `div` **text 11px/600** — “C · 저장 중 — 입력 잠금”
    `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
  - `div` **Card(18)**
    `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:16px`
    - `div`
      `display:flex align-items:center justify-content:space-between gap:8px border-bottom:1px solid #EFF2F8`
      - `div`
        `display:flex align-items:baseline gap:7px`
        - `span` **text 15px/700** — “자산 추가”
          `font-size:15px font-weight:700 letter-spacing:-0.02em color:#101828`
      - `div`
        `width:28px height:28px border-radius:9px background:#F4F6FB display:flex align-items:center justify-content:center`
    - `div`
      `opacity:.55`
      - `div`
        `display:flex gap:10px`
        - `div`
          `flex:1`
        - `div`
          `width:150px`
    - `div`
      `display:flex gap:9px margin-top:14px border-top:1px solid #EFF2F8`
      - `div` **text 15px/600** — “취소”
        `display:flex align-items:center justify-content:center gap:6px height:46px flex:1 border-radius:13px background:#E8ECF5 border:none color:#B4BECD font-size:15px font-weight:600`
      - `div` **text 15px/600** — “자산 추가”
        `display:flex align-items:center justify-content:center gap:6px height:46px flex:1.4 opacity:.6 border-radius:13px background:#3556E6 border:none color:#FFFFFF font-size:15px font-weight:600`
    - `div` **text 12px/400** — “기기에 저장 중… 잠시만 기다려 주세요.”
      `font-size:12px color:#626D88 margin-top:9px`
  - `div` **text 11px/600** — “D · 저장 실패 — 실패한 자리 옆에 한 번”
    `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
  - `div`
    `display:flex flex-direction:column gap:8px`
    - `div` **Card(18)**
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
      - `div` **text 11.5px/600** — “기록 추가 · 저장을 눌렀는데 기기에 못 씀”
        `font-size:11.5px font-weight:600 color:#626D88`
      - `div` **Callout(info)**
        `display:flex align-items:center justify-content:space-between gap:10px padding:11px 12px background:#F4F6FB border-radius:12px`
        - `div`
        - `div`
          `width:46px height:27px border-radius:99px background:#E3E8F1 padding:3px display:flex justify-content:flex-start`
      - `div`
        `display:flex gap:9px margin-top:14px border-top:1px solid #EFF2F8`
        - `div` **text 15px/600** — “취소”
          `display:flex align-items:center justify-content:center gap:6px height:46px flex:1 border-radius:13px background:#FFFFFF border:1px solid #D7DEEA color:#475467 font-size:15px font-weight:600`
        - `div` **text 15px/600** — “저장”
          `display:flex align-items:center justify-content:center gap:6px height:46px flex:1.4 border-radius:13px background:#3556E6 border:none color:#FFFFFF font-size:15px font-weight:600`
      - `div` **text 12px/400** — “기기에 저장하지 못했습니다. 입력한 값은 그대로 있어요. 저장 공간을 확인한 뒤 다시 저장해 주세요.”
        `font-size:12px line-height:1.5 color:#C0342F margin-top:10px`
    - `div` **Card(18)**
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
      - `div` **text 11.5px/600** — “하루 시트 · 금액 칸 아래”
        `font-size:11.5px font-weight:600 color:#626D88`
      - `div`
        `flex:1`
        - `div` **text 12px/600** — “금액”
          `font-size:12px font-weight:600 color:#475467`
        - `div` **InputField**
          `display:flex align-items:center gap:5px height:46px padding:0 12px border-radius:11px border:1px solid #CFD7E6 background:#FFFFFF`
      - `div` — “· 저장을 눌러야 기록돼요”
        `font-size:11.5px color:#626D88 margin-top:6px`
        - `b` — “1.2만원”
          `font-weight:600 color:#475467`
      - `div` — “저장하지 못했어요. 적은 내용은 그대로 있어요. ·”
        `margin-top:9px padding:10px 12px border-radius:11px background:#FCEBEA font-size:12.5px line-height:1.5 color:#C0342F`
        - `b` — “다시 시도”
          `font-weight:600 color:#3556E6`
    - `div` **Card(18)**
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
      - `div` **text 11.5px/600** — “미래 › 상환 계획 · 저장 칸”
        `font-size:11.5px font-weight:600 color:#626D88`
      - `div` **text 14px/700** — “이 계획을 저장할까요?”
        `font-size:14px font-weight:700 color:#101828`
      - `div` **text 12px/400** — “저장해야 홈 · 자산 경로 · 목적지 계산에 반영돼요.”
        `font-size:12px color:#626D88 margin-top:3px`
      - `div`
        `display:flex gap:8px margin-top:11px`
        - `div` **text 15px/600** — “가정 종료”
          `display:flex align-items:center justify-content:center gap:6px height:42px flex:1 border-radius:13px background:#FFFFFF border:1px solid #D7DEEA color:#475467 font-size:15px font-weight:600`
        - `div` **text 15px/600** — “상환 계획 저장”
          `display:flex align-items:center justify-content:center gap:6px height:42px flex:1.4 border-radius:13px background:#3556E6 border:none color:#FFFFFF font-size:15px font-weight:600`
      - `div` **text 12.5px/400** — “상환 계획을 저장하지 못했습니다. 이전 계획(고금리 우선 · 월 15만원)을 그대로 써요.”
        `margin-top:10px padding:10px 12px border-radius:11px background:#FCEBEA font-size:12.5px line-height:1.5 color:#C0342F`
  - `div` **text 11px/600** — “E · 저장 알림 — 6초 카드 → 한 줄 띠”
    `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
  - `div` **Card(18)**
    `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
    - `div` **text 11.5px/600** — “처음 6초 — 아래 탭 막대 바로 위”
      `font-size:11.5px font-weight:600 color:#626D88`
    - `div`
      `background:#101828 border-radius:16px padding:13px 14px color:#FFFFFF box-shadow:0 10px 28px -14px rgba(16,24,40,.6)`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:10px`
        - `span` — “한도를 저장했어요 · 총한도 216만원 · 자동”
          `display:inline-flex align-items:center gap:7px font-size:13.5px font-weight:600`
        - `span` **text 12.5px/400** — “닫기”
          `font-size:12.5px color:rgba(255,255,255,.72)`
      - `div` **text 13px/600** — “되돌리기”
        `display:inline-flex align-items:center height:34px padding:0 13px margin-top:11px border-radius:10px border:1px solid rgba(255,255,255,.38) font-size:13px font-weight:600`
    - `div`
      `height:12px`
    - `div` **text 11.5px/600** — “6초 뒤 — 같은 알림이 한 줄 띠로(길면 요약 끝을 … 로 줄임)”
      `font-size:11.5px font-weight:600 color:#626D88`
    - `div`
      `display:flex align-items:center height:40px padding:0 4px 0 12px background:#101828 border-radius:12px color:#FFFFFF`
      - `span`
        `display:flex align-items:center gap:6px flex:1`
        - `span` **text 13px/600** — “한도를 저장했어요 · 총한도 216만원…”
          `font-size:13px font-weight:600 line-height:16px white-space:nowrap`
      - `span` **text 14px/400** — “·”
        `font-size:14px color:rgba(255,255,255,.5)`
      - `b` **text 13px/700** — “되돌리기”
        `padding:0 9px font-size:13px font-weight:700 white-space:nowrap`
      - `span` **text 14px/400** — “·”
        `font-size:14px color:rgba(255,255,255,.5)`
      - `span` **text 13px/600** — “닫기”
        `padding:0 9px font-size:13px font-weight:600 color:rgba(255,255,255,.72) white-space:nowrap`
    - `div` **text 12px/400** — “6초 뒤 한 줄로 줄고 1분 뒤 사라져요 · 탭을 옮겨도 남아요 · 새로 저장하면 바뀌어요. 되돌리기는 이 알림에만”
      `font-size:12px line-height:1.5 color:#626D88 margin-top:10px`
  - `div` **text 11px/600** — “F · 저장하지 않고 닫기”
    `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
  - `div`
    `display:flex flex-direction:column gap:8px`
    - `div` **Card(18)**
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:16px`
      - `div`
        `text-align:center padding:4px 4px 0`
        - `div` **text 16px/700** — “저장하지 않고 닫을까요?”
          `font-size:16px font-weight:700 letter-spacing:-0.02em color:#101828`
        - `div` **text 12.5px/400** — “이번에 넣은 내용은 저장되지 않아요. 계속 작성하면 넣은 값을 그대로 둘 수 있어요.”
          `font-size:12.5px line-height:1.55 color:#626D88 margin-top:6px`
      - `div`
        `display:flex flex-direction:column gap:7px margin-top:15px`
        - `div` **text 14px/600** — “변경 버리고 닫기”
          `display:flex align-items:center justify-content:center height:40px border-radius:11px background:#FCEBEA color:#C0342F font-size:14px font-weight:600`
        - `div` **text 14px/600** — “계속 작성”
          `display:flex align-items:center justify-content:center height:40px border-radius:11px background:#E8ECF5 border:2px solid #3556E6 box-shadow:0 0 0 3px rgba(53,86,230,.18) color:#101828 font-size:14px font-weight:600`
    - `div` **Callout(info)**
      `display:flex gap:8px padding:10px 11px background:#F4F6FB border-radius:12px`
      - `span`
        `margin-top:1px`
      - `span` **text 11.5px/400** — “처음 초점은 「계속 작성」. 하루 시트는 예외(확인 없음 · 초안은 메모리에만, 앱을 다시 켜면 사라짐)”
        `font-size:11.5px line-height:1.5 color:#626D88`
  - `div` **text 11px/600** — “G · 부채 상환 목적지 — 넣어 둔 부채가 없을 때”
    `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
  - `div` **Card(18)**
    `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:16px`
    - `div`
      `display:flex align-items:center justify-content:space-between gap:8px border-bottom:1px solid #EFF2F8`
      - `div`
        `display:flex align-items:baseline gap:7px`
        - `span` **text 15px/700** — “목적지 추가”
          `font-size:15px font-weight:700 letter-spacing:-0.02em color:#101828`
      - `div`
        `width:28px height:28px border-radius:9px background:#F4F6FB display:flex align-items:center justify-content:center`
    - `div` **text 12px/600** — “유형”
      `font-size:12px font-weight:600 color:#475467`
    - `div`
      `display:flex gap:5px`
      - `div`
        `flex:1 padding:8px 4px border-radius:11px text-align:center border:1px solid #E3E8F1 background:#FFFFFF`
        - `div`
          `display:flex justify-content:center`
        - `div` **text 10.5px/500** — “일반 저축”
          `font-size:10.5px font-weight:500 color:#475467 margin-top:4px white-space:nowrap`
      - `div`
        `flex:1 padding:8px 4px border-radius:11px text-align:center border:1px solid #E3E8F1 background:#FFFFFF`
        - `div`
          `display:flex justify-content:center`
        - `div` **text 10.5px/500** — “비상금”
          `font-size:10.5px font-weight:500 color:#475467 margin-top:4px white-space:nowrap`
      - `div`
        `flex:1 padding:8px 4px border-radius:11px text-align:center border:1px solid #E3E8F1 background:#FFFFFF`
        - `div`
          `display:flex justify-content:center`
        - `div` **text 10.5px/500** — “투자”
          `font-size:10.5px font-weight:500 color:#475467 margin-top:4px white-space:nowrap`
      - `div`
        `flex:1 padding:8px 4px border-radius:11px text-align:center border:1px solid #E3E8F1 background:#FFFFFF`
        - `div`
          `display:flex justify-content:center`
        - `div` **text 10.5px/500** — “순자산”
          `font-size:10.5px font-weight:500 color:#475467 margin-top:4px white-space:nowrap`
      - `div`
        `flex:1 padding:8px 4px border-radius:11px text-align:center border:1.5px solid #B45309 background:#B4530914`
        - `div`
          `display:flex justify-content:center`
        - `div` **text 10.5px/700** — “부채 상환”
          `font-size:10.5px font-weight:700 color:#B45309 margin-top:4px white-space:nowrap`
    - `div`
      `margin-top:13px`
      - `div` **text 12px/600** — “갚을 부채”
        `font-size:12px font-weight:600 color:#475467`
      - `div` **text 12.5px/400** — “먼저 부채를 넣어 주세요”
        `font-size:12.5px color:#626D88`
      - `div` **text 13px/600** — “부채 추가하기 ›”
        `font-size:13px font-weight:600 color:#3556E6 margin-top:6px`
    - `div` **text 12px/400** — “누르면 자산 › 부채로 가서 새 부채 창이 열립니다.”
      `font-size:12px line-height:1.5 color:#626D88 margin-top:12px`
    - `div`
      `display:flex gap:9px margin-top:14px border-top:1px solid #EFF2F8`
      - `div` **text 15px/600** — “취소”
        `display:flex align-items:center justify-content:center gap:6px height:46px flex:1 border-radius:13px background:#FFFFFF border:1px solid #D7DEEA color:#475467 font-size:15px font-weight:600`
      - `div` **text 15px/600** — “목적지 추가”
        `display:flex align-items:center justify-content:center gap:6px height:46px flex:1.4 border-radius:13px background:#3556E6 border:none color:#FFFFFF font-size:15px font-weight:600`
