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
