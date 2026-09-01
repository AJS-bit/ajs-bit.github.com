/* ============================================================
   금융 계산 엔진
   메인 지표: 순자산 대비 소비율 (월 소비 / 순자산)
   ============================================================ */
import { ASSET_TYPES, CAT, RISK, CATEGORIES, rev } from './store.js';
import { n, monthKey, addMonths, daysInMonth, elapsedDays, monthsUntil, clamp } from './format.js';

/* ---------- 잔액 ---------- */
export function totals(s) {
  const assets = s.assets.reduce((t, a) => t + n(a.value), 0);
  const debts = s.debts.reduce((t, d) => t + n(d.balance), 0);
  const liquid = s.assets
    .filter((a) => ASSET_TYPES[a.type]?.liquid)
    .reduce((t, a) => t + n(a.value), 0);
  const cash = s.assets
    .filter((a) => a.type === 'cash')
    .reduce((t, a) => t + n(a.value), 0);
  const invested = s.assets
    .filter((a) => a.type === 'investment' || a.type === 'pension')
    .reduce((t, a) => t + n(a.value), 0);
  return { assets, debts, net: assets - debts, liquid, cash, invested };
}

export const assetRate = (a, s) =>
  a.returnRate != null && a.returnRate !== ''
    ? n(a.returnRate) / 100
    : a.type === 'investment'
      ? n(s.profile.expectedReturn)
      : (ASSET_TYPES[a.type]?.rate ?? 0);

/* ---------- 월 지출 집계 ---------- */
export function monthTx(s, key) {
  return s.transactions.filter((t) => String(t.date).slice(0, 7) === key);
}

/** 소비지출(이체·상환 제외), 카테고리 합계, 고정비 등 */
export function spendOf(s, key) {
  const tx = monthTx(s, key);
  const byCat = {};
  let spend = 0, transfer = 0, fixed = 0, count = 0;
  for (const t of tx) {
    const amt = n(t.amount);
    if (amt <= 0) continue;
    const c = CAT[t.category];
    if (c?.skip) { transfer += amt; continue; }
    spend += amt;
    count += 1;
    if (c?.fixed) fixed += amt;
    byCat[t.category] = (byCat[t.category] || 0) + amt;
  }
  return { spend, transfer, fixed, variable: spend - fixed, byCat, count, tx };
}

export const income = (s) => n(s.profile.monthlyIncome) + n(s.profile.extraIncome);
export const minDebtPayment = (s) => s.debts.reduce((t, d) => t + n(d.minPayment), 0);

/** 최근 N개월 평균 소비를 고정비/변동비로 나눠 반환. 기록 없는 달은 제외. */
export function avgBreakdown(s, months = 3, before = monthKey()) {
  const rows = [];
  for (let i = 1; i <= months; i++) {
    const k = addMonths(before, -i);
    const r = spendOf(s, k);
    if (r.count > 0) rows.push(r);
  }
  if (!rows.length) return null;
  const mean = (f) => rows.reduce((t, r) => t + f(r), 0) / rows.length;
  return { spend: mean((r) => r.spend), fixed: mean((r) => r.fixed), variable: mean((r) => r.variable) };
}

/** 최근 N개월 평균 소비(데이터 있는 달 기준) */
export function avgSpend(s, months = 3, before = monthKey()) {
  return avgBreakdown(s, months, before)?.spend ?? null;
}

/** 카테고리별 최근 N개월 평균. 기록이 전혀 없으면 null. */
export function avgByCat(s, months = 3, before = monthKey()) {
  const rows = [];
  for (let i = 1; i <= months; i++) {
    const r = spendOf(s, addMonths(before, -i));
    if (r.count > 0) rows.push(r.byCat);
  }
  if (!rows.length) return null;
  const out = {};
  for (const c of CATEGORIES) {
    if (c.skip) continue;
    out[c.id] = rows.reduce((t, b) => t + (b[c.id] || 0), 0) / rows.length;
  }
  return out;
}

