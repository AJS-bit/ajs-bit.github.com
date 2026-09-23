# -*- coding: utf-8 -*-
"""앱마크(그라디언트 네모 + 종이비행기) 규격 — 2026-09-23 사용자 결정 「앱 안 아이콘은 너무 작고 폰 아이콘은 너무 크다 · 가운데가 틀어졌다」.
종이비행기는 네모 한 변의 약 54%(보이는 모양 기준 · svg 폭 = 네모 × 0.656)로 폰 런처 아이콘과 같은 비율이고,
테두리 상자가 아니라 **무게중심**(24 좌표계에서 13.2, 10.8)을 가운데에 둔다 — viewBox 를 (1.2, −1.2)만큼 옮긴다.
네모 크기별 (둥근 모서리, 그림 크기): 모바일 머리줄 32 · 빈 상태 32 · 설명 시트 30 · 데스크톱 34 · 첫 실행 62."""
import re

VIEWBOX = '1.2 -1.2 24 24'
SPEC = {32: (10, 21), 30: (10, 20), 34: (11, 22), 62: (20, 41)}
OLD_TO_NEW = {28: 32}          # 모바일 머리줄 28 → 32

MARK_RE = re.compile(r'<div style="width: (\d+)px; height: (\d+)px; border-radius: (\d+)px;([^"]*)"([^>]*)>(\s*)'
                     r'<svg width="([\d.]+)" height="([\d.]+)" viewBox="[^"]+"([^>]*)><path d="M20\.28')


def fix(html):
    def sub(m):
        tile = OLD_TO_NEW.get(int(m.group(1)), int(m.group(1)))
        rad, g = SPEC[tile]
        return (f'<div style="width: {tile}px; height: {tile}px; border-radius: {rad}px;{m.group(4)}"{m.group(5)}>{m.group(6)}'
                f'<svg width="{g}" height="{g}" viewBox="{VIEWBOX}"{m.group(9)}><path d="M20.28')
    out, n = MARK_RE.subn(sub, html)
    assert n == html.count('M20.28 2.32'), f'앱마크 {html.count("M20.28 2.32")}개 중 {n}개만 잡힘'
    return out
