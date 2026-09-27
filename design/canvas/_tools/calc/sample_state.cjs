// -*- coding: utf-8 -*-
// 시안의 가상 사용자(design/sample-data.json)를 앱의 AppState로 옮긴다 — 앱 엔진이 시안 숫자를 직접 계산하게.
//
//   const { buildState } = require('./sample_state.cjs'); const state = buildState();
//
// 앱(v5-stage1)의 엔진이 9월 8일 기준으로 sample-data.json의 확정값을 그대로 내도록 짠 픽스처다.
//  - 9월 1~8일 기록 = gen_screens.LEDGER_V5(합 1,120,000원 · 카테고리 합 = 소비 · 한도 장) · 6일 ETF 자동이체 30만(이체)
//  - 8월 = gen_calendar.AUG의 날짜별 합(합 1,715,200원) · 7월 = SpendingPast(191만 · 주거 48 · 식비 41 · 쇼핑 26 · 13개 카테고리)
//  - 6월은 어떤 장에도 그려지지 않는다. 엔진의 월말 예상 = max(이번 달 고정비, 3개월 평균 고정비) + 이번 달 변동비
//    + 남은 날 비율 × 3개월 평균 변동비(finance.ts metrics)가 정확히 2,084,000원이 되도록 6월 금액을 정했다.
//  - 카테고리 한도(D1 · 소비 목표 216만원을 나눔)가 한도 장의 값과 같도록: 주거/관리는 직접 50만(LimitEditor 「직접 지정함」),
//    고정비 통신 8만 · 보험 12만 · 구독 4만은 3개월 평균, 변동비 9개는 3개월 합이 한도에 비례(식비 45 · 쇼핑 30 · 교통 12 ·
//    문화/여가 15 · 카페/간식 10 · 의료/건강 8 · 교육 5 · 경조사 7 · 기타 10 = 142만).
//  - 6 · 7 · 8월은 마감한 달(월말 예상 표본 통과 — 홈 히어로가 월말 예상을 보여 준다).
//  - 목적지 목표일 · 우선순위는 시안에 없던 입력이라 여기서 정했다(NUMBERS.md 「입력 가정」).
//  - 개인 모드(dataMode 'personal' — 시안의 홈 · 탭은 샘플 띠 없는 내 데이터) · 반복 기록 규칙 3건 · 9월 연결(생활비 통장) — 2026-09-27 fix-up
//    (LedgerV5 · DesktopLedger 가 그린 세계와 같게. 숫자는 하나도 안 바뀐다).
'use strict';
const fs = require('node:fs');
const path = require('node:path');

const SAMPLE = path.join(__dirname, '..', '..', '..', 'sample-data.json');

// 9월 — gen_screens.py LEDGER_V5 와 같은 행(카테고리 null = 카테고리 없는 기록 → 기타 + quickEntry.uncategorized)
const SEP_ROWS = [
  [8, [['카페/간식', '커피', 4500], ['식비', '점심', 9000], ['쇼핑', '생필품', 17000], [null, '편의점', 6500]]],
  [6, [['저축/투자', 'ETF 자동이체', 300000]]],
  [5, [[null, '버스', 4500], [null, '', 3000], [null, '커피', 4500]]],
  [4, [[null, '커피', 4500]]],
  [3, [['교통', '택시', 45000], ['식비', '점심', 9000], [null, '간식', 4500]]],
  [1, [['주거/관리', '관리비', 320000], ['주거/관리', '전기·가스·수도', 150000], ['보험', '보험료', 120000],
       ['통신', '인터넷·TV', 80000], ['구독', 'OTT·음악', 35500], ['식비', '장보기', 214500], ['교통', '교통카드 충전', 25000],
       ['쇼핑', '생활용품', 13000], ['문화/여가', '영화', 10000], ['기타', '세탁소', 28000], [null, '커피', 4500], ['식비', '점심', 7500]]],
];
const SEP_CHECK = [1, 4, 5];
const SEP_NOSPEND = [6];

// 8월 — gen_calendar.py AUG(날짜 → 그날 소비 합계). null = 기록 없음, 0 = 안 썼어요
const AUG = {1: 23500, 2: 61000, 3: 9800, 4: 4500, 5: 712000, 6: 15300, 7: 38000, 8: 52400, 9: 0, 10: 12000,
  11: 6700, 12: 89000, 13: 4500, 14: 27600, 15: 118000, 16: null, 17: 9900, 18: 33000, 19: 4500,
  20: 64500, 21: 17800, 22: 72000, 23: 41200, 24: 5600, 25: 68000, 26: 8900, 27: 29500, 28: 96000,
  29: 35000, 30: null, 31: 55000};
