# -*- coding: utf-8 -*-
"""NAVI 로고 파일 묶음 — 2026-10-09 사용자 결정 「라이트 모드랑 기본 앱 아이콘은 A + 노란 원 · 다크 모드의 앱 안 로고와 시작 화면은 샴페인」.

그림 규격은 `design/canvas/_tools/brand_mark.py` 하나에서 가져온다(보이는 아이콘 한 변 = 1024 좌표 · LIGHT / DARK / MONO —
시안 장의 마크 · 앱 안 마크와 같은 좌표 · 같은 색).
- 기본 앱 아이콘(폰 런처 · 앱 목록 · 스토어 · 웹) = LIGHT 「A + 노란 원」 하나. 런처는 폰 모드를 따라가지 못해서
  (설치 · 업데이트 때 고른 그림을 계속 씀 — 에뮬레이터로 확인) 하나로 고정한다.
- 시작 화면(안드로이드 12+) = 적응형 아이콘. 밝은 모드는 런처 아이콘 그대로, 어두운 모드는 DARK 「샴페인」
  (values / values-night 의 `navi_splash_icon` 이 고른다). 바탕색 navi_splash(#EDF0F7 / #080C16)는 그대로.
- 테마(단색) 아이콘 · 알림 작은 아이콘 = MONO(같은 길 · 점 · 원을 안전 원 안으로 줄인 단색판).

좌표 옮기기
- 적응형 층(108dp 중 가운데 72dp가 보임): dp = 18 + v × 72 ÷ 1024. 길은 층 밖까지 이어져 층 가장자리에서 잘린다.
- 108 전체가 보이는 것(26 미만 벡터 · 웹 svg · PNG): v × 108 ÷ 1024.
- 알림 작은 아이콘(24dp): 단색판을 세로 20dp(가운데 기준)로 — 상태 표시줄 아이콘의 보이는 칸.

    python3 gen_brand.py      # → design/brand/ 아래 svg · android(앱 android/app/src/main/res 와 같은 경로 · 같은 바이트) · png · og.html
    node og_shot.cjs          # og.html → png/og-1730x909.png(앱 public/og.png 와 같은 파일)
"""
import pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'canvas' / '_tools'))
import brand_mark as bm                       # noqa: E402

X = 'xmlns="http://www.w3.org/2000/svg"'
WEB_RADIUS = 256                              # 웹 아이콘 모서리 — 한 변의 25%(예전 108 칸의 27과 같은 비율)
LEGACY_RADIUS = 108 * 18 / 56                 # 26 미만 런처의 둥근 네모 모서리(예전 그대로)
FG = lambda v: 18 + v * 72 / bm.VIEW          # noqa: E731 — 적응형 층 좌표
FULL = lambda v: v * 108 / bm.VIEW            # noqa: E731 — 108 전체가 보이는 아이콘
POINTS = [(float(a), float(b)) for a, b in re.findall(r'(-?[\d.]+) (-?[\d.]+)', bm.BAND)]
MONO_POINTS = [(float(a), float(b)) for a, b in re.findall(r'(-?[\d.]+) (-?[\d.]+)', bm.MONO_BAND)]


def _mono_box():
    """단색판의 실제 그림 범위(선 두께 · 원 선 포함) — 알림 아이콘 · 그림만 svg 의 viewBox."""
    xs, ys = [], []
    h = bm.MONO_BAND_W / 2
    for x, y in MONO_POINTS:
        xs += [x - h, x + h]; ys += [y - h, y + h]
    for x, y in bm.MONO_DOTS:
        xs += [x - bm.MONO_DOT_R, x + bm.MONO_DOT_R]; ys += [y - bm.MONO_DOT_R, y + bm.MONO_DOT_R]
    rx, ry = bm.MONO_RING
    o = bm.MONO_RING_R + bm.MONO_RING_W / 2
    xs += [rx - o, rx + o]; ys += [ry - o, ry + o]
    return min(xs), min(ys), max(xs), max(ys)


