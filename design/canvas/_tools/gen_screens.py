# -*- coding: utf-8 -*-
import pathlib
from gen_common import *

OUT = pathlib.Path('/home/user/ajs-bit.github.com/design/canvas')


def w(name, body):
    (OUT / f'{name}.dc.html').write_text(doc(body), encoding='utf-8')
    print('wrote', name)


# ══════════════ 1. 온보딩 · 첫 실행 ══════════════
steps = []
for t, d in [("모든 기록은 이 기기에만", "로그인도 계정도 없어요. 인터넷이 끊겨도 그대로 씁니다."),
             ("실수령 급여 하나면 시작", "자산을 입력하지 않아도 소비율·한도·목적지가 계산됩니다."),
             ("언제든 백업으로 옮기기", "JSON 파일 하나로 내보내고 다시 불러올 수 있어요.")]:
    steps.append(
        f'<div style="display: flex; gap: 11px; padding: 12px 0; border-top: 1px solid {C["LINE_SOFT"]};">'
        f'<span style="flex-shrink: 0; margin-top: 1px;">{icon("check", 16, C["POS"], 2.6)}</span>'
        f'<div><div style="font-size: 13.5px; font-weight: 600; color: {C["INK"]};">{t}</div>'
        f'<div style="font-size: 12px; line-height: 1.45; color: {C["INK3"]}; margin-top: 2px;">{d}</div></div></div>')

w('Onboarding', frame(
    f'<div style="flex: 1; min-height: 0; display: flex; flex-direction: column; padding: 0 20px; overflow: hidden;">'
    f'<div style="height: 92px; flex-shrink: 0;"></div>'
    f'<div style="width: 62px; height: 62px; border-radius: 20px; background: linear-gradient(140deg, #3556E6 0%, #7A3FE4 100%); '
    f'display: flex; align-items: center; justify-content: center; flex-shrink: 0;">'
    f'<svg width="33" height="33" viewBox="0 0 24 24" fill="#FFFFFF"><path d="M21.3 3.1 3.9 10.4c-.9.4-.8 1.7.1 2l6.6 2.2c.3.1.5.3.6.6l2.2 6.6c.3.9 1.6 1 2 .1L22.7 4.5c.3-.8-.6-1.7-1.4-1.4Z"/></svg></div>'
    f'<div style="display: flex; align-items: baseline; gap: 9px; margin-top: 18px;">'
    f'<span style="font-size: 27px; font-weight: 700; letter-spacing: 0.06em; color: {C["INK"]};">NAVI</span>'
    f'<span style="font-size: 13px; font-weight: 500; color: {C["INK3"]};">자산 성장 내비게이션</span></div>'
    f'<h1 style="margin: 14px 0 0; font-size: 26px; font-weight: 700; letter-spacing: -0.035em; line-height: 1.35; color: {C["INK"]};">'
    f'월급의 얼마를<br>쓰고 있는지부터</h1>'
    f'<p style="margin: 10px 0 0; font-size: 14px; line-height: 1.6; color: {C["INK2"]};">'
    f'지금 위치를 알면 목적지까지 얼마나 조절하면 되는지 보입니다.</p>'
    f'<div style="margin-top: 24px;">{"".join(steps)}</div>'
    f'<div style="margin-top: auto; padding-bottom: 24px; display: flex; flex-direction: column; gap: 10px;">'
    f'{btn("내 데이터로 시작하기", "primary", h=52, radius=14, size=16)}'
    f'{btn("샘플로 둘러보기", "secondary", h=50, radius=14, size=15)}'
    f'<p style="margin: 6px 0 0; text-align: center; font-size: 11.5px; line-height: 1.5; color: {C["INK3"]};">'
    f'샘플은 가상 데이터이며 내 기록과 섞이지 않아요.</p></div></div>'))


