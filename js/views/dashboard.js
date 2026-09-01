/* 홈 — 자산 현황 · 소비율(메인 지표) · 월급 대비 소비 · 경고 · 맞춤 한도 */
import { state, ASSET_TYPES } from '../store.js';
import { metrics, spendingLimit, warnings, allocateGoals } from '../finance.js';
import { burnHistory } from '../coach.js';
import { compact, won, pct, pctSigned, months as fmtMonths, monthLabel, n, clamp } from '../format.js';
import { gauge, donut, legend, lineChart, progress, esc } from '../charts.js';
import { card, empty } from '../ui.js';

export const title = '홈';

export function render() {
  const s = state;
  const m = metrics(s);
  const lim = spendingLimit(s);
  const warns = warnings(s);
  const hasAny = s.assets.length || s.debts.length || s.transactions.length;

  if (!hasAny) return onboarding();

  return `
    ${netWorthCard(m)}
    ${burnCard(m, s)}
    <div class="grid-2">
      <div>${limitCard(m, lim)}${incomeCard(m)}</div>
      <div>${scoreCard(m)}${warnCard(warns)}</div>
    </div>
    ${statsCard(m)}
    ${trendCard(s, m)}
    <button class="fab" data-act="quick-add" aria-label="지출 빠른 입력">＋</button>
  `;
}

/* ---------- 온보딩 ---------- */
function onboarding() {
  return `
    <section class="card" style="text-align:center;padding:26px 18px">
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
          ['🧭', '소비율', '월 소비 ÷ 순자산. 연환산 4% 이하면 자산 수익만으로 살 수 있는 구간입니다.'],
          ['💳', '월급 대비 소비', '실수령액 중 얼마를 쓰는지. 현금흐름의 건강도를 봅니다.'],
          ['🎚️', '맞춤 한도', '목표 달성에 필요한 저축을 먼저 떼고 남는 돈이 이번 달 한도입니다.'],
          ['🔮', '미래 자산 예측', '자산별 수익률·저축·부채상환을 월 단위로 굴려 순자산 경로를 그립니다.'],
        ].map(([e, t, d]) => `<div class="item" style="border:0;padding:8px 0">
          <div class="item__ico">${e}</div>
          <div class="item__main"><b>${t}</b><span style="white-space:normal;line-height:1.5">${d}</span></div>
        </div>`).join('')}
      </div>
    </section>`;
}

/* ---------- 자산 현황 ---------- */
function netWorthCard(m) {
  const ch = m.netMoM;
  const slices = Object.entries(ASSET_TYPES).map(([k, v]) => ({
    label: v.label, color: v.color,
    value: state.assets.filter((a) => a.type === k).reduce((t, a) => t + n(a.value), 0),
  }));
  return `<section class="card">
    <div class="card__hd">
      <h3>자산 현황</h3>
      <span class="sub">${monthLabel(m.key)}</span>
    </div>
    <div class="row" style="align-items:flex-start;gap:16px;flex-wrap:wrap">
      <div style="flex:1;min-width:230px">
        <span class="lbl">순자산</span>
        <div class="big num ${m.net < 0 ? 'neg' : ''}" style="margin:2px 0 6px">${compact(m.net)}</div>
        ${ch && ch.abs !== null ? `<span class="chip ${ch.abs >= 0 ? 'chip--pos' : 'chip--neg'}">
            ${ch.abs >= 0 ? '▲' : '▼'} ${compact(Math.abs(ch.abs))} 전월비${ch.pct !== null ? ` (${pctSigned(ch.pct)})` : ''}</span>`
          : `<span class="chip">이번 달 기준</span>`}
        <div class="stats" style="margin-top:14px">
          <div class="stat"><span class="lbl">총자산</span><div class="v num">${compact(m.assets)}</div></div>
          <div class="stat"><span class="lbl">총부채</span><div class="v num ${m.debts > 0 ? 'neg' : ''}">${compact(m.debts)}</div>
            <div class="s">${m.dti !== null ? `자산의 ${pct(m.dti, 0)}` : '—'}</div></div>
        </div>
      </div>
      <div style="width:168px;margin:0 auto">
        ${donut(slices, { centerTop: compact(m.assets), centerBottom: '총자산' })}
      </div>
    </div>
    ${legend(slices, m.assets)}
  </section>`;
}