MX0, MY0, MX1, MY1 = _mono_box()
MCX, MCY = (MX0 + MX1) / 2, (MY0 + MY1) / 2
STAT_SIDE = (MY1 - MY0) * 24 / 20             # 24dp 안에서 세로 20dp
STAT = lambda v, c: (v - c + STAT_SIDE / 2) * 24 / STAT_SIDE   # noqa: E731


def _n(v):
    s = f'{v:.3f}'.rstrip('0').rstrip('.')
    return '0' if s in ('-0', '') else s


# ── SVG ──────────────────────────────────────────────────────────────────────────────
def _layer(inner, s=72 / 1024, t=18):
    return f'<g transform="translate({_n(t)} {_n(t)}) scale({s:.7g})">{inner}</g>'


def _art_parts(dark=False, gid='navi-champagne'):
    """art() 에서 바탕 네모를 뺀 앞 그림(적응형 전경용)."""
    return re.sub(r'<rect width="1024" height="1024" fill="#[0-9A-F]{6}"/>', '', bm.art(dark, gid))


def svg_files():
    out = {}
    clip = f'<clipPath id="navi-r"><rect width="1024" height="1024" rx="{WEB_RADIUS}"/></clipPath>'
    # 앱 아이콘(모서리 둥근 네모 · 웹 favicon) · 다크(어두운 모드의 앱 안 로고 · 시작 화면과 같은 그림)
    out['svg/navi-icon.svg'] = f'<svg {X} viewBox="0 0 1024 1024"><title>NAVI</title><defs>{clip}</defs><g clip-path="url(#navi-r)">{bm.art()}</g></svg>'
    out['svg/navi-icon-dark.svg'] = (f'<svg {X} viewBox="0 0 1024 1024"><title>NAVI</title><defs>{clip}</defs>'
                                     f'<g clip-path="url(#navi-r)">{bm.art(True)}</g></svg>')
    # 스토어 · 마스크 적용 전(네모 꽉 채움)
    out['svg/navi-icon-square.svg'] = f'<svg {X} viewBox="0 0 1024 1024"><title>NAVI</title>{bm.art()}</svg>'
    # 안드로이드 적응형 층(108 좌표 · 가운데 72만 보임)
    out['svg/adaptive-background.svg'] = f'<svg {X} viewBox="0 0 108 108"><rect width="108" height="108" fill="{bm.LIGHT["bg"]}"/></svg>'
    out['svg/adaptive-foreground.svg'] = f'<svg {X} viewBox="0 0 108 108">{_layer(_art_parts())}</svg>'
    out['svg/adaptive-background-dark.svg'] = f'<svg {X} viewBox="0 0 108 108"><rect width="108" height="108" fill="{bm.DARK["bg"]}"/></svg>'
    out['svg/adaptive-foreground-dark.svg'] = f'<svg {X} viewBox="0 0 108 108">{_layer(_art_parts(True))}</svg>'
    out['svg/adaptive-monochrome.svg'] = f'<svg {X} viewBox="0 0 108 108">{_layer(bm.mono())}</svg>'
    # 알림 작은 아이콘(24 · 흰 단색 · 세로 20dp)
    vb = f'{_n(MCX - STAT_SIDE / 2)} {_n(MCY - STAT_SIDE / 2)} {_n(STAT_SIDE)} {_n(STAT_SIDE)}'
    out['svg/notification-24.svg'] = f'<svg {X} width="24" height="24" viewBox="{vb}">{bm.mono("#FFFFFF")}</svg>'
    # 그림만(투명 바탕 · 문서 · 워드마크용) — 단색판을 그림 테두리에 딱 맞춘 viewBox
    tight = f'{_n(MX0)} {_n(MY0)} {_n(MX1 - MX0)} {_n(MY1 - MY0)}'
    out['svg/navi-symbol.svg'] = f'<svg {X} viewBox="{tight}"><title>NAVI</title>{bm.mono(bm.LIGHT["bg"])}</svg>'
    out['svg/navi-symbol-white.svg'] = f'<svg {X} viewBox="{tight}"><title>NAVI</title>{bm.mono("#FFFFFF")}</svg>'
    return out


