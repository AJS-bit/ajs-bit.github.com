/* 홈 — 목표까지 남은 거리(히어로) · 소비율 조절 · 핵심 요약
   상세 지표는 자산/지출/목표 탭으로 넘기고 홈은 의도적으로 단순하게 유지한다. */
import { state, commit } from '../store.js';
import { metrics, spendingLimit, allocateGoals, futureValue, monthsToTarget, totals, warnings } from '../finance.js';
import {
  compact, won, pct, pctSigned, months as fmtMonths, n, clamp,
} from '../format.js';
import { ring, spark, gauge, progress, esc } from '../charts.js';
import { setHTML, setText, WARN_ACTION } from '../ui.js';

export const title = '홈';

/* 홈에 띄울 목표 고르기 — 사용자가 고른 것 우선, 없으면 우선순위·마감 순 */
function featured(rows) {
  if (!rows.length) return null;
  const picked = rows.find((r) => r.goal.id === state.settings.homeGoal);
  return picked || rows[0];
}

export function render() {
  const s = state;
  const t = totals(s);
  const hasAny = s.assets.length || s.debts.length || s.transactions.length;
  if (!hasAny) return onboarding();

  const m = metrics(s);
  const lim = spendingLimit(s);
  const alloc = allocateGoals(s);
  const fg = featured(alloc.rows);

  return `
    ${fg ? goalHero(fg, alloc, m) : goalEmpty()}
    ${alertCard()}
    ${burnCard(m, s)}
    ${summary(m, t)}
    ${todayCard(m, lim, s)}
    <button class="fab" data-act="quick-add" aria-label="지출 입력">＋</button>
  `;
}

/* ================= 지금 조치할 일 =================
   경고가 상단 벨 배지 뒤에만 있어서 홈에서는 보이지 않았다. 숫자는 가득한데
   "지금 뭘 해야 하나"에 답하는 자리가 없었던 것이다.
   가장 급한 한 건만 꺼내 놓고 나머지는 기존 알림 모달로 넘긴다.
   급한 경고(danger/warn)가 없으면 아무것도 그리지 않아 홈이 길어지지 않는다.
   info/good 까지 세면 배지가 늘 켜져 신호가 죽으므로 배지와 같은 기준을 쓴다. */
function alertCard() {
  const ws = warnings(state).filter((w) => w.level === 'danger' || w.level === 'warn');
  if (!ws.length) return '';
  const top = ws[0];
  return `<div class="alert alert--${top.level}" style="margin-bottom:14px">
    <span class="alert__ico">${top.icon}</span>
    <div style="flex:1;min-width:0">
      <b>${esc(top.title)}</b>
      <p>${esc(top.body)}</p>
      ${top.route || ws.length > 1 ? `<div class="btn-row" style="margin-top:9px">
        ${top.route ? `<button class="btn btn--sm" data-nav="${top.route}">${esc(WARN_ACTION[top.route] || '보러 가기')}</button>` : ''}
        ${ws.length > 1 ? `<button class="btn btn--sm btn--ghost" data-act="all-warnings">나머지 ${ws.length - 1}건</button>` : ''}
      </div>` : ''}
    </div>
  </div>`;
}

