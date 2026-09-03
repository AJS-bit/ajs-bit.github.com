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

// 2-1) 가장 급한 경고는 홈에서 바로 보여야 한다
//      예전에는 벨 배지 뒤에만 있어서 홈이 "지금 뭘 해야 하나"에 답하지 못했다.
const homeAlert = p.locator('#main > .alert').first();
ok('홈에 최상위 경고 노출', await homeAlert.count() === 1);
const alertText = await homeAlert.innerText();
ok('경고 제목과 근거가 함께 나옴', alertText.length > 20, alertText.split('\n')[1] || '');
ok('나머지 건수로 모달 연결', (await homeAlert.locator('[data-act="all-warnings"]').count()) === 1);
await homeAlert.locator('[data-act="all-warnings"]').click(); await p.waitForSelector('.modal__box');
ok('더보기 → 알림 모달', (await p.locator('.modal .alert').count()) >= 3);
await p.click('.modal__hd [data-close]'); await p.waitForTimeout(300);

// 2-2) 경고에서 조치할 곳으로 갈 수 있어야 한다
//      예전에는 홈·알림 모달·지출 한도 셋 다 링크가 없어 전부 막다른 길이었다.
const where = () => p.evaluate(() => ({
  tab: document.querySelector('.nav button.is-on')?.innerText.trim(),
  sub: document.querySelector('#main .tabs button.is-on')?.innerText.trim(),
}));
const actBtn = p.locator('#main > .alert').first().locator('button[data-nav]');
ok('홈 경고에 조치 버튼', await actBtn.count() === 1, await actBtn.innerText().catch(() => ''));
await actBtn.click(); await p.waitForTimeout(600);
const dest = await where();
ok('조치 버튼이 해당 화면으로 이동', dest.tab === '자산' && dest.sub === '상환 전략',
  `${dest.tab}·${dest.sub}`);

// 알림 모달의 버튼은 한 번의 클릭으로 모달을 닫으며 이동해야 한다
await p.click('[data-act=notifications]'); await p.waitForSelector('.modal__box');
await p.locator('.modal .alert button[data-nav]').first().click(); await p.waitForTimeout(700);
ok('모달 버튼 클릭 시 모달이 닫힘', (await p.locator('.modal__box').count()) === 0);
ok('모달에서도 해당 화면으로 이동', (await where()).tab === '자산');

// 지출·한도는 그 경고를 조치하는 자리다. 같은 곳으로 보내는 링크는 없어야 한다
await p.click('.nav button:has-text("지출")'); await p.waitForTimeout(250);
await p.click('.tabs button:has-text("한도")'); await p.waitForTimeout(500);
const limitLinks = await p.evaluate(() => {
  const c = [...document.querySelectorAll('.card')]
    .find((x) => x.querySelector('h3')?.innerText.includes('소비 경고'));
  return [...c.querySelectorAll('.alert')].map((a) => a.querySelector('button[data-nav]')?.dataset.nav || null);
});
ok('지출·한도에서 limit 경고엔 링크 없음', !limitLinks.includes('limit'), JSON.stringify(limitLinks));
ok('다른 화면 경고엔 링크 있음', limitLinks.some((x) => x && x !== 'limit'));
await p.click('.nav button:has-text("홈")'); await p.waitForTimeout(400);

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