# ── 안드로이드 벡터 드로어블 ───────────────────────────────────────────────────────────
def _circle(cx, cy, r):
    return f'M{_n(cx - r)},{_n(cy)}A{_n(r)},{_n(r)} 0 1 0 {_n(cx + r)},{_n(cy)}A{_n(r)},{_n(r)} 0 1 0 {_n(cx - r)},{_n(cy)}Z'


def _poly(points, T):
    return 'M' + 'L'.join(f'{_n(T(x))},{_n(T(y))}' for x, y in points)


def _rrect(w, r):
    return (f'M{_n(r)},0H{_n(w - r)}A{_n(r)},{_n(r)} 0 0 1 {_n(w)},{_n(r)}V{_n(w - r)}A{_n(r)},{_n(r)} 0 0 1 {_n(w - r)},{_n(w)}'
            f'H{_n(r)}A{_n(r)},{_n(r)} 0 0 1 0,{_n(w - r)}V{_n(r)}A{_n(r)},{_n(r)} 0 0 1 {_n(r)},0Z')


def _argb(hex6, alpha=1.0):
    return f'#{round(alpha * 255):02X}{hex6[1:]}' if alpha < 1 else f'#FF{hex6[1:]}'


def _art_paths(T, s, dark=False, indent='  '):
    """보이는 1024 칸을 T 로 옮긴 길 · 점 · 원 path(선 두께는 s 배). dark = 샴페인 그라디언트 길."""
    p = bm.DARK if dark else bm.LIGHT
    band = _poly(POINTS, T)
    common = (f'android:strokeWidth="{_n(bm.BAND_W * s)}" android:strokeLineJoin="round" android:strokeLineCap="round" '
              f'android:fillColor="#00000000" android:pathData="{band}"')
    if dark:
        x1, y1, x2, y2 = bm.DARK_LINE
        items = ''.join(f'<item android:offset="{o}" android:color="{_argb(c)}"/>' for o, c in bm.DARK_RAMP)
        band_xml = (f'{indent}<path {common}>\n{indent}  <aapt:attr name="android:strokeColor">'
                    f'<gradient android:type="linear" android:startX="{_n(T(x1))}" android:startY="{_n(T(y1))}" '
                    f'android:endX="{_n(T(x2))}" android:endY="{_n(T(y2))}" android:tileMode="clamp">{items}</gradient>'
                    f'</aapt:attr>\n{indent}</path>\n')
    else:
        band_xml = f'{indent}<path android:strokeColor="{_argb(p["band"])}" {common}/>\n'
    dots = ''.join(_circle(T(x), T(y), bm.DOT_R * s) for x, y in bm.DOTS)
    rx, ry = bm.RING
    return (band_xml
            + f'{indent}<path android:fillColor="{_argb(p["dot"])}" android:fillAlpha="{p["dot_op"]}" android:pathData="{dots}"/>\n'
            + f'{indent}<path android:fillColor="#00000000" android:strokeColor="{_argb(bm.GOLD)}" android:strokeWidth="{_n(bm.RING_W * s)}" '
              f'android:pathData="{_circle(T(rx), T(ry), bm.RING_R * s)}"/>\n')


def _mono_paths(T, s, color, indent='  '):
    dots = ''.join(_circle(T(x), T(y), bm.MONO_DOT_R * s) for x, y in bm.MONO_DOTS)
    rx, ry = bm.MONO_RING
    return (f'{indent}<path android:fillColor="#00000000" android:strokeColor="{color}" android:strokeWidth="{_n(bm.MONO_BAND_W * s)}" '
            f'android:strokeLineJoin="round" android:strokeLineCap="round" android:pathData="{_poly(MONO_POINTS, T)}"/>\n'
            f'{indent}<path android:fillColor="{color}" android:pathData="{dots}"/>\n'
            f'{indent}<path android:fillColor="#00000000" android:strokeColor="{color}" android:strokeWidth="{_n(bm.MONO_RING_W * s)}" '
            f'android:pathData="{_circle(T(rx), T(ry), bm.MONO_RING_R * s)}"/>\n')


