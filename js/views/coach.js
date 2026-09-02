/* 코치 — 온디바이스 규칙 기반 소비 코칭 */
import { state, RISK } from '../store.js';
import { metrics } from '../finance.js';
import { insights, savingOpportunities, burnHistory, impactOfSaving } from '../coach.js';
import { compact, won, pct, monthLabel, n } from '../format.js';
import { lineChart, esc } from '../charts.js';
import { card, empty, setHTML, setText } from '../ui.js';

export const title = '코치';
export const tabs = [
  { id: 'coach', label: '코칭' },
  { id: 'sim', label: '가정해보기' },
  { id: 'data', label: '데이터' },
];

export const whatif = { cutPct: 10, category: null };

export function render(tab = 'coach') {
  if (tab === 'sim') return whatIfTab();
  if (tab === 'data') return dataTab();
  return coachTab();
}

/* ================= 코칭 ================= */
function coachTab() {
  const s = state;
  const m = metrics(s);
  const cards = insights(s);
  const hist = burnHistory(s, 6).filter((h) => h.hasData);

  return `
    <section class="card">
      <div class="card__hd"><h3>🤖 소비 코치</h3><span class="sub">${monthLabel(m.key)} 진단</span></div>
      <p class="hint">
        입력한 자산·지출·목표를 규칙 엔진으로 분석해 우선순위대로 조언합니다.
        모든 계산은 <b style="color:var(--ink)">이 기기 안에서</b> 이뤄지며 데이터는 외부로 전송되지 않습니다.
      </p>
      ${m.net > 0 ? `<div class="divider"></div>
      <div class="row">
        <span class="lbl">현재 진단</span>
        <span class="chip chip--${m.grade.tone === 'pos' ? 'pos' : m.grade.tone === 'neg' ? 'neg' : m.grade.tone === 'warn' ? 'warn' : 'accent'}">
          소비율 ${pct(m.burnAnnual)}/년 · ${m.grade.label}</span>
      </div>` : ''}
    </section>

    ${cards.map((c, i) => `
      <section class="card" style="border-left:3px solid var(--${c.tone === 'good' ? 'pos' : c.tone === 'danger' ? 'neg' : c.tone === 'warn' ? 'warn' : 'accent'})">
        <div class="card__hd">
          <h3 style="display:flex;gap:8px;align-items:center;font-size:14.5px">
            <span style="font-size:17px">${c.icon}</span>${esc(c.title)}</h3>
          <span class="chip ${c.priority <= 1 ? 'chip--warn' : ''}" style="font-size:10px;padding:2px 8px">
            ${c.priority === 0 ? '긴급' : c.priority === 1 ? '중요' : c.priority === 2 ? '참고' : '정보'}</span>
        </div>
        <p style="font-size:13.2px;line-height:1.65;color:var(--ink2)">${c.body}</p>
        ${c.actions?.length ? `<div class="btn-row" style="margin-top:12px">
          ${c.actions.map((a) => `<button class="btn btn--sm ${i === 0 ? 'btn--primary' : ''}"
            ${a.route ? `data-nav="${a.route}"` : `data-act="${a.act}"`}>${esc(a.label)}</button>`).join('')}
        </div>` : ''}
      </section>`).join('')}

    ${hist.length >= 2 ? `<section class="card">
      <div class="card__hd"><h3>소비율 추이</h3><span class="sub">낮을수록 좋음</span></div>
      ${lineChart([{ data: hist.map((h) => h.burn), color: 'var(--accent)', fill: true }], {
        height: 150, labels: hist.map((h) => h.month.slice(5) + '월'), yFormat: (v) => v.toFixed(2) + '%',
      })}
    </section>` : ''}`;
}

/* ================= 가정해보기 =================
   슬라이더가 두 개 있는 탭이다. 드래그 중에는 화면을 통째로 다시 그릴 수 없으므로
   (잡고 있던 슬라이더 노드가 사라져 드래그가 끊긴다) 출력 부분을 함수로 떼어내고
   컨테이너에 id 를 붙여 둔다. 아래 liveWhatIf() / liveTargetBurn() 이 그 영역만
   갈아끼운다. 최초 렌더와 부분 갱신이 같은 함수를 쓰므로 둘이 어긋날 수 없다. */
