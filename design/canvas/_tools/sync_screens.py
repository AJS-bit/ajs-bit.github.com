# -*- coding: utf-8 -*-
"""canvas.json(=gen_canvas.py 결과)의 제목 · 페이지 · 크기를 design/screens.json에 맞춘다.

아트보드 크기는 세 곳(.dc.html 루트 · gen_canvas.py · screens.json)이 같아야 한다. 이 스크립트는
gen_canvas.py 뒤에 돌려 셋째 자리를 맞추고, .dc.html 루트 크기와 어긋나는 장이 있으면 알려 준다.
새 장은 아래 SOURCE에 출처(앱 파일 또는 계획 절)를 적어야 한다.
"""
import json, pathlib, re, sys

CANVAS = pathlib.Path(__file__).resolve().parent.parent
DESIGN = CANVAS.parent

SOURCE = {   # 새 장의 출처 — 기존 장은 screens.json에 이미 있는 값을 그대로 둔다
    'TourDebts1': '미구현 · 첫 실행 안내 · plan/v5-calendar.md §10 11판 · design/CHANGES-2026-09-22.md',
    'TourDebts2': '미구현 · 첫 실행 안내 · plan/v5-calendar.md §10 11판 · design/CHANGES-2026-09-22.md',
    'TourDebts3': '미구현 · 첫 실행 안내 · plan/v5-calendar.md §10 11판 · design/CHANGES-2026-09-22.md',
    'TourStrategy1': '미구현 · 첫 실행 안내 · plan/v5-calendar.md §10 11판 · design/CHANGES-2026-09-22.md',
    'TourStrategy2': '미구현 · 첫 실행 안내 · plan/v5-calendar.md §10 11판 · design/CHANGES-2026-09-22.md',
    'TourStrategy3': '미구현 · 첫 실행 안내 · plan/v5-calendar.md §10 11판 · design/CHANGES-2026-09-22.md',
    'TourLedger1': '미구현 · 첫 실행 안내 · plan/v5-calendar.md §10 11판 · design/CHANGES-2026-09-22.md',
    'TourLedger2': '미구현 · 첫 실행 안내 · plan/v5-calendar.md §10 11판 · design/CHANGES-2026-09-22.md',
    'TourLedger3': '미구현 · 첫 실행 안내 · plan/v5-calendar.md §10 11판 · design/CHANGES-2026-09-22.md',
    'TourLimits1': '미구현 · 첫 실행 안내 · plan/v5-calendar.md §10 11판 · design/CHANGES-2026-09-22.md',
    'TourLimits2': '미구현 · 첫 실행 안내 · plan/v5-calendar.md §10 11판 · design/CHANGES-2026-09-22.md',
    'TourLimits3': '미구현 · 첫 실행 안내 · plan/v5-calendar.md §10 11판 · design/CHANGES-2026-09-22.md',
    'TourGoalDesign1': '미구현 · 첫 실행 안내 · plan/v5-calendar.md §10 11판 · design/CHANGES-2026-09-22.md',
    'TourGoalDesign2': '미구현 · 첫 실행 안내 · plan/v5-calendar.md §10 11판 · design/CHANGES-2026-09-22.md',
    'TourGoalDesign3': '미구현 · 첫 실행 안내 · plan/v5-calendar.md §10 11판 · design/CHANGES-2026-09-22.md',
    'TourPayoff1': '미구현 · 첫 실행 안내 · plan/v5-calendar.md §10 11판 · design/CHANGES-2026-09-22.md',
    'TourPayoff2': '미구현 · 첫 실행 안내 · plan/v5-calendar.md §10 11판 · design/CHANGES-2026-09-22.md',
    'TourPayoff3': '미구현 · 첫 실행 안내 · plan/v5-calendar.md §10 11판 · design/CHANGES-2026-09-22.md',
    'TourHome1': '미구현 · 첫 실행 안내 · plan/v5-calendar.md §10 11판 · design/CHANGES-2026-09-22.md',
    'TourHome2': '미구현 · 첫 실행 안내 · plan/v5-calendar.md §10 11판 · design/CHANGES-2026-09-22.md',
    'TourHome3': '미구현 · 첫 실행 안내 · plan/v5-calendar.md §10 11판 · design/CHANGES-2026-09-22.md',
    'TourAssets1': '미구현 · 첫 실행 안내 · plan/v5-calendar.md §10 11판 · design/CHANGES-2026-09-22.md',
    'TourAssets2': '미구현 · 첫 실행 안내 · plan/v5-calendar.md §10 11판 · design/CHANGES-2026-09-22.md',
    'TourAssets3': '미구현 · 첫 실행 안내 · plan/v5-calendar.md §10 11판 · design/CHANGES-2026-09-22.md',
    'TourSpending1': '미구현 · 첫 실행 안내 · plan/v5-calendar.md §10 11판 · design/CHANGES-2026-09-22.md',
    'TourSpending2': '미구현 · 첫 실행 안내 · plan/v5-calendar.md §10 11판 · design/CHANGES-2026-09-22.md',
    'TourSpending3': '미구현 · 첫 실행 안내 · plan/v5-calendar.md §10 11판 · design/CHANGES-2026-09-22.md',
    'TourGoals1': '미구현 · 첫 실행 안내 · plan/v5-calendar.md §10 11판 · design/CHANGES-2026-09-22.md',
    'TourGoals2': '미구현 · 첫 실행 안내 · plan/v5-calendar.md §10 11판 · design/CHANGES-2026-09-22.md',
    'TourGoals3': '미구현 · 첫 실행 안내 · plan/v5-calendar.md §10 11판 · design/CHANGES-2026-09-22.md',
    'TourFuture1': '미구현 · 첫 실행 안내 · plan/v5-calendar.md §10 11판 · design/CHANGES-2026-09-22.md',
    'TourFuture2': '미구현 · 첫 실행 안내 · plan/v5-calendar.md §10 11판 · design/CHANGES-2026-09-22.md',
    'TourFuture3': '미구현 · 첫 실행 안내 · plan/v5-calendar.md §10 11판 · design/CHANGES-2026-09-22.md',
    'HomeSetupStocksOn': 'v4 미구현 · plan/v4-stocks.md §3', 'SettingsHomeEntry': 'v4 미구현 · plan/v4-stocks.md §3 · plan/v5-calendar.md §12-2',
    'HomeLayoutEdit': 'v4 미구현 · plan/v4-stocks.md §3 · plan/v5-calendar.md §12-2 · §7', 'DestPayoff': 'v4 미구현 · plan/v4-stocks.md §4',
    'DaySheetScrolled': 'v5 · plan/v5-calendar.md §4', 'DaySheetNoSpend': 'v5 · plan/v5-calendar.md §4 · §8',
    'ReviewListSheet': 'v5 · plan/v5-calendar.md §3-3', 'HomeDefaultScroll': 'v5 · plan/v5-calendar.md §3-1 · §10 2단계',
    'CalendarStatusLines': 'v5 · plan/v5-calendar.md §3-3', 'DaySheetNoSpendStates': 'v5 · plan/v5-calendar.md §4 · §8',
    'DoneCardStates': 'v5 · plan/v5-calendar.md §4-4', 'DaySheetStates': 'v5 · plan/v5-calendar.md §4 · §8',
    'LedgerV5': 'v5 · plan/v5-calendar.md §9 · components/navi/spending-tab.tsx', 'MonthlyCloseV5': 'v5 · plan/v5-calendar.md §9',
    'TransactionAddFromDaySheet': 'v5 · plan/v5-calendar.md §4',
    'InsufficientElsewhere': 'v5 · plan/v5-calendar.md §3-4 · §9-22', 'FutureProvisional': 'v5 · plan/v5-calendar.md §3-4',
    'EtcSubline': 'v5 · plan/v5-calendar.md §5-3 · §9', 'LimitCardCases': 'v5 · plan/v5-calendar.md §10 3단계',
    'RecurringPrefill': 'v5 · plan/v5-calendar.md §10 3단계', 'ImportBackupNotes': 'v5 · plan/v5-calendar.md §10 3단계',
    'DesktopHomeV5': 'v5 · 데스크톱 달력 자리(2026-09-21 결정 · plan/v5-calendar.md §10 10판 메모)',
}

