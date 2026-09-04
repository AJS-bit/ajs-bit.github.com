/* 자산 — 자산/부채 관리 + 부채상환 전략 */
import { state, ASSET_TYPES, DEBT_TYPES } from '../store.js';
import { metrics, totals, simulateDebt, assetRate, weightedReturn } from '../finance.js';
import { compact, won, pct, months as fmtMonths, n, clamp } from '../format.js';
import { donut, legend, lineChart, esc } from '../charts.js';
import { card, empty, setHTML, setText } from '../ui.js';

export const title = '자산';
export const tabs = [
  { id: 'assets', label: '자산' },
  { id: 'debts', label: '부채' },
  { id: 'strategy', label: '상환 전략' },
];

export function render(tab = 'assets') {
  if (tab === 'debts') return debtsTab();
  if (tab === 'strategy') return strategyTab();
  return assetsTab();
}

/* ================= 자산 ================= */
function assetsTab() {
  const s = state;
  const t = totals(s);
  const m = metrics(s);
  const slices = Object.entries(ASSET_TYPES).map(([k, v]) => ({
    label: v.label, color: v.color,
    value: s.assets.filter((a) => a.type === k).reduce((x, a) => x + n(a.value), 0),
  }));
  const weighted = weightedReturn(s);

  return `
    <section class="card">
      <div class="row" style="align-items:flex-start;gap:16px;flex-wrap:wrap">
        <div style="flex:1;min-width:230px">
          <span class="lbl">순자산</span>
          <div class="big num ${t.net < 0 ? 'neg' : ''}">${compact(t.net)}</div>
          <div class="stats" style="margin-top:12px">
            <div class="stat"><span class="lbl">총자산</span><div class="v num">${compact(t.assets)}</div></div>
            <div class="stat"><span class="lbl">총부채</span><div class="v num ${t.debts ? 'neg' : ''}">${compact(t.debts)}</div></div>
          </div>
        </div>
        <div style="width:160px;margin:0 auto">${donut(slices, { size: 160, centerTop: compact(t.assets), centerBottom: '총자산' })}</div>
      </div>
      ${legend(slices, t.assets)}
      <div class="divider"></div>
      <div class="stats stats--3">
        <div class="stat"><span class="lbl">유동자산</span><div class="v num">${compact(t.liquid)}</div>
          <div class="s">${t.assets > 0 ? pct((t.liquid / t.assets) * 100, 0) : '—'}</div></div>
        <div class="stat"><span class="lbl">투자자산</span><div class="v num">${compact(t.invested)}</div>
          <div class="s">${t.assets > 0 ? pct((t.invested / t.assets) * 100, 0) : '—'}</div></div>
        <div class="stat"><span class="lbl">가중 기대수익</span><div class="v num pos">${pct(weighted * 100, 2)}</div>
          <div class="s">연 ${compact(t.assets * weighted)}</div></div>
      </div>
    </section>

    <section class="card">
      <div class="card__hd"><h3>보유 자산 ${s.assets.length ? `<span class="sub">${s.assets.length}건</span>` : ''}</h3>
        <button class="btn btn--sm btn--primary" data-act="add-asset">＋ 추가</button></div>
      ${s.assets.length ? `<div class="list">${s.assets
        .slice().sort((a, b) => n(b.value) - n(a.value))
        .map((a) => {
          const ty = ASSET_TYPES[a.type] || ASSET_TYPES.other;
          const share = t.assets > 0 ? (n(a.value) / t.assets) * 100 : 0;
          return `<div class="item">
            <div class="item__ico" style="background:${ty.color}22">${ty.emoji}</div>
            <div class="item__main">
              <b>${esc(a.name || ty.label)}</b>
              <span>${ty.label} · 연 ${(assetRate(a, s) * 100).toFixed(1)}% · 비중 ${share.toFixed(0)}%</span>
            </div>
            <div class="item__val num">${compact(a.value)}
              <small>${won(a.value)}</small></div>
            <button class="item__del" data-act="edit-asset" data-id="${a.id}" aria-label="수정">✎</button>
            <button class="item__del" data-act="del-asset" data-id="${a.id}" aria-label="삭제">✕</button>
          </div>`;
        }).join('')}</div>`
        : empty('💰', '자산을 추가하면 순자산과 소비율이 계산됩니다.',
            `<button class="btn btn--primary btn--sm" data-act="add-asset">첫 자산 추가</button>`)}
    </section>

    ${netTrend(s)}
    ${keyStats(m)}
    ${card('자산 구성 진단', diagnosis(t, m), { sub: '비중 점검' })}
  `;
}