// 8월에 날짜가 정해진 행: 5일 고정비 · 25일 휴대폰 요금(반복 기록) · 카테고리 없는 3건 21,200원(8월 마감 창).
// 관리비는 9월(320,000)과 금액이 달라야 한다 — 같으면 앱이 내역에 「매달 나가는 돈으로 등록할까요?」를 띄운다(LedgerV5에 없는 줄).
// 보험료도 같은 까닭으로 8월 메모를 「실손 보험료」로 둔다(앱 recurringCandidates = 같은 메모 · 같은 금액 — 9월 1일 「보험료」 120,000원).
// 그 제안 줄은 RecurringPrefill(하루 시트 페이지)에 따로 그린다.
const AUG_FIXED = {
  5: [['주거/관리', '관리비', 310000], ['주거/관리', '전기·가스·수도', 190000], ['보험', '실손 보험료', 120000],
      ['통신', '인터넷', 25000], ['구독', 'OTT·음악', 40000], ['식비', '장보기', 27000]],
  25: [['통신', '휴대폰 요금', 55000], ['식비', '점심', 13000]],
  // 이 세 건은 8월 마감(9월 2일) 때 카테고리 없음이었다(MonthlyCloseV5 「카테고리 없음 3건 21,200원」). 마감 뒤 「기타」로 골랐다 —
  // 카테고리 칸은 처음부터 기타라 금액 · 카테고리 합 · 마감값(1,715,200)이 그대로이고 합계 고치기도 없다(2026-09-27 fix-up · 캐논).
  // 그래서 9월 8일의 카테고리 없는 기록은 9월 7건 32,000원뿐이다(달력 「카테고리 없는 기록 7건」 = LedgerV5 = ClassifySheet).
  14: [['기타', '편의점', 9600]],
  19: [['기타', '커피', 4500]],
  26: [['기타', '간식', 7100]],
};
// 8월 나머지(날짜 합에서 위 행을 뺀 돈)를 카테고리에 나눈다 — 이 순서대로 날짜를 채운다
const AUG_REST = [['식비', 260000], ['쇼핑', 180000], ['교통', 104000], ['문화/여가', 125000], ['카페/간식', 80000],
  ['의료/건강', 66000], ['교육', 45000], ['경조사', 50000], ['기타', 4000]];

// 7월(SpendingPast) · 6월 — 카테고리별 한 달 합
const JUL = {'주거/관리': 480000, '통신': 80000, '보험': 120000, '구독': 40000, '식비': 410000, '쇼핑': 260000, '교통': 110000,
  '문화/여가': 120000, '카페/간식': 90000, '의료/건강': 60000, '교육': 45000, '경조사': 50000, '기타': 45000};
const JUN = {'주거/관리': 496900, '통신': 80000, '보험': 120000, '구독': 40000, '식비': 505000, '쇼핑': 370000, '교통': 110000,
  '문화/여가': 160000, '카페/간식': 100000, '의료/건강': 90000, '교육': 45000, '경조사': 89000, '기타': 199800};
const DAY_OF = {'주거/관리': 5, '통신': 5, '보험': 5, '구독': 5, '식비': 12, '쇼핑': 18, '교통': 3, '문화/여가': 21,
  '카페/간식': 9, '의료/건강': 15, '교육': 10, '경조사': 26, '기타': 28};

const pad = (n) => String(n).padStart(2, '0');

// 반복 기록 규칙 — RecurringPrefill · DesktopLedger 「반복 기록 · 매달 6일 · 25일 · 꺼 둠」(3건 · 켜짐 2건).
// 규칙이 만든 기록은 앱처럼 id = recurring:{규칙 id}:{YYYY-MM}(materializeRecurringTransactions 가 같은 달을 다시 만들지 않는다).
const RULES = [
  { id: 'etf', memo: 'ETF 자동이체', category: '저축/투자', amount: 300000, dayOfMonth: 6, startMonth: '2026-06', enabled: true },
  { id: 'phone', memo: '휴대폰 요금', category: '통신', amount: 55000, dayOfMonth: 25, startMonth: '2026-08', enabled: true },
  { id: 'gym', memo: '헬스장', category: '문화/여가', amount: 50000, dayOfMonth: 10, startMonth: '2026-06', enabled: false },
];
const RULE_OF = { 'ETF 자동이체': 'etf', '휴대폰 요금': 'phone' };
// 9월 1일 고정비 넷과 6일 ETF 이체는 생활비 통장과 연결(LedgerV5 「· 생활비 통장」 · 「생활비 통장 → ETF 계좌」)
const LINKED_SEP1 = ['관리비', '전기·가스·수도', '보험료', '인터넷·TV'];