# ══════════════ 2. 저장소 로딩 · 실패 · 복구 ══════════════
def big_state(ic, icol, ibg, title, body, actions, extra=""):
    return card(
        f'<div style="display: flex; flex-direction: column; align-items: center; text-align: center; padding: 6px 4px;">'
        f'<div style="width: 48px; height: 48px; border-radius: 15px; background: {ibg}; display: flex; align-items: center; justify-content: center;">{icon(ic, 24, icol, 2)}</div>'
        f'<div style="font-size: 16px; font-weight: 700; letter-spacing: -0.02em; color: {C["INK"]}; margin-top: 13px;">{title}</div>'
        f'<div style="font-size: 12.5px; line-height: 1.55; color: {C["INK2"]}; margin-top: 6px;">{body}</div>'
        f'{extra}<div style="display: flex; gap: 8px; width: 100%; margin-top: 15px;">{actions}</div></div>', pad="18px 16px")


w('StorageStates', state_sheet(
    '저장소 로딩 · 실패 · 복구',
    '기기 저장소를 읽지 못했을 때도 기존 기록을 덮어쓰지 않습니다. 복구는 항상 미리보기를 거칩니다.',
    [('A · 불러오는 중',
      card(f'<div style="display: flex; flex-direction: column; align-items: center; text-align: center; padding: 14px 4px;">'
           f'<div style="width: 44px; height: 44px; border-radius: 99px; border: 3px solid {C["TRACK"]}; border-top-color: {C["BRAND"]};"></div>'
           f'<div style="font-size: 14px; font-weight: 600; color: {C["INK"]}; margin-top: 14px;">저장된 기록을 불러오는 중</div>'
           f'<div style="font-size: 12px; color: {C["INK3"]}; margin-top: 4px;">잠시만 기다려 주세요</div></div>', pad="18px 16px")),
     ('B · 불러오기 실패',
      big_state('warn', C["NEG"], C["NEG_SOFT"], '기록을 불러오지 못했어요',
                '기기 저장소를 읽을 수 없습니다. 기존 기록은 지워지지 않았으니 다시 시도하거나 백업 파일로 복구해 주세요.',
                btn('다시 불러오기', 'primary', h=44).replace('width: 100%;', 'flex: 1;') +
                btn('백업으로 복구', 'secondary', h=44).replace('width: 100%;', 'flex: 1;'),
                extra=f'<div style="width: 100%; margin-top: 13px;">{note("복구를 눌러도 바로 덮어쓰지 않아요. 무엇이 바뀌는지 먼저 보여 드립니다.", "mute")}</div>')),
     ('C · 복구 파일 오류',
      big_state('x', C["NEG"], C["NEG_SOFT"], '이 파일은 읽을 수 없어요',
                'NAVI 백업 형식이 아니거나 파일이 손상됐습니다. 현재 기록은 그대로입니다.',
                btn('다른 파일 선택', 'primary', h=44).replace('width: 100%;', 'flex: 1;') +
                btn('취소', 'secondary', h=44).replace('width: 100%;', 'flex: 1;'),
                extra='<div style="width: 100%; margin-top: 13px;">' + note('navi-backup-2026-08.json · 12.4KB<br>오류 — 필수 항목 <span style="font-weight:600">version</span>이 없습니다', 'neg', 'warn') + '</div>')),
     ('D · 샘플에서 내 데이터로 전환',
      big_state('arrowr', C["BRAND"], C["BRAND_SOFT"], '내 데이터로 시작할까요?',
                '샘플 기록은 모두 지워지고 빈 상태에서 시작합니다. 샘플은 백업되지 않아요.',
                btn('내 데이터로 시작', 'primary', h=44).replace('width: 100%;', 'flex: 1;') +
                btn('계속 둘러보기', 'secondary', h=44).replace('width: 100%;', 'flex: 1;')))],
    h=1264))


def kvrow(k, v, vcol, strong=False, last=False):
    return (f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px; min-height: 40px; '
            f'{"" if last else "border-bottom: 1px solid " + C["LINE_ROW"] + ";"}">'
            f'<span style="font-size: 13px; font-weight: {600 if strong else 400}; color: {C["INK"] if strong else C["INK2"]};">{k}</span>'
            f'<span style="font-size: {15 if strong else 13.5}px; font-weight: 600; letter-spacing: -0.02em; color: {vcol};">{v}</span></div>')