HEAD = '<?xml version="1.0" encoding="utf-8"?>\n<!-- NAVI 아이콘 — design/brand/gen_brand.py 가 만든다(규격 design/canvas/_tools/brand_mark.py). 손으로 고치지 말 것 -->\n'
NS = 'xmlns:android="http://schemas.android.com/apk/res/android"'
AAPT = ' xmlns:aapt="http://schemas.android.com/aapt"'


def _vector(dp, view, body, aapt=False):
    return (f'{HEAD}<vector {NS}{AAPT if aapt else ""}\n    android:width="{dp}dp" android:height="{dp}dp"\n'
            f'    android:viewportWidth="{view}" android:viewportHeight="{view}">\n{body}</vector>\n')


def _solid(hex6):
    return _vector(108, 108, f'  <path android:fillColor="{_argb(hex6)}" android:pathData="M0,0H108V108H0Z"/>\n')


def _adaptive(bg, fg, mono=None):
    m = f'\n    <monochrome android:drawable="@drawable/{mono}"/>' if mono else ''
    return (f'{HEAD}<adaptive-icon {NS}>\n    <background android:drawable="@drawable/{bg}"/>\n'
            f'    <foreground android:drawable="@drawable/{fg}"/>{m}\n</adaptive-icon>\n')


def legacy_launcher(shape):
    """26 미만 런처(적응형 아이콘 없음) — 108 전체가 보이는 둥근 네모(ic_launcher_navi) · 원(ic_launcher_round_navi)."""
    bg = _circle(54, 54, 54) if shape == 'round' else _rrect(108, LEGACY_RADIUS)
    s = 108 / bm.VIEW
    body = (f'  <path android:fillColor="{_argb(bm.LIGHT["bg"])}" android:pathData="{bg}"/>\n'
            f'  <group>\n    <clip-path android:pathData="{bg}"/>\n{_art_paths(FULL, s, indent="    ")}  </group>\n')
    return _vector(108, 108, body)


