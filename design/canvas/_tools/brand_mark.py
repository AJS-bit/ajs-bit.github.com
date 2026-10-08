# -*- coding: utf-8 -*-
"""앱마크 규격 — 2026-10-09 사용자 결정 「라이트 모드랑 기본 앱 아이콘은 A + 노란 원 · 앱 안 로고와 시작 화면은 2-C 샴페인」
(「샴페인은 다크 모드 말하는 거야」) → 「반영해」. 탐색 · 전후 기록은 design/CHANGES-2026-10-09.md.

그림은 「하루가 쌓인 길」(2026-09-30)을 이어받는다 — 적은 날 = 계단처럼 오르는 굵은 길 한 획(왼쪽 아래에서 아이콘 밖으로 이어짐)
· 안 적은 날 = 작은 점 넷 · 목적지 = 노란 원. 좌표는 **보이는 아이콘 한 변 = 1024**(폰 런처의 보이는 72dp · 앱 안 네모 · 웹 아이콘이 모두 이 칸).
길은 칸 밖(-380, 1380)에서 들어오므로 네모가 잘라 낸다(앱 안 네모는 overflow hidden · 런처는 적응형 층 마스크).

두 그림 — 바탕 · 길 · 점만 다르고 자리 · 굵기 · 노란 원은 같다.
- LIGHT 「A + 노란 원」: 바탕 #2445FF · 길 흰색 · 점 흰색 45% · 원 #FFC94D. **기본 앱 아이콘(런처 · 앱 목록 · 스토어 — 모드를 못 따라감)**,
  라이트 모드의 앱 안 로고 · 시작 화면.
- DARK 「샴페인」: 바탕 #07070B · 길 백금 → 샴페인 그라디언트(왼쪽 아래 → 목적지 쪽) · 점 #A09C90 38% · 원 #FFC94D.
  다크 모드의 앱 안 로고 · 시작 화면. 폰에서 띠가 생길 수 있는 바탕 비네팅은 뺐다.
- MONO: 테마(단색) 아이콘 · 알림 작은 아이콘 — 같은 길 · 점 · 원을 안전 원(66%) 안으로 줄인 단색판(투명 바탕 · 검정 한 색).

시안 장: 라이트 장은 LIGHT, 다크 장은 DARK(darken.py 가 `to_dark()` 로 바꿔 끼움 · dc-keep 으로 감싸 색 변환을 안 탐).
네모 크기 · 모서리는 예전 그대로 — 모바일 머리줄 32 → 10 · 설명 시트 30 → 10 · 데스크톱 34 → 11 · 저장소 화면 40 → 11 · 알림 흉내 16 → 5.
옛 「54%」(2026-09-30)는 칸 그림의 비율이었고, 새 그림은 보이는 네모를 꽉 채우는 아이콘 그림이라 비율 대신 이 1024 칸 하나가 규격이다."""
import re

VIEW = 1024
BAND = 'M-380 1380 L-110 1380 L-110 1110 L160 1110 L160 840 L430 840 L430 570 L700 570'   # 적은 날 — 계단 길 한 획
BAND_W = 195
DOTS = ((160, 300), (430, 300), (160, 570), (700, 840))                                   # 아직 안 적은 날
DOT_R = 30
RING, RING_R, RING_W = (700, 300), 79.5, 54                                               # 목적지
GOLD = '#FFC94D'

LIGHT = {'bg': '#2445FF', 'band': '#FFFFFF', 'dot': '#FFFFFF', 'dot_op': '0.45'}
DARK = {'bg': '#07070B', 'band': None, 'dot': '#A09C90', 'dot_op': '0.38'}
DARK_RAMP = ((0, '#6F6D68'), (0.5, '#ABA698'), (0.85, '#CDBF98'), (1, '#D3C79F'))          # 백금 → 샴페인
DARK_LINE = (100, 1000, 720, 560)                                                          # 램프 방향(1024 좌표 · 길을 따라 목적지 쪽)

# 단색판 — 같은 그림을 안드로이드 적응형 아이콘의 안전 원(보이는 칸의 66%) 안으로(가장 먼 원 가장자리 336px < 338px)
MONO_BAND = 'M355.1 744.06 L355.1 591.25 L509.46 591.25 L509.46 436.9 L663.81 436.9'
MONO_BAND_W = 111.48
MONO_DOTS = ((355.1, 282.55), (509.46, 282.55), (355.1, 436.9), (663.81, 591.25))
MONO_DOT_R = 20.54
MONO_RING, MONO_RING_R, MONO_RING_W = (663.81, 282.55), 45.42, 30.91


def _f(v):
    return f'{v:.2f}'.rstrip('0').rstrip('.')


