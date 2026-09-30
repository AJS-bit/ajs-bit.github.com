# -*- coding: utf-8 -*-
"""NAVI 로고 파일 묶음 — 2026-09-30 사용자 결정 「클로드 C2로 가자」(하루가 쌓인 길).

그림 규격은 `design/canvas/_tools/brand_mark.py` 하나에서 가져온다(시안 장의 마크와 같은 좌표 · 같은 두께).
바탕은 파랑 → 보라 대각선(#3556E6 → #7A3FE4 · 지금 앱 아이콘 · 시안 마크 네모와 같은 색).

비율 — 사용자가 고른 폰 미리보기(https://claude.ai/artifact/MEPXZ4GNUjBRBwSnhJoXEX)에서 그림은 **보이는 아이콘 한 변의 45.4%**.
안드로이드 적응형 아이콘은 108dp 층 중 가운데 72dp만 보이므로 전경 그림을 가운데 기준 72/108 로 줄인다(`FG_SCALE`).
그러면 그림은 108 좌표에서 37.67 ~ 70.33 — 안전 원(지름 66) 안에 넉넉히 든다.

    python3 gen_brand.py      # → design/brand/ 아래 svg · android · png
"""
import math, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'canvas' / '_tools'))
import brand_mark as bm                       # noqa: E402

BLUE, VIOLET = '#3556E6', '#7A3FE4'
FG_SCALE = 72 / 108                           # 적응형 전경 — 보이는 72dp 안에서 45.4%
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
    # 앱 아이콘(모서리 둥근 네모 · 앱 안 마크 · 웹) — 108 전체가 보이는 아이콘, 그림 45.4%
    out['svg/navi-icon.svg'] = (f'<svg {X} viewBox="0 0 108 108"><title>NAVI</title>{GRAD}'
                                f'<rect width="108" height="108" rx="27" fill="url(#navi-bg)"/>{bm.symbol("#FFFFFF")}</svg>')
    # 스토어 · 마스크 적용 전(네모 꽉 채움)
    out['svg/navi-icon-square.svg'] = (f'<svg {X} viewBox="0 0 108 108"><title>NAVI</title>{GRAD}'
                                       f'<rect width="108" height="108" fill="url(#navi-bg)"/>{bm.symbol("#FFFFFF")}</svg>')
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


def _rrect(x, y, w, h, r):
    return (f'M{_num(x + r)},{_num(y)}H{_num(x + w - r)}A{_num(r)},{_num(r)} 0 0 1 {_num(x + w)},{_num(y + r)}'
            f'V{_num(y + h - r)}A{_num(r)},{_num(r)} 0 0 1 {_num(x + w - r)},{_num(y + h)}'
            f'H{_num(x + r)}A{_num(r)},{_num(r)} 0 0 1 {_num(x)},{_num(y + h - r)}'
            f'V{_num(y + r)}A{_num(r)},{_num(r)} 0 0 1 {_num(x + r)},{_num(y)}Z')


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


def android_files():
    return {
        'android/ic_launcher_foreground.xml': vector(108, (0, 0, 108, 108), '#FFFFFFFF', s=FG_SCALE),
        'android/ic_launcher_monochrome.xml': vector(108, (0, 0, 108, 108), '#FF000000', mono=True, s=FG_SCALE),
        'android/ic_launcher_background.xml': background_vector(),
        # 알림 작은 아이콘 — 24dp 에 보이는 칸 18 ~ 90(72) 을 꽉 채움 · 흰 단색(색은 시스템이 입힘)
        'android/ic_stat_navi.xml': vector(24, (18, 18, 72, 72), '#FFFFFFFF', mono=True),
    }


# ── PNG (PIL · 8배로 그려 줄임) ──────────────────────────────────────────────────────
def png(size, kind):
    """kind: 'icon'(둥근 네모 · 웹 · 레거시 런처) · 'round'(원) · 'square'(꽉 참 · 스토어) · 'notify'(흰 단색 · 투명)."""
    from PIL import Image, ImageDraw
    K = 8
    S = size * K
    k = S / 108

    def lerp(a, b, t):
        return tuple(round(int(a[i:i + 2], 16) + (int(b[i:i + 2], 16) - int(a[i:i + 2], 16)) * t) for i in (1, 3, 5))

    if kind == 'notify':
        im = Image.new('RGBA', (S, S), (0, 0, 0, 0))
        view, off, mono = 72, 18, True
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
    P = lambda v: (v - off) * k
    d = ImageDraw.Draw(im)
    white = (255, 255, 255, 255)
    for rc in bm.PATH:
        x, y = bm._xy(rc)
        d.rounded_rectangle((P(x), P(y), P(x + bm.CELL), P(y + bm.CELL)), radius=3.6 * k, fill=white)
    for rc in bm.EMPTY:
        x, y = bm._xy(rc)
        r = 3.0 if mono else 2.3
        cx, cy = x + bm.CELL / 2, y + bm.CELL / 2
        d.ellipse((P(cx - r), P(cy - r), P(cx + r), P(cy + r)), fill=white)
    sw = 3.6 if mono else 3.4
    x, y = bm._xy(bm.DEST)
    cx, cy, r = x + bm.CELL / 2, y + bm.CELL / 2, bm.CELL / 2 + 0.6 - sw / 2
    ro, ri = r + sw / 2, r - sw / 2
    ring = Image.new('L', (S, S), 0)
    rd = ImageDraw.Draw(ring)
    rd.ellipse((P(cx - ro), P(cy - ro), P(cx + ro), P(cy + ro)), fill=255)
    rd.ellipse((P(cx - ri), P(cy - ri), P(cx + ri), P(cy + ri)), fill=0)
    im.paste(Image.new('RGBA', (S, S), white), (0, 0), ring)
    if kind != 'notify':
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
