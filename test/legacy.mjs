/* 구형 브라우저에서 빈 화면이 되지 않는가.

   이 앱의 js/ 는 ES2020(옵셔널 체이닝 ?. · 널 병합 ??)을 190곳 남짓 쓴다.
   지원하지 않는 엔진에서는 모듈이 **파싱 단계에서** 죽어 아무 코드도 실행되지
   않는다. type="module" 자체는 Chrome 61부터 인식하므로 nomodule 대체도 걸리지
   않아, 상단바만 남은 빈 화면이 된다.

   안드로이드 WebView 66(Chrome 66, 2018)에서 실제로 그랬다 — APK 를 만들어
   에뮬레이터에 올렸더니 본문이 통째로 비었고 콘솔에만
   "Uncaught SyntaxError: Unexpected token ." 이 찍혀 있었다.

   index.html 의 고전 스크립트가 문법 지원을 직접 재서 이유를 알려주는지 본다.
   구형 엔진을 흉내내기 위해 new Function 을 문법 검사에서 던지도록 바꿔 끼운다. */
import { chromium } from 'playwright';

const URL = process.env.URL || 'http://localhost:8000';
const errs = [];
const b = await chromium.launch({ executablePath: process.env.CHROMIUM || undefined });
const p = await b.newPage({ viewport: { width: 390, height: 844 } });
p.on('pageerror', (e) => errs.push('PAGEERROR: ' + e.message));

let pass = 0, fail = 0;
const t = (ok, name, extra = '') => { ok ? pass++ : fail++; console.log(`  ${ok ? 'PASS' : 'FAIL'}  ${name}${extra ? '  ' + extra : ''}`); };

// 옵셔널 체이닝을 모르는 엔진 흉내 — index.html 의 검사가 쓰는 통로를 막는다
await p.addInitScript(() => {
  const Real = Function;
  window.Function = function (...args) {
    if (typeof args[args.length - 1] === 'string' && args[args.length - 1].includes('?.')) {
      throw new SyntaxError('Unexpected token .');
    }
    return new Real(...args);
  };
  window.Function.prototype = Real.prototype;
});

await p.goto(URL + '/', { waitUntil: 'domcontentloaded' });
await p.waitForTimeout(400);

const txt = await p.evaluate(() => document.getElementById('main').innerText);
t(txt.includes('브라우저가 오래되었습니다'), '구형 엔진에서 빈 화면 대신 이유를 보여준다', txt.split('\n')[1] || '(비어 있음)');
t(txt.includes('WebView'), '안드로이드에서 무엇을 업데이트해야 하는지 알려준다');
t(txt.trim().length > 40, '안내가 실제로 렌더링됐다', `${txt.trim().length}자`);

// 최신 엔진에서는 이 안내가 나오면 안 된다 (평소 화면을 가리면 안 되므로)
const p2 = await b.newPage({ viewport: { width: 390, height: 844 } });
p2.on('pageerror', (e) => errs.push('PAGEERROR(modern): ' + e.message));
await p2.goto(URL + '/', { waitUntil: 'networkidle' });
await p2.waitForTimeout(400);
const modern = await p2.evaluate(() => document.getElementById('main').innerText);
t(!modern.includes('브라우저가 오래되었습니다'), '최신 엔진에서는 안내가 뜨지 않는다');
t(modern.includes('순자산 대비 소비율'), '최신 엔진에서는 평소 온보딩이 뜬다');

// --- 하한을 넘는 문법이 새로 들어오지 않았는가 ---
// 이 앱의 하한은 Chrome 80(옵셔널 체이닝 · 널 병합)이다. 그보다 높은 문법이
// 한 줄이라도 섞이면 index.html 의 검사를 통과한 브라우저에서 여전히 빈 화면이
// 된다. 실제로 `||=`(Chrome 85) 한 줄 때문에 안드로이드 11(WebView 83)에서
// spending.js 가 통째로 죽었다.
import { readFileSync, readdirSync, statSync } from 'fs';
const walk = (d) => readdirSync(d).flatMap((f) => {
  const p = `${d}/${f}`;
  return statSync(p).isDirectory() ? walk(p) : p.endsWith('.js') ? [p] : [];
});
const strip = (src) => src.replace(/\/\*[\s\S]*?\*\//g, '').replace(/^\s*\/\/.*$/gm, '');
const tooNew = [];
for (const f of walk('./js')) {
  const src = strip(readFileSync(f, 'utf8'));
  src.split('\n').forEach((line, i) => {
    if (/(\?\?=|\|\|=|&&=)/.test(line)) tooNew.push(`${f}:${i + 1} 논리 할당(Chrome 85)`);
    if (/\.replaceAll\(/.test(line)) tooNew.push(`${f}:${i + 1} String.replaceAll(Chrome 85)`);
    if (/\.at\(-?\d/.test(line)) tooNew.push(`${f}:${i + 1} Array.at(Chrome 92)`);
    if (/Object\.hasOwn|structuredClone|toSorted\(|findLast\(/.test(line)) tooNew.push(`${f}:${i + 1} Chrome 93+ API`);
  });
}
t(tooNew.length === 0, 'Chrome 80 을 넘는 문법이 없다', tooNew.join(' · ') || '0건');

console.log(`\n  ${pass} PASS / ${fail} FAIL`);
console.log('ERRORS:', errs.length ? errs.join('\n') : 'none');
await b.close();
process.exit(fail || errs.length ? 1 : 0);
