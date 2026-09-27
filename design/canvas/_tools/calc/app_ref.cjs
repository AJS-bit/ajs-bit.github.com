#!/usr/bin/env node
// -*- coding: utf-8 -*-
// 앱(v5-stage1)의 계산 코드를 그대로 돌려 시안 숫자를 얻는다 — 규칙 5 「어긋나면 엔진이 맞습니다」.
//
//   node app_ref.cjs                       # → app_ref.json (crosscheck.py가 대조하는 기준값)
//   node app_ref.cjs --state out.json      # 시안 사용자를 AppState로도 쓴다(앱 하네스에 그대로 넣으면 시안 숫자가 나온다)
//   NAVI_APP=<앱 저장소> node app_ref.cjs    # 기본 ~/Documents/Codex/2026-09-01/ai/work/wealth-navigator
//
// 앱 저장소가 없는 곳에서는 돌지 않는다. 그때는 저장된 app_ref.json을 그대로 쓰고 crosscheck.py만 돌린다.
// 기준 시각 2026-09-08 12:00(서울) — 시안의 오늘.
'use strict';
process.env.TZ = 'Asia/Seoul';
const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');
const { createRequire } = require('node:module');

const NOW_ISO = '2026-09-08T03:00:00Z';
const APP = process.env.NAVI_APP || path.join(os.homedir(), 'Documents/Codex/2026-09-01/ai/work/wealth-navigator');
const OUT = path.join(__dirname, 'app_ref.json');

// 엔진은 기본 인수로 new Date()를 쓰는 곳이 있다(allocateGoals의 monthsUntil 등) — 인수 없는 Date를 시안의 오늘로 고정한다.
const RealDate = Date;
const FIXED = new RealDate(NOW_ISO).getTime();
class FixedDate extends RealDate {
  constructor(...args) { if (args.length === 0) super(FIXED); else super(...args); }
  static now() { return FIXED; }
}
globalThis.Date = FixedDate;

function loadApp() {
  const local = createRequire(path.join(APP, 'package.json'));
  const esbuild = createRequire(local.resolve('vitest/package.json'))('esbuild');
  const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'navi-appref-'));
  const entry = path.join(tmp, 'entry.ts');
  const mods = ['engine', 'navi-current', 'navi-goals', 'navi-goal-tools', 'navi-goal-eta', 'navi-limit-view', 'navi-verdict',
    'navi-hero', 'navi-debt-view', 'navi-analysis', 'navi-projection', 'navi-alert-rows', 'navi-insights', 'navi-quick-entry',
    'navi-state', 'navi-salary', 'navi-effective', 'navi-next-action'];
  fs.writeFileSync(entry, mods.map((m) => `export * as ${m.replace(/-/g, '_')} from '@/lib/${m}';`).join('\n')
    + `\nexport { homeLimitView, limitAmountText } from '@/components/navi/home-limit-card';`);
  const outfile = path.join(tmp, 'app.cjs');
  esbuild.buildSync({ entryPoints: [entry], bundle: true, platform: 'node', format: 'cjs', outfile, logLevel: 'silent',
    alias: { '@': APP }, nodePaths: [path.join(APP, 'node_modules')], absWorkingDir: APP, jsx: 'automatic',
    loader: { '.css': 'empty', '.svg': 'empty', '.png': 'empty' } });
  const mod = require(outfile);
  const head = require('node:child_process').execSync('git rev-parse --short HEAD', { cwd: APP }).toString().trim();
  return { mod, head };
}

