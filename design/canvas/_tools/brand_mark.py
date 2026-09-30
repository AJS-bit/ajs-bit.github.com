# -*- coding: utf-8 -*-
"""앱마크 규격 — 2026-09-30 사용자 결정 「클로드 C2로 가자 · 앱이랑 시안, 캔버스 뭐든 다 이걸로 통일」.

그림 「하루가 쌓인 길」: 적은 날 = 채운 칸 넷(왼쪽 아래에서 오른쪽 위로 계단) · 안 적은 날 = 작은 점 넷(앱이 기록 없는 날을 「—」로 두는 것)
· 목적지 = 속이 빈 원(목적지 링). 바탕 네모는 그대로(140deg #3556E6 → #7A3FE4 · 다크는 darken.py 의 밝은 그라디언트).
종이비행기(2026-09-23 규격)는 폰에서 길 안내 앱처럼 보인다는 지적으로 바뀌었다 — 탐색 기록은 CHANGES-2026-09-30.md.

좌표는 안드로이드 적응형 아이콘과 같은 108 × 108. 그림은 29.5 ~ 78.5(네모 한 변의 45.4%)이고, 이 비율은 사용자가 보고 고른
폰 미리보기와 같다. 그래서 마크 svg 는 **네모와 같은 크기 · viewBox 0 0 108 108** 이다(네모 크기가 바뀌어도 비율이 따라감).
흰색은 `white` 로 적는다 — darken.py 의 `#FFFFFF → surface` 변환을 타지 않아 다크에서도 흰 그림이다.
작은 알림 아이콘(네모 20px 미만)은 단색판(점 · 원 선을 조금 굵게 · viewBox 18 18 72 72 = 안드로이드 알림 아이콘의 보이는 칸)을 쓴다.
네모 크기별 둥근 모서리: 모바일 머리줄 32 → 10 · 설명 시트 30 → 10 · 데스크톱 34 → 11 · 알림 흉내 16 → 5."""
import re

CELL, GAP = 13.0, 5.0
LEFT = 54.0 - (CELL * 3 + GAP * 2) / 2          # 29.5
PATH = [(2, 0), (2, 1), (1, 1), (1, 2)]          # 적은 날 — 계단처럼 오름
DEST = (0, 2)                                     # 목적지
EMPTY = [(0, 0), (0, 1), (1, 0), (2, 2)]          # 아직 안 적은 날


def _f(v):
    return f'{v:.2f}'.rstrip('0').rstrip('.')


def _xy(rc):
    r, c = rc
    return LEFT + c * (CELL + GAP), LEFT + r * (CELL + GAP)


def symbol(fg='white', mono=False):
    """108 좌표의 그림 조각. mono = 알림 · 테마 아이콘용(점 r 3.0 · 원 선 3.6)."""
    out = []
    for rc in PATH:
        x, y = _xy(rc)
        out.append(f'<rect x="{_f(x)}" y="{_f(y)}" width="{_f(CELL)}" height="{_f(CELL)}" rx="3.6" fill="{fg}"/>')
    for rc in EMPTY:
        x, y = _xy(rc)
        out.append(f'<circle cx="{_f(x + CELL / 2)}" cy="{_f(y + CELL / 2)}" r="{3.0 if mono else 2.3}" fill="{fg}"/>')
    sw = 3.6 if mono else 3.4
    x, y = _xy(DEST)
    out.append(f'<circle cx="{_f(x + CELL / 2)}" cy="{_f(y + CELL / 2)}" r="{_f(CELL / 2 + 0.6 - sw / 2)}" fill="none" stroke="{fg}" stroke-width="{sw}"/>')
    return ''.join(out)


def svg(tile):
    """네모 안에 넣는 마크 svg(네모와 같은 크기)."""
    if tile < 20:
        return f'<svg width="{tile}" height="{tile}" viewBox="18 18 72 72">{symbol(mono=True)}</svg>'
    return f'<svg width="{tile}" height="{tile}" viewBox="0 0 108 108">{symbol()}</svg>'


def tile(size=32, radius=10, grad='linear-gradient(140deg, #3556E6 0%, #7A3FE4 100%)', extra=' flex-shrink: 0;'):
    return (f'<div style="width: {size}px; height: {size}px; border-radius: {radius}px; background: {grad}; '
            f'display: flex; align-items: center; justify-content: center;{extra}">{svg(size)}</div>')


# 옛 종이비행기 svg(어떤 크기든) → 네모 크기에 맞춘 새 마크. 손으로 고친 장에도 쓴다(멱등).
OLD_RE = re.compile(r'(<div style="width: (\d+)px; height: \d+px; border-radius: \d+px;[^"]*"[^>]*>\s*)'
                    r'<svg width="[\d.]+" height="[\d.]+" viewBox="[^"]+" fill="#FFFFFF"><path d="M20\.28[^"]*"/></svg>')


def fix(html):
    out = OLD_RE.sub(lambda m: m.group(1) + svg(int(m.group(2))), html)
    assert 'M20.28' not in out, f'종이비행기 {out.count("M20.28")}개가 남음'
    return out
