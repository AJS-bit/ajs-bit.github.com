"""아트보드(.dc.html) → 블록 개요(Markdown).

원본 마크업은 한 화면이 300~400줄이라 통째로 읽기 부담스럽습니다.
이 스크립트는 깊이 3까지의 블록 구조만 남기고, 각 블록의 역할을
스타일에서 뽑은 요약(카드/버튼/칩/…)과 첫 텍스트로 한 줄씩 적습니다.

    python3 outline.py            # ../  아트보드 전부 → spec/<이름>.outline.md
    python3 outline.py Main       # 한 개만 표준출력으로
"""
import re, sys, pathlib
from html.parser import HTMLParser

HERE = pathlib.Path(__file__).resolve().parent
CANVAS = HERE.parent

VOID = {'br', 'img', 'input', 'hr', 'meta', 'link', 'path', 'circle', 'rect', 'line', 'polyline', 'polygon', 'ellipse'}
KEEP = ['display', 'flex-direction', 'align-items', 'justify-content', 'flex-wrap',
        'grid-template-columns', 'gap', 'padding', 'height', 'min-height', 'width', 'background',
        'border', 'border-top', 'border-bottom', 'border-left', 'border-radius', 'box-shadow',
        'font-size', 'font-weight', 'color', 'line-height', 'text-align', 'letter-spacing',
        'white-space', 'position', 'left', 'right', 'top', 'bottom',
        'inset', 'transform', 'margin-top', 'flex', 'opacity']


class Node:
    def __init__(self, tag, style, attrs):
        self.tag, self.style, self.attrs = tag, style, attrs
        self.kids, self.text = [], ''


class T(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node('root', '', {})
        self.stack = [self.root]

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        n = Node(tag, re.sub(r'\s+', ' ', a.get('style', '')).strip(), a)
        self.stack[-1].kids.append(n)
        if tag not in VOID:
            self.stack.append(n)

    def handle_startendtag(self, tag, attrs):
        pass

    def handle_endtag(self, tag):
        if tag not in VOID and len(self.stack) > 1:
            self.stack.pop()

    def handle_data(self, d):
        d = d.strip()
        if d:
            self.stack[-1].text += (' ' if self.stack[-1].text else '') + d


def sd(style):
    """스타일 요약 — 구현에 필요한 선언만 남긴다."""
    out = []
    for decl in style.split(';'):
        if ':' not in decl:
            continue
        k, v = decl.split(':', 1)
        k, v = k.strip(), v.strip()
        if k in KEEP:
            out.append(f'{k}:{v}')
    return ' '.join(out)


def role(n):
    """스타일에서 컴포넌트 이름을 추정한다. SPEC-COMPONENTS.md의 이름과 맞춘다."""
    s = n.style
    if 'height: 32px' in s and '#E9EDFD' in s: return 'SampleBanner'
    if 'height: 66px' in s and 'border-top: 1px solid' in s: return 'BottomNav'
    if 'padding: 12px 16px 10px' in s: return 'Header'
    if 'border-radius: 26px 26px 0 0' in s: return 'BottomSheet'
    if 'height: 190px' in s and 'align-items: flex-end' in s: return 'Scrim여백'
    if 'width: 390px' in s and 'height: 844px' in s: return '화면프레임'
    if 'flex: 1' in s and 'min-height: 0' in s and 'padding: 0 14px' in s: return '본문(스크롤 영역)'
    if 'width: 38px' in s and 'height: 4px' in s: return 'GrabHandle'
    if 'border-left: 3px solid #DE8A2A' in s or 'border-left: 3px solid #A9772C' in s: return 'TurnCard'
    if 'border-radius: 20px' in s and 'box-shadow' in s: return 'HeroCard'
    if 'border-radius: 20px' in s and 'background: #FFFFFF' in s: return 'Card(20)'
    if 'border-radius: 18px' in s and 'background: #FFFFFF' in s: return 'Card(18)'
    if 'border-radius: 99px' in s and 'padding: 4px 9px' in s: return 'StatusPill'
    if 'border-radius: 99px' in s and 'height: 4px' in s: return 'GrabHandle'
    if 'border-radius: 99px' in s and ('height: 6px' in s or 'height: 9px' in s or 'height: 10px' in s): return 'ProgressTrack'
    if 'height: 48px' in s and 'background: #3556E6' in s: return 'PrimaryButton(48)'
    if 'height: 44px' in s and 'background: #3556E6' in s: return 'PrimaryButton(44)'
    if 'height: 48px' in s and 'border: 1px solid #D7DEEA' in s: return 'SecondaryButton(48)'
    if 'height: 44px' in s and 'border: 1px solid #D7DEEA' in s: return 'SecondaryButton(44)'
    if 'height: 46px' in s and 'border: 1px solid #CFD7E6' in s: return 'InputField'
    if 'height: 36px' in s and 'border-radius: 9px' in s: return 'SegmentedItem'
    if 'border-radius: 12px' in s and 'background: #F4F6FB' in s: return 'Callout(info)'
    if 'border-radius: 12px' in s and 'background: #FDF1E0' in s: return 'Callout(warn)'
    if n.tag == 'svg': return 'icon'
    m = re.search(r'font-size: ([\d.]+)px', s)
    if m and not n.kids:
        w = re.search(r'font-weight: (\d+)', s)
        return f'text {m.group(1)}px/{w.group(1) if w else 400}'
    return ''


def walk(n, depth, maxd, buf):
    for k in n.kids:
        if k.tag in ('svg', 'script', 'style'):
            continue
        r = role(k)
        t = k.text[:64]
        digest = sd(k.style)
        line = '  ' * depth + f'- `{k.tag}`'
        if r:
            line += f' **{r}**'
        if t:
            line += f' — “{t}”'
        if digest:
            line += f'\n{"  " * depth}  `{digest}`'
        buf.append(line)
        if depth < maxd:
            walk(k, depth + 1, maxd, buf)


def outline(path, maxd=4):
    t = path.read_text()
    body = re.search(r'</helmet>(.*?)</x-dc>', t, re.S).group(1)
    p = T(); p.feed(body)
    buf = []
    walk(p.root, 0, maxd, buf)
    return '\n'.join(buf)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        print(outline(CANVAS / f'{sys.argv[1]}.dc.html'))
    else:
        out = HERE.parent.parent / 'spec'
        out.mkdir(exist_ok=True)
        n = 0
        for f in sorted(CANVAS.glob('*.dc.html')):
            if f.name.startswith('Dark'):
                continue
            (out / f'{f.stem.replace(".dc","")}.outline.md').write_text(
                f'# {f.stem.replace(".dc","")} — 블록 개요\n\n'
                f'원본 `canvas/{f.name}`. 값이 다르면 **원본이 맞습니다.**\n\n'
                + outline(f) + '\n')
            n += 1
        print(n, 'outlines')
