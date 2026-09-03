/* 자산 나침반 — 앱 컨트롤러 (라우팅 · 액션 · 모달) */
import { state, commit, subscribe, ASSET_TYPES, DEBT_TYPES, CATEGORIES, SPEND_CATEGORIES, RISK, addAsset, addDebt, addTx, addGoal, remove, patch, snapshot, replaceAll, resetAll, exportJSON } from './store.js';
import { totals, metrics, spendingLimit, warnings } from './finance.js';
import { demoState } from './seed.js';
import { $, modal, toast, confirmDialog, WARN_ACTION } from './ui.js';
import { esc } from './charts.js';
import { n, today, monthKey, addMonths, uid, clamp, won, compact } from './format.js';

import * as Dashboard from './views/dashboard.js';
import * as Assets from './views/assets.js';
import * as Spending from './views/spending.js';
import * as Goals from './views/goals.js';
import * as Coach from './views/coach.js';

const VIEWS = { dashboard: Dashboard, assets: Assets, spending: Spending, goals: Goals, coach: Coach };

const NAV = [
  { id: 'dashboard', label: '홈', icon: '<path d="M4 11 12 4l8 7v8a1 1 0 0 1-1 1h-4v-6H9v6H5a1 1 0 0 1-1-1z"/>' },
  { id: 'assets', label: '자산', icon: '<path d="M3 7.5A1.5 1.5 0 0 1 4.5 6h15A1.5 1.5 0 0 1 21 7.5v9a1.5 1.5 0 0 1-1.5 1.5h-15A1.5 1.5 0 0 1 3 16.5z"/><circle cx="16.5" cy="12" r="1.6" fill="var(--bg)"/>' },
  { id: 'spending', label: '지출', icon: '<path d="M6 3h12l1.5 18-7.5-3-7.5 3z"/>' },
  { id: 'goals', label: '목표', icon: '<circle cx="12" cy="12" r="8.4"/><circle cx="12" cy="12" r="4.8" fill="var(--bg)"/><circle cx="12" cy="12" r="1.8"/>' },
  { id: 'coach', label: '코치', icon: '<rect x="4" y="7" width="16" height="12" rx="3.2"/><circle cx="9" cy="13" r="1.5" fill="var(--bg)"/><circle cx="15" cy="13" r="1.5" fill="var(--bg)"/><path d="M12 3v3.4" stroke="currentColor" stroke-width="1.8" fill="none"/>' },
];

let route = 'dashboard';
let subtab = {};

/* ---------- 렌더 ---------- */
function renderNav() {
  $('#nav').innerHTML = NAV.map((v) => `
    <button data-nav="${v.id}" class="${route === v.id ? 'is-on' : ''}" aria-current="${route === v.id ? 'page' : 'false'}">
      <svg viewBox="0 0 24 24" width="21" height="21" fill="currentColor">${v.icon}</svg>
      <span>${v.label}</span>
    </button>`).join('');
}

/* 상단 벨 배지 = 처리할 경고 건수 (info/good 은 세지 않는다) */
function renderBadge() {
  const badge = $('#bell-badge');
  if (!badge) return;
  const ws = warnings(state).filter((w) => w.level === 'danger' || w.level === 'warn');
  badge.hidden = ws.length === 0;
  badge.textContent = ws.length > 9 ? '9+' : String(ws.length);
  badge.classList.toggle('badge--warn', !ws.some((w) => w.level === 'danger'));
}

function render() {
  const view = VIEWS[route] || Dashboard;
  const tab = subtab[route] || view.tabs?.[0]?.id;
  const tabsHTML = view.tabs
    ? `<div class="tabs">${view.tabs.map((t) => `
        <button data-tab="${t.id}" class="${tab === t.id ? 'is-on' : ''}">${t.label}</button>`).join('')}</div>`
    : '';
  const main = $('#main');
  const y = main.scrollTop;
  main.innerHTML = tabsHTML + view.render(tab);
  renderNav();
  renderBadge();
  main.scrollTop = y;
}