def art(dark=False, gid='navi-champagne'):
    """1024 좌표의 그림 조각(바탕 네모 포함). dark 의 길 그라디언트 id = gid(한 문서 안에서 겹치지 않게)."""
    p = DARK if dark else LIGHT
    defs, band = '', p['band']
    if dark:
        x1, y1, x2, y2 = DARK_LINE
        stops = ''.join(f'<stop offset="{o}" stop-color="{c}"/>' for o, c in DARK_RAMP)
        defs = (f'<defs><linearGradient id="{gid}" gradientUnits="userSpaceOnUse" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}">'
                f'{stops}</linearGradient></defs>')
        band = f'url(#{gid})'
    dots = ''.join(f'<circle cx="{x}" cy="{y}" r="{DOT_R}" fill="{p["dot"]}"/>' for x, y in DOTS)
    return (f'{defs}<rect width="{VIEW}" height="{VIEW}" fill="{p["bg"]}"/>'
            f'<path d="{BAND}" fill="none" stroke="{band}" stroke-width="{BAND_W}" stroke-linejoin="round" stroke-linecap="round"/>'
            f'<g opacity="{p["dot_op"]}">{dots}</g>'
            f'<circle cx="{RING[0]}" cy="{RING[1]}" r="{RING_R}" fill="none" stroke="{GOLD}" stroke-width="{RING_W}"/>')


def mono(color='#000000'):
    """단색판 조각(1024 좌표 · 투명 바탕)."""
    dots = ''.join(f'<circle cx="{x}" cy="{y}" r="{MONO_DOT_R}" fill="{color}"/>' for x, y in MONO_DOTS)
    return (f'<path d="{MONO_BAND}" fill="none" stroke="{color}" stroke-width="{MONO_BAND_W}" stroke-linejoin="round" stroke-linecap="round"/>'
            f'{dots}<circle cx="{MONO_RING[0]}" cy="{MONO_RING[1]}" r="{MONO_RING_R}" fill="none" stroke="{color}" stroke-width="{MONO_RING_W}"/>')


def svg(size, dark=False, gid='navi-champagne'):
    """네모와 같은 크기의 마크 svg — 보이는 네모 전체가 그림."""
    return f'<svg width="{size}" height="{size}" viewBox="0 0 {VIEW} {VIEW}" style="display: block;">{art(dark, gid)}</svg>'


def tile_open(size=32, radius=10, extra=' flex-shrink: 0;'):
    return f'<div style="width: {size}px; height: {size}px; border-radius: {radius}px; overflow: hidden;{extra}">'


def tile(size=32, radius=10, extra=' flex-shrink: 0;'):
    """시안 장의 마크 네모(라이트 그림). 다크 장은 darken.py 가 to_dark() 로 바꾼다."""
    return f'{tile_open(size, radius, extra)}{svg(size)}</div>'


# 라이트 마크 svg → 다크 마크(샴페인). dc-keep 으로 감싸 darken 의 색 변환을 타지 않게 한다. 그라디언트 id 는 장 이름 + 차례.
LIGHT_RE = re.compile(r'<svg width="(\d+)" height="\d+" viewBox="0 0 1024 1024" style="display: block;">'
                      rf'<rect width="1024" height="1024" fill="{LIGHT["bg"]}"/>.*?</svg>', re.S)


def to_dark(html, name=''):
    slug = re.sub(r'[^A-Za-z0-9]+', '-', name).strip('-') or 'board'
    n = iter(range(1, 10 ** 6))
    return LIGHT_RE.sub(lambda m: f'<!--dc-keep-->{svg(int(m.group(1)), True, f"navi-champagne-{slug}-{next(n)}")}<!--/dc-keep-->', html)


# 옛 마크 네모(2026-09-30 「하루가 쌓인 길」 칸 그림 · 파랑 → 보라 네모 · viewBox 8.63 8.63 90.74 90.74) → 지금 규격. 손으로 쓴 장에도 쓴다(멱등).
OLD_RE = re.compile(r'<div style="width: (\d+)px; height: \d+px; border-radius: (\d+)px; '
                    r'background: linear-gradient\(140deg, #3556E6 0%, #7A3FE4 100%\); display: flex; align-items: center; justify-content: center;'
                    r'((?: flex-shrink: 0;)?)">(\s*)<svg width="\d+" height="\d+" viewBox="8\.63 8\.63 90\.74 90\.74">(?:<(?:rect|circle) [^>]*/>)+</svg>')


def fix(html):
    """손으로 쓴 장의 옛 마크 네모를 지금 규격으로(멱등)."""
    out = OLD_RE.sub(lambda m: tile_open(int(m.group(1)), int(m.group(2)), m.group(3)) + m.group(4) + svg(int(m.group(1))), html)
    assert 'viewBox="8.63 8.63 90.74 90.74"' not in out, f'옛 마크 {out.count("8.63 8.63 90.74 90.74")}개가 남음'
    return out