/* ---------- 메인 지표: 소비율 ---------- */
function burnCard(m, s) {
  const target = n(s.profile.targetBurn);
  const max = Math.max(target * 3, 1);
  const g = m.grade;
  const tone = g.tone === 'muted' ? 'accent' : g.tone;

  if (m.net <= 0) {
    return `<section class="card" style="border-color:var(--neg)">
      <div class="card__hd"><h3>🧭 소비율</h3><span class="chip chip--neg">${esc(g.label)}</span></div>
      <p class="hint">${esc(g.desc)} 순자산이 0 이하일 때는 소비율을 계산할 수 없습니다.
        먼저 <b style="color:var(--ink)">부채 상환</b>으로 순자산을 0 위로 올리는 것이 1순위입니다.</p>
      <div class="btn-row" style="margin-top:12px"><button class="btn btn--primary btn--sm" data-nav="debt">부채상환 전략 보기</button></div>
    </section>`;
  }

  return `<section class="card">
    <div class="card__hd">
      <h3>🧭 소비율 <span class="sub">순자산 대비</span></h3>
      <span class="chip chip--${tone === 'pos' ? 'pos' : tone === 'neg' ? 'neg' : tone === 'warn' ? 'warn' : 'accent'}">${esc(g.label)}</span>
    </div>
    <div class="row" style="gap:14px;flex-wrap:wrap;align-items:center">
      <div style="flex:1;min-width:190px;max-width:280px;margin:0 auto">
        ${gauge({
          value: m.burnProjected, max,
          label: m.burnProjected === null ? '—' : `${m.burnProjected.toFixed(2)}%`,
          sub: `이번 달 · 목표 ${target.toFixed(1)}%`,
          tone, ticks: [{ at: target }],
        })}
      </div>
      <div style="flex:1;min-width:190px">
        <div class="stats">
          <div class="stat"><span class="lbl">연환산 소비율</span>
            <div class="v num ${tone === 'pos' ? 'pos' : tone === 'neg' ? 'neg' : tone === 'warn' ? 'warn' : ''}">${pct(m.burnAnnual)}</div>
            <div class="s">순자산의 ${pct(m.burnAnnual, 0)}를 1년에 소비</div></div>
          <div class="stat"><span class="lbl">월 소비(예상)</span>
            <div class="v num">${compact(m.projected)}</div>
            <div class="s">${m.done < m.days ? `${m.done}일차 · 현재 ${compact(m.spend)}` : '확정'}</div></div>
        </div>
        <p class="hint" style="margin-top:10px">${esc(g.desc)}</p>
      </div>
    </div>
    <div class="divider"></div>
    <div class="kv"><span>순자산 ${compact(m.net)} 기준 목표 월 소비</span><b class="num">${won(m.net * target / 100)}</b></div>
    <div class="kv"><span>현재 예상과의 차이</span>
      <b class="num ${m.projected > (m.net * target) / 100 ? 'neg' : 'pos'}">
        ${m.projected > (m.net * target) / 100 ? '+' : ''}${won(m.projected - (m.net * target) / 100)}</b></div>
  </section>`;
}