/* ---------- 파생 계산 캐시 ----------
   metrics/한도/목표배분은 한 번 렌더링에 여러 번 호출된다.
   상태 리비전이 바뀌기 전까지는 결과를 재사용한다. */
const _cache = new Map();
function memo(tag, key, fn) {
  const k = `${rev()}|${tag}|${key}`;
  if (_cache.has(k)) return _cache.get(k);
  if (_cache.size > 64) _cache.clear();
  const v = fn();
  _cache.set(k, v);
  return v;
}

/* ---------- 핵심 지표 ---------- */
export function metrics(s, key = monthKey()) {
  return memo('metrics', key, () => computeMetrics(s, key));
}

function computeMetrics(s, key) {
  const t = totals(s);
  const cur = spendOf(s, key);
  const inc = income(s);
  const debtPay = minDebtPayment(s) + n(s.settings.extraDebtPay);

  const days = daysInMonth(key);
  const done = clamp(elapsedDays(key), 0, days);

  // 월말 지출 추정.
  // 고정비는 특정 날짜에 한꺼번에 빠지고 변동비는 매일 조금씩 나간다.
  // 둘을 같은 방식으로 추정하면 월초에 고정비가 결제된 순간 예상이 폭주하므로 나눠서 계산한다.
  //   · 고정비: 이번 달 실제 결제액과 과거 평균 중 큰 값 (아직 안 빠진 청구서 대비)
  //   · 변동비: 지금까지 쓴 금액 + 남은 기간만큼의 과거 평균
  const hist = avgBreakdown(s, 3, key);
  let projected;
  if (done >= days || done === 0) {
    projected = cur.spend;                              // 지난 달 = 확정
  } else if (hist === null) {
    projected = (cur.spend / done) * days;              // 비교할 과거가 없으면 단순 페이스
  } else {
    const remain = (days - done) / days;
    projected = Math.max(cur.fixed, hist.fixed) + cur.variable + remain * hist.variable;
  }

  const net = t.net;
  const burn = net > 0 ? (cur.spend / net) * 100 : null;              // 월 소비율
  const burnProjected = net > 0 ? (projected / net) * 100 : null;
  const burnAnnual = net > 0 ? ((projected * 12) / net) * 100 : null; // 연환산 소비율

  const incomeRatio = inc > 0 ? (cur.spend / inc) * 100 : null;
  const incomeRatioProjected = inc > 0 ? (projected / inc) * 100 : null;

  const capacity = inc - projected - debtPay;                          // 월 저축여력
  const savingsRate = inc > 0 ? (capacity / inc) * 100 : null;

  const annualSpend = projected * 12;
  const runway = projected > 0 ? t.liquid / projected : null;          // 생존 개월수
  const emergency = projected > 0 ? t.cash / projected : null;         // 비상금 개월수
  const fiProgress = annualSpend > 0 ? (net / (annualSpend * 25)) * 100 : null; // 4% 룰
  const dti = t.assets > 0 ? (t.debts / t.assets) * 100 : null;

  const prev = spendOf(s, addMonths(key, -1));
  const spendMoM = prev.count > 0 && prev.spend > 0 ? ((projected - prev.spend) / prev.spend) * 100 : null;
  const netMoM = netChange(s, key);

  return {
    key, days, done, ...t,
    spend: cur.spend, projected, transfer: cur.transfer,
    fixed: cur.fixed, variable: cur.variable, byCat: cur.byCat, txCount: cur.count,
    income: inc, debtPay, capacity, savingsRate,
    burn, burnProjected, burnAnnual, incomeRatio, incomeRatioProjected,
    annualSpend, runway, emergency, fiProgress, dti,
    spendMoM, netMoM,
    grade: gradeBurn(burnAnnual),
    score: growthScore({ burnAnnual, savingsRate, dti, fiProgress, net, cash: t.cash, projected, s }),
  };
}