function go(r, tab) {
  if (VIEWS[r]) { route = r; if (tab) subtab[r] = tab; }
  else if (r === 'debt') { route = 'assets'; subtab.assets = 'strategy'; }
  else if (r === 'forecast') { route = 'goals'; subtab.goals = 'forecast'; }
  else if (r === 'limit') { route = 'spending'; subtab.spending = 'limit'; }
  else if (r === 'tx') { route = 'spending'; subtab.spending = 'list'; }
  window.scrollTo({ top: 0 });
  $('#main').scrollTop = 0;
  render();
  location.hash = route;
}

/* ---------- 모달: 자산 ---------- */
async function assetModal(existing) {
  const r = await modal({
    title: existing ? '자산 수정' : '자산 추가',
    fields: [
      { key: 'name', label: '이름', value: existing?.name ?? '', placeholder: '예: 주거래 통장', required: true },
      { key: 'type', label: '종류', type: 'select', value: existing?.type ?? 'cash',
        options: Object.entries(ASSET_TYPES).map(([k, v]) => ({ value: k, label: `${v.emoji} ${v.label}` })) },
      { key: 'value', label: '평가금액', money: true, value: existing?.value ?? '', required: true },
      { key: 'returnRate', label: '연 기대수익률 (비워두면 종류별 기본값)', type: 'number', unit: '%',
        step: '0.1', value: existing?.returnRate ?? '' },
    ],
    submit: existing ? '수정' : '추가',
  });
  if (!r) return;
  const fields = { name: r.name, type: r.type, value: r.value, updatedAt: today(),
    returnRate: r.returnRate === 0 && !String(r.returnRate).length ? '' : r.returnRate };
  if (existing) { patch('assets', existing.id, fields); toast('자산을 수정했습니다'); }
  else { addAsset(fields); toast('자산을 추가했습니다'); }
  syncSnapshot();
}

/* ---------- 모달: 부채 ---------- */
async function debtModal(existing) {
  const r = await modal({
    title: existing ? '부채 수정' : '부채 추가',
    fields: [
      { key: 'name', label: '이름', value: existing?.name ?? '', placeholder: '예: 마이너스통장', required: true },
      { key: 'type', label: '종류', type: 'select', value: existing?.type ?? 'credit',
        options: Object.entries(DEBT_TYPES).map(([k, v]) => ({ value: k, label: `${v.emoji} ${v.label}` })) },
      { key: 'balance', label: '남은 원금', money: true, value: existing?.balance ?? '', required: true },
      { key: 'rate', label: '연 이자율', type: 'number', unit: '%', step: '0.01', value: existing?.rate ?? 5 },
      { key: 'minPayment', label: '월 상환액 (최소)', money: true, value: existing?.minPayment ?? '',
        help: '원리금 합계로 매달 실제 나가는 금액을 넣으세요.' },
    ],
    submit: existing ? '수정' : '추가',
  });
  if (!r) return;
  if (existing) { patch('debts', existing.id, r); toast('부채를 수정했습니다'); }
  else { addDebt(r); toast('부채를 추가했습니다'); }
  syncSnapshot();
}

/* ---------- 모달: 지출 ---------- */
async function txModal(existing) {
  const catOptions = CATEGORIES.map((c) => ({ value: c.id, label: `${c.emoji} ${c.id}${c.skip ? ' (소비율 제외)' : ''}` }));
  const r = await modal({
    title: existing ? '지출 수정' : '지출 입력',
    fields: [
      { key: 'amount', label: '금액', money: true, value: existing?.amount ?? '', required: true },
      { key: 'category', label: '카테고리', type: 'select', value: existing?.category ?? '식비', options: catOptions },
      { key: 'date', label: '날짜', type: 'date', value: existing?.date ?? today() },
      { key: 'memo', label: '메모', value: existing?.memo ?? '', placeholder: '선택 사항' },
    ],
    submit: existing ? '수정' : '기록',
  });
  if (!r) return;
  if (existing) { patch('transactions', existing.id, r); toast('수정했습니다'); }
  else {
    addTx(r);
    const m = metrics(state);
    const lim = spendingLimit(state);
    const msg = m.net > 0 && n(r.amount) > m.net * 0.005
      ? `기록 완료 · 순자산의 ${((n(r.amount) / m.net) * 100).toFixed(2)}%`
      : lim.total > 0 && lim.remain < 0 ? `기록 완료 · 한도 ${won(-lim.remain)} 초과`
      : lim.total > 0 ? `기록 완료 · 남은 한도 ${won(lim.remain)}` : '기록했습니다';
    toast(msg, 2800);
  }
}