# ══════════════ 3. 자산 › 부채 ══════════════
DEBTS = [("주택담보대출", "담보 · 원리금균등", 6200, "3.4", 32, C["INK"]),
         ("신용대출", "신용 · 원리금균등", 2480, "6.8", 21, C["INK"]),
         ("카드 할부", "할부 · 잔여 9회", 180, "14.5", 2, C["NEG"])]
rows = []
for i, (name, meta, bal, rate, minpay, col) in enumerate(DEBTS):
    hi = badge('고금리', 'neg') if col == C["NEG"] else ''
    rows.append(
        f'<div style="display: flex; align-items: center; gap: 10px; min-height: 52px; '
        f'{"border-bottom: 1px solid " + C["LINE_SOFT"] + ";" if i < len(DEBTS) - 1 else ""}">'
        f'<div style="flex: 1; min-width: 0;">'
        f'<div style="display: flex; align-items: center; gap: 6px;">'
        f'<span style="font-size: 13.5px; font-weight: 600; color: {C["INK"]};">{name}</span>{hi}</div>'
        f'<div style="font-size: 11px; color: {C["INK3"]}; margin-top: 2px;">{meta} · 월 최소 {minpay}만원</div></div>'
        f'<div style="text-align: right;">{amount(f"{bal:,}")}'
        f'<div style="font-size: 11.5px; font-weight: 600; color: {col};">연 {rate}%</div></div>'
        f'{icon("more", 16, C["INK4"], 2.2)}</div>')

w('Debts', frame(
    screen_header('자산', '가진 것과 갚을 것', tabs=['자산 구성', '부채', '상환 전략'], active=1) +
    content([
        hero(eyebrow_row('총부채', badge('가중 평균 연 4.58%', 'mute')) +
             f'<div style="display: flex; align-items: flex-end; justify-content: space-between; gap: 10px; margin-top: 6px;">'
             f'<div style="display: flex; align-items: baseline; gap: 2px;">'
             f'<span style="font-size: 38px; font-weight: 700; letter-spacing: -0.04em; line-height: 1.05; color: {C["INK"]};">8,860</span>'
             f'<span style="font-size: 19px; font-weight: 600; color: {C["INK2"]};">만원</span></div>'
             f'<div style="display: flex; flex-direction: column; align-items: flex-end; gap: 1px; padding-bottom: 3px;">'
             f'<span style="font-size: 11px; font-weight: 500; color: {C["INK3"]};">월 최소 상환</span>'
             f'<span style="font-size: 17px; font-weight: 600; letter-spacing: -0.02em; color: {C["INK"]};">55만원</span></div></div>'
             f'<div style="display: flex; height: 10px; border-radius: 99px; overflow: hidden; margin-top: 14px; gap: 2px;">'
             f'<div style="width: 70%; background: #94a3b8;"></div>'
             f'<div style="width: 28%; background: #f59e0b;"></div>'
             f'<div style="width: 2%; background: {C["NEG"]};"></div></div>'
             f'<div style="display: flex; align-items: center; justify-content: space-between; margin-top: 8px;">'
             f'<span style="font-size: 11px; color: {C["INK3"]};">담보 70% · 신용 28% · 할부 2%</span>'
             f'<span style="font-size: 11px; color: {C["INK3"]};">총자산의 48.7%</span></div>'),
        guidance('warn', '고금리 경고', '카드 할부 연 14.5%부터 갚으세요',
                 '남은 180만원이지만 이자 부담은 신용대출의 절반에 가까워요.', '상환 전략 보기'),
        card(section_head('부채 3건', '8,860만원', smallbtn('추가', 'soft', 'plus')) +
             f'<div style="display: flex; flex-direction: column; margin-top: 6px;">{"".join(rows)}</div>'),
        card(f'<div style="display: flex; align-items: baseline; justify-content: space-between; gap: 8px;">'
             f'<span style="font-size: 13.5px; font-weight: 600; color: {C["INK"]};">이번 달 상환 예정 '
             f'<span style="font-weight: 500; color: {C["INK3"]};">9월 25일</span></span>'
             f'<span style="font-size: 15px; font-weight: 600; letter-spacing: -0.02em; color: {C["INK"]};">75만원</span></div>'
             f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px; margin-top: 6px;">'
             f'<span style="font-size: 11.5px; color: {C["INK3"]};">최소 55만원 + 추가 20만원</span>'
             f'<span style="font-size: 11.5px; color: {C["INK3"]};">소비율에는 포함되지 않아요</span></div>', pad="13px 14px"),
    ]) + bottomnav(1)))


