# HeroFootnotes — 블록 개요

원본 `canvas/HeroFootnotes.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div`
  `width:1200px height:640px background:#EDF0F7 color:#101828 padding:28px 30px 30px display:flex flex-direction:column gap:10px`
  - `span` **text 11px/600** — “구현 참고 · 앱 화면이 아닙니다”
    `font-size:11px font-weight:600 letter-spacing:0.02em color:#475467 border:1px solid #E3E8F1 background:#FFFFFF border-radius:99px padding:4px 10px`
  - `h2` **text 20px/700** — “홈 맨 위 카드에 붙는 작은 안내 줄”
    `font-size:20px font-weight:700 letter-spacing:-0.025em color:#101828`
  - `p` **text 13px/400** — “예상 소비를 계산한 방식에 덧붙일 말이 있을 때만 기준 조정 줄 아래에 회색 글이 한두 줄 붙습니다.”
    `font-size:13px line-height:1.55 color:#626D88`
  - `div`
    `display:flex gap:32px align-items:flex-start`
    - `div`
      `width:362px display:flex flex-direction:column gap:8px`
      - `div` **HeroCard**
        `background:#FFFFFF border:1px solid #E3E8F1 border-radius:20px padding:16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
        - `div`
          `display:flex align-items:center justify-content:space-between gap:8px`
        - `div`
          `display:flex align-items:flex-end justify-content:space-between gap:10px margin-top:8px`
        - `div`
          `display:flex align-items:baseline justify-content:space-between gap:10px margin-top:5px`
        - `div`
          `margin-top:15px`
        - `div`
          `display:grid grid-template-columns:repeat(3, minmax(0, 1fr)) gap:0 margin-top:14px border-top:1px solid #EFF2F8`
        - `div`
          `display:flex align-items:center justify-content:space-between gap:10px margin-top:12px`
        - `div`
          `position:relative margin-top:4px border-radius:4px box-shadow:0 0 0 3px rgba(53,86,230,.16)`
      - `p` — “안내 줄은 에 붙습니다. 그림은 2번의 경우입니다.”
        `font-size:12px line-height:1.5 color:#626D88`
        - `b` — “기준 조정 줄 아래, 카드의 맨 끝”
          `font-weight:600 color:#475467`
    - `div`
      `flex:1 display:grid grid-template-columns:repeat(2, 362px) gap:24px 20px align-items:start`
      - `div`
        `display:flex flex-direction:column gap:8px`
        - `div`
        - `div`
          `background:#FFFFFF border:1px solid #E3E8F1 border-top:none border-radius:0 0 20px 20px padding:4px 16px 16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
      - `div`
        `display:flex flex-direction:column gap:8px`
        - `div`
        - `div`
          `background:#FFFFFF border:1px solid #E3E8F1 border-top:none border-radius:0 0 20px 20px padding:4px 16px 16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
      - `div`
        `display:flex flex-direction:column gap:8px`
        - `div`
        - `div`
          `background:#FFFFFF border:1px solid #E3E8F1 border-top:none border-radius:0 0 20px 20px padding:4px 16px 16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
      - `div`
        `display:flex flex-direction:column gap:8px`
        - `div`
        - `div`
          `background:#FFFFFF border:1px solid #E3E8F1 border-top:none border-radius:0 0 20px 20px padding:4px 16px 16px box-shadow:0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)`
  - `p` — “오른쪽 견본은 카드의 만 잘라 보여 줍니다. 카드의 나머지는 네 경우 모두 같고, 안내 줄이 붙은 만큼만 카드가 길”
    `font-size:12px line-height:1.6 color:#626D88`
    - `b` — “아랫부분”
      `font-weight:600 color:#475467`