function netTrend(s) {
  const snaps = s.snapshots.slice(-12);
  if (snaps.length < 2) return '';
  return card('순자산 추이',
    lineChart([{ data: snaps.map((x) => x.net), color: 'var(--pos)', fill: true }], {
      height: 160, labels: snaps.map((x) => x.month.slice(5) + '월'),
    }), { sub: `${snaps.length}개월 기록` });
}

function keyStats(m) {
  return `<section class="card">
    <div class="card__hd"><h3>핵심 지표</h3><span class="sub">이번 달 기준</span></div>
    <div class="stats stats--3">
      <div class="stat"><span class="lbl">저축여력</span>
        <div class="v num ${m.capacity < 0 ? 'neg' : 'pos'}">${compact(m.capacity)}</div><div class="s">월</div></div>
      <div class="stat"><span class="lbl">생존 개월수</span>
        <div class="v num">${m.runway === null ? '—' : fmtMonths(m.runway)}</div><div class="s">유동자산 기준</div></div>
      <div class="stat"><span class="lbl">비상금</span>
        <div class="v num ${m.emergency !== null && m.emergency < 3 ? 'warn' : ''}">${m.emergency === null ? '—' : m.emergency.toFixed(1) + '개월'}</div>
        <div class="s">목표 ${state.profile.emergencyMonths}개월</div></div>
      <div class="stat"><span class="lbl">경제적 자유</span>
        <div class="v num">${pct(m.fiProgress, 1)}</div><div class="s">연소비 25배</div></div>
      <div class="stat"><span class="lbl">고정비</span>
        <div class="v num">${compact(m.fixed)}</div>
        <div class="s">소비의 ${m.spend > 0 ? pct((m.fixed / m.spend) * 100, 0) : '—'}</div></div>
      <div class="stat"><span class="lbl">부채비율</span>
        <div class="v num ${m.dti !== null && m.dti > 60 ? 'warn' : ''}">${pct(m.dti, 0)}</div>
        <div class="s">부채 ÷ 자산</div></div>
    </div>
  </section>`;
}

function diagnosis(t, m) {
  if (t.assets <= 0) return empty('🩺', '자산을 입력하면 구성 진단이 표시됩니다.');
  const rows = [];
  const cashShare = (t.cash / t.assets) * 100;
  const investShare = (t.invested / t.assets) * 100;
  const need = m.projected * n(state.profile.emergencyMonths);

  if (m.projected > 0 && t.cash < need)
    rows.push(['warn', '🧯', `비상금 ${(t.cash / m.projected).toFixed(1)}개월치`, `목표 ${state.profile.emergencyMonths}개월(${won(need)})까지 ${won(need - t.cash)} 부족합니다.`]);
  else if (m.projected > 0)
    rows.push(['good', '🧯', `비상금 ${(t.cash / m.projected).toFixed(1)}개월치 확보`, `위기 시 자산을 헐지 않고 버틸 수 있습니다.`]);

  if (cashShare > 60 && t.assets > 5_000_000)
    rows.push(['warn', '💤', `현금 비중 ${cashShare.toFixed(0)}%`, `물가 연 ${(n(state.profile.inflation) * 100).toFixed(1)}% 기준 매년 ${won(t.cash * n(state.profile.inflation))}의 구매력이 줄어듭니다.`]);
  if (investShare < 20 && t.assets > 10_000_000)
    rows.push(['info', '🌱', `투자자산 ${investShare.toFixed(0)}%`, `자산이 스스로 일하는 비중이 낮습니다. 복리 효과가 제한됩니다.`]);
  if (m.dti !== null && m.dti > 60)
    rows.push(['danger', '⚖️', `부채비율 ${m.dti.toFixed(0)}%`, `자산의 절반 이상이 빚입니다. 금리 변동에 취약합니다.`]);
  if (!rows.length) rows.push(['good', '✅', '자산 구성이 균형적입니다', '현금·투자·부채 비중에 특별한 경고 신호가 없습니다.']);

  return rows.map(([lv, ico, tt, bd]) => `<div class="alert alert--${lv}">
    <span class="alert__ico">${ico}</span><div><b>${esc(tt)}</b><p>${esc(bd)}</p></div></div>`).join('');
}