def android_files():
    s = 72 / bm.VIEW
    stat = lambda c: (lambda v: STAT(v, c))   # noqa: E731
    sx, sy = stat(MCX), stat(MCY)
    dots = ''.join(_circle(sx(x), sy(y), bm.MONO_DOT_R * 24 / STAT_SIDE) for x, y in bm.MONO_DOTS)
    rx, ry = bm.MONO_RING
    w = 24 / STAT_SIDE
    stat_body = (f'  <path android:fillColor="#00000000" android:strokeColor="#FFFFFFFF" android:strokeWidth="{_n(bm.MONO_BAND_W * w)}" '
                 f'android:strokeLineJoin="round" android:strokeLineCap="round" '
                 f'android:pathData="M' + 'L'.join(f'{_n(sx(x))},{_n(sy(y))}' for x, y in MONO_POINTS) + '"/>\n'
                 f'  <path android:fillColor="#FFFFFFFF" android:pathData="{dots}"/>\n'
                 f'  <path android:fillColor="#00000000" android:strokeColor="#FFFFFFFF" android:strokeWidth="{_n(bm.MONO_RING_W * w)}" '
                 f'android:pathData="{_circle(sx(rx), sy(ry), bm.MONO_RING_R * w)}"/>\n')
    alias = lambda target: (f'<?xml version="1.0" encoding="utf-8"?>\n<!-- 시작 화면 아이콘 — design/brand/gen_brand.py. '   # noqa: E731
                            f'밝은 모드 = 런처 아이콘(A + 노란 원) · 어두운 모드 = 샴페인 -->\n<resources>\n'
                            f'    <item name="navi_splash_icon" type="drawable">@mipmap/{target}</item>\n</resources>\n')
    return {
        # 런처 · 앱 목록(하나로 고정) — 바탕 · 전경 · 단색
        'android/drawable/ic_launcher_navi_background.xml': _solid(bm.LIGHT['bg']),
        'android/drawable/ic_launcher_foreground_navi.xml': _vector(108, 108, _art_paths(FG, s)),
        'android/drawable/ic_launcher_monochrome_navi.xml': _vector(108, 108, _mono_paths(FG, s, '#FF000000')),
        'android/mipmap-anydpi-v26/ic_launcher_navi.xml': _adaptive('ic_launcher_navi_background', 'ic_launcher_foreground_navi', 'ic_launcher_monochrome_navi'),
        'android/mipmap-anydpi-v26/ic_launcher_round_navi.xml': _adaptive('ic_launcher_navi_background', 'ic_launcher_foreground_navi', 'ic_launcher_monochrome_navi'),
        'android/mipmap-anydpi/ic_launcher_navi.xml': legacy_launcher('square'),
        'android/mipmap-anydpi/ic_launcher_round_navi.xml': legacy_launcher('round'),
        # 어두운 모드 시작 화면 — 샴페인(런처에는 쓰지 않음)
        'android/drawable/navi_splash_dark_background.xml': _solid(bm.DARK['bg']),
        'android/drawable/navi_splash_dark_foreground.xml': _vector(108, 108, _art_paths(FG, s, dark=True), aapt=True),
        'android/mipmap-anydpi-v26/navi_splash_dark.xml': _adaptive('navi_splash_dark_background', 'navi_splash_dark_foreground'),
        'android/values/navi_splash_icon.xml': alias('ic_launcher_navi'),
        'android/values-night/navi_splash_icon.xml': alias('navi_splash_dark'),
        # 알림 작은 아이콘 — 24dp · 흰 단색(색은 시스템이 입힘)
        'android/drawable/ic_stat_navi.xml': _vector(24, 24, stat_body),
    }


# ── PNG (PIL · 4배로 그려 줄임) ──────────────────────────────────────────────────────
def png(size, kind):
    """kind: 'icon'(둥근 네모 · 웹) · 'square'(꽉 참 · 스토어 · 애플 터치) · 'notify'(흰 단색 · 투명 · 세로 20/24)."""
    from PIL import Image, ImageDraw
    K = 4
    S = size * K

    def hexrgb(h, a=255):
        return (int(h[1:3], 16), int(h[3:5], 16), int(h[5:7], 16), a)

    def stroke_mask(points, w, T, k):
        m = Image.new('L', (S, S), 0)
        d = ImageDraw.Draw(m)
        pts = [(T(x), T(y)) for x, y in points]
        for a, b in zip(pts, pts[1:]):
            d.line([a, b], fill=255, width=round(w * k))
        r = w * k / 2
        for x, y in pts:
            d.ellipse((x - r, y - r, x + r, y + r), fill=255)
        return m

    def disc_mask(centers, r, T, k, alpha=255):
        m = Image.new('L', (S, S), 0)
        d = ImageDraw.Draw(m)
        for x, y in centers:
            d.ellipse((T(x) - r * k, T(y) - r * k, T(x) + r * k, T(y) + r * k), fill=alpha)
        return m

    def ring_mask(c, r, w, T, k):
        m = Image.new('L', (S, S), 0)
        d = ImageDraw.Draw(m)
        o, i = (r + w / 2) * k, (r - w / 2) * k
        d.ellipse((T(c[0]) - o, T(c[1]) - o, T(c[0]) + o, T(c[1]) + o), fill=255)
        d.ellipse((T(c[0]) - i, T(c[1]) - i, T(c[0]) + i, T(c[1]) + i), fill=0)
        return m

    if kind == 'notify':
        k = S / STAT_SIDE
        T = lambda v: v * k   # noqa: E731
        U = lambda pts: [(x - MCX + STAT_SIDE / 2, y - MCY + STAT_SIDE / 2) for x, y in pts]   # noqa: E731 — 알림 칸 좌표
        alpha = Image.new('L', (S, S), 0)
        for m in (stroke_mask(U(MONO_POINTS), bm.MONO_BAND_W, T, k), disc_mask(U(bm.MONO_DOTS), bm.MONO_DOT_R, T, k),
                  ring_mask(U([bm.MONO_RING])[0], bm.MONO_RING_R, bm.MONO_RING_W, T, k)):
            alpha = Image.composite(Image.new('L', (S, S), 255), alpha, m)
        im = Image.new('RGBA', (S, S), (255, 255, 255, 0))
        im.putalpha(alpha)
        return im.resize((size, size), Image.LANCZOS)

    k = S / bm.VIEW
    T = lambda v: v * k   # noqa: E731
    p = bm.LIGHT
    im = Image.new('RGBA', (S, S), hexrgb(p['bg']))
    im.paste(Image.new('RGBA', (S, S), hexrgb(p['band'])), (0, 0), stroke_mask(POINTS, bm.BAND_W, T, k))
    im.paste(Image.new('RGBA', (S, S), hexrgb(p['dot'])), (0, 0), disc_mask(bm.DOTS, bm.DOT_R, T, k, round(255 * float(p['dot_op']))))
    im.paste(Image.new('RGBA', (S, S), hexrgb(bm.GOLD)), (0, 0), ring_mask(bm.RING, bm.RING_R, bm.RING_W, T, k))
    if kind == 'icon':
        mask = Image.new('L', (S, S), 0)
        ImageDraw.Draw(mask).rounded_rectangle((0, 0, S - 1, S - 1), radius=WEB_RADIUS * k, fill=255)
        im.putalpha(mask)
    return im.resize((size, size), Image.LANCZOS)


