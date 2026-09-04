/* 숫자 · 통화 · 날짜 포맷 유틸 */

export const n = (v) => {
  const x = typeof v === 'string' ? Number(v.replace(/[^\d.-]/g, '')) : Number(v);
  return Number.isFinite(x) ? x : 0;
};

/** 1234567 -> "1,234,567원" */
export function won(v, { sign = false, unit = '원' } = {}) {
  const x = Math.round(n(v));
  const s = sign && x > 0 ? '+' : '';
  return s + x.toLocaleString('ko-KR') + unit;
}

/** 추정치를 1원 단위까지 말하지 않는다.
    과거 3개월 평균에서 나온 숫자를 "363,131원"이라 하면 실측처럼 읽힌다.
    10만원 이상은 천원, 미만은 백원 단위로 접는다.
    실제로 정확한 값(한도·잔액·이번 달 구독료)에는 쓰지 않는다. */
export function approx(v, opt) {
  const x = Math.round(n(v));
  const unit = Math.abs(x) >= 100000 ? 1000 : 100;
  return won(Math.round(x / unit) * unit, opt);
}

/** 123456789 -> "1억 2,346만" · 12340000 -> "1,234만" */
export function compact(v) {
  const raw = Math.round(n(v));
  const neg = raw < 0 ? '-' : '';
  const x = Math.abs(raw);
  if (x >= 1e8) {
    const eok = Math.floor(x / 1e8);
    const man = Math.round((x % 1e8) / 1e4);
    if (man === 0) return `${neg}${eok.toLocaleString('ko-KR')}억`;
    if (man === 10000) return `${neg}${(eok + 1).toLocaleString('ko-KR')}억`;
    return `${neg}${eok.toLocaleString('ko-KR')}억 ${man.toLocaleString('ko-KR')}만`;
  }
  if (x >= 1e4) return `${neg}${Math.round(x / 1e4).toLocaleString('ko-KR')}만`;
  return `${neg}${x.toLocaleString('ko-KR')}`;
}

/** 부호가 붙는 축약 표기 */
export function compactSigned(v) {
  const x = n(v);
  return (x > 0 ? '+' : '') + compact(x);
}

/** 퍼센트. null/무한대는 '—' */
export function pct(v, d = 1) {
  if (v === null || v === undefined || !Number.isFinite(v)) return '—';
  return `${n(v).toFixed(d)}%`;
}

export function pctSigned(v, d = 1) {
  if (v === null || !Number.isFinite(v)) return '—';
  return (v > 0 ? '+' : '') + n(v).toFixed(d) + '%';
}

/** 개월수 -> "3년 2개월" */
export function months(m) {
  if (m === null || !Number.isFinite(m)) return '—';
  if (m >= 12 * 80) return '80년+';
  const t = Math.max(0, Math.round(m));
  const y = Math.floor(t / 12);
  const r = t % 12;
  if (y === 0) return `${r}개월`;
  if (r === 0) return `${y}년`;
  return `${y}년 ${r}개월`;
}

export const today = () => new Date().toISOString().slice(0, 10);
export const monthKey = (d = new Date()) =>
  (typeof d === 'string' ? d : d.toISOString().slice(0, 10)).slice(0, 7);

/** "2026-09" -> "2026년 9월" */
export function monthLabel(key) {
  const [y, m] = String(key).split('-');
  return `${y}년 ${Number(m)}월`;
}

export function shortMonth(key) {
  const [, m] = String(key).split('-');
  return `${Number(m)}월`;
}

/** key 기준 n개월 이동 */
export function addMonths(key, delta) {
  const [y, m] = String(key).split('-').map(Number);
  const d = new Date(y, m - 1 + delta, 1);
  return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}`;
}

export function daysInMonth(key) {
  const [y, m] = String(key).split('-').map(Number);
  return new Date(y, m, 0).getDate();
}

/** 오늘이 해당 달의 며칠째인지(과거 달이면 말일) */
export function elapsedDays(key) {
  const now = new Date();
  const cur = monthKey(now);
  if (key < cur) return daysInMonth(key);
  if (key > cur) return 0;
  return now.getDate();
}

export function dateLabel(iso) {
  const [, m, d] = String(iso).split('-');
  return `${Number(m)}.${Number(d)}`;
}

/** 목표일까지 남은 개월수 */
export function monthsUntil(iso) {
  if (!iso) return null;
  const t = new Date(iso + 'T00:00:00');
  const now = new Date();
  return (t.getFullYear() - now.getFullYear()) * 12 + (t.getMonth() - now.getMonth())
    + (t.getDate() - now.getDate()) / 30;
}

export const clamp = (v, lo, hi) => Math.min(hi, Math.max(lo, v));
export const uid = () => Math.random().toString(36).slice(2, 10) + Date.now().toString(36).slice(-4);
