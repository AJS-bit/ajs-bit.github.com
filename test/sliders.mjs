import { chromium } from 'playwright';

const OUT = process.env.OUT || './test/out';   // 스크린샷 저장 위치
const URL = process.env.URL || 'http://localhost:8000';
const b = await chromium.launch({ executablePath: process.env.CHROMIUM || undefined });
const p = await b.newPage({ viewport: { width: 420, height: 1600 } });
await p.goto(URL + '/', { waitUntil: 'networkidle' });
await p.click('button:has-text("예시 데이터로 둘러보기")'); await p.waitForTimeout(700);

// 실제 마우스 드래그를 흉내내고, 드래그 도중에 값이 바뀌는지 본다
async function realDrag(name, sliderSel, readSel, goTo) {
  const el = p.locator(sliderSel).first();
  if (!await el.count()) { console.log(`${name}: 슬라이더 없음`); return; }
  await el.evaluate((n) => n.scrollIntoView({ block: 'center' })); await new Promise(r=>setTimeout(r,150));
  const box = await el.boundingBox();
  const before = await p.locator(readSel).first().textContent().catch(()=>null);

  await p.mouse.move(box.x + box.width * 0.3, box.y + box.height / 2);
  await p.mouse.down();
  // 드래그를 여러 구간으로 나눠 각 지점의 값을 수집한다
  const samples = [];
  for (const f of [0.45, 0.6, 0.75, goTo]) {
    await p.mouse.move(box.x + box.width * f, box.y + box.height / 2, { steps: 4 });
    await p.waitForTimeout(90);
    samples.push(await p.locator(readSel).first().textContent().catch(()=>null));
  }
  const during = samples[samples.length - 1];
  const distinct = new Set(samples).size;
  await p.mouse.up();
  await p.waitForTimeout(300);
  const after = await p.locator(readSel).first().textContent().catch(()=>null);

  const live = distinct > 1;
  console.log(`${live ? '  연속추적 O ' : '  연속추적 X '} ${name}  (드래그 중 서로 다른 값 ${distinct}종)`);
  console.log(`      ${before} → [${samples.join(' → ')}] → 놓은뒤 ${after}`);
}

await realDrag('홈 · 소비 시나리오', '[data-scenario=spend]', '#burn-spend', 0.8);

await p.click('.nav button:has-text("자산")'); await p.waitForTimeout(250);
await p.click('.tabs button:has-text("상환 전략")'); await p.waitForTimeout(350);
await realDrag('상환전략 · 추가 상환액', '[data-act=extra-pay]', '.stat:nth-child(2) .v', 0.85);

await p.click('.nav button:has-text("목표")'); await p.waitForTimeout(250);
await p.click('.tabs button:has-text("시뮬레이션")'); await p.waitForTimeout(350);
await realDrag('시뮬레이션 · 목표 기간', '[data-sim=years]', '.card:has-text("결과") .stat:nth-child(3) .v', 0.8);

await p.click('.tabs button:has-text("미래 예측")'); await p.waitForTimeout(350);
await realDrag('미래예측 · 예측 기간', '[data-fc=years]', '.big.num', 0.85);

await p.click('.nav button:has-text("코치")'); await p.waitForTimeout(250);
await p.click('.tabs button:has-text("가정해보기")'); await p.waitForTimeout(350);
await realDrag('가정해보기 · 절감률', '[data-whatif=cutPct]', '.stat .v', 0.8);

await b.close();
