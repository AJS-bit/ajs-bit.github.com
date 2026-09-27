# -*- coding: utf-8 -*-
"""시안 계산기가 원본 엔진과 같은 답을 내는지 대조한다.

    python3 crosscheck.py

1. amort.py ↔ engine_ref.py(simulateDebt 포팅) — 다 갚는 달 · 총이자
2. engine_ref.py ↔ 앱이 실제로 낸 값(app_ref.json) — 상환 방식 · 추가 상환액마다 개월 · 이자 · 부채별 다 갚는 달
3. goal_alloc.py ↔ app_ref.json — 매달 모을 수 있는 돈 · 모두 도착하려면 · 목적지별 필요한 돈 · 매달 넣을 돈 · 도착 달 · 목표일 대비
4. limits.py ↔ app_ref.json — 판정 선(D1) · 저축 · 상환 계획 참고 금액 · 오늘 포함 남은 날 · 하루 금액 · 히어로 오른쪽 줄
5. projection.py ↔ app_ref.json — 10년 뒤 순자산(투자 환경 셋) · 다음 자산 지점 · 소비 절감 가정 · 기간별
6. design/sample-data.json 의 derived 값 ↔ 위 계산

app_ref.json 은 `node app_ref.cjs`가 앱(v5-stage1) 계산 코드를 시안 사용자(sample_state.cjs)에 돌려 만든 기준값이다.
앱이 바뀌면 app_ref.cjs를 다시 돌리고 이 파일을 통과시킨다. 어긋나면 계산기(파이썬)가 틀린 것이다 — 규칙 5 「엔진이 맞다」.
"""
import json
import math
import sys
import pathlib

HERE = pathlib.Path(__file__).parent
sys.path.insert(0, str(HERE))
from amort import Debt, simulate  # noqa: E402
from engine_ref import simulate_debt, ym  # noqa: E402
from sample import load, month_label  # noqa: E402
import goal_alloc  # noqa: E402
import limits  # noqa: E402
import projection  # noqa: E402

DEBTS = [dict(name='주택담보대출', balance=6200, apr=3.4,  minimum=32),
         dict(name='신용대출',     balance=2200, apr=6.8,  minimum=20),
         dict(name='학자금대출',   balance=280,  apr=2.5,  minimum=5),
         dict(name='카드 할부',    balance=180,  apr=14.5, minimum=20)]
MINE = [Debt(d['name'], d['balance'], d['apr'], d['minimum']) for d in DEBTS]
CASES = [('고금리 우선 +15만', 'avalanche', 15), ('소액 우선 +15만', 'snowball', 15), ('추가 없이(기준선)', 'avalanche', 0)]

bad = 0


def check(ok, text):
    global bad
    bad += not ok
    print(f'  {"✓" if ok else "✗"} {text}')


def near(a, b, tol=1.0):
    if a is None or b is None:
        return a is b
    return abs(a - b) <= tol


