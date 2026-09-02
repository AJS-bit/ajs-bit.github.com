/* 상태 저장소 — localStorage 영속화. 데이터는 기기 밖으로 나가지 않는다. */
import { uid, monthKey, today } from './format.js';

const KEY = 'asset-compass.v1';

/* ---------- 분류 체계 ---------- */
export const ASSET_TYPES = {
  cash:       { label: '현금성',   emoji: '💵', rate: 0.030, liquid: true,  color: '#38bdf8' },
  investment: { label: '투자',     emoji: '📈', rate: 0.070, liquid: true,  color: '#5b8dff' },
  pension:    { label: '연금',     emoji: '🏦', rate: 0.055, liquid: false, color: '#8b5cf6' },
  realestate: { label: '부동산',   emoji: '🏠', rate: 0.025, liquid: false, color: '#f59e0b' },
  other:      { label: '기타',     emoji: '🎁', rate: 0.000, liquid: false, color: '#64748b' },
};

export const DEBT_TYPES = {
  mortgage: { label: '주택담보', emoji: '🏠', rate: 4.0 },
  credit:   { label: '신용대출', emoji: '💳', rate: 6.5 },
  student:  { label: '학자금',   emoji: '🎓', rate: 2.0 },
  card:     { label: '카드/리볼빙', emoji: '🧾', rate: 15.0 },
  personal: { label: '개인/기타', emoji: '🤝', rate: 5.0 },
};

/* 소비 카테고리. fixed=고정비, skip=소비율 계산에서 제외(이체/상환) */
export const CATEGORIES = [
  { id: '식비',      emoji: '🍚', color: '#f97316', share: 0.22 },
  { id: '카페/간식', emoji: '☕', color: '#d97706', share: 0.05 },
  { id: '교통',      emoji: '🚌', color: '#0ea5e9', share: 0.07 },
  { id: '주거/관리', emoji: '🏡', color: '#8b5cf6', share: 0.22, fixed: true },
  { id: '통신',      emoji: '📱', color: '#6366f1', share: 0.04, fixed: true },
  { id: '보험',      emoji: '🛡️', color: '#0d9488', share: 0.05, fixed: true },
  { id: '구독',      emoji: '🔁', color: '#a855f7', share: 0.02, fixed: true },
  { id: '쇼핑',      emoji: '🛍️', color: '#ec4899', share: 0.10 },
  { id: '문화/여가', emoji: '🎬', color: '#14b8a6', share: 0.07 },
  { id: '의료/건강', emoji: '💊', color: '#22c55e', share: 0.05 },
  { id: '교육',      emoji: '📚', color: '#3b82f6', share: 0.05 },
  { id: '경조사',    emoji: '🎁', color: '#f43f5e', share: 0.03 },
  { id: '기타',      emoji: '⋯',  color: '#64748b', share: 0.03 },
  { id: '저축/투자', emoji: '🌱', color: '#34d17e', share: 0,    skip: true },
  { id: '대출상환',  emoji: '🏧', color: '#94a3b8', share: 0,    skip: true },
];
export const CAT = Object.fromEntries(CATEGORIES.map((c) => [c.id, c]));
export const SPEND_CATEGORIES = CATEGORIES.filter((c) => !c.skip);

export const RISK = {
  conservative: { label: '안정형', expectedReturn: 0.04, badReturn: 0.01, goodReturn: 0.06 },
  balanced:     { label: '균형형', expectedReturn: 0.06, badReturn: 0.02, goodReturn: 0.09 },
  aggressive:   { label: '공격형', expectedReturn: 0.08, badReturn: 0.00, goodReturn: 0.13 },
};

/* ---------- 기본 상태 ---------- */
export function blankState() {
  return {
    version: 1,
    profile: {
      nickname: '',
      monthlyIncome: 0,       // 월 실수령액
      extraIncome: 0,         // 부수입
      riskProfile: 'balanced',
      expectedReturn: 0.06,   // 투자자산 연 기대수익률
      inflation: 0.025,
      targetBurn: 2.0,        // 목표 월 소비율(순자산 대비 %)
      emergencyMonths: 6,
      startedAt: today(),
    },
    assets: [],
    debts: [],
    transactions: [],
    goals: [],
    limits: { mode: 'auto', total: null, categories: {} },
    snapshots: [],            // [{ month:'2026-09', net, assets, debts }]
    settings: { theme: 'light', onboarded: false, debtStrategy: 'avalanche', extraDebtPay: 0 },
  };
}

