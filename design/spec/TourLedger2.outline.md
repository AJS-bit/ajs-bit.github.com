# TourLedger2 — 블록 개요

원본 `canvas/TourLedger2.dc.html`. 값이 다르면 **원본이 맞습니다.**

- `div` **화면프레임**
  `width:390px height:844px background:#EDF0F7 color:#101828 display:flex flex-direction:column position:relative`
  - `div`
    `display:flex flex-direction:column gap:10px padding:14px 16px 12px`
    - `div`
      `display:flex align-items:center justify-content:space-between gap:8px`
      - `h1` **text 21px/700** — “소비”
        `font-size:21px font-weight:700 letter-spacing:-0.03em line-height:1.2 color:#101828`
      - `div`
        `display:flex align-items:center gap:8px`
        - `div`
          `display:flex align-items:center gap:2px height:34px padding:0 4px border-radius:10px background:#FFFFFF border:1px solid #E3E8F1`
        - `div` — “거래”
          `display:inline-flex align-items:center gap:3px height:34px padding:0 11px border-radius:10px background:#3556E6 color:#FFFFFF font-size:13px font-weight:600`
    - `div`
      `display:flex gap:4px background:#E3E8F1 border-radius:12px padding:3px`
      - `div` **SegmentedItem** — “이번 달”
        `flex:1 height:36px border-radius:9px display:flex align-items:center justify-content:center font-size:13.5px font-weight:500 color:#5B6880`
      - `div` **SegmentedItem** — “내역”
        `flex:1 height:36px border-radius:9px background:#FFFFFF display:flex align-items:center justify-content:center font-size:13.5px font-weight:600 color:#101828 box-shadow:0 1px 2px rgba(16,24,40,.06)`
      - `div` **SegmentedItem** — “한도”
        `flex:1 height:36px border-radius:9px display:flex align-items:center justify-content:center font-size:13.5px font-weight:500 color:#5B6880`
  - `div` **본문(스크롤 영역)**
    `flex:1 min-height:0 display:flex flex-direction:column gap:10px padding:0 14px`
    - `div` **Card(18)**
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:14px`
      - `div`
        `display:flex align-items:center gap:8px`
        - `div`
          `flex:1 display:flex align-items:center gap:9px height:40px padding:0 12px border-radius:11px background:#F4F6FB`
        - `div`
          `width:40px height:40px border-radius:11px border:1px solid #E3E8F1 display:flex align-items:center justify-content:center`
      - `div`
        `display:flex gap:5px margin-top:10px`
        - `div` **SampleBanner** — “전체 14건”
          `display:inline-flex align-items:center gap:4px height:32px padding:0 10px border-radius:99px background:#E9EDFD color:#3556E6 font-weight:600 font-size:12.5px white-space:nowrap`
        - `div` **text 12.5px/600** — “분류 안 함 7건”
          `display:inline-flex align-items:center gap:4px height:32px padding:0 10px border-radius:99px border:1px solid #E3E8F1 color:#101828 font-weight:600 font-size:12.5px white-space:nowrap`
        - `div` — “식비”
          `display:inline-flex align-items:center gap:4px height:32px padding:0 10px border-radius:99px border:1px solid #E3E8F1 color:#475467 font-weight:500 font-size:12.5px white-space:nowrap`
        - `div` **text 12.5px/500** — “더보기”
          `display:inline-flex align-items:center gap:4px height:32px padding:0 10px border-radius:99px border:1px solid #E3E8F1 color:#475467 font-weight:500 font-size:12.5px white-space:nowrap`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:8px margin-top:11px border-top:1px solid #EFF2F8`
        - `span` — “일반 소비”
          `font-size:12px color:#475467`
        - `span` **text 11.5px/400** — “이체 30만은 제외”
          `font-size:11.5px color:#626D88`
    - `div` **Card(18)**
      `background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:4px 14px 10px`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:10px padding:12px 0 6px`
        - `span` — “9월 8일”
          `font-size:13px font-weight:600 color:#101828 white-space:nowrap`
        - `span` **text 12.5px/600** — “소비 3.7만”
          `display:inline-flex align-items:center gap:5px font-size:12.5px font-weight:600 color:#475467 white-space:nowrap`
      - `div`
        `position:relative display:flex align-items:center gap:11px min-height:54px border-top:1px solid #F3F5FA`
        - `div`
          `width:34px height:34px border-radius:10px background:#d9770618 display:flex align-items:center justify-content:center`
        - `div`
          `flex:1`
        - `span` **text 14.5px/600** — “−4,500”
          `font-size:14.5px font-weight:600 letter-spacing:-0.02em color:#101828 white-space:nowrap`
        - `span`
          `display:inline-flex`
      - `div`
        `position:relative display:flex align-items:center gap:11px min-height:54px border-top:1px solid #F3F5FA`
        - `div`
          `width:34px height:34px border-radius:10px background:#f9731618 display:flex align-items:center justify-content:center`
        - `div`
          `flex:1`
        - `span` **text 14.5px/600** — “−9,000”
          `font-size:14.5px font-weight:600 letter-spacing:-0.02em color:#101828 white-space:nowrap`
        - `span`
          `display:inline-flex`
        - `div`
          `position:absolute right:0 top:40px background:#FFFFFF border:1px solid #E3E8F1 border-radius:13px padding:4px 0 box-shadow:0 1px 2px rgba(16,24,40,.04), 0 12px 28px -12px rgba(16,24,40,.32)`
      - `div`
        `position:relative display:flex align-items:center gap:11px min-height:54px border-top:1px solid #F3F5FA`
        - `div`
          `width:34px height:34px border-radius:10px background:#ec489918 display:flex align-items:center justify-content:center`
        - `div`
          `flex:1`
        - `span` **text 14.5px/600** — “−17,000”
          `font-size:14.5px font-weight:600 letter-spacing:-0.02em color:#101828 white-space:nowrap`
        - `span`
          `display:inline-flex`
      - `div`
        `position:relative display:flex align-items:center gap:11px min-height:54px border-top:1px solid #F3F5FA`
        - `div`
          `width:34px height:34px border-radius:10px background:#F4F6FB display:flex align-items:center justify-content:center`
        - `div`
          `flex:1`
        - `span` **text 14.5px/600** — “−6,500”
          `font-size:14.5px font-weight:600 letter-spacing:-0.02em color:#101828 white-space:nowrap`
        - `span`
          `display:inline-flex`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:10px padding:12px 0 6px`
        - `span` — “9월 6일”
          `font-size:13px font-weight:600 color:#101828 white-space:nowrap`
        - `span` **text 12.5px/600** — “이체 30만”
          `display:inline-flex align-items:center gap:5px font-size:12.5px font-weight:600 color:#475467 white-space:nowrap`
      - `div`
        `position:relative display:flex align-items:center gap:11px min-height:54px border-top:1px solid #F3F5FA`
        - `div`
          `width:34px height:34px border-radius:10px background:#34d17e18 display:flex align-items:center justify-content:center`
        - `div`
          `flex:1`
        - `span` **text 14.5px/600** — “−300,000”
          `font-size:14.5px font-weight:600 letter-spacing:-0.02em color:#475467 white-space:nowrap`
        - `span`
          `display:inline-flex`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:10px padding:12px 0 6px`
        - `span` — “9월 5일”
          `font-size:13px font-weight:600 color:#101828 white-space:nowrap`
        - `span` — “소비 1.2만”
          `display:inline-flex align-items:center gap:5px font-size:12.5px font-weight:600 color:#475467 white-space:nowrap`
      - `div`
        `position:relative display:flex align-items:center gap:11px min-height:54px border-top:1px solid #F3F5FA`
        - `div`
          `width:34px height:34px border-radius:10px background:#F4F6FB display:flex align-items:center justify-content:center`
        - `div`
          `flex:1`
        - `span` **text 14.5px/600** — “−4,500”
          `font-size:14.5px font-weight:600 letter-spacing:-0.02em color:#101828 white-space:nowrap`
        - `span`
          `display:inline-flex`
      - `div`
        `position:relative display:flex align-items:center gap:11px min-height:54px border-top:1px solid #F3F5FA`
        - `div`
          `width:34px height:34px border-radius:10px background:#F4F6FB display:flex align-items:center justify-content:center`
        - `div`
          `flex:1`
        - `span` **text 14.5px/600** — “−3,000”
          `font-size:14.5px font-weight:600 letter-spacing:-0.02em color:#101828 white-space:nowrap`
        - `span`
          `display:inline-flex`
      - `div`
        `position:relative display:flex align-items:center gap:11px min-height:54px border-top:1px solid #F3F5FA`
        - `div`
          `width:34px height:34px border-radius:10px background:#F4F6FB display:flex align-items:center justify-content:center`
        - `div`
          `flex:1`
        - `span` **text 14.5px/600** — “−4,500”
          `font-size:14.5px font-weight:600 letter-spacing:-0.02em color:#101828 white-space:nowrap`
        - `span`
          `display:inline-flex`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:10px padding:12px 0 6px`
        - `span` — “9월 4일”
          `font-size:13px font-weight:600 color:#101828 white-space:nowrap`
        - `span` — “소비 4,500”
          `display:inline-flex align-items:center gap:5px font-size:12.5px font-weight:600 color:#475467 white-space:nowrap`
      - `div`
        `position:relative display:flex align-items:center gap:11px min-height:54px border-top:1px solid #F3F5FA`
        - `div`
          `width:34px height:34px border-radius:10px background:#F4F6FB display:flex align-items:center justify-content:center`
        - `div`
          `flex:1`
        - `span` **text 14.5px/600** — “−4,500”
          `font-size:14.5px font-weight:600 letter-spacing:-0.02em color:#101828 white-space:nowrap`
        - `span`
          `display:inline-flex`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:10px padding:12px 0 6px`
        - `span` — “9월 3일”
          `font-size:13px font-weight:600 color:#101828 white-space:nowrap`
        - `span` **text 12.5px/600** — “소비 5.9만”
          `display:inline-flex align-items:center gap:5px font-size:12.5px font-weight:600 color:#475467 white-space:nowrap`
      - `div`
        `position:relative display:flex align-items:center gap:11px min-height:54px border-top:1px solid #F3F5FA`
        - `div`
          `width:34px height:34px border-radius:10px background:#0ea5e918 display:flex align-items:center justify-content:center`
        - `div`
          `flex:1`
        - `span` **text 14.5px/600** — “−45,000”
          `font-size:14.5px font-weight:600 letter-spacing:-0.02em color:#101828 white-space:nowrap`
        - `span`
          `display:inline-flex`
      - `div`
        `position:relative display:flex align-items:center gap:11px min-height:54px border-top:1px solid #F3F5FA`
        - `div`
          `width:34px height:34px border-radius:10px background:#f9731618 display:flex align-items:center justify-content:center`
        - `div`
          `flex:1`
        - `span` **text 14.5px/600** — “−9,000”
          `font-size:14.5px font-weight:600 letter-spacing:-0.02em color:#101828 white-space:nowrap`
        - `span`
          `display:inline-flex`
      - `div`
        `position:relative display:flex align-items:center gap:11px min-height:54px border-top:1px solid #F3F5FA`
        - `div`
          `width:34px height:34px border-radius:10px background:#F4F6FB display:flex align-items:center justify-content:center`
        - `div`
          `flex:1`
        - `span` **text 14.5px/600** — “−4,500”
          `font-size:14.5px font-weight:600 letter-spacing:-0.02em color:#101828 white-space:nowrap`
        - `span`
          `display:inline-flex`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:10px padding:12px 0 6px`
        - `span` — “9월 1일”
          `font-size:13px font-weight:600 color:#101828 white-space:nowrap`
        - `span` — “소비 1.2만”
          `display:inline-flex align-items:center gap:5px font-size:12.5px font-weight:600 color:#475467 white-space:nowrap`
      - `div`
        `position:relative display:flex align-items:center gap:11px min-height:54px border-top:1px solid #F3F5FA`
        - `div`
          `width:34px height:34px border-radius:10px background:#F4F6FB display:flex align-items:center justify-content:center`
        - `div`
          `flex:1`
        - `span` **text 14.5px/600** — “−4,500”
          `font-size:14.5px font-weight:600 letter-spacing:-0.02em color:#101828 white-space:nowrap`
        - `span`
          `display:inline-flex`
      - `div`
        `position:relative display:flex align-items:center gap:11px min-height:54px border-top:1px solid #F3F5FA`
        - `div`
          `width:34px height:34px border-radius:10px background:#f9731618 display:flex align-items:center justify-content:center`
        - `div`
          `flex:1`
        - `span` **text 14.5px/600** — “−7,500”
          `font-size:14.5px font-weight:600 letter-spacing:-0.02em color:#101828 white-space:nowrap`
        - `span`
          `display:inline-flex`
  - `div` **BottomNav**
    `display:flex align-items:flex-start justify-content:space-between gap:2px height:66px padding:8px 10px 0 background:#FFFFFF border-top:1px solid #E3E8F1`
    - `div`
      `display:flex flex-direction:column align-items:center gap:3px flex:1`
      - `div`
        `width:40px height:24px display:flex align-items:center justify-content:center`
      - `span` **text 11px/500** — “홈”
        `font-size:11px font-weight:500 color:#606B7D`
    - `div`
      `display:flex flex-direction:column align-items:center gap:3px flex:1`
      - `div`
        `width:40px height:24px display:flex align-items:center justify-content:center`
      - `span` **text 11px/500** — “자산”
        `font-size:11px font-weight:500 color:#606B7D`
    - `div`
      `display:flex flex-direction:column align-items:center gap:3px flex:1`
      - `div`
        `width:40px height:24px border-radius:99px background:#E9EDFD display:flex align-items:center justify-content:center`
      - `span` **text 11px/600** — “소비”
        `font-size:11px font-weight:600 color:#3556E6`
    - `div`
      `display:flex flex-direction:column align-items:center gap:3px flex:1`
      - `div`
        `width:40px height:24px display:flex align-items:center justify-content:center`
      - `span` **text 11px/500** — “목표”
        `font-size:11px font-weight:500 color:#606B7D`
    - `div`
      `display:flex flex-direction:column align-items:center gap:3px flex:1`
      - `div`
        `width:40px height:24px display:flex align-items:center justify-content:center`
      - `span` **text 11px/500** — “미래”
        `font-size:11px font-weight:500 color:#606B7D`
  - `div`
    `position:absolute inset:0`
    - `div`
      `position:absolute left:14px top:274px width:362px height:490px border-radius:18px box-shadow:0 0 0 2px rgba(255,255,255,.95), 0 0 0 4px #3556E6, 0 0 0 9999px rgba(16,24,40,.62)`
    - `div` **Card(18)**
      `position:absolute left:14px width:362px bottom:582px background:#FFFFFF border:1px solid #E3E8F1 border-radius:18px padding:16px display:flex flex-direction:column gap:8px box-shadow:0 12px 32px -12px rgba(16,24,40,.45)`
      - `div`
        `position:absolute bottom:-7px left:30px width:13px height:13px background:#FFFFFF transform:rotate(45deg) border-bottom:1px solid #E3E8F1`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:8px`
        - `span` — “처음 안내”
          `display:inline-flex align-items:center gap:5px height:22px padding:0 9px border-radius:99px background:#E9EDFD color:#3556E6 font-size:11.5px font-weight:700 letter-spacing:0.02em`
        - `span` **text 11.5px/600** — “내역 2 / 3”
          `font-size:11.5px font-weight:600 color:#626D88 white-space:nowrap`
      - `span` **text 16px/700** — “날짜별로 묶여요”
        `font-size:16px font-weight:700 letter-spacing:-0.02em line-height:1.35 color:#101828`
      - `span` **text 13px/400** — “날마다 소비 합계와 이체가 머리글에 있어요. 달력에서 저장한 기록도 여기 같이 쌓이고, 누르면 고칠 수 있어요.”
        `font-size:13px line-height:1.55 color:#475467`
      - `div`
        `display:flex align-items:center justify-content:space-between gap:8px margin-top:6px`
        - `span` **text 13px/600** — “건너뛰기”
          `font-size:13px font-weight:600 color:#626D88 padding:8px 4px`
        - `span` **text 14px/600** — “다음”
          `display:inline-flex align-items:center justify-content:center height:40px padding:0 20px border-radius:12px background:#3556E6 color:#FFFFFF font-size:14px font-weight:600 white-space:nowrap`