/* ================= 1. 목표 히어로 ================= */
function goalHero(r, alloc, m) {
  const g = r.goal;
  const ret = n(state.profile.expectedReturn);
  const eta = r.etaMonths;
  const left = r.monthsLeft;
  const late = eta !== null && left > 0 ? eta - left : null;
  const onTrack = late === null ? null : late <= 1;
  const prog = r.progress;

  // 적립 경로: 지금부터 목표 도달(또는 기한)까지 월별 예상 잔액
  const span = Math.max(6, Math.min(600, Math.round(Math.max(eta ?? 0, left) * 1.05)));
  const step = Math.max(1, Math.round(span / 40));
  const path = [];
  for (let i = 0; i <= span; i += step) path.push(futureValue(n(g.saved), r.allocated, i, ret));
  const deadlineIdx = left > 0 && left <= span ? Math.round(left / step) : null;

  const tone = prog >= 100 ? 'pos' : onTrack === false ? 'warn' : 'accent';
  const centerMid = prog >= 100 ? '달성' : eta === null ? '—' : fmtMonths(eta);

  return `
    <section class="hero">
      <div class="hero__top">
        <div class="hero__name">${g.emoji || '🎯'} <span>${esc(g.name || '목표')}</span></div>
        <button class="btn btn--sm btn--ghost" data-nav="goals">전체 목표</button>
      </div>

      ${alloc.rows.length > 1 ? `<div class="goal-pills">
        ${alloc.rows.map((x) => `<button data-act="pick-goal" data-id="${x.goal.id}"
          class="${x.goal.id === g.id ? 'is-on' : ''}">${x.goal.emoji || '🎯'} ${esc(x.goal.name || '목표')}</button>`).join('')}
      </div>` : ''}

      <div style="max-width:210px;margin:2px auto 0">
        ${ring({
          ratio: prog, size: 210, thickness: 15, tone,
          top: prog >= 100 ? '목표 달성' : '목표까지',
          mid: centerMid,
          bottom: prog >= 100 ? '' : `${pct(prog, 0)} 진행`,
        })}
      </div>

      ${path.length > 2 ? `<div style="margin:8px -2px 0">
        ${spark(path, {
          height: 68, color: `var(--${tone})`, target: n(g.target), markAt: deadlineIdx,
          markLabel: deadlineIdx !== null ? '목표일' : '', targetLabel: '목표 금액',
        })}
        <div class="row" style="margin-top:2px">
          <span class="hint">지금</span>
          <span class="hint">${g.targetDate ? `목표일 ${g.targetDate.slice(0, 7).replace('-', '.')}` : '기한 없음'}</span>
        </div>
      </div>` : ''}

      <div class="hero__foot">
        <div><span class="lbl">모은 금액</span><b>${compact(g.saved)}</b></div>
        <div><span class="lbl">목표 금액</span><b>${compact(g.target)}</b></div>
        <div><span class="lbl">월 저축</span>
          <b class="${r.gap > 1000 ? 'warn' : 'pos'}">${compact(r.allocated)}</b></div>
      </div>

      ${statusLine(r, late, onTrack, m)}
    </section>`;
}

function statusLine(r, late, onTrack, m) {
  if (r.progress >= 100) {
    return `<div class="alert alert--good" style="margin-top:12px">
      <span class="alert__ico">🎉</span><div><b>목표를 달성했습니다</b>
      <p>새 목표를 세우거나, 이 금액을 다음 단계로 옮길 시점입니다.</p></div></div>`;
  }
  if (r.gap > 1000) {
    return `<div class="alert alert--warn" style="margin-top:12px">
      <span class="alert__ico">⚠️</span><div><b>월 ${won(r.gap)}이 부족합니다</b>
      <p>기한을 맞추려면 월 ${won(r.required)}이 필요한데 지금 배분 가능액은 ${won(r.allocated)}입니다.
      지출을 ${won(r.gap)} 줄이거나 목표일을 미루면 맞습니다.</p></div></div>`;
  }
  if (onTrack === false) {
    return `<div class="alert alert--warn" style="margin-top:12px">
      <span class="alert__ico">⏳</span><div><b>기한보다 ${fmtMonths(late)} 늦어집니다</b>
      <p>현재 저축 페이스 기준입니다.</p></div></div>`;
  }
  return `<div class="alert alert--good" style="margin-top:12px">
    <span class="alert__ico">✅</span><div><b>순조롭게 가고 있습니다</b>
    <p>이 페이스를 유지하면 기한 내 달성합니다. 월 저축여력 ${won(Math.max(0, m.capacity))}.</p></div></div>`;
}