/* ---------- 모달: 목표 ---------- */
async function goalModal(existing) {
  const d = new Date(); d.setMonth(d.getMonth() + 36);
  const r = await modal({
    title: existing ? '목표 수정' : '목표 추가',
    fields: [
      { key: 'emoji', label: '아이콘', value: existing?.emoji ?? '🎯', placeholder: '🎯' },
      { key: 'name', label: '목표 이름', value: existing?.name ?? '', placeholder: '예: 내 집 마련 종잣돈', required: true },
      { key: 'target', label: '목표 금액', money: true, value: existing?.target ?? '', required: true },
      { key: 'saved', label: '현재까지 모은 금액', money: true, value: existing?.saved ?? 0 },
      { key: 'targetDate', label: '목표 시점', type: 'date', value: existing?.targetDate || d.toISOString().slice(0, 10) },
      { key: 'priority', label: '우선순위', type: 'seg', value: String(existing?.priority ?? 2),
        options: [{ value: '1', label: '최우선' }, { value: '2', label: '보통' }, { value: '3', label: '여유' }] },
    ],
    submit: existing ? '수정' : '추가',
  });
  if (!r) return;
  const fields = { ...r, priority: Number(r.priority) || 2 };
  if (existing) { patch('goals', existing.id, fields); toast('목표를 수정했습니다'); }
  else { addGoal(fields); toast('목표를 추가했습니다'); }
}

/* ---------- 모달: 설정 ---------- */
async function settingsModal() {
  const p = state.profile;
  const r = await modal({
    title: '설정',
    fields: [
      { key: 'monthlyIncome', label: '월 실수령액', money: true, value: p.monthlyIncome,
        help: '세금·4대보험을 뺀 실제 입금액' },
      { key: 'extraIncome', label: '월 부수입', money: true, value: p.extraIncome },
      { key: 'riskProfile', label: '투자 성향', type: 'seg', value: p.riskProfile,
        options: Object.entries(RISK).map(([k, v]) => ({ value: k, label: v.label })) },
      { key: 'expectedReturn', label: '연 기대수익률', type: 'number', unit: '%', step: '0.1',
        value: (n(p.expectedReturn) * 100).toFixed(1), help: '투자자산에 적용됩니다' },
      { key: 'inflation', label: '물가상승률', type: 'number', unit: '%', step: '0.1', value: (n(p.inflation) * 100).toFixed(1) },
      { key: 'targetBurn', label: '목표 월 소비율 (순자산 대비)', type: 'number', unit: '%', step: '0.1',
        value: n(p.targetBurn), help: '연 4% 이하면 자산 수익만으로 생활 가능한 수준입니다 (월 0.33%)' },
      { key: 'emergencyMonths', label: '비상금 목표', type: 'number', unit: '개월', step: '1', value: p.emergencyMonths },
      { key: 'theme', label: '화면 테마', type: 'seg', value: state.settings.theme || 'dark',
        options: [{ value: 'dark', label: '다크' }, { value: 'light', label: '라이트' }, { value: 'system', label: '시스템 설정' }] },
    ],
    submit: '저장',
  });
  if (!r) return;
  applyTheme(r.theme);
  Object.assign(state.profile, {
    monthlyIncome: r.monthlyIncome,
    extraIncome: r.extraIncome,
    riskProfile: r.riskProfile,
    expectedReturn: n(r.expectedReturn) / 100,
    inflation: n(r.inflation) / 100,
    targetBurn: clamp(n(r.targetBurn), 0.05, 50),
    emergencyMonths: clamp(Math.round(n(r.emergencyMonths)), 1, 36),
  });
  commit();
  toast('설정을 저장했습니다');
}

