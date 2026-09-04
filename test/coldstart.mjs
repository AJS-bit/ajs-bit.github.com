/* 콜드 스타트 검증 — 첫 사용자가 보는 화면.
   못 재는 항목에 점수를 주면 안 된다. 예전에는 각 항목이 값을 못 구할 때
   넉넉한 기본값으로 대체해서, 자산 하나만 넣은 사용자가 75점 '우수' 와
   '완전자립' 등급을 받았다. 기록할 이유를 앱이 스스로 없애는 상태였다. */
import { chromium } from 'playwright';

const URL = process.env.URL || 'http://localhost:8000';
const errs = [];
const b = await chromium.launch({ executablePath: process.env.CHROMIUM || undefined });
const p = await b.newPage({ viewport: { width: 390, height: 844 } });
p.on('console', (m) => { if (m.type() === 'error') errs.push('CONSOLE: ' + m.text()); });
p.on('pageerror', (e) => errs.push('PAGEERROR: ' + e.message));

let pass = 0, fail = 0;
const t = (ok, name, extra = '') => { ok ? pass++ : fail++; console.log(`  ${ok ? 'PASS' : 'FAIL'}  ${name}${extra ? '  ' + extra : ''}`); };

const snap = () => p.evaluate(async () => {
  const { state } = await import('/js/store.js');
  const { metrics } = await import('/js/finance.js');
  const m = metrics(state);
  return { burnAnnual: m.burnAnnual, grade: m.grade.label, total: m.score.total,
    tier: m.score.tier.label, ready: m.score.ready,
    parts: m.score.parts.map((x) => ({ label: x.label, score: Math.round(x.score), measured: x.measured })) };
});

await p.goto(URL + '/', { waitUntil: 'networkidle' });
await p.evaluate(() => localStorage.clear());
await p.reload({ waitUntil: 'networkidle' }); await p.waitForTimeout(500);

// 자산 1건만 입력한, 가장 흔한 첫 사용자 상태
await p.click('button:has-text("자산 추가하기")'); await p.waitForTimeout(500);
await p.fill('#f_name', '월급통장');
await p.fill('#f_value', '30000000');
await p.click('.modal__box button[type=submit]'); await p.waitForTimeout(800);

const cold = await snap();
t(cold.burnAnnual === null, '지출 기록이 없으면 소비율은 0%가 아니라 측정 불가', `burnAnnual=${cold.burnAnnual}`);
t(cold.grade === '측정 불가', '등급이 완전자립으로 나오지 않는다', `등급=${cold.grade}`);
t(cold.ready === false, '점수가 아직 준비되지 않았음을 알린다');
t(cold.tier === '측정 준비 중', '등급 라벨이 우수/탁월이 아니다', `tier=${cold.tier}`);
const burnPart = cold.parts.find((x) => x.label === '자산 대비 소비');
t(burnPart.measured === false && burnPart.score === 0, '지출 미입력 항목은 0점', `${burnPart.score}점`);
const savePart = cold.parts.find((x) => x.label === '저축률');
t(savePart.measured === false && savePart.score === 0, '수입 미입력 항목은 0점', `${savePart.score}점`);
t(cold.total < 35, '총점이 우수 구간에 들지 않는다', `${cold.total}점`);
t((await p.locator('.summary button:has-text("성장 점수") .v').innerText()).trim() === '—', '홈에 숫자 대신 —');
t((await p.locator('.summary button:has-text("성장 점수") .s').innerText()).includes('입력'), '무엇을 넣어야 하는지 알려준다');

// 홈 한도 카드가 근거를 밝히는가 — 40만원이 어디서 나온 숫자인지
const homeText = await p.evaluate(() => document.getElementById('main').innerText);
t(/목표 소비율 \d+\.\d% 기준입니다/.test(homeText), '홈 한도 카드가 계산 근거를 밝힌다');
t(homeText.includes('월 실수령액을 넣으면'), '수입을 넣으면 정확해진다고 알린다');

// 지출·이번 달이 0.00% 라고 단정하지 않는가 (0% 는 4% 룰 최고 등급으로 읽힌다)
await p.click('.nav button:has-text("지출")'); await p.waitForTimeout(450);
const spendText = await p.evaluate(() => document.getElementById('main').innerText);
t(!spendText.includes('0.00%'), '기록 0건에서 소비율을 0.00% 로 단정하지 않는다');
t(spendText.includes('기록 후 계산'), '지출 탭도 홈과 같이 측정 불가를 말한다');
await p.click('.nav button:has-text("홈")'); await p.waitForTimeout(400);

// 코치가 침묵하지 않고 다음 행동을 알려주는가
await p.click('.nav button:has-text("코치")'); await p.waitForTimeout(500);
const coachText = await p.evaluate(() => document.getElementById('main').innerText);
t(coachText.includes('지출을 기록'), '코치가 지출 기록을 안내한다');
t(!coachText.includes('완전자립'), '코치가 완전자립이라고 말하지 않는다');

// 지출을 한 건 넣으면 점수가 살아나는가
await p.click('.nav button:has-text("지출")'); await p.waitForTimeout(400);
await p.click('[data-act="quick-add"], .fab'); await p.waitForTimeout(600);
await p.fill('#f_amount', '300000');
await p.click('.modal__box button[type=submit]'); await p.waitForTimeout(900);
const warm = await snap();
t(warm.ready === true, '지출 한 건으로 점수 측정이 시작된다');
t(warm.burnAnnual !== null, '소비율이 계산된다', `연 ${warm.burnAnnual?.toFixed(1)}%`);

console.log(`\n  ${pass} PASS / ${fail} FAIL`);
console.log('ERRORS:', errs.length ? errs.join('\n') : 'none');
await b.close();
process.exit(fail || errs.length ? 1 : 0);
