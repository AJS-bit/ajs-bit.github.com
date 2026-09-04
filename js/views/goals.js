/* 목표 — 여러 목표 관리 · 기본 목표 · 목표자산 시뮬레이션 · 미래 자산 예측 */
import { state } from '../store.js';
import { metrics, allocateGoals, requiredSaving, monthsToTarget, futureValue, project, totals, weightedReturn } from '../finance.js';
import { compact, won, pct, months as fmtMonths, n, clamp } from '../format.js';
import { lineChart, progress, legend, esc } from '../charts.js';
import { card, empty, setHTML, setText, setAttr } from '../ui.js';

export const title = '목표';
export const tabs = [
  { id: 'list', label: '내 목표' },
  { id: 'sim', label: '시뮬레이션' },
  { id: 'forecast', label: '미래 예측' },
];

/* 시뮬레이터 로컬 상태 */
export const sim = { target: 100_000_000, years: 10, monthly: null, returnRate: null };
export const fc = { years: 20, extraSave: 0 };

export function render(tab = 'list') {
  if (tab === 'sim') return simTab();
  if (tab === 'forecast') return forecastTab();
  return listTab();
}

/* ================= 내 목표 ================= */
export const PRESETS = [
  { key: 'emergency', emoji: '🧯', name: '비상금', desc: '생활비 6개월치', months: 18, priority: 1,
    amount: (s, m) => Math.max(3_000_000, Math.round((m.projected || 1_500_000) * n(s.profile.emergencyMonths))) },
  { key: 'debtfree', emoji: '🏔️', name: '부채 완전상환', desc: '모든 빚 청산', months: 36, priority: 1,
    amount: (s) => totals(s).debts, hideIf: (s) => totals(s).debts <= 0 },
  { key: 'first100', emoji: '💎', name: '순자산 1억', desc: '자산 형성의 분기점', months: 60, priority: 2,
    amount: () => 100_000_000, hideIf: (s) => totals(s).net >= 100_000_000 },
  { key: 'house', emoji: '🏠', name: '주택자금', desc: '내 집 마련 종잣돈', months: 84, priority: 2,
    amount: () => 200_000_000 },
  { key: 'fi', emoji: '🏝️', name: '경제적 자유', desc: '연 소비의 25배', months: 240, priority: 3,
    amount: (s, m) => Math.max(300_000_000, Math.round((m.annualSpend || 24_000_000) * 25)) },
];

function listTab() {
  const s = state;
  const m = metrics(s);
  const { rows, budget, totalRequired, surplus } = allocateGoals(s);

  if (!s.goals.length) {
    return `
      <section class="card">
        <div class="card__hd"><h3>🎯 기본 목표로 시작하기</h3></div>
        <p class="hint" style="margin-bottom:14px">
          목표가 있어야 <b style="color:var(--ink)">맞춤 한도</b>가 계산됩니다.
          내 상황에 맞춰 금액이 자동 계산된 기본 목표를 골라보세요.
        </p>
        <div class="list">${PRESETS.filter((p) => !p.hideIf?.(s)).map((p) => `
          <div class="item">
            <div class="item__ico">${p.emoji}</div>
            <div class="item__main"><b>${p.name}</b><span>${p.desc} · 목표 ${compact(p.amount(s, m))}</span></div>
            <button class="btn btn--sm" data-act="add-preset" data-key="${p.key}">추가</button>
          </div>`).join('')}</div>
        <div class="btn-row" style="margin-top:14px">
          <button class="btn btn--primary btn--block" data-act="add-all-presets">추천 목표 한 번에 만들기</button>
        </div>
      </section>
      ${card('직접 만들기', empty('🎯', '금액과 기한을 정해 나만의 목표를 만들 수 있습니다.',
        `<button class="btn btn--primary btn--sm" data-act="add-goal">＋ 목표 추가</button>`))}`;
  }

  return `
    <section class="card">
      <div class="card__hd"><h3>저축여력 배분</h3><span class="sub">월 ${won(budget)}</span></div>
      <div class="stats stats--3">
        <div class="stat"><span class="lbl">월 저축여력</span><div class="v num ${budget <= 0 ? 'neg' : 'pos'}">${compact(budget)}</div></div>
        <div class="stat"><span class="lbl">목표 필요액</span><div class="v num">${compact(totalRequired)}</div></div>
        <div class="stat"><span class="lbl">${surplus >= 0 ? '여유' : '부족'}</span>
          <div class="v num ${surplus >= 0 ? 'pos' : 'neg'}">${compact(Math.abs(surplus))}</div></div>
      </div>
      ${totalRequired > 0 ? `<div style="margin-top:12px">
        ${progress(budget > 0 ? (totalRequired / budget) * 100 : 100, { tone: surplus >= 0 ? 'pos' : 'neg', height: 10 })}
        <p class="hint" style="margin-top:6px">${surplus >= 0
          ? `모든 목표를 기한 내 달성할 수 있습니다. 남는 ${won(surplus)}은 목표를 추가하거나 투자에 더 넣으세요.`
          : `월 ${won(-surplus)}이 부족합니다. 우선순위 순으로 배분했고, 낮은 순위 목표는 기한이 밀립니다.`}</p>
      </div>` : ''}
    </section>

    <div class="card__hd" style="margin:4px 2px 8px">
      <h3 style="font-size:13px;color:var(--ink3)">목표 ${rows.length}개</h3>
      <button class="btn btn--sm btn--primary" data-act="add-goal">＋ 추가</button>
    </div>

    ${rows.map((r) => goalCard(r, s)).join('')}

    <section class="card card--flat">
      <p class="hint">배분 규칙: 저축여력이 충분하면 각 목표의 필요액을 그대로 배정하고,
      부족하면 <b style="color:var(--ink)">우선순위 × 마감 임박도</b>로 가중 배분합니다.</p>
    </section>`;
}

