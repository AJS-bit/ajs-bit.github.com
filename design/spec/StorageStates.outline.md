# StorageStates — 블록 개요

원본 `canvas/StorageStates.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div`
  `width:390px height:1309px background:#EDF0F7 color:#101828 padding:18px 14px 20px display:flex flex-direction:column gap:8px`
  - `div`
    `padding:0 2px 6px`
    - `h2` **text 18px/700** — “저장소 로딩 · 실패 · 복구”
      `font-size:18px font-weight:700 letter-spacing:-0.025em color:#101828`
    - `p` **text 12px/400** — “기기 저장소를 읽지 못했을 때도 기존 기록을 덮어쓰지 않습니다. 복구는 항상 미리보기를 거칩니다.”
      `font-size:12px line-height:1.45 color:#626D88`
  - `div` **text 11px/600** — “A · 불러오는 중”
    `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
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
      `display:flex flex-direction:column align-items:center text-align:center padding:6px 4px`
      - `div`
        `width:48px height:48px border-radius:15px background:#FCEBEA display:flex align-items:center justify-content:center`
      - `div` **text 16px/700** — “기록을 불러오지 못했어요”
        `font-size:16px font-weight:700 letter-spacing:-0.02em color:#101828 margin-top:13px`
      - `div` **text 12.5px/400** — “기기 저장소를 읽을 수 없습니다. 기존 기록은 지워지지 않았으니 다시 시도하거나 백업 파일로 복구해 주세요.”
        `font-size:12.5px line-height:1.55 color:#475467 margin-top:6px`
      - `div`
        `width:100% margin-top:13px`
        - `div` **Callout(info)**
          `display:flex gap:8px padding:10px 11px background:#F4F6FB border-radius:12px`
      - `div`
        `display:flex gap:8px width:100% margin-top:15px`
        - `div` **PrimaryButton(44)** — “다시 불러오기”
          `display:flex align-items:center justify-content:center gap:6px height:44px flex:1 border-radius:13px background:#3556E6 border:none color:#FFFFFF font-size:15px font-weight:600`
        - `div` **SecondaryButton(44)** — “백업으로 복구”
          `display:flex align-items:center justify-content:center gap:6px height:44px flex:1 border-radius:13px background:#FFFFFF border:1px solid #D7DEEA color:#475467 font-size:15px font-weight:600`
  - `div` **text 11px/600** — “C · 복구 파일 오류”
    `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
  - `div` **Card(18)**
    `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:18px 16px`
    - `div`
      `display:flex flex-direction:column align-items:center text-align:center padding:6px 4px`
      - `div`
        `width:48px height:48px border-radius:15px background:#FCEBEA display:flex align-items:center justify-content:center`
      - `div` **text 16px/700** — “이 파일은 읽을 수 없어요”
        `font-size:16px font-weight:700 letter-spacing:-0.02em color:#101828 margin-top:13px`
      - `div` **text 12.5px/400** — “NAVI 백업 형식이 아니거나 파일이 손상됐습니다. 현재 기록은 그대로입니다.”
        `font-size:12.5px line-height:1.55 color:#475467 margin-top:6px`
      - `div`
        `width:100% margin-top:13px`
        - `div`
          `display:flex gap:8px padding:10px 11px background:#FCEBEA border-radius:12px`
      - `div`
        `display:flex gap:8px width:100% margin-top:15px`
        - `div` **PrimaryButton(44)** — “다른 파일 선택”
          `display:flex align-items:center justify-content:center gap:6px height:44px flex:1 border-radius:13px background:#3556E6 border:none color:#FFFFFF font-size:15px font-weight:600`
        - `div` **SecondaryButton(44)** — “취소”
          `display:flex align-items:center justify-content:center gap:6px height:44px flex:1 border-radius:13px background:#FFFFFF border:1px solid #D7DEEA color:#475467 font-size:15px font-weight:600`
  - `div` **text 11px/600** — “D · 샘플에서 내 데이터로 전환”
    `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
  - `div` **Card(18)**
    `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:18px 16px`
    - `div`
      `display:flex flex-direction:column align-items:center text-align:center padding:6px 4px`
      - `div`
        `width:48px height:48px border-radius:15px background:#E9EDFD display:flex align-items:center justify-content:center`
      - `div` **text 16px/700** — “내 데이터로 시작할까요?”
        `font-size:16px font-weight:700 letter-spacing:-0.02em color:#101828 margin-top:13px`
      - `div` **text 12.5px/400** — “샘플 기록은 모두 지워지고 빈 상태에서 시작합니다. 샘플은 백업되지 않아요.”
        `font-size:12.5px line-height:1.55 color:#475467 margin-top:6px`
      - `div`
        `display:flex gap:8px width:100% margin-top:15px`
        - `div` **PrimaryButton(44)** — “내 데이터로 시작”
          `display:flex align-items:center justify-content:center gap:6px height:44px flex:1 border-radius:13px background:#3556E6 border:none color:#FFFFFF font-size:15px font-weight:600`
        - `div` **SecondaryButton(44)** — “계속 둘러보기”
          `display:flex align-items:center justify-content:center gap:6px height:44px flex:1 border-radius:13px background:#FFFFFF border:1px solid #D7DEEA color:#475467 font-size:15px font-weight:600`
