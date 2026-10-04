// 아트보드 전 · 후 넘침 비교. node ba_overflow.cjs <목록.json> <결과.json>
// 목록: ["Future", "DarkFuture", ...] (design/canvas/<이름>.dc.html). 전 = git HEAD, 후 = 작업 트리.
// 환경변수: NAVI_UI_PLAYWRIGHT_MODULE(playwright 경로) · NAVI_UI_BROWSER(크로미움 실행 파일).
// 결과: 장마다 maxBottom · maxRight(맨 아래 · 맨 오른쪽 위치)와 잘린 칸 · nowrap 넘침의 글자 서명 목록.
// 주의: '새로 잘림'은 글자 서명(앞 28자)을 견주므로 낱말이 바뀐 칸은 오탐이 난다 — scrollWidth · scrollHeight 로 다시 잴 것.
const fs = require('node:fs'), path = require('node:path'), os = require('node:os');
const { execFileSync } = require('node:child_process');
const { chromium } = require(process.env.NAVI_UI_PLAYWRIGHT_MODULE);
const REPO = path.resolve(__dirname, '../../..');
const CANVAS = path.join(REPO, 'design/canvas');
const sizes = Object.fromEntries(JSON.parse(fs.readFileSync(path.join(CANVAS, 'canvas.json'), 'utf8')).artboards.map((a) => [a.file, [a.w, a.h]]));
const names = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'ovf-'));
function standalone(text, w, h) {
  const helm = text.match(/<helmet>([\s\S]*?)<\/helmet>/)[1];
  const body = text.match(/<\/helmet>([\s\S]*?)<\/x-dc>/)[1];
  return `<!doctype html><html><head><meta charset="utf-8">${helm}\n<style>html,body{margin:0;background:#fff}.frame{width:${w}px;height:${h}px;overflow:hidden;position:relative}</style></head><body><div class="frame">${body}</div></body></html>`;
}
const MEASURE = () => {
  const frame = document.querySelector('.frame');
  const fr = frame.getBoundingClientRect();
  let maxBottom = 0, maxRight = 0; const clipped = [], nowrap = [];
  const sig = (el) => el.tagName.toLowerCase() + ':' + (el.textContent || '').trim().replace(/\s+/g, ' ').slice(0, 28);
  for (const el of frame.querySelectorAll('*')) {
    const r = el.getBoundingClientRect();
    if (r.width === 0 && r.height === 0) continue;
    const cs = getComputedStyle(el);
    if (cs.position !== 'fixed') { maxBottom = Math.max(maxBottom, r.bottom - fr.top); maxRight = Math.max(maxRight, r.right - fr.left); }
    if (cs.overflow !== 'visible' && (el.scrollWidth > el.clientWidth + 1 || el.scrollHeight > el.clientHeight + 1) && el !== frame) clipped.push(sig(el));
    if (cs.whiteSpace === 'nowrap' && el.scrollWidth > el.clientWidth + 1 && el.children.length === 0) nowrap.push(sig(el));
  }
  return { maxBottom: Math.round(maxBottom * 10) / 10, maxRight: Math.round(maxRight * 10) / 10, clipped, nowrap };
};
(async () => {
  const browser = await chromium.launch({ headless: true, executablePath: process.env.NAVI_UI_BROWSER, args: ['--no-proxy-server'] });
  const results = {};
  let idx = 0;
  const work = async () => {
    const page = await (await browser.newContext()).newPage();
    while (idx < names.length) {
      const name = names[idx++];
      const file = `${name}.dc.html`;
      const [w, h] = sizes[file] || [390, 844];
      const rel = `design/canvas/${file}`;
      let before = '';
      try { before = execFileSync('git', ['-C', REPO, 'show', `HEAD:${rel}`], { encoding: 'utf8', maxBuffer: 1 << 28 }); } catch { results[name] = { error: 'no HEAD version' }; continue; }
      const after = fs.readFileSync(path.join(REPO, rel), 'utf8');
      const out = { w, h };
      for (const [k, text] of [['before', before], ['after', after]]) {
        const p = path.join(tmp, `${name}.${k}.html`);
        fs.writeFileSync(p, standalone(text, w, h));
        try {
          await page.goto('file://' + p, { waitUntil: 'load', timeout: 20000 });
          await page.evaluate(() => document.fonts.ready);
          await page.waitForTimeout(500);
          out[k] = await page.evaluate(MEASURE);
        } catch (e) { out[k] = { error: String(e).slice(0, 80) }; }
      }
      results[name] = out;
      process.stdout.write('.');
    }
    await page.context().close();
  };
  await Promise.all([work(), work(), work()]);
  await browser.close();
  fs.writeFileSync(process.argv[3], JSON.stringify(results));
  console.log('\ndone', Object.keys(results).length);
})().catch((e) => { console.error('FAIL', e); process.exit(1); });