function goalEmpty() {
  return `<section class="hero" style="text-align:center">
    <div style="font-size:34px;margin-bottom:8px">🎯</div>
    <h2 style="font-size:17px;margin-bottom:7px">목표를 정하면 방향이 생깁니다</h2>
    <p class="hint" style="max-width:340px;margin:0 auto 16px">
      목표가 있어야 "이번 달 얼마까지 써도 되는지"를 역산할 수 있습니다.
      비상금·주택자금 같은 기본 목표를 상황에 맞춰 자동으로 만들어 드립니다.
    </p>
    <button class="btn btn--primary" data-nav="goals">목표 만들기</button>
  </section>`;
}

/* ================= 2. 소비율 (슬라이더 + 직접 입력) ================= */
/* ---------- 이번 달 소비 시나리오 ----------
   NAVI 에서 가져온 판단: **실제 값을 바꾸는 조작과 가상 시나리오를 구분한다.**
   예전 홈 슬라이더는 목표 소비율(%)을 조절하면서 state.profile.targetBurn 을
   실제로 저장했다. 둘러보다 실수로 목표가 바뀌었고, 코치 탭에도 같은 조작이
   있어 어디서 뭘 바꿨는지 알기 어려웠다.

   이제 홈 슬라이더는 **이번 달 소비액을 가정해보는 것**이고 아무것도 저장하지
   않는다. 목표 소비율을 실제로 바꾸는 곳은 설정과 코치·가정해보기 두 곳이다.

   단위도 바꿨다. 사람은 "%"가 아니라 "만원"으로 생각하고, 알고 싶은 것은
   상한이 아니라 "그래서 목표가 언제 되냐"다. */
let scenarioSpend = null;                 // null = 실제 월말 예상 그대로
let scenarioBase = null;                  // 가정을 세운 시점의 실제 예상

export function setScenarioSpend(v, baseline) { scenarioSpend = v; scenarioBase = baseline; }
export function resetScenario() { scenarioSpend = null; scenarioBase = null; }

/** 거래가 추가되는 등 실제 예상이 달라지면 가정을 자동으로 푼다.
    안 그러면 새 지출을 넣은 뒤에도 옛 가정이 남아 헷갈린다. */
function syncScenario(baseline) {
  if (scenarioBase !== null && Math.abs(scenarioBase - baseline) > 1) resetScenario();
  if (scenarioSpend !== null) scenarioBase = baseline;
}

const manwon = (v) => `${compact(v)}원`;

/** 시나리오 슬라이더의 범위. 실제 예상의 50~150% 를 5만원 단위로 잡는다. */
function scenarioRange(baseline) {
  const min = Math.max(0, Math.floor((baseline * 0.5) / 50000) * 50000);
  const max = Math.max(min + 100000, Math.ceil((baseline * 1.5) / 50000) * 50000);
  return { min, max };
}

/**
 * 아낀(또는 더 쓴) 금액이 대표 목표를 얼마나 앞당기는지.
 *
 * `allocateGoals(s, 조정된여력)` 으로 다시 배분하면 안 된다. 여력이 필요액 합계를
 * 넘는 순간 각 목표가 '필요액만' 받도록 설계돼 있어서, 가중 배분으로 더 받던
 * 최우선 목표의 몫이 오히려 줄어든다. 그러면 **덜 썼는데 목표가 늦어지는**
 * 화면이 나온다 (실제로 1년 3개월 → 1년 6개월로 보였다).
 * 배분 규칙은 엔진의 설계이므로 건드리지 않고, 여기서는 아낀 돈을 그 목표에
 * 그대로 더 넣었을 때로 환산한다. 단조롭고 해석이 분명하다.
 */
function goalShift(s, row, delta) {
  if (!row) return null;
  const ret = n(s.profile.expectedReturn);
  const now = row.etaMonths;
  const next = monthsToTarget(row.goal.target, row.goal.saved, Math.max(0, row.allocated + delta), ret);
  return { now, next, saved: now !== null && next !== null ? now - next : null };
}