function goalCard(r, s) {
  const g = r.goal;
  const left = r.monthsLeft;
  const ret = n(s.profile.expectedReturn);
  const eta = r.etaMonths;
  const late = eta !== null && left > 0 ? eta - left : null;
  const tone = r.progress >= 100 ? 'pos' : r.gap > 1000 ? 'warn' : 'accent';
  const pri = ['', '최우선', '보통', '여유'][clamp(n(g.priority), 1, 3)];

  return `<section class="card">
    <div class="card__hd">
      <h3 style="display:flex;align-items:center;gap:8px">${g.emoji || '🎯'} ${esc(g.name || '목표')}</h3>
      <div class="btn-row">
        <span class="chip chip--${n(g.priority) === 1 ? 'accent' : ''}">${pri}</span>
        <button class="btn btn--sm btn--ghost" data-act="edit-goal" data-id="${g.id}">수정</button>
      </div>
    </div>
    <div class="row" style="margin-bottom:8px">
      <span class="mid num">${compact(g.saved)}</span>
      <span class="lbl">/ ${compact(g.target)} · ${pct(r.progress, 0)}</span>
    </div>
    ${progress(r.progress, { tone, height: 10 })}
    <div class="stats stats--3" style="margin-top:14px">
      <div class="stat"><span class="lbl">필요 월 저축</span><div class="v num">${compact(r.required)}</div>
        <div class="s">${left > 0 ? `${Math.round(left)}개월 남음` : '기한 없음'}</div></div>
      <div class="stat"><span class="lbl">배분액</span>
        <div class="v num ${r.gap > 1000 ? 'warn' : 'pos'}">${compact(r.allocated)}</div>
        <div class="s">${r.gap > 1000 ? `${compact(r.gap)} 부족` : '충족'}</div></div>
      <div class="stat"><span class="lbl">예상 달성</span>
        <div class="v num ${late !== null && late > 1 ? 'warn' : ''}">${eta === null ? '—' : fmtMonths(eta)}</div>
        <div class="s">${late === null ? '' : late > 1 ? `기한 ${fmtMonths(late)} 초과` : '기한 내'}</div></div>
    </div>
    ${r.gap > 1000 ? `<div class="alert alert--warn" style="margin-top:12px">
      <span class="alert__ico">💡</span><div><b>기한을 맞추려면</b>
      <p>월 ${won(r.gap)}을 더 넣거나, 목표일을 ${eta !== null ? fmtMonths(Math.max(0, eta - left)) : ''} 미루거나,
      목표액을 ${compact(Math.max(0, n(g.target) - futureValue(n(g.saved), r.allocated, left, ret)))} 낮추면 됩니다.</p></div></div>` : ''}
    <div class="btn-row" style="margin-top:12px">
      <button class="btn btn--sm" data-act="add-to-goal" data-id="${g.id}">＋ 적립</button>
      <button class="btn btn--sm btn--ghost" data-act="sim-goal" data-id="${g.id}">시뮬레이션</button>
      <button class="btn btn--sm btn--ghost btn--danger" data-act="del-goal" data-id="${g.id}">삭제</button>
    </div>
  </section>`;
}