/* ================= 부채 ================= */
function debtsTab() {
  const s = state;
  const t = totals(s);
  const totalMin = s.debts.reduce((x, d) => x + n(d.minPayment), 0);
  const monthlyInterest = s.debts.reduce((x, d) => x + (n(d.balance) * n(d.rate)) / 100 / 12, 0);
  const wavg = t.debts > 0 ? s.debts.reduce((x, d) => x + n(d.balance) * n(d.rate), 0) / t.debts : 0;

  return `
    <section class="card">
      <span class="lbl">총부채</span>
      <div class="big num ${t.debts > 0 ? 'neg' : 'pos'}">${compact(t.debts)}</div>
      <div class="stats stats--3" style="margin-top:12px">
        <div class="stat"><span class="lbl">가중 평균 금리</span><div class="v num">${pct(wavg, 2)}</div></div>
        <div class="stat"><span class="lbl">월 최소상환</span><div class="v num">${compact(totalMin)}</div></div>
        <div class="stat"><span class="lbl">월 이자</span><div class="v num neg">${compact(monthlyInterest)}</div>
          <div class="s">연 ${compact(monthlyInterest * 12)}</div></div>
      </div>
      ${monthlyInterest > 0 ? `<p class="hint" style="margin-top:10px">
        매달 ${won(monthlyInterest)}이 이자로 사라집니다. 이 돈을 연 ${(n(s.profile.expectedReturn) * 100).toFixed(1)}%로 굴리면
        10년 뒤 ${compact(monthlyInterest * ((Math.pow(1 + n(s.profile.expectedReturn) / 12, 120) - 1) / (n(s.profile.expectedReturn) / 12)))}가 됩니다.</p>` : ''}
    </section>

    <section class="card">
      <div class="card__hd"><h3>부채 목록 ${s.debts.length ? `<span class="sub">${s.debts.length}건</span>` : ''}</h3>
        <button class="btn btn--sm btn--primary" data-act="add-debt">＋ 추가</button></div>
      ${s.debts.length ? `<div class="list">${s.debts
        .slice().sort((a, b) => n(b.rate) - n(a.rate))
        .map((d) => {
          const ty = DEBT_TYPES[d.type] || DEBT_TYPES.personal;
          const hi = n(d.rate) >= 10;
          return `<div class="item">
            <div class="item__ico" style="background:${hi ? 'var(--neg-soft)' : 'var(--surface2)'}">${ty.emoji}</div>
            <div class="item__main">
              <b>${esc(d.name || ty.label)} ${hi ? '<span class="chip chip--neg" style="padding:1px 6px;font-size:10px">고금리</span>' : ''}</b>
              <span>연 ${n(d.rate).toFixed(2)}% · 월 상환 ${won(d.minPayment)} · 월 이자 ${won((n(d.balance) * n(d.rate)) / 100 / 12)}</span>
            </div>
            <div class="item__val num neg">${compact(d.balance)}</div>
            <button class="item__del" data-act="edit-debt" data-id="${d.id}" aria-label="수정">✎</button>
            <button class="item__del" data-act="del-debt" data-id="${d.id}" aria-label="삭제">✕</button>
          </div>`;
        }).join('')}</div>`
        : empty('🎉', '등록된 부채가 없습니다.<br>부채가 없다는 건 그 자체로 큰 자산입니다.',
            `<button class="btn btn--sm" data-act="add-debt">부채 추가</button>`)}
    </section>`;
}

/* ================= 상환 전략 ================= */
/* 추가 상환 슬라이더의 상한.
   m.capacity 는 추가 상환액을 이미 뺀 값이라, 상한을 capacity 로 잡으면
   오른쪽으로 끌수록 상한도 같이 줄어드는 움직이는 과녁이 된다.
   추가 상환을 하기 전의 여력(capacity + extra)을 기준으로 고정한다. */
function payMax(m, extra) {
  return Math.max(500000, Math.round(Math.max(0, m.capacity + extra) / 50000) * 50000);
}