function burnCard(m, s) {
  const target = n(s.profile.targetBurn);

  if (m.net <= 0) {
    return `<section class="card" style="border-color:var(--neg)">
      <div class="card__hd"><h3>🧭 소비율</h3><span class="chip chip--neg">순자산 마이너스</span></div>
      <p class="hint">부채가 자산보다 많아 소비율을 계산할 수 없습니다.
        지금은 <b style="color:var(--ink)">부채 상환 속도</b>가 진짜 지표입니다.</p>
      <div class="btn-row" style="margin-top:12px">
        <button class="btn btn--primary btn--sm" data-nav="debt">상환 전략 보기</button></div>
    </section>`;
  }

  const g = m.grade;
  const tone = g.tone === 'muted' ? 'accent' : g.tone;
  const chip = tone === 'pos' ? 'pos' : tone === 'neg' ? 'neg' : tone === 'warn' ? 'warn' : 'accent';
  const baseline = Math.max(0, m.projected);
  syncScenario(baseline);

  // 지출 기록이 없으면 조정할 대상 자체가 없다. 0원짜리 슬라이더를 띄우는 대신
  // 무엇을 하면 되는지 알려준다. (소비율도 이때 '측정 불가'로 나온다)
  if (baseline <= 0) {
    return `<section class="card">
      <div class="card__hd">
        <h3>🧭 소비율 <span class="sub">순자산 대비</span></h3>
        <span class="chip">측정 불가</span>
      </div>
      <div style="max-width:250px;margin:0 auto">${burnGauge(m, s, 'accent')}</div>
      <p class="hint" style="margin-top:12px">이번 달 지출을 기록하면 순자산 대비 소비율과
        이번 달 쓸 수 있는 금액을 계산합니다. 한 건만 넣어도 시작됩니다.</p>
      <div class="btn-row" style="margin-top:12px">
        <button class="btn btn--primary btn--sm" data-act="quick-add">지출 기록</button></div>
    </section>`;
  }

  const { min, max } = scenarioRange(baseline);
  const spend = scenarioSpend === null ? baseline : clamp(scenarioSpend, min, max);

  return `<section class="card">
    <div class="card__hd">
      <h3>🧭 소비율 <span class="sub">순자산 대비</span></h3>
      <span class="chip chip--${chip}">연 ${pct(m.burnAnnual)} · ${esc(g.label)}</span>
    </div>

    <div style="max-width:250px;margin:0 auto" id="burn-gauge">${burnGauge(m, s, tone)}</div>

    <!-- 등급(4% 룰 절대 기준)과 목표선(내가 정한 상대 기준)은 다른 자다.
         같은 26.3% 를 홈은 '양호', 지출·벨은 '목표선 초과'라 불러 앱이
         오락가락해 보였다. 두 기준이 다르다는 것을 여기서 밝힌다. -->
    <p class="hint" style="text-align:center;margin-top:-2px">
      ${esc(g.label)}는 4% 룰 기준 등급입니다 ·
      내 목표선 연 ${pct(target * 12, 1)}${m.burnAnnual > target * 12
        ? `<span class="neg"> 초과</span>` : `<span class="pos"> 이내</span>`}
    </p>

    <div class="divider"></div>

    <div class="field" style="margin:0">
      <label style="display:flex;justify-content:space-between;align-items:baseline">
        <span>이번 달 소비를 조정해보면</span>
        <b class="num" style="font-size:19px;color:var(--accent)" id="burn-spend">${manwon(spend)}</b>
      </label>
      <input class="range" type="range" min="${min}" max="${max}" step="50000"
        value="${spend}" data-scenario="spend" aria-label="이번 달 소비 시나리오">
      <div class="row" style="margin-top:4px">
        <span class="hint">${manwon(min)}</span>
        <button class="btn btn--sm btn--ghost" data-act="scenario-reset" id="burn-reset"
          ${scenarioSpend === null ? 'disabled' : ''}>현재 예상으로</button>
        <span class="hint">${manwon(max)}</span>
      </div>
      <div class="help" id="burn-basis">${scenarioBasis(baseline, spend)}</div>
    </div>

    <div id="burn-out">${burnOut(m, s, target, spend)}</div>
  </section>`;
}