/* ---------- 모달: 카테고리 한도 ---------- */
async function catLimitModal() {
  const lim = spendingLimit(state);
  await modal({
    title: '카테고리별 한도',
    wide: true,
    fields: SPEND_CATEGORIES.map((c) => ({
      key: c.id, label: `${c.emoji} ${c.id}`, money: true,
      value: Math.round(lim.categories[c.id] || 0),
    })),
    submit: '저장',
    onSubmit: (data) => {
      state.limits.categories = {};
      for (const c of SPEND_CATEGORIES) {
        const v = n(data[c.id]);
        if (v > 0) state.limits.categories[c.id] = v;
      }
      commit();
      toast('카테고리 한도를 저장했습니다');
    },
  });
}

/* ---------- 알림 ----------
   경고를 읽고 나면 조치할 곳으로 갈 수 있어야 한다. 예전에는 홈·알림 모달·지출 한도
   세 곳이 모두 경고를 보여주면서 링크가 하나도 없어 전부 막다른 길이었다.
   모달 안의 버튼에는 data-nav 와 data-close 를 함께 준다. modal() 이 [data-close] 에
   직접 리스너를 달고 document.body 위임 리스너가 data-nav 를 처리하므로,
   한 번의 클릭으로 모달이 닫히면서 이동한다. modal() 은 고치지 않아도 된다. */

async function notificationsModal() {
  const ws = warnings(state);
  const act = ws.filter((w) => w.level === 'danger' || w.level === 'warn');
  await modal({
    title: act.length ? `알림 ${act.length}건` : '알림',
    fields: [], onSubmit: null,
    html: `
      ${act.length === 0 ? `<div class="alert alert--good">
        <span class="alert__ico">✅</span><div><b>지금 조치할 일이 없습니다</b>
        <p>현재 소비 구조에서 급한 경고가 없습니다.</p></div></div>` : ''}
      ${ws.map((w) => `<div class="alert alert--${w.level}">
        <span class="alert__ico">${w.icon}</span>
        <div><b>${esc(w.title)}</b><p>${esc(w.body)}</p>
        ${w.route ? `<button class="btn btn--sm btn--ghost" style="margin-top:8px"
          data-nav="${w.route}" data-close>${esc(WARN_ACTION[w.route] || '보러 가기')}</button>` : ''}
        </div></div>`).join('')}`,
  });
}

/* ---------- 데이터 입출력 ---------- */
function exportData() {
  const blob = new Blob([exportJSON()], { type: 'application/json' });
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = `자산나침반_${today()}.json`;
  document.body.appendChild(a); a.click(); a.remove();
  setTimeout(() => URL.revokeObjectURL(a.href), 1000);
  toast('내보내기 완료');
}

function importData() {
  const inp = document.createElement('input');
  inp.type = 'file'; inp.accept = 'application/json,.json';
  inp.onchange = () => {
    const f = inp.files?.[0]; if (!f) return;
    const fr = new FileReader();
    fr.onload = () => {
      try {
        const data = JSON.parse(String(fr.result));
        if (!data || typeof data !== 'object') throw new Error('형식 오류');
        replaceAll(data);
        toast('불러오기 완료');
        go('dashboard');
      } catch (e) { toast('파일을 읽을 수 없습니다'); }
    };
    fr.readAsText(f);
  };
  inp.click();
}

/* ---------- 순자산 스냅샷 자동 기록 ---------- */
function syncSnapshot() {
  const t = totals(state);
  if (state.assets.length || state.debts.length) snapshot(t.net, t.assets, t.debts);
}