/* ================= 목표자산 시뮬레이션 ================= */
/** 월 저축액 슬라이더의 상한. 목표·기간·수익률이 바뀌면 함께 움직인다. */
const simMonthlyMax = (need) => Math.max(3_000_000, Math.round(need * 2 / 100000) * 100000);

/** 시뮬레이션 탭의 파생값. 최초 렌더와 드래그 중 부분 갱신이 같은 값을 쓴다. */
function simData() {
  const s = state;
  const m = metrics(s);
  const t = totals(s);
  // 기본값을 설정의 위험성향(투자자산 가정)으로 두면, 현금만 가진 사용자에게
  // 이 탭은 연 6% 를, 옆 탭(미래 예측)은 연 0% 를 보여준다. 출발점은 실제 포트폴리오다.
  const ret = sim.returnRate === null ? weightedReturn(s) : sim.returnRate;
  const monthsN = Math.round(sim.years * 12);
  const pv = t.net;
  const need = requiredSaving(sim.target, pv, monthsN, ret);
  const monthly = sim.monthly === null ? Math.max(0, m.capacity) : sim.monthly;
  const eta = monthsToTarget(sim.target, pv, monthly, ret);
  const fvAtPlan = futureValue(pv, monthly, monthsN, ret);
  const gapSave = need - monthly;

  const path = [];
  const pathNeed = [];
  for (let i = 0; i <= monthsN; i += Math.max(1, Math.round(monthsN / 60))) {
    path.push(futureValue(pv, monthly, i, ret));
    pathNeed.push(futureValue(pv, need, i, ret));
  }
  const labels = path.map((_, i) => {
    const mo = Math.round((i * monthsN) / Math.max(1, path.length - 1));
    return mo % 12 === 0 ? `${mo / 12}년` : '';
  });

  const principal = monthly * monthsN;
  const interest = Math.max(0, fvAtPlan - pv - principal);

  return { s, m, ret, monthsN, pv, need, monthly, eta, fvAtPlan, gapSave,
    path, pathNeed, labels, principal, interest };
}

/* 슬라이더가 든 카드는 드래그 중에 다시 그릴 수 없으므로
   값이 바뀌는 부분만 sim-* id 로 떼어 두고 liveSim() 이 갈아끼운다. */
function simTab() {
  const d = simData();
  const { s, m, ret, pv, need, monthly } = d;

  return `
    <section class="card">
      <div class="card__hd"><h3>🎯 목표자산 시뮬레이션</h3>
        <span class="sub">현재 순자산 ${compact(pv)}</span></div>

      <div class="field">
        <label>목표 금액 <b class="num" style="color:var(--accent);float:right" id="sim-v-target">${compact(sim.target)}</b></label>
        <input class="range" type="range" min="10000000" max="3000000000" step="10000000"
          value="${sim.target}" data-sim="target">
        <div class="btn-row" style="margin-top:8px" id="sim-presets">${simPresets()}</div>
      </div>

      <div class="field">
        <label>목표 기간 <b class="num" style="color:var(--accent);float:right" id="sim-v-years">${sim.years}년</b></label>
        <input class="range" type="range" min="1" max="40" step="1" value="${sim.years}" data-sim="years">
      </div>

      <div class="field">
        <label>연 기대수익률 <b class="num" style="color:var(--accent);float:right" id="sim-v-ret">${(ret * 100).toFixed(1)}%</b></label>
        <input class="range" type="range" min="0" max="0.15" step="0.005" value="${ret}" data-sim="returnRate">
        <div class="help">기본값은 지금 보유한 자산의 가중 기대수익 ${(weightedReturn(s) * 100).toFixed(1)}%입니다.
          설정의 위험성향(${s.profile.riskProfile === 'conservative' ? '안정형' : s.profile.riskProfile === 'aggressive' ? '공격형' : '균형형'}) 기본값 ${(n(s.profile.expectedReturn) * 100).toFixed(1)}%는 투자자산에만 적용됩니다.</div>
      </div>

      <div class="field">
        <label>월 저축액 <b class="num" style="color:var(--accent);float:right" id="sim-v-monthly">${won(monthly)}</b></label>
        <input class="range" type="range" min="0" max="${simMonthlyMax(need)}"
          step="50000" value="${clamp(monthly, 0, simMonthlyMax(need))}" data-sim="monthly">
        <div class="help" id="sim-monthly-help">${simMonthlyHelp(d)}</div>
      </div>
    </section>

    <div id="sim-out">${simOut(d)}</div>`;
}