/** 슬라이더 아래 한 줄 — 지금 보고 있는 것이 실제인지 가정인지 밝힌다 */
function scenarioBasis(baseline, spend) {
  const d = baseline - spend;
  if (Math.abs(d) < 1) return `월말 예상 소비입니다. 끌어서 가정해 보세요.`;
  return `실제 예상에서 <b class="${d > 0 ? 'pos' : 'neg'}">${d > 0 ? '−' : '+'}${manwon(Math.abs(d))}</b> 가정 · 저장되지 않습니다.`;
}

/** 시나리오에 따라 바뀌는 결과. 슬라이더 바깥이라 통째로 갈아끼운다. */
function burnOut(m, s, target, spend) {
  const baseline = Math.max(0, m.projected);
  const delta = baseline - spend;                     // 아낀 금액 (음수면 더 쓴 것)
  const capacity = m.income - spend - m.debtPay;
  const cap = (m.net * target) / 100;
  const diff = spend - cap;
  const row = featured(allocateGoals(s).rows);
  const shift = goalShift(s, row, delta);
  const shiftText = !shift || shift.next === null ? '도달 불가'
    : `${fmtMonths(Math.round(shift.next))} 후`;
  const shiftSub = !shift || shift.saved === null || Math.abs(shift.saved) < 0.05 ? ''
    : `<small class="${shift.saved > 0 ? 'pos' : 'neg'}">${Math.abs(shift.saved).toFixed(1)}개월 ${shift.saved > 0 ? '단축' : '지연'}</small>`;

  return `
    <div class="divider"></div>
    <div class="kv"><span>월 저축여력</span>
      <b class="num ${capacity < 0 ? 'neg' : 'pos'}">${won(capacity)}</b></div>
    ${row ? `<div class="kv"><span>${esc(row.goal.name || '목표')} 달성</span>
      <b class="num">${shiftText} ${shiftSub}</b></div>` : ''}
    <div class="kv"><span>목표 상한(월 ${target.toFixed(1)}%)과의 차이</span>
      <b class="num ${diff > 0 ? 'neg' : 'pos'}">${diff > 0 ? '+' : ''}${won(diff)}</b></div>
    <p class="hint" style="margin-top:8px">상한 ${won(cap)} · 목표 소비율은 설정에서 바꿉니다.</p>`;
}

/* 게이지 눈금은 **목표와 무관하게 고정**한다.
   예전에는 max 가 목표×3 이라, 목표 슬라이더를 끌면 분모만 커져서
   가운데 숫자는 그대로인데 호만 줄어들었다. 오른쪽으로 끌수록 호가 짧아지니
   방향이 거꾸로 느껴졌고(목표 0.7%→8% 에서 호가 100%→9.3%), 눈금자가 매번
   다시 그려지니 어제와 오늘을 비교할 수도 없었다.
   이제 바늘은 소비율, 눈금은 목표 위치다. 역할이 나뉜다.

   바늘은 **시나리오 소비율**을 가리킨다. 소비액 슬라이더를 왼쪽으로 끌면 호가
   짧아지고 목표 눈금 안으로 들어온다 — 방향이 직관과 맞는다.

   상한 월 6% = 연 72%. 완전자립(연 4%)부터 주의(연 100%) 직전까지 담기는 범위다. */
const BURN_GAUGE_MAX = 6;

function burnGauge(m, s, tone) {
  const target = n(s.profile.targetBurn);
  const baseline = Math.max(0, m.projected);
  const spend = scenarioSpend === null ? baseline : scenarioSpend;
  const burn = m.net > 0 && baseline > 0 ? (spend / m.net) * 100 : null;
  return gauge({
    value: burn, max: BURN_GAUGE_MAX,
    label: burn === null ? '—' : `${burn.toFixed(2)}%`,
    // 가운데 숫자는 '월' 기준인데 칩은 '연' 기준이라 26.3 과 2.19 의 관계를
    // 사용자가 암산해야 했다. 기준과 목표값을 숫자 바로 아래에 붙인다.
    // (눈금 라벨로 넣으면 호가 그 위를 지나가며 가린다)
    sub: `${scenarioSpend === null ? '이번 달 예상' : '가정한 소비'} · 목표 ${target.toFixed(1)}%`,
    tone, ticks: [{ at: target, tone: 'accent', label: '목표' }],
  });
}