/* ---------- 액션 라우팅 ---------- */
const ACTIONS = {
  notifications: notificationsModal,
  settings: settingsModal,
  'add-asset': () => assetModal(),
  'add-debt': () => debtModal(),
  'add-goal': () => goalModal(),
  'quick-add': () => txModal(),
  export: exportData,
  import: importData,
  'edit-cat-limits': catLimitModal,

  'edit-asset': (el) => assetModal(state.assets.find((a) => a.id === el.dataset.id)),
  'edit-debt': (el) => debtModal(state.debts.find((d) => d.id === el.dataset.id)),
  'edit-tx': (el) => txModal(state.transactions.find((t) => t.id === el.dataset.id)),
  'edit-goal': (el) => goalModal(state.goals.find((g) => g.id === el.dataset.id)),

  'del-asset': async (el) => {
    const a = state.assets.find((x) => x.id === el.dataset.id);
    if (await confirmDialog('자산 삭제', `<b>${esc(a?.name || '')}</b> (${compact(a?.value)})을 삭제할까요?`)) {
      remove('assets', el.dataset.id); syncSnapshot(); toast('삭제했습니다');
    }
  },
  'del-debt': async (el) => {
    const d = state.debts.find((x) => x.id === el.dataset.id);
    if (await confirmDialog('부채 삭제', `<b>${esc(d?.name || '')}</b> (${compact(d?.balance)})을 삭제할까요?`)) {
      remove('debts', el.dataset.id); syncSnapshot(); toast('삭제했습니다');
    }
  },
  'del-tx': (el) => { remove('transactions', el.dataset.id); toast('삭제했습니다'); },
  'del-goal': async (el) => {
    const g = state.goals.find((x) => x.id === el.dataset.id);
    if (await confirmDialog('목표 삭제', `<b>${esc(g?.name || '')}</b> 목표를 삭제할까요?`)) {
      remove('goals', el.dataset.id); toast('삭제했습니다');
    }
  },

  'load-demo': async () => {
    if (state.assets.length || state.transactions.length) {
      if (!(await confirmDialog('예시 데이터 불러오기',
        '현재 입력한 데이터가 예시 데이터로 <b>대체</b>됩니다. 계속할까요?', '대체하기'))) return;
    }
    replaceAll(demoState());
    toast('예시 데이터를 불러왔습니다');
    go('dashboard');
  },
  reset: async () => {
    if (await confirmDialog('전체 초기화',
      '모든 자산·지출·목표 기록이 <b>영구 삭제</b>됩니다. 되돌릴 수 없습니다.', '전부 삭제')) {
      resetAll(); toast('초기화했습니다'); go('dashboard');
    }
  },

  'all-warnings': () => notificationsModal(),


  'edit-limit': async () => {
    const lim = spendingLimit(state);
    const r = await modal({
      title: '한도 설정',
      fields: [
        { key: 'mode', label: '계산 방식', type: 'seg', value: state.limits.mode,
          options: [{ value: 'auto', label: '자동 계산' }, { value: 'manual', label: '직접 입력' }] },
        { key: 'total', label: '총 한도 (직접 입력 시)', money: true, value: Math.round(n(state.limits.total) || lim.total) },
        { key: 'targetBurn', label: '목표 월 소비율', type: 'number', unit: '%', step: '0.1', value: n(state.profile.targetBurn) },
      ],
      submit: '저장',
    });
    if (!r) return;
    state.limits.mode = r.mode;
    state.limits.total = r.total;
    state.profile.targetBurn = clamp(n(r.targetBurn), 0.05, 50);
    commit();
    toast('한도를 저장했습니다');
  },

  'reset-cat-limits': () => { state.limits.categories = {}; commit(); toast('자동 배분으로 되돌렸습니다'); },

  'month-prev': () => { Spending.setMonth(addMonths(Spending.getMonth(), -1)); render(); },
  'month-next': () => {
    if (Spending.getMonth() >= monthKey()) return;
    Spending.setMonth(addMonths(Spending.getMonth(), 1)); render();
  },

  'pick-goal': (el) => { state.settings.homeGoal = el.dataset.id; commit(); },

  'add-preset': (el) => addPreset(el.dataset.key),
  'add-all-presets': () => {
    const s = state;
    Goals.PRESETS.filter((p) => !p.hideIf?.(s)).forEach((p) => addPreset(p.key, true));
    commit(); toast('추천 목표를 만들었습니다');
  },

  'add-to-goal': async (el) => {
    const g = state.goals.find((x) => x.id === el.dataset.id);
    if (!g) return;
    const r = await modal({
      title: `${g.emoji} ${g.name} 적립`,
      fields: [{ key: 'amount', label: '적립 금액', money: true, value: '', required: true }],
      html: `<p class="hint">현재 ${compact(g.saved)} / 목표 ${compact(g.target)}</p>`,
      submit: '적립',
    });
    if (!r) return;
    patch('goals', g.id, { saved: n(g.saved) + n(r.amount) });
    toast(`${won(r.amount)} 적립했습니다`);
  },

  'sim-goal': (el) => {
    const g = state.goals.find((x) => x.id === el.dataset.id);
    if (!g) return;
    Goals.sim.target = n(g.target);
    const left = Math.max(1, Math.round((new Date(g.targetDate) - new Date()) / (1000 * 60 * 60 * 24 * 30)));
    Goals.sim.years = clamp(Math.round(left / 12) || 1, 1, 40);
    Goals.sim.monthly = null;
    go('goals', 'sim');
  },

  'sim-to-goal': () => {
    addGoal({
      name: `${compact(Goals.sim.target)} 모으기`, emoji: '🎯',
      target: Goals.sim.target, saved: Math.max(0, totals(state).net),
      targetDate: (() => { const d = new Date(); d.setFullYear(d.getFullYear() + Goals.sim.years); return d.toISOString().slice(0, 10); })(),
      priority: 2,
    });
    toast('목표로 저장했습니다');
    go('goals', 'list');
  },
};

