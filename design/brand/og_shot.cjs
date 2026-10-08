// og.html → png/og-1730x909.png(앱 public/og.png 와 같은 파일). gen_brand.py 뒤에 돌린다.
// 환경변수: NAVI_UI_PLAYWRIGHT_MODULE(playwright 경로) · NAVI_UI_BROWSER(크로미움 실행 파일) — design/canvas/_tools/ba_shot.cjs 와 같음.
const path = require('node:path');
const { chromium } = require(process.env.NAVI_UI_PLAYWRIGHT_MODULE);
(async () => {
  const browser = await chromium.launch({ headless: true, executablePath: process.env.NAVI_UI_BROWSER, args: ['--no-proxy-server'] });
  const page = await (await browser.newContext({ viewport: { width: 1730, height: 909 }, deviceScaleFactor: 1 })).newPage();
  await page.goto('file://' + path.join(__dirname, 'og.html'), { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  await page.screenshot({ path: path.join(__dirname, 'png/og-1730x909.png') });
  await browser.close();
  console.log('wrote png/og-1730x909.png');
})();