/* ---------- 맞춤 한도 ---------- */
function limitCard(m, lim) {
  if (!(lim.total > 0)) {
    return card('🎚️ 맞춤 한도', empty('🎚️',
      '월 실수령액과 목표를 입력하면<br>목표 달성에 필요한 저축을 뺀 나머지를 한도로 계산합니다.',
      `<button class="btn btn--sm btn--primary" data-act="settings">수입 입력</button>`));
  }
  const ratio = lim.ratio ?? 0;
  const paceRatio = lim.total > 0 ? (lim.pace / lim.total) * 100 : 0;
  const basisText = lim.basis === 'manual' ? '직접 설정'
    : lim.basis === 'net' ? `순자산 목표 소비율(${n(state.profile.targetBurn).toFixed(1)}%/월) 기준`
    : '목표 저축 차감 후 잔액 기준';
  return `<section class="card">
    <div class="card__hd"><h3>🎚️ 맞춤 한도</h3>
      <button class="btn btn--sm btn--ghost" data-act="edit-limit">조정</button></div>
    <div class="row" style="margin-bottom:8px">
      <span class="mid num ${ratio > 100 ? 'neg' : ''}">${won(m.spend)}</span>
      <span class="lbl">/ ${won(lim.total)}</span>
    </div>
    ${progress(ratio, { tone: ratio > 100 ? 'neg' : ratio > paceRatio ? 'warn' : 'pos', markAt: paceRatio, height: 10 })}
    <div class="row" style="margin-top:7px">
      <span class="hint">오늘(${m.done}일차) 적정선 ${won(lim.pace)}</span>
      <span class="hint ${lim.remain < 0 ? 'neg' : 'pos'}">${lim.remain >= 0 ? '남음' : '초과'} ${won(Math.abs(lim.remain))}</span>
    </div>
    <div class="divider"></div>
    <div class="kv"><span>하루 적정 지출</span><b class="num">${won(lim.daily)}</b></div>
    <div class="kv"><span>남은 ${m.days - m.done}일 하루 한도</span>
      <b class="num ${lim.remain < 0 ? 'neg' : ''}">${m.days - m.done > 0 ? won(Math.max(0, lim.remain) / (m.days - m.done)) : '—'}</b></div>
    <div class="kv"><span>목표 저축 우선 배정</span><b class="num">${won(lim.goalNeed)}</b></div>
    <p class="hint" style="margin-top:8px">산출 기준: ${basisText}</p>
  </section>`;
}

/* ---------- 월급 대비 소비 ---------- */
function incomeCard(m) {
  if (!(m.income > 0)) return '';
  const r = m.incomeRatioProjected ?? 0;
  const tone = r > 90 ? 'neg' : r > 70 ? 'warn' : 'pos';
  const debtR = m.income > 0 ? (m.debtPay / m.income) * 100 : 0;
  const saveR = clamp(100 - r - debtR, 0, 100);
  return `<section class="card">
    <div class="card__hd"><h3>💳 월급 대비 소비</h3><span class="sub">실수령 ${compact(m.income)}</span></div>
    <div class="row" style="margin-bottom:10px">
      <span class="mid num ${tone === 'neg' ? 'neg' : tone === 'warn' ? 'warn' : ''}">${pct(r, 0)}</span>
      <span class="chip chip--${tone === 'pos' ? 'pos' : tone}">${r > 90 ? '위험' : r > 70 ? '주의' : r > 50 ? '보통' : '우수'}</span>
    </div>
    <div class="bar" style="height:12px;display:flex">
      <i style="width:${clamp(r, 0, 100)}%;background:var(--${tone === 'pos' ? 'accent' : tone});border-radius:0"></i>
      <i style="width:${clamp(debtR, 0, 100)}%;background:var(--ink3);border-radius:0"></i>
      <i style="width:${saveR}%;background:var(--pos);border-radius:0"></i>
    </div>
    <div class="legend" style="margin-top:9px">
      <span><i style="background:var(--${tone === 'pos' ? 'accent' : tone})"></i>소비 ${won(m.projected)}</span>
      ${m.debtPay > 0 ? `<span><i style="background:var(--ink3)"></i>부채상환 ${won(m.debtPay)}</span>` : ''}
      <span><i style="background:var(--pos)"></i>저축여력 ${won(m.capacity)}</span>
    </div>
    <div class="divider"></div>
    <div class="kv"><span>저축률</span>
      <b class="num ${m.savingsRate < 0 ? 'neg' : m.savingsRate >= 30 ? 'pos' : ''}">${pct(m.savingsRate, 0)}</b></div>
    <div class="kv"><span>이 페이스로 1년</span><b class="num">${compact(m.capacity * 12)}</b></div>
  </section>`;
}