/** 이전 스냅샷 대비 순자산 증감 */
export function netChange(s, key = monthKey()) {
  if (s.snapshots.length < 2) return null;
  const sorted = [...s.snapshots].sort((a, b) => (a.month < b.month ? -1 : 1));
  const cur = sorted[sorted.length - 1];
  const prev = sorted[sorted.length - 2];
  if (!prev || !prev.net) return null;
  return { abs: cur.net - prev.net, pct: prev.net !== 0 ? ((cur.net - prev.net) / Math.abs(prev.net)) * 100 : null };
}

/* ---------- 연 소비율 등급 ---------- */
export const BURN_GRADES = [
  { max: 4,     key: 'fi',     label: '완전자립',  tone: 'pos',  desc: '연 소비가 순자산의 4% 이하 — 자산 수익만으로 생활 가능한 구간입니다.' },
  { max: 10,    key: 'strong', label: '매우 안정', tone: 'pos',  desc: '자산이 소비를 압도합니다. 경제적 자유가 눈앞입니다.' },
  { max: 25,    key: 'good',   label: '안정',      tone: 'pos',  desc: '자산 대비 소비가 낮아 복리가 제대로 일하고 있습니다.' },
  { max: 50,    key: 'ok',     label: '양호',      tone: 'accent', desc: '건전한 축적 구간입니다. 이 페이스를 유지하세요.' },
  { max: 100,   key: 'watch',  label: '주의',      tone: 'warn', desc: '1년치 소비가 순자산에 육박합니다. 저축률을 끌어올릴 시점입니다.' },
  { max: 200,   key: 'alert',  label: '경고',      tone: 'warn', desc: '자산보다 소비가 큽니다. 고정비 구조부터 손봐야 합니다.' },
  { max: Infinity, key: 'risk', label: '위험',     tone: 'neg',  desc: '자산 축적이 소비에 잠식되고 있습니다. 즉시 조정이 필요합니다.' },
];

export function gradeBurn(burnAnnual) {
  if (burnAnnual === null || !Number.isFinite(burnAnnual)) {
    return { key: 'none', label: '측정 불가', tone: 'muted', desc: '순자산과 지출을 입력하면 소비율이 계산됩니다.' };
  }
  if (burnAnnual < 0) return { key: 'neg', label: '순자산 마이너스', tone: 'neg', desc: '부채가 자산보다 많습니다. 부채 상환이 최우선 목표입니다.' };
  return BURN_GRADES.find((g) => burnAnnual < g.max);
}

/* ---------- 재산 성장 점수 (0~100) ---------- */
export function growthScore({ burnAnnual, savingsRate, dti, fiProgress, net, cash, projected, s }) {
  const parts = [];

  // 1) 자산 효율 = 연 소비율 (40점) — 로그 스케일
  let eff;
  if (net <= 0) eff = 0;
  else if (burnAnnual === null) eff = 20;
  else if (burnAnnual <= 4) eff = 40;
  else eff = clamp(40 * (1 - Math.log10(burnAnnual / 4) / Math.log10(100)), 0, 40);
  parts.push({ key: 'burn', label: '자산 대비 소비', score: eff, max: 40 });

  // 2) 저축률 (30점) — 50%면 만점
  const sav = savingsRate === null ? 12 : clamp((savingsRate / 50) * 30, 0, 30);
  parts.push({ key: 'save', label: '저축률', score: sav, max: 30 });

  // 3) 부채 건전성 (15점)
  let debtScore;
  if (dti === null) debtScore = 15;
  else debtScore = clamp(15 * (1 - dti / 80), 0, 15);
  const highRate = (s?.debts || []).some((d) => n(d.rate) >= 10 && n(d.balance) > 0);
  if (highRate) debtScore = Math.min(debtScore, 7);
  parts.push({ key: 'debt', label: '부채 건전성', score: debtScore, max: 15 });

  // 4) 안전판 = 비상금 (15점)
  const need = projected * (s?.profile?.emergencyMonths || 6);
  const safe = need > 0 ? clamp((cash / need) * 15, 0, 15) : 8;
  parts.push({ key: 'safe', label: '비상금', score: safe, max: 15 });

  const total = Math.round(parts.reduce((t, p) => t + p.score, 0));
  const tier =
    total >= 85 ? { label: '탁월', tone: 'pos' } :
    total >= 70 ? { label: '우수', tone: 'pos' } :
    total >= 55 ? { label: '보통', tone: 'accent' } :
    total >= 35 ? { label: '개선 필요', tone: 'warn' } :
                  { label: '위험', tone: 'neg' };
  return { total, parts, tier, fiProgress };
}

