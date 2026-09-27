# Onboarding — 블록 개요

원본 `canvas/Onboarding.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div` **화면프레임**
  `width:390px height:844px background:#EDF0F7 color:#101828 display:flex flex-direction:column`
  - `div`
    `flex:1 min-height:0 display:flex flex-direction:column padding:0 20px`
    - `div`
      `display:flex align-items:center gap:8px height:56px margin-top:8px`
      - `span`
        `width:32px height:44px display:inline-flex align-items:center justify-content:center`
      - `div`
        `width:32px height:32px border-radius:10px background:linear-gradient(140deg, #3556E6 0%, #7A3FE4 100%) display:flex align-items:center justify-content:center`
      - `span` **text 12px/500** — “시작 방법 고르기”
        `font-size:12px font-weight:500 color:#626D88`
    - `h1` **text 22px/700** — “어떤 데이터로 시작할까요?”
      `font-size:22px font-weight:700 letter-spacing:-0.03em line-height:1.35 color:#101828`
    - `p` **text 13.5px/400** — “NAVI는 인터넷 없이 실행되고, 자산 · 소비 · 목적지를 이 기기에 암호화해 저장해요. 샘플은 기능을 둘러보는 ”
      `font-size:13.5px line-height:1.5 color:#475467`
    - `div`
      `display:flex flex-direction:column gap:10px margin-top:20px`
      - `div`
        `display:flex align-items:center gap:12px min-height:84px padding:16px border-radius:18px background:#3556E6 border:none`
        - `div`
          `width:40px height:40px border-radius:12px background:rgba(255,255,255,.18) display:flex align-items:center justify-content:center`
        - `div`
          `flex:1`
      - `div` **Card(18)**
        `display:flex align-items:center gap:12px min-height:84px padding:16px border-radius:18px background:#FFFFFF border:1px solid #E3E8F1`
        - `div` **Callout(info)**
          `width:40px height:40px border-radius:12px background:#F4F6FB display:flex align-items:center justify-content:center`
        - `div`
          `flex:1`
    - `div`
      `height:1px background:#E3E8F1`
    - `p` **text 13px/400** — “앱을 삭제하거나 앱 데이터를 지우면 기록도 사라져요. 기기를 바꾸기 전에 설정에서 백업 파일을 저장해 주세요.”
      `font-size:13px line-height:1.6 color:#626D88`
