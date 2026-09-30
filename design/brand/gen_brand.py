# -*- coding: utf-8 -*-
"""NAVI 로고 파일 묶음 — 2026-09-30 사용자 결정 「클로드 C2로 가자」(하루가 쌓인 길).

그림 규격은 `design/canvas/_tools/brand_mark.py` 하나에서 가져온다(시안 장의 마크와 같은 좌표 · 같은 두께).
바탕은 파랑 → 보라 대각선(#3556E6 → #7A3FE4 · 지금 앱 아이콘 · 시안 마크 네모와 같은 색).

비율 — **어디서나 보이는 아이콘 한 변의 54%**(2026-09-30 둘째 결정 「54%로 가고 앱 아이콘도 똑같이 통일」 · brand_mark.RATIO).
- 적응형 전경: 108dp 층 중 가운데 72dp만 보이므로 그림을 가운데 기준 `FG_SCALE`(= 0.54 × 72 ÷ 49)배 — 108 좌표에서 34.56 ~ 73.44,
  가장 먼 점(왼쪽 아래 칸 모서리)이 가운데에서 26.3칸이라 안전 원(반지름 33) 안.
- 108 전체가 보이는 것(웹 아이콘 · 26 미만 벡터 · PNG): `TILE_SCALE`(= 0.54 × 108 ÷ 49)배. 26 미만 런처 벡터 둘은
  `android/mipmap-anydpi/`(앱 res/mipmap-anydpi 의 ic_launcher_navi.xml · ic_launcher_round_navi.xml 과 같은 바이트 — legacy_launcher).
- 시작 화면(안드로이드 12+)은 따로 그리지 않고 적응형 아이콘을 그대로 쓴다(앱 styles.xml · 밝은 바탕 / 어두운 모드는 어두운 바탕).

    python3 gen_brand.py      # → design/brand/ 아래 svg · android · png
"""
import math, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'canvas' / '_tools'))
import brand_mark as bm                       # noqa: E402

BLUE, VIOLET = '#3556E6', '#7A3FE4'
FG_SCALE = bm.RATIO * 72 / 49                 # 적응형 전경 — 보이는 72dp 안에서 54%
TILE_SCALE = bm.RATIO * 108 / 49               # 108 전체가 보이는 아이콘 — 54%
GRAD = (f'<defs><linearGradient id="navi-bg" x1="0" y1="0" x2="1" y2="1">'
        f'<stop offset="0" stop-color="{BLUE}"/><stop offset="1" stop-color="{VIOLET}"/></linearGradient></defs>')


def scaled(inner, s):
    """가운데(54, 54) 기준으로 s 배."""
    return f'<g transform="translate(54 54) scale({s:.6g}) translate(-54 -54)">{inner}</g>'


