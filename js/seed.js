/* 예시 데이터 — 앱을 바로 체험해 볼 수 있는 가상의 30대 직장인 프로필 */
import { blankState } from './store.js';
import { uid, monthKey, addMonths } from './format.js';

const PATTERN = [
  ['식비', 420000, 14], ['카페/간식', 78000, 9], ['교통', 95000, 6],
  ['주거/관리', 620000, 1], ['통신', 62000, 1], ['보험', 140000, 1],
  ['구독', 34900, 3], ['쇼핑', 260000, 4], ['문화/여가', 145000, 4],
  ['의료/건강', 62000, 2], ['경조사', 100000, 1], ['기타', 70000, 3],
];

function monthTx(key, scale = 1) {
  const out = [];
  const dim = new Date(Number(key.slice(0, 4)), Number(key.slice(5, 7)), 0).getDate();
  for (const [cat, total, count] of PATTERN) {
    const amt = (total * scale) / count;
    for (let i = 0; i < count; i++) {
      // 1일부터 말일까지 고르게. 고정비(count=1)는 1일에 빠지도록 한다.
      const day = count === 1 ? 1 : Math.min(dim, 1 + Math.round((i / count) * (dim - 1)));
      out.push({
        id: uid(),
        date: `${key}-${String(day).padStart(2, '0')}`,
        amount: Math.round((amt * (0.8 + ((i * 37) % 40) / 100)) / 100) * 100,
        category: cat,
        memo: '',
      });
    }
  }
  return out;
}

export function demoState() {
  const s = blankState();
  const cur = monthKey();

  s.profile = {
    ...s.profile,
    nickname: '',
    monthlyIncome: 3_600_000,
    extraIncome: 200_000,
    riskProfile: 'balanced',
    expectedReturn: 0.06,
    inflation: 0.025,
    targetBurn: 1.8,
    emergencyMonths: 6,
  };

  s.assets = [
    { id: uid(), name: '주거래 통장', type: 'cash', value: 6_400_000 },
    { id: uid(), name: 'CMA 비상금', type: 'cash', value: 8_200_000 },
    { id: uid(), name: '해외 ETF 계좌', type: 'investment', value: 24_500_000, returnRate: 7.5 },
    { id: uid(), name: '국내 주식', type: 'investment', value: 9_800_000, returnRate: 5 },
    { id: uid(), name: '연금저축펀드', type: 'pension', value: 13_200_000 },
    { id: uid(), name: '전세보증금', type: 'realestate', value: 120_000_000, returnRate: 0 },
  ];

  s.debts = [
    { id: uid(), name: '전세자금대출', type: 'mortgage', balance: 80_000_000, rate: 3.6, minPayment: 240_000 },
    { id: uid(), name: '마이너스통장', type: 'credit', balance: 6_500_000, rate: 6.9, minPayment: 200_000 },
    { id: uid(), name: '카드 할부', type: 'card', balance: 2_100_000, rate: 14.5, minPayment: 350_000 },
  ];

  s.transactions = [];
  for (let i = 0; i <= 4; i++) {
    const k = addMonths(cur, -i);
    // 이번 달은 경과일까지만, 과거는 전체
    const scale = 1 + ((i * 7) % 13) / 100 - 0.05;
    const tx = monthTx(k, scale);
    s.transactions.push(...(i === 0 ? tx.filter((t) => t.date <= new Date().toISOString().slice(0, 10)) : tx));
  }
  s.transactions.sort((a, b) => (a.date < b.date ? 1 : -1));

  const assetsSum = s.assets.reduce((t, a) => t + a.value, 0);
  const debtsSum = s.debts.reduce((t, d) => t + d.balance, 0);

  s.goals = [
    { id: uid(), name: '비상금 6개월', emoji: '🧯', target: 13_000_000, targetDate: dateAfter(18), priority: 1, saved: 8_200_000, kind: 'preset' },
    { id: uid(), name: '카드·마통 완전상환', emoji: '🏔️', target: 8_600_000, targetDate: dateAfter(36), priority: 1, saved: 0, kind: 'preset' },
    { id: uid(), name: '순자산 1억', emoji: '💎', target: 100_000_000, targetDate: dateAfter(84), priority: 2, saved: assetsSum - debtsSum, kind: 'preset' },
    { id: uid(), name: '내 집 마련 종잣돈', emoji: '🏠', target: 200_000_000, targetDate: dateAfter(180), priority: 3, saved: 0, kind: 'preset' },
  ];

  s.snapshots = [];
  for (let i = 11; i >= 0; i--) {
    const k = addMonths(cur, -i);
    const drift = 1 - i * 0.021;
    s.snapshots.push({
      month: k,
      assets: Math.round(assetsSum * drift),
      debts: Math.round(debtsSum * (1 + i * 0.004)),
      net: Math.round(assetsSum * drift - debtsSum * (1 + i * 0.004)),
    });
  }

  s.settings = { ...s.settings, onboarded: true, debtStrategy: 'avalanche', extraDebtPay: 300_000 };
  return s;
}

function dateAfter(months) {
  const d = new Date();
  d.setMonth(d.getMonth() + months);
  return d.toISOString().slice(0, 10);
}
