/* 부분 갱신 검증 — 슬라이더 드래그 중에는 화면을 통째로 다시 그리지 않고
   출력 영역만 갈아끼운다. 그 뒤에도 같은 카드 안의 버튼들이 살아있는지,
   라벨과 저장값이 어긋나지 않는지 본다. sliders.mjs 가 "값이 따라오는가"를
   본다면 이 스크립트는 "갈아끼운 자리가 멀쩡한가"를 본다. */
import { chromium } from 'playwright';
const URL = process.env.URL || 'http://localhost:8000';
const errs = [];
const b = await chromium.launch({ executablePath: process.env.CHROMIUM || undefined });
const p = await b.newPage({ viewport: { width: 420, height: 1400 } });
p.on('console', (m) => { if (m.type() === 'error') errs.push('CONSOLE: ' + m.text()); });
p.on('pageerror', (e) => errs.push('PAGEERROR: ' + e.message));
await p.goto(URL + '/', { waitUntil: 'networkidle' });
await p.click('button:has-text("예시 데이터로 둘러보기")'); await p.waitForTimeout(700);
let pass = 0, fail = 0;
const t = (ok, name, extra = '') => { ok ? pass++ : fail++; console.log(`  ${ok ? 'PASS' : 'FAIL'}  ${name}${extra ? '  ' + extra : ''}`); };

// --- 시뮬레이션: 부분 갱신 뒤에도 프리셋 버튼이 살아있는가
await p.click('.nav button:has-text("목표")'); await p.waitForTimeout(250);
await p.click('.tabs button:has-text("시뮬레이션")'); await p.waitForTimeout(350);
const yrs = p.locator('[data-sim=years]');
await yrs.evaluate((n) => { n.value = '25'; n.dispatchEvent(new Event('input', { bubbles: true })); });
await p.waitForTimeout(250);
t((await p.locator('#sim-v-years').textContent()) === '25년', '기간 라벨 갱신');
t((await p.locator('#sim-out').textContent()).includes('25년 뒤'), '결과 영역 갱신');
await p.click('#sim-presets button:has-text("3억")'); await p.waitForTimeout(300);
t((await p.locator('#sim-v-target').textContent()).includes('3억'), '프리셋 버튼 동작(부분갱신 후)');
t((await p.locator('#sim-presets .btn--primary').textContent()).includes('3억'), '프리셋 선택 표시');
await p.click('button:has-text("필요액으로 맞추기")'); await p.waitForTimeout(300);
t(await p.locator('[data-sim=monthly]').count() === 1, '필요액 맞추기 동작');
await p.click('button:has-text("이 시뮬레이션을 목표로 저장")'); await p.waitForTimeout(500);
t(await p.locator('.tabs button.is-on:has-text("내 목표")').count() === 1, '목표로 저장 → 목록 이동');

// --- 미래 예측
await p.click('.tabs button:has-text("미래 예측")'); await p.waitForTimeout(350);
await p.locator('[data-fc=extraSave]').evaluate((n) => { n.value = '500000'; n.dispatchEvent(new Event('input', { bubbles: true })); });
await p.waitForTimeout(250);
t((await p.locator('#fc-v-extra').textContent()).includes('500,000'), '저축추가 라벨 갱신');
t((await p.locator('#fc-help').textContent()).includes('증가'), '도움말에 증가분 표시');
t((await p.locator('#fc-out').textContent()).includes('마일스톤'), '예측 카드 영역 유지');

// --- 상환 전략: 전략 버튼이 부분 갱신 뒤에도 동작하는가
await p.click('.nav button:has-text("자산")'); await p.waitForTimeout(250);
await p.click('.tabs button:has-text("상환 전략")'); await p.waitForTimeout(350);
await p.locator('[data-act=extra-pay]').evaluate((n) => { n.value = '400000'; n.dispatchEvent(new Event('input', { bubbles: true })); });
await p.waitForTimeout(250);
t((await p.locator('#repay-extra').textContent()).includes('400,000'), '추가 상환액 라벨 갱신');
t((await p.locator('#repay-sub').textContent()).includes('400,000'), '카드 헤더 갱신');
await p.click('label[data-v="snowball"]'); await p.waitForTimeout(400);
t((await p.locator('#repay-out').textContent()).includes('잔액 작은 순'), '전략 전환 동작(부분갱신 후)');

