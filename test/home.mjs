import { chromium } from 'playwright';

const OUT = process.env.OUT || './test/out';   // 스크린샷 저장 위치
const URL = process.env.URL || 'http://localhost:8000';
const errs = [];
const b = await chromium.launch({ executablePath: process.env.CHROMIUM || undefined });
const p = await b.newPage({ viewport: { width: 420, height: 1400 } });
p.on('pageerror', e => errs.push('PAGEERROR: ' + e.message));
p.on('console', m => { if (m.type()==='error') errs.push('CONSOLE: '+m.text()); });
const ok = (n, c, extra='') => console.log((c?'  PASS  ':'  FAIL  ')+n+(extra?'  '+extra:''));

await p.goto(URL + '/', { waitUntil: 'networkidle' });
await p.click('button:has-text("예시 데이터로 둘러보기")'); await p.waitForTimeout(800);

// 1) 알림 벨 배지
const badge = await p.locator('#bell-badge').textContent();
ok('알림 배지 표시', /^\d/.test(badge), '배지=' + badge);

// 2) 알림 모달
await p.click('[data-act=notifications]'); await p.waitForSelector('.modal__box');
const alerts = await p.locator('.modal .alert').count();
ok('알림 모달 경고 목록', alerts >= 3, alerts + '건');
await p.click('.modal__hd [data-close]'); await p.waitForTimeout(300);

// 3) 테마 토글이 상단바에서 사라졌는지
ok('상단바에 테마 버튼 없음', await p.locator('.topbar [data-act=theme]').count() === 0);

// 4) 설정 안에서 테마 변경
await p.click('[data-act=settings]'); await p.waitForSelector('.modal__box');
ok('설정에 테마 항목 존재', await p.locator('.modal label:has-text("화면 테마")').count() === 1);
await p.click('.modal label:has-text("라이트")');
await p.click('.modal button[type=submit]'); await p.waitForTimeout(500);
ok('설정에서 라이트 전환', await p.evaluate(() => document.documentElement.dataset.theme) === 'light');
await p.screenshot({ path: OUT + '/home-light.png', fullPage: true });

// 다시 다크로
await p.click('[data-act=settings]'); await p.waitForSelector('.modal__box');
await p.click('.modal label:has-text("다크")');
await p.click('.modal button[type=submit]'); await p.waitForTimeout(400);

// 5) 홈 소비 시나리오 — 실제 값을 바꾸지 않는 가정이어야 한다
//    예전 홈 슬라이더는 목표 소비율(%)을 조절하며 targetBurn 을 실제로 저장했다.
//    둘러보다 실수로 목표가 바뀌고, 코치 탭에도 같은 조작이 있어 헷갈렸다.
const savedBefore = await p.evaluate(() => JSON.parse(localStorage.getItem('asset-compass.v1')).profile.targetBurn);
const spendBefore = await p.locator('#burn-spend').textContent();
const gaugeV = () => p.locator('.card:has([data-scenario=spend]) text.gauge__v').textContent();
const vBefore = await gaugeV();

const sl = p.locator('[data-scenario=spend]');
const lo = await sl.getAttribute('min');
await sl.fill(lo);
await p.dispatchEvent('[data-scenario=spend]', 'input'); await p.waitForTimeout(300);
ok('슬라이더 → 소비액 갱신', (await p.locator('#burn-spend').textContent()) !== spendBefore,
  `${spendBefore} → ${await p.locator('#burn-spend').textContent()}`);
ok('게이지 바늘도 함께 움직임', (await gaugeV()) !== vBefore, `${vBefore} → ${await gaugeV()}`);

// 6) 놓아도 저장되지 않는다 (핵심)
await p.dispatchEvent('[data-scenario=spend]', 'change'); await p.waitForTimeout(400);
const savedAfter = await p.evaluate(() => JSON.parse(localStorage.getItem('asset-compass.v1')).profile.targetBurn);
ok('시나리오는 저장되지 않음', savedAfter === savedBefore, `targetBurn ${savedBefore} → ${savedAfter}`);

// 7) 초기화로 실제 예상 복귀
await p.click('[data-act="scenario-reset"]'); await p.waitForTimeout(400);
ok('현재 예상으로 초기화', (await p.locator('#burn-spend').textContent()) === spendBefore);

// 8) 홈 목표 전환
await p.click('.goal-pills button:nth-child(3)'); await p.waitForTimeout(500);
const heroName = await p.locator('.hero__name span').innerText();
ok('홈 목표 전환', heroName.includes('순자산'), '히어로=' + heroName);

// 9) 새로고침 후에도 선택 유지
await p.reload({ waitUntil: 'networkidle' }); await p.waitForTimeout(600);
ok('선택한 목표 유지', (await p.locator('.hero__name span').innerText()).includes('순자산'));

// 10) 홈 단순화 확인 (카드 수)
const cards = await p.locator('#main > section, #main > .summary').count();
ok('홈 섹션 4개 이내', cards <= 5, cards + '개 섹션');

console.log('\nERRORS:', errs.length ? errs.join('\n') : 'none');
await b.close();