function whatIfTab() {
  const tb = n(state.profile.targetBurn);
  return `
    <section class="card">
      <div class="card__hd"><h3>🔬 가정해보기</h3><span class="sub">지출 절감 효과</span></div>
      <div class="field">
        <label>모든 카테고리를 <b style="color:var(--accent)" id="whatif-pct">${whatif.cutPct}%</b> 줄인다면</label>
        <input class="range" type="range" min="0" max="40" step="1" value="${whatif.cutPct}" data-whatif="cutPct">
      </div>
      <div id="whatif-out">${whatIfOut()}</div>
    </section>

    <section class="card">
      <div class="card__hd"><h3>🧭 목표 소비율 맞추기</h3></div>
      <div class="field">
        <label>목표 월 소비율 <b class="num" style="color:var(--accent);float:right" id="tb-pct">${tb.toFixed(1)}%</b>
          <span id="tb-annual">(연 ${(tb * 12).toFixed(1)}%)</span></label>
        <input class="range" type="range" min="0.2" max="10" step="0.1" value="${tb}" data-act="target-burn">
      </div>
      <div id="tb-out">${targetBurnOut()}</div>
    </section>`;
}

/** 절감률 슬라이더의 출력 */
function whatIfOut() {
  const s = state;
  const m = metrics(s);
  const ops = savingOpportunities(s, whatif.cutPct / 100);
  const totalCut = ops.reduce((t, o) => t + o.cut, 0);
  const imp = impactOfSaving(s, totalCut);

  const newSpend = m.projected - totalCut;
  const newBurn = m.net > 0 ? (newSpend * 12 / m.net) * 100 : null;

  if (m.txCount === 0) {
    return empty('🧾', '이번 달 지출을 기록하면 절감 효과를 계산합니다.',
      `<button class="btn btn--primary btn--sm" data-act="quick-add">지출 기록</button>`);
  }
  return `
      <div class="stats">
        <div class="stat"><span class="lbl">월 절감액</span><div class="v num pos">${won(totalCut)}</div>
          <div class="s">연 ${compact(totalCut * 12)}</div></div>
        <div class="stat"><span class="lbl">소비율 변화</span>
          <div class="v num pos">${pct(m.burnAnnual)} → ${pct(newBurn)}</div>
          <div class="s">연환산</div></div>
        <div class="stat"><span class="lbl">저축률 변화</span>
          <div class="v num pos">${pct(m.savingsRate, 0)} → ${pct(m.income > 0 ? ((m.capacity + totalCut) / m.income) * 100 : null, 0)}</div></div>
        <div class="stat"><span class="lbl">${imp.kind === 'goal' ? '목표 단축' : '10년 뒤 차이'}</span>
          <div class="v num pos">${imp.kind === 'goal' ? `${imp.monthsSaved.toFixed(1)}개월` : compact(imp.delta || 0)}</div>
          <div class="s">${imp.kind === 'goal' ? esc(imp.goal.name || '1순위 목표') : '복리 반영'}</div></div>
      </div>
      <div class="divider"></div>
      <div class="list">${ops.slice(0, 8).map((o) => `<div class="item">
        <div class="item__ico" style="background:${o.color}22">${o.emoji}</div>
        <div class="item__main"><b>${esc(o.category)}</b>
          <span>${won(o.amount)} → ${won(o.amount - o.cut)}</span></div>
        <div class="item__val num pos">−${won(o.cut)}
          <small>${o.months !== null && o.months >= 0.1 ? `목표 ${o.months.toFixed(1)}개월 단축` : `10년 뒤 ${compact(o.wealth || 0)}`}</small></div>
      </div>`).join('')}</div>`;
}

/** 목표 소비율 슬라이더의 출력 */
function targetBurnOut() {
  const s = state;
  const m = metrics(s);
  const tb = n(s.profile.targetBurn);
  if (!(m.net > 0)) return `<p class="hint">순자산이 0보다 커야 목표 소비율을 계산할 수 있습니다.</p>`;
  const cap = (m.net * tb) / 100;
  const over = m.projected > cap ? 'neg' : 'pos';
  return `
        <div class="kv"><span>목표 월 소비 상한</span><b class="num">${won(cap)}</b></div>
        <div class="kv"><span>현재 예상 월 소비</span><b class="num ${over}">${won(m.projected)}</b></div>
        <div class="kv"><span>차이</span><b class="num ${over}">${won(m.projected - cap)}</b></div>
        <div class="kv"><span>이 소비율을 유지하려면 필요한 순자산</span>
          <b class="num">${compact((m.projected * 100) / tb)}</b></div>
        <p class="hint" style="margin-top:10px">
          소비율은 <b style="color:var(--ink)">지출을 줄이거나</b> <b style="color:var(--ink)">자산을 늘려서</b> 낮출 수 있습니다.
          자산이 커질수록 같은 지출도 소비율이 자연히 내려갑니다.
        </p>`;
}

