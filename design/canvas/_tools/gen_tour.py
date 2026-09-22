# -*- coding: utf-8 -*-
"""첫 실행 안내(투어) 15장 — 탭에 처음 들어갈 때 한 번씩 뜨는 안내. 2026-09-22 사용자 요청 · 시안 승인 뒤 반영.

기존 탭 장(HomeCalendarStrip · Assets · Spending · Goals · Future)을 그대로 읽어 그 위에 어두운 막 + 강조 테두리 + 안내 카드를 얹는다.
강조할 요소의 좌표는 Brave 헤드리스에서 실제 웹폰트로 잰 값(아래 표). 탭 장을 고쳐 카드 위치가 바뀌면 다시 재서 표를 고친다.
규칙(plan/v5-calendar.md §10 11판 · CHANGES-2026-09-22.md):
  · 처음 설치해 첫 실행할 때만. 탭에 처음 들어가면 그 탭의 안내가 1단계부터. 홈 · 자산 · 소비 · 목적지 · 미래 각 3단계.
  · 「건너뛰기」 = 그 탭의 남은 단계를 건너뜀. 다시 보려면 설정 › 도움말 › 「처음 안내 다시 보기」.
  · 저장 settings.onboarding.tourSeen = {home, assets, spending, goals, future} (보호 파일 · 백업 형식 불변).
  · 어두운 막 rgba(16,24,40,.62) · 강조 테두리 브랜드 파랑 4px + 흰 2px(요소의 모서리 그대로) · 카드는 요소 아래 12px, 아래에 자리가 없으면 위.
이 파일은 gen_v5.py 뒤(HomeCalendarStrip 이 다시 써진 뒤)에 돌린다. 다크 짝은 darken 으로 같이 쓴다."""
import pathlib
from gen_common import C, icon
from darken import darken

OUT = pathlib.Path(__file__).resolve().parent.parent
DIM = 'rgba(16,24,40,.62)'
ROOT_OPEN = ('<div style="width: 390px; height: 844px; background: #EDF0F7; color: #101828; display: flex; flex-direction: column; '
             'overflow: hidden; font-variant-numeric: tabular-nums;">')


def coach(target, title, body, step, last, above=False, radius=20):
    """target = (x, y, w, h) 강조할 요소. 카드는 그 아래(기본) 또는 위(above)에 12px 띄운다. 카드 높이를 몰라도 되게 위는 bottom 으로 앉힌다."""
    x, y, w_, h = target
    ring = (f'<div style="position: absolute; left: {x}px; top: {y}px; width: {w_}px; height: {h}px; border-radius: {radius}px; '
            f'box-shadow: 0 0 0 2px rgba(255,255,255,.95), 0 0 0 4px {C["BRAND"]}, 0 0 0 9999px {DIM};"></div>')
    counter = f'<span style="font-size: 11.5px; font-weight: 600; color: {C["INK3"]}; white-space: nowrap;">{step}</span>'
    primary = (f'<span style="display: inline-flex; align-items: center; justify-content: center; height: 40px; padding: 0 20px; border-radius: 12px; '
               f'background: {C["BRAND"]}; color: #FFFFFF; font-size: 14px; font-weight: 600; white-space: nowrap; flex-shrink: 0;">{"알겠어요" if last else "다음"}</span>')
    pos = f'bottom: {844 - y + 12}px;' if above else f'top: {y + h + 12}px;'
    caret_pos = 'bottom: -7px;' if above else 'top: -7px;'
    caret_border = (f'border-right: 1px solid {C["LINE"]}; border-bottom: 1px solid {C["LINE"]};' if above
                    else f'border-left: 1px solid {C["LINE"]}; border-top: 1px solid {C["LINE"]};')
    card_html = (
        f'<div style="position: absolute; left: 14px; width: 362px; {pos} background: {C["SURF"]}; border: 1px solid {C["LINE"]}; border-radius: 18px; '
        f'padding: 16px; display: flex; flex-direction: column; gap: 8px; box-shadow: 0 12px 32px -12px rgba(16,24,40,.45);">'
        f'<div style="position: absolute; {caret_pos} left: 30px; width: 13px; height: 13px; background: {C["SURF"]}; transform: rotate(45deg); {caret_border}"></div>'
        f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px;">'
        f'<span style="display: inline-flex; align-items: center; gap: 5px; height: 22px; padding: 0 9px; border-radius: 99px; background: {C["BRAND_SOFT"]}; '
        f'color: {C["BRAND"]}; font-size: 11.5px; font-weight: 700; letter-spacing: 0.02em;">{icon("help", 12, C["BRAND"], 2.2)}처음 안내</span>{counter}</div>'
        f'<span style="font-size: 16px; font-weight: 700; letter-spacing: -0.02em; line-height: 1.35; color: {C["INK"]};">{title}</span>'
        f'<span style="font-size: 13px; line-height: 1.55; color: {C["INK2"]};">{body}</span>'
        f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px; margin-top: 6px;">'
        f'<span style="font-size: 13px; font-weight: 600; color: {C["INK3"]}; padding: 8px 4px;">건너뛰기</span>{primary}</div></div>')
    return f'<div style="position: absolute; inset: 0; z-index: 5; overflow: hidden;">{ring}{card_html}</div>'