/* ============================================================
   미래 예측
   ============================================================ */
const mRate = (annual) => Math.pow(1 + annual, 1 / 12) - 1;

/** 부채 상환 시뮬레이션. strategy: avalanche(고금리) | snowball(소액) | current */
export function simulateDebt(debts, extra = 0, strategy = 'avalanche', maxMonths = 600) {
  let list = debts
    .filter((d) => n(d.balance) > 0)
    .map((d) => ({
      id: d.id, name: d.name, rate: n(d.rate) / 100 / 12,
      balance: n(d.balance), min: Math.max(n(d.minPayment), 0), paidOffAt: null, interest: 0,
    }));
  if (!list.length) return { months: 0, totalInterest: 0, timeline: [{ balance: 0, freed: 0 }], order: [], feasible: true };

  const order = (arr) => {
    const c = [...arr];
    if (strategy === 'snowball') c.sort((a, b) => a.balance - b.balance);
    else if (strategy === 'avalanche') c.sort((a, b) => b.rate - a.rate);
    return c;
  };

  // current = 추가 상환 없이 최소 상환만 유지하는 비교 기준선
  const budget = list.reduce((t, d) => t + d.min, 0) + (strategy === 'current' ? 0 : n(extra));
  let totalInterest = 0;
  const timeline = [];
  let m = 0;
  let feasible = true;

  while (list.some((d) => d.balance > 0.5) && m < maxMonths) {
    m += 1;
    let pool = budget;
    // 1) 이자 반영 + 최소상환
    for (const d of list) {
      if (d.balance <= 0) continue;
      const int = d.balance * d.rate;
      d.balance += int; d.interest += int; totalInterest += int;
    }
    for (const d of list) {
      if (d.balance <= 0) continue;
      const pay = Math.min(d.min, d.balance, pool);
      d.balance -= pay; pool -= pay;
    }
    // 2) 남은 재원을 전략 우선순위 대상에 집중
    for (const d of order(list)) {
      if (pool <= 0) break;
      if (d.balance <= 0) continue;
      const pay = Math.min(d.balance, pool);
      d.balance -= pay; pool -= pay;
    }
    for (const d of list) {
      if (d.balance <= 0.5 && d.paidOffAt === null) { d.paidOffAt = m; d.balance = 0; }
    }
    const remaining = list.reduce((t, d) => t + Math.max(0, d.balance), 0);
    const freed = list.filter((d) => d.paidOffAt !== null).reduce((t, d) => t + d.min, 0) + (pool > 0 ? pool : 0);
    timeline.push({ balance: remaining, freed, month: m });
    if (m > 2 && remaining >= (timeline[m - 2]?.balance ?? Infinity)) { feasible = false; break; }
  }
  const ok = feasible && m < maxMonths;
  return {
    months: ok ? m : null, simulatedMonths: m, totalInterest, timeline, feasible: ok,
    order: list.map((d) => ({ id: d.id, name: d.name, paidOffAt: d.paidOffAt, interest: d.interest })),
  };
}

/**
 * 순자산 예측. 자산별 수익률 + 저축 + 부채상환 반영.
 * scenario: bad | base | good
 */