/* ---------- 성장 점수 ---------- */
function scoreCard(m) {
  const sc = m.score;
  return `<section class="card">
    <div class="card__hd"><h3>📊 재산 성장 점수</h3>
      <span class="chip chip--${sc.tier.tone === 'pos' ? 'pos' : sc.tier.tone === 'neg' ? 'neg' : sc.tier.tone === 'warn' ? 'warn' : 'accent'}">${sc.tier.label}</span></div>
    <div class="row" style="margin-bottom:12px">
      <span class="big num">${sc.total}<span style="font-size:15px;color:var(--ink3)"> / 100</span></span>
    </div>
    ${progress((sc.total / 100) * 100, { tone: sc.tier.tone === 'pos' ? 'pos' : sc.tier.tone === 'neg' ? 'neg' : sc.tier.tone === 'warn' ? 'warn' : 'accent', height: 10 })}
    <div class="stack" style="margin-top:14px">
      ${sc.parts.map((p) => `<div>
        <div class="row" style="margin-bottom:4px">
          <span style="font-size:12.5px;font-weight:600">${p.label}</span>
          <span class="num" style="font-size:12px;color:var(--ink3)">${p.score.toFixed(0)} / ${p.max}</span>
        </div>
        <div class="bar bar--thin"><i style="width:${(p.score / p.max) * 100}%"></i></div>
      </div>`).join('')}
    </div>
  </section>`;
}

/* ---------- 경고 ---------- */
function warnCard(warns) {
  const top = warns.slice(0, 3);
  return `<section class="card">
    <div class="card__hd"><h3>⚠️ 소비 경고</h3>
      ${warns.length > 3 ? `<button class="btn btn--sm btn--ghost" data-act="all-warnings">전체 ${warns.length}건</button>` : ''}</div>
    ${top.map((w) => `<div class="alert alert--${w.level}">
      <span class="alert__ico">${w.icon}</span>
      <div><b>${esc(w.title)}</b><p>${esc(w.body)}</p></div>
    </div>`).join('')}
  </section>`;
}

/* ---------- 핵심 지표 ---------- */
function statsCard(m) {
  const alloc = allocateGoals(state);
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
        <div class="v num">${pct(m.fiProgress, 1)}</div><div class="s">연소비 25배 기준</div></div>
      <div class="stat"><span class="lbl">고정비</span>
        <div class="v num">${compact(m.fixed)}</div>
        <div class="s">소비의 ${m.spend > 0 ? pct((m.fixed / m.spend) * 100, 0) : '—'}</div></div>
      <div class="stat"><span class="lbl">목표 필요저축</span>
        <div class="v num ${alloc.surplus < 0 ? 'warn' : ''}">${compact(alloc.totalRequired)}</div>
        <div class="s">${alloc.surplus >= 0 ? `여유 ${compact(alloc.surplus)}` : `부족 ${compact(-alloc.surplus)}`}</div></div>
    </div>
  </section>`;
}

/* ---------- 추이 ---------- */
function trendCard(s, m) {
  const hist = burnHistory(s, 6);
  const withData = hist.filter((h) => h.hasData);
  const snaps = s.snapshots.slice(-12);

  const burnBlock = withData.length >= 2
    ? `${lineChart([{ data: withData.map((h) => h.burn), color: 'var(--accent)', fill: true }], {
        height: 150, labels: withData.map((h) => h.month.slice(5) + '월'), yFormat: (v) => v.toFixed(2) + '%',
      })}<p class="hint" style="margin-top:6px">월별 순자산 대비 소비율(%). 아래로 내려갈수록 재산이 빨리 늘어납니다.</p>`
    : empty('📈', '두 달 이상 지출을 기록하면<br>소비율 추이가 나타납니다.');

  const netBlock = snaps.length >= 2
    ? lineChart([{ data: snaps.map((x) => x.net), color: 'var(--pos)', fill: true }], {
        height: 150, labels: snaps.map((x) => x.month.slice(5) + '월'),
      })
    : empty('💰', '매달 자산을 갱신하면<br>순자산 추이가 쌓입니다.');

  return `<div class="grid-2">
    ${card('소비율 추이', burnBlock, { sub: '최근 6개월' })}
    ${card('순자산 추이', netBlock, { sub: `${snaps.length}개월 기록` })}
  </div>`;
}