PNGS = {'png/icon-512.png': (512, 'icon'), 'png/icon-192.png': (192, 'icon'), 'png/apple-touch-icon-180.png': (180, 'square'),
        'png/favicon-32.png': (32, 'icon'), 'png/play-store-512.png': (512, 'square'), 'png/notification-96.png': (96, 'notify')}


# ── 공유 그림(og) ────────────────────────────────────────────────────────────────────
def og_html(icon_svg):
    icon = icon_svg.replace('<svg ', '<svg width="300" height="300" ', 1)
    return ('<!doctype html><meta charset="utf-8">\n'
            '<!-- 공유 그림(og.png · 1730 × 909) — design/brand/gen_brand.py 가 만든다. 렌더: node og_shot.cjs(헤드리스 크롬 1730 × 909) -->\n'
            '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+KR:wght@500;700&display=swap">\n'
            '<style>\n*{box-sizing:border-box} html,body{margin:0}\n'
            'body{width:1730px;height:909px;background:radial-gradient(120% 140% at 0% 0%,#22335E 0%,#182644 45%,#111B33 100%);\n'
            "font-family:'IBM Plex Sans KR','Apple SD Gothic Neo',sans-serif;display:flex;align-items:center;gap:88px;padding:0 170px;overflow:hidden}\n"
            '.icon{flex:none;filter:drop-shadow(0 30px 60px rgba(0,0,0,.35))}\n'
            'h1{margin:0;font-size:176px;font-weight:700;letter-spacing:.06em;color:#FFFFFF;line-height:1}\n'
            'p{margin:34px 0 0;font-size:58px;font-weight:500;color:#C9D3F5;letter-spacing:-.01em}\n</style>\n'
            f'<body><div class="icon">{icon}</div><div><h1>NAVI</h1><p>자산 성장 내비게이션</p></div></body>')


def main():
    for old in ('android/ic_launcher_background.xml', 'android/ic_launcher_foreground.xml', 'android/ic_launcher_monochrome.xml',
                'android/ic_stat_navi.xml'):   # 2026-10-09 앞의 자리(앱 res 와 다른 이름) — 이제 android/ 는 앱 res 와 같은 경로
        (HERE / old).unlink(missing_ok=True)
    svgs = svg_files()
    files = {**svgs, **android_files(), 'og.html': og_html(svgs['svg/navi-icon.svg'])}
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