export function project(s, months = 120, { scenario = 'base', monthlySave = null, extraDebt = null, spendDelta = 0 } = {}) {
  const m = metrics(s);
  const risk = RISK[s.profile.riskProfile] || RISK.balanced;
  const mult = scenario === 'bad' ? risk.badReturn / (risk.expectedReturn || 1)
             : scenario === 'good' ? risk.goodReturn / (risk.expectedReturn || 1)
             : 1;
  const shift = scenario === 'bad' ? -0.02 : scenario === 'good' ? 0.03 : 0;

  const assets = s.assets.map((a) => {
    const base = assetRate(a, s);
    const r = a.type === 'cash' || a.type === 'other' ? base : Math.max(-0.5, base * (mult || 1) + shift);
    return { value: n(a.value), r: mRate(r), type: a.type };
  });
  if (!assets.length) assets.push({ value: 0, r: mRate(s.profile.expectedReturn), type: 'investment' });

  const extra = extraDebt === null ? n(s.settings.extraDebtPay) : n(extraDebt);
  const debt = simulateDebt(s.debts, extra, s.settings.debtStrategy || 'avalanche', months + 12);
  const baseSave = (monthlySave === null ? m.capacity : n(monthlySave)) + spendDelta;

  const target = assets.find((a) => a.type === 'investment') || assets[0];
  const totalDebtPay = s.debts.reduce((t, d) => t + n(d.minPayment), 0) + extra;
  const series = [];
  let debtBal = m.debts;
  let freedFrom = null;   // 부채 완제 시점

  for (let i = 1; i <= months; i++) {
    for (const a of assets) a.value *= 1 + a.r;

    const step = debt.timeline[i - 1];
    debtBal = step ? Math.max(0, step.balance) : 0;
    if (debtBal <= 0 && freedFrom === null && m.debts > 0) freedFrom = i;

    // 부채를 다 갚으면 그 상환액이 통째로 저축으로 전환된다
    const freed = freedFrom !== null && i >= freedFrom ? totalDebtPay : 0;
    target.value += baseSave + freed;            // 음수면 자산에서 인출

    const assetSum = assets.reduce((t, a) => t + a.value, 0);
    series.push({ i, month: addMonths(m.key, i), assets: assetSum, debts: debtBal, net: assetSum - debtBal, save: baseSave + freed });
  }
  return { series, debt, monthlySave: baseSave, start: { net: m.net, assets: m.assets, debts: m.debts } };
}

/* ---------- 목표 계산 ---------- */
/** 목표 달성에 필요한 월 저축액 */
export function requiredSaving(targetAmount, currentAmount, months, annualReturn) {
  const fv = n(targetAmount), pv = n(currentAmount), N = Math.max(1, Math.round(months));
  const r = mRate(annualReturn);
  if (r === 0) return Math.max(0, (fv - pv) / N);
  const growth = Math.pow(1 + r, N);
  const pmt = (fv - pv * growth) / ((growth - 1) / r);
  return Math.max(0, pmt);
}

/** 월 저축액으로 목표 도달까지 걸리는 개월수 */
export function monthsToTarget(targetAmount, currentAmount, monthlySave, annualReturn) {
  const fv = n(targetAmount), pv = n(currentAmount), pmt = n(monthlySave);
  if (pv >= fv) return 0;
  const r = mRate(annualReturn);
  if (r <= 0) return pmt > 0 ? (fv - pv) / pmt : null;
  const num = fv * r + pmt;
  const den = pv * r + pmt;
  if (den <= 0 || num / den <= 0) return null;
  const mm = Math.log(num / den) / Math.log(1 + r);
  return Number.isFinite(mm) && mm > 0 && mm < 1200 ? mm : null;
}

/** 미래가치 */
export function futureValue(pv, pmt, months, annualReturn) {
  const r = mRate(annualReturn);
  const N = Math.max(0, months);
  if (r === 0) return n(pv) + n(pmt) * N;
  const g = Math.pow(1 + r, N);
  return n(pv) * g + n(pmt) * ((g - 1) / r);
}

/**
 * 여러 목표에 저축여력 배분.
 * 우선순위(1=최우선) 가중 + 마감 임박 가중.
 */
export function allocateGoals(s, capacity = null) {
  if (capacity === null) return memo('alloc', '-', () => computeAllocation(s, null));
  return computeAllocation(s, capacity);
}

