/* 지출 — 기록 · 카테고리 한도 · 소비 페이스 · 경고 */
import { state, CAT, SPEND_CATEGORIES } from '../store.js';
import { metrics, spendingLimit, warnings, monthTx, spendOf } from '../finance.js';
import { savingOpportunities, burnHistory } from '../coach.js';
import { compact, won, pct, monthLabel, addMonths, monthKey, dateLabel, daysInMonth, elapsedDays, n } from '../format.js';
import { hBars, lineChart, progress, vBars, esc } from '../charts.js';
import { card, empty, WARN_ACTION } from '../ui.js';

export const title = '지출';
export const tabs = [
  { id: 'month', label: '이번 달' },
  { id: 'list', label: '내역' },
  { id: 'limit', label: '한도' },
];

let viewMonth = monthKey();
export const setMonth = (k) => { viewMonth = k; };
export const getMonth = () => viewMonth;

export function render(tab = 'month') {
  if (tab === 'list') return listTab();
  if (tab === 'limit') return limitTab();
  return monthTab();
}

function monthNav() {
  const cur = monthKey();
  return `<div class="row" style="margin-bottom:12px">
    <button class="btn btn--sm" data-act="month-prev">‹</button>
    <b style="font-size:14.5px">${monthLabel(viewMonth)}</b>
    <button class="btn btn--sm" data-act="month-next" ${viewMonth >= cur ? 'disabled style="opacity:.4"' : ''}>›</button>
  </div>`;
}

/* ================= 이번 달 ================= */
function monthTab() {
  const s = state;
  const m = metrics(s, viewMonth);
  const lim = spendingLimit(s);
  const sp = spendOf(s, viewMonth);
  const isCurrent = viewMonth === monthKey();

  const catRows = SPEND_CATEGORIES
    .map((c) => ({ label: c.id, value: sp.byCat[c.id] || 0, color: c.color, cap: isCurrent ? lim.categories[c.id] : null }))
    .filter((r) => r.value > 0 || (r.cap && isCurrent))
    .sort((a, b) => b.value - a.value);

  return `
    ${monthNav()}
    <section class="card">
      <!-- min-width 가 작으면 좁은 화면에서 두 칸이 억지로 나란히 서고, 그 안의
           .stats(2열)까지 겹쳐 칸 폭이 47px 까지 좁아진다. .stat .v 는
           overflow-wrap:anywhere 라 '0.97' 과 '%' 가 갈라졌다. 200px 로 잡으면
           그 구간에서 위아래로 떨어져 각자 전체 폭을 쓴다. -->
      <div class="row" style="align-items:flex-start;flex-wrap:wrap;gap:14px">
        <div style="flex:1;min-width:200px">
          <span class="lbl">소비 지출</span>
          <div class="big num">${compact(sp.spend)}</div>
          <span class="hint">${won(sp.spend)} · ${sp.count}건</span>
        </div>
        <div style="flex:1;min-width:200px">
          <div class="stats">
            <!-- 기록이 0건이면 0.00% 가 아니라 '측정 불가'다. 0% 는 4% 룰에서
                 최고 등급이라 "완벽하다"로 읽힌다. 홈은 이미 '측정 불가'인데
                 여기만 0.00% 를 단정해 같은 앱이 다른 말을 하고 있었다. -->
            <div class="stat"><span class="lbl">순자산 대비</span>
              <div class="v num">${sp.count > 0 && m.net > 0 ? pct((sp.spend / m.net) * 100, 2) : '—'}</div>
              <div class="s">${sp.count === 0 ? '기록 후 계산' : m.net > 0 ? `연환산 ${pct((sp.spend * 12 / m.net) * 100, 1)}` : '순자산 미입력'}</div></div>
            <div class="stat"><span class="lbl">월급 대비</span>
              <div class="v num">${sp.count > 0 && m.income > 0 ? pct((sp.spend / m.income) * 100, 0) : '—'}</div>
              <div class="s">${m.income > 0 ? `실수령 ${compact(m.income)}` : '수입 미입력'}</div></div>
          </div>
        </div>
      </div>
      ${isCurrent && lim.total > 0 ? `
        <div class="divider"></div>
        <div class="row" style="margin-bottom:6px">
          <span class="lbl">맞춤 한도 ${won(lim.total)}</span>
          <span class="hint ${lim.remain < 0 ? 'neg' : 'pos'}">${lim.remain >= 0 ? '남음' : '초과'} ${won(Math.abs(lim.remain))}</span>
        </div>
        ${progress(lim.ratio ?? 0, { tone: (lim.ratio ?? 0) > 100 ? 'neg' : 'accent', markAt: (lim.pace / lim.total) * 100, height: 10 })}
        <p class="hint" style="margin-top:6px">회색 선 = 오늘(${m.done}일차)까지의 적정 누적 지출</p>` : ''}
      ${sp.transfer > 0 ? `<p class="hint" style="margin-top:10px">저축/투자·대출상환 ${won(sp.transfer)}은 소비율 계산에서 제외됩니다.</p>` : ''}
    </section>

    ${sp.count ? `<section class="card">
      <div class="card__hd"><h3>일별 누적 지출</h3><span class="sub">한도 페이스 대비</span></div>
      ${dailyChart(s, viewMonth, lim, isCurrent)}
    </section>` : ''}

    <section class="card">
      <div class="card__hd"><h3>카테고리별</h3>
        <span class="sub">고정비 ${compact(sp.fixed)} / 변동비 ${compact(sp.variable)}</span></div>
      ${catRows.length ? hBars(catRows, { format: (v) => compact(v) })
        : empty('🧾', '이번 달 지출 기록이 없습니다.',
            `<button class="btn btn--primary btn--sm" data-act="quick-add">지출 기록하기</button>`)}
    </section>

    ${sp.count ? opportunityCard() : ''}
    ${burnTrend(s)}
    ${monthCompare(s)}
    <button class="fab" data-act="quick-add" aria-label="지출 입력">＋</button>`;
}

