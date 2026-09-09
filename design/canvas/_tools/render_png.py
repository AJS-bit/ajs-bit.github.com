"""아트보드(.dc.html) → PNG. `design/preview/`의 렌더를 만든 스크립트입니다.

만든 앱 화면을 아트보드와 나란히 비교할 때 같은 방식으로 캡처하면 됩니다.

    python3 render_png.py                   # 전부 → ../../preview/
    python3 render_png.py Main Assets       # 일부만
    python3 render_png.py --scale 2         # 2배 (기본 1.5)
    python3 render_png.py --out /tmp/shots  # 출력 위치

크로미움 경로는 --chrome 또는 환경변수 CHROME으로 지정합니다.
웹폰트는 네트워크 없이 되도록 자체 호스팅본을 쓰세요. `--font-css`에 로컬 CSS 경로를
주면 아트보드의 Google Fonts link를 그것으로 바꿔 렌더합니다. 주지 않으면 원격을
그대로 쓰므로, 네트워크가 막힌 환경에서는 폰트가 폴백으로 떨어집니다.
"""
import argparse, json, os, pathlib, re, shutil, subprocess, sys, tempfile

# 헤드리스 크로미움은 --window-size 높이에 창 크롬 높이를 포함해서 계산하는 빌드가 있다.
# 그대로 찍으면 아래쪽이 소리 없이 잘린다(바텀 네비가 통째로 사라진다). 넉넉히 찍고 잘라낸다.
PAD = 160

HERE = pathlib.Path(__file__).resolve().parent
CANVAS = HERE.parent
DESIGN = CANVAS.parent

CHROME_CANDIDATES = [
    os.environ.get('CHROME', ''),
    '/opt/pw-browsers/chromium-1194/chrome-linux/chrome',
    shutil.which('chromium') or '',
    shutil.which('chromium-browser') or '',
    shutil.which('google-chrome') or '',
]


def find_chrome(explicit=None):
    for c in ([explicit] if explicit else []) + CHROME_CANDIDATES:
        if c and pathlib.Path(c).exists():
            return c
    sys.exit('크로미움을 찾지 못했습니다. --chrome 으로 경로를 주세요.')


def standalone(dc_path, w, h, font_css=None):
    """.dc.html의 <helmet>과 본문을 평범한 HTML 한 장으로 편다."""
    t = dc_path.read_text()
    helm = re.search(r'<helmet>(.*?)</helmet>', t, re.S).group(1)
    body = re.search(r'</helmet>(.*?)</x-dc>', t, re.S).group(1)
    if font_css:
        helm = re.sub(r'<link rel="stylesheet" href="https://fonts\.googleapis\.com[^>]*>',
                      f'<link rel="stylesheet" href="{font_css}">', helm)
    return (f'<!doctype html><html><head><meta charset="utf-8">{helm}\n'
            f'<style>html,body{{margin:0;background:#fff}}'
            f'.frame{{width:{w}px;height:{h}px;overflow:hidden;position:relative}}</style></head>'
            f'<body><div class="frame">{body}</div></body></html>')


def crop(png, w, h):
    """PAD만큼 더 찍은 이미지를 아트보드 크기로 잘라낸다."""
    if not png.exists():
        return
    try:
        from PIL import Image
    except ImportError:
        print(f'  Pillow가 없어 자르지 못했습니다: {png.name} (아래 {PAD}px는 여백입니다)')
        return
    im = Image.open(png)
    if im.size != (w, h):
        im.convert('RGB').crop((0, 0, w, h)).save(png)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('names', nargs='*', help='아트보드 이름 (비우면 전부)')
    ap.add_argument('--out', default=str(DESIGN / 'preview'))
    ap.add_argument('--scale', type=float, default=1.5)
    ap.add_argument('--chrome', default=None)
    ap.add_argument('--font-css', default=None, help='로컬 웹폰트 CSS 경로 (file:// 또는 상대경로)')
    a = ap.parse_args()

    chrome = find_chrome(a.chrome)
    sizes = {x['file']: (x['w'], x['h']) for x in json.loads((CANVAS / 'canvas.json').read_text())['artboards']}
    out = pathlib.Path(a.out); out.mkdir(parents=True, exist_ok=True)

    targets = [CANVAS / f'{n}.dc.html' for n in a.names] if a.names else sorted(CANVAS.glob('*.dc.html'))
    tmp = pathlib.Path(tempfile.mkdtemp(prefix='navi-render-'))
    n = 0
    for f in targets:
        if not f.exists():
            print(f'  건너뜀 (없음): {f.name}'); continue
        w, h = sizes.get(f.name, (390, 844))
        page = tmp / f.name.replace('.dc.html', '.html')
        page.write_text(standalone(f, w, h, a.font_css))
        shot = out / f.name.replace('.dc.html', '.png')
        subprocess.run([
            chrome, '--headless', '--disable-gpu', '--no-sandbox', '--hide-scrollbars',
            f'--force-device-scale-factor={a.scale}', '--virtual-time-budget=4000',
            f'--window-size={w},{h + PAD}',
            f'--screenshot={shot}',
            page.as_uri(),
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        crop(shot, round(w * a.scale), round(h * a.scale))
        n += 1
    shutil.rmtree(tmp, ignore_errors=True)
    print(f'{n}장 → {out}')


if __name__ == '__main__':
    main()