/* ---------- 드래그 중 부분 갱신 ----------
   홈은 슬라이더와 출력이 한 카드에 섞여 있어 카드째 다시 그릴 수 없다.
   그래서 값이 바뀌는 자리를 하나씩 짚어 갱신한다. 게이지가 여기서 빠져 있어
   드래그 중에는 숫자만 움직이고 게이지는 놓아야 따라오던 문제가 있었다. */
export function liveBurn() {
  const s = state;
  const m = metrics(s);
  const main = document.getElementById('main');
  if (!main || !main.querySelector('[data-scenario="spend"]')) return;   // 홈이 아닌 화면

  const baseline = Math.max(0, m.projected);
  if (scenarioSpend !== null) scenarioBase = baseline;
  const { min, max } = scenarioRange(baseline);
  const spend = scenarioSpend === null ? baseline : clamp(scenarioSpend, min, max);

  setText('burn-spend', manwon(spend));
  setHTML('burn-basis', scenarioBasis(baseline, spend));
  setHTML('burn-gauge', burnGauge(m, s, gaugeTone(m)));
  setHTML('burn-out', burnOut(m, s, n(s.profile.targetBurn), spend));
  const reset = document.getElementById('burn-reset');
  if (reset) reset.disabled = scenarioSpend === null;
}

const gaugeTone = (m) => (m.grade.tone === 'muted' ? 'accent' : m.grade.tone);

/* ================= 3. 요약 3칸 ================= */
function summary(m, t) {
  const ch = m.netMoM;
  const ir = m.incomeRatioProjected;
  const sc = m.score;
  return `<div class="summary">
    <button data-nav="assets">
      <span class="lbl">순자산</span>
      <span class="v ${m.net < 0 ? 'neg' : ''}">${compact(m.net)}</span>
      <span class="s">${ch && ch.abs !== null
        ? `${ch.abs >= 0 ? '▲' : '▼'} ${compact(Math.abs(ch.abs))} 전월비`
        : `자산 ${compact(t.assets)}`}</span>
    </button>
    <button data-nav="spending">
      <span class="lbl">월급 대비</span>
      <span class="v ${ir === null ? '' : ir > 90 ? 'neg' : ir > 70 ? 'warn' : 'pos'}">${pct(ir, 0)}</span>
      <span class="s">${m.income > 0 ? `저축률 ${pct(m.savingsRate, 0)}` : '수입 미입력'}</span>
    </button>
    <button data-nav="coach">
      <span class="lbl">성장 점수</span>
      <span class="v">${sc.ready
        ? `${sc.total}<span style="font-size:11px;color:var(--ink3)">/100</span>`
        : '—'}</span>
      <span class="s">${sc.ready
        ? sc.tier.label
        : `${esc(sc.missing[0]?.need || '지출 기록')} 입력 후 계산`}</span>
    </button>
  </div>`;
}