function dailyChart(s, key, lim, isCurrent) {
  const days = daysInMonth(key);
  const done = isCurrent ? elapsedDays(key) : days;
  const daily = Array(days).fill(0);
  for (const t of monthTx(s, key)) {
    if (CAT[t.category]?.skip) continue;
    const d = Number(String(t.date).slice(8, 10));
    if (d >= 1 && d <= days) daily[d - 1] += n(t.amount);
  }
  let acc = 0;
  const cum = daily.map((v) => (acc += v));
  const shown = cum.slice(0, Math.max(1, done));
  const series = [{ data: shown, color: 'var(--accent)', fill: true, dot: false }];
  if (lim.total > 0) {
    series.push({
      data: Array.from({ length: Math.max(1, done) }, (_, i) => ((i + 1) / days) * lim.total),
      color: 'var(--ink3)', dash: '5 4', dot: false, width: 1.6,
    });
  }
  return lineChart(series, {
    height: 160, labels: Array.from({ length: Math.max(1, done) }, (_, i) => `${i + 1}일`),
  }) + `<div class="legend">
    <span><i style="background:var(--accent)"></i>실제 누적 ${won(acc)}</span>
    ${lim.total > 0 ? `<span><i style="background:var(--ink3)"></i>한도 페이스</span>` : ''}</div>`;
}

function burnTrend(s) {
  const hist = burnHistory(s, 6).filter((h) => h.hasData && h.burn !== null);
  if (hist.length < 2) return '';
  return card('소비율 추이',
    lineChart([{ data: hist.map((h) => h.burn), color: 'var(--accent)', fill: true }], {
      height: 150, labels: hist.map((h) => h.month.slice(5) + '월'), yFormat: (v) => v.toFixed(2) + '%',
    }) + '<p class="hint" style="margin-top:6px">월별 순자산 대비 소비율(%). 아래로 내려갈수록 재산이 빨리 늘어납니다.</p>',
    { sub: '최근 6개월' });
}

function monthCompare(s) {
  const rows = [];
  for (let i = 5; i >= 0; i--) {
    const k = addMonths(monthKey(), -i);
    const { spend, count } = spendOf(s, k);
    rows.push({ label: k.slice(5) + '월', value: spend, dim: count === 0, color: k === viewMonth ? 'var(--accent)' : 'var(--ink3)' });
  }
  if (!rows.some((r) => r.value > 0)) return '';
  return card('월별 소비 추이', vBars(rows, { height: 130 }), { sub: '최근 6개월' });
}

