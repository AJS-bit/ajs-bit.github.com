/* DOM · 모달 · 토스트 헬퍼 */
import { esc } from './charts.js';
import { n } from './format.js';

export const $ = (sel, root = document) => root.querySelector(sel);
export const $$ = (sel, root = document) => [...root.querySelectorAll(sel)];

/** 위임 이벤트 */
export function delegate(root, type, sel, fn) {
  root.addEventListener(type, (e) => {
    const t = e.target.closest(sel);
    if (t && root.contains(t)) fn(e, t);
  });
}

export function toast(msg, ms = 2200) {
  const root = $('#toast-root');
  const el = document.createElement('div');
  el.className = 'toast';
  el.textContent = msg;
  root.appendChild(el);
  setTimeout(() => { el.style.opacity = '0'; el.style.transition = 'opacity .25s'; }, ms - 250);
  setTimeout(() => el.remove(), ms);
}

/**
 * 모달. fields 배열로 폼을 만들고 제출값을 resolve.
 * field: {key,label,type,value,options,help,unit,required,min,max,step,money}
 */
export function modal({ title, fields = [], html = '', submit = '저장', onSubmit, wide = false, danger = false }) {
  return new Promise((resolve) => {
    const root = $('#modal-root');
    // 같은 클릭이 두 번 처리되는 등의 이유로 모달이 겹쳐 쌓이지 않게 한다
    if (root.children.length) { resolve(null); return; }
    const box = document.createElement('div');
    box.className = 'modal';
    box.innerHTML = `
      <div class="modal__bg" data-close></div>
      <div class="modal__box" role="dialog" aria-modal="true" aria-label="${esc(title)}" style="${wide ? 'max-width:640px' : ''}">
        <div class="modal__hd">
          <h3>${esc(title)}</h3>
          <button class="iconbtn" data-close aria-label="닫기">✕</button>
        </div>
        <form id="mform" novalidate>
          ${fields.map(fieldHTML).join('')}
          ${html}
          ${onSubmit !== null ? `<div class="btn-row" style="margin-top:16px">
            <button type="submit" class="btn btn--primary btn--block ${danger ? 'btn--danger' : ''}">${esc(submit)}</button>
          </div>` : ''}
        </form>
      </div>`;
    root.appendChild(box);

    const close = (val) => { box.remove(); resolve(val); };
    box.querySelectorAll('[data-close]').forEach((b) => b.addEventListener('click', () => close(null)));
    const onKey = (e) => { if (e.key === 'Escape') { close(null); document.removeEventListener('keydown', onKey); } };
    document.addEventListener('keydown', onKey);

    // 금액 입력 천단위 콤마
    box.querySelectorAll('input[data-money]').forEach((inp) => {
      const fmt = () => {
        const v = inp.value.replace(/[^\d]/g, '');
        inp.value = v ? Number(v).toLocaleString('ko-KR') : '';
      };
      fmt();
      inp.addEventListener('input', () => {
        const end = inp.value.length - inp.selectionStart;
        fmt();
        const pos = Math.max(0, inp.value.length - end);
        try { inp.setSelectionRange(pos, pos); } catch { /* noop */ }
      });
    });

    box.querySelector('#mform').addEventListener('submit', (e) => {
      e.preventDefault();
      const data = {};
      for (const f of fields) {
        // seg 는 같은 name 을 공유하는 라디오 묶음이라 첫 요소가 아니라 선택된 것을 읽어야 한다
        const el = f.type === 'seg'
          ? box.querySelector(`[name="${f.key}"]:checked`)
          : box.querySelector(`[name="${f.key}"]`);
        if (!el) continue;
        if (f.type === 'checkbox') data[f.key] = el.checked;
        else if (f.type === 'number' || f.money) data[f.key] = n(el.value);
        else data[f.key] = el.value.trim();
        if (f.required && (data[f.key] === '' || (f.money && !data[f.key]))) {
          el.focus(); toast(`${f.label}을(를) 입력해 주세요`); return;
        }
      }
      document.removeEventListener('keydown', onKey);
      if (onSubmit) { const r = onSubmit(data, box); if (r === false) return; }
      close(data);
    });

    setTimeout(() => box.querySelector('input,select,textarea')?.focus(), 60);
  });
}