# ── SVG ──────────────────────────────────────────────────────────────────────────────
def svg_files():
    out = {}
    X = 'xmlns="http://www.w3.org/2000/svg"'
    # 그림만(투명 바탕 · 파랑) — 문서 · 워드마크용. 그림 테두리에 딱 맞춘 viewBox
    out['svg/navi-symbol.svg'] = f'<svg {X} viewBox="29.5 29.5 49 49"><title>NAVI</title>{bm.symbol(BLUE)}</svg>'
    out['svg/navi-symbol-white.svg'] = f'<svg {X} viewBox="29.5 29.5 49 49"><title>NAVI</title>{bm.symbol("#FFFFFF")}</svg>'
    # 앱 아이콘(모서리 둥근 네모 · 웹) — 108 전체가 보이는 아이콘, 그림 54%
    out['svg/navi-icon.svg'] = (f'<svg {X} viewBox="0 0 108 108"><title>NAVI</title>{GRAD}'
                                f'<rect width="108" height="108" rx="27" fill="url(#navi-bg)"/>{scaled(bm.symbol("#FFFFFF"), TILE_SCALE)}</svg>')
    # 스토어 · 마스크 적용 전(네모 꽉 채움)
    out['svg/navi-icon-square.svg'] = (f'<svg {X} viewBox="0 0 108 108"><title>NAVI</title>{GRAD}'
                                       f'<rect width="108" height="108" fill="url(#navi-bg)"/>{scaled(bm.symbol("#FFFFFF"), TILE_SCALE)}</svg>')
    # 안드로이드 적응형 층(108 좌표 · 가운데 72만 보임)
    out['svg/adaptive-foreground.svg'] = f'<svg {X} viewBox="0 0 108 108">{scaled(bm.symbol("#FFFFFF"), FG_SCALE)}</svg>'
    out['svg/adaptive-background.svg'] = f'<svg {X} viewBox="0 0 108 108">{GRAD}<rect width="108" height="108" fill="url(#navi-bg)"/></svg>'
    out['svg/adaptive-monochrome.svg'] = f'<svg {X} viewBox="0 0 108 108">{scaled(bm.symbol("#000000", mono=True), FG_SCALE)}</svg>'
    # 알림 작은 아이콘(24 · 흰 단색 · 점과 원 선을 조금 굵게)
    out['svg/notification-24.svg'] = f'<svg {X} width="24" height="24" viewBox="18 18 72 72">{bm.symbol("#FFFFFF", mono=True)}</svg>'
    return out


# ── 안드로이드 벡터 드로어블 ───────────────────────────────────────────────────────────
def _num(v):
    return f'{v:.3f}'.rstrip('0').rstrip('.')


def _js(v):
    """자바스크립트 String(number) 와 같은 쓰는 법 — 정수는 소수점 없이, 아니면 되돌려 읽을 수 있는 가장 짧은 자릿수(26 미만 런처의 바탕 path)."""
    v = float(v)
    return str(int(v)) if v.is_integer() else repr(v)


def _rrect(x, y, w, h, r, num=_num):
    return (f'M{num(x + r)},{num(y)}H{num(x + w - r)}A{num(r)},{num(r)} 0 0 1 {num(x + w)},{num(y + r)}'
            f'V{num(y + h - r)}A{num(r)},{num(r)} 0 0 1 {num(x + w - r)},{num(y + h)}'
            f'H{num(x + r)}A{num(r)},{num(r)} 0 0 1 {num(x)},{num(y + h - r)}'
            f'V{num(y + r)}A{num(r)},{num(r)} 0 0 1 {num(x + r)},{num(y)}Z')


def _circle(cx, cy, r):
    return f'M{_num(cx - r)},{_num(cy)}A{_num(r)},{_num(r)} 0 1 0 {_num(cx + r)},{_num(cy)}A{_num(r)},{_num(r)} 0 1 0 {_num(cx - r)},{_num(cy)}Z'


def shapes(mono=False, s=1.0, c=54.0):
    """그림을 (채움 path, 선 path, 선 두께) 로 — 가운데 c 기준 s 배."""
    T = lambda v: c + (v - c) * s
    fills = []
    for rc in bm.PATH:
        x, y = bm._xy(rc)
        fills.append(_rrect(T(x), T(y), bm.CELL * s, bm.CELL * s, 3.6 * s))
    for rc in bm.EMPTY:
        x, y = bm._xy(rc)
        fills.append(_circle(T(x + bm.CELL / 2), T(y + bm.CELL / 2), (3.0 if mono else 2.3) * s))
    sw = 3.6 if mono else 3.4
    x, y = bm._xy(bm.DEST)
    ring = _circle(T(x + bm.CELL / 2), T(y + bm.CELL / 2), (bm.CELL / 2 + 0.6 - sw / 2) * s)
    return ''.join(fills), ring, sw * s


