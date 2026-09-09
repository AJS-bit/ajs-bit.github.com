# -*- coding: utf-8 -*-
"""amort.py가 원본 엔진(engine_ref.py)과 같은 답을 내는지 대조한다.

    python3 crosscheck.py

어긋나면 amort.py가 틀린 것입니다. 시안 수치를 고치기 전에 반드시 통과시키세요.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from amort import Debt, simulate
from engine_ref import simulate_debt

DEBTS = [dict(name='주택담보대출', balance=6200, apr=3.4,  minimum=32),
         dict(name='신용대출',     balance=2200, apr=6.8,  minimum=20),
         dict(name='학자금대출',   balance=280,  apr=2.5,  minimum=5),
         dict(name='카드 할부',    balance=180,  apr=14.5, minimum=20)]
MINE = [Debt(d['name'], d['balance'], d['apr'], d['minimum']) for d in DEBTS]

CASES = [('고금리 우선 +15만', 'avalanche', 15), ('소액 우선 +15만', 'snowball', 15),
         ('최소만', 'current', 0)]

def main():
    bad = 0
    print(f'{"":18}{"amort.py":>20}{"원본 엔진":>20}')
    for tag, st, ex in CASES:
        a = simulate(MINE, ex, order=('snowball' if st == 'snowball' else 'avalanche'))
        b = simulate_debt(DEBTS, ex, st)
        ok = a['months'] == b['months'] and abs(a['interest'] - b['interest']) < 1
        bad += not ok
        print(f'  {"✓" if ok else "✗"} {tag:16} {a["months"]:3}개월 {a["interest"]:7,.0f}만'
              f'   {b["months"]:3}개월 {b["interest"]:7,.0f}만')
    print('\n일치' if not bad else f'\n{bad}건 불일치 — amort.py를 고치세요')
    return 1 if bad else 0

if __name__ == '__main__':
    sys.exit(main())