# ══════════════ 4. 자산 › 상환 전략 ══════════════
order = []
for i, (name, eta, saved) in enumerate([("카드 할부", "2027년 3월 완제", "1순위"),
                                        ("신용대출", "2028년 11월 완제", "2순위"),
                                        ("주택담보대출", "2038년 2월 완제", "3순위")]):
    order.append(
        f'<div style="display: flex; align-items: center; gap: 11px; min-height: 46px; '
        f'{"border-bottom: 1px solid " + C["LINE_SOFT"] + ";" if i < 2 else ""}">'
        f'<span style="width: 22px; height: 22px; border-radius: 99px; background: {C["BRAND_SOFT"] if i == 0 else C["TRACK"]}; '
        f'color: {C["BRAND"] if i == 0 else "#8593AD"}; font-size: 11.5px; font-weight: 700; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">{i+1}</span>'
        f'<span style="flex: 1; font-size: 13.5px; font-weight: 600; color: {C["INK"]};">{name}</span>'
        f'<span style="font-size: 12px; color: {C["INK3"]};">{eta}</span></div>')

w('Strategy', frame(
    screen_header('자산', '가진 것과 갚을 것', tabs=['자산 구성', '부채', '상환 전략'], active=2) +
    content([
        hero(eyebrow_row('상환 방식', badge('선택 즉시 저장됨', 'pos', 'check')) +
             f'<div style="display: flex; gap: 8px; margin-top: 11px;">'
             f'<div style="flex: 1; padding: 12px; border-radius: 14px; border: 1.5px solid {C["BRAND"]}; background: {C["BRAND_SOFT"]};">'
             f'<div style="font-size: 13.5px; font-weight: 700; color: {C["BRAND"]};">고금리 우선</div>'
             f'<div style="font-size: 11.5px; line-height: 1.45; color: {C["INK2"]}; margin-top: 3px;">이자를 가장 적게 내는 방법</div></div>'
             f'<div style="flex: 1; padding: 12px; border-radius: 14px; border: 1px solid {C["LINE"]}; background: {C["SURF"]};">'
             f'<div style="font-size: 13.5px; font-weight: 600; color: {C["INK"]};">소액 우선</div>'
             f'<div style="font-size: 11.5px; line-height: 1.45; color: {C["INK3"]}; margin-top: 3px;">건수를 빨리 줄이는 방법</div></div></div>'
             f'<div style="margin-top: 15px; padding-top: 14px; border-top: 1px solid {C["LINE_SOFT"]};">'
             f'<div style="display: flex; align-items: flex-end; gap: 10px;">'
             f'{field("월 추가 상환액", "20", "만원", w=132)}'
             f'<div style="flex: 1; padding-bottom: 4px;">'
             f'<div style="font-size: 11.5px; color: {C["INK3"]};">최소 상환 55만원에 더해서</div>'
             f'<div style="font-size: 13.5px; font-weight: 600; color: {C["INK"]}; margin-top: 2px;">매월 75만원 상환</div></div></div>'
             f'<div style="margin-top: 9px;">{note("입력 후 다른 곳을 누르면 저장됩니다. 방식 선택은 누르는 즉시 반영돼요.", "mute")}</div></div>'),
        card(f'<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 0;">'
             f'<div style="padding-right: 12px;">'
             f'<div style="font-size: 11.5px; font-weight: 500; color: {C["INK3"]};">예상 완제</div>'
             f'<div style="font-size: 21px; font-weight: 600; letter-spacing: -0.025em; color: {C["INK"]}; margin-top: 3px;">2038년 2월</div>'
             f'<div style="font-size: 11px; color: {C["INK3"]}; margin-top: 2px;">11년 5개월 뒤</div></div>'
             f'<div style="padding-left: 12px; border-left: 1px solid {C["LINE_SOFT"]};">'
             f'<div style="font-size: 11.5px; font-weight: 500; color: {C["INK3"]};">총이자</div>'
             f'<div style="font-size: 21px; font-weight: 600; letter-spacing: -0.025em; color: {C["INK"]}; margin-top: 3px;">1,840만원</div>'
             f'<div style="font-size: 11px; font-weight: 600; color: {C["POS"]}; margin-top: 2px;">소액 우선보다 120만원 절약</div></div></div>'),
        card(section_head('상환 순서', '고금리 우선') +
             f'<div style="display: flex; flex-direction: column; margin-top: 6px;">{"".join(order)}</div>'),
    ]) + bottomnav(1)))


