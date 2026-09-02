/* ============================================================
   소비 코치 — 온디바이스 규칙 기반 분석 엔진
   외부 전송 없이 내 데이터만으로 우선순위별 조언을 생성한다.
   각 조언은 "숫자로 된 근거 + 실행하면 얼마나 좋아지는지"를 함께 낸다.
   ============================================================ */
import { CAT, RISK } from './store.js';
import { metrics, spendingLimit, allocateGoals, monthsToTarget, simulateDebt, spendOf, avgSpend, totals } from './finance.js';
import { n, compact, addMonths, monthKey } from './format.js';

const won = (v) => Math.round(n(v)).toLocaleString('ko-KR') + '원';

/**
 * 카테고리 지출을 줄였을 때 1순위 목표 달성이 몇 개월 앞당겨지는지.
 * 이 앱의 핵심 전환 장치: 지출을 '기회비용'으로 환산한다.
 */
export function impactOfSaving(s, monthlyCut) {
  const m = metrics(s);
  const { rows } = allocateGoals(s);
  const top = rows.find((r) => n(r.goal.target) > 0);
  const ret = n(s.profile.expectedReturn);
  if (!top) {
    // 목표가 없으면 10년 뒤 자산 차이로 환산
    const g = Math.pow(1 + ret / 12, 120);
    return { kind: 'wealth', years: 10, delta: monthlyCut * ((g - 1) / (ret / 12)) };
  }
  const base = monthsToTarget(top.goal.target, top.goal.saved, top.allocated, ret);
  const better = monthsToTarget(top.goal.target, top.goal.saved, top.allocated + monthlyCut, ret);
  if (base === null || better === null) {
    const g = Math.pow(1 + ret / 12, 120);
    return { kind: 'wealth', years: 10, delta: monthlyCut * ((g - 1) / (ret / 12)) };
  }
  return { kind: 'goal', goal: top.goal, monthsSaved: Math.max(0, base - better), base, better };
}