def vector(size_dp, viewport, fill_color, mono=False, s=1.0, c=54.0, tint=None):
    fills, ring, sw = shapes(mono, s, c)
    vx, vy, vw, vh = viewport
    group = f'<group android:translateX="{_num(-vx)}" android:translateY="{_num(-vy)}">' if (vx or vy) else '<group>'
    t = f'\n    android:tint="{tint}"' if tint else ''
    return (f'<?xml version="1.0" encoding="utf-8"?>\n'
            f'<!-- NAVI 「하루가 쌓인 길」 — design/brand/gen_brand.py 가 만든다. 손으로 고치지 말 것 -->\n'
            f'<vector xmlns:android="http://schemas.android.com/apk/res/android"\n'
            f'    android:width="{size_dp}dp" android:height="{size_dp}dp"\n'
            f'    android:viewportWidth="{_num(vw)}" android:viewportHeight="{_num(vh)}"{t}>\n'
            f'  {group}\n'
            f'    <path android:fillColor="{fill_color}" android:pathData="{fills}"/>\n'
            f'    <path android:fillColor="#00000000" android:strokeColor="{fill_color}" android:strokeWidth="{_num(sw)}" android:pathData="{ring}"/>\n'
            f'  </group>\n</vector>\n')


def background_vector():
    return ('<?xml version="1.0" encoding="utf-8"?>\n'
            '<!-- NAVI 아이콘 바탕 — 파랑 → 보라 대각선. design/brand/gen_brand.py -->\n'
            '<vector xmlns:android="http://schemas.android.com/apk/res/android"\n'
            '    xmlns:aapt="http://schemas.android.com/aapt"\n'
            '    android:width="108dp" android:height="108dp" android:viewportWidth="108" android:viewportHeight="108">\n'
            '  <path android:pathData="M0,0h108v108h-108z">\n'
            '    <aapt:attr name="android:fillColor">\n'
            '      <gradient android:type="linear" android:startX="0" android:startY="0" android:endX="108" android:endY="108">\n'
            f'        <item android:offset="0" android:color="#FF{BLUE[1:]}"/>\n'
            f'        <item android:offset="1" android:color="#FF{VIOLET[1:]}"/>\n'
            '      </gradient>\n    </aapt:attr>\n  </path>\n</vector>\n')


def _css_gradient_line(deg, w=108, h=108):
    """CSS linear-gradient(deg) 의 시작 · 끝 점을 w × h 칸 좌표로(안드로이드 gradient startX … endY) — 앱 안 마크 네모의 140deg 와 같은 방향."""
    a = math.radians(deg)
    dx, dy = math.sin(a), -math.cos(a)
    half = (abs(w * math.sin(a)) + abs(h * math.cos(a))) / 2
    return w / 2 - dx * half, h / 2 - dy * half, w / 2 + dx * half, h / 2 + dy * half


# 26 미만 런처(적응형 아이콘이 없는 안드로이드 7.x) — 108 전체가 보여 그림은 TILE_SCALE(보이는 네모의 54%).
# 앱 android/app/src/main/res/mipmap-anydpi/ic_launcher_navi.xml · ic_launcher_round_navi.xml 에 같은 이름 · 같은 바이트로 들어간다
# (이 폴더의 android/mipmap-anydpi/ 두 파일). 바탕 모양 · 색은 앱 파일에 전부터 있던 그대로 — 모서리 둥근 네모(모서리 108 × 18 ÷ 56 · 옛 56 칸 네모의 18) ·
# 원(반지름 54) · 140deg 파랑 → 보라(앱 안 마크 네모와 같은 각을 108 칸에 옮긴 시작 · 끝 점 · 소수 여섯 자리). 숫자 쓰는 법도 그 파일 그대로
# (바탕 path 는 자바스크립트 숫자 글자 · 그림 path 는 이 파일의 _num 세 자리).
LEGACY_RADIUS = 108 * 18 / 56                    # 34.714285714285715
LEGACY_NOTE = ('Pre-26 shows the whole 108dp tile: the symbol is 54% of it, the same ratio as every NAVI icon '
               '(design/brand/gen_brand.py TILE_SCALE).')