/* ---------- 영속화 ---------- */
function migrate(raw) {
  const base = blankState();
  const s = { ...base, ...raw };
  s.profile = { ...base.profile, ...(raw.profile || {}) };
  s.limits = { ...base.limits, ...(raw.limits || {}) };
  s.settings = { ...base.settings, ...(raw.settings || {}) };
  for (const k of ['assets', 'debts', 'transactions', 'goals', 'snapshots']) {
    if (!Array.isArray(s[k])) s[k] = [];
  }
  return s;
}

function load() {
  try {
    const raw = localStorage.getItem(KEY);
    if (!raw) return blankState();
    return migrate(JSON.parse(raw));
  } catch (e) {
    console.warn('저장된 데이터를 읽지 못했습니다.', e);
    return blankState();
  }
}

export const state = load();

const listeners = new Set();
export function subscribe(fn) { listeners.add(fn); return () => listeners.delete(fn); }

/* 상태가 바뀔 때마다 증가. 파생 계산 캐시를 무효화하는 데 쓴다. */
let _rev = 0;
export const rev = () => _rev;

let saveTimer = null;
export function commit({ silent = false } = {}) {
  _rev += 1;
  clearTimeout(saveTimer);
  saveTimer = setTimeout(() => {
    try { localStorage.setItem(KEY, JSON.stringify(state)); }
    catch (e) { console.warn('저장 실패', e); }
  }, 120);
  if (!silent) listeners.forEach((fn) => fn(state));
}

/** 변경 함수를 감싸 실행하고 저장 + 리렌더 */
export function update(fn) { const r = fn(state); commit(); return r; }

/* ---------- 컬렉션 헬퍼 ---------- */
export function addAsset(a) {
  state.assets.push({ id: uid(), name: '', type: 'cash', value: 0, updatedAt: today(), ...a });
  commit();
}
export function addDebt(d) {
  state.debts.push({ id: uid(), name: '', type: 'credit', balance: 0, rate: 5, minPayment: 0, ...d });
  commit();
}
export function addTx(t) {
  state.transactions.push({ id: uid(), date: today(), amount: 0, category: '기타', memo: '', ...t });
  state.transactions.sort((a, b) => (a.date < b.date ? 1 : a.date > b.date ? -1 : 0));
  commit();
}
export function addGoal(g) {
  state.goals.push({
    id: uid(), name: '', emoji: '🎯', target: 0, targetDate: '',
    priority: 2, saved: 0, kind: 'custom', ...g,
  });
  commit();
}
export function remove(coll, id) {
  const i = state[coll].findIndex((x) => x.id === id);
  if (i >= 0) { state[coll].splice(i, 1); commit(); }
}
export function patch(coll, id, fields) {
  const it = state[coll].find((x) => x.id === id);
  if (it) { Object.assign(it, fields); commit(); }
}

/** 이번 달 순자산 스냅샷 기록(같은 달이면 갱신) */
export function snapshot(net, assets, debts, month = monthKey()) {
  const found = state.snapshots.find((s) => s.month === month);
  if (found) Object.assign(found, { net, assets, debts });
  else state.snapshots.push({ month, net, assets, debts });
  state.snapshots.sort((a, b) => (a.month < b.month ? -1 : 1));
  if (state.snapshots.length > 120) state.snapshots.splice(0, state.snapshots.length - 120);
  commit({ silent: true });
}

export function replaceAll(next) {
  const fresh = migrate(next);
  Object.keys(state).forEach((k) => delete state[k]);
  Object.assign(state, fresh);
  commit();
}

export function resetAll() { replaceAll(blankState()); }

export function exportJSON() {
  return JSON.stringify({ ...state, _exportedAt: new Date().toISOString() }, null, 2);
}
