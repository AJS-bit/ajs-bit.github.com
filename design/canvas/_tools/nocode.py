# -*- coding: utf-8 -*-
"""보드 글에서 결정 번호 · 점검 번호(D9 · AMEND 2 · home-8 · NUMBERS §4 …)를 걷어 낸다 — fix-up 3.
clean(text) 는 괄호 안이 번호뿐이면 괄호째, 섞여 있으면 번호만 뗀다. find(text) 는 남은 번호를 돌려준다."""
import re
C1 = r'(?:D(?:[1-9]|1\d|20)(?:\s*(?:~|–|-)\s*D(?:[1-9]|1\d|20))?|AMEND(?:\s?[12])?|(?:home|first-run|record|a11y|goals|assets|spending|tasks|future|language-ia)-\d+(?:\s*#\d+(?:\s*·\s*#\d+)*)?(?:\s*[A-D]\b)?|DZ\d|NUMBERS\s*§\s*\d+(?:-\d+)?|NUMBERS)'
CODE = r'(?<![A-Za-z0-9_/.-])' + C1 + r'(?![0-9A-Za-z_])'
SEP = r'\s*(?:·|,|/|\+)\s*'
PURE = re.compile(r'\s?\((?:' + CODE + r')(?:' + SEP + r'(?:' + CODE + r'))*\)')
PURE_FW = re.compile(r'\s?（(?:' + CODE + r')(?:' + SEP + r'(?:' + CODE + r'))*）')
LEAD = re.compile(r'\((?:' + CODE + r')(?:' + SEP + r'(?:' + CODE + r'))*\s*(?:·|—|:)\s*')      # (D9 · basisWhen) → (basisWhen)
TRAIL = re.compile(r'(?:' + SEP.replace(r'\+', '') + r'|\s*—\s*)(?:' + CODE + r')(?:' + SEP + r'(?:' + CODE + r'))*(?=\s*\))')   # (… · D9) → (…)
MID = re.compile(r'\s*·\s*(?:' + CODE + r')(?=\s*·)')
FIND = re.compile(CODE)


def clean(s):
    s = PURE.sub('', s)
    s = PURE_FW.sub('', s)
    s = LEAD.sub('(', s)
    s = TRAIL.sub('', s)
    s = MID.sub('', s)
    return s


def find(s):
    return [m.group(0) for m in FIND.finditer(s)]