/** 코칭 카드 생성 */
export function insights(s) {
  const m = metrics(s);
  const lim = spendingLimit(s);
  const t = totals(s);
  const alloc = allocateGoals(s);
  const cards = [];
  const add = (c) => cards.push({ priority: 3, tone: 'info', ...c });

  const hasData = m.txCount > 0 || t.assets > 0;
  if (!hasData) {
    return [{
      priority: 0, tone: 'info', icon: '🚀', title: '먼저 자산과 지출을 입력해 주세요',
      body: '자산 현황과 이번 달 지출을 넣으면 순자산 대비 소비율을 계산하고, 목표까지 남은 거리를 알려드립니다.',
      actions: [{ label: '자산 추가', route: 'assets' }, { label: '지출 기록', route: 'spending' }],
    }];
  }

  /* --- 1. 메인 지표: 순자산 대비 소비율 --- */
  if (m.burnAnnual !== null && m.net > 0) {
    const g = m.grade;
    const targetAnnual = n(s.profile.targetBurn) * 12;
    const diff = m.burnAnnual - targetAnnual;
    add({
      priority: diff > 0 ? 1 : 2,
      tone: g.tone === 'pos' ? 'good' : g.tone === 'neg' ? 'danger' : g.tone === 'warn' ? 'warn' : 'info',
      icon: '🧭', title: `소비율 ${m.burnAnnual.toFixed(1)}%/년 — ${g.label}`,
      body: diff > 0
        ? `${g.desc} 목표선(${targetAnnual.toFixed(1)}%)까지 오려면 월 소비를 ${won(Math.max(0, m.projected - (m.net * n(s.profile.targetBurn)) / 100))} 줄이거나, 순자산을 ${compact(Math.max(0, (m.projected * 12) / (targetAnnual / 100) - m.net))} 더 쌓으면 됩니다.`
        : `${g.desc} 현재 월 소비 ${won(m.projected)}는 순자산의 ${m.burn.toFixed(2)}%입니다.`,
    });
  } else if (m.net > 0 && m.projected <= 0) {
    // 지출 기록이 없으면 소비율이 '측정 불가'라 위 카드가 나오지 않는다.
    // 이 앱의 메인 지표가 비어 있는 상태이므로 무엇을 하면 되는지 알려준다.
    add({
      priority: 1, tone: 'info', icon: '🧾', title: '이번 달 지출을 기록해 주세요',
      body: `자산 ${compact(t.assets)}는 입력됐습니다. 소비율·맞춤 한도·성장 점수는 지출 기록이 있어야 계산됩니다. 한 건만 넣어도 시작됩니다.`,
      actions: [{ label: '지출 기록', act: 'quick-add' }],
    });
  } else if (m.net <= 0) {
    add({
      priority: 0, tone: 'danger', icon: '🔻', title: '순자산이 아직 마이너스입니다',
      body: `자산 ${compact(t.assets)} / 부채 ${compact(t.debts)}. 이 구간에서는 소비율보다 '부채 감소 속도'가 진짜 지표입니다. 부채 탭에서 상환 전략을 먼저 잡으세요.`,
      actions: [{ label: '부채 전략 보기', route: 'debt' }],
    });
  }

  /* --- 2. 저축률 --- */
  if (m.income > 0) {
    const sr = m.savingsRate;
    if (sr < 0) {
      add({ priority: 0, tone: 'danger', icon: '🔥', title: '적자 구조입니다',
        body: `수입 ${won(m.income)} − 소비 ${won(m.projected)} − 부채상환 ${won(m.debtPay)} = ${won(m.capacity)}. 매달 자산이 줄어듭니다.` });
    } else if (sr < 20) {
      add({ priority: 1, tone: 'warn', icon: '🪫', title: `저축률 ${sr.toFixed(0)}% — 축적 속도가 느립니다`,
        body: `저축률 30%로 올리면 월 ${won(m.income * 0.3 - m.capacity)}을 더 모읍니다. 고정비 ${won(m.fixed)}(소비의 ${m.spend > 0 ? ((m.fixed / m.spend) * 100).toFixed(0) : 0}%)부터 점검해 보세요.` });
    } else if (sr >= 40) {
      add({ priority: 2, tone: 'good', icon: '💪', title: `저축률 ${sr.toFixed(0)}% — 상위권입니다`,
        body: `월 ${won(m.capacity)}을 모으고 있습니다. 이 페이스면 연 ${compact(m.capacity * 12)}씩 순자산이 늘어납니다.` });
    }
  } else {
    add({ priority: 1, tone: 'info', icon: '📝', title: '월 실수령액을 입력해 주세요',
      body: '월급 대비 소비, 저축여력, 맞춤 한도는 실수령액이 있어야 계산됩니다.', actions: [{ label: '설정 열기', act: 'settings' }] });
  }

  /* --- 3. 한도 페이스 --- */
  if (lim.total > 0 && m.txCount > 0 && m.done < m.days) {
    const gap = m.spend - lim.pace;
    const leftDays = m.days - m.done;
    const leftBudget = lim.total - m.spend;
    add({
      priority: gap > 0 ? 1 : 3,
      tone: gap > lim.daily ? 'warn' : 'info', icon: '📅',
      title: gap > 0 ? `한도보다 ${won(gap)} 앞서 있습니다` : `한도보다 ${won(-gap)} 여유가 있습니다`,
      body: leftBudget > 0
        ? `남은 ${leftDays}일 동안 하루 ${won(leftBudget / leftDays)}씩 쓰면 한도(${won(lim.total)})를 지킵니다.`
        : `이미 한도를 ${won(-leftBudget)} 넘겼습니다. 남은 ${leftDays}일은 필수 지출만 하는 게 좋습니다.`,
    });
  }

  /* --- 4. 카테고리 집중도 + 절감 기회비용 --- */
  const catRows = Object.entries(m.byCat).sort((a, b) => b[1] - a[1]);
  if (catRows.length) {
    const [topCat, topAmt] = catRows[0];
    const share = m.spend > 0 ? (topAmt / m.spend) * 100 : 0;
    const cut = topAmt * 0.15;
    const imp = impactOfSaving(s, cut);
    const impText = imp.kind === 'goal' && imp.monthsSaved >= 0.5
      ? `여기서 15%(${won(cut)})만 줄이면 '${imp.goal.name || '목표'}' 달성이 약 ${imp.monthsSaved.toFixed(1)}개월 앞당겨집니다.`
      : `여기서 15%(${won(cut)})만 줄여 굴리면 10년 뒤 ${compact(imp.delta || 0)}이 더 쌓입니다.`;
    add({
      priority: share > 35 ? 1 : 2, tone: share > 40 ? 'warn' : 'info',
      icon: CAT[topCat]?.emoji || '📊',
      title: `${topCat}가 소비의 ${share.toFixed(0)}%`,
      body: `이번 달 ${won(topAmt)}. ${impText}`,
      actions: [{ label: '지출 내역 보기', route: 'spending' }],
    });
  }

  /* --- 5. 고정비 구조 --- */
  if (m.spend > 0) {
    const fixedShare = (m.fixed / m.spend) * 100;
    if (fixedShare > 55) {
      add({ priority: 1, tone: 'warn', icon: '🧱', title: `고정비 비중 ${fixedShare.toFixed(0)}% — 구조가 뻣뻣합니다`,
        body: `월 ${won(m.fixed)}이 자동으로 빠집니다. 고정비는 한 번 줄이면 매달 반복 절감되므로 변동비보다 효율이 큽니다. 통신·구독·보험 순으로 점검하세요.` });
    }
    // 구독 누수
    const sub = m.byCat['구독'] || 0;
    if (sub > 0) {
      const yearly = sub * 12;
      add({ priority: 3, tone: 'info', icon: '🔁', title: `구독료 월 ${won(sub)}`,
        body: `연간 ${won(yearly)}입니다. 순자산의 ${m.net > 0 ? ((yearly / m.net) * 100).toFixed(2) : '—'}%가 매년 자동 이탈합니다.` });
    }
  }

  /* --- 6. 소비 추세 --- */
  const prevAvg = avgSpend(s, 3);
  if (prevAvg && m.txCount > 0) {
    const d = ((m.projected - prevAvg) / prevAvg) * 100;
    if (Math.abs(d) >= 12) {
      add({ priority: d > 0 ? 1 : 2, tone: d > 0 ? 'warn' : 'good',
        icon: d > 0 ? '📈' : '📉',
        title: `최근 3개월 평균 대비 ${d > 0 ? '+' : ''}${d.toFixed(0)}%`,
        body: `평균 ${won(prevAvg)} → 이번 달 예상 ${won(m.projected)}. ${d > 0 ? '일시적 지출인지, 새 고정비가 생긴 건지 확인하세요.' : '이 흐름을 유지하면 연 ' + won((prevAvg - m.projected) * 12) + '을 더 모읍니다.'}` });
    }
  }

  /* --- 7. 비상금 --- */
  if (m.projected > 0) {
    const need = m.projected * n(s.profile.emergencyMonths);
    if (t.cash < need) {
      add({ priority: m.emergency < 3 ? 1 : 2, tone: m.emergency < 3 ? 'warn' : 'info', icon: '🧯',
        title: `비상금 ${m.emergency.toFixed(1)}개월치`,
        body: `목표 ${s.profile.emergencyMonths}개월(${won(need)})까지 ${won(need - t.cash)} 남았습니다. 투자보다 먼저 채워야 위기에 자산을 헐지 않습니다.` });
    } else if (t.cash > need * 2.5 && t.assets > 0) {
      add({ priority: 2, tone: 'info', icon: '💤', title: '현금이 필요 이상으로 많습니다',
        body: `현금 ${compact(t.cash)}는 ${m.emergency.toFixed(1)}개월치입니다. 초과분 ${compact(t.cash - need)}은 물가(연 ${(n(s.profile.inflation) * 100).toFixed(1)}%)에 매년 ${won((t.cash - need) * n(s.profile.inflation))}씩 녹습니다.` });
    }
  }

  /* --- 8. 자산 배분 --- */
  if (t.assets > 0) {
    const cashShare = (t.cash / t.assets) * 100;
    const investShare = (t.invested / t.assets) * 100;
    if (investShare < 20 && t.assets > 10_000_000) {
      add({ priority: 2, tone: 'info', icon: '🌱', title: `투자자산 비중 ${investShare.toFixed(0)}%`,
        body: `자산 대부분이 수익을 거의 못 냅니다. ${RISK[s.profile.riskProfile].label} 기준 기대수익 ${(n(s.profile.expectedReturn) * 100).toFixed(1)}%를 적용하면 연 ${won(t.assets * 0.3 * n(s.profile.expectedReturn))} 차이가 납니다.` });
    }
    void cashShare;
  }

  /* --- 9. 부채: 상환 vs 투자 --- */
  const debts = s.debts.filter((d) => n(d.balance) > 0);
  if (debts.length) {
    const worst = [...debts].sort((a, b) => n(b.rate) - n(a.rate))[0];
    const ret = n(s.profile.expectedReturn) * 100;
    const av = simulateDebt(debts, n(s.settings.extraDebtPay), 'avalanche');
    const cu = simulateDebt(debts, 0, 'current');
    if (n(worst.rate) > ret) {
      add({ priority: 1, tone: 'warn', icon: '⚖️', title: `${worst.name || '부채'} ${n(worst.rate)}% > 기대수익 ${ret.toFixed(1)}%`,
        body: `이 부채를 갚는 것이 투자보다 확실히 유리합니다. 여유자금은 상환에 먼저 쓰세요. 100만원을 상환하면 연 ${won(1_000_000 * (n(worst.rate) / 100 - n(s.profile.expectedReturn)))} 만큼 이득입니다.`,
        actions: [{ label: '상환 전략', route: 'debt' }] });
    }
    if (cu.months && av.months && cu.totalInterest - av.totalInterest > 10000) {
      add({ priority: 2, tone: 'info', icon: '🏔️', title: '상환 전략만 바꿔도 이자가 줄어듭니다',
        body: `최소상환 유지 시 ${cu.months}개월·이자 ${won(cu.totalInterest)} → 고금리 우선(아발란치) ${av.months}개월·이자 ${won(av.totalInterest)}. ${won(cu.totalInterest - av.totalInterest)} 절약.`,
        actions: [{ label: '상환 전략', route: 'debt' }] });
    }
  }

  /* --- 10. 목표 진척 --- */
  if (alloc.rows.length) {
    const behind = alloc.rows.filter((r) => r.gap > 1000);
    if (behind.length) {
      const b = behind[0];
      add({ priority: 1, tone: 'warn', icon: '🎯', title: `'${b.goal.name || '목표'}' 페이스가 부족합니다`,
        body: `목표일까지 ${Math.round(b.monthsLeft)}개월, 필요 월 저축 ${won(b.required)}인데 배분 가능액은 ${won(b.allocated)}입니다. 매달 ${won(b.gap)}이 부족합니다.`,
        actions: [{ label: '목표 조정', route: 'goals' }] });
    } else if (alloc.surplus > 0 && alloc.totalRequired > 0) {
      add({ priority: 2, tone: 'good', icon: '🎯', title: '모든 목표가 궤도에 있습니다',
        body: `필요 저축 ${won(alloc.totalRequired)}을 모두 충당하고 ${won(alloc.surplus)}이 남습니다. 남는 돈은 새 목표를 만들거나 투자 비중을 늘리세요.` });
    }
  } else {
    add({ priority: 2, tone: 'info', icon: '🏁', title: '목표가 아직 없습니다',
      body: '목표가 있어야 맞춤 한도가 계산됩니다. 비상금·주택자금 같은 기본 목표를 한 번에 만들 수 있습니다.',
      actions: [{ label: '기본 목표 만들기', route: 'goals' }] });
  }

  /* --- 11. FI 진척 --- */
  if (m.fiProgress !== null && m.fiProgress > 0 && m.net > 0) {
    const eta = monthsToTarget(m.annualSpend * 25, m.net, Math.max(0, m.capacity), n(s.profile.expectedReturn));
    add({ priority: 3, tone: 'info', icon: '🏝️', title: `경제적 자유까지 ${m.fiProgress.toFixed(1)}%`,
      body: `연 소비 ${compact(m.annualSpend)}의 25배인 ${compact(m.annualSpend * 25)}가 목표선입니다.` +
        (eta !== null && eta < 1200 ? ` 현재 저축 페이스로 약 ${Math.round(eta / 12)}년 ${Math.round(eta % 12)}개월 남았습니다.` : ' 저축여력을 늘리면 도달 시점이 계산됩니다.') });
  }

  cards.sort((a, b) => a.priority - b.priority);
  return cards;
}

