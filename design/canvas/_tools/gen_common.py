# -*- coding: utf-8 -*-
"""NAVI v3 아트보드 공통 조각."""

C = dict(
    BG="#EDF0F7", SURF="#FFFFFF", INSET="#F4F6FB", TRACK="#E8ECF5",
    LINE="#E3E8F1", LINE_SOFT="#EFF2F8", LINE_ROW="#F3F5FA",
    INK="#101828", INK2="#475467", INK3="#6B7794", INK4="#98A4BC",
    DIS="#B4BECD", INPUT="#CFD7E6", BORDER="#D7DEEA", TAB_INK="#5B6880",
    BRAND="#3556E6", BRAND_SOFT="#E9EDFD", BRAND_BANNER="#3B4E8F",
    POS="#0F7B47", POS_SOFT="#E4F4EA",
    WARN="#B45309", WARN_SOFT="#FDF1E0", WARN_INK="#7A3E0A", WARN_RULE="#DE8A2A",
    NEG="#C0342F", NEG_SOFT="#FCEBEA",
    VIO="#7A3FE4", VIO_STRONG="#6B32D6", VIO_SOFT="#F1EAFD", VIO_LINE="#B79BFF",
    SKY="#0B7FBF", SKY_SOFT="#E4F2FB", SKY_INK="#0A5F8F",
)

CAT = {
    "식비": "#f97316", "카페/간식": "#d97706", "교통": "#0ea5e9", "주거/관리": "#8b5cf6",
    "통신": "#6366f1", "보험": "#0d9488", "구독": "#a855f7", "쇼핑": "#ec4899",
    "문화/여가": "#14b8a6", "의료/건강": "#22c55e", "교육": "#3b82f6", "경조사": "#f43f5e",
    "기타": "#64748b", "저축/투자": "#34d17e", "대출상환": "#94a3b8",
}
ASSET = {"현금성": "#38bdf8", "투자": "#5b8dff", "연금": "#8b5cf6", "부동산": "#f59e0b", "기타": "#64748b"}