def legacy_launcher(shape):
    """26 미만 런처 벡터 — shape 'square'(모서리 둥근 네모 · ic_launcher_navi) · 'round'(원 · ic_launcher_round_navi)."""
    if shape == 'round':
        c, r = 54, 54
        bg = f'M{_js(c)},{_js(c - r)}A{_js(r)},{_js(r)} 0 1 1 {_js(c)},{_js(c + r)}A{_js(r)},{_js(r)} 0 1 1 {_js(c)},{_js(c - r)}Z'
    else:
        bg = _rrect(0, 0, 108, 108, LEGACY_RADIUS, num=_js)
    x1, y1, x2, y2 = _css_gradient_line(140)
    grad = (f'<aapt:attr name="android:fillColor"><gradient android:type="linear" android:startX="{x1:.6f}" android:startY="{y1:.6f}" '
            f'android:endX="{x2:.6f}" android:endY="{y2:.6f}"><item android:offset="0" android:color="{BLUE}"/>'
            f'<item android:offset="1" android:color="{VIOLET}"/></gradient></aapt:attr>')
    fills, ring, sw = shapes(False, TILE_SCALE)
    return ('<?xml version="1.0" encoding="utf-8"?>\n'
            '<vector xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt" '
            'android:width="108dp" android:height="108dp" android:viewportWidth="108" android:viewportHeight="108">\n'
            f'    <path android:pathData="{bg}">{grad}</path>\n'
            f'    <!-- {LEGACY_NOTE} -->\n'
            f'    <path android:fillColor="#FFFFFF" android:pathData="{fills}"/>\n'
            f'    <path android:fillColor="#00000000" android:strokeColor="#FFFFFF" android:strokeWidth="{_num(sw)}" android:pathData="{ring}"/>\n'
            '</vector>\n')


def android_files():
    return {
        'android/ic_launcher_foreground.xml': vector(108, (0, 0, 108, 108), '#FFFFFFFF', s=FG_SCALE),
        'android/ic_launcher_monochrome.xml': vector(108, (0, 0, 108, 108), '#FF000000', mono=True, s=FG_SCALE),
        'android/ic_launcher_background.xml': background_vector(),
        # 알림 작은 아이콘 — 24dp 에 보이는 칸 18 ~ 90(72) 을 꽉 채움 · 흰 단색(색은 시스템이 입힘)
        'android/ic_stat_navi.xml': vector(24, (18, 18, 72, 72), '#FFFFFFFF', mono=True),
        # 26 미만 런처 — 앱 res/mipmap-anydpi 에 같은 이름으로(위 legacy_launcher)
        'android/mipmap-anydpi/ic_launcher_navi.xml': legacy_launcher('square'),
        'android/mipmap-anydpi/ic_launcher_round_navi.xml': legacy_launcher('round'),
    }