# ══════════════ 5. 소비 › 내역 (모바일) ══════════════
def tx(cat, ic, memo, link_txt, amt, badges="", muted=False):
    col = C["INK2"] if muted else C["INK"]
    b = f'<span style="display: inline-flex; gap: 5px; margin-left: 6px;">{badges}</span>' if badges else ''
    return (f'<div style="display: flex; align-items: center; gap: 11px; min-height: 54px; border-top: 1px solid {C["LINE_ROW"]};">'
            f'{caticon(cat, ic, 34)}'
            f'<div style="flex: 1; min-width: 0;">'
            f'<div style="font-size: 13.5px; font-weight: 500; color: {C["INK"]};">{memo}{b}</div>'
            f'<div style="font-size: 11px; color: {C["INK3"]}; margin-top: 2px;">{cat} · {link_txt}</div></div>'
            f'<span style="font-size: 14.5px; font-weight: 600; letter-spacing: -0.02em; color: {col};">{amt}</span>'
            f'{icon("more", 16, C["INK4"], 2.2)}</div>')


minib = lambda t, tone: (f'<span style="font-size: 10px; font-weight: 600; color: '
                         f'{C["TAB_INK"] if tone == "mute" else C["BRAND"]}; background: '
                         f'{C["LINE_SOFT"] if tone == "mute" else C["BRAND_SOFT"]}; border-radius: 5px; padding: 2px 5px;">{t}</span>')

daygroup = lambda d, w_, s: (f'<div style="display: flex; align-items: baseline; justify-content: space-between; gap: 10px; padding: 12px 0 6px;">'
                             f'<span style="font-size: 13px; font-weight: 600; color: {C["INK"]};">{d} '
                             f'<span style="font-weight: 500; color: {C["INK3"]};">{w_}</span></span>'
                             f'<span style="font-size: 12.5px; font-weight: 600; color: {C["INK2"]};">{s}</span></div>')