/** 목표 금액 프리셋 버튼 — 선택 상태가 슬라이더를 따라 바뀐다 */
function simPresets() {
  return [50_000_000, 100_000_000, 300_000_000, 500_000_000, 1_000_000_000]
    .map((v) => `<button class="btn btn--sm ${sim.target === v ? 'btn--primary' : ''}" data-sim-set="target" data-v="${v}">${compact(v)}</button>`).join('');
}

/** 월 저축액 슬라이더 아래 도움말 — '필요액으로 맞추기' 값이 목표를 따라 바뀐다 */
function simMonthlyHelp(d) {
  const { m, need } = d;
  return `현재 저축여력 ${won(Math.max(0, m.capacity))}
          <button class="btn btn--sm btn--ghost" data-sim-set="monthly" data-v="${Math.max(0, Math.round(m.capacity))}" style="margin-left:6px">여력으로 맞추기</button>
          <button class="btn btn--sm btn--ghost" data-sim-set="monthly" data-v="${Math.round(need)}">필요액으로 맞추기</button>`;
}

/** 슬라이더 바깥의 결과 카드들 */
function simOut(d) {
  const { pv, need, monthly, eta, fvAtPlan, gapSave, path, pathNeed, labels, principal, interest } = d;
  return `

    <section class="card">
      <div class="card__hd"><h3>결과</h3></div>
      <div class="stats">
        <div class="stat"><span class="lbl">${sim.years}년 뒤 필요한 월 저축</span>
          <div class="v num" style="color:var(--accent)">${won(need)}</div>
          <div class="s ${gapSave > 0 ? 'neg' : 'pos'}">${gapSave > 0 ? `현재보다 ${won(gapSave)} 더` : `현재로 충분 (+${won(-gapSave)})`}</div></div>
        <div class="stat"><span class="lbl">현재 저축액으로 달성 시점</span>
          <div class="v num">${eta === null ? '도달 불가' : fmtMonths(eta)}</div>
          <div class="s">${eta === null ? '수익률 또는 저축액을 올려야 합니다' : `약 ${(eta / 12).toFixed(1)}년 후`}</div></div>
        <div class="stat"><span class="lbl">${sim.years}년 뒤 예상 자산</span>
          <div class="v num ${fvAtPlan >= sim.target ? 'pos' : ''}">${compact(fvAtPlan)}</div>
          <div class="s">목표의 ${pct((fvAtPlan / Math.max(1, sim.target)) * 100, 0)}</div></div>
        <div class="stat"><span class="lbl">복리 수익분</span>
          <div class="v num pos">${compact(interest)}</div>
          <div class="s">원금 ${compact(pv + principal)}</div></div>
      </div>
    </section>

    <section class="card">
      <div class="card__hd"><h3>자산 성장 경로</h3><span class="sub">${sim.years}년</span></div>
      ${lineChart([
        { data: pathNeed, color: 'var(--ink3)', dash: '5 4', dot: false, width: 1.6 },
        { data: path, color: 'var(--accent)', fill: true, dot: false },
      ], { height: 190, labels })}
      <div class="legend">
        <span><i style="background:var(--accent)"></i>월 ${won(monthly)} 저축 시</span>
        <span><i style="background:var(--ink3)"></i>목표 달성 필요 경로</span>
      </div>
      <div class="divider"></div>
      <div class="kv"><span>목표 금액</span><b class="num">${won(sim.target)}</b></div>
      <div class="kv"><span>현재 순자산</span><b class="num">${won(pv)}</b></div>
      <div class="kv"><span>${sim.years}년간 총 저축 원금</span><b class="num">${won(principal)}</b></div>
      <div class="kv"><span>복리로 불어난 금액</span><b class="num pos">${won(interest)}</b></div>
      <div class="btn-row" style="margin-top:14px">
        <button class="btn btn--primary btn--block" data-act="sim-to-goal">이 시뮬레이션을 목표로 저장</button>
      </div>
    </section>`;
}

/* ---------- 드래그 중 부분 갱신 ----------
   `except` 는 지금 잡고 있는 슬라이더다. 그 노드의 속성은 건드리면 안 된다. */