/* ================= 4. 오늘 쓸 수 있는 돈 ================= */
function todayCard(m, lim, s) {
  if (!(lim.total > 0)) {
    return `<section class="card">
      <div class="card__hd"><h3>🎚️ 맞춤 한도</h3></div>
      <p class="hint">월 실수령액을 입력하면 목표 저축을 뺀 나머지를 이번 달 한도로 계산합니다.</p>
      <div class="btn-row" style="margin-top:12px">
        <button class="btn btn--primary btn--sm" data-act="settings">수입 입력</button></div>
    </section>`;
  }
  const ratio = lim.ratio ?? 0;
  const paceRatio = (lim.pace / lim.total) * 100;
  const leftDays = Math.max(0, m.days - m.done);
  const perDay = leftDays > 0 ? Math.max(0, lim.remain) / leftDays : 0;

  return `<section class="card">
    <div class="card__hd">
      <h3>🎚️ 이번 달 한도</h3>
      <button class="btn btn--sm btn--ghost" data-nav="spending">자세히</button>
    </div>
    <div class="row" style="align-items:flex-end;margin-bottom:9px">
      <div>
        <span class="lbl">${lim.remain >= 0 ? '남은 금액' : '초과'}</span>
        <div class="mid num ${lim.remain < 0 ? 'neg' : ''}">${won(Math.abs(lim.remain))}</div>
      </div>
      <span class="hint num">${won(m.spend)} / ${won(lim.total)}</span>
    </div>
    ${progress(ratio, { tone: ratio > 100 ? 'neg' : ratio > paceRatio ? 'warn' : 'pos', markAt: paceRatio, height: 10 })}
    <div class="row" style="margin-top:7px">
      <span class="hint">회색선 = 오늘(${m.done}일차) 적정선</span>
      <span class="hint">${leftDays > 0 ? `남은 ${leftDays}일 · 하루 ${won(perDay)}` : '월말'}</span>
    </div>
    <p class="hint" style="margin-top:7px">${limitBasis(m, lim, s)}</p>
  </section>`;
}

/* 한도 숫자만 던지면 "이 40만원은 어디서 나왔지" 가 된다. 근거는 지출·한도
   탭까지 가야 보였고, 자산만 넣은 사용자는 바로 위 카드가 '측정 불가'인데
   한도만 단정하는 화면을 본다. 어느 쪽 계산이 적용됐는지 여기서 밝힌다. */
function limitBasis(m, lim, s) {
  if (lim.basis === 'manual') return '직접 입력한 한도입니다.';
  if (lim.basis === 'income') return '실수령 + 부수입 − 목표 저축 − 부채 상환 기준입니다.';
  const line = `순자산 ${compact(m.net)} × 목표 소비율 ${pct(n(s.profile.targetBurn), 1)} 기준입니다.`;
  return m.income > 0 ? line : `${line} 월 실수령액을 넣으면 더 정확해집니다.`;
}

/* ================= 온보딩 ================= */
function onboarding() {
  return `
    <section class="hero" style="text-align:center">
      <div style="font-size:38px;margin-bottom:10px">🧭</div>
      <h2 style="font-size:19px;margin-bottom:8px">순자산 대비 소비율로 관리하세요</h2>
      <p class="hint" style="max-width:400px;margin:0 auto 18px">
        가계부는 "얼마 썼나"를 봅니다. 자산 나침반은 <b style="color:var(--ink)">"내 재산에 비해 얼마나 썼나"</b>를 봅니다.<br>
        같은 30만원도 순자산 1천만원인 사람과 3억인 사람에게 전혀 다른 의미이기 때문입니다.
      </p>
      <div class="btn-row" style="justify-content:center">
        <button class="btn btn--primary" data-act="add-asset">자산 추가하기</button>
        <button class="btn" data-act="load-demo">예시 데이터로 둘러보기</button>
      </div>
    </section>
    <section class="card">
      <div class="card__hd"><h3>이렇게 계산합니다</h3></div>
      <div class="stack">
        ${[
          ['🎯', '목표까지 남은 거리', '홈 맨 위에서 목표 달성까지 몇 개월 남았는지 한눈에 봅니다.'],
          ['🧭', '소비율', '월 소비 ÷ 순자산. 연환산 4% 이하면 자산 수익만으로 살 수 있는 구간입니다.'],
          ['🎚️', '맞춤 한도', '목표 달성에 필요한 저축을 먼저 떼고 남는 돈이 이번 달 한도입니다.'],
          ['🔮', '미래 자산 예측', '자산별 수익률·저축·부채상환을 월 단위로 굴려 순자산 경로를 그립니다.'],
        ].map(([e, t, d]) => `<div class="item" style="border:0;padding:8px 0">
          <div class="item__ico">${e}</div>
          <div class="item__main"><b>${t}</b><span style="white-space:normal;line-height:1.5">${d}</span></div>
        </div>`).join('')}
      </div>
    </section>`;
}