function main() {
  const args = process.argv.slice(2);
  const { buildState } = require('./sample_state.cjs');
  const { mod: A, head } = loadApp();
  const E = A.engine, C = A.navi_current, G = A.navi_goals, GT = A.navi_goal_tools, GE = A.navi_goal_eta, LV = A.navi_limit_view;
  const V = A.navi_verdict, H = A.navi_hero, D = A.navi_debt_view, AN = A.navi_analysis, P = A.navi_projection;
  const now = new Date(NOW_ISO);
  const raw = buildState();
  const state = A.navi_state.syncFinancialState(raw, now);
  const si = state.stateIndex;
  if (args[0] === '--state') { fs.writeFileSync(args[1], JSON.stringify(state, null, 1)); console.error('state →', args[1]); }

  const r = (v) => (typeof v === 'number' ? Math.round(v * 1e6) / 1e6 : v);
  const out = { _: `앱 ${head} 계산 코드를 시안 사용자(sample-data.json → sample_state.cjs)에 돌린 값 · 기준 ${NOW_ISO} (서울 9월 8일)`, app: head };

  // ── 이번 달 · 히어로 ─────────────────────────────
  const cur = C.naviMetrics(state, '2026-09', now);
  const limit = C.naviSpendingLimit(state, now);
  const salary = state.profile.monthlyIncome;
  const target = A.navi_salary.salaryTarget(state);
  const line = H.targetLine(cur.spend, salary, target);
  out.month = {
    days: cur.days, done: cur.done, daysLeftInclusive: LV.daysLeftIncludingToday(cur),
    spend: cur.spend, projected: r(cur.projected), fixed: cur.fixed, variable: cur.variable,
    income: cur.income, debtPay: cur.debtPay, capacity: r(cur.capacity),
    salaryRatio: r(cur.salaryRatio), salaryRatioProjected: r(cur.salaryRatioProjected),
    net: cur.net, assets: cur.assets, debts: cur.debts, burn: r(cur.burn), burnProjected: r(cur.burnProjected),
    targetAmount: H.targetAmount(salary, target), targetLine: { ...line, text: H.targetLineText(line) },
    netWorthRatioText: H.netWorthRatioText(cur.burn), badgeKey: A.navi_salary.salaryGrade(cur.salaryRatioProjected, target).key,
    monthEndLeft: H.targetAmount(salary, target) - cur.projected,
  };
  // ── 한도(D1) ─────────────────────────────
  out.limit = {
    total: limit.total, basis: limit.basis, fromSalary: limit.fromSalary, fromIncome: r(limit.fromIncome), goalNeed: r(limit.goalNeed),
    goalRequired: r(limit.goalRequired), goalNeedCapped: limit.goalNeedCapped, debtPay: limit.debtPay, income: limit.income,
    planCapInfo: r(V.planCapInfo(limit)), remain: limit.remain, used: limit.used, ratio: r(limit.ratio),
    dailyWon: LV.dailyAllowanceWon(limit.remain, cur), daily: r(LV.dailyAllowance(limit.remain, cur)),
    categories: limit.categories, fixedCost: limit.fixedCost, variableBudget: limit.variableBudget, personalized: limit.personalized,
  };
  // 같은 날 · 같은 한도에서 쓴 돈만 다른 장면(완료 카드 · 이력 부족 히어로 · 한도 카드 경우) — 오늘 포함 23일로 나눈다
  const daily = (spent) => ({ spent, remain: limit.total - spent, dailyWon: LV.dailyAllowanceWon(limit.total - spent, cur),
    line: H.targetLineText(H.targetLine(spent, salary, target)) });
  out.scenes = { canon: daily(cur.spend), doneCard: daily(cur.spend + 12000), heroInsufficient: daily(5000) };

  // ── 목적지 배분(naviGoalAllocation) ─────────────────────────────
  const alloc = G.naviGoalAllocation(state, cur.capacity);
  const rowOut = (row) => {
    const type = G.naviGoalType(row.goal);
    const saving = type !== 'debt-payoff' && type !== 'net-worth';
    const eta = GE.goalEtaMonths(state, row, now);
    const cap = saving ? undefined : Infinity;
    return {
      name: row.goal.name, type, priority: row.goal.priority, targetDate: row.goal.targetDate, monthsLeft: r(row.monthsLeft),
      weight: r(row.weight), required: r(row.required), allocated: r(row.allocated), gap: r(row.gap), etaMonths: r(eta),
      arrivalMonths: eta === null ? null : GT.goalArrivalMonths(eta),
      arrival: GT.goalArrivalLabel(eta, now, cap, saving ? row.goal.targetDate : null),
      deadline: GT.goalDeadline(eta, row.goal.targetDate, now, cap, saving),
      progress: r(row.progress), saved: row.goal.saved, target: row.goal.target,
    };
  };
  out.goals = { budget: r(alloc.budget), totalRequired: r(alloc.totalRequired), surplus: r(alloc.surplus),
    unplanned: alloc.unplannedGoals.map((g) => g.name), rows: alloc.rows.map(rowOut),
    netWorthReturn: r(G.naviGoalAnnualReturn(state, state.goals.find((g) => g.kind === 'net-worth'))) };
  // 적립 50만(GoalContribute) — 비상금 6개월 1,020 → 1,070만
  const em = state.goals.find((g) => g.kind === 'emergency');
  const afterContribute = GT.contributeToGoal(state, em.id, 500000);
  const a2 = G.naviGoalAllocation(afterContribute, cur.capacity);
  const emBefore = alloc.rows.find((x) => x.goal.id === em.id), emAfter = a2.rows.find((x) => x.goal.id === em.id);
  out.contribute = { before: rowOut(emBefore), after: { ...rowOut(emAfter) } };
  out.contribute.after.arrival = GT.goalArrivalLabel(emAfter.etaMonths, now, undefined, em.targetDate);
  // 새 목적지 설계(GoalDesign) — 결혼 자금 3,000만 · 지금 500만 · 7년(84개월) · 연 4.0%
  const sim = GT.simulateGoal({ target: 30000000, saved: 5000000, months: 84, annualReturn: 0.04, monthlySave: 0 });
  const draftGoal = { id: 'goal-draft', name: '결혼 자금', emoji: '🎯', target: 30000000, saved: 5000000, priority: 2, kind: 'investment',
    targetDate: GT.goalDateAfter(84, now) };
  const leftover = GT.leftoverCapacity(state, cur.capacity);
  out.design = { required: r(sim.required), final: r(sim.final), targetDate: draftGoal.targetDate, leftover,
    budget: r(alloc.budget), surplus: r(alloc.surplus),
    preview: GT.goalSavePreview(state, draftGoal, cur.capacity, now, { annualReturn: 0.04 }).map((l) => l.text),
    presets: GT.goalPresets(state, cur.projected, now).map((g) => ({ id: g.id, name: g.name, target: g.target, targetDate: g.targetDate })) };

  // ── 상환(simulateDebt) ─────────────────────────────
  const debts = A.navi_effective.effectiveDebtState(state).debts;
  const run = (extra, st) => { const x = E.simulateDebt(debts, extra, st);
    return { months: x.months, label: x.months === null ? null : D.payoffMonthText(x.months, now), interest: r(x.totalInterest),
      order: x.order.map((o) => ({ name: o.name, paidOffAt: o.paidOffAt, label: o.paidOffAt === null ? null : D.payoffMonthText(o.paidOffAt, now), interest: r(o.interest) })) }; };
  const pay = {};
  for (const extra of [0, 150000, 200000, 300000]) for (const st of ['avalanche', 'snowball']) pay[`${st}_${extra}`] = run(extra, st);
  pay.current = run(0, 'current');
  const lines = (extra, st) => D.baselineLines(E.simulateDebt(debts, extra, st), D.baselinePlan(debts, st), extra, now);
  pay.baseline15 = lines(150000, 'avalanche'); pay.baseline20 = lines(200000, 'avalanche'); pay.baseline30 = lines(300000, 'avalanche');
  pay.info15 = D.payoffInfoText(E.simulateDebt(debts, 150000, 'avalanche'), E.simulateDebt(debts, 150000, 'snowball'));
  pay.info20 = D.payoffInfoText(E.simulateDebt(debts, 200000, 'avalanche'), E.simulateDebt(debts, 200000, 'snowball'));
  pay.info30 = D.payoffInfoText(E.simulateDebt(debts, 300000, 'avalanche'), E.simulateDebt(debts, 300000, 'snowball'));
  const cmp = (extra) => D.comparisonText({ strategy: 'avalanche', run: E.simulateDebt(debts, extra, 'avalanche') }, { strategy: 'snowball', run: E.simulateDebt(debts, extra, 'snowball') });
  pay.compare15 = cmp(150000); pay.compare20 = cmp(200000); pay.compare30 = cmp(300000);
  pay.breakdown15 = D.debtPaymentBreakdown(state); pay.breakdown20 = D.debtPaymentBreakdown(state, 200000); pay.breakdown30 = D.debtPaymentBreakdown(state, 300000);
  pay.minNote = D.minPaymentNote(state);
  // 상환 계획 초안 — 매달 남는 돈(future-11) · 저축 · 상환 계획까지 지키려면(assets-2)
  const draftState = (extra) => ({ ...state, settings: { ...state.settings, extraDebtPay: extra } });
  pay.capacity = {}; pay.planCap = {};
  for (const extra of [0, 150000, 200000, 300000]) {
    const s = draftState(extra);
    pay.capacity[extra] = r(C.naviMetrics(s, '2026-09', now).capacity);
    const l = C.naviSpendingLimit(s, now); pay.planCap[extra] = { fromIncome: r(l.fromIncome), info: r(V.planCapInfo(l)), total: l.total };
  }
  out.payoff = pay;

  // ── 미래 경로(naviProject) ─────────────────────────────
  const proj = (scenario, months = 120, spendDelta = 0, s = state) => C.naviProject(s, months, { scenario, spendDelta }, now);
  const fut = {};
  for (const sc of ['bad', 'base', 'good']) {
    const p = proj(sc);
    const fin = p.series.at(-1).net;
    fut[sc] = { rate: r(E.projectionSavingRate(state, sc)), final: r(fin), estimate: AN.estimateText(fin), short: AN.shortEstimate(fin),
      delta: r(fin - p.start.net), deltaText: AN.estimateText(Math.abs(fin - p.start.net)), monthlySave: r(p.monthlySave) };
  }
  const base600 = proj('base', 600);
  fut.start = base600.start;
  fut.milestones = AN.milestoneRows(base600, AN.nextMilestones(base600.start.net, 3)).map((m) => ({ target: m.target, month: m.month, whenText: m.whenText, dateText: m.dateText }));
  fut.status = P.naviProjectionStatus(state, now).kind;
  fut.years = {};
  for (const y of [5, 10, 20, 30]) { const p = proj('base', y * 12); fut.years[y] = { final: r(p.series.at(-1).net), estimate: AN.estimateText(p.series.at(-1).net) }; }
  // 소비 절감 가정(FutureStates D) — 월 15만원
  const cut = proj('base', 120, 150000); const cutFin = cut.series.at(-1).net;
  fut.cut15 = { final: r(cutFin), estimate: AN.estimateText(cutFin), diff: r(cutFin - fut.base.final), diffText: AN.estimateText(cutFin - fut.base.final) };
  out.future = fut;

  // ── 알림 · 코칭 ─────────────────────────────
  const rows = A.navi_alert_rows.naviAlertRows(state, now);
  out.alerts = { counts: A.navi_alert_rows.alertCounts(rows), rows: rows.map((x) => ({ level: x.level, title: x.title, body: x.body, link: x.link?.label })),
    footer: A.navi_alert_rows.alertFooterNote(rows) };
  out.insights = A.navi_insights.naviInsights(state, now).map((i) => ({ priority: i.priority, tone: i.tone, title: i.title, body: i.body }));
  out.savings = A.navi_insights.naviSavingOpportunities(state, 0.15, now).map((o) => ({ category: o.category, used: o.used, cut: r(o.cut), cap: o.cap,
    goalName: o.goalName, period: o.period, tenYears: r(o.tenYears), impact: o.impact.kind === 'goal' ? { monthsSaved: r(o.impact.monthsSaved), base: r(o.impact.base), better: r(o.impact.better) } : { delta: r(o.impact.delta) } }));
  const cut15 = cur.projected * 0.15;
  const imp = A.navi_insights.naviImpactOfSaving(state, cut15, now);
  out.coachCut = { ratio: 0.15, monthly: r(cut15), impact: imp.kind === 'goal' ? { goal: imp.goal.name, monthsSaved: r(imp.monthsSaved), base: r(imp.base), better: r(imp.better) } : { delta: r(imp.delta) },
    tenYears: r(E.futureValue(0, cut15, 120, state.profile.expectedReturn)) };
  // 코칭 「카테고리 절감 가정」 — 기본 −10% · 칸 두 개(coach-panel.tsx savingEffect와 같은 글)
  const I = A.navi_insights;
  const tile = (o) => o.months !== null
    ? (o.months < 0.1 ? `1년이면 ${I.monthYearWon(o.cut).year}` : `약 ${I.periodWords(o.months)} 빨리 도착`)
    : `10년 뒤 +${E.compact(Math.round(o.wealth ?? 0))}원`;
  out.categoryCuts = {};
  for (const ratio of [0.10, 0.15]) {
    out.categoryCuts[ratio] = I.naviCategoryCuts(state, ratio, now).map((o) => ({ category: o.category, used: o.used, cut: r(o.cut),
      month: I.monthYearWon(o.cut).month, tile: tile(o), months: r(o.months), goalName: o.goalName, cap: o.cap }));
  }
  out.score = { total: cur.score.total, ready: cur.score.ready, tier: cur.score.tier, parts: cur.score.parts.map((p) => ({ key: p.key, label: p.label, score: r(p.score), max: p.max, measured: p.measured })) };
  out.glance = { burnProjected: r(cur.burnProjected), burnText: `${cur.burnProjected.toFixed(1)}%`, score: `${Math.round(cur.score.total)}점`, tenYear: fut.base.estimate };
  out.netWorthRatio = H.netWorthRatioLines({ spent: cur.spend, netWorth: cur.net, ratio: cur.burn, projected: cur.projected });
  try { out.nextAction = A.navi_next_action.nextBestAction(state, now); } catch (e) { out.nextAction = String(e); }

  // ── 홈 한도 카드 경우(LimitCardCases) — 같은 사용자에 기록만 더하거나 월급을 뺀 상태를 앱 homeLimitView에 넣는다 ──
  const withTx = (amount, date = '2026-09-08') => ({ ...state, transactions: [{ id: 'case-tx', date, amount, category: '식비', memo: '' }, ...state.transactions] });
  const view = (s, at = now) => { const v = A.homeLimitView(s, at);
    return { status: v.status, daily: v.dailyLabel ? A.limitAmountText(v.dailyLabel) : null, right: A.limitAmountText(v.right), usage: v.usage,
      desktopNote: v.desktopNote, desktopRight: A.limitAmountText(v.desktopRight), tone: v.tone }; };
  const lastNow = new Date('2026-09-30T03:00:00Z');
  const noSalary = { ...state, profile: { ...state.profile, monthlyIncome: 0 } };
  out.limitCases = {
    base: view(state),
    none: view(noSalary),
    zero: view(withTx(limit.total - cur.spend)),
    over32k: view(withTx(limit.total - cur.spend + 32000)),
    lastDay90k: view(withTx(limit.total - cur.spend - 90000, '2026-09-29'), lastNow),
    doneCard: view(withTx(12000)),
    heroInsufficient5k: view({ ...state, transactions: [{ id: 'case-tx', date: '2026-09-08', amount: 5000, category: '식비', memo: '' },
      ...state.transactions.filter((t) => !t.date.startsWith('2026-09'))] }),
  };
  // 완료 카드(DoneCard) — 9월 8일 편의점 12,000원을 카테고리 없이 저장한 뒤 · 이력 부족 히어로 — 9/5 처음 · 커피 5,000원 하나(기록 이력 없음)
  const doneState = { ...state, transactions: [{ id: 'done-tx', date: '2026-09-08', amount: 12000, category: '기타', memo: '편의점' }, ...state.transactions],
    settings: { ...state.settings, quickEntry: { ...state.settings.quickEntry, uncategorized: [...state.settings.quickEntry.uncategorized, 'done-tx'] } } };
  const firstState = { ...state, transactions: [{ id: 'first-tx', date: '2026-09-08', amount: 5000, category: '카페/간식', memo: '커피' }],
    settings: { ...state.settings, monthlyCloses: {}, quickEntry: { version: 1, since: '2026-09-05', dayLog: {}, uncategorized: [] } } };
  const sceneMetrics = (s) => { const m = C.naviMetrics(s, '2026-09', now); const l = C.naviSpendingLimit(s, now);
    return { spend: m.spend, projected: r(m.projected), salaryRatio: r(m.salaryRatio), salaryRatioProjected: r(m.salaryRatioProjected),
      burn: r(m.burn), ratioText: H.actualRatioText(m.salaryRatio), netWorthRatioText: H.netWorthRatioText(m.burn),
      monthEndLeft: r(H.targetAmount(salary, target) - m.projected), limitRatio: r(l.ratio), remain: l.remain, dailyWon: LV.dailyAllowanceWon(l.remain, m),
      line: H.targetLineText(H.targetLine(m.spend, salary, target)), passed: A.navi_quick_entry.recordRange(s, now).passed }; };
  out.sceneMetrics = { doneCard: sceneMetrics(doneState), heroInsufficient: sceneMetrics(firstState) };
  // 지난 달(SpendingPast 7월 · MonthlyCloseV5 8월) — 마감값 기준
  out.pastMonths = {};
  for (const key of ['2026-06', '2026-07', '2026-08']) { const m = C.naviMetrics(state, key, now);
    out.pastMonths[key] = { spend: m.spend, salary: m.salary, salaryRatio: r(m.salaryRatio), net: m.net, burn: r(m.burn), burnText: m.burn === null ? null : `${m.burn.toFixed(1)}%`,
      limit: m.salary ? m.salary * target / 100 : null, left: m.salary ? m.salary * target / 100 - m.spend : null, count: m.txCount }; }
  const insightTitles = (s, at = now) => A.navi_insights.naviInsights(s, at).filter((i) => /한도/.test(i.title)).map((i) => `${i.title} — ${i.body}`);
  out.limitCases.coach = { base: insightTitles(state), over32k: insightTitles(withTx(limit.total - cur.spend + 32000)),
    lastDay90k: insightTitles(withTx(limit.total - cur.spend - 90000, '2026-09-29'), lastNow) };

  fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
  console.error('→', OUT);
}

main();