export function liveSim(except) {
  const d = simData();
  setText('sim-v-target', compact(sim.target));
  setText('sim-v-years', `${sim.years}년`);
  setText('sim-v-ret', `${(d.ret * 100).toFixed(1)}%`);
  setText('sim-v-monthly', won(d.monthly));
  setHTML('sim-presets', simPresets());
  setHTML('sim-monthly-help', simMonthlyHelp(d));
  setAttr('[data-sim="monthly"]', 'max', simMonthlyMax(d.need), except);
  setHTML('sim-out', simOut(d));
}

/* ================= 미래 자산 예측 ================= */
/** 미래 예측 탭의 파생값. 최초 렌더와 드래그 중 부분 갱신이 같은 값을 쓴다. */
function fcData() {
  const s = state;
  const m = metrics(s);
  const monthsN = fc.years * 12;
  const base = project(s, monthsN, { scenario: 'base', spendDelta: fc.extraSave });
  const bad = project(s, monthsN, { scenario: 'bad', spendDelta: fc.extraSave });
  const good = project(s, monthsN, { scenario: 'good', spendDelta: fc.extraSave });

  const stepN = Math.max(1, Math.round(monthsN / 60));
  const pick = (arr) => arr.filter((_, i) => i % stepN === 0 || i === arr.length - 1);
  const netBase = pick(base.series).map((x) => x.net);
  const netBad = pick(bad.series).map((x) => x.net);
  const netGood = pick(good.series).map((x) => x.net);
  const labels = pick(base.series).map((x, i, a) => {
    const yr = Math.round(((i / Math.max(1, a.length - 1)) * monthsN) / 12);
    return `${yr}년`;
  });

  const milestones = [100_000_000, 300_000_000, 500_000_000, 1_000_000_000, Math.round(m.annualSpend * 25)]
    .filter((v, i, a) => v > m.net && v > 0 && a.indexOf(v) === i)
    .sort((a, b) => a - b)
    .slice(0, 5)
    .map((v) => {
      const hit = base.series.find((x) => x.net >= v);
      return { amount: v, months: hit ? hit.i : null, isFI: Math.abs(v - m.annualSpend * 25) < 1 };
    });

  const debtFree = base.debt.months;
  const end = base.series[base.series.length - 1];

  return { s, m, monthsN, base, stepN, netBase, netBad, netGood, labels, milestones, debtFree, end };
}

/* 슬라이더가 든 카드는 드래그 중에 다시 그릴 수 없으므로
   값이 바뀌는 부분만 fc-* id 로 떼어 두고 liveFc() 가 갈아끼운다. */
function forecastTab() {
  const d = fcData();

  return `
    <section class="card">
      <div class="card__hd"><h3>🔮 미래 자산 예측</h3>
        <span class="sub" id="fc-sub">${fc.years}년 후</span></div>
      <div class="row" style="align-items:flex-start;gap:12px;flex-wrap:wrap" id="fc-head">${fcHead(d)}</div>

      <div class="field" style="margin-top:16px">
        <label>예측 기간 <b class="num" style="color:var(--accent);float:right" id="fc-v-years">${fc.years}년</b></label>
        <input class="range" type="range" min="1" max="40" step="1" value="${fc.years}" data-fc="years">
      </div>
      <div class="field" style="margin-bottom:4px">
        <label>월 저축 추가 <b class="num" style="color:var(--accent);float:right" id="fc-v-extra">${won(fc.extraSave)}</b></label>
        <input class="range" type="range" min="0" max="2000000" step="50000" value="${clamp(fc.extraSave, 0, 2000000)}" data-fc="extraSave">
        <div class="help" id="fc-help">${fcHelp(d)}</div>
      </div>
    </section>

    <div id="fc-out">${fcOut(d)}</div>`;
}

/** 슬라이더가 든 카드 안쪽의 요약 (예상 순자산 · 시나리오 범위) */
function fcHead(d) {
  const { m, netBad, netGood, end } = d;
  return `
        <div style="flex:1;min-width:240px">
          <span class="lbl">${fc.years}년 뒤 예상 순자산</span>
          <div class="big num pos">${compact(end?.net ?? 0)}</div>
          <span class="hint">현재 ${compact(m.net)} → ${m.net > 0 ? `${((end?.net ?? 0) / m.net).toFixed(1)}배` : ''}</span>
        </div>
        <div style="flex:1;min-width:240px">
          <div class="stats">
            <div class="stat"><span class="lbl">비관 시나리오</span><div class="v num">${compact(netBad[netBad.length - 1] ?? 0)}</div></div>
            <div class="stat"><span class="lbl">낙관 시나리오</span><div class="v num pos">${compact(netGood[netGood.length - 1] ?? 0)}</div></div>
          </div>
        </div>`;
}