function opportunityCard() {
  const ops = savingOpportunities(state, 0.1).slice(0, 5);
  if (!ops.length) return '';
  return `<section class="card">
    <div class="card__hd"><h3>💡 10% 줄이면?</h3><span class="sub">기회비용 환산</span></div>
    <div class="list">${ops.map((o) => `<div class="item">
      <div class="item__ico" style="background:${o.color}22">${o.emoji}</div>
      <div class="item__main"><b>${esc(o.category)} 10% 절감</b>
        <span>월 ${won(o.cut)} 절약</span></div>
      <div class="item__val num pos">${o.months !== null && o.months >= 0.1
        ? `${o.months.toFixed(1)}개월<small>목표 단축</small>`
        : `${compact(o.wealth || 0)}<small>10년 뒤 차이</small>`}</div>
    </div>`).join('')}</div>
    <p class="hint" style="margin-top:10px">지출을 '쓴 돈'이 아니라 '미뤄진 목표'로 환산한 값입니다.</p>
  </section>`;
}

/* ================= 내역 ================= */
function listTab() {
  const s = state;
  const tx = monthTx(s, viewMonth).slice().sort((a, b) => (a.date < b.date ? 1 : a.date > b.date ? -1 : 0));
  const byDate = {};
  // `||=` 는 Chrome 85 부터다. 앱의 나머지 문법은 Chrome 80(옵셔널 체이닝)이면
  // 충분한데 이 한 줄 때문에 요구 버전이 5단계 올라간다. 안드로이드 11 의 기본
  // WebView 가 83 이라 실제로 여기서 SyntaxError 가 났다.
  for (const t of tx) { if (!byDate[t.date]) byDate[t.date] = []; byDate[t.date].push(t); }
  const m = metrics(s, viewMonth);

  return `
    ${monthNav()}
    <section class="card">
      <div class="card__hd"><h3>거래 내역 <span class="sub">${tx.length}건</span></h3>
        <button class="btn btn--sm btn--primary" data-act="quick-add">＋ 입력</button></div>
      ${tx.length ? Object.entries(byDate).map(([date, items]) => {
        const sum = items.filter((t) => !CAT[t.category]?.skip).reduce((x, t) => x + n(t.amount), 0);
        return `<div style="margin-bottom:6px">
          <div class="row" style="padding:8px 2px 4px">
            <span class="lbl">${dateLabel(date)}</span>
            <span class="lbl num">${won(sum)}</span>
          </div>
          <div class="list">${items.map((t) => {
            const c = CAT[t.category] || CAT['기타'];
            return `<div class="item">
              <div class="item__ico" style="background:${c.color}22">${c.emoji}</div>
              <div class="item__main"><b>${esc(t.memo || t.category)}</b>
                <span>${esc(t.category)}${c.skip ? ' · 소비율 제외' : ''}${m.net > 0 && n(t.amount) > m.net * 0.005 ? ` · 순자산의 ${((n(t.amount) / m.net) * 100).toFixed(2)}%` : ''}</span></div>
              <div class="item__val num ${c.skip ? 'muted' : ''}">${won(t.amount)}</div>
              <button class="item__del" data-act="edit-tx" data-id="${t.id}" aria-label="수정">✎</button>
              <button class="item__del" data-act="del-tx" data-id="${t.id}" aria-label="삭제">✕</button>
            </div>`;
          }).join('')}</div>
        </div>`;
      }).join('') : empty('🧾', `${monthLabel(viewMonth)} 기록이 없습니다.`,
        `<button class="btn btn--primary btn--sm" data-act="quick-add">지출 기록하기</button>`)}
    </section>
    <button class="fab" data-act="quick-add" aria-label="지출 입력">＋</button>`;
}