/** 상환 전략 탭의 파생값. 최초 렌더와 드래그 중 부분 갱신이 같은 값을 쓴다. */
function strategyData() {
  const s = state;
  const m = metrics(s);
  const debts = s.debts.filter((d) => n(d.balance) > 0);
  if (!debts.length) return null;

  const extra = n(s.settings.extraDebtPay);
  const strategy = s.settings.debtStrategy || 'avalanche';
  const runs = {
    current: simulateDebt(debts, 0, 'current'),
    avalanche: simulateDebt(debts, extra, 'avalanche'),
    snowball: simulateDebt(debts, extra, 'snowball'),
  };
  const chosen = runs[strategy] || runs.avalanche;
  const base = runs.current;
  const saveInterest = base.totalInterest - chosen.totalInterest;
  const saveMonths = base.months !== null && chosen.months !== null ? base.months - chosen.months : null;

  const worst = [...debts].sort((a, b) => n(b.rate) - n(a.rate))[0];
  const ret = n(s.profile.expectedReturn) * 100;
  const payFirst = n(worst.rate) > ret;
  // 부채를 다 갚으면 상환액 전액이 저축여력에 더해진다
  const freedMonthly = m.debtPay + Math.max(0, m.capacity);

  const maxLen = Math.max(base.simulatedMonths || 0, chosen.simulatedMonths || 0, 1);
  const pad = (tl, len) => {
    const a = tl.map((x) => x.balance);
    while (a.length < len) a.push(0);
    return a.slice(0, len);
  };

  return { s, m, debts, extra, strategy, chosen, base, saveInterest, saveMonths,
    worst, ret, payFirst, freedMonthly, maxLen, pad };
}

/* 슬라이더가 들어있는 카드는 드래그 중에 다시 그릴 수 없다.
   그래서 값이 바뀌는 부분만 repay-* id 로 떼어 두고 liveExtraPay() 가 갈아끼운다. */
function strategyTab() {
  const d = strategyData();
  if (!d) {
    return card('🏔️ 부채상환 전략',
      empty('🎉', '상환할 부채가 없습니다.<br>저축여력 전액을 자산 증식에 쓸 수 있는 최고의 상태입니다.',
        `<button class="btn btn--sm" data-nav="goals">목표 설정하러 가기</button>`));
  }
  const { m, extra, strategy } = d;

  return `
    <section class="card">
      <div class="card__hd"><h3>🏔️ 상환 전략 비교</h3>
        <span class="sub" id="repay-sub">추가 상환 ${won(extra)}/월</span></div>
      <div class="seg" style="margin-bottom:14px">
        ${[['avalanche', '고금리 우선', '이자 최소'], ['snowball', '소액 우선', '심리적 동기'], ['current', '최소상환만', '기준선']]
          .map(([k, l, d]) => `<label class="${strategy === k ? 'is-on' : ''}" data-act="set-strategy" data-v="${k}"
            style="flex:1;text-align:center;min-width:96px">${l}<br><span style="font-size:10px;opacity:.75;font-weight:500">${d}</span></label>`).join('')}
      </div>

      <div class="field">
        <label>추가 상환액 (월) — 저축여력 <span id="repay-capacity">${won(Math.max(0, m.capacity))}</span> 중</label>
        <input class="range" type="range" min="0" step="50000"
          max="${payMax(m, extra)}"
          value="${clamp(extra, 0, payMax(m, extra))}" data-act="extra-pay">
        <div class="row" style="margin-top:4px"><span class="hint">0원</span>
          <span class="hint num" style="color:var(--accent);font-weight:700" id="repay-extra">${won(extra)}</span></div>
      </div>

      <div id="repay-stats">${repayStats(d)}</div>
    </section>

    <div id="repay-out">${repayOut(d)}</div>`;
}

/** 추가 상환액에 따라 바뀌는 요약 숫자 (슬라이더가 든 카드 안쪽) */
function repayStats(d) {
  const { m, chosen, saveInterest, saveMonths } = d;
  return `
      <div class="stats stats--3">
        <div class="stat"><span class="lbl">상환 완료까지</span>
          <div class="v num">${chosen.months === null ? '불가' : fmtMonths(chosen.months)}</div>
          ${saveMonths ? `<div class="s pos">${fmtMonths(saveMonths)} 단축</div>` : ''}</div>
        <div class="stat"><span class="lbl">총 이자</span>
          <div class="v num neg">${compact(chosen.totalInterest)}</div>
          ${saveInterest > 1000 ? `<div class="s pos">${compact(saveInterest)} 절약</div>` : ''}</div>
        <div class="stat"><span class="lbl">총 상환액</span>
          <div class="v num">${compact(m.debts + chosen.totalInterest)}</div>
          <div class="s">원금 ${compact(m.debts)}</div></div>
      </div>
      ${chosen.months === null ? `<div class="alert alert--danger" style="margin-top:12px">
        <span class="alert__ico">🛑</span><div><b>현재 상환액으로는 원금이 줄지 않습니다</b>
        <p>이자가 상환액을 앞섭니다. 월 상환액을 늘리거나 금리 인하·채무조정을 알아봐야 합니다.</p></div></div>` : ''}`;
}

