# -*- coding: utf-8 -*-
"""canvas.json(=gen_canvas.py 결과)의 제목 · 페이지 · 크기를 design/screens.json에 맞춘다.

아트보드 크기는 세 곳(.dc.html 루트 · gen_canvas.py · screens.json)이 같아야 한다. 이 스크립트는
gen_canvas.py 뒤에 돌려 셋째 자리를 맞추고, .dc.html 루트 크기와 어긋나는 장이 있으면 알려 준다.
새 장은 아래 SOURCE에 출처(앱 파일 또는 계획 절)를 적어야 한다.
"""
import html as html_mod, json, pathlib, re, sys

import nocode

CANVAS = pathlib.Path(__file__).resolve().parent.parent
DESIGN = CANVAS.parent

SOURCE = {   # 새 장의 출처 — 기존 장은 screens.json에 이미 있는 값을 그대로 둔다
    # 2026-09-26 DZ4 새 장(앱 v5-stage1 a724aac)
    'HomeTargetEditor': 'components/navi/home-hero.tsx 소비 목표 조정 편집기 (home-1 · D1 · D4)',
    'HomeMonthStart': 'components/navi/calendar-card.tsx 최근 7일 제목 · home-hero 0건 (home-17 · home-6 · D9 · first-run-5)',
    'HomeSampleMode': 'app/page.tsx 샘플 띠 · calendar-card 샘플 문장 (D8 · language-ia-21 · first-run-17 · D9)',
    'DaySheetDeleted': 'components/navi/day-sheet.tsx inlineNotice (record-6 · D10)',
    'DaySheetPastEmpty': 'components/navi/day-sheet.tsx 어제 · 빈 날 (record-11 · record-18)',
    'DaySheetEditMoved': 'components/navi/day-sheet.tsx moved (record-15)',
    'ClassifySheetPicker': 'components/navi/classify-sheet.tsx 줄 고르기 펼침 (spending-3 · a11y-1)',
    'PayoffStates': 'components/navi/payoff-plan.tsx 초안 · 다 갚지 못함 · 최소 상환만 · 모자람 (future-2/4/6/11/22/25 · D6 · D13 · D15)',
    'FutureStates': 'components/navi/future-view.tsx 절감 가정 · 기록 없음 · 늘어나는 대출 · 초안 · 자세히 (future-1/2/5/11/12/19/21)',
    'HomeGlanceRows': 'components/navi/home-glance.tsx 자산 한눈에 줄 펼침 (home-12)',
    'SampleModeTabs': 'app/page.tsx 샘플 띠 (D8 · language-ia-21 · first-run-17)',
    'DebtUnpayable': 'components/navi/asset-view.tsx 부채 · 상환 계획 요약 (tasks-4 · D7 · D11 · D15)',
    'SettingsNotify': '미구현 · 기기 알림 · design/CHANGES-2026-09-23.md · NAVI-NOTIFY-MEETING-2026-09-23.md', 'NotifyCases': '미구현 · 기기 알림 · design/CHANGES-2026-09-23.md',
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
    # 2026-09-25 앱 따라잡기(v5-stage1 a724aac · 사용성 점검 140건) — DZ1 새 장
    'ProfileDialogNoItems': 'components/navi/numbers-sheet.tsx (D5 · first-run-2)', 'SalarySheet': 'components/navi/salary-sheet.tsx (D5 · first-run-22)',
    'NetWorthRatioSheet': 'components/navi/net-worth-ratio-sheet.tsx (home-8)', 'AssetEditDialog': 'components/navi/asset-view.tsx (assets-4)',
    'AssetBalanceCheck': 'components/navi/balance-check-sheet.tsx (assets-15)', 'RecurringDialogOverlap': 'components/navi/spending-view.tsx 반복 기록 (record-2)',
    'SpendingPastOpen': 'components/navi/spending-overview.tsx 월 마감 카드 (spending-4 · D9)', 'SpendingPastChanged': 'components/navi/spending-overview.tsx · reclose-spend-dialog.tsx (record-1 · D9)',
    'AssetDebtTypes': 'lib/navi-asset-labels.ts · components/navi/asset-view.tsx (assets-6 · assets-7 · assets-14 · assets-23)',
    # 2026-09-26 DZ2 새 장
    'GoalsStates': 'components/navi/goals-view.tsx 매달 모으는 돈 가정 · 한 줄 펼침 · 도착한 목적지 · 목표일 없음 · 도착하기 어려움 · 부채 상환 늦음(펼침) · goal-tools.tsx 설계 저장 미리 보기 (goals-9 · goals-10 · goals-7 · goals-24 · goals-26 · goals-8 · goals-3 · D12 · D13)',
    'GoalDesignStates': 'components/navi/goal-tools.tsx 처음 · 다른 금액으로 계산해 보기 (goals-16 · goals-28 · D13)',
    # 2026-09-26 DZ5 첫 실행 안내 새 장
    'TourHomeChecklist': 'components/navi/first-run-tour.tsx · lib/navi-tour.ts TOUR_HOME_CHECKLIST_STEP · components/navi/start-checklist.tsx (first-run-5 · AMEND 2)',
    'TourHelpReplay': 'components/navi/first-run-tour.tsx · lib/navi-tour-policy.ts tourBadge · showTourHelp (first-run-3 · AMEND 2 · D14)',
    'TourRules': 'lib/navi-tour.ts · lib/navi-tour-policy.ts isEmptyScreen · components/navi/first-run-tour.tsx · app/first-run-tour.css (AMEND 2 · first-run-3/4/21 · D7 · D8)',
    # 2026-09-27 fix-up 2 새 장
    'TourHomeSample1': 'components/navi/first-run-tour.tsx · lib/navi-tour.ts TOUR_STEPS · 샘플 띠 app/page.tsx (D8 · language-ia-21 · AMEND 2)',
    'HeroOverTarget': 'components/navi/home-hero.tsx 배지 · 오른쪽 줄 · 셋째 칸 (D1 · D4 · home-1 · home-8)',
    # 2026-09-27 fix-up 3 새 장
    'HomePrimaryGoal': 'app/page.tsx 홈 카드 primaryGoal · lib/navi-home-layout.ts HOME_CARD_KEYS (goals-14 · first-run-14)',
    'HomeTargetSaved': 'components/navi/home-hero.tsx 소비 목표 저장 · components/navi/save-notice.tsx (home-1 · D1 · D4 · D10)',
    'AssetsStale': 'components/navi/asset-view.tsx 잔액 확인 띠 · lib/navi-asset-freshness.ts (assets-15)',
    'AlertsPanelInfo': 'lib/navi-alert-rows.ts 참고 줄 · components/navi/coach-panel.tsx 알림 (home-10 · assets-15)',
    'GoalDialogPreview': 'components/navi/goal-dialog.tsx 저축 유형 · 저장 전 미리 보기 (goals-15 · goals-3 · D1)',
}

