/* 의존성 없는 인라인 SVG 차트 */
import { compact, clamp, n } from './format.js';

const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
const id = () => 'g' + Math.random().toString(36).slice(2, 8);

/* ---------- 소비율 게이지 (메인 지표) ---------- */
export function gauge({ value, max = 100, label, sub, tone = 'accent', ticks = [] }) {
  const R = 78, CX = 100, CY = 96, W = 15;
  const start = -220, end = 40, span = end - start;
  const v = value === null ? 0 : clamp((value / max) * 100, 0, 100);
  const pol = (deg, r = R) => {
    const a = (deg * Math.PI) / 180;
    return [CX + r * Math.cos(a), CY + r * Math.sin(a)];
  };
  const arc = (a1, a2, r = R) => {
    const [x1, y1] = pol(a1, r), [x2, y2] = pol(a2, r);
    return `M ${x1.toFixed(2)} ${y1.toFixed(2)} A ${r} ${r} 0 ${a2 - a1 > 180 ? 1 : 0} 1 ${x2.toFixed(2)} ${y2.toFixed(2)}`;
  };
  const gid = id();
  const tickMarks = ticks.map((t) => {
    const a = start + (clamp((t.at / max) * 100, 0, 100) / 100) * span;
    const [x1, y1] = pol(a, R - W / 2 - 2), [x2, y2] = pol(a, R + W / 2 + 2);
    return `<line x1="${x1.toFixed(1)}" y1="${y1.toFixed(1)}" x2="${x2.toFixed(1)}" y2="${y2.toFixed(1)}"
      stroke="var(--ink3)" stroke-width="2" stroke-linecap="round" opacity=".85"/>`;
  }).join('');

  return `<svg class="chart" viewBox="0 0 200 132" role="img" aria-label="${esc(label)} ${esc(sub || '')}">
    <defs><linearGradient id="${gid}" x1="0" y1="1" x2="1" y2="0">
      <stop offset="0%" stop-color="var(--${tone})" stop-opacity=".55"/>
      <stop offset="100%" stop-color="var(--${tone})"/>
    </linearGradient></defs>
    <path d="${arc(start, end)}" fill="none" stroke="var(--surface2)" stroke-width="${W}" stroke-linecap="round"/>
    <path d="${arc(start, start + (v / 100) * span)}" fill="none" stroke="url(#${gid})"
      stroke-width="${W}" stroke-linecap="round" style="transition:d .6s"/>
    ${tickMarks}
    <text x="${CX}" y="${CY - 8}" text-anchor="middle" font-size="30" font-weight="800"
      fill="var(--ink)" style="letter-spacing:-1px">${esc(label)}</text>
    <text x="${CX}" y="${CY + 14}" text-anchor="middle" font-size="11.5" font-weight="600"
      fill="var(--ink3)">${esc(sub || '')}</text>
  </svg>`;
}

/* ---------- 도넛 ---------- */
export function donut(slices, { size = 168, thickness = 26, centerTop = '', centerBottom = '' } = {}) {
  const total = slices.reduce((t, s) => t + Math.max(0, n(s.value)), 0);
  const R = size / 2 - thickness / 2 - 2, C = size / 2;
  if (total <= 0) {
    return `<svg class="chart" viewBox="0 0 ${size} ${size}" style="max-width:${size}px;margin:0 auto">
      <circle cx="${C}" cy="${C}" r="${R}" fill="none" stroke="var(--surface2)" stroke-width="${thickness}"/>
      <text x="${C}" y="${C + 4}" text-anchor="middle" font-size="12" fill="var(--ink3)">데이터 없음</text></svg>`;
  }
  const circ = 2 * Math.PI * R;
  let off = 0;
  const arcs = slices.filter((s) => n(s.value) > 0).map((s) => {
    const frac = n(s.value) / total;
    const dash = `${(frac * circ).toFixed(2)} ${(circ - frac * circ).toFixed(2)}`;
    const el = `<circle cx="${C}" cy="${C}" r="${R}" fill="none" stroke="${s.color}" stroke-width="${thickness}"
      stroke-dasharray="${dash}" stroke-dashoffset="${(-off * circ).toFixed(2)}"
      transform="rotate(-90 ${C} ${C})"><title>${esc(s.label)} ${compact(s.value)} (${(frac * 100).toFixed(1)}%)</title></circle>`;
    off += frac;
    return el;
  }).join('');
  return `<svg class="chart" viewBox="0 0 ${size} ${size}" style="max-width:${size}px;margin:0 auto">
    ${arcs}
    ${centerTop ? `<text x="${C}" y="${C - 3}" text-anchor="middle" font-size="17" font-weight="800" fill="var(--ink)">${esc(centerTop)}</text>` : ''}
    ${centerBottom ? `<text x="${C}" y="${C + 15}" text-anchor="middle" font-size="10.5" font-weight="600" fill="var(--ink3)">${esc(centerBottom)}</text>` : ''}
  </svg>`;
}

