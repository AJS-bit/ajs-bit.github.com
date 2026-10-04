# StorageStates — 블록 개요

원본 `canvas/StorageStates.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div`
  `width:390px height:2787px background:#EDF0F7 color:#101828 padding:18px 14px 20px display:flex flex-direction:column gap:8px`
  - `div`
    `padding:0 2px 6px`
    - `span` **text 11px/600** — “구현 참고 · 앱 화면이 아닙니다”
      `display:inline-block font-size:11px font-weight:600 letter-spacing:0.02em color:#475467 border:1px solid #E3E8F1 background:#FFFFFF border-radius:99px padding:4px 10px white-space:nowrap`
    - `h2` **text 18px/700** — “저장소 로딩 · 실패 · 복구”
      `font-size:18px font-weight:700 letter-spacing:-0.025em color:#101828`
    - `p` **text 12px/400** — “기록을 불러오거나 복구할 때 생길 수 있는 경우입니다. 실제로는 한 번에 하나만 보입니다.”
      `font-size:12px line-height:1.45 color:#626D88`
  - `div` **text 11px/600** — “A · 불러오는 중”
    `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
  - `div`
    `display:flex align-items:center gap:9px padding:2px 4px 4px`
    - `div`
      `width:40px height:40px border-radius:11px background:linear-gradient(140deg, #3556E6 0%, #7A3FE4 100%) display:flex align-items:center justify-content:center`
    - `span` **text 17px/700** — “NAVI”
      `font-size:17px font-weight:700 letter-spacing:0.06em color:#101828`
  - `div` **Card(18)**
    `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:18px 16px`
    - `div`
      `display:flex flex-direction:column align-items:center text-align:center padding:14px 4px`
      - `div`
        `width:44px height:44px border-radius:99px border:3px solid #E8ECF5`
      - `div` **text 14px/600** — “저장된 기록을 불러오는 중”
        `font-size:14px font-weight:600 color:#101828 margin-top:14px`
      - `div` **text 12px/400** — “잠시만 기다려 주세요”
        `font-size:12px color:#626D88 margin-top:4px`
  - `div` **text 11px/600** — “B · 불러오기 실패”
    `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
  - `div` **Card(18)**
    `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:18px 16px`
    - `div`
      `display:flex flex-direction:column align-items:center text-align:center padding:6px 4px 2px`
      - `div`
        `width:44px height:44px border-radius:14px background:#FCEBEA display:flex align-items:center justify-content:center`
      - `div` **text 16px/700** — “저장된 기록을 불러오지 못했어요”
        `font-size:16px font-weight:700 letter-spacing:-0.02em color:#101828 margin-top:12px`
      - `div` **text 12.5px/400** — “기기에 저장된 기록을 읽지 못했어요. 원본은 지우지 않고 그대로 두었어요.”
        `font-size:12.5px line-height:1.55 color:#475467 margin-top:6px`
      - `div`
        `display:flex flex-direction:column gap:8px width:100% margin-top:15px`
        - `div` **PrimaryButton(44)** — “원본을 파일로 저장”
          `display:flex align-items:center justify-content:center gap:6px height:44px width:100% border-radius:13px background:#3556E6 border:none color:#FFFFFF font-size:15px font-weight:600`
        - `div` **SecondaryButton(44)** — “백업으로 복구”
          `display:flex align-items:center justify-content:center gap:6px height:44px width:100% border-radius:13px background:#FFFFFF border:1px solid #D7DEEA color:#475467 font-size:15px font-weight:600`
        - `div` **text 15px/600** — “새로 시작”
          `display:flex align-items:center justify-content:center gap:6px height:44px width:100% border-radius:13px background:#E8ECF5 border:none color:#B4BECD font-size:15px font-weight:600`
        - `div` **text 11.5px/400** — “원본을 파일로 저장한 뒤에 새로 시작할 수 있어요”
          `font-size:11.5px line-height:1.45 color:#626D88 margin-top:-2px`
      - `span` **text 13px/600** — “다시 불러오기”
        `font-size:13px font-weight:600 color:#3556E6 margin-top:12px`
  - `div` **text 11px/600** — “B′ · 원본을 파일로 저장한 뒤”
    `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
  - `div` **Card(18)**
    `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:18px 16px`
    - `div`
      `display:flex flex-direction:column align-items:center text-align:center padding:6px 4px 2px`
      - `div`
        `width:44px height:44px border-radius:14px background:#FCEBEA display:flex align-items:center justify-content:center`
      - `div` **text 16px/700** — “저장된 기록을 불러오지 못했어요”
        `font-size:16px font-weight:700 letter-spacing:-0.02em color:#101828 margin-top:12px`
      - `div` **text 12.5px/400** — “기기에 저장된 기록을 읽지 못했어요. 원본은 지우지 않고 그대로 두었어요.”
        `font-size:12.5px line-height:1.55 color:#475467 margin-top:6px`
      - `div`
        `display:flex flex-direction:column gap:8px width:100% margin-top:15px`
        - `div` **PrimaryButton(44)** — “원본을 파일로 저장”
          `display:flex align-items:center justify-content:center gap:6px height:44px width:100% border-radius:13px background:#3556E6 border:none color:#FFFFFF font-size:15px font-weight:600`
        - `div` **text 12px/600** — “원본을 파일로 저장했어요”
          `font-size:12px font-weight:600 color:#0F7B47 margin-top:-2px`
        - `div` **SecondaryButton(44)** — “백업으로 복구”
          `display:flex align-items:center justify-content:center gap:6px height:44px width:100% border-radius:13px background:#FFFFFF border:1px solid #D7DEEA color:#475467 font-size:15px font-weight:600`
        - `div` **SecondaryButton(44)** — “새로 시작”
          `display:flex align-items:center justify-content:center gap:6px height:44px width:100% border-radius:13px background:#FFFFFF border:1px solid #D7DEEA color:#475467 font-size:15px font-weight:600`
      - `span` **text 13px/600** — “다시 불러오기”
        `font-size:13px font-weight:600 color:#3556E6 margin-top:12px`
  - `div` **text 11.5px/400** — “「새로 시작」을 누르면 한 번 더 묻습니다. 원본을 저장하지 못하면 주 버튼 아래에 빨간 줄이 한 번 뜹니다(rol”
    `font-size:11.5px line-height:1.5 color:#626D88 padding:0 4px`
  - `div` **Card(18)**
    `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:12px 14px`
    - `div`
      `display:flex flex-direction:column gap:8px`
      - `div` **PrimaryButton(44)** — “원본을 파일로 저장”
        `display:flex align-items:center justify-content:center gap:6px height:44px width:100% border-radius:13px background:#3556E6 border:none color:#FFFFFF font-size:15px font-weight:600`
      - `div` **text 12px/400** — “원본을 파일로 저장하지 못했습니다. 다시 눌러 보세요.”
        `font-size:12px line-height:1.45 color:#C0342F margin-top:-2px`
  - `div` **HeroCard**
    `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px box-shadow:0 16px 40px -18px rgba(16,24,40,.35)`
    - `div`
      `padding:20px 18px 16px text-align:center`
      - `div` **text 16px/700** — “새로 시작할까요?”
        `font-size:16px font-weight:700 letter-spacing:-0.02em line-height:1.4 color:#101828`
      - `div` **text 12.5px/400** — “저장해 둔 원본 파일은 그대로 있어요. 앱의 기록은 비우고 처음 설정부터 시작해요.”
        `font-size:12.5px line-height:1.55 color:#475467 margin-top:6px`
    - `div`
      `display:flex flex-direction:column gap:8px padding:12px 14px 14px background:#F4F6FB border-top:1px solid #E3E8F1`
      - `div` **PrimaryButton(44)** — “새로 시작”
        `display:flex align-items:center justify-content:center gap:6px height:44px width:100% border-radius:13px background:#3556E6 border:none color:#FFFFFF font-size:15px font-weight:600`
      - `div` **text 15px/600** — “취소”
        `display:flex align-items:center justify-content:center gap:6px height:44px width:100% border-radius:13px background:#E8ECF5 border:none color:#101828 font-size:15px font-weight:600`
  - `div` **text 11.5px/400** — “원본 저장에 두 번 실패한 뒤에는 확인 창이 빨간 쪽으로 바뀝니다.”
    `font-size:11.5px line-height:1.5 color:#626D88 padding:0 4px`
  - `div` **HeroCard**
    `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px box-shadow:0 16px 40px -18px rgba(16,24,40,.35)`
    - `div`
      `padding:20px 18px 16px text-align:center`
      - `div` **text 16px/700** — “새로 시작할까요?”
        `font-size:16px font-weight:700 letter-spacing:-0.02em line-height:1.4 color:#101828`
      - `div` **text 12.5px/400** — “원본을 파일로 저장하지 못했어요. 새로 시작하면 이 기기에 남은 기록은 되살릴 수 없어요.”
        `font-size:12.5px line-height:1.55 color:#475467 margin-top:6px`
    - `div`
      `display:flex flex-direction:column gap:8px padding:12px 14px 14px background:#F4F6FB border-top:1px solid #E3E8F1`
      - `div` **text 15px/600** — “그래도 새로 시작”
        `display:flex align-items:center justify-content:center gap:6px height:44px width:100% border-radius:13px background:#FCEBEA border:none color:#C0342F font-size:15px font-weight:600`
      - `div` **text 15px/600** — “취소”
        `display:flex align-items:center justify-content:center gap:6px height:44px width:100% border-radius:13px background:#E8ECF5 border:none color:#101828 font-size:15px font-weight:600`
  - `div` **text 11px/600** — “C · 백업 파일을 읽지 못함 — 같은 화면 안의 오류 줄”
    `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
  - `div` **Card(18)**
    `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:18px 16px`
    - `div`
      `display:flex flex-direction:column align-items:center text-align:center padding:6px 4px 2px`
      - `div`
        `width:44px height:44px border-radius:14px background:#FCEBEA display:flex align-items:center justify-content:center`
      - `div` **text 16px/700** — “저장된 기록을 불러오지 못했어요”
        `font-size:16px font-weight:700 letter-spacing:-0.02em color:#101828 margin-top:12px`
      - `div` **text 12.5px/400** — “기기에 저장된 기록을 읽지 못했어요. 원본은 지우지 않고 그대로 두었어요.”
        `font-size:12.5px line-height:1.55 color:#475467 margin-top:6px`
      - `div`
        `display:flex flex-direction:column gap:8px width:100% margin-top:15px`
        - `div` **PrimaryButton(44)** — “원본을 파일로 저장”
          `display:flex align-items:center justify-content:center gap:6px height:44px width:100% border-radius:13px background:#3556E6 border:none color:#FFFFFF font-size:15px font-weight:600`
        - `div` **SecondaryButton(44)** — “백업으로 복구”
          `display:flex align-items:center justify-content:center gap:6px height:44px width:100% border-radius:13px background:#FFFFFF border:1px solid #D7DEEA color:#475467 font-size:15px font-weight:600`
        - `div` **text 15px/600** — “새로 시작”
          `display:flex align-items:center justify-content:center gap:6px height:44px width:100% border-radius:13px background:#E8ECF5 border:none color:#B4BECD font-size:15px font-weight:600`
        - `div` **text 11.5px/400** — “원본을 파일로 저장한 뒤에 새로 시작할 수 있어요”
          `font-size:11.5px line-height:1.45 color:#626D88 margin-top:-2px`
      - `span` **text 13px/600** — “다시 불러오기”
        `font-size:13px font-weight:600 color:#3556E6 margin-top:12px`
      - `div`
        `width:100% margin-top:13px text-align:left`
        - `div` **text 12px/400** — “백업 파일을 읽지 못했습니다. NAVI 또는 자산 나침반의 JSON 백업을 골라 주세요. 지금 기록은 그대로예요.”
          `padding:10px 12px background:#FCEBEA border-radius:12px text-align:center font-size:12px line-height:1.5 color:#7C221E`
  - `div` **text 11.5px/400** — “읽을 수 있는 백업을 고르면 이 카드 아래에 「백업 불러오기」가 열립니다 — 「{파일} · 저장 전에 무엇이 바뀌는”
    `font-size:11.5px line-height:1.5 color:#626D88 padding:0 4px`
  - `div` **text 11px/600** — “D · 샘플에서 내 데이터로 전환”
    `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
  - `div` **HeroCard**
    `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px box-shadow:0 16px 40px -18px rgba(16,24,40,.35)`
    - `div`
      `padding:20px 18px 16px text-align:center`
      - `div` **text 16px/700** — “샘플을 치우고 내 데이터로 시작할까요?”
        `font-size:16px font-weight:700 letter-spacing:-0.02em line-height:1.4 color:#101828`
      - `div` **text 12.5px/400** — “지금 보는 샘플만 지워져요. 샘플은 백업되지 않아요.”
        `font-size:12.5px line-height:1.55 color:#475467 margin-top:6px`
    - `div`
      `display:flex flex-direction:column gap:8px padding:12px 14px 14px background:#F4F6FB border-top:1px solid #E3E8F1`
      - `div` **PrimaryButton(44)** — “내 데이터로 시작”
        `display:flex align-items:center justify-content:center gap:6px height:44px width:100% border-radius:13px background:#3556E6 border:none color:#FFFFFF font-size:15px font-weight:600`
      - `div` **text 15px/600** — “계속 둘러보기”
        `display:flex align-items:center justify-content:center gap:6px height:44px width:100% border-radius:13px background:#E8ECF5 border:none color:#101828 font-size:15px font-weight:600`
  - `div` **text 11.5px/400** — “샘플 모드 맨 위 띠 「샘플 데이터로 둘러보는 중 · 내 데이터로 시작 ›」에서 열립니다. 「내 데이터로 시작」을 ”
    `font-size:11.5px line-height:1.5 color:#626D88 padding:0 4px`