/** 추가 상환액에 따라 바뀌는 카드들 (슬라이더 바깥) */
function repayOut(d) {
  const { s, m, debts, strategy, chosen, base, worst, ret, payFirst, freedMonthly, maxLen, pad } = d;
  return `
    <section class="card">
      <div class="card__hd"><h3>부채 잔액 경로</h3><span class="sub">최소상환 vs ${strategy === 'snowball' ? '소액 우선' : '고금리 우선'}</span></div>
      ${lineChart([
        { data: pad(base.timeline, maxLen), color: 'var(--ink3)', dash: '4 4', dot: false },
        { data: pad(chosen.timeline, maxLen), color: 'var(--accent)', fill: true, dot: false },
      ], { height: 170, labels: Array.from({ length: maxLen }, (_, i) =>
        maxLen > 24 ? ((i + 1) % 12 === 0 ? `${(i + 1) / 12}년` : '') : `${i + 1}개월`) })}
      <div class="legend">
        <span><i style="background:var(--ink3)"></i>최소상환만 (${base.months === null ? '불가' : fmtMonths(base.months)})</span>
        <span><i style="background:var(--accent)"></i>선택 전략 (${chosen.months === null ? '불가' : fmtMonths(chosen.months)})</span>
      </div>
    </section>

    <section class="card">
      <div class="card__hd"><h3>완제 순서</h3><span class="sub">${strategy === 'snowball' ? '잔액 작은 순' : strategy === 'avalanche' ? '금리 높은 순' : '기본'}</span></div>
      <div class="list">
        ${chosen.order.slice().sort((a, b) => (a.paidOffAt ?? 9e9) - (b.paidOffAt ?? 9e9)).map((o, i) => {
          const d = debts.find((x) => x.id === o.id);
          return `<div class="item">
            <div class="item__ico">${i + 1}</div>
            <div class="item__main"><b>${esc(d?.name || '부채')}</b>
              <span>연 ${n(d?.rate).toFixed(2)}% · 잔액 ${compact(d?.balance)} · 지급 이자 ${compact(o.interest)}</span></div>
            <div class="item__val num">${o.paidOffAt ? fmtMonths(o.paidOffAt) : '—'}<small>후 완제</small></div>
          </div>`;
        }).join('')}
      </div>
    </section>

    <section class="card">
      <div class="card__hd"><h3>⚖️ 상환 vs 투자</h3></div>
      <div class="alert alert--${payFirst ? 'warn' : 'info'}">
        <span class="alert__ico">${payFirst ? '🧨' : '📈'}</span>
        <div><b>${payFirst ? '상환이 유리합니다' : '투자가 유리할 수 있습니다'}</b>
        <p>최고 금리 ${esc(worst.name || '부채')} <b>${n(worst.rate).toFixed(2)}%</b> vs 기대수익률 <b>${ret.toFixed(1)}%</b>.
        ${payFirst
          ? `상환은 세금·변동성 없이 확정 ${n(worst.rate).toFixed(2)}% 수익과 같습니다. 여유자금 100만원당 연 ${won(1_000_000 * (n(worst.rate) - ret) / 100)} 이득.`
          : `기대수익이 금리보다 높지만 투자는 변동성이 있습니다. 최소상환은 반드시 유지하세요.`}</p></div>
      </div>
      <div class="kv"><span>부채 완제 후 매달 투자 가능액</span><b class="num pos">${won(freedMonthly)}</b></div>
      <p class="hint" style="margin:6px 0 2px">상환액 ${won(m.debtPay)}이 그대로 풀리고, 현재 저축여력 ${won(Math.max(0, m.capacity))}이 더해진 금액입니다.</p>
      <div class="kv"><span>완제 시점부터 10년 굴리면</span>
        <b class="num">${compact((() => {
          const r = n(s.profile.expectedReturn) / 12;
          return r > 0 ? freedMonthly * ((Math.pow(1 + r, 120) - 1) / r) : freedMonthly * 120;
        })())}</b></div>
    </section>`;
}

/* ---------- 드래그 중 부분 갱신 ---------- */
export function liveExtraPay() {
  const d = strategyData();
  if (!d) return;
  setText('repay-sub', `추가 상환 ${won(d.extra)}/월`);
  setText('repay-extra', won(d.extra));
  setText('repay-capacity', won(Math.max(0, d.m.capacity)));
  setHTML('repay-stats', repayStats(d));
  setHTML('repay-out', repayOut(d));
}