function computeAllocation(s, capacity) {
  const m = metrics(s);
  const budget = capacity === null ? Math.max(0, m.capacity) : Math.max(0, capacity);
  const ret = n(s.profile.expectedReturn);

  const rows = s.goals.map((g) => {
    const left = Math.max(0, monthsUntil(g.targetDate) ?? 0);
    const need = left > 0 ? requiredSaving(g.target, g.saved, left, ret) : Math.max(0, n(g.target) - n(g.saved));
    const urgency = left > 0 ? 1 + clamp(24 / Math.max(left, 1), 0, 3) : 4;
    const weight = (4 - clamp(n(g.priority), 1, 3)) * urgency;
    return { goal: g, monthsLeft: left, required: need, weight, progress: n(g.target) > 0 ? clamp((n(g.saved) / n(g.target)) * 100, 0, 100) : 0 };
  });

  const totalRequired = rows.reduce((t, r) => t + r.required, 0);
  const totalWeight = rows.reduce((t, r) => t + r.weight, 0) || 1;

  for (const r of rows) {
    r.allocated = totalRequired <= budget
      ? r.required                                     // 여력이 충분하면 필요액 그대로
      : (r.weight / totalWeight) * budget;             // 부족하면 가중 배분
    r.gap = r.required - r.allocated;
    r.etaMonths = monthsToTarget(r.goal.target, r.goal.saved, r.allocated, ret);
    r.onTrack = r.gap <= 1000 && r.required > 0;
    r.feasible = r.allocated > 0 && r.etaMonths !== null;
  }
  rows.sort((a, b) => n(a.goal.priority) - n(b.goal.priority) || a.monthsLeft - b.monthsLeft);
  return { rows, budget, totalRequired, surplus: budget - totalRequired };
}

/* ---------- 맞춤 한도 ---------- */
/**
 * 한도 = 수입 − 목표 필요 저축 − 부채 최소상환
 * 순자산 기반 안전선(목표 소비율)도 함께 제시하고 더 보수적인 값을 쓴다.
 */
export function spendingLimit(s) {
  return memo('limit', '-', () => computeLimit(s));
}

function computeLimit(s) {
  const m = metrics(s);
  const alloc = allocateGoals(s);
  const inc = m.income;

  // 목표 저축이 아무리 커도 부채상환 후 가처분의 70%까지만 가져간다.
  // (한도가 0이 되면 지킬 수 없는 숫자가 되어 지표로서 쓸모가 없다)
  const disposable = Math.max(0, inc - m.debtPay);
  const goalNeed = Math.min(alloc.totalRequired, disposable * 0.7);
  const goalNeedCapped = alloc.totalRequired > disposable * 0.7;
  const fromIncome = inc > 0 ? Math.max(0, inc - goalNeed - m.debtPay) : null;
  const fromNet = m.net > 0 ? m.net * (n(s.profile.targetBurn) / 100) : null;

  let total, basis;
  if (s.limits.mode === 'manual' && n(s.limits.total) > 0) {
    total = n(s.limits.total); basis = 'manual';
  } else if (fromIncome !== null && fromNet !== null) {
    total = Math.min(fromIncome, fromNet);
    basis = total === fromNet ? 'net' : 'income';
  } else {
    total = fromIncome ?? fromNet ?? 0;
    basis = fromIncome !== null ? 'income' : 'net';
  }

  /* 카테고리 한도 배분.
     주거·통신·보험 같은 고정비는 계약이라 이번 달에 줄일 수 없다.
     그래서 고정비에는 실제 지출 수준을 그대로 인정하고,
     남은 예산만 변동비 카테고리에 (내 실제 소비 비중대로) 나눈다.
     기록이 없으면 표준 비중 템플릿으로 대체한다. */
  const spendCats = CATEGORIES.filter((c) => !c.skip);
  const hist = avgByCat(s, 3);
  const fixedCats = spendCats.filter((c) => c.fixed);
  const varCats = spendCats.filter((c) => !c.fixed);

  const auto = {};
  let fixedCost = 0;
  if (hist) {
    for (const c of fixedCats) auto[c.id] = Math.max(hist[c.id] || 0, m.byCat[c.id] || 0);
    const fixedNeed = fixedCats.reduce((t, c) => t + auto[c.id], 0);
    const varBudget = Math.max(0, total - fixedNeed);
    const varHist = varCats.reduce((t, c) => t + (hist[c.id] || 0), 0);
    for (const c of varCats) {
      const share = varHist > 0 ? (hist[c.id] || 0) / varHist : c.share;
      auto[c.id] = varBudget * share;
    }
    fixedCost = fixedNeed;
  } else {
    for (const c of spendCats) auto[c.id] = total * c.share;
    fixedCost = fixedCats.reduce((t, c) => t + total * c.share, 0);
  }

  const manual = s.limits.categories || {};
  const manualSum = spendCats.reduce((t, c) => t + n(manual[c.id]), 0);
  const cats = {};
  for (const c of spendCats) {
    cats[c.id] = n(manual[c.id]) > 0 ? n(manual[c.id]) : Math.round(auto[c.id] / 1000) * 1000;
  }

  return {
    total, basis, fromIncome, fromNet, goalNeed, goalNeedCapped,
    goalRequired: alloc.totalRequired,
    fixedCost, variableBudget: Math.max(0, total - fixedCost), personalized: !!hist,
    categories: cats, manualSum,
    daily: total / m.days,
    pace: (total / m.days) * m.done,     // 오늘까지 써도 되는 누적 금액
    used: m.spend,
    remain: total - m.spend,
    ratio: total > 0 ? (m.spend / total) * 100 : null,
  };
}