def main():
    ref = json.loads((HERE / 'app_ref.json').read_text(encoding='utf-8'))
    S = load()
    now = S['now']
    print(f'기준값: 앱 {ref["app"]} · app_ref.json\n')

    print('1. amort.py ↔ engine_ref.py (만원)')
    for tag, st, ex in CASES:
        a = simulate(MINE, ex, order=('snowball' if st == 'snowball' else 'avalanche'))
        b = simulate_debt(DEBTS, ex, st)
        ay, am = a['end']
        check(a['months'] == b['months'] and abs(a['interest'] - b['interest']) < 1 and f'{ay}년 {am}월' == ym(b['months']),
              f'{tag:14} amort {a["months"]}개월 {a["interest"]:,.0f}만 {ay}년 {am}월 · 엔진 {b["months"]}개월 {b["interest"]:,.0f}만 {ym(b["months"])}')

    print('\n2. engine_ref.py ↔ 앱 simulateDebt (원)')
    won = [dict(name=d['name'], balance=d['balance'], apr=d['apr'], minimum=d['minimum']) for d in S['debts']]
    for key, app in ref['payoff'].items():
        if not (key == 'current' or key.split('_')[0] in ('avalanche', 'snowball')) or not isinstance(app, dict) or 'months' not in app:
            continue
        st, ex = ('current', 0) if key == 'current' else (key.split('_')[0], int(key.split('_')[1]))
        r = simulate_debt(won, ex, st, unit=1)
        paid = {n: p for n, p, _ in r['order']}
        orders = all(paid[o['name']] == o['paidOffAt'] for o in app['order'])
        label = month_label(now.year, now.month, r['months'])
        check(r['months'] == app['months'] and near(r['interest'], app['interest']) and orders and label == app['label'],
              f'{key:16} {r["months"]}개월 {label} · 이자 {r["interest"]:,.0f}원  (앱 {app["months"]}개월 {app["label"]} · {app["interest"]:,.0f}원)')

    print('\n3. goal_alloc.py ↔ 앱 naviGoalAllocation')
    a = goal_alloc.allocate(S)
    g = ref['goals']
    check(near(a['budget'], g['budget']) and near(a['totalRequired'], g['totalRequired']) and near(a['surplus'], g['surplus']),
          f'매달 모을 수 있는 돈 {a["budget"]:,.0f} · 모두 도착하려면 {a["totalRequired"]:,.0f} · 남는(−모자란) 돈 {a["surplus"]:,.0f}')
    rows = {r['name']: r for r in a['rows']}
    check([r['name'] for r in a['rows']] == [r['name'] for r in g['rows']], '목록 순서(우선순위 · 남은 달 · 이름)')
    for app in g['rows']:
        mine = rows[app['name']]
        check(near(mine['required'], app['required']) and near(mine['allocated'], app['allocated']) and near(mine['weight'], app['weight'], 1e-6)
              and near(mine['eta'], app['etaMonths'], 1e-4) and mine['arrival'] == app['arrival'] and mine['deadline']['text'] == app['deadline']['text'],
              f'{app["name"]:14} 필요 {mine["required"]:>10,.0f} · 매달 {mine["allocated"]:>10,.0f} · {mine["arrival"]} · {mine["deadline"]["text"]}')
    S2 = load()
    for x in S2['goals']:
        if x['kind'] == 'emergency':
            x['saved'] += 500_000
    em = next(r for r in goal_alloc.allocate(S2)['rows'] if r['type'] == 'emergency')
    app = ref['contribute']['after']
    check(near(em['required'], app['required']) and near(em['allocated'], app['allocated']) and em['arrival'] == app['arrival'],
          f'적립 50만 뒤 비상금 필요 {em["required"]:,.0f} · 매달 {em["allocated"]:,.0f} · {em["arrival"]}')
    req = goal_alloc.required_saving(30_000_000, 5_000_000, 84, 0.04)
    check(near(req, ref['design']['required']), f'새 목적지 설계 결혼 자금 필요한 돈 {req:,.0f}원')

    print('\n4. limits.py ↔ 앱 naviSpendingLimit · 한도 표시')
    lim = ref['limit']
    check(limits.verdict_total(S) == lim['total'] and near(limits.from_income(S), lim['fromIncome']) and near(limits.plan_cap_info(S), lim['planCapInfo']),
          f'판정 선 {limits.verdict_total(S):,.0f} · 저축 · 상환 계획 참고 {limits.from_income(S):,.0f}')
    check(limits.days_left() == ref['month']['daysLeftInclusive'], f'오늘 포함 {limits.days_left()}일 남음')
    for key, app in ref['scenes'].items():
        mine = limits.scene(S, app['spent'])
        check(mine['dailyWon'] == app['dailyWon'] and mine['line'] == app['line'],
              f'{key:16} 쓴 돈 {app["spent"]:>9,} → 오늘 포함 하루 {mine["dailyWon"]:,}원 · {mine["line"]}')
    for extra, app in ref['payoff']['planCap'].items():
        e = int(extra)
        check(near(limits.from_income(S, e), app['fromIncome']) and near(projection.capacity(S, e), ref['payoff']['capacity'][extra]),
              f'추가 상환 {e:>7,} → 매달 남는 돈 {projection.capacity(S, e):,.0f} · 계획 참고 {limits.from_income(S, e):,.0f}')

    print('\n5. projection.py ↔ 앱 naviProject')
    fut = ref['future']
    for sc in ('bad', 'base', 'good'):
        p = projection.project(S, 120, sc)
        fin = p['series'][-1]['net']
        check(near(fin, fut[sc]['final']) and projection.estimate_text(fin) == fut[sc]['estimate'] and projection.short_estimate(fin) == fut[sc]['short']
              and near(projection.scenario_rate(S['expected_return'], sc), fut[sc]['rate'], 1e-6),
              f'{sc:4} 연 {projection.scenario_rate(S["expected_return"], sc) * 100:.1f}% · 10년 뒤 {fin:,.0f} {projection.estimate_text(fin)}')
    for y, app in fut['years'].items():
        fin = projection.project(S, int(y) * 12, 'base')['series'][-1]['net']
        check(near(fin, app['final']), f'{y}년 뒤 {projection.estimate_text(fin)}')
    for m, app in zip(projection.milestones(S), fut['milestones']):
        check(m['target'] == app['target'] and m['when'] == app['whenText'] and m['date'] == app['dateText'],
              f'다음 자산 지점 {m["target"]:,} · {m["when"]} · {m["date"]}')
    cut = projection.project(S, 120, 'base', spend_delta=150_000)['series'][-1]['net']
    check(near(cut, fut['cut15']['final']), f'월 15만원 절감 가정 → {projection.estimate_text(cut)}')

    print('\n6. design/sample-data.json derived ↔ 계산')
    d = S['raw']['derived']
    check(d['capacity'] == round(projection.capacity(S)), f'capacity {d["capacity"]:,}')
    check(d['limit']['total'] == limits.verdict_total(S) and d['limit']['planCap'] == round(limits.from_income(S))
          and d['limit']['daysLeftInclusive'] == limits.days_left() and d['limit']['dailyWon'] == limits.scene(S, S['spend'])['dailyWon'],
          'limit (total · planCap · daysLeftInclusive · dailyWon)')
    for key, st, ex in (('avalanche', 'avalanche', S['extra']), ('snowball', 'snowball', S['extra']), ('baseline', 'avalanche', 0), ('minimumOnly', 'current', 0)):
        r = simulate_debt(won, ex, st, unit=1)
        y, mo = map(int, d['payoff'][key]['end'].split('-'))
        check(d['payoff'][key]['months'] == r['months'] and d['payoff'][key]['totalInterest'] == round(r['interest'])
              and month_label(y, mo) == month_label(now.year, now.month, r['months']), f'payoff.{key} {d["payoff"][key]["end"]} · {d["payoff"][key]["totalInterest"]:,}')
    check(d['allocationNeeded'] == round(a['totalRequired']), f'allocationNeeded {d["allocationNeeded"]:,}')
    for r in a['rows']:
        y, mo = map(int, d['goalEta'][r['name']].split('-'))
        check(month_label(y, mo) == r['arrival'], f'goalEta {r["name"]} {d["goalEta"][r["name"]]}')
    for sc, key in (('bad', 'bad'), ('base', 'base'), ('good', 'good')):
        fin = projection.project(S, 120, sc)['series'][-1]['net']
        check(d['netWorthIn10y'][key] == round(fin), f'netWorthIn10y.{key} {d["netWorthIn10y"][key]:,}')
    for m in projection.milestones(S):
        y, mo = map(int, d['netWorthMilestones'][str(m['target'])].split('-'))
        check(month_label(y, mo) == m['date'], f'netWorthMilestones {m["target"]:,} {d["netWorthMilestones"][str(m["target"])]}')

    print('\n일치' if not bad else f'\n{bad}건 불일치 — 계산기(파이썬)를 고치세요. 앱이 바뀌었으면 node app_ref.cjs를 먼저 다시 돌리세요')
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