function buildState(opts = {}) {
  const sample = JSON.parse(fs.readFileSync(opts.samplePath || SAMPLE, 'utf8'));
  let seq = 0;
  const id = (p) => `${p}-${++seq}`;
  const tx = [];
  const uncategorized = [];
  const dayLog = {};
  // 반복 기록이 만든 건은 앱 규칙대로 id = recurring:{규칙}:{달}(앱이 같은 달을 두 번 만들지 않게) — seq 는 그대로 하나 쓴다
  const push = (date, category, memo, amount, fixedId) => {
    const seqId = id('tx');
    const row = { id: fixedId ?? seqId, date, amount, category: category ?? '기타', memo };
    if (category === null) uncategorized.push(row.id);
    tx.push(row);
  };

  // 9월
  for (const [d, rows] of SEP_ROWS) for (const [c, m, a] of rows) push(`2026-09-${pad(d)}`, c, m, a, RULE_OF[m] && `recurring:${RULE_OF[m]}:2026-09`);
  for (const d of SEP_CHECK) dayLog[`2026-09-${pad(d)}`] = { closed: true, noSpend: false, at: `2026-09-${pad(d)}T21:00:00+09:00` };
  for (const d of SEP_NOSPEND) dayLog[`2026-09-${pad(d)}`] = { closed: false, noSpend: true, at: `2026-09-${pad(d)}T21:00:00+09:00` };

  // 8월 — 날짜가 정해진 행을 먼저 놓고, 남은 금액을 AUG_REST 순서대로 날짜에 채운다
  const left = {};
  for (const [d, v] of Object.entries(AUG)) left[d] = v ?? 0;
  for (const [d, rows] of Object.entries(AUG_FIXED)) for (const [c, m, a] of rows) { push(`2026-08-${pad(d)}`, c, m, a, RULE_OF[m] && `recurring:${RULE_OF[m]}:2026-08`); left[d] -= a; }
  const days = Object.keys(left).map(Number).sort((a, b) => a - b);
  for (const [c, total] of AUG_REST) {
    let need = total;
    for (const d of days) {
      if (need <= 0) break;
      if (left[d] <= 0) continue;
      const take = Math.min(left[d], need);
      push(`2026-08-${pad(d)}`, c, '', take);
      left[d] -= take; need -= take;
    }
    if (need !== 0) throw new Error(`8월 ${c} 배정 실패 ${need}`);
  }
  if (days.some((d) => left[d] !== 0)) throw new Error('8월 날짜 합이 맞지 않아요');
  push('2026-08-06', '저축/투자', 'ETF 자동이체', 300000, 'recurring:etf:2026-08');
  for (const d of days) {
    if (AUG[d] === 0) dayLog[`2026-08-${pad(d)}`] = { closed: false, noSpend: true, at: `2026-08-${pad(d)}T21:00:00+09:00` };
    else if (AUG[d] && d !== 31) dayLog[`2026-08-${pad(d)}`] = { closed: true, noSpend: false, at: `2026-08-${pad(d)}T21:00:00+09:00` };
  }

  // 7월 · 6월
  for (const [month, table] of [['2026-07', JUL], ['2026-06', JUN]]) {
    for (const [c, a] of Object.entries(table)) push(`${month}-${pad(DAY_OF[c])}`, c, '', a);
    push(`${month}-06`, '저축/투자', 'ETF 자동이체', 300000, `recurring:etf:${month}`);
  }
  tx.sort((a, b) => (a.date < b.date ? 1 : a.date > b.date ? -1 : 0));

  const typeOf = { '부동산': 'realestate', '투자': 'investment', '연금': 'pension', '현금성': 'cash', '기타': 'other' };
  const assets = sample.assets.map((a) => ({ id: id('asset'), name: a.name, type: typeOf[a.type], value: a.value, returnRate: a.rate, updatedAt: '2026-09-01' }));
  const debts = sample.debts.map((d) => ({ id: id('debt'), name: d.name, type: d.type, balance: d.balance, rate: d.apr, minPayment: d.minimum }));
  const credit = debts.find((d) => d.name === '신용대출');
  const G = Object.fromEntries(sample.goals.map((g) => [g.kind, g]));
  const goalIds = { emergency: id('goal'), investment: id('goal'), debt: id('goal'), net: id('goal') };
  const goals = [
    { id: goalIds.emergency, name: G.emergency.name, emoji: '🧯', kind: 'emergency', target: G.emergency.target, saved: G.emergency.saved,
      targetDate: G.emergency.targetDate, priority: G.emergency.priority },
    { id: goalIds.investment, name: G.investment.name, emoji: '🌱', kind: 'investment', target: G.investment.target, saved: G.investment.saved,
      targetDate: G.investment.targetDate, priority: G.investment.priority },
    { id: goalIds.debt, name: G['debt-payoff'].name, emoji: '🏔️', kind: `debt-payoff:${encodeURIComponent(credit.id)}`,
      target: G['debt-payoff'].originalPrincipal, saved: 0, targetDate: G['debt-payoff'].targetDate, priority: G['debt-payoff'].priority },
    { id: goalIds.net, name: G['net-worth'].name, emoji: '💎', kind: 'net-worth', target: G['net-worth'].target, saved: 0,
      targetDate: opts.netWorthTargetDate ?? G['net-worth'].targetDate, priority: G['net-worth'].priority },
  ];
  const p = sample.profile;
  const assetId = (name) => assets.find((a) => a.name === name).id;
  const transactionLinks = {};
  for (const t of tx) {
    if (t.date === '2026-09-01' && LINKED_SEP1.includes(t.memo)) transactionLinks[t.id] = { fromAssetId: assetId('생활비 통장'), toAssetId: '', debtId: '', principal: 0, settled: true };
    if (t.id === 'recurring:etf:2026-09') transactionLinks[t.id] = { fromAssetId: assetId('생활비 통장'), toAssetId: assetId('ETF 계좌'), debtId: '', principal: 0, settled: true };
  }
  // 마감값 — 8월은 MonthlyCloseV5(2026-09-02 마감 · 월말 자산 180,400,000 · 부채 89,200,000), 7월은 SpendingPast(마감 실수령 352만 ·
  // 순자산 대비 2.0% = 1,910,000 ÷ 9,330만). 6월은 그려진 곳이 없다.
  const closes = {
    '2026-06': { salary: 3600000, income: 3900000, debtPay: 920000, assets: 180000000, debts: 89700000, cash: 13900000, liquid: 61800000, invested: 66100000, closedAt: '2026-07-01' },
    '2026-07': { salary: 3520000, income: 3820000, debtPay: 920000, assets: 182300000, debts: 89000000, cash: 14100000, liquid: 62400000, invested: 66800000, closedAt: '2026-08-02' },
    '2026-08': { salary: 3600000, income: 3900000, debtPay: 920000, assets: 180400000, debts: 89200000, cash: 14400000, liquid: 63000000, invested: 67200000, closedAt: '2026-09-02' },
  };
  for (const [m, c] of Object.entries(closes)) c.spend = tx.filter((t) => t.date.startsWith(m) && t.category !== '저축/투자' && t.category !== '대출상환').reduce((s, t) => s + t.amount, 0);
  // 순자산 기록 — Assets 「6개월 420만원」(2026-03 8,930만 → 2026-09 9,350만). 마감한 달은 마감값과 같게.
  const snapshots = [
    ['2026-03', 178800000, 89500000], ['2026-04', 179300000, 89800000], ['2026-05', 179800000, 89900000],
    ['2026-06', 180000000, 89700000], ['2026-07', 182300000, 89000000], ['2026-08', 180400000, 89200000],
    ['2026-09', 182100000, 88600000],
  ].map(([month, a, d]) => ({ month, assets: a, debts: d, net: a - d }));
  return {
    profile: {
      nickname: undefined, monthlyIncome: p.netSalary, extraIncome: p.sideIncome, targetSalaryRatio: p.spendTargetPct,
      age: p.age, ageAsOfYear: 2026, riskProfile: 'balanced', expectedReturn: p.expectedReturn / 100, inflation: 0.025,
      targetBurn: p.targetBurn, emergencyMonths: 6, startedAt: '2026-06-01',
    },
    assets, debts, transactions: tx, goals,
    limits: { mode: 'auto', total: null, categories: { '주거/관리': 500000 } },
    snapshots,
    settings: {
      debtStrategy: sample.repayment.strategy, extraDebtPay: sample.repayment.extraMonthly, dataMode: 'personal',
      recurringRules: RULES.map((r) => ({ ...r })), transactionLinks,
      monthlyCloses: closes,
      goalPlans: { [goalIds.investment]: { annualReturn: G.investment.annualReturn / 100, monthlySave: 0 } },
      quickEntry: { version: 1, since: '2026-06-01', dayLog, uncategorized },
      onboarding: { introSeen: true, homeLayoutChosen: true, tourSeen: Object.fromEntries(['home', 'assets', 'debts', 'strategy', 'spending', 'ledger', 'limits', 'goals', 'goalDesign', 'future', 'payoff'].map((k) => [k, true])) },
    },
  };
}

module.exports = { buildState, SAMPLE, JUL, JUN, AUG, AUG_REST };