# ── PNG (PIL · 8배로 그려 줄임) ──────────────────────────────────────────────────────
def png(size, kind):
    """kind: 'icon'(둥근 네모 · 웹 · 레거시 런처) · 'round'(원) · 'square'(꽉 참 · 스토어) · 'notify'(흰 단색 · 투명)
    · 'fg'(적응형 전경 PNG — 투명 바탕에 흰 그림 × FG_SCALE)."""
    if kind == 'fg':
        from PIL import Image
        big = png(round(size * FG_SCALE), 'notify_plain')
        im = Image.new('RGBA', (size, size), (0, 0, 0, 0))
        off = (size - big.width) // 2
        im.paste(big, (off, off), big)
        return im
    from PIL import Image, ImageDraw
    K = 8
    S = size * K
    k = S / 108

    def lerp(a, b, t):
        return tuple(round(int(a[i:i + 2], 16) + (int(b[i:i + 2], 16) - int(a[i:i + 2], 16)) * t) for i in (1, 3, 5))

    if kind == 'notify':
        im = Image.new('RGBA', (S, S), (0, 0, 0, 0))
        view, off, mono = 72, 18, True
    elif kind == 'notify_plain':          # 108 전체 칸 · 보통 두께 · 투명(전경 PNG 의 재료)
        im = Image.new('RGBA', (S, S), (0, 0, 0, 0))
        view, off, mono = 108, 0, False
    else:
        # 대각선 그라디언트: t = (x + y) / (2S)
        row = Image.new('RGB', (2 * S, 1))
        row.putdata([lerp(BLUE, VIOLET, i / (2 * S - 1)) for i in range(2 * S)])
        im = Image.new('RGBA', (S, S))
        for y in range(S):
            im.paste(row.crop((y, 0, y + S, 1)), (0, y))
        mask = Image.new('L', (S, S), 0)
        d = ImageDraw.Draw(mask)
        if kind == 'icon':
            d.rounded_rectangle((0, 0, S - 1, S - 1), radius=27 * k, fill=255)
        elif kind == 'round':
            d.ellipse((0, 0, S - 1, S - 1), fill=255)
        else:
            d.rectangle((0, 0, S, S), fill=255)
        im.putalpha(mask)
        view, off, mono = 108, 0, False
    k = S / view
    sym = TILE_SCALE if kind in ('icon', 'round', 'square') else 1.0
    P = lambda v: (54 + (v - 54) * sym - off) * k
    d = ImageDraw.Draw(im)
    white = (255, 255, 255, 255)
    for rc in bm.PATH:
        x, y = bm._xy(rc)
        d.rounded_rectangle((P(x), P(y), P(x + bm.CELL), P(y + bm.CELL)), radius=3.6 * k * sym, fill=white)
    for rc in bm.EMPTY:
        x, y = bm._xy(rc)
        r = 3.0 if mono else 2.3
        cx, cy = x + bm.CELL / 2, y + bm.CELL / 2
        d.ellipse((P(cx) - r * sym * k, P(cy) - r * sym * k, P(cx) + r * sym * k, P(cy) + r * sym * k), fill=white)
    sw = 3.6 if mono else 3.4
    x, y = bm._xy(bm.DEST)
    cx, cy, r = x + bm.CELL / 2, y + bm.CELL / 2, bm.CELL / 2 + 0.6 - sw / 2
    ro, ri = r + sw / 2, r - sw / 2
    ring = Image.new('L', (S, S), 0)
    rd = ImageDraw.Draw(ring)
    ro, ri = ro * sym * k, ri * sym * k
    rd.ellipse((P(cx) - ro, P(cy) - ro, P(cx) + ro, P(cy) + ro), fill=255)
    rd.ellipse((P(cx) - ri, P(cy) - ri, P(cx) + ri, P(cy) + ri), fill=0)
    im.paste(Image.new('RGBA', (S, S), white), (0, 0), ring)
    if kind not in ('notify', 'notify_plain'):
        im.putalpha(Image.composite(im.getchannel('A'), Image.new('L', (S, S), 0), mask))
    return im.resize((size, size), Image.LANCZOS)


PNGS = {'png/icon-512.png': (512, 'icon'), 'png/icon-192.png': (192, 'icon'), 'png/apple-touch-icon-180.png': (180, 'square'),
        'png/favicon-32.png': (32, 'icon'), 'png/play-store-512.png': (512, 'square'), 'png/notification-96.png': (96, 'notify')}


def main():
    files = {**svg_files(), **android_files()}
    for rel, text in files.items():
        p = HERE / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding='utf-8')
    for rel, (size, kind) in PNGS.items():
        p = HERE / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        png(size, kind).save(p, optimize=True)
    print(len(files), 'text +', len(PNGS), 'png →', HERE)


if __name__ == '__main__':
    main()