function addPreset(key, silent = false) {
  const p = Goals.PRESETS.find((x) => x.key === key);
  if (!p) return;
  const m = metrics(state);
  const d = new Date(); d.setMonth(d.getMonth() + p.months);
  const amount = Math.round(p.amount(state, m) / 10000) * 10000;
  if (amount <= 0) return;
  state.goals.push({
    id: uid(), name: p.name, emoji: p.emoji, target: amount,
    targetDate: d.toISOString().slice(0, 10), priority: p.priority,
    saved: p.key === 'emergency' ? Math.min(totals(state).cash, amount)
      : p.key === 'first100' ? Math.max(0, totals(state).net) : 0,
    kind: 'preset',
  });
  if (!silent) { commit(); toast(`'${p.name}' 목표를 만들었습니다`); }
}

/* ---------- 이벤트 바인딩 ---------- */
function bind() {
  const main = $('#main');

  document.body.addEventListener('click', (e) => {
    const navBtn = e.target.closest('[data-nav]');
    if (navBtn) { go(navBtn.dataset.nav); return; }
    const tabBtn = e.target.closest('#main [data-tab]');
    if (tabBtn) { subtab[route] = tabBtn.dataset.tab; render(); return; }
    const act = e.target.closest('[data-act]');
    if (act && ACTIONS[act.dataset.act]) { ACTIONS[act.dataset.act](act); return; }

    // 인라인 토글류
    const strat = e.target.closest('[data-act="set-strategy"]');
    if (strat) { state.settings.debtStrategy = strat.dataset.v; commit(); return; }
    const lm = e.target.closest('[data-act="limit-mode"]');
    if (lm) { state.limits.mode = lm.dataset.v; commit(); return; }
    const reset = e.target.closest('[data-act="scenario-reset"]');
    if (reset) { Dashboard.resetScenario(); render(); return; }
    const simSet = e.target.closest('[data-sim-set]');
    if (simSet) { Goals.sim[simSet.dataset.simSet] = n(simSet.dataset.v); render(); return; }
  });

  // 슬라이더 (즉시 반영)
  main.addEventListener('input', (e) => {
    const el = e.target;
    if (el.dataset.sim) {
      Goals.sim[el.dataset.sim] = el.dataset.sim === 'returnRate' ? Number(el.value) : n(el.value);
      Goals.liveSim(el);
    } else if (el.dataset.fc) {
      Goals.fc[el.dataset.fc] = n(el.value); Goals.liveFc();
    } else if (el.dataset.whatif) {
      Coach.whatif[el.dataset.whatif] = n(el.value); Coach.liveWhatIf();
    } else if (el.dataset.act === 'extra-pay') {
      state.settings.extraDebtPay = n(el.value); commit({ silent: true }); Assets.liveExtraPay();
    } else if (el.dataset.act === 'target-burn') {
      state.profile.targetBurn = Number(el.value); commit({ silent: true }); Coach.liveTargetBurn();
    } else if (el.dataset.scenario === 'spend') {
      // 가상 시나리오다. 저장하지 않는다.
      Dashboard.setScenarioSpend(n(el.value), null);
      Dashboard.liveBurn();
    }
  });

  main.addEventListener('change', (e) => {
    const el = e.target;
    // 드래그를 놓은 시점에만 전체를 다시 그린다. 상단 알림 배지처럼
    // 화면 밖 요소는 부분 갱신이 닿지 않으므로 여기서 맞춘다.
    if (el.dataset.act === 'manual-total') {
      state.limits.total = n(el.value); state.limits.mode = 'manual'; commit();
    } else if (el.dataset.sim || el.dataset.fc || el.dataset.whatif) {
      render();
    } else if (el.dataset.act === 'extra-pay' || el.dataset.act === 'target-burn') {
      commit();
    } else if (el.dataset.scenario === 'spend') {
      // 드래그를 놓은 시점에만 전체를 다시 그린다. 저장은 하지 않는다.
      render();
    }
  });

  window.addEventListener('hashchange', () => {
    const h = location.hash.slice(1);
    if (h && VIEWS[h] && h !== route) { route = h; render(); }
  });

  // 키보드 단축키
  document.addEventListener('keydown', (e) => {
    if (e.target.matches('input,select,textarea') || $('#modal-root').children.length) return;
    const i = ['1', '2', '3', '4', '5'].indexOf(e.key);
    if (i >= 0) go(NAV[i].id);
    if (e.key === 'n' || e.key === 'ㅜ') txModal();
  });
}

