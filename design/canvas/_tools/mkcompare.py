# -*- coding: utf-8 -*-
"""라이트/다크 아트보드를 한 장에 나란히 놓은 비교 시트를 만든다."""
import json, pathlib, re, sys

SRC = pathlib.Path('/home/user/ajs-bit.github.com/design/canvas')
SP = pathlib.Path('/tmp/claude-0/-home-user-ajs-bit-github-com/8f2afc13-0278-5882-ad06-7ee97dbbe248/scratchpad')
CV = json.loads((SRC / 'canvas.json').read_text())
SIZE = {a['file']: (a['w'], a['h']) for a in CV['artboards']}


def body(name):
    t = (SRC / f'{name}.dc.html').read_text()
    return re.search(r'</helmet>(.*?)</x-dc>', t, re.S).group(1)


def helmet():
    t = (SRC / 'Main.dc.html').read_text()
    return re.search(r'<helmet>(.*?)</helmet>', t, re.S).group(1)


def sheet(pairs, title, scale=1.0, pad=34):
    """pairs: [(라벨, 라이트 이름, 다크 이름)]"""
    cols = []
    for label, lt, dk in pairs:
        w, h = SIZE[f'{lt}.dc.html']
        cells = []
        for nm, tag in ((lt, 'LIGHT'), (dk, 'DARK')):
            cells.append(
                f'<div style="display:flex;flex-direction:column;gap:9px;align-items:center">'
                f'<div style="font:600 12px/1 system-ui;letter-spacing:.12em;color:#8593AD">{tag}</div>'
                f'<div style="width:{w}px;height:{h}px;overflow:hidden;border-radius:20px;'
                f'box-shadow:0 2px 4px rgba(16,24,40,.10),0 18px 44px -20px rgba(16,24,40,.45)">{body(nm)}</div></div>')
        cols.append(
            f'<div style="display:flex;flex-direction:column;gap:14px;align-items:center">'
            f'<div style="font:700 17px/1.2 system-ui;letter-spacing:-.02em;color:#101828">{label}</div>'
            f'<div style="display:flex;gap:18px">{"".join(cells)}</div></div>')

    return f'''<!doctype html><html><head><meta charset="utf-8">{helmet()}
<style>html,body{{margin:0;background:#DFE4EE}}</style></head><body>
<div style="display:inline-block;padding:{pad}px;transform:scale({scale});transform-origin:0 0">
  <div style="font:700 26px/1.2 system-ui;letter-spacing:-.03em;color:#101828;margin-bottom:6px">{title}</div>
  <div style="font:400 14px/1.5 system-ui;color:#5B6880;margin-bottom:24px">NAVI v3 · 레이아웃·타이포·간격은 완전히 동일하고 토큰만 바뀝니다</div>
  <div style="display:flex;gap:42px;align-items:flex-start">{"".join(cols)}</div>
</div></body></html>'''


SETS = {
    'compare-1-screens': ('탭 5개 — 홈 · 자산 · 소비', [
        ('홈', 'Main', 'DarkHome'),
        ('자산', 'Assets', 'DarkAssets'),
        ('소비', 'Spending', 'DarkSpending'),
    ]),
    'compare-2-screens': ('탭 5개 — 목적지 · 미래 · 지난 달', [
        ('목적지', 'Goals', 'DarkGoals'),
        ('미래', 'Future', 'DarkFuture'),
        ('소비 · 지난 달', 'SpendingPast', 'DarkSpendingPast'),
    ]),
    'compare-3-modals': ('모달 — 거래 추가 · 적립액 추가 · 월 마감', [
        ('거래 추가', 'TransactionAdd', 'DarkTransactionAdd'),
        ('적립액 추가', 'GoalContribute', 'DarkGoalContribute'),
        ('월 마감', 'MonthlyClose', 'DarkMonthlyClose'),
    ]),
    'compare-4-states': ('상태 — 미입력 · 모달 오류', [
        ('미입력 5종', 'EmptyStates', 'DarkEmptyStates'),
        ('모달 오류 6종', 'ModalErrors', 'DarkModalErrors'),
    ]),
    'compare-5-desktop': ('데스크톱 — 홈', [
        ('홈 · 1440px', 'DesktopHome', 'DarkDesktopHome'),
    ]),
    'compare-6-desktop': ('데스크톱 — 소비 내역', [
        ('소비 내역 · 1440px', 'DesktopLedger', 'DarkDesktopLedger'),
    ]),
}

if __name__ == '__main__':
    out = SP / 'compare'
    out.mkdir(exist_ok=True)
    for name, (title, pairs) in SETS.items():
        scale = 0.62 if 'states' in name else (0.66 if 'desktop' in name else 1.0)
        (out / f'{name}.html').write_text(sheet(pairs, title, scale))
        print(name, 'ok')