export function legend(slices, total) {
  const t = total ?? slices.reduce((a, s) => a + n(s.value), 0);
  return `<div class="legend">${slices.filter((s) => n(s.value) > 0).map((s) => `
    <span><i style="background:${s.color}"></i>${esc(s.label)}
      <b class="num" style="color:var(--ink)">${t > 0 ? ((n(s.value) / t) * 100).toFixed(0) : 0}%</b></span>`).join('')}</div>`;
}

/* ---------- 라인/영역 차트 (여러 시리즈) ---------- */
export function lineChart(series, { height = 170, labels = [], yFormat = compact, band = null, markers = [] } = {}) {
  const W = 340, H = height, PL = 6, PR = 6, PT = 14, PB = 22;
  const all = series.flatMap((s) => s.data).filter(Number.isFinite);
  if (!all.length) return `<div class="empty"><p>표시할 데이터가 없습니다.</p></div>`;
  const bandVals = band ? [...band.lo, ...band.hi] : [];
  let min = Math.min(...all, ...bandVals, 0);
  let max = Math.max(...all, ...bandVals);
  if (max === min) max = min + 1;
  const pad = (max - min) * 0.08;
  max += pad; min -= min < 0 ? pad : 0;

  const len = Math.max(...series.map((s) => s.data.length));
  const X = (i) => PL + (i / Math.max(1, len - 1)) * (W - PL - PR);
  const Y = (v) => PT + (1 - (v - min) / (max - min)) * (H - PT - PB);

  const gid = id();
  let out = `<svg class="chart" viewBox="0 0 ${W} ${H}" preserveAspectRatio="none" style="height:${H}px">
    <defs><linearGradient id="${gid}" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="var(--accent)" stop-opacity=".28"/>
      <stop offset="100%" stop-color="var(--accent)" stop-opacity="0"/></linearGradient></defs>`;

  // 가로 기준선
  for (let g = 0; g <= 3; g++) {
    const v = min + ((max - min) * g) / 3;
    out += `<line x1="${PL}" y1="${Y(v).toFixed(1)}" x2="${W - PR}" y2="${Y(v).toFixed(1)}"
      stroke="var(--line)" stroke-width=".7" stroke-dasharray="3 4"/>`;
  }
  // 0선
  if (min < 0 && max > 0) out += `<line x1="${PL}" y1="${Y(0).toFixed(1)}" x2="${W - PR}" y2="${Y(0).toFixed(1)}" stroke="var(--ink3)" stroke-width="1"/>`;

  // 시나리오 밴드
  if (band) {
    const up = band.hi.map((v, i) => `${X(i).toFixed(1)},${Y(v).toFixed(1)}`).join(' ');
    const dn = band.lo.map((v, i) => `${X(i).toFixed(1)},${Y(v).toFixed(1)}`).reverse().join(' ');
    out += `<polygon points="${up} ${dn}" fill="var(--accent)" opacity=".13"/>`;
  }

  for (const s of series) {
    const pts = s.data.map((v, i) => `${X(i).toFixed(1)},${Y(v).toFixed(1)}`).join(' ');
    if (s.fill) out += `<polygon points="${X(0).toFixed(1)},${Y(min).toFixed(1)} ${pts} ${X(s.data.length - 1).toFixed(1)},${Y(min).toFixed(1)}" fill="url(#${gid})"/>`;
    out += `<polyline points="${pts}" fill="none" stroke="${s.color || 'var(--accent)'}"
      stroke-width="${s.width || 2.2}" stroke-linecap="round" stroke-linejoin="round"
      ${s.dash ? `stroke-dasharray="${s.dash}"` : ''} vector-effect="non-scaling-stroke"/>`;
    if (s.dot !== false && s.data.length <= 24) {
      out += s.data.map((v, i) => `<circle cx="${X(i).toFixed(1)}" cy="${Y(v).toFixed(1)}" r="2.6"
        fill="${s.color || 'var(--accent)'}"><title>${esc(labels[i] || i)} · ${yFormat(v)}</title></circle>`).join('');
    }
  }

  for (const mk of markers) {
    const x = X(mk.at);
    out += `<line x1="${x.toFixed(1)}" y1="${PT}" x2="${x.toFixed(1)}" y2="${H - PB}" stroke="var(--warn)" stroke-width="1.4" stroke-dasharray="4 3"/>
      <text x="${clamp(x, 22, W - 22).toFixed(1)}" y="${PT - 4}" text-anchor="middle" font-size="9" fill="var(--warn)" font-weight="700">${esc(mk.label)}</text>`;
  }

  const step = Math.max(1, Math.ceil(len / 6));
  out += labels.map((l, i) => (i % step === 0 || i === len - 1)
    ? `<text x="${clamp(X(i), 14, W - 14).toFixed(1)}" y="${H - 6}" text-anchor="middle" font-size="9" fill="var(--ink3)">${esc(l)}</text>` : '').join('');
  return out + '</svg>';
}

