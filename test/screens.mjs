import { chromium } from 'playwright';

const OUT = process.env.OUT || './test/out';   // 스크린샷 저장 위치
const URL = process.env.URL || 'http://localhost:8000';
const errs = [];
const browser = await chromium.launch({ executablePath: process.env.CHROMIUM || undefined });
const page = await browser.newPage({ viewport: { width: 420, height: 900 } });
page.on('console', (m) => { if (m.type() === 'error') errs.push('CONSOLE: ' + m.text()); });
page.on('pageerror', (e) => errs.push('PAGEERROR: ' + e.message));

await page.goto(URL + '/', { waitUntil: 'networkidle' });
console.log('title:', await page.title());
console.log('onboarding visible:', await page.locator('text=순자산 대비 소비율로 관리하세요').isVisible());

// 예시 데이터 로드
await page.click('button:has-text("예시 데이터로 둘러보기")');
await page.waitForTimeout(600);
console.log('순자산(요약칸):', await page.locator('.summary .v').first().innerText());
console.log('목표 히어로:', await page.locator('.hero__name span').first().innerText());
console.log('링 중앙(남은기간):', await page.locator('.hero svg text').nth(1).textContent());
console.log('알림 배지:', await page.locator('#bell-badge').textContent(), '| 숨김:', await page.locator('#bell-badge').isHidden());

const shots = [];
async function shot(name) { await page.waitForTimeout(350); await page.screenshot({ path: `${OUT}/shot-${name}.png`, fullPage: true }); shots.push(name); }

await shot('01-home');

const routes = [
  ['자산', ['자산','부채','상환 전략']],
  ['지출', ['이번 달','내역','한도']],
  ['목표', ['내 목표','시뮬레이션','미래 예측']],
  ['코치', ['코칭','가정해보기','데이터']],
];
let i = 2;
for (const [nav, tabs] of routes) {
  await page.click(`.nav button:has-text("${nav}")`);
  await page.waitForTimeout(300);
  for (const t of tabs) {
    await page.click(`.tabs button:has-text("${t}")`);
    await shot(`${String(i++).padStart(2,'0')}-${nav}-${t}`);
  }
}
console.log('shots:', shots.length);
console.log('ERRORS:', errs.length ? errs.join('\n') : 'none');
await browser.close();
