# -*- coding: utf-8 -*-
"""낱말 중간 꺾임 막기(D14 · a11y-11) — 아트보드 HTML 의 글자 사이에 `white-space:nowrap` 묶음을 넣는다.

keep-all 이어도 브라우저는 닫는 낫표 뒤(「…」로 · 」(안 …) · 한글 바로 뒤 여는 괄호(선(소비 …) · 붙임표(record-13 ·
NAVI-NOTIFY-…)에서 줄을 바꾼다. 그런 자리만 골라 짧게 묶는다 — 글자 · 문구는 바꾸지 않는다(모양만).

- 짧은 낫표 · 따옴표(안 14자 이하) + 뒤 조사: 「직접 ›」는 · ‘가정’은 → 통째로
- 긴 낫표의 끝 낱말 + 」 + 바로 붙은 글자: …썼어요」로 · …적기」(안
- 한글 바로 뒤 괄호: 선(소비 · 월급(실수령)의 · 조정(HomeTargetEditor)에서 — 닫는 괄호까지, 못 닫으면 괄호 안 첫 낱말까지
- 숫자 % + 조사: 50%로 · 60%를(% 뒤 꺾임)
- 붙임표 낱말: record-11 #4 · a11y-1 · NAVI-NOTIFY-MEETING-2026-09-23.md
- 띄어 쓰지 않은 가운뎃점 낱말: 저축·투자와
- 낫표 안 링크 화살표는 앞 낱말과: 「… 고르기 ›」

flex · grid 상자 바로 안의 글자는 건드리지 않는다(묶으면 flex 항목이 셋으로 쪼개져 간격이 생긴다). svg · style 안도 그대로.
표식 `<span style="white-space:nowrap">`(띄어쓰기 없음) 안의 글자는 다시 묶지 않아 여러 번 돌려도 같다(멱등).
gen_v5 · gen_v5_sheets · gen_v5_screens(gen_v5.w) · gen_notify · refresh_components_v5 가 DZ4 장에 쓴다(2026-09-26).
"""
import re

MARK = '<span style="white-space:nowrap">'
_VOID = {'br', 'img', 'input', 'meta', 'link', 'hr', 'wbr', 'col', 'source', 'path', 'circle', 'line', 'rect', 'polyline', 'polygon', 'ellipse', 'stop', 'use'}
_TOK = re.compile(r'<!--[\s\S]*?-->|<[^>]+>|[^<]+')
_RULES = [      # (패턴, 최대 길이)
    (re.compile(r'[「‘“][^「」‘’“”<>]{1,14}[」’”][가-힣]{0,3}'), 26),          # 짧은 낫표 · 따옴표 + 조사
    (re.compile(r'[^\s<>「‘“]*[」’”](?=[^\s<>])[^\s<>]{1,8}'), 26),          # 긴 낫표의 끝 낱말 + 」 + 붙은 글자
    # 한글 바로 뒤 괄호 — 닫는 괄호까지(안 24자 이하 · 뒤 조사 3자) 또는 괄호 안 첫 낱말까지. 영문 이름 중간에서 끊지 않는다(2026-09-27 fix-up 5 · 예전 12자에서 잘려 「조정(HomeTargetEdito」에서 묶음이 끝났다)
    (re.compile(r'[^\s<>]*[가-힣」’”]\((?:[^\s<>)]{1,24}\)[^\s<>]{0,3}|[^\s<>)]{1,12}(?=\s|$))'), 34),
    (re.compile(r'[0-9][0-9,.]*%[가-힣]{1,3}'), 12),                           # 숫자 % + 조사(50%로 · 60%를) — keep-all 이어도 % 뒤에서 꺾인다(2026-09-27 fix-up 5)
    (re.compile(r'[A-Za-z][A-Za-z0-9]*(?:-[A-Za-z0-9.]+)+(?: #\d+)?'), 40),   # 붙임표 낱말(파일 이름 포함)
    (re.compile(r'[^\s<>]*[가-힣]·[가-힣][^\s<>]*'), 26),                      # 띄어 쓰지 않은 가운뎃점(저축·투자와)
    (re.compile(r'[^\s<>「‘“]+ (?:›|&rsaquo;)[」’”][^\s<>]{0,3}'), 26),        # 낫표 안 링크 화살표(「… 고르기 ›」)는 앞 낱말과
]
_MAXLEN = 40


def _is_flex(tag):
    m = re.search(r'style="([^"]*)"', tag)
    return bool(m and re.search(r'display:\s*(?:inline-)?(?:flex|grid)', m.group(1)))


def _wrap(text):
    spans = []
    for rx, mx in _RULES:
        for m in rx.finditer(text):
            a, b = m.span()
            if b - a <= mx and len(text[a:b].strip()) > 1:
                spans.append([a, b])
    if not spans:
        return text
    spans.sort()
    merged = [spans[0]]
    for a, b in spans[1:]:
        if a <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], b)
        else:
            merged.append([a, b])
    out, k = [], 0
    for a, b in merged:
        if b - a > _MAXLEN * 1.5:          # 합쳐져 너무 길어지면 묶지 않는다(넘침 방지)
            continue
        out.append(text[k:a] + MARK + text[a:b] + '</span>')
        k = b
    out.append(text[k:])
    return ''.join(out)


def nobreak(html):
    """HTML 전체에서 글자 조각만 골라 묶는다. <x-dc> 밖(머리 · helmet)은 그대로."""
    out, stack, prev = [], [], ''
    for m in _TOK.finditer(html):
        t = m.group(0)
        if t.startswith('<!--'):
            out.append(t)
            continue
        if t.startswith('<'):
            name = re.match(r'</?\s*([A-Za-z0-9:-]+)', t)
            name = name.group(1).lower() if name else ''
            if t.startswith('</'):
                if any(n_ == name for n_, _ in stack):      # 열린 적 없는 닫는 태그(</path> 등)로 스택을 비우지 않는다
                    while stack:
                        n_, _ = stack.pop()
                        if n_ == name:
                            break
            elif not (t.endswith('/>') or name in _VOID or t.startswith('<!')):
                stack.append((name, t))
            out.append(t)
            prev = t
            continue
        names = [n_ for n_, _ in stack]
        skip = (not t.strip() or 'svg' in names or 'style' in names or 'script' in names or 'helmet' in names or 'head' in names
                or not stack or prev == MARK or _is_flex(stack[-1][1]))
        out.append(t if skip else _wrap(t))
    return ''.join(out)