/* ---------- 가로 막대 리스트 ---------- */
export function hBars(rows, { max = null, format = compact } = {}) {
  const top = max ?? Math.max(...rows.map((r) => n(r.value)), 1);
  return `<div class="stack">${rows.map((r) => {
    const w = clamp((n(r.value) / top) * 100, 0, 100);
    const over = r.cap && n(r.value) > n(r.cap);
    return `<div>
      <div class="row" style="margin-bottom:5px">
        <span style="font-size:12.8px;font-weight:650;display:flex;align-items:center;gap:7px">
          <i class="tag-dot" style="background:${r.color || 'var(--accent)'}"></i>${esc(r.label)}</span>
        <span class="num" style="font-size:12.5px;font-weight:700;color:${over ? 'var(--neg)' : 'var(--ink2)'}">
          ${format(r.value)}${r.cap ? ` <span style="color:var(--ink3);font-weight:500">/ ${format(r.cap)}</span>` : ''}</span>
      </div>
      <div class="bar bar--thin"><i style="width:${w.toFixed(1)}%;background:${over ? 'var(--neg)' : r.color || 'var(--accent)'}"></i></div>
    </div>`;
  }).join('')}</div>`;
}

/* ---------- 세로 막대 (월별) ---------- */
export function vBars(rows, { height = 120, format = compact } = {}) {
  const W = 340, H = height, PB = 20, PT = 12;
  const max = Math.max(...rows.map((r) => n(r.value)), 1);
  const bw = (W - 8) / rows.length;
  return `<svg class="chart" viewBox="0 0 ${W} ${H}" style="height:${H}px">
    ${rows.map((r, i) => {
      const h = clamp((n(r.value) / max) * (H - PT - PB), 1, H - PT - PB);
      const x = 4 + i * bw + bw * 0.18;
      const w = bw * 0.64;
      return `<g><rect x="${x.toFixed(1)}" y="${(H - PB - h).toFixed(1)}" width="${w.toFixed(1)}" height="${h.toFixed(1)}"
        rx="${Math.min(4, w / 2).toFixed(1)}" fill="${r.color || 'var(--accent)'}" opacity="${r.dim ? '.35' : '1'}">
        <title>${esc(r.label)} · ${format(r.value)}</title></rect>
        <text x="${(x + w / 2).toFixed(1)}" y="${H - 6}" text-anchor="middle" font-size="9" fill="var(--ink3)">${esc(r.label)}</text></g>`;
    }).join('')}
  </svg>`;
}

/* ---------- 진행 바 ---------- */
export function progress(ratio, { tone = 'accent', markAt = null, height = 8 } = {}) {
  const w = clamp(n(ratio), 0, 100);
  const over = n(ratio) > 100;
  return `<div class="bar" style="height:${height}px">
    <i style="width:${w.toFixed(1)}%;background:var(--${over ? 'neg' : tone})"></i>
    ${markAt !== null && markAt !== undefined ? `<span class="mark" style="left:${clamp(markAt, 0, 100).toFixed(1)}%"></span>` : ''}
  </div>`;
}

export { esc };