/* ---------- 테마 ---------- */
const prefersDark = () =>
  typeof matchMedia === 'function' && matchMedia('(prefers-color-scheme: dark)').matches;

/** 'dark' | 'light' | 'system' */
function applyTheme(pref) {
  const resolved = pref === 'system' ? (prefersDark() ? 'dark' : 'light') : pref === 'light' ? 'light' : 'dark';
  document.documentElement.dataset.theme = resolved;
  document.querySelector('meta[name=theme-color]')
    ?.setAttribute('content', resolved === 'dark' ? '#0b0f19' : '#f4f6fb');
  state.settings.theme = pref;
  commit({ silent: true });
}

/* ---------- 부팅 ---------- */
function boot() {
  applyTheme(state.settings.theme || 'dark');
  if (typeof matchMedia === 'function') {
    matchMedia('(prefers-color-scheme: dark)').addEventListener?.('change', () => {
      if (state.settings.theme === 'system') { applyTheme('system'); render(); }
    });
  }

  const h = location.hash.slice(1);
  if (VIEWS[h]) route = h;

  subscribe(render);
  bind();
  syncSnapshot();
  render();

  if ('serviceWorker' in navigator && location.protocol === 'https:') {
    navigator.serviceWorker.register('./sw.js').catch(() => {});
  }
}

boot();