_P = {
    "gear": '<circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 1 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 1 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 1 1-2.83-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 1 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 1 1 2.83-2.83l.06.06A1.65 1.65 0 0 0 9 4.6h.09A1.65 1.65 0 0 0 10.6 3.09V3a2 2 0 1 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 1 1 2.83 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 1 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1Z"/>',
    "chat": '<path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5Z"/>',
    "bell": '<path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"/><path d="M13.7 21a2 2 0 0 1-3.4 0"/>',
    "home": '<path d="m3 10 9-7 9 7v10a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2Z"/><path d="M9 22V12h6v10"/>',
    "wallet": '<path d="M19 7V5a2 2 0 0 0-2-2H5a2 2 0 0 0 0 4h15a1 1 0 0 1 1 1v3"/><path d="M3 5v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-3"/><path d="M18 12a2 2 0 0 0 0 4h3v-4Z"/>',
    "card": '<rect x="2" y="5" width="20" height="14" rx="2"/><path d="M2 10h20"/>',
    "target": '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.2"/>',
    "chart": '<path d="M3 3v18h18"/><path d="m7 14 4-4 3 3 5-6"/>',
    "right": '<path d="m9 18 6-6-6-6"/>', "left": '<path d="m15 18-6-6 6-6"/>',
    "down": '<path d="m6 9 6 6 6-6"/>', "up": '<path d="m18 15-6-6-6 6"/>',
    "plus": '<path d="M12 5v14M5 12h14"/>', "x": '<path d="M18 6 6 18M6 6l12 12"/>',
    "check": '<path d="M20 6 9 17l-5-5"/>',
    "warn": '<path d="M10.3 3.9 1.8 18a2 2 0 0 0 1.7 3h17a2 2 0 0 0 1.7-3L13.7 3.9a2 2 0 0 0-3.4 0Z"/><path d="M12 9v4M12 17h.01"/>',
    "info": '<circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/>',
    "help": '<circle cx="12" cy="12" r="10"/><path d="M9.1 9a3 3 0 0 1 5.8 1c0 2-3 3-3 3M12 17h.01"/>',
    "pencil": '<path d="M12 20h9"/><path d="M16.5 3.5a2.1 2.1 0 0 1 3 3L7 19l-4 1 1-4Z"/>',
    "trash": '<path d="M3 6h18M8 6V4a1 1 0 0 1 1-1h6a1 1 0 0 1 1 1v2M19 6l-1 14a2 2 0 0 1-2 2H8a2 2 0 0 1-2-2L5 6"/>',
    "refresh": '<path d="M3 12a9 9 0 1 0 3-6.7"/><path d="M3 3v6h6"/>',
    "refresh2": '<path d="M21 12a9 9 0 1 1-3-6.7"/><path d="M21 3v6h-6"/>',
    "search": '<circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/>',
    "cal": '<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/>',
    "lock": '<rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>',
    "arrowur": '<path d="M7 17 17 7"/><path d="M9 7h8v8"/>',
    "arrowr": '<path d="M5 12h14M13 6l6 6-6 6"/>',
    "arrowu": '<path d="M12 19V5M5 12l7-7 7 7"/>',
    "arrowd": '<path d="M12 5v14M5 12l7 7 7-7"/>',
    "pin": '<path d="M12 21s7-5.2 7-11a7 7 0 1 0-14 0c0 5.8 7 11 7 11Z"/><circle cx="12" cy="10" r="2.4"/>',
    "users": '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/>',
    "spark": '<path d="M12 2v4M12 18v4M4.9 4.9l2.9 2.9M16.2 16.2l2.9 2.9M2 12h4M18 12h4M4.9 19.1l2.9-2.9M16.2 7.8l2.9-2.9"/>',
    "more": '<circle cx="5" cy="12" r="1"/><circle cx="12" cy="12" r="1"/><circle cx="19" cy="12" r="1"/>',
    "shield": '<path d="M20 13c0 5-3.5 7.5-7.7 9a1 1 0 0 1-.6 0C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.2-2.7a1 1 0 0 1 1.5 0C14.5 3.8 17 5 19 5a1 1 0 0 1 1 1Z"/>',
    "download": '<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><path d="m7 10 5 5 5-5"/><path d="M12 15V3"/>',
    "upload": '<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><path d="m17 8-5-5-5 5"/><path d="M12 3v12"/>',
    "sliders": '<path d="M4 21v-7M4 10V3M12 21v-9M12 8V3M20 21v-5M20 12V3M1 14h6M9 8h6M17 16h6"/>',
    "repeat": '<path d="m17 2 4 4-4 4"/><path d="M3 11V9a4 4 0 0 1 4-4h14"/><path d="m7 22-4-4 4-4"/><path d="M21 13v2a4 4 0 0 1-4 4H3"/>',
    "loader": '<path d="M12 3a9 9 0 1 0 9 9"/>',
    "rice": '<path d="M3 2v7c0 1.1.9 2 2 2h2a2 2 0 0 0 2-2V2"/><path d="M6 2v20"/><path d="M18 2c-1.7 1-3 3.5-3 6.5 0 2 1 3.5 3 3.5v10"/>',
    "bag": '<path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4Z"/><path d="M3 6h18"/><path d="M16 10a4 4 0 0 1-8 0"/>',
    "bus": '<path d="M8 6v6M16 6v6M2 12h19.6"/><path d="M18 18h3s.5-1.7.8-2.8c.1-.4.2-.8.2-1.2v-4a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2v6c0 1 .8 2 2 2h1"/><circle cx="7" cy="18" r="2"/><circle cx="16" cy="18" r="2"/>',
    "house": '<path d="m3 10 9-7 9 7v10a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2Z"/>',
    "phone": '<rect x="5" y="2" width="14" height="20" rx="2"/><path d="M12 18h.01"/>',
    "leaf": '<path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.5 19 2c1 2 2 4.2 2 8 0 5.5-4.8 10-10 10Z"/><path d="M2 21c0-3 1.9-5.7 4.5-7"/>',
    "bank": '<path d="M3 21h18M4 10h16M5 10V6l7-4 7 4v4M6 21v-7M10 21v-7M14 21v-7M18 21v-7"/>',
    "coffee": '<path d="M17 8h1a4 4 0 1 1 0 8h-1"/><path d="M3 8h14v9a4 4 0 0 1-4 4H7a4 4 0 0 1-4-4Z"/><path d="M6 2v2M10 2v2M14 2v2"/>',
    "flag": '<path d="M4 15s1-1 4-1 5 2 8 2 4-1 4-1V4s-1 1-4 1-5-2-8-2-4 1-4 1Z"/><path d="M4 22v-7"/>',
}


