/* 의존성 없는 인라인 SVG 차트 */
import { compact, clamp, n } from './format.js';

const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
const id = () => 'g' + Math.random().toString(36).slice(2, 8);

/* ---------- 소비율 게이지 (메인 지표) ---------- */
export function gauge({ value, max = 100, label, sub, tone = 'accent', ticks = [] }) {
  // 원호 끝점이 viewBox 밖으로 나가면 아래 요소와 겹친다.
  // end=35° 기준 최하단 y = CY + R·sin35 + W/2 = 88 + 44.7 + 7.5 ≈ 140 이므로 높이 146으로 잡는다.
  const R = 78, CX = 100, CY = 88, W = 15, H = 146;
  const start = -215, end = 35, span = end - start;
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

  return `<svg class="chart" viewBox="0 0 200 ${H}" role="img" aria-label="${esc(label)} ${esc(sub || '')}">
    <defs><linearGradient id="${gid}" x1="0" y1="1" x2="1" y2="0">
      <stop offset="0%" stop-color="var(--${tone})" stop-opacity=".55"/>
      <stop offset="100%" stop-color="var(--${tone})"/>
    </linearGradient></defs>
    <path d="${arc(start, end)}" fill="none" stroke="var(--surface2)" stroke-width="${W}" stroke-linecap="round"/>
    <path d="${arc(start, start + (v / 100) * span)}" fill="none" stroke="url(#${gid})"
      stroke-width="${W}" stroke-linecap="round" style="transition:d .6s"/>
    ${tickMarks}
    <text x="${CX}" y="${CY - 2}" text-anchor="middle" font-size="30" font-weight="800"
      fill="var(--ink)" style="letter-spacing:-1px">${esc(label)}</text>
    <text x="${CX}" y="${CY + 19}" text-anchor="middle" font-size="11" font-weight="600"
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

/* ---------- 원형 진행 링 (목표 진척용) ---------- */
export function ring({ ratio, size = 200, thickness = 14, tone = 'accent', top = '', mid = '', bottom = '', markAt = null }) {
  const R = size / 2 - thickness / 2 - 3;
  const C = size / 2;
  const circ = 2 * Math.PI * R;
  const v = clamp(n(ratio), 0, 100);
  const gid = id();
  const markDeg = markAt !== null ? (clamp(markAt, 0, 100) / 100) * 360 - 90 : null;
  const mk = markDeg !== null
    ? (() => {
        const a = (markDeg * Math.PI) / 180;
        const x1 = C + (R - thickness / 2 - 1) * Math.cos(a), y1 = C + (R - thickness / 2 - 1) * Math.sin(a);
        const x2 = C + (R + thickness / 2 + 1) * Math.cos(a), y2 = C + (R + thickness / 2 + 1) * Math.sin(a);
        return `<line x1="${x1.toFixed(1)}" y1="${y1.toFixed(1)}" x2="${x2.toFixed(1)}" y2="${y2.toFixed(1)}"
          stroke="var(--ink3)" stroke-width="2.4" stroke-linecap="round"/>`;
      })()
    : '';
  return `<svg class="chart" viewBox="0 0 ${size} ${size}" style="max-width:${size}px;margin:0 auto;display:block">
    <defs><linearGradient id="${gid}" x1="0" y1="1" x2="1" y2="0">
      <stop offset="0%" stop-color="var(--${tone})" stop-opacity=".5"/>
      <stop offset="100%" stop-color="var(--${tone})"/>
    </linearGradient></defs>
    <circle cx="${C}" cy="${C}" r="${R}" fill="none" stroke="var(--line)" stroke-width="${thickness}" opacity=".85"/>
    <circle cx="${C}" cy="${C}" r="${R}" fill="none" stroke="url(#${gid})" stroke-width="${thickness}"
      stroke-linecap="round" transform="rotate(-90 ${C} ${C})"
      stroke-dasharray="${((v / 100) * circ).toFixed(2)} ${circ.toFixed(2)}"
      style="transition:stroke-dasharray .6s cubic-bezier(.3,.9,.3,1)"/>
    ${mk}
    ${top ? `<text x="${C}" y="${C - 24}" text-anchor="middle" font-size="11.5" font-weight="700" fill="var(--ink3)">${esc(top)}</text>` : ''}
    <text x="${C}" y="${C + 8}" text-anchor="middle" font-size="27" font-weight="800" fill="var(--ink)" style="letter-spacing:-1px">${esc(mid)}</text>
    ${bottom ? `<text x="${C}" y="${C + 30}" text-anchor="middle" font-size="11.5" font-weight="600" fill="var(--ink3)">${esc(bottom)}</text>` : ''}
  </svg>`;
}

/* ---------- 스파크라인 (작은 경로 그래프) ----------
   markLabel/targetLabel 을 주면 세로 마커선과 가로 목표선에 설명이 붙는다.
   라벨 없이는 주황 점선이 무엇인지 알 수 없다.
   라벨을 쓰면 위쪽 TOP 만큼을 글자 자리로 비우므로 그래프가 그만큼 낮아진다.
   height 를 그대로 두면 선이 눌리니 호출부에서 높이를 함께 올릴 것. */
export function spark(data, {
  height = 54, color = 'var(--accent)', target = null, markAt = null,
  markLabel = '', targetLabel = '',
} = {}) {
  const W = 320, H = height, P = 3;
  const TOP = markLabel ? 14 : P;               // 세로 마커 라벨이 앉는 위쪽 여백
  const vals = data.filter(Number.isFinite);
  if (vals.length < 2) return '';
  // 목표 대비 성장이 보이도록 실제 구간을 쓴다 (0 기준으로 잡으면 선이 평평해진다)
  const max = Math.max(...vals, target ?? -Infinity);
  const lo = Math.min(...vals);
  const min = lo - (max - lo) * 0.12;
  const X = (i) => P + (i / (data.length - 1)) * (W - P * 2);
  const Y = (v) => TOP + (1 - (v - min) / Math.max(1, max - min)) * (H - TOP - P);
  const pts = data.map((v, i) => `${X(i).toFixed(1)},${Y(v).toFixed(1)}`).join(' ');
  const gid = id();

  const svg = `<svg class="chart" viewBox="0 0 ${W} ${H}" preserveAspectRatio="none" style="height:${H}px">
    <defs><linearGradient id="${gid}" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="${color}" stop-opacity=".3"/>
      <stop offset="100%" stop-color="${color}" stop-opacity="0"/></linearGradient></defs>
    ${target !== null ? `<line x1="${P}" y1="${Y(target).toFixed(1)}" x2="${W - P}" y2="${Y(target).toFixed(1)}"
      stroke="var(--ink3)" stroke-width="1" stroke-dasharray="4 3"/>` : ''}
    <polygon points="${X(0).toFixed(1)},${H - P} ${pts} ${X(data.length - 1).toFixed(1)},${H - P}" fill="url(#${gid})"/>
    <polyline points="${pts}" fill="none" stroke="${color}" stroke-width="2.2"
      stroke-linecap="round" stroke-linejoin="round" vector-effect="non-scaling-stroke"/>
    ${markAt !== null ? `<line x1="${X(markAt).toFixed(1)}" y1="${TOP}" x2="${X(markAt).toFixed(1)}" y2="${H - P}"
      stroke="var(--warn)" stroke-width="1.4" stroke-dasharray="3 3"/>` : ''}
  </svg>`;

  const showTarget = target !== null && targetLabel;
  const showMark = markAt !== null && markLabel;
  if (!showTarget && !showMark) return svg;

  // 라벨은 SVG 안에 넣지 않는다.
  // preserveAspectRatio="none" 이라 가로만 늘어나는데(높이는 style 로 못박혀 세로 배율이
  // 항상 1) 글자를 안에 넣으면 글자까지 같이 납작해진다. 화면이 넓을수록 심해서
  // 뷰포트 1100px 에서는 2.5배까지 퍼졌다. 그래서 HTML 로 얹는다.
  //   · 세로: 세로 배율이 1이므로 viewBox 의 y 를 그대로 px 로 쓴다
  //   · 가로: 컨테이너 대비 백분율. 마커는 선 위에 중앙 정렬하되 양 끝에서
  //           잘리지 않게 CSS clamp() 로 글자 절반만큼 안쪽에 묶는다
  const ty = Y(target) + 10 > H - 2 ? Y(target) - 12 : Y(target) + 2;
  const half = (t) => Math.round(t.length * 5.6) + 3;
  return `<div class="spark">${svg}
    ${showTarget ? `<span class="spark__lbl" style="top:${ty.toFixed(1)}px;left:${(P + 2) / W * 100}%">${esc(targetLabel)}</span>` : ''}
    ${showMark ? `<span class="spark__lbl spark__lbl--mark" style="top:0;left:clamp(${half(markLabel)}px, ${(X(markAt) / W * 100).toFixed(2)}%, calc(100% - ${half(markLabel)}px))">${esc(markLabel)}</span>` : ''}
  </div>`;
}