/* ---------- 드래그 중 부분 갱신 ---------- */
export function liveWhatIf() {
  setText('whatif-pct', `${whatif.cutPct}%`);
  setHTML('whatif-out', whatIfOut());
}

export function liveTargetBurn() {
  const tb = n(state.profile.targetBurn);
  setText('tb-pct', `${tb.toFixed(1)}%`);
  setText('tb-annual', `(연 ${(tb * 12).toFixed(1)}%)`);
  setHTML('tb-out', targetBurnOut());
}

/* ================= 데이터 ================= */
function dataTab() {
  const s = state;
  const m = metrics(s);
  return `
    <section class="card">
      <div class="card__hd"><h3>⚙️ 내 설정</h3>
        <button class="btn btn--sm btn--primary" data-act="settings">수정</button></div>
      <div class="kv"><span>월 실수령액</span><b class="num">${won(s.profile.monthlyIncome)}</b></div>
      <div class="kv"><span>부수입</span><b class="num">${won(s.profile.extraIncome)}</b></div>
      <div class="kv"><span>위험성향</span><b>${RISK[s.profile.riskProfile]?.label || '균형형'}</b></div>
      <div class="kv"><span>연 기대수익률</span><b class="num">${(n(s.profile.expectedReturn) * 100).toFixed(1)}%</b></div>
      <div class="kv"><span>물가상승률</span><b class="num">${(n(s.profile.inflation) * 100).toFixed(1)}%</b></div>
      <div class="kv"><span>목표 월 소비율</span><b class="num">${n(s.profile.targetBurn).toFixed(1)}%</b></div>
      <div class="kv"><span>비상금 목표</span><b class="num">${s.profile.emergencyMonths}개월</b></div>
    </section>

    <section class="card">
      <div class="card__hd"><h3>📦 기록 현황</h3></div>
      <div class="stats stats--3">
        <div class="stat"><span class="lbl">자산</span><div class="v num">${s.assets.length}건</div></div>
        <div class="stat"><span class="lbl">부채</span><div class="v num">${s.debts.length}건</div></div>
        <div class="stat"><span class="lbl">거래</span><div class="v num">${s.transactions.length}건</div></div>
        <div class="stat"><span class="lbl">목표</span><div class="v num">${s.goals.length}개</div></div>
        <div class="stat"><span class="lbl">순자산 기록</span><div class="v num">${s.snapshots.length}개월</div></div>
        <div class="stat"><span class="lbl">시작일</span><div class="v" style="font-size:13px">${esc(s.profile.startedAt || '—')}</div></div>
      </div>
    </section>

    <section class="card">
      <div class="card__hd"><h3>🔐 데이터 관리</h3></div>
      <p class="hint" style="margin-bottom:14px">
        모든 데이터는 이 브라우저의 저장소에만 있습니다. 서버로 전송되지 않으며,
        브라우저 데이터를 지우면 함께 사라집니다. 정기적으로 내보내 두세요.
      </p>
      <div class="btn-row">
        <button class="btn" data-act="export">JSON 내보내기</button>
        <button class="btn" data-act="import">불러오기</button>
        <button class="btn" data-act="load-demo">예시 데이터</button>
        <button class="btn btn--danger" data-act="reset">전체 초기화</button>
      </div>
    </section>

    <section class="card card--flat">
      <p class="hint">
        <b style="color:var(--ink)">계산 기준</b><br>
        · 소비율 = 월 소비지출 ÷ 순자산 (저축/투자 이체·대출상환 제외)<br>
        · 월 중에는 경과일 기준 페이스로 월말 지출을 추정합니다<br>
        · 저축여력 = 수입 − 예상 소비 − 부채 상환액<br>
        · 미래 예측은 자산별 기대수익률을 월복리로 적용하며, 세금·수수료는 반영하지 않습니다<br>
        · 투자 성과는 보장되지 않으며 이 앱은 투자 자문이 아닌 참고 도구입니다
      </p>
    </section>`;
}