w('Ledger', frame(
    screen_header('소비', tabs=['이번 달', '내역', '한도'], active=1,
                  trailing=f'<div style="display: flex; align-items: center; gap: 8px;">{month_stepper()}{add_tx_button()}</div>') +
    content([
        card(f'<div style="display: flex; align-items: center; gap: 8px;">'
             f'<div style="flex: 1; display: flex; align-items: center; gap: 9px; height: 40px; padding: 0 12px; border-radius: 11px; background: {C["INSET"]};">'
             f'{icon("search", 16, "#8593AD", 1.9)}<span style="font-size: 13.5px; color: {C["INK4"]};">메모·카테고리 검색</span></div>'
             f'<div style="width: 40px; height: 40px; border-radius: 11px; border: 1px solid {C["LINE"]}; display: flex; align-items: center; justify-content: center;">{icon("repeat", 17, C["INK2"], 1.9)}</div></div>'
             f'<div style="display: flex; gap: 6px; margin-top: 10px; overflow: hidden;">'
             f'<div style="display: inline-flex; align-items: center; gap: 4px; height: 32px; padding: 0 12px; border-radius: 99px; background: {C["BRAND_SOFT"]}; color: {C["BRAND"]}; font-size: 12.5px; font-weight: 600; flex-shrink: 0;">전체 32건{icon("down", 13, C["BRAND"], 2)}</div>'
             f'<div style="display: inline-flex; align-items: center; gap: 5px; height: 32px; padding: 0 12px; border-radius: 99px; border: 1px solid {C["LINE"]}; color: {C["INK2"]}; font-size: 12.5px; font-weight: 500; flex-shrink: 0;">{catdot("식비", 8)}식비</div>'
             f'<div style="display: inline-flex; align-items: center; gap: 5px; height: 32px; padding: 0 12px; border-radius: 99px; border: 1px solid {C["LINE"]}; color: {C["INK2"]}; font-size: 12.5px; font-weight: 500; flex-shrink: 0;">{catdot("주거/관리", 8)}주거</div>'
             f'<div style="display: inline-flex; align-items: center; height: 32px; padding: 0 12px; border-radius: 99px; border: 1px solid {C["LINE"]}; color: {C["INK3"]}; font-size: 12.5px; font-weight: 500; flex-shrink: 0;">더보기</div></div>'
             f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px; margin-top: 11px; padding-top: 10px; border-top: 1px solid {C["LINE_SOFT"]};">'
             f'<span style="font-size: 12px; color: {C["INK2"]};">일반 소비 <span style="font-weight: 600; color: {C["INK"]};">112만원</span></span>'
             f'<span style="font-size: 11.5px; color: {C["INK3"]};">이체 90만 · 상환 55만은 제외</span></div>'),
        card(daygroup('9월 8일', '화요일 · 오늘', '32,000원') +
             tx('식비', 'rice', '점심 · 팀 회식', '생활비 통장', '−32,000') +
             daygroup('9월 7일', '월요일', '118,400원') +
             tx('교통', 'bus', '교통카드 충전', '연결 없음', '−50,000') +
             tx('쇼핑', 'bag', '생필품', '신용카드', '−62,000') +
             tx('카페/간식', 'coffee', '카페', '생활비 통장', '−6,400') +
             daygroup('9월 5일', '토요일', '320,000원') +
             tx('저축/투자', 'leaf', 'ETF 자동이체', '생활비 → ETF 계좌', '−300,000',
                badges=minib('소비율 제외', 'mute') + minib('반복', 'brand'), muted=True) +
             daygroup('9월 3일', '수요일', '470,000원') +
             tx('주거/관리', 'house', '월세 · 관리비', '생활비 통장', '−470,000'),
             pad="4px 14px 10px"),
    ]) + bottomnav(2)))


# ══════════════ 6. 목적지 › 새 목적지 설계 ══════════════
presets = []
for name, meta, col, ic in [("비상금 6개월", "생활비 기준 1,500만원", C["SKY"], "shield"),
                            ("전세 보증금", "목표액 직접 입력", C["VIO"], "house"),
                            ("은퇴 연금", "30년 뒤 목표", C["POS"], "leaf")]:
    presets.append(
        f'<div style="flex: 1; min-width: 0; padding: 11px 10px; border-radius: 13px; border: 1px solid {C["LINE"]}; background: {C["SURF"]};">'
        f'<div style="width: 26px; height: 26px; border-radius: 8px; background: {col}18; display: flex; align-items: center; justify-content: center;">{icon(ic, 14, col, 2)}</div>'
        f'<div style="font-size: 12.5px; font-weight: 600; color: {C["INK"]}; margin-top: 7px;">{name}</div>'
        f'<div style="font-size: 10.5px; line-height: 1.4; color: {C["INK3"]}; margin-top: 2px;">{meta}</div></div>')