def with_coach(html, overlay):
    assert html.count(ROOT_OPEN) == 1, 'root'
    html = html.replace(ROOT_OPEN, ROOT_OPEN.replace('overflow: hidden;', 'overflow: hidden; position: relative;'), 1)
    k = html.rindex('</div>\n</x-dc>')
    return html[:k] + overlay + html[k:]


# 실측 좌표(x, y, w, h) — 2026-09-22 · 히어로 버튼을 뺀 뒤. 홈: 히어로 296 · 달력 172 · 다음 안내 116. 세그먼트는 모서리 14, 버튼 13, 카드 20.
TOUR = {
    'Home': ('HomeCalendarStrip', '홈', [
        ((14, 90, 362, 296), '여기가 현재 위치예요', '월급에서 이번 달 얼마나 쓸지 예상한 비율이에요. 내 목표 아래면 순항 중으로 표시돼요.', False, 20),
        ((14, 395, 362, 172), '날짜를 누르면 바로 기록', '그날 쓴 금액을 숫자만 넣고 저장하면 끝이에요. 분류는 나중에 소비 탭에서 해도 돼요.', False, 20),
        ((14, 576, 362, 116), '지금 할 일 한 가지', '기록이 쌓이면 가장 효과가 큰 일 하나를 골라 알려 줘요. 누르면 그 화면으로 바로 가요.', True, 20)]),
    'Assets': ('Assets', '자산', [
        ((16, 60, 358, 42), '가진 것과 갚을 것', '자산 구성 · 부채 · 상환 전략 세 탭이에요. 부채가 있으면 상환 전략에서 갚는 순서를 정해요.', False, 14),
        ((14, 114, 362, 275), '순자산 = 자산 − 부채', '여섯 달 흐름을 그래프로 봐요. 자산이나 부채를 고치면 바로 다시 계산돼요.', False, 20),
        ((14, 399, 362, 69), '생활비 몇 달치가 있나요', '현금과 바로 뺄 수 있는 돈으로 생활비를 몇 달 버틸 수 있는지예요. 비상금 목적지와 이어져요.', False, 20)]),
    'Spending': ('Spending', '소비', [
        ((16, 58, 358, 42), '이번 달 · 내역 · 한도', '이번 달은 쓰는 속도, 내역은 기록 정리, 한도는 카테고리별 상한이에요. 달력에서 저장한 기록은 내역에서 분류해요.', False, 14),
        ((14, 112, 362, 342), '계획한 속도로 쓰고 있나요', '실선은 지금까지 쓴 돈, 점선은 월말 예상이에요. 회색 계획선보다 위에 있으면 빠르게 쓰는 중이에요.', False, 20),
        ((14, 464, 362, 289), '카테고리마다 얼마 썼는지', '한도 대비 비율이 100%를 넘으면 빨갛게 표시돼요. 전체 보기에서 한도를 조정해요.', True, 20)]),
    'Goals': ('Goals', '목적지', [
        ((14, 114, 362, 178), '저축을 목적지에 나눠요', '월 저축 여력을 목적지마다 얼마씩 넣을지 정해요. 모자라면 여기서 먼저 알려 줘요.', False, 20),
        ((14, 302, 362, 380), '도착 예상일이 보여요', '지금 속도로 언제 도착하는지 계산해요. 적립을 누르면 그 목적지에 넣은 돈을 기록해요.', True, 20),
        ((14, 692, 362, 46), '목적지를 정해 보세요', '비상금 · 여행 · 전세금처럼 모을 목표예요. 새 목적지 설계 탭에서 한 걸음씩 만들 수도 있어요.', True, 13)]),
    'Future': ('Future', '미래', [
        ((14, 114, 362, 386), '앞으로의 자산 경로', '기간과 투자 환경을 고르면 지금 속도로 자산이 어떻게 자라는지 그려요. 실제 기록은 바뀌지 않아요.', False, 20),
        ((14, 510, 362, 151), '다음 지점까지 얼마나', '1억원처럼 다음 고비까지 몇 달 남았는지 보여 줘요. 저축을 늘리면 앞당겨져요.', True, 20),
        ((14, 671, 362, 103), '보라 점선은 저장되지 않는 가정', '월 소비를 줄이면 10년 뒤 얼마가 달라지는지 시험해 보는 자리예요. 저장 기록과는 따로예요.', True, 20)]),
}
NAMES = [f'Tour{k}{i}' for k, (_, _, steps) in TOUR.items() for i in range(1, len(steps) + 1)]

if __name__ == '__main__':
    for key, (base, label, steps) in TOUR.items():
        html = (OUT / f'{base}.dc.html').read_text(encoding='utf-8')
        n = len(steps)
        for i, (target, title, body, above, radius) in enumerate(steps, 1):
            name = f'Tour{key}{i}'
            light = with_coach(html, coach(target, title, body, f'{label} {i} / {n}', last=(i == n), above=above, radius=radius))
            (OUT / f'{name}.dc.html').write_text(light, encoding='utf-8')
            (OUT / f'Dark{name}.dc.html').write_text(darken(light, name), encoding='utf-8')
            print('wrote', name, '+ Dark' + name)
