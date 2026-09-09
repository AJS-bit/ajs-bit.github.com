# Confirmations — 블록 개요

원본 `canvas/Confirmations.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div`
  `width:390px height:1228px background:#EDF0F7 color:#101828 padding:18px 14px 20px display:flex flex-direction:column gap:8px`
  - `div`
    `padding:0 2px 6px`
    - `h2` **text 18px/700** — “삭제 · 초기화 확인”
      `font-size:18px font-weight:700 letter-spacing:-0.025em color:#101828`
    - `p` **text 12px/400** — “무엇이 함께 사라지는지 대상 이름과 영향을 항상 적습니다. 파괴적인 행동은 오른쪽, 취소는 왼쪽입니다.”
      `font-size:12px line-height:1.45 color:#626D88`
  - `div` **text 11px/600** — “A · 자산 삭제”
    `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
  - `div` **Card(20)**
    `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px`
    - `div`
      `display:flex gap:12px`
      - `div`
        `width:38px height:38px border-radius:12px background:#FCEBEA display:flex align-items:center justify-content:center`
      - `div`
        - `div` **text 15.5px/700** — “ETF 계좌를 삭제할까요?”
          `font-size:15.5px font-weight:700 letter-spacing:-0.02em color:#101828`
        - `div` — “평가액 4,890만원이 총자산에서 빠지고 순자산이 4,460만원이 됩니다. 이 계좌에 연결된 거래 12건은”
          `font-size:12.5px line-height:1.55 color:#475467 margin-top:5px`
    - `div`
      `display:flex gap:8px margin-top:14px`
      - `div` **SecondaryButton(44)** — “취소”
        `display:flex align-items:center justify-content:center gap:6px height:44px flex:1 border-radius:13px background:#FFFFFF border:1px solid #D7DEEA color:#475467 font-size:15px font-weight:600`
      - `div` **text 15px/600** — “삭제”
        `display:flex align-items:center justify-content:center gap:6px height:44px flex:1 border-radius:13px background:#FCEBEA border:none color:#C0342F font-size:15px font-weight:600`
  - `div` **text 11px/600** — “B · 거래 삭제 · 잔액 반영됨”
    `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
  - `div` **Card(20)**
    `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px`
    - `div`
      `display:flex gap:12px`
      - `div`
        `width:38px height:38px border-radius:12px background:#FCEBEA display:flex align-items:center justify-content:center`
      - `div`
        - `div` **text 15.5px/700** — “이 거래를 삭제할까요?”
          `font-size:15.5px font-weight:700 letter-spacing:-0.02em color:#101828`
        - `div` — “9월 5일 · ETF 자동이체 300,000원. 생활비 통장 잔액이 , ETF 계좌가 으로 되돌아갑니다.”
          `font-size:12.5px line-height:1.55 color:#475467 margin-top:5px`
    - `div`
      `display:flex gap:8px margin-top:14px`
      - `div` **SecondaryButton(44)** — “취소”
        `display:flex align-items:center justify-content:center gap:6px height:44px flex:1 border-radius:13px background:#FFFFFF border:1px solid #D7DEEA color:#475467 font-size:15px font-weight:600`
      - `div` **text 15px/600** — “삭제”
        `display:flex align-items:center justify-content:center gap:6px height:44px flex:1 border-radius:13px background:#FCEBEA border:none color:#C0342F font-size:15px font-weight:600`
  - `div` **text 11px/600** — “C · 목적지 삭제”
    `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
  - `div` **Card(20)**
    `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px`
    - `div`
      `display:flex gap:12px`
      - `div`
        `width:38px height:38px border-radius:12px background:#FCEBEA display:flex align-items:center justify-content:center`
      - `div`
        - `div` **text 15.5px/700** — “비상금 6개월을 삭제할까요?”
          `font-size:15.5px font-weight:700 letter-spacing:-0.02em color:#101828`
        - `div` — “적립한 1,020만원 기록은 자산에 그대로 남습니다. 홈 대표 목적지가 으로 바뀝니다.”
          `font-size:12.5px line-height:1.55 color:#475467 margin-top:5px`
    - `div`
      `display:flex gap:8px margin-top:14px`
      - `div` **SecondaryButton(44)** — “취소”
        `display:flex align-items:center justify-content:center gap:6px height:44px flex:1 border-radius:13px background:#FFFFFF border:1px solid #D7DEEA color:#475467 font-size:15px font-weight:600`
      - `div` **text 15px/600** — “삭제”
        `display:flex align-items:center justify-content:center gap:6px height:44px flex:1 border-radius:13px background:#FCEBEA border:none color:#C0342F font-size:15px font-weight:600`
  - `div` **text 11px/600** — “D · 반복 규칙 삭제”
    `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
  - `div` **Card(20)**
    `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px`
    - `div`
      `display:flex gap:12px`
      - `div` **Callout(warn)**
        `width:38px height:38px border-radius:12px background:#FDF1E0 display:flex align-items:center justify-content:center`
      - `div`
        - `div` **text 15.5px/700** — “ETF 자동이체 규칙을 삭제할까요?”
          `font-size:15.5px font-weight:700 letter-spacing:-0.02em color:#101828`
        - `div` **text 12.5px/400** — “앞으로 자동 생성되지 않습니다. 이미 만들어진 거래 8건은 남아요.”
          `font-size:12.5px line-height:1.55 color:#475467 margin-top:5px`
    - `div`
      `display:flex gap:8px margin-top:14px`
      - `div` **SecondaryButton(44)** — “취소”
        `display:flex align-items:center justify-content:center gap:6px height:44px flex:1 border-radius:13px background:#FFFFFF border:1px solid #D7DEEA color:#475467 font-size:15px font-weight:600`
      - `div` **PrimaryButton(44)** — “규칙만 삭제”
        `display:flex align-items:center justify-content:center gap:6px height:44px flex:1 border-radius:13px background:#3556E6 border:none color:#FFFFFF font-size:15px font-weight:600`
  - `div` **text 11px/600** — “E · 전체 초기화”
    `font-size:11px font-weight:600 letter-spacing:0.06em color:#606B7D padding:6px 2px 0`
  - `div` **Card(20)**
    `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px`
    - `div`
      `display:flex gap:12px`
      - `div`
        `width:38px height:38px border-radius:12px background:#FCEBEA display:flex align-items:center justify-content:center`
      - `div`
        - `div` **text 15.5px/700** — “모두 지우고 새로 시작할까요?”
          `font-size:15.5px font-weight:700 letter-spacing:-0.02em color:#101828`
        - `div` — “거래 132건 · 자산 5건 · 부채 4건 · 목적지 4건 · 월 마감 6건이 사라집니다.”
          `font-size:12.5px line-height:1.55 color:#475467 margin-top:5px`
    - `div`
      `margin-top:12px`
      - `div` **Callout(warn)**
        `display:flex gap:8px padding:10px 11px background:#FDF1E0 border-radius:12px`
        - `span`
          `margin-top:1px`
        - `span` **text 11.5px/400** — “먼저 백업을 내보내면 나중에 그대로 복구할 수 있어요.”
          `font-size:11.5px line-height:1.5 color:#7A3E0A`
    - `div`
      `margin-top:9px`
      - `div`
        `display:flex align-items:flex-start gap:9px`
        - `span`
          `width:20px height:20px border-radius:6px border:1.5px solid #CFD7E6`
        - `span` **text 12.5px/400** — “백업을 내보냈거나, 지워도 괜찮습니다.”
          `font-size:12.5px line-height:1.5 color:#475467`
    - `div`
      `display:flex gap:8px margin-top:14px`
      - `div` **SecondaryButton(44)** — “취소”
        `display:flex align-items:center justify-content:center gap:6px height:44px flex:1 border-radius:13px background:#FFFFFF border:1px solid #D7DEEA color:#475467 font-size:15px font-weight:600`
      - `div` **text 15px/600** — “모두 삭제”
        `display:flex align-items:center justify-content:center gap:6px height:44px flex:1 border-radius:13px background:#FCEBEA border:none color:#C0342F font-size:15px font-weight:600`