# 옛 출처가 「미구현」이던 장 가운데 앱(v5-stage1 a724aac · 2026-09-25 사용성 점검 140건 반영)에 들어간 것 — 옛 값보다 이 값이 먼저다(2026-09-26 DZ5).
# v4 2 ~ 5단계(탭 합치기 · 주식)는 아직 앱에 없어 그대로 둔다.
_TOUR_SRC = 'components/navi/first-run-tour.tsx · lib/navi-tour.ts TOUR_STEPS · lib/navi-tour-policy.ts (AMEND 2 · first-run-3/4/21)'
SOURCE_NOW = {
    **{f'Tour{k}{i}': _TOUR_SRC for k in ('Home', 'Assets', 'Spending', 'Goals', 'Future', 'Debts', 'Strategy', 'Ledger', 'Limits', 'GoalDesign', 'Payoff')
       for i in (1, 2, 3)},
    'IntroPosition': 'components/navi/intro-flow.tsx (first-run-13 · plan/v4-stocks.md §3)',
    'IntroRoute': 'components/navi/intro-flow.tsx (first-run-13 · plan/v4-stocks.md §3)',
    'IntroDestination': 'components/navi/intro-flow.tsx (first-run-13 · plan/v4-stocks.md §3)',
    'HomeSetup': 'components/navi/home-layout-editor.tsx (AMEND 1 · first-run-12/14/15/16 · plan/v4-stocks.md §3)',
    'HomeSetupStocksOn': 'components/navi/home-layout-editor.tsx (AMEND 1 · first-run-16 · plan/v4-stocks.md §3)',
    'HomeLayoutEdit': 'components/navi/home-layout-editor.tsx (first-run-15 · plan/v5-calendar.md §12-2)',
    'SettingsHomeEntry': 'components/navi/settings-sheet.tsx (D5 · home-9)',
    'Onboarding': 'components/navi/data-choice-screen.tsx (first-run-19 · D8 · AMEND 1)',
    'HomeConfigured': 'app/page.tsx · components/navi/start-checklist.tsx · home-hero.tsx (first-run-5 · first-run-14 · D7 · D9)',
    'HomeCalendarStrip': 'components/navi/calendar-card.tsx · home-hero.tsx (plan/v5-calendar.md §3)',
    'HomeCalendar': 'components/navi/calendar-card.tsx (plan/v5-calendar.md §3)',
    'HomeCalendar360': 'components/navi/calendar-card.tsx (plan/v5-calendar.md §3)',
    'HomeCalendarPrev': 'components/navi/calendar-card.tsx (plan/v5-calendar.md §3 · home-18)',
    'CalendarCells': 'components/navi/calendar-card.tsx (plan/v5-calendar.md §3 · record-11)',
    'CalendarGridSizes': 'components/navi/calendar-card.tsx (plan/v5-calendar.md §3 · home-17)',
    'DaySheet': 'components/navi/day-sheet.tsx (plan/v5-calendar.md §4)', 'DaySheetList': 'components/navi/day-sheet.tsx (plan/v5-calendar.md §4)',
    'DaySheetEdit': 'components/navi/day-sheet.tsx (plan/v5-calendar.md §4 · record-15)', 'DaySheet360': 'components/navi/day-sheet.tsx (plan/v5-calendar.md §4)',
    'DaySheetConfirm': 'components/navi/day-sheet.tsx (plan/v5-calendar.md §4 · record-3 · record-5)',
    'DoneCard': 'components/navi/done-card.tsx (plan/v5-calendar.md §4-4 · record-6 · record-20)',
    'ClassifySheet': 'components/navi/classify-sheet.tsx (plan/v5-calendar.md §5-4 · spending-3)',
    'HeroInsufficient': 'components/navi/home-hero.tsx (plan/v5-calendar.md §3-4 · D9)', 'HeroFootnotes': 'components/navi/home-hero.tsx (plan/v5-calendar.md §3-4 · home-8)',
    'SettingsNotify': 'components/navi/notify-settings.tsx (plan/v5-calendar.md §14 · tasks-12)', 'NotifyCases': 'lib/navi-notify.ts · components/navi/notify-settings.tsx (plan/v5-calendar.md §14)',
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
    src = SOURCE_NOW.get(base) or e.get('source') or (old.get(base) or {}).get('source') or SOURCE.get(base)
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
    if not dark:      # 그린 글에는 결정 · 점검 번호(D9 · AMEND 2 · home-8 · NUMBERS §4 …)를 쓰지 않는다 — 번호는 설계 문서(CHANGES · SPEC)에만(2026-09-27 fix-up 3)
        txt = html_mod.unescape(re.sub(r'<[^>]+>', '', re.sub(r'<style[\s\S]*?</style>', '', html)))
        codes = nocode.find(txt)
        if codes:
            bad.append(f'보드 글에 결정 · 점검 번호: {name} — {", ".join(sorted(set(codes)))[:120]}')
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