goal_chart = f'''<svg width="326" height="120" viewBox="0 0 326 120" fill="none" style="display: block; width: 100%; height: 120px;">
  <defs><linearGradient id="gfill" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="{C["VIO"]}" stop-opacity="0.22"/><stop offset="100%" stop-color="{C["VIO"]}" stop-opacity="0"/>
  </linearGradient></defs>
  <line x1="10" y1="19.1" x2="316" y2="19.1" stroke="{C["LINE"]}" stroke-width="1" stroke-dasharray="4 4"/>
  <text x="10" y="14" font-size="9.5" fill="{C["INK4"]}">목표 3,000만</text>
  <path d="M10 83.2 L71.2 71.6 L132.4 59.6 L193.6 47 L254.8 33.8 L316 19.1 L316 96 L10 96 Z" fill="url(#gfill)"/>
  <path d="M10 83.2 L71.2 71.6 L132.4 59.6 L193.6 47 L254.8 33.8 L316 19.1" stroke="{C["VIO"]}" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M10 83.2 L71.2 72.1 L132.4 61 L193.6 50 L254.8 38.9 L316 27.8" stroke="{C["INK4"]}" stroke-width="1.6" stroke-dasharray="4 4" stroke-linecap="round" stroke-linejoin="round"/>
  <circle cx="316" cy="19.1" r="3.6" fill="{C["VIO"]}"/>
  <circle cx="10" cy="83.2" r="3" fill="{C["VIO"]}"/>
  <text x="196" y="76" font-size="10" fill="{C["INK4"]}">원금만 2,660만</text>
  <line x1="10" y1="96" x2="316" y2="96" stroke="{C["LINE"]}" stroke-width="1"/>
  <text x="10" y="112" font-size="10.5" fill="{C["INK4"]}">오늘 500만</text>
  <text x="316" y="112" text-anchor="end" font-size="10.5" font-weight="600" fill="{C["INK2"]}">5년 뒤 3,000만</text>
</svg>'''

w('GoalDesign', frame(
    screen_header('목적지', '4개 진행 중', tabs=['내 목적지', '새 목적지 설계'], active=1) +
    content([
        card(f'<div style="font-size: 11px; font-weight: 600; letter-spacing: 0.07em; color: {C["INK3"]};">추천 목적지에서 시작</div>'
             f'<div style="display: flex; gap: 8px; margin-top: 9px;">{"".join(presets)}</div>', pad="13px 14px"),
        hero(f'<div style="display: flex; gap: 10px;">{field("이름", "결혼 자금", w=None)}{field("목표액", "3,000", "만원", required=True, w=124)}</div>'
             f'<div style="display: flex; gap: 10px; margin-top: 12px;">'
             f'{field("시작 적립액", "500", "만원", w=None)}{field("기간", "5", "년", required=True, w=104)}'
             f'{field("연 수익률", "4.0", "%", w=104)}</div>'
             f'<div style="margin-top: 15px; padding: 13px; background: {C["VIO_SOFT"]}; border-radius: 14px;">'
             f'<div style="display: flex; align-items: flex-end; justify-content: space-between; gap: 10px;">'
             f'<div><div style="font-size: 11.5px; font-weight: 600; color: {C["VIO_STRONG"]};">필요한 월 납입액</div>'
             f'<div style="display: flex; align-items: baseline; gap: 2px; margin-top: 3px;">'
             f'<span style="font-size: 30px; font-weight: 700; letter-spacing: -0.035em; color: {C["VIO_STRONG"]};">36</span>'
             f'<span style="font-size: 16px; font-weight: 600; color: {C["VIO_STRONG"]};">만원</span></div></div>'
             f'{badge("저장되지 않는 계산", "vio", "spark")}</div>'
             f'<div style="font-size: 11.5px; line-height: 1.45; color: #4E2496; margin-top: 6px;">'
             f'현재 잔여자금 63만원 안에서 충당할 수 있어요. 저장하면 배분에 반영됩니다.</div></div>'
             f'<div style="margin-top: 12px;">{goal_chart}</div>'
             f'{btn("목적지로 저장", "primary")}', pad=15),
    ]) + bottomnav(3)))