canvas = json.loads((CANVAS / 'canvas.json').read_text(encoding='utf-8'))
pages = {p['id']: p['name'] for p in canvas['pages']}
path = DESIGN / 'screens.json'
doc = json.loads(path.read_text(encoding='utf-8'))
old = {a['name']: a for a in doc['artboards']}
out, bad = [], []
for a in canvas['artboards']:
    name = a['file'][:-len('.dc.html')]
    dark = name.startswith('Dark')
    base = ('Main' if name == 'DarkHome' else name[4:]) if dark else name
    e = dict(old.get(name) or {})
    src = e.get('source') or (old.get(base) or {}).get('source') or SOURCE.get(base)
    if not src:
        bad.append(f'출처 없음: {name} — SOURCE에 추가')
        src = ''
    e.update({'file': a['file'], 'name': name, 'base': base, 'theme': 'dark' if dark else 'light',
              'title': a['title'], 'page': pages[a['page']], 'w': a['w'], 'h': a['h'], 'source': src})
    out.append(e)
    html = (CANVAS / a['file']).read_text(encoding='utf-8').split('</helmet>')[1]
    m = re.search(r'width:\s*(\d+)px;\s*height:\s*(\d+)px', html)
    if not m or (int(m.group(1)), int(m.group(2))) != (a['w'], a['h']):
        bad.append(f'크기 어긋남: {name} — 파일 {m.group(1) if m else "?"}×{m.group(2) if m else "?"} · 등록부 {a["w"]}×{a["h"]}')
gone = sorted(set(old) - {e['name'] for e in out})
order = {n: i for i, n in enumerate(old)}   # 있던 장은 제자리, 새 장은 캔버스 순서로 끝에 — diff를 작게
out.sort(key=lambda e: order.get(e['name'], len(order)))
doc['artboards'] = out
path.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(f'screens.json: {len(out)}장 (라이트 {sum(1 for e in out if e["theme"] == "light")} · 다크 {sum(1 for e in out if e["theme"] == "dark")})')
for g in gone:
    print('캔버스에서 빠진 장(목록에서 지움):', g)
for b in bad:
    print('!', b)
sys.exit(1 if bad else 0)