/* ---------- 소비 경고 ---------- */
export function warnings(s) {
  const m = metrics(s);
  const lim = spendingLimit(s);
  const out = [];
  const push = (level, icon, title, body) => out.push({ level, icon, title, body });

  if (m.net < 0) {
    push('danger', '🔻', '순자산이 마이너스입니다',
      `부채가 자산보다 ${Math.abs(m.net).toLocaleString('ko-KR')}원 많습니다. 소비율 대신 부채 상환 속도를 1순위 지표로 삼으세요.`);
  }

  if (m.txCount > 0 && lim.total > 0) {
    if (m.spend > lim.total) {
      push('danger', '🚨', '이번 달 한도를 넘었습니다',
        `한도 ${Math.round(lim.total).toLocaleString('ko-KR')}원 대비 ${Math.round(m.spend - lim.total).toLocaleString('ko-KR')}원 초과했습니다.`);
    } else if (m.spend > lim.pace * 1.15 && m.done < m.days) {
      const over = Math.round(m.spend - lim.pace);
      push('warn', '⏱️', '지출 페이스가 빠릅니다',
        `${m.done}일차 기준 적정 누적은 ${Math.round(lim.pace).toLocaleString('ko-KR')}원인데 ${over.toLocaleString('ko-KR')}원 앞서 있습니다. 이대로면 월말 ${Math.round(m.projected).toLocaleString('ko-KR')}원 예상.`);
    }
  }

  if (m.burnAnnual !== null && m.net > 0) {
    const targetAnnual = n(s.profile.targetBurn) * 12;
    if (m.burnAnnual > targetAnnual * 1.2) {
      push('warn', '📉', '순자산 대비 소비율이 목표선을 넘었습니다',
        `연환산 ${m.burnAnnual.toFixed(1)}% (목표 ${targetAnnual.toFixed(1)}%). 월 소비를 ${Math.round(Math.max(0, m.projected - (m.net * n(s.profile.targetBurn)) / 100)).toLocaleString('ko-KR')}원 줄이면 목표선에 맞습니다.`);
    }
  }

  if (m.incomeRatioProjected !== null && m.incomeRatioProjected > 70) {
    push(m.incomeRatioProjected > 90 ? 'danger' : 'warn', '💸', '월급 대비 소비가 높습니다',
      `실수령의 ${m.incomeRatioProjected.toFixed(0)}%를 쓰고 있습니다. 부채상환까지 더하면 저축여력은 ${Math.round(m.capacity).toLocaleString('ko-KR')}원입니다.`);
  }

  if (m.capacity < 0) {
    push('danger', '🔥', '이번 달 적자입니다',
      `수입보다 ${Math.abs(Math.round(m.capacity)).toLocaleString('ko-KR')}원 더 나가는 구조입니다. 자산을 헐어야 유지됩니다.`);
  }

  // 카테고리 초과 / 임박
  // 고정비는 한도가 실제 청구액과 같게 잡히므로 늘 100% 근처다. 의미 있는 초과만 알린다.
  for (const [cid, used] of Object.entries(m.byCat)) {
    const cap = lim.categories[cid];
    if (!cap) continue;
    const isFixed = !!CAT[cid]?.fixed;
    const r = (used / cap) * 100;
    if (r >= (isFixed ? 110 : 100)) push('warn', CAT[cid]?.emoji || '⚠️', `${cid} 한도 초과`,
      `${Math.round(used).toLocaleString('ko-KR')}원 사용 / 한도 ${Math.round(cap).toLocaleString('ko-KR')}원 (${r.toFixed(0)}%).` +
      (isFixed ? ' 고정비가 예년보다 늘었습니다.' : ''));
    else if (!isFixed && r >= 85) push('info', CAT[cid]?.emoji || 'ℹ️', `${cid} 한도 임박`,
      `한도의 ${r.toFixed(0)}%를 썼습니다. 남은 예산 ${Math.round(cap - used).toLocaleString('ko-KR')}원.`);
  }

  // 고정비가 한도를 다 먹는 구조
  if (lim.total > 0 && lim.fixedCost > lim.total * 0.6) {
    push('warn', '🧱', '고정비가 한도의 대부분을 차지합니다',
      `한도 ${Math.round(lim.total).toLocaleString('ko-KR')}원 중 고정비가 ${Math.round(lim.fixedCost).toLocaleString('ko-KR')}원입니다. ` +
      `변동비로 쓸 수 있는 돈은 ${Math.round(lim.variableBudget).toLocaleString('ko-KR')}원뿐이라 조절 여지가 적습니다.`);
  }

  // 큰 단일 지출
  if (m.net > 0) {
    const largest = monthTx(s, m.key)
      .filter((t) => !CAT[t.category]?.skip)
      .sort((a, b) => n(b.amount) - n(a.amount))[0];
    if (largest && n(largest.amount) > m.net * 0.01) {
      push('info', '🔍', '순자산 1%가 넘는 지출',
        `${largest.category} ${Math.round(n(largest.amount)).toLocaleString('ko-KR')}원 — 순자산의 ${((n(largest.amount) / m.net) * 100).toFixed(1)}%입니다.`);
    }
  }

  // 비상금
  if (m.emergency !== null && m.projected > 0 && m.emergency < 3) {
    push('warn', '🧯', '비상금이 부족합니다',
      `현금성 자산이 ${m.emergency.toFixed(1)}개월치입니다. 목표 ${s.profile.emergencyMonths}개월까지 ${Math.round(Math.max(0, m.projected * s.profile.emergencyMonths - m.cash)).toLocaleString('ko-KR')}원 더 필요합니다.`);
  }

  // 고금리 부채
  const hi = s.debts.filter((d) => n(d.rate) >= 10 && n(d.balance) > 0);
  if (hi.length) {
    push('danger', '🧨', '고금리 부채가 있습니다',
      `${hi.map((d) => `${d.name || '부채'} ${n(d.rate)}%`).join(', ')} — 어떤 투자보다 상환 수익률이 확실합니다.`);
  }

  if (!out.length) {
    push('good', '✅', '경고 없음', '현재 소비 구조에서 즉시 조치가 필요한 항목이 없습니다.');
  }
  const rank = { danger: 0, warn: 1, info: 2, good: 3 };
  out.sort((a, b) => rank[a.level] - rank[b.level]);
  return out;
}