/** 카테고리별 10% 절감 시 목표 단축 효과 랭킹 */
export function savingOpportunities(s, ratio = 0.1) {
  const m = metrics(s);
  return Object.entries(m.byCat)
    .filter(([cid]) => !CAT[cid]?.skip)
    .map(([cid, amt]) => {
      const cut = amt * ratio;
      const imp = impactOfSaving(s, cut);
      return {
        category: cid, emoji: CAT[cid]?.emoji || '•', color: CAT[cid]?.color,
        amount: amt, cut, impact: imp,
        months: imp.kind === 'goal' ? imp.monthsSaved : null,
        wealth: imp.kind === 'wealth' ? imp.delta : null,
      };
    })
    .sort((a, b) => b.cut - a.cut);
}

/** 최근 6개월 소비율 추이 */
export function burnHistory(s, count = 6) {
  const out = [];
  const cur = monthKey();
  for (let i = count - 1; i >= 0; i--) {
    const k = addMonths(cur, -i);
    const { spend, count: c } = spendOf(s, k);
    const snap = s.snapshots.find((x) => x.month === k);
    const net = snap ? snap.net : totals(s).net;
    out.push({
      month: k, spend, net,
      burn: c > 0 && net > 0 ? (spend / net) * 100 : null,   // 기록 없는 달은 null (그래프에서 제외)
      hasData: c > 0,
    });
  }
  return out;
}