def icon(name, size=18, stroke="#475467", w=1.8, fill="none"):
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="{fill}" stroke="{stroke}" '
            f'stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round">{_P[name]}</svg>')


HELMET = """<helmet>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+KR:wght@300;400;500;600;700&display=swap">
  <style>
    * { box-sizing: border-box; }
    body { margin: 0; font-family: 'IBM Plex Sans KR', 'Apple SD Gothic Neo', 'Noto Sans KR', system-ui, sans-serif; -webkit-font-smoothing: antialiased; }
    a { color: #3556E6; text-decoration: none; }
    a:hover { color: #2743C4; }
    text { font-family: 'IBM Plex Sans KR', system-ui, sans-serif; }
  </style>
</helmet>"""


def doc(body):
    return f"""<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <script src="./support.js"></script>
</head>
<body>
<x-dc>
{HELMET}

{body}
</x-dc>
</body>
</html>
"""


def frame(inner, h=844, w=390, bg=None):
    bg = bg or C["BG"]
    return (f'<div style="width: {w}px; height: {h}px; background: {bg}; color: {C["INK"]}; display: flex; '
            f'flex-direction: column; overflow: hidden; font-variant-numeric: tabular-nums;">\n{inner}\n</div>')


def topicons(badge=True, chat=False):
    out = ['<div style="display: flex; align-items: center; gap: 2px;">']
    out.append(f'<div style="width: 36px; height: 36px; border-radius: 11px; display: flex; align-items: center; justify-content: center;">{icon("gear", 19, C["INK2"], 1.7)}</div>')
    if chat:
        out.append(f'<div style="width: 36px; height: 36px; border-radius: 11px; display: flex; align-items: center; justify-content: center;">{icon("chat", 19, C["INK2"], 1.7)}</div>')
    b = (f'<span style="position: absolute; top: 4px; right: 4px; min-width: 15px; height: 15px; border-radius: 99px; '
         f'background: {C["NEG"]}; color: #FFFFFF; font-size: 10px; font-weight: 700; display: flex; align-items: center; '
         f'justify-content: center; padding: 0 4px; border: 2px solid {C["BG"]};">3</span>') if badge else ''
    out.append(f'<div style="width: 36px; height: 36px; border-radius: 11px; display: flex; align-items: center; justify-content: center; position: relative;">{icon("bell", 19, C["INK2"], 1.7)}{b}</div>')
    out.append('</div>')
    return "".join(out)