// --- 가정해보기
await p.click('.nav button:has-text("코치")'); await p.waitForTimeout(250);
await p.click('.tabs button:has-text("가정해보기")'); await p.waitForTimeout(350);
await p.locator('[data-whatif=cutPct]').evaluate((n) => { n.value = '30'; n.dispatchEvent(new Event('input', { bubbles: true })); });
await p.waitForTimeout(250);
t((await p.locator('#whatif-pct').textContent()) === '30%', '절감률 라벨 갱신');
await p.locator('[data-act=target-burn]').evaluate((n) => { n.value = '3.0'; n.dispatchEvent(new Event('input', { bubbles: true })); });
await p.waitForTimeout(250);
t((await p.locator('#tb-pct').textContent()) === '3.0%', '목표 소비율 라벨 갱신');
t((await p.locator('#tb-annual').textContent()).includes('36.0'), '연환산 갱신');
// 놓았을 때 저장되는지
await p.locator('[data-act=target-burn]').evaluate((n) => n.dispatchEvent(new Event('change', { bubbles: true })));
await p.waitForTimeout(400);
const saved = await p.evaluate(() => JSON.parse(localStorage.getItem('asset-compass.v1') || '{}')?.profile?.targetBurn);
t(saved === 3, '목표 소비율 영속화', `targetBurn=${saved}`);

// --- 홈 소비율: 게이지가 슬라이더를 따라오는가
// 홈은 슬라이더와 출력이 한 카드에 있어 카드째 다시 그릴 수 없다. 갱신 대상을
// 손으로 짚는 방식이라 하나 빠뜨리기 쉽고, 실제로 게이지가 빠져 있었다.
await p.click('.nav button:has-text("홈")'); await p.waitForTimeout(400);
// 게이지 눈금은 목표와 무관하게 고정이다. 목표를 바꾸면 **호가 아니라 목표 눈금**이
// 움직여야 한다. 예전에는 눈금 최대값이 목표×3 이라 호가 거꾸로 줄어들었다.
const gaugeParts = () => p.evaluate(() => {
  const card = [...document.querySelectorAll('.card')].find((c) => c.querySelector('[data-burn=range]'));
  const svg = card.querySelector('svg.chart');
  return {
    arc: [...svg.querySelectorAll('path')].map((x) => x.getAttribute('d')).join('|'),
    tick: [...svg.querySelectorAll('line')].map((x) => `${x.getAttribute('x1')},${x.getAttribute('y1')}`).join('|'),
    label: [...svg.querySelectorAll('text')].map((x) => x.textContent).join('|'),
  };
});
const g0 = await gaugeParts();
const cap0 = await p.locator('#burn-cap').textContent();
t(g0.label.includes('목표'), '게이지에 목표 눈금 라벨이 있다');
await p.locator('[data-burn=range]').evaluate((n) => { n.value = '6'; n.dispatchEvent(new Event('input', { bubbles: true })); });
await p.waitForTimeout(300);
const g1 = await gaugeParts();
t((await p.locator('#burn-cap').textContent()) !== cap0, '홈 소비 상한 갱신');
t((await p.locator('[data-burn=num]').inputValue()) === '6.0', '홈 숫자칸 동기화');
t(g1.tick !== g0.tick, '목표 눈금이 슬라이더를 따라 이동한다');
t(g1.arc === g0.arc, '게이지 호는 목표와 무관하게 고정된다');

console.log(`\n  ${pass} PASS / ${fail} FAIL`);
console.log('ERRORS:', errs.length ? errs.join('\n') : 'none');
await b.close();
process.exit(fail || errs.length ? 1 : 0);