function fieldHTML(f) {
  // 소제목. 값을 읽지 않으므로 submit 루프에서는 el 이 없어 그대로 건너뛴다.
  if (f.type === 'group') {
    return `<div class="lbl" style="margin:16px 0 8px;padding-top:12px;border-top:1px solid var(--line)">${f.label}</div>`;
  }
  const id = `f_${f.key}`;
  const common = `id="${id}" name="${f.key}" ${f.required ? 'required' : ''}`;
  let input;
  if (f.type === 'select') {
    input = `<select ${common}>${f.options.map((o) => {
      const val = typeof o === 'string' ? o : o.value;
      const lab = typeof o === 'string' ? o : o.label;
      return `<option value="${esc(val)}" ${String(f.value) === String(val) ? 'selected' : ''}>${esc(lab)}</option>`;
    }).join('')}</select>`;
  } else if (f.type === 'textarea') {
    input = `<textarea ${common} rows="3">${esc(f.value ?? '')}</textarea>`;
  } else if (f.type === 'seg') {
    input = `<div class="seg">${f.options.map((o, i) => `
      <input type="radio" id="${id}_${i}" name="${f.key}" value="${esc(o.value)}" ${String(f.value) === String(o.value) ? 'checked' : ''}>
      <label for="${id}_${i}">${esc(o.label)}</label>`).join('')}</div>`;
  } else if (f.money) {
    input = `<div class="unit"><input ${common} type="text" inputmode="numeric" data-money
      value="${f.value ?? ''}" placeholder="0"><span>원</span></div>`;
  } else if (f.unit) {
    input = `<div class="unit"><input ${common} type="${f.type || 'number'}" step="${f.step ?? 'any'}"
      ${f.min !== undefined ? `min="${f.min}"` : ''} ${f.max !== undefined ? `max="${f.max}"` : ''}
      value="${f.value ?? ''}"><span>${esc(f.unit)}</span></div>`;
  } else {
    input = `<input ${common} type="${f.type || 'text'}" value="${esc(f.value ?? '')}"
      ${f.placeholder ? `placeholder="${esc(f.placeholder)}"` : ''}
      ${f.min !== undefined ? `min="${f.min}"` : ''} ${f.max !== undefined ? `max="${f.max}"` : ''}
      ${f.step ? `step="${f.step}"` : ''}>`;
  }
  return `<div class="field">
    ${f.label ? `<label for="${id}">${esc(f.label)}</label>` : ''}
    ${input}
    ${f.help ? `<div class="help">${f.help}</div>` : ''}
  </div>`;
}

export async function confirmDialog(title, body, submit = '삭제') {
  const r = await modal({
    title, fields: [], html: `<p class="hint" style="margin-bottom:4px">${body}</p>`,
    submit, danger: true,
  });
  return r !== null;
}

export const card = (title, body, { sub = '', action = '' } = {}) => `
  <section class="card">
    ${title ? `<div class="card__hd"><h3>${esc(title)}</h3>
      ${action || (sub ? `<span class="sub">${esc(sub)}</span>` : '')}</div>` : ''}
    ${body}
  </section>`;

export const empty = (emoji, text, btn = '') => `
  <div class="empty"><span class="e">${emoji}</span><p>${text}</p>${btn}</div>`;

/* ---------- 부분 갱신 ----------
   슬라이더를 드래그하는 동안에는 #main 을 통째로 다시 그릴 수 없다.
   잡고 있던 노드가 사라지면 브라우저가 드래그를 놓아버리기 때문이다.
   그래서 슬라이더가 들어있는 카드는 건드리지 않고 출력 영역만 갈아끼운다.
   출력 HTML 은 최초 렌더와 같은 함수로 만들어야 둘이 어긋나지 않는다. */
export function setHTML(id, html) {
  const el = document.getElementById(id);
  if (el && el.innerHTML !== html) el.innerHTML = html;
}

export function setText(id, text) {
  const el = document.getElementById(id);
  if (el && el.textContent !== text) el.textContent = text;
}

/**
 * 슬라이더의 min/max 처럼 다른 슬라이더 때문에 범위가 달라지는 속성을 고친다.
 * 지금 드래그 중인 노드(`except`)는 값이 튀므로 반드시 건너뛴다.
 * 크롬은 range 의 input 이벤트를 포커스 이동보다 먼저 쏘는 경우가 있어
 * `document.activeElement` 로는 "지금 잡고 있는 슬라이더"를 알 수 없다.
 * 그래서 판단하지 않고 이벤트 대상을 그대로 넘겨받는다.
 */
export function setAttr(sel, name, value, except) {
  const el = document.querySelector(sel);
  if (!el || el === except) return;
  if (el.getAttribute(name) !== String(value)) el.setAttribute(name, String(value));
}

/* 경고의 route 별칭 → 버튼 문구.
   warnings() 가 내는 route 를 사람이 읽는 말로 옮긴다.
   홈·알림 모달·지출 한도 세 곳이 같은 문구를 쓰도록 한 곳에 둔다. */
export const WARN_ACTION = {
  limit: '한도 보기',
  tx: '내역 보기',
  debt: '상환 전략 보기',
  assets: '자산 보기',
};