/** 저축 추가 슬라이더 아래 도움말 */
function fcHelp(d) {
  const { s, monthsN, end } = d;
  return `지출을 줄여 저축을 늘렸을 때의 효과를 바로 확인할 수 있습니다.
          ${fc.extraSave > 0 ? `<b class="pos">현재 설정으로 ${fc.years}년 뒤 ${compact((end?.net ?? 0) - (project(s, monthsN, { scenario: 'base' }).series.at(-1)?.net ?? 0))} 증가</b>` : ''}`;
}

/** 슬라이더 바깥의 예측 카드들 */
function fcOut(d) {
  const { s, m, monthsN, base, stepN, netBase, netBad, netGood, labels, milestones, debtFree } = d;
  return `

    <section class="card">
      <div class="card__hd"><h3>순자산 예측 경로</h3><span class="sub">비관 ~ 낙관 범위</span></div>
      ${lineChart([{ data: netBase, color: 'var(--accent)', dot: false }], {
        height: 200, labels, band: { lo: netBad, hi: netGood },
        markers: debtFree && debtFree <= monthsN ? [{ at: Math.round(debtFree / stepN), label: '부채완제' }] : [],
      })}
      <div class="legend">
        <span><i style="background:var(--accent)"></i>기본 (자산 가중 연 ${(weightedReturn(s) * 100).toFixed(1)}%)</span>
        <span><i style="background:var(--accent);opacity:.3"></i>시나리오 범위</span>
        ${debtFree ? `<span><i style="background:var(--warn)"></i>부채 완제 ${fmtMonths(debtFree)} 후</span>` : ''}
      </div>
      <p class="hint" style="margin-top:10px">
        월 저축 ${won(base.monthlySave)}${debtFree ? `, 부채 완제 후에는 상환액 ${won(m.debtPay)}이 저축으로 전환되어 속도가 빨라집니다` : ''}.
        자산별 기대수익률을 각각 적용해 월 단위로 계산했습니다.
      </p>
    </section>

    <section class="card">
      <div class="card__hd"><h3>🏁 마일스톤 도달 시점</h3></div>
      ${milestones.length ? `<div class="list">${milestones.map((ms) => `
        <div class="item">
          <div class="item__ico">${ms.isFI ? '🏝️' : '💎'}</div>
          <div class="item__main"><b>${ms.isFI ? '경제적 자유' : `순자산 ${compact(ms.amount)}`}</b>
            <span>${ms.isFI ? `연 소비 ${compact(m.annualSpend)}의 25배` : `현재보다 ${compact(ms.amount - m.net)} 더`}</span></div>
          <div class="item__val num ${ms.months ? '' : 'muted'}">${ms.months ? fmtMonths(ms.months) : `${fc.years}년 내 미도달`}
            <small>${ms.months ? new Date(new Date().setMonth(new Date().getMonth() + ms.months)).getFullYear() + '년경' : '기간 연장 필요'}</small></div>
        </div>`).join('')}</div>`
        : `<p class="hint">이미 주요 마일스톤을 넘었습니다. 목표를 새로 설정해 보세요.</p>`}
    </section>

    ${m.capacity < 0 ? `<div class="alert alert--danger">
      <span class="alert__ico">🔥</span><div><b>현재 저축여력이 마이너스입니다</b>
      <p>예측은 매달 ${won(-m.capacity)}씩 자산을 헐어 쓰는 것으로 계산됩니다. 지출 구조를 먼저 바꿔야 합니다.</p></div></div>` : ''}`;
}

/* ---------- 드래그 중 부분 갱신 ---------- */
export function liveFc() {
  const d = fcData();
  setText('fc-sub', `${fc.years}년 후`);
  setText('fc-v-years', `${fc.years}년`);
  setText('fc-v-extra', won(fc.extraSave));
  setHTML('fc-head', fcHead(d));
  setHTML('fc-help', fcHelp(d));
  setHTML('fc-out', fcOut(d));
}