/* ================= 한도 ================= */
function limitTab() {
  const s = state;
  const m = metrics(s);
  const lim = spendingLimit(s);
  const auto = s.limits.mode !== 'manual';

  return `
    <section class="card">
      <div class="card__hd"><h3>🎚️ 맞춤 한도 계산</h3></div>
      <div class="seg" style="margin-bottom:14px">
        <label class="${auto ? 'is-on' : ''}" data-act="limit-mode" data-v="auto" style="flex:1;text-align:center">자동 계산</label>
        <label class="${!auto ? 'is-on' : ''}" data-act="limit-mode" data-v="manual" style="flex:1;text-align:center">직접 입력</label>
      </div>
      <div class="big num" style="margin-bottom:4px">${won(lim.total)}</div>
      <span class="hint">이번 달 쓸 수 있는 총액</span>
      <div class="divider"></div>
      <div class="kv"><span>월 실수령 + 부수입</span><b class="num">${won(m.income)}</b></div>
      <div class="kv"><span>− 목표 달성 필요 저축${lim.goalNeedCapped ? ' <span class="chip chip--warn" style="font-size:10px;padding:1px 6px">상한</span>' : ''}</span>
        <b class="num neg">−${won(lim.goalNeed)}</b></div>
      <div class="kv"><span>− 부채 상환</span><b class="num neg">−${won(m.debtPay)}</b></div>
      <div class="kv"><span>= 수입 기준 한도</span><b class="num">${lim.fromIncome === null ? '—' : won(lim.fromIncome)}</b></div>
      <div class="kv"><span>순자산 ${compact(m.net)} × 목표 소비율 ${n(s.profile.targetBurn).toFixed(1)}%</span>
        <b class="num">${lim.fromNet === null ? '—' : won(lim.fromNet)}</b></div>
      <div class="kv"><span><b>적용 한도</b> (보수적인 쪽)</span><b class="num" style="color:var(--accent)">${won(lim.total)}</b></div>
      ${!auto ? `<div class="field" style="margin-top:14px">
        <label>총 한도 직접 입력</label>
        <div class="unit"><input type="text" inputmode="numeric" data-act="manual-total"
          value="${Math.round(n(s.limits.total) || lim.total).toLocaleString('ko-KR')}"><span>원</span></div>
      </div>` : ''}
      ${lim.goalNeedCapped ? `<div class="alert alert--warn" style="margin-top:12px">
        <span class="alert__ico">⚖️</span><div><b>목표가 수입보다 앞서 있습니다</b>
        <p>모든 목표를 기한 내 달성하려면 월 ${won(lim.goalRequired)}이 필요하지만,
        생활이 가능하도록 가처분소득의 70%인 ${won(lim.goalNeed)}까지만 저축에 배정했습니다.
        목표 시점을 늦추거나 금액을 낮추면 한도에 여유가 생깁니다.</p></div></div>` : ''}
      <div class="btn-row" style="margin-top:14px">
        <button class="btn btn--sm" data-act="settings">목표 소비율 조정</button>
        <button class="btn btn--sm" data-nav="goals">목표 관리</button>
      </div>
    </section>

    <section class="card">
      <div class="card__hd"><h3>카테고리별 한도</h3>
        <div class="btn-row">
          <button class="btn btn--sm btn--ghost" data-act="reset-cat-limits">자동 배분</button>
          <button class="btn btn--sm btn--primary" data-act="edit-cat-limits">조정</button>
        </div></div>
      ${hBars(SPEND_CATEGORIES.map((c) => ({
        label: c.id, color: c.color, value: m.byCat[c.id] || 0, cap: lim.categories[c.id],
      })).filter((r) => r.cap > 0 || r.value > 0), { format: (v) => compact(v) })}
      <div class="divider"></div>
      <div class="kv"><span>고정비 (줄이기 어려움)</span><b class="num">${won(lim.fixedCost)}</b></div>
      <div class="kv"><span>변동비 예산 (조절 가능)</span><b class="num ${lim.variableBudget <= 0 ? 'neg' : 'pos'}">${won(lim.variableBudget)}</b></div>
      <p class="hint" style="margin-top:12px">
        ${lim.personalized
          ? '주거·통신·보험·구독은 계약이라 당장 못 줄이므로 실제 지출을 그대로 인정하고, 남은 예산만 내 실제 소비 비중대로 변동비에 나눴습니다.'
          : '지출 기록이 쌓이면 내 실제 소비 비중에 맞춰 자동으로 개인화됩니다. 지금은 표준 비중을 씁니다.'}
        조정하면 그 값이 우선 적용됩니다.
        ${lim.manualSum > 0 ? `<br>직접 설정 합계 ${won(lim.manualSum)} / 총 한도 ${won(lim.total)}
        ${lim.manualSum > lim.total ? `<b class="neg"> — ${won(lim.manualSum - lim.total)} 초과</b>` : ''}` : ''}
      </p>
    </section>

    <section class="card">
      <div class="card__hd"><h3>⚠️ 소비 경고 전체</h3></div>
      ${warnings(s).map((w) => `<div class="alert alert--${w.level}">
        <span class="alert__ico">${w.icon}</span><div><b>${esc(w.title)}</b><p>${esc(w.body)}</p>
        ${w.route && w.route !== 'limit' ? `<button class="btn btn--sm btn--ghost" style="margin-top:8px"
          data-nav="${w.route}">${esc(WARN_ACTION[w.route])}</button>` : ''}
        </div></div>`).join('')}
    </section>`;
}
