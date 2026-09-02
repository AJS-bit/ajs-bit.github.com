/* 홈 — 목표까지 남은 거리(히어로) · 소비율 조절 · 핵심 요약
   상세 지표는 자산/지출/목표 탭으로 넘기고 홈은 의도적으로 단순하게 유지한다. */
import { state, commit } from '../store.js';
import { metrics, spendingLimit, allocateGoals, futureValue, totals } from '../finance.js';
import {
  compact, won, pct, pctSigned, months as fmtMonths, n, clamp,
} from '../format.js';
import { ring, spark, gauge, progress, esc } from '../charts.js';
import { setHTML, setText } from '../ui.js';

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
    ${burnCard(m, s, lim)}
    ${summary(m, t)}
    ${todayCard(m, lim)}
    <button class="fab" data-act="quick-add" aria-label="지출 입력">＋</button>
  `;
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
function burnCard(m, s, lim) {
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
  const cap = (m.net * target) / 100;
  const diff = m.projected - cap;

  return `<section class="card">
    <div class="card__hd">
      <h3>🧭 소비율 <span class="sub">순자산 대비</span></h3>
      <span class="chip chip--${chip}">연 ${pct(m.burnAnnual)} · ${esc(g.label)}</span>
    </div>

    <div style="max-width:250px;margin:0 auto" id="burn-gauge">${burnGauge(m, target, tone)}</div>

    <div class="field" style="margin:6px 0 0">
      <label style="display:flex;justify-content:space-between;align-items:center">
        <span>목표 월 소비율</span>
        <span class="hint" id="burn-annual">연 ${(target * 12).toFixed(1)}%</span>
      </label>
      <div class="tune">
        <input type="range" min="0.1" max="8" step="0.1" value="${clamp(target, 0.1, 8)}" data-burn="range" aria-label="목표 월 소비율">
        <div class="numbox">
          <input type="number" min="0.05" max="50" step="0.1" value="${target.toFixed(1)}" data-burn="num" aria-label="목표 월 소비율 직접 입력">
          <span>%</span>
        </div>
      </div>
    </div>

    <div class="divider"></div>
    <div class="kv"><span>목표 월 소비 상한</span><b class="num" id="burn-cap">${won(cap)}</b></div>
    <div class="kv"><span>이번 달 예상 (${compact(m.projected)})과의 차이</span>
      <b class="num ${diff > 0 ? 'neg' : 'pos'}" id="burn-diff">${diff > 0 ? '+' : ''}${won(diff)}</b></div>
  </section>`;
}

/* 게이지 눈금은 **목표와 무관하게 고정**한다.
   예전에는 max 가 목표×3 이라, 목표 슬라이더를 끌면 분모만 커져서
   가운데 숫자는 그대로인데 호만 줄어들었다. 오른쪽으로 끌수록 호가 짧아지니
   방향이 거꾸로 느껴졌고(목표 0.7%→8% 에서 호가 100%→9.3%), 눈금자가 매번
   다시 그려지니 어제와 오늘을 비교할 수도 없었다.
   이제 바늘은 실제 소비율, 눈금은 목표 위치다. 역할이 나뉜다.

   상한 월 6% = 연 72%. 완전자립(연 4%)부터 주의(연 100%) 직전까지 담기는 범위이고,
   목표 슬라이더 상한(월 8%)을 넘겨 잡으면 목표 눈금이 끝에 붙는다. */
const BURN_GAUGE_MAX = 6;

function burnGauge(m, target, tone) {
  return gauge({
    value: m.burnProjected, max: BURN_GAUGE_MAX,
    label: m.burnProjected === null ? '—' : `${m.burnProjected.toFixed(2)}%`,
    sub: '이번 달 예상',
    tone, ticks: [{ at: target, tone: 'accent', label: '목표' }],
  });
}

/* ---------- 드래그 중 부분 갱신 ----------
   홈은 슬라이더와 출력이 한 카드에 섞여 있어 카드째 다시 그릴 수 없다.
   그래서 값이 바뀌는 자리를 하나씩 짚어 갱신한다. 게이지가 여기서 빠져 있어
   드래그 중에는 숫자만 움직이고 게이지는 놓아야 따라오던 문제가 있었다.
   `source` 는 방금 조작한 입력(슬라이더/숫자칸)이라 되받아쓰지 않는다. */
export function liveBurn(source) {
  const s = state;
  const m = metrics(s);
  const target = n(s.profile.targetBurn);
  const main = document.getElementById('main');
  if (!main) return;

  const range = main.querySelector('[data-burn="range"]');
  const num = main.querySelector('[data-burn="num"]');
  if (!range && !num) return;                       // 홈이 아닌 화면
  if (range && source !== 'range') range.value = String(clamp(target, 0.1, 8));
  if (num && source !== 'num') num.value = target.toFixed(1);

  const cap = (m.net * target) / 100;
  const diff = m.projected - cap;
  setText('burn-annual', `연 ${(target * 12).toFixed(1)}%`);
  setText('burn-cap', won(cap));
  const d = document.getElementById('burn-diff');
  if (d) {
    d.textContent = `${diff > 0 ? '+' : ''}${won(diff)}`;
    d.classList.remove('neg', 'pos');
    d.classList.add(diff > 0 ? 'neg' : 'pos');
  }

  const g = m.grade;
  const tone = g.tone === 'muted' ? 'accent' : g.tone;
  setHTML('burn-gauge', burnGauge(m, target, tone));
}

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
function todayCard(m, lim) {
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
  </section>`;
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