# ══════════════ 7. 미래 › 상환 계획 ══════════════
def compare(name, eta, months, interest, best=False):
    bd = f'1.5px solid {C["VIO"]}' if best else f'1px solid {C["LINE"]}'
    bg = C["VIO_SOFT"] if best else C["SURF"]
    tag = (f'<span style="background: {C["VIO"]}; color: #FFFFFF; font-size: 10px; font-weight: 700; '
           f'border-radius: 6px; padding: 3px 6px; flex-shrink: 0;">추천</span>') if best else ''
    return (f'<div style="flex: 1; min-width: 0; padding: 13px; border-radius: 14px; border: {bd}; background: {bg};">'
            f'<div style="display: flex; align-items: center; gap: 5px;">'
            f'<span style="font-size: 13px; font-weight: 700; white-space: nowrap; color: {C["VIO_STRONG"] if best else C["INK"]};">{name}</span>{tag}</div>'
            f'<div style="font-size: 11.5px; color: {C["INK3"]}; margin-top: 9px;">완제 예상</div>'
            f'<div style="font-size: 16px; font-weight: 600; letter-spacing: -0.02em; color: {C["INK"]};">{eta}</div>'
            f'<div style="font-size: 11px; color: {C["INK3"]};">{months}</div>'
            f'<div style="font-size: 11.5px; color: {C["INK3"]}; margin-top: 8px;">총이자</div>'
            f'<div style="font-size: 16px; font-weight: 600; letter-spacing: -0.02em; color: {C["INK"]};">{interest}</div></div>')

w('Payoff', frame(
    screen_header('미래', '앞으로의 항로', tabs=['자산 경로', '상환 계획'], active=1) +
    content([
        card(f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px;">'
             f'{badge("저장되지 않는 가정", "vio", "spark")}'
             f'<span style="font-size: 12px; font-weight: 600; color: {C["INK3"]};">되돌리기</span></div>'
             f'<p style="margin: 11px 0 0; font-size: 15px; font-weight: 600; letter-spacing: -0.015em; color: {C["INK"]};">월 추가 상환을 얼마나 할까요?</p>'
             f'<div style="display: flex; align-items: baseline; gap: 7px; margin-top: 9px;">'
             f'<span style="font-size: 14px; font-weight: 500; color: {C["INK4"]}; text-decoration: line-through;">0원</span>'
             f'<span style="align-self: center;">{icon("arrowr", 13, C["VIO_STRONG"], 2.4)}</span>'
             f'<span style="font-size: 25px; font-weight: 700; letter-spacing: -0.03em; color: {C["VIO_STRONG"]};">20<span style="font-size: 15px; font-weight: 600;">만원</span></span>'
             f'<span style="font-size: 12.5px; font-weight: 600; color: {C["VIO_STRONG"]}; margin-left: auto;">매월 75만원 상환</span></div>'
             f'<div style="margin-top: 8px;">{slider(40, C["VIO"])}</div>'
             f'<div style="display: flex; align-items: center; justify-content: space-between; margin-top: 5px;">'
             f'<span style="font-size: 11px; color: {C["INK4"]};">최소 상환만</span>'
             f'<span style="font-size: 11px; color: {C["INK4"]};">월 50만원</span></div>'
             f'<div style="margin-top: 11px;">{note("최소 상환(월 55만원)은 줄일 수 없어 슬라이더에 포함되지 않습니다.", "mute")}</div>',
             extra=f'border: 1px dashed {C["VIO_LINE"]};'),
        card(f'<div style="display: flex; gap: 8px;">{compare("고금리 우선", "2038년 2월", "11년 5개월 뒤", "1,840만원", best=True)}'
             f'{compare("소액 우선", "2038년 5월", "11년 8개월 뒤", "1,960만원")}</div>'
             f'<div style="margin-top: 11px;">{note("고금리 우선이 이자를 <b style=font-weight:600>120만원</b> 적게 냅니다. 추가 상환 없이 두면 완제 2041년 9월 · 총이자 2,470만원.", "mute")}</div>',
             pad="13px 14px"),
        card(f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 10px;">'
             f'<div style="min-width: 0;"><div style="font-size: 13.5px; font-weight: 600; color: {C["INK"]};">이 계획을 저장할까요?</div>'
             f'<div style="font-size: 11.5px; line-height: 1.45; color: {C["INK3"]}; margin-top: 2px;">저장해야 자산 경로와 목적지 계산에 반영됩니다.</div></div></div>'
             f'<div style="display: flex; gap: 8px; margin-top: 12px;">'
             f'{btn("가정 취소", "secondary", h=44).replace("width: 100%;", "flex: 1;")}'
             f'{btn("상환 계획 저장", "primary", h=44).replace("width: 100%;", "flex: 1.4;")}</div>'),
    ]) + bottomnav(4)))
