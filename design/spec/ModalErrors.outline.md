# ModalErrors — 블록 개요

원본 `canvas/ModalErrors.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div`
  `width:390px height:2061px background:#EDF0F7 color:#101828 padding:18px 14px 20px display:flex flex-direction:column gap:8px`
  - `div`
    `padding:0 2px 6px`
    - `h2` **text 18px/700** — “모달 오류 · 저장 상태 6종”
      `font-size:18px font-weight:700 letter-spacing:-0.025em color:#101828`
    - `p` **text 12px/400** — “오류는 무엇이 잘못됐는지와 어떻게 고치는지를 같이 말합니다. 실패해도 입력한 값은 지우지 않습니다.”
      `font-size:12px line-height:1.45 color:#626D88`
  - `div` **text 11px/600** — “A · 필수 값 미입력 — 저장 비활성”
    `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
  - `div` **Card(18)**
    `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:16px`
    - `div`
      `display:flex align-items:center justify-content:space-between gap:8px border-bottom:1px solid #EFF2F8`
      - `div`
        `display:flex align-items:baseline gap:7px`
        - `span` **text 15px/700** — “거래 추가”
          `font-size:15px font-weight:700 letter-spacing:-0.02em color:#101828`
        - `span` **text 11.5px/400** — “9월 8일”
          `font-size:11.5px color:#626D88`
      - `div`
        `width:28px height:28px border-radius:9px background:#F4F6FB display:flex align-items:center justify-content:center`
    - `div`
      `display:flex gap:10px`
      - `div`
        `flex:1`
        - `div` — “금액”
          `font-size:12px font-weight:600 color:#475467`
        - `div`
          `display:flex align-items:center gap:5px height:46px padding:0 12px border-radius:11px border:1.5px solid #C0342F background:#FFFFFF`
        - `div`
          `display:flex align-items:center gap:5px margin-top:6px`
    - `div`
      `display:flex gap:10px margin-top:13px`
      - `div`
        `flex:1`
        - `div` **text 12px/600** — “카테고리”
          `font-size:12px font-weight:600 color:#475467`
        - `div` **InputField**
          `display:flex align-items:center gap:5px height:46px padding:0 12px border-radius:11px border:1px solid #CFD7E6 background:#FFFFFF`
    - `div`
      `margin-top:13px`
      - `div` **Callout(info)**
        `display:flex gap:8px padding:10px 11px background:#F4F6FB border-radius:12px`
        - `span`
          `margin-top:1px`
        - `span` — “0원을 저장하면 그날 소비가 0원으로 기록되고, 비워 두면 아무것도 기록되지 않습니다.”
          `font-size:11.5px line-height:1.5 color:#626D88`
    - `div`
      `display:flex gap:9px margin-top:14px border-top:1px solid #EFF2F8`
      - `div` **text 15px/600** — “취소”
        `display:flex align-items:center justify-content:center gap:6px height:46px flex:1 border-radius:13px background:#FFFFFF border:1px solid #D7DEEA color:#475467 font-size:15px font-weight:600`
      - `div` **text 15px/600** — “저장”
        `display:flex align-items:center justify-content:center gap:6px height:46px flex:1.4 border-radius:13px background:#E8ECF5 border:none color:#B4BECD font-size:15px font-weight:600`
  - `div` **text 11px/600** — “B · 값이 규칙에 어긋남 — 배분 합 초과”
    `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
  - `div` **Card(18)**
    `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:16px`
    - `div`
      `display:flex align-items:center justify-content:space-between gap:8px border-bottom:1px solid #EFF2F8`
      - `div`
        `display:flex align-items:baseline gap:7px`
        - `span` **text 15px/700** — “카테고리 배분 편집”
          `font-size:15px font-weight:700 letter-spacing:-0.02em color:#101828`
        - `span` **text 11.5px/400** — “13개”
          `font-size:11.5px color:#626D88`
      - `div`
        `width:28px height:28px border-radius:9px background:#F4F6FB display:flex align-items:center justify-content:center`
    - `div`
      `display:flex align-items:center justify-content:space-between gap:10px`
      - `div`
        `flex:1`
        - `div` **text 12px/600** — “식비”
          `font-size:12px font-weight:600 color:#475467`
        - `div`
          `display:flex align-items:center gap:5px height:46px padding:0 12px border-radius:11px border:1.5px solid #C0342F background:#FFFFFF`
        - `div`
          `display:flex align-items:center gap:5px margin-top:6px`
    - `div` **ProgressTrack**
      `position:relative height:10px border-radius:99px background:#E8ECF5 margin-top:10px`
      - `div`
        `position:absolute inset:0 8.5% 0 0 border-radius:99px 0 0 99px background:#3556E6`
      - `div`
        `position:absolute right:0 top:0 bottom:0 width:8.5% border-radius:0 99px 99px 0 background:repeating-linear-gradient(135deg, #C0342F 0 4px, #E0908C 4px 8px)`
      - `div`
        `position:absolute left:91.5% top:-5px width:2px height:20px border-radius:2px background:#101828`
    - `div`
      `display:flex justify-content:space-between margin-top:7px`
      - `span` — “배분 합”
        `font-size:11px color:#626D88`
        - `b` — “236만원”
          `font-weight:600`
      - `span` **text 11px/600** — “총한도 216만원 · 20만원 초과”
        `font-size:11px font-weight:600 color:#C0342F`
    - `div`
      `margin-top:13px`
      - `div`
        `display:flex gap:8px padding:10px 11px background:#FCEBEA border-radius:12px`
        - `span`
          `margin-top:1px`
        - `span` **text 11.5px/400** — “총한도를 넘는 배분은 저장할 수 없습니다. 아래 중 하나를 고르거나 다른 카테고리를 줄여 주세요.”
          `font-size:11.5px line-height:1.5 color:#7C221E`
    - `div`
      `display:flex flex-direction:column gap:7px margin-top:11px`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:8px height:42px padding:0 12px border-radius:11px border:1px solid #D7DEEA background:#FFFFFF`
        - `span` **text 13px/600** — “식비를 45만원으로 되돌리기”
          `font-size:13px font-weight:600 color:#101828 white-space:nowrap`
        - `span`
          `display:inline-flex align-items:center gap:5px`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:8px height:42px padding:0 12px border-radius:11px border:1px solid #D7DEEA background:#FFFFFF`
        - `span` **text 13px/600** — “총한도를 236만원으로 올리기”
          `font-size:13px font-weight:600 color:#101828 white-space:nowrap`
        - `span`
          `display:inline-flex align-items:center gap:5px`
    - `div`
      `display:flex gap:9px margin-top:14px border-top:1px solid #EFF2F8`
      - `div` **text 15px/600** — “취소”
        `display:flex align-items:center justify-content:center gap:6px height:46px flex:1 border-radius:13px background:#FFFFFF border:1px solid #D7DEEA color:#475467 font-size:15px font-weight:600`
      - `div` **text 15px/600** — “저장”
        `display:flex align-items:center justify-content:center gap:6px height:46px flex:1.4 border-radius:13px background:#E8ECF5 border:none color:#B4BECD font-size:15px font-weight:600`
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
      `margin-top:13px`
      - `div` **Callout(info)**
        `display:flex gap:8px padding:10px 11px background:#F4F6FB border-radius:12px`
        - `span`
          `margin-top:1px`
        - `span` **text 11.5px/400** — “기기에 저장하는 중이에요. 창을 닫아도 저장은 계속됩니다.”
          `font-size:11.5px line-height:1.5 color:#626D88`
    - `div`
      `display:flex gap:9px margin-top:14px border-top:1px solid #EFF2F8`
      - `div` **text 15px/600** — “취소”
        `display:flex align-items:center justify-content:center gap:6px height:46px flex:1 border-radius:13px background:#E8ECF5 border:none color:#B4BECD font-size:15px font-weight:600`
      - `div` — “저장 중”
        `display:flex align-items:center justify-content:center gap:8px height:46px flex:1.4 border-radius:13px background:#3556E6 opacity:.72 color:#FFFFFF font-size:15px font-weight:600`
        - `span`
          `width:16px height:16px border-radius:99px border:2px solid #8FA6F2 display:inline-block`
  - `div` **text 11px/600** — “D · 저장 실패 — 입력값 보존”
    `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
  - `div` **Card(18)**
    `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:16px`
    - `div`
      `display:flex gap:12px`
      - `div`
        `width:40px height:40px border-radius:13px background:#FCEBEA display:flex align-items:center justify-content:center`
      - `div`
        - `div` **text 16px/700** — “저장하지 못했어요”
          `font-size:16px font-weight:700 letter-spacing:-0.02em color:#101828`
        - `div` — “기기 저장소에 쓸 수 없습니다. 다시 시도해 주세요.”
          `font-size:12.5px line-height:1.55 color:#475467 margin-top:5px`
    - `div`
      `margin-top:12px`
      - `div` **Callout(info)**
        `display:flex gap:8px padding:10px 11px background:#F4F6FB border-radius:12px`
        - `span`
          `margin-top:1px`
        - `span` **text 11.5px/400** — “저장 공간이 부족할 수 있어요. 계속 실패하면 백업 파일로 내보낸 뒤 공간을 확보해 주세요.”
          `font-size:11.5px line-height:1.5 color:#626D88`
    - `div`
      `display:flex gap:9px margin-top:14px`
      - `div` — “다시 저장”
        `display:flex align-items:center justify-content:center gap:6px height:46px flex:1.4 border-radius:13px background:#3556E6 border:none color:#FFFFFF font-size:15px font-weight:600`
      - `div` — “백업 내보내기”
        `display:flex align-items:center justify-content:center gap:6px height:46px flex:1 border-radius:13px background:#FFFFFF border:1px solid #D7DEEA color:#475467 font-size:15px font-weight:600`
  - `div` **text 11px/600** — “E · 저장 완료 — 무엇이 바뀌었는지”
    `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
  - `div` **Card(18)**
    `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:16px`
    - `div`
      `display:flex align-items:center gap:12px`
      - `div`
        `width:38px height:38px border-radius:99px background:#E4F4EA display:flex align-items:center justify-content:center`
      - `div` **text 15px/700** — “저장했어요”
        `flex:1 font-size:15px font-weight:700 letter-spacing:-0.02em color:#101828`
      - `span` **StatusPill** — “되돌리기”
        `display:inline-flex align-items:center gap:4px background:#F0F2F7 color:#5B6880 font-size:11.5px font-weight:600 border-radius:99px padding:4px 9px`
    - `div` **text 12px/400** — “식비 12,000원 · 남은 한도 103만원 · 사용 113만원”
      `font-size:12px color:#626D88 margin-top:7px`
    - `div`
      `position:relative height:3px border-radius:99px background:#E8ECF5 margin-top:13px`
      - `div`
        `position:absolute inset:0 62% 0 0 border-radius:99px background:#0F7B47`
    - `div` **text 11px/400** — “2초 후 자동으로 닫혀요”
      `font-size:11px color:#697182 margin-top:6px`
  - `div` **text 11px/600** — “F · 저장하지 않고 닫기”
    `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
  - `div` **Card(18)**
    `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:16px`
    - `div` **text 16px/700** — “저장하지 않고 닫을까요?”
      `font-size:16px font-weight:700 letter-spacing:-0.02em color:#101828`
    - `div` **text 12.5px/400** — “금액과 카테고리를 입력했지만 아직 저장하지 않았습니다. 닫으면 입력한 내용이 사라집니다.”
      `font-size:12.5px line-height:1.55 color:#475467 margin-top:6px`
    - `div`
      `display:flex gap:9px margin-top:15px`
      - `div` **text 15px/600** — “계속 입력”
        `display:flex align-items:center justify-content:center gap:6px height:46px flex:1 border-radius:13px background:#FFFFFF border:1px solid #D7DEEA color:#475467 font-size:15px font-weight:600`
      - `div` **text 15px/600** — “저장하지 않고 닫기”
        `display:flex align-items:center justify-content:center gap:6px height:46px flex:1.3 border-radius:13px background:#FCEBEA border:none color:#C0342F font-size:15px font-weight:600`