def screen_header(title, sub=None, tabs=None, active=0, trailing=None):
    """제목 + (부제/트레일링) + 서브탭."""
    left = f'<h1 style="margin: 0; font-size: 21px; font-weight: 700; letter-spacing: -0.03em; line-height: 1.2; color: {C["INK"]};">{title}</h1>'
    if sub:
        left = (f'<div style="display: flex; align-items: baseline; gap: 8px;">{left}'
                f'<span style="font-size: 12px; font-weight: 500; color: {C["INK3"]};">{sub}</span></div>')
    right = trailing if trailing is not None else topicons()
    rows = [f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px;">{left}{right}</div>']
    if tabs:
        cells = []
        for i, t in enumerate(tabs):
            if i == active:
                cells.append(f'<div style="flex: 1; height: 36px; border-radius: 9px; background: {C["SURF"]}; display: flex; align-items: center; justify-content: center; font-size: 13.5px; font-weight: 600; color: {C["INK"]}; box-shadow: 0 1px 2px rgba(16,24,40,.06);">{t}</div>')
            else:
                cells.append(f'<div style="flex: 1; height: 36px; border-radius: 9px; display: flex; align-items: center; justify-content: center; font-size: 13.5px; font-weight: 500; color: {C["TAB_INK"]};">{t}</div>')
        rows.append(f'<div style="display: flex; gap: 4px; background: {C["LINE"]}; border-radius: 12px; padding: 3px;">{"".join(cells)}</div>')
    return (f'<div style="display: flex; flex-direction: column; gap: 10px; padding: 14px 16px 12px; flex-shrink: 0;">'
            f'{"".join(rows)}</div>')


def month_stepper():
    return (f'<div style="display: flex; align-items: center; gap: 2px; height: 34px; padding: 0 4px; border-radius: 10px; '
            f'background: {C["SURF"]}; border: 1px solid {C["LINE"]};">{icon("left", 16, C["TAB_INK"], 2)}'
            f'<span style="font-size: 13px; font-weight: 600; color: {C["INK"]}; padding: 0 4px;">2026년 9월</span>'
            f'{icon("right", 16, "#C4CCDA", 2)}</div>')


def add_tx_button():
    return (f'<div style="display: inline-flex; align-items: center; gap: 3px; height: 34px; padding: 0 11px; border-radius: 10px; '
            f'background: {C["BRAND"]}; color: #FFFFFF; font-size: 13px; font-weight: 600;">{icon("plus", 14, "#FFFFFF", 2.4)}거래</div>')


NAV_ITEMS = [("home", "홈"), ("wallet", "자산"), ("card", "소비"), ("target", "목표"), ("chart", "미래")]


def bottomnav(active):
    cells = []
    for i, (ic, label) in enumerate(NAV_ITEMS):
        if i == active:
            cells.append(
                f'<div style="display: flex; flex-direction: column; align-items: center; gap: 3px; flex: 1; padding-top: 4px;">'
                f'<div style="width: 40px; height: 24px; border-radius: 99px; background: {C["BRAND_SOFT"]}; display: flex; align-items: center; justify-content: center;">{icon(ic, 18, C["BRAND"], 2)}</div>'
                f'<span style="font-size: 11px; font-weight: 600; color: {C["BRAND"]};">{label}</span></div>')
        else:
            cells.append(
                f'<div style="display: flex; flex-direction: column; align-items: center; gap: 3px; flex: 1; padding-top: 4px;">'
                f'<div style="width: 40px; height: 24px; display: flex; align-items: center; justify-content: center;">{icon(ic, 18, "#8593AD", 1.9)}</div>'
                f'<span style="font-size: 11px; font-weight: 500; color: #8593AD;">{label}</span></div>')
    return (f'<div style="display: flex; align-items: flex-start; justify-content: space-between; gap: 2px; height: 66px; '
            f'padding: 8px 10px 0; background: {C["SURF"]}; border-top: 1px solid {C["LINE"]}; flex-shrink: 0;">{"".join(cells)}</div>')


def content(cards, gap=10):
    return (f'<div style="flex: 1; min-height: 0; display: flex; flex-direction: column; gap: {gap}px; '
            f'padding: 0 14px; overflow: hidden;">{"".join(cards)}</div>')


# ---------- 카드 ----------
def hero(inner, pad=16):
    return (f'<div style="background: {C["SURF"]}; border: 1px solid {C["LINE"]}; border-radius: 20px; padding: {pad}px; '
            f'box-shadow: 0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24); flex-shrink: 0;">{inner}</div>')


def card(inner, pad="14px", radius=18, extra=""):
    return (f'<div style="background: {C["SURF"]}; border: 1px solid {C["LINE"]}; border-radius: {radius}px; '
            f'padding: {pad}; flex-shrink: 0; {extra}">{inner}</div>')


def guidance(tone, eyebrow, title, body, link=None):
    m = {"warn": (C["WARN"], C["WARN_SOFT"], C["WARN_RULE"], "arrowur"),
         "neg": (C["NEG"], C["NEG_SOFT"], "#D9827E", "warn"),
         "pos": (C["POS"], C["POS_SOFT"], "#6FBE94", "check"),
         "info": (C["SKY"], C["SKY_SOFT"], "#7EC4E8", "info")}
    col, soft, rule, ic = m[tone]
    lk = f'<span style="font-size: 12.5px; font-weight: 600; color: {C["BRAND"]}; margin-top: 5px;">{link} &rsaquo;</span>' if link else ''
    return (f'<div style="display: flex; gap: 12px; background: {C["SURF"]}; border: 1px solid {C["LINE"]}; '
            f'border-left: 3px solid {rule}; border-radius: 18px; padding: 13px 14px; flex-shrink: 0;">'
            f'<div style="width: 34px; height: 34px; border-radius: 11px; background: {soft}; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">{icon(ic, 18, col, 2)}</div>'
            f'<div style="display: flex; flex-direction: column; gap: 3px; min-width: 0;">'
            f'<span style="font-size: 11px; font-weight: 600; letter-spacing: 0.06em; color: {col};">{eyebrow}</span>'
            f'<span style="font-size: 15px; font-weight: 600; letter-spacing: -0.015em; line-height: 1.35; color: {C["INK"]};">{title}</span>'
            f'<span style="font-size: 12.5px; line-height: 1.45; color: {C["INK2"]};">{body}</span>{lk}</div></div>')


def eyebrow_row(text, right=""):
    return (f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px;">'
            f'<span style="font-size: 11px; font-weight: 600; letter-spacing: 0.07em; color: {C["INK3"]};">{text}</span>{right}</div>')


def badge(text, tone="brand", ic=None):
    m = {"brand": (C["BRAND"], C["BRAND_SOFT"]), "pos": (C["POS"], C["POS_SOFT"]),
         "warn": (C["WARN"], C["WARN_SOFT"]), "neg": (C["NEG"], C["NEG_SOFT"]),
         "vio": (C["VIO_STRONG"], C["VIO_SOFT"]), "sky": (C["SKY"], C["SKY_SOFT"]),
         "mute": (C["TAB_INK"], "#F0F2F7")}
    col, bg = m[tone]
    g = icon(ic, 11, col, 2.4) if ic else ''
    return (f'<span style="display: inline-flex; align-items: center; gap: 4px; background: {bg}; color: {col}; '
            f'font-size: 11.5px; font-weight: 600; border-radius: 99px; padding: 4px 9px;">{g}{text}</span>')


def bar(pct, color=None, h=8, track=None):
    color = color or C["BRAND"]
    track = track or C["TRACK"]
    return (f'<div style="position: relative; height: {h}px; border-radius: 99px; background: {track}; overflow: hidden;">'
            f'<div style="position: absolute; inset: 0 {100-pct:.4g}% 0 0; border-radius: 99px; background: {color};"></div></div>')


def btn(label, kind="primary", ic=None, h=46, full=True, radius=13, size=15):
    flex = "width: 100%;" if full else ""
    m = {
        "primary": (C["BRAND"], "#FFFFFF", "none"),
        "secondary": (C["SURF"], C["INK2"], f'1px solid {C["BORDER"]}'),
        "outline": (C["SURF"], C["BRAND"], f'1.5px solid {C["BRAND"]}'),
        "soft": (C["BRAND_SOFT"], C["BRAND"], "none"),
        "danger": (C["NEG_SOFT"], C["NEG"], "none"),
        "disabled": (C["TRACK"], C["DIS"], "none"),
    }
    bg, fg, bd = m[kind]
    g = icon(ic, 16, fg, 2.2) if ic else ''
    return (f'<div style="display: flex; align-items: center; justify-content: center; gap: 6px; height: {h}px; {flex} '
            f'border-radius: {radius}px; background: {bg}; border: {bd}; color: {fg}; font-size: {size}px; font-weight: 600;">{g}{label}</div>')


def smallbtn(label, kind="soft", ic=None, h=30):
    m = {"soft": (C["BRAND_SOFT"], C["BRAND"], "none"),
         "secondary": (C["SURF"], C["INK2"], f'1px solid {C["LINE"]}'),
         "danger": (C["NEG_SOFT"], C["NEG"], "none"),
         "primary": (C["BRAND"], "#FFFFFF", "none")}
    bg, fg, bd = m[kind]
    g = icon(ic, 13, fg, 2) if ic else ''
    return (f'<div style="display: inline-flex; align-items: center; gap: 4px; height: {h}px; padding: 0 11px; '
            f'border-radius: 9px; background: {bg}; border: {bd}; color: {fg}; font-size: 12.5px; font-weight: 600;">{g}{label}</div>')


def link(text):
    return f'<span style="font-size: 12.5px; font-weight: 600; color: {C["BRAND"]};">{text} &rsaquo;</span>'


def note(text, tone="mute", ic="info"):
    m = {"mute": (C["INSET"], C["INK3"], C["INK3"]), "warn": (C["WARN_SOFT"], C["WARN_INK"], C["WARN"]),
         "vio": (C["VIO_SOFT"], "#4E2496", C["VIO_STRONG"]), "sky": (C["SKY_SOFT"], C["SKY_INK"], C["SKY"]),
         "pos": (C["POS_SOFT"], "#14603D", C["POS"]), "neg": (C["NEG_SOFT"], "#7C221E", C["NEG"])}
    bg, fg, icol = m[tone]
    return (f'<div style="display: flex; gap: 8px; padding: 10px 11px; background: {bg}; border-radius: 12px;">'
            f'<span style="flex-shrink: 0; margin-top: 1px;">{icon(ic, 14, icol, 1.9)}</span>'
            f'<span style="font-size: 11.5px; line-height: 1.5; color: {fg};">{text}</span></div>')


def section_head(title, meta=None, right=""):
    m = f'<span style="font-size: 12px; color: {C["INK3"]};">{meta}</span>' if meta else ''
    return (f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px;">'
            f'<div style="display: flex; align-items: baseline; gap: 7px;">'
            f'<span style="font-size: 14px; font-weight: 600; color: {C["INK"]};">{title}</span>{m}</div>{right}</div>')


def field(label, value, unit=None, required=False, optional=False, state="default", helper=None, w=None, right_align=False):
    """입력 필드."""
    req = f' <span style="color: {C["NEG"]};">*</span>' if required else ''
    opt = f' <span style="font-weight: 500; color: {C["INK4"]};">선택</span>' if optional else ''
    bd, bg, fg, extra = f'1px solid {C["INPUT"]}', C["SURF"], C["INK"], ''
    if state == "focus":
        bd, extra = f'1.5px solid {C["BRAND"]}', 'box-shadow: 0 0 0 3px rgba(53,86,230,.16);'
    elif state == "error":
        bd = f'1.5px solid {C["NEG"]}'
    elif state == "readonly":
        bd, bg, fg = f'1px solid {C["LINE"]}', C["INSET"], C["INK4"]
    elif state == "auto":
        fg = C["DIS"]
    u = f'<span style="font-size: 13px; font-weight: 500; color: {C["INK3"]};">{unit}</span>' if unit else ''
    lock = icon("lock", 15, C["INK4"], 1.9) if state == "readonly" else ''
    align = 'text-align: right;' if (unit or right_align) else ''
    weight = 600 if (unit or right_align) else 400
    fsize = 17 if unit else 15
    hl = ''
    if helper:
        hc = C["NEG"] if state == "error" else C["INK3"]
        hi = f'{icon("warn", 13, C["NEG"], 2.2)}' if state == "error" else ''
        hl = (f'<div style="display: flex; align-items: center; gap: 5px; margin-top: 6px;">{hi}'
              f'<span style="font-size: 11.5px; color: {hc};">{helper}</span></div>')
    width = f'width: {w}px;' if w else 'flex: 1;'
    return (f'<div style="{width} min-width: 0;">'
            f'<div style="font-size: 12px; font-weight: 600; color: {C["INK2"]}; margin-bottom: 7px;">{label}{req}{opt}</div>'
            f'<div style="display: flex; align-items: center; gap: 5px; height: 46px; padding: 0 12px; border-radius: 11px; '
            f'border: {bd}; background: {bg}; {extra}">'
            f'<span style="flex: 1; {align} font-size: {fsize}px; font-weight: {weight}; color: {fg}; overflow: hidden; white-space: nowrap;">{value}</span>{u}{lock}</div>{hl}</div>')


def select_field(label, value, w=None, optional=False):
    opt = f' <span style="font-weight: 500; color: {C["INK4"]};">선택</span>' if optional else ''
    width = f'width: {w}px;' if w else 'flex: 1;'
    return (f'<div style="{width} min-width: 0;">'
            f'<div style="font-size: 12px; font-weight: 600; color: {C["INK2"]}; margin-bottom: 7px;">{label}{opt}</div>'
            f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px; height: 46px; padding: 0 12px; '
            f'border-radius: 11px; border: 1px solid {C["INPUT"]}; background: {C["SURF"]};">'
            f'<span style="font-size: 15px; font-weight: 500; color: {C["INK"]};">{value}</span>{icon("down", 16, C["INK4"], 2)}</div></div>')


def segmented(options, active=0, small=False):
    h = 32 if small else 36
    fs = 12.5 if small else 13
    cells = []
    for i, o in enumerate(options):
        if i == active:
            cells.append(f'<div style="flex: 1; height: {h}px; border-radius: 8px; background: {C["SURF"]}; display: flex; align-items: center; justify-content: center; font-size: {fs}px; font-weight: 600; color: {C["INK"]}; box-shadow: 0 1px 2px rgba(16,24,40,.08);">{o}</div>')
        else:
            cells.append(f'<div style="flex: 1; height: {h}px; border-radius: 8px; display: flex; align-items: center; justify-content: center; font-size: {fs}px; font-weight: 500; color: {C["TAB_INK"]};">{o}</div>')
    return f'<div style="display: flex; gap: 4px; background: {C["INSET"]}; border-radius: 11px; padding: 3px;">{"".join(cells)}</div>'


def toggle(on=True):
    if on:
        return (f'<div style="width: 46px; height: 27px; border-radius: 99px; background: {C["BRAND"]}; padding: 3px; '
                f'display: flex; justify-content: flex-end; flex-shrink: 0;"><span style="width: 21px; height: 21px; border-radius: 99px; background: #FFFFFF;"></span></div>')
    return (f'<div style="width: 46px; height: 27px; border-radius: 99px; background: {C["LINE"]}; padding: 3px; '
            f'display: flex; justify-content: flex-start; flex-shrink: 0;"><span style="width: 21px; height: 21px; border-radius: 99px; background: #FFFFFF;"></span></div>')


def slider(pct, color=None, h=22):
    color = color or C["BRAND"]
    k = h - 2
    return (f'<div style="position: relative; height: {h}px;">'
            f'<div style="position: absolute; left: 0; right: 0; top: {h//2-2}px; height: 5px; border-radius: 99px; background: {C["TRACK"]};"></div>'
            f'<div style="position: absolute; left: 0; width: {pct}%; top: {h//2-2}px; height: 5px; border-radius: 99px; background: {color};"></div>'
            f'<div style="position: absolute; left: {pct}%; top: 0; width: {k}px; height: {k}px; margin-left: -{k//2}px; border-radius: 99px; '
            f'background: #FFFFFF; border: 2.5px solid {color}; box-shadow: 0 2px 6px rgba(16,24,40,.2);"></div></div>')


def row(left, right, h=46, border_top=False, border_bottom=True, pad=""):
    bt = f'border-top: 1px solid {C["LINE_ROW"]};' if border_top else ''
    bb = f'border-bottom: 1px solid {C["LINE_ROW"]};' if border_bottom else ''
    return (f'<div style="display: flex; align-items: center; gap: 10px; min-height: {h}px; {bt}{bb}{pad}">{left}'
            f'<div style="margin-left: auto; display: flex; align-items: center; gap: 8px;">{right}</div></div>')


def amount(value, unit="만원", size=14.5, color=None, unit_size=11.5):
    color = color or C["INK"]
    return (f'<span style="font-size: {size}px; font-weight: 600; letter-spacing: -0.02em; color: {color};">{value}'
            f'<span style="font-size: {unit_size}px; font-weight: 500; color: {C["INK3"]};">{unit}</span></span>')


def display_num(value, unit="%", size=54, unit_size=25, color=None):
    color = color or C["INK"]
    return (f'<div style="display: flex; align-items: baseline; gap: 2px;">'
            f'<span style="font-size: {size}px; font-weight: 700; letter-spacing: -0.045em; line-height: 1; color: {color};">{value}</span>'
            f'<span style="font-size: {unit_size}px; font-weight: 600; letter-spacing: -0.02em; color: {C["INK2"]};">{unit}</span></div>')


def metric3(items):
    """[(label, value, unit, color)] 3개."""
    cells = []
    for i, (lab, val, unit, col) in enumerate(items):
        col = col or C["INK"]
        bl = f'border-left: 1px solid {C["LINE_SOFT"]};' if i else ''
        pad = 'padding-right: 10px;' if i == 0 else ('padding: 0 10px;' if i == 1 else 'padding-left: 10px;')
        cells.append(f'<div style="display: flex; flex-direction: column; gap: 3px; {pad}{bl}">'
                     f'<span style="font-size: 11.5px; font-weight: 500; color: {C["INK3"]};">{lab}</span>'
                     f'<span style="font-size: 18px; font-weight: 600; letter-spacing: -0.02em; color: {col};">{val}'
                     f'<span style="font-size: 13px; font-weight: 500; color: {C["INK2"] if col == C["INK"] else col};">{unit}</span></span></div>')
    return (f'<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 0; margin-top: 14px; '
            f'padding-top: 13px; border-top: 1px solid {C["LINE_SOFT"]};">{"".join(cells)}</div>')


def ring(pct, color, size=44, label=None):
    inner = size - 11
    label = label if label is not None else str(pct)
    fs = 11.5 if size < 50 else 13
    return (f'<div style="width: {size}px; height: {size}px; border-radius: 99px; background: conic-gradient({color} 0% {pct}%, {C["TRACK"]} {pct}% 100%); '
            f'display: flex; align-items: center; justify-content: center; flex-shrink: 0;">'
            f'<div style="width: {inner}px; height: {inner}px; border-radius: 99px; background: {C["SURF"]}; display: flex; align-items: center; '
            f'justify-content: center; font-size: {fs}px; font-weight: 700; color: {color};">{label}</div></div>')


def catdot(name, size=9):
    return f'<span style="width: {size}px; height: {size}px; border-radius: 3px; background: {CAT.get(name, ASSET.get(name, "#64748b"))}; flex-shrink: 0;"></span>'


def caticon(name, ic, size=30):
    col = CAT.get(name, ASSET.get(name, "#64748b"))
    return (f'<div style="width: {size}px; height: {size}px; border-radius: 10px; background: {col}18; display: flex; '
            f'align-items: center; justify-content: center; flex-shrink: 0;">{icon(ic, size // 2, col, 1.9)}</div>')


# ---------- 바텀시트 모달 ----------
def sheet(title, desc, body, footer, scrim_h=60, sticky=None, header_right=None):
    hr = header_right if header_right is not None else (
        f'<div style="width: 36px; height: 36px; border-radius: 11px; background: {C["INSET"]}; display: flex; '
        f'align-items: center; justify-content: center; flex-shrink: 0;">{icon("x", 17, C["INK2"], 2.2)}</div>')
    d = f'<p style="margin: 4px 0 0; font-size: 12.5px; line-height: 1.45; color: {C["INK3"]};">{desc}</p>' if desc else ''
    st = sticky or ''
    return frame(
        f'<div style="height: {scrim_h}px; display: flex; align-items: flex-end; justify-content: center; padding-bottom: 12px; flex-shrink: 0;">'
        f'<span style="font-size: 11.5px; font-weight: 500; color: rgba(255,255,255,.5);">배경을 눌러 닫기</span></div>'
        f'<div style="flex: 1; min-height: 0; background: {C["SURF"]}; border-radius: 26px 26px 0 0; display: flex; flex-direction: column; overflow: hidden; color: {C["INK"]};">'
        f'<div style="display: flex; justify-content: center; padding: 9px 0 0; flex-shrink: 0;">'
        f'<span style="width: 38px; height: 4px; border-radius: 99px; background: {C["BORDER"]};"></span></div>'
        f'<div style="display: flex; align-items: flex-start; justify-content: space-between; gap: 10px; padding: 12px 18px 14px; '
        f'border-bottom: 1px solid {C["LINE_SOFT"]}; flex-shrink: 0;"><div>'
        f'<h2 style="margin: 0; font-size: 18px; font-weight: 700; letter-spacing: -0.025em; color: {C["INK"]};">{title}</h2>{d}</div>{hr}</div>'
        f'<div style="flex: 1; min-height: 0; overflow: hidden; padding: 14px 18px 0; display: flex; flex-direction: column; gap: 15px;">{body}</div>'
        f'{st}'
        f'<div style="display: flex; gap: 10px; padding: 12px 18px 20px; border-top: 1px solid {C["LINE_SOFT"]}; flex-shrink: 0;">{footer}</div>'
        f'</div>',
        bg="#2A3245")


def sheet_footer(cancel="취소", save="저장", save_kind="primary"):
    return (btn(cancel, "secondary", h=48).replace('width: 100%;', 'flex: 1;') +
            btn(save, save_kind, h=48).replace('width: 100%;', 'flex: 1.4;'))


def state_sheet(title, desc, blocks, h=1360):
    """라벨 붙은 상태 카드 목록 아트보드."""
    out = [f'<div style="padding: 0 2px 6px;">'
           f'<h2 style="margin: 0; font-size: 18px; font-weight: 700; letter-spacing: -0.025em; color: {C["INK"]};">{title}</h2>'
           f'<p style="margin: 4px 0 0; font-size: 12px; line-height: 1.45; color: {C["INK3"]};">{desc}</p></div>']
    for label, block in blocks:
        out.append(f'<div style="font-size: 11px; font-weight: 600; letter-spacing: 0.06em; color: #8593AD; padding: 6px 2px 0;">{label}</div>')
        out.append(block)
    return (f'<div style="width: 390px; height: {h}px; background: {C["BG"]}; color: {C["INK"]}; padding: 18px 14px 20px; '
            f'display: flex; flex-direction: column; gap: 8px; overflow: hidden; font-variant-numeric: tabular-nums;">{"".join(out)}</div>')
