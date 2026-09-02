import { chromium } from 'playwright';

const OUT = process.env.OUT || './test/out';   // 스크린샷 저장 위치
const URL = process.env.URL || 'http://localhost:8000';
const errs = [];
const b = await chromium.launch({ executablePath: process.env.CHROMIUM || undefined });
const p = await b.newPage({ viewport: { width: 420, height: 900 } });
p.on('pageerror', e => errs.push('PAGEERROR: ' + e.message));
p.on('console', m => { if (m.type() === 'error') errs.push('CONSOLE: ' + m.text()); });
const ok = (n, c) => console.log((c ? '  PASS  ' : '  FAIL  ') + n);

await p.goto(URL + '/', { waitUntil: 'networkidle' });

// --- 1. 빈 상태에서 자산 직접 추가 ---
await p.click('button:has-text("자산 추가하기")');
await p.waitForSelector('.modal__box');
await p.fill('#f_name', '월급통장');
await p.fill('#f_value', '12000000');
await p.click('.modal button[type=submit]');
await p.waitForTimeout(400);
ok('자산 추가 후 순자산 표시', (await p.locator('.summary .v').first().innerText()).includes('1,200만'));

// --- 2. 지출 입력 ---
await p.click('.fab');
await p.waitForSelector('.modal__box');
await p.fill('#f_amount', '45000');
await p.selectOption('#f_category', '식비');
await p.click('.modal button[type=submit]');
await p.waitForTimeout(400);
const burn = await p.locator('.card:has-text("소비율") svg text.gauge__v').first().textContent().catch(()=>'');
ok('지출 입력 후 소비율 계산됨', burn.includes('%'));
console.log('        소비율 게이지:', burn);

// --- 3. 금액 입력 천단위 콤마 ---
await p.click('.fab'); await p.waitForSelector('.modal__box');
await p.fill('#f_amount', '1234567');
const shown = await p.inputValue('#f_amount');
ok('금액 콤마 포맷', shown === '1,234,567');
await p.click('.modal__hd [data-close]'); await p.waitForTimeout(200);

// --- 4. 설정에서 월급 입력 ---
await p.click('.topbar [data-act=settings]');
await p.waitForSelector('.modal__box');
await p.fill('#f_monthlyIncome', '3500000');
await p.click('.modal button[type=submit]');
await p.waitForTimeout(400);
ok('월급 대비 요약칸 등장', await p.locator('.summary >> text=월급 대비').first().isVisible());

// --- 5. 기본 목표 한 번에 만들기 ---
await p.click('.nav button:has-text("목표")'); await p.waitForTimeout(300);
await p.click('button:has-text("추천 목표 한 번에 만들기")'); await p.waitForTimeout(500);
const goalCount = await p.locator('.card:has-text("필요 월 저축")').count();
ok('기본 목표 생성됨 (' + goalCount + '개)', goalCount >= 2);

// --- 6. 시뮬레이션 슬라이더 ---
await p.click('.tabs button:has-text("시뮬레이션")'); await p.waitForTimeout(300);
const before = await p.locator('text=/현재 저축액으로 달성 시점/').locator('..').locator('.v').innerText();
await p.click('button[data-sim-set=target][data-v="500000000"]'); await p.waitForTimeout(400);
const after = await p.locator('text=/현재 저축액으로 달성 시점/').locator('..').locator('.v').innerText();
ok('시뮬레이션 목표 변경 반영 (' + before + ' → ' + after + ')', before !== after);

// --- 7. 미래 예측 슬라이더 ---
await p.click('.tabs button:has-text("미래 예측")'); await p.waitForTimeout(300);
const n1 = await p.locator('.big.num').first().innerText();
await p.locator('input[data-fc=years]').fill('35');
await p.dispatchEvent('input[data-fc=years]', 'input');
await p.waitForTimeout(400);
const n2 = await p.locator('.big.num').first().innerText();
ok('예측 기간 변경 반영 (' + n1 + ' → ' + n2 + ')', n1 !== n2);

// --- 8. 테마 전환 ---
await p.click('[data-act=settings]'); await p.waitForSelector('.modal__box');
await p.click('.modal label:has-text("라이트")');
await p.click('.modal button[type=submit]'); await p.waitForTimeout(400);
ok('설정에서 라이트 테마 전환', await p.evaluate(() => document.documentElement.dataset.theme) === 'light');
await p.screenshot({ path: OUT + '/light.png' });

// --- 9. 새로고침 후 데이터 유지 ---
await p.reload({ waitUntil: 'networkidle' }); await p.waitForTimeout(500);
const persisted = await p.evaluate(() => { const d = JSON.parse(localStorage.getItem('asset-compass.v1'));
  return { assets: d.assets.length, tx: d.transactions.length, goals: d.goals.length, income: d.profile.monthlyIncome }; });
ok('localStorage 영속화 ' + JSON.stringify(persisted),
   persisted.assets === 1 && persisted.tx >= 1 && persisted.goals === 4 && persisted.income === 3500000);
await p.click('.nav button:has-text("홈")'); await p.waitForTimeout(300);
ok('새로고침 후 홈 순자산 유지', (await p.locator('.summary .v').first().innerText()).includes('만'));

// --- 10. 키보드 단축키 ---
await p.keyboard.press('3'); await p.waitForTimeout(300);
ok('숫자키 네비게이션', await p.locator('.nav button:has-text("지출")').getAttribute('class') === 'is-on');

console.log('\nERRORS:', errs.length ? errs.join('\n') : 'none');
await b.close();
