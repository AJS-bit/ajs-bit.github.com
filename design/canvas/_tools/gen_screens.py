# -*- coding: utf-8 -*-
import pathlib
from gen_common import *

OUT = pathlib.Path(__file__).resolve().parent.parent


KEEP_ALL_FROM = '-webkit-font-smoothing: antialiased; }'
KEEP_ALL_TO = '-webkit-font-smoothing: antialiased; word-break: keep-all; }'


def w(name, body, keep_all=False):
    """keep_all=True 면 body 에 word-break: keep-all 을 넣어 한글이 낱말 중간에서 갈라지지 않게 한다."""
    html = doc(body)
    if keep_all:
        assert html.count(KEEP_ALL_FROM) == 1
        html = html.replace(KEEP_ALL_FROM, KEEP_ALL_TO)
    (OUT / f'{name}.dc.html').write_text(html, encoding='utf-8')
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
    f'<svg width="33" height="33" viewBox="0 0 24 24" fill="#FFFFFF"><path d="M20.28 2.32 2.88 9.62c-.9.4-.8 1.7.1 2l6.6 2.2c.3.1.5.3.6.6l2.2 6.6c.3.9 1.6 1 2 .1L21.68 3.72c.3-.8-.6-1.7-1.4-1.4Z"/></svg></div>'
    f'<div style="display: flex; align-items: baseline; gap: 9px; margin-top: 18px;">'
    f'<span style="font-size: 27px; font-weight: 700; letter-spacing: 0.06em; color: {C["INK"]};">NAVI</span>'
    f'<span style="font-size: 13px; font-weight: 500; color: {C["INK3"]};">자산 성장 내비게이션</span></div>'
    f'<h1 style="margin: 14px 0 0; font-size: 26px; font-weight: 700; letter-spacing: -0.035em; line-height: 1.35; color: {C["INK"]};">'
    f'월급의 얼마를<br>쓰고 있는지부터</h1>'
    f'<p style="margin: 10px 0 0; font-size: 14px; line-height: 1.6; color: {C["INK2"]};">'
    f'지금 위치를 알면<br>목적지까지 얼마나 조절할지 보여요.</p>'
    f'<div style="margin-top: 24px;">{"".join(steps)}</div>'
    f'<div style="margin-top: auto; padding-bottom: 24px; display: flex; flex-direction: column; gap: 10px;">'
    f'{btn("내 데이터로 시작하기", "primary", h=52, radius=14, size=16)}'
    f'{btn("샘플로 둘러보기", "secondary", h=50, radius=14, size=15)}'
    f'<p style="margin: 6px 0 0; text-align: center; font-size: 11.5px; line-height: 1.5; color: {C["INK3"]};">'
    f'샘플은 가상 데이터이며 내 기록과 섞이지 않아요.</p></div></div>'), keep_all=True)


# ══════════════ 2. 저장소 로딩 · 실패 · 복구 ══════════════
def big_state(ic, icol, ibg, title, body, actions, extra=""):
    return card(
        f'<div style="display: flex; flex-direction: column; align-items: center; text-align: center; padding: 6px 4px;">'
        f'<div style="width: 48px; height: 48px; border-radius: 15px; background: {ibg}; display: flex; align-items: center; justify-content: center;">{icon(ic, 24, icol, 2)}</div>'
        f'<div style="font-size: 16px; font-weight: 700; letter-spacing: -0.02em; color: {C["INK"]}; margin-top: 13px;">{title}</div>'
        f'<div style="font-size: 12.5px; line-height: 1.55; color: {C["INK2"]}; margin-top: 6px;">{body}</div>'
        f'{extra}<div style="display: flex; gap: 8px; width: 100%; margin-top: 15px;">{actions}</div></div>', pad="18px 16px")


REF_PILL = (f'<span style="display: inline-block; margin-bottom: 8px; font-size: 11px; font-weight: 600; letter-spacing: 0.02em; '
            f'color: {C["INK2"]}; border: 1px solid {C["LINE"]}; background: {C["SURF"]}; border-radius: 99px; padding: 4px 10px; '
            f'white-space: nowrap;">구현 참고 · 앱 화면이 아닙니다</span>')

w('StorageStates', state_sheet(
    '저장소 로딩 · 실패 · 복구',
    '기록을 불러오거나 복구할 때 생길 수 있는 네 가지 경우입니다. 실제로는 한 번에 하나만 보입니다.',
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
                extra='<div style="width: 100%; margin-top: 13px;">' + note('navi-backup-2026-08.json · 12.4KB<br>NAVI에서 내보낸 백업 파일이 아니에요', 'neg', 'warn') + '</div>')),
     ('D · 샘플에서 내 데이터로 전환',
      big_state('arrowr', C["BRAND"], C["BRAND_SOFT"], '내 데이터로 시작할까요?',
                '샘플 기록은 모두 지워지고 빈 상태에서 시작합니다. 샘플은 백업되지 않아요.',
                btn('내 데이터로 시작', 'primary', h=44).replace('width: 100%;', 'flex: 1;') +
                btn('계속 둘러보기', 'secondary', h=44).replace('width: 100%;', 'flex: 1;')))],
    h=1324).replace('<h2 ', REF_PILL + '<h2 ', 1), keep_all=True)


def kvrow(k, v, vcol, strong=False, last=False):
    return (f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px; min-height: 40px; '
            f'{"" if last else "border-bottom: 1px solid " + C["LINE_ROW"] + ";"}">'
            f'<span style="font-size: 13px; font-weight: {600 if strong else 400}; color: {C["INK"] if strong else C["INK2"]};">{k}</span>'
            f'<span style="font-size: {15 if strong else 13.5}px; font-weight: 600; letter-spacing: -0.02em; color: {vcol};">{v}</span></div>')


# ══════════════ 3. 자산 › 부채 ══════════════
DEBTS = [("주택담보대출", "담보 · 원리금균등", 6200, "3.4", 32, C["INK"]),
         ("신용대출", "신용 · 원리금균등", 2200, "6.8", 20, C["INK"]),
         ("학자금대출", "학자금 · 원리금균등", 280, "2.5", 5, C["INK"]),
         ("카드 할부", "할부 · 잔여 9회", 180, "14.5", 20, C["NEG"])]
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
        hero(eyebrow_row('총부채', badge('가중 평균 연 4.44%', 'mute')) +
             f'<div style="display: flex; align-items: flex-end; justify-content: space-between; gap: 10px; margin-top: 6px;">'
             f'<div style="display: flex; align-items: baseline; gap: 2px;">'
             f'<span style="font-size: 38px; font-weight: 700; letter-spacing: -0.04em; line-height: 1.05; color: {C["INK"]};">8,860</span>'
             f'<span style="font-size: 19px; font-weight: 600; color: {C["INK2"]};">만원</span></div>'
             f'<div style="display: flex; flex-direction: column; align-items: flex-end; gap: 1px; padding-bottom: 3px;">'
             f'<span style="font-size: 11px; font-weight: 500; color: {C["INK3"]};">월 최소 상환</span>'
             f'<span style="font-size: 17px; font-weight: 600; letter-spacing: -0.02em; color: {C["INK"]};">77만원</span></div></div>'
             f'<div style="display: flex; height: 10px; border-radius: 99px; overflow: hidden; margin-top: 14px; gap: 2px;">'
             f'<div style="width: 70%; background: #94a3b8;"></div>'
             f'<div style="width: 25%; background: #f59e0b;"></div>'
             f'<div style="width: 3%; background: #64748b;"></div>'
             f'<div style="width: 2%; background: {C["NEG"]};"></div></div>'
             f'<div style="display: flex; align-items: center; justify-content: space-between; margin-top: 8px;">'
             f'<span style="font-size: 11px; color: {C["INK3"]};">담보 70% · 신용 25% · 학자금 3% · 할부 2%</span>'
             f'<span style="font-size: 11px; color: {C["INK3"]};">총자산의 48.7%</span></div>'),
        guidance('warn', '고금리 경고', '카드 할부 연 14.5%부터 갚으세요',
                 '잔액은 전체의 2%지만 금리는 신용대출의 2.1배예요.', '상환 전략 보기'),
        card(section_head('부채 4건', '8,860만원', smallbtn('추가', 'soft', 'plus')) +
             f'<div style="display: flex; flex-direction: column; margin-top: 6px;">{"".join(rows)}</div>'),
        card(f'<div style="display: flex; align-items: baseline; justify-content: space-between; gap: 8px;">'
             f'<span style="font-size: 13.5px; font-weight: 600; color: {C["INK"]};">이번 달 상환 예정 '
             f'<span style="font-weight: 500; color: {C["INK3"]};">9월 25일</span></span>'
             f'<span style="font-size: 15px; font-weight: 600; letter-spacing: -0.02em; color: {C["INK"]};">92만원</span></div>'
             f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px; margin-top: 6px;">'
             f'<span style="font-size: 11.5px; color: {C["INK3"]};">최소 77만원 + 추가 15만원</span>'
             f'<span style="font-size: 11.5px; color: {C["INK3"]};">소비율에는 포함되지 않아요</span></div>', pad="13px 14px"),
    ]) + bottomnav(1)), keep_all=True)


# ══════════════ 4. 자산 › 상환 전략 ══════════════
order = []
for i, (name, eta, saved) in enumerate([("카드 할부", "2027년 2월 완제", "1순위"),
                                        ("신용대출", "2030년 10월 완제", "2순위"),
                                        ("학자금대출", "2031년 8월 완제", "3순위"),
                                        ("주택담보대출", "2036년 4월 완제", "4순위")]):
    order.append(
        f'<div style="display: flex; align-items: center; gap: 11px; min-height: 46px; '
        f'{"border-bottom: 1px solid " + C["LINE_SOFT"] + ";" if i < 3 else ""}">'
        f'<span style="width: 22px; height: 22px; border-radius: 99px; background: {C["BRAND_SOFT"] if i == 0 else C["TRACK"]}; '
        f'color: {C["BRAND"] if i == 0 else "#606B7D"}; font-size: 11.5px; font-weight: 700; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">{i+1}</span>'
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
             f'{field("월 추가 상환액", "15", "만원", w=132)}'
             f'<div style="flex: 1; padding-bottom: 4px;">'
             f'<div style="font-size: 11.5px; color: {C["INK3"]};">최소 상환 77만원에 더해서</div>'
             f'<div style="font-size: 13.5px; font-weight: 600; color: {C["INK"]}; margin-top: 2px;">매월 92만원 상환</div></div></div>'
             f'<div style="margin-top: 9px;">{note("금액은 입력하고 다른 곳을 누르면 저장돼요.", "mute")}</div></div>'),
        card(f'<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 0;">'
             f'<div style="padding-right: 12px;">'
             f'<div style="font-size: 11.5px; font-weight: 500; color: {C["INK3"]};">예상 완제</div>'
             f'<div style="font-size: 21px; font-weight: 600; letter-spacing: -0.025em; color: {C["INK"]}; margin-top: 3px;">2036년 4월</div>'
             f'<div style="font-size: 11px; color: {C["INK3"]}; margin-top: 2px;">9년 8개월 뒤</div></div>'
             f'<div style="padding-left: 12px; border-left: 1px solid {C["LINE_SOFT"]};">'
             f'<div style="font-size: 11.5px; font-weight: 500; color: {C["INK3"]};">총이자</div>'
             f'<div style="font-size: 21px; font-weight: 600; letter-spacing: -0.025em; color: {C["INK"]}; margin-top: 3px;">1,734만원</div>'
             f'<div style="font-size: 11px; font-weight: 600; color: {C["POS"]}; margin-top: 2px;">소액 우선보다 30만원 절약</div></div></div>'),
        card(section_head('완제 순서', '고금리 우선') +
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
                             f'<span style="font-size: 12.5px; font-weight: 600; color: {C["INK2"]}; white-space: nowrap;">{s}</span></div>')

# 날짜 합계는 소비만 센다 — 소비율에서 빠지는 이체는 회색 덧말로 따로 적는다
excl = lambda t: f' <span style="font-weight: 500; color: {C["INK4"]};">· {t}</span>'

w('Ledger', frame(
    screen_header('소비', tabs=['이번 달', '내역', '한도'], active=1,
                  trailing=f'<div style="display: flex; align-items: center; gap: 8px;">{month_stepper()}{add_tx_button()}</div>') +
    content([
        card(f'<div style="display: flex; align-items: center; gap: 8px;">'
             f'<div style="flex: 1; display: flex; align-items: center; gap: 9px; height: 40px; padding: 0 12px; border-radius: 11px; background: {C["INSET"]};">'
             f'{icon("search", 16, "#606B7D", 1.9)}<span style="font-size: 13.5px; color: {C["INK4"]};">메모·카테고리 검색</span></div>'
             f'<div style="width: 40px; height: 40px; border-radius: 11px; border: 1px solid {C["LINE"]}; display: flex; align-items: center; justify-content: center;">{icon("repeat", 17, C["INK2"], 1.9)}</div></div>'
             f'<div style="display: flex; gap: 6px; margin-top: 10px; overflow: hidden;">'
             f'<div style="display: inline-flex; align-items: center; gap: 4px; height: 32px; padding: 0 12px; border-radius: 99px; background: {C["BRAND_SOFT"]}; color: {C["BRAND"]}; font-size: 12.5px; font-weight: 600; flex-shrink: 0;">전체 32건{icon("down", 13, C["BRAND"], 2)}</div>'
             f'<div style="display: inline-flex; align-items: center; gap: 5px; height: 32px; padding: 0 12px; border-radius: 99px; border: 1px solid {C["LINE"]}; color: {C["INK2"]}; font-size: 12.5px; font-weight: 500; flex-shrink: 0;">{catdot("식비", 8)}식비</div>'
             f'<div style="display: inline-flex; align-items: center; gap: 5px; height: 32px; padding: 0 12px; border-radius: 99px; border: 1px solid {C["LINE"]}; color: {C["INK2"]}; font-size: 12.5px; font-weight: 500; flex-shrink: 0;">{catdot("주거/관리", 8)}주거</div>'
             f'<div style="display: inline-flex; align-items: center; height: 32px; padding: 0 12px; border-radius: 99px; border: 1px solid {C["LINE"]}; color: {C["INK3"]}; font-size: 12.5px; font-weight: 500; flex-shrink: 0;">더보기</div></div>'
             f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px; margin-top: 11px; padding-top: 10px; border-top: 1px solid {C["LINE_SOFT"]};">'
             f'<span style="font-size: 12px; color: {C["INK2"]};">일반 소비 <span style="font-weight: 600; color: {C["INK"]};">112만원</span></span>'
             f'<span style="font-size: 11.5px; color: {C["INK3"]};">이체 63만 · 상환 92만은 제외</span></div>'),
        card(daygroup('9월 8일', '화요일 · 오늘', '32,000원') +
             tx('식비', 'rice', '점심 · 팀 회식', '생활비 통장', '−32,000') +
             daygroup('9월 7일', '월요일', '118,400원') +
             tx('교통', 'bus', '교통카드 충전', '계좌 미지정', '−50,000') +
             tx('쇼핑', 'bag', '생필품', '신용카드', '−62,000') +
             tx('카페/간식', 'coffee', '카페', '생활비 통장', '−6,400') +
             daygroup('9월 5일', '토요일', '20,000원' + excl('이체 30만원 제외')) +
             tx('저축/투자', 'leaf', 'ETF 자동이체', '생활비 → ETF 계좌', '−300,000',
                badges=minib('소비율 제외', 'mute') + minib('반복', 'brand'), muted=True) +
             tx('통신', 'phone', '휴대폰 요금', '생활비 통장', '−20,000', badges=minib('반복', 'brand')) +
             daygroup('9월 3일', '목요일', '470,000원') +
             tx('주거/관리', 'house', '월세 · 관리비', '생활비 통장', '−470,000'),
             pad="4px 14px 10px"),
    ]) + bottomnav(2)))


# ══════════════ 5-2. 소비 › 내역 — v5-1 이후 (LedgerV5) ══════════════
# plan/v5-calendar.md §9-6 · §3-3: 필터 칩 `분류 안 함 7건` · 분류 안 함 행(부제 `분류 안 함`, 메모 없으면 제목 `분류 안 함 기록`, 점선 없음) ·
# 날짜 그룹 헤더 `소비 8.7만 · 이체 30만`(0인 항목 생략) + 확인한 날 체크 · 행 ⋯ 에 `매달 반복으로 만들기`(분류 안 함 행 제외).
# 날짜별 합계는 달력 시안(gen_calendar.SEP)과 같은 값이어야 한다 — 아래 assert 가 지킨다. v3 기준 그림 `Ledger` 는 그대로 둔다.
# 9월 8일(오늘) 행은 하루 시트의 `오늘 기록`(계획 §4-2 도면 · gen_v5.RECENT)과 같은 자료다 — 커피 4,500 = 카페/간식 · 편의점 6,500 = 분류 안 함.
# 9월 6일 이체는 등록된 반복 거래 `ETF 자동이체`(매월 6일 · RecurringPrefill 등록 목록)가 자동으로 기록한 행이다 — `소비율 제외` + `반복` 배지(v3 Ledger 의 같은 행과 같은 모양).
from gen_calendar import SEP, SEP_CHECK, SEP_TRANSFER, SEP_TOTAL, fmt_sum

WEEKDAY = ['일요일', '월요일', '화요일', '수요일', '목요일', '금요일', '토요일']

# (날짜, [(카테고리 | None = 분류 안 함, 아이콘, 메모, 계좌 글, 금액, 종류)]) — 종류 'spend' | 'transfer'(손으로 적은 이체) | 'transfer-auto'(반복 거래가 자동 기록한 이체)
LEDGER_V5 = [
    (8, [('카페/간식', 'coffee', '커피', '계좌 미지정', 4_500, 'spend'),
         ('식비', 'rice', '점심', '계좌 미지정', 9_000, 'spend'),
         ('쇼핑', 'bag', '생필품', '계좌 미지정', 17_000, 'spend'),
         (None, None, '편의점', None, 6_500, 'spend')]),
    (6, [('저축/투자', 'leaf', 'ETF 자동이체', '생활비 → ETF 계좌', 300_000, 'transfer-auto')]),
    (5, [(None, None, '버스', None, 4_500, 'spend'),
         (None, None, '', None, 3_000, 'spend'),
         (None, None, '커피', None, 4_500, 'spend')]),
    (4, [(None, None, '커피', None, 4_500, 'spend')]),
    (3, [('교통', 'bus', '택시', '계좌 미지정', 45_000, 'spend'),
         ('식비', 'rice', '점심', '계좌 미지정', 9_000, 'spend'),
         (None, None, '간식', None, 4_500, 'spend')]),
    (1, [(None, None, '커피', None, 4_500, 'spend'),
         ('식비', 'rice', '점심', '계좌 미지정', 7_500, 'spend')]),
]
for _d, _rows in LEDGER_V5:       # 칸 숫자 = 내역 날짜 헤더와 같은 숫자(§12-22)
    assert sum(r[4] for r in _rows if r[5] == 'spend') == (SEP[_d] or 0), _d
V5_COUNT = sum(len(rows) for _, rows in LEDGER_V5)
V5_UNCAT = [r for _, rows in LEDGER_V5 for r in rows if r[0] is None]
assert len(V5_UNCAT) == 7 and sum(r[4] for r in V5_UNCAT) == 32_000      # `분류 안 함 7건` · 히어로 각주 `분류 안 한 32,000원`
V5_TRANSFER = sum(r[4] for _, rows in LEDGER_V5 for r in rows if r[5].startswith('transfer'))
assert V5_TRANSFER == 300_000 and {d for d, rows in LEDGER_V5 if any(r[5].startswith('transfer') for r in rows)} == SEP_TRANSFER      # 내역의 이체 날짜 = 달력의 이체 배지 날짜


def head_sum(n):
    """날짜 헤더의 금액 — 달력 칸과 같은 formatSum 하나(`.0`은 fmt_sum 이 뗀다 — 300,000 → `30만`. 머리글만의 예외 없음)."""
    return fmt_sum(n)


def row_menu(items):
    """행 ⋯ 를 눌렀을 때 뜨는 메뉴. 색 없이 잉크 단계만."""
    cells = ''.join(
        f'<div style="display: flex; align-items: center; height: 40px; padding: 0 14px; font-size: 13.5px; font-weight: {600 if strong else 500}; '
        f'color: {C["NEG"] if danger else C["INK"]}; white-space: nowrap;{"" if i == 0 else " border-top: 1px solid " + C["LINE_ROW"] + ";"}">{t}</div>'
        for i, (t, strong, danger) in enumerate(items))
    return (f'<div style="position: absolute; right: 0; top: 40px; z-index: 2; min-width: 176px; background: {C["SURF"]}; border: 1px solid {C["LINE"]}; '
            f'border-radius: 13px; padding: 4px 0; box-shadow: 0 1px 2px rgba(16,24,40,.04), 0 12px 28px -12px rgba(16,24,40,.32);">{cells}</div>')


def tx5(cat, ic, memo, link_txt, amt, kind, menu=''):
    """v5 내역 행. cat 이 None 이면 분류 안 함 행 — 부제 `분류 안 함`, 메모가 없으면 제목 `분류 안 함 기록`, 점선 없음."""
    if cat is None:
        tile = (f'<div style="width: 34px; height: 34px; border-radius: 10px; background: {C["INSET"]}; display: flex; align-items: center; '
                f'justify-content: center; flex-shrink: 0;">{icon("help", 17, C["INK3"], 1.9)}</div>')
        title, sub = (memo or '분류 안 함 기록'), '분류 안 함'
    else:
        tile, title, sub = caticon(cat, ic, 34), memo, f'{cat} · {link_txt}'
    muted = kind.startswith('transfer')
    badges = (minib('소비율 제외', 'mute') if muted else '') + (minib('반복', 'brand') if kind == 'transfer-auto' else '')      # `반복` 배지는 자동 기록된 반복 거래에만 단다(9월 6일 ETF 자동이체)
    b = f'<span style="display: inline-flex; gap: 5px; margin-left: 6px;">{badges}</span>' if badges else ''
    return (f'<div style="position: relative; display: flex; align-items: center; gap: 11px; min-height: 54px; border-top: 1px solid {C["LINE_ROW"]};">'
            f'{tile}<div style="flex: 1; min-width: 0;">'
            f'<div style="font-size: 13.5px; font-weight: 500; color: {C["INK"]}; white-space: nowrap;">{title}{b}</div>'
            f'<div style="font-size: 11px; color: {C["INK3"]}; margin-top: 2px;">{sub}</div></div>'
            f'<span style="font-size: 14.5px; font-weight: 600; letter-spacing: -0.02em; color: {C["INK2"] if muted else C["INK"]}; white-space: nowrap; flex-shrink: 0;">&minus;{amt:,}</span>'
            f'<span style="flex-shrink: 0; display: inline-flex;">{icon("more", 16, C["INK2"] if menu else C["INK4"], 2.2)}</span>{menu}</div>')


def daygroup5(day, rows):
    spend = sum(r[4] for r in rows if r[5] == 'spend')
    transfer = sum(r[4] for r in rows if r[5].startswith('transfer'))
    parts = ([f'소비 {head_sum(spend)}'] if spend else []) + ([f'이체 {head_sum(transfer)}'] if transfer else [])     # 0인 항목은 생략
    chk = (f'<span style="display: inline-flex; flex-shrink: 0;">{icon("check", 12, C["INK2"], 2.8)}</span>') if day in SEP_CHECK else ''
    wd = WEEKDAY[(1 + day) % 7] + (' · 오늘' if day == 8 else '')           # 2026-09-01 = 화요일
    return (f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 10px; padding: 12px 0 6px;">'
            f'<span style="font-size: 13px; font-weight: 600; color: {C["INK"]}; white-space: nowrap;">9월 {day}일 '
            f'<span style="font-weight: 500; color: {C["INK3"]};">{wd}</span></span>'
            f'<span style="display: inline-flex; align-items: center; gap: 5px; font-size: 12.5px; font-weight: 600; color: {C["INK2"]}; white-space: nowrap; flex-shrink: 0;">'
            f'{" · ".join(parts)}{chk}</span></div>')


MENU_ROW = (8, 1)      # ⋯ 메뉴를 펼쳐 보이는 행 — 9월 8일 둘째 행(식비 · 점심). 분류 안 함 행의 메뉴에는 `매달 반복으로 만들기`가 없다.
ledger5_rows = ''
for _d, _rows in LEDGER_V5:
    ledger5_rows += daygroup5(_d, _rows)
    for _i, _r in enumerate(_rows):
        _menu = row_menu([('수정', False, False), ('매달 반복으로 만들기', True, False), ('삭제', False, True)]) if (_d, _i) == MENU_ROW else ''
        ledger5_rows += tx5(*_r, menu=_menu)

chip5 = lambda inner, on=False, strong=False: (
    f'<div style="display: inline-flex; align-items: center; gap: 4px; height: 32px; padding: 0 10px; border-radius: 99px; '
    + (f'background: {C["BRAND_SOFT"]}; color: {C["BRAND"]}; font-weight: 600;' if on else
       f'border: 1px solid {C["LINE"]}; color: {C["INK"] if strong else C["INK2"]}; font-weight: {600 if strong else 500};')
    + f' font-size: 12.5px; white-space: nowrap; flex-shrink: 0;">{inner}</div>')

w('LedgerV5', frame(
    screen_header('소비', tabs=['이번 달', '내역', '한도'], active=1,
                  trailing=f'<div style="display: flex; align-items: center; gap: 8px;">{month_stepper()}{add_tx_button()}</div>') +
    content([
        card(f'<div style="display: flex; align-items: center; gap: 8px;">'
             f'<div style="flex: 1; display: flex; align-items: center; gap: 9px; height: 40px; padding: 0 12px; border-radius: 11px; background: {C["INSET"]};">'
             f'{icon("search", 16, "#606B7D", 1.9)}<span style="font-size: 13.5px; color: {C["INK4"]};">메모·카테고리 검색</span></div>'
             f'<div style="width: 40px; height: 40px; border-radius: 11px; border: 1px solid {C["LINE"]}; display: flex; align-items: center; justify-content: center;">{icon("repeat", 17, C["INK2"], 1.9)}</div></div>'
             f'<div style="display: flex; gap: 5px; margin-top: 10px; overflow: hidden;">'
             + chip5(f'전체 {V5_COUNT}건{icon("down", 13, C["BRAND"], 2)}', on=True)
             + chip5(f'분류 안 함 {len(V5_UNCAT)}건', strong=True)          # 주황 없이 굵기만 — 누르면 분류하기 시트
             + chip5(f'{catdot("식비", 8)}식비')
             + chip5('더보기') +
             f'</div>'
             f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px; margin-top: 11px; padding-top: 10px; border-top: 1px solid {C["LINE_SOFT"]};">'
             f'<span style="font-size: 12px; color: {C["INK2"]};">일반 소비 <span style="font-weight: 600; color: {C["INK"]};">{SEP_TOTAL:,}원</span></span>'
             f'<span style="font-size: 11.5px; color: {C["INK3"]};">이체 {head_sum(V5_TRANSFER)}은 제외</span></div>'),
        card(ledger5_rows, pad="4px 14px 10px"),
    ]) + bottomnav(2)), keep_all=True)


# ══════════════ 6. 목적지 › 새 목적지 설계 ══════════════
presets = []
for name, meta, col, ic in [("비상금 6개월", "6개월치 생활비", C["SKY"], "shield"),
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
  <text x="196" y="76" font-size="10" fill="{C["INK4"]}">원금만 2,516만</text>
  <line x1="10" y1="96" x2="316" y2="96" stroke="{C["LINE"]}" stroke-width="1"/>
  <text x="10" y="112" font-size="10.5" fill="{C["INK4"]}">오늘 500만</text>
  <text x="316" y="112" text-anchor="end" font-size="10.5" font-weight="600" fill="{C["INK2"]}">7년 뒤 3,000만</text>
</svg>'''

w('GoalDesign', frame(
    screen_header('목적지', '4개 진행 중', tabs=['내 목적지', '새 목적지 설계'], active=1) +
    content([
        card(f'<div style="font-size: 11px; font-weight: 600; letter-spacing: 0.07em; color: {C["INK3"]};">추천 목적지에서 시작</div>'
             f'<div style="display: flex; gap: 8px; margin-top: 9px;">{"".join(presets)}</div>', pad="13px 14px"),
        hero(f'<div style="display: flex; gap: 10px;">{field("이름", "결혼 자금", w=None)}{field("목표액", "3,000", "만원", required=True, w=124)}</div>'
             f'<div style="display: flex; gap: 10px; margin-top: 12px;">'
             f'{field("시작 적립액", "500", "만원", w=None)}{field("기간", "7", "년", required=True, w=104)}'
             f'{field("연 수익률", "4.0", "%", w=104)}</div>'
             f'<div style="margin-top: 15px; padding: 13px; background: {C["VIO_SOFT"]}; border-radius: 14px;">'
             f'<div style="display: flex; align-items: flex-end; justify-content: space-between; gap: 10px;">'
             f'<div><div style="font-size: 11.5px; font-weight: 600; color: {C["VIO_STRONG"]};">필요한 월 납입액</div>'
             f'<div style="display: flex; align-items: baseline; gap: 2px; margin-top: 3px;">'
             f'<span style="font-size: 30px; font-weight: 700; letter-spacing: -0.035em; color: {C["VIO_STRONG"]};">24</span>'
             f'<span style="font-size: 16px; font-weight: 600; color: {C["VIO_STRONG"]};">만원</span></div></div>'
             f'{badge("저장되지 않는 계산", "vio", "spark")}</div>'
             f'<div style="font-size: 11.5px; line-height: 1.45; color: #4E2496; margin-top: 6px;">'
             f'지금 월 저축 63만원은 모두 배분돼 있어요. 새로 필요한 월 24만원은 이번 달 저축·투자 여력 27만원 안에서 낼 수 있어요.</div></div>'
             f'<div style="margin-top: 12px;">{goal_chart}</div>'
             f'{btn("목적지로 저장", "primary")}', pad=15),
    ]) + bottomnav(3)), keep_all=True)


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
             f'<span style="font-size: 12px; font-weight: 600; color: {C["INK3"]}; white-space: nowrap; flex-shrink: 0;">되돌리기</span></div>'
             f'<p style="margin: 11px 0 0; font-size: 15px; font-weight: 600; letter-spacing: -0.015em; color: {C["INK"]};">월 추가 상환을 얼마나 할까요?</p>'
             f'<div style="display: flex; align-items: baseline; gap: 7px; margin-top: 9px;">'
             f'<span style="font-size: 14px; font-weight: 500; color: {C["INK4"]}; text-decoration: line-through;">15만원</span>'
             f'<span style="align-self: center;">{icon("arrowr", 13, C["VIO_STRONG"], 2.4)}</span>'
             f'<span style="font-size: 25px; font-weight: 700; letter-spacing: -0.03em; color: {C["VIO_STRONG"]};">20<span style="font-size: 15px; font-weight: 600;">만원</span></span>'
             f'<span style="font-size: 12.5px; font-weight: 600; color: {C["VIO_STRONG"]}; margin-left: auto;">매월 97만원 상환</span></div>'
             f'<div style="margin-top: 8px;">{slider(round(20 / 27 * 100), C["VIO"])}</div>'
             f'<div style="display: flex; align-items: center; justify-content: space-between; margin-top: 5px;">'
             f'<span style="font-size: 11px; color: {C["INK4"]};">최소 상환만</span>'
             f'<span style="font-size: 11px; color: {C["INK4"]};">월 27만원</span></div>'
             f'<div style="margin-top: 11px;">{note("최소 상환 월 77만원은 줄일 수 없어 슬라이더에서 뺐어요.", "mute")}</div>',
             extra=f'border: 1px dashed {C["VIO_LINE"]};'),
        card(f'<div style="display: flex; gap: 8px;">{compare("고금리 우선", "2035년 8월", "9년 뒤", "1,614만원", best=True)}'
             f'{compare("소액 우선", "2035년 9월", "9년 1개월 뒤", "1,643만원")}</div>'
             f'<div style="margin-top: 11px;">{note("고금리 우선이 이자를 <b style=font-weight:600>약 30만원</b> 적게 내고 한 달 먼저 끝나요. 추가 상환 없이 두면 완제 2038년 9월 · 총이자 2,248만원.", "mute")}</div>',
             pad="13px 14px"),
        card(f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 10px;">'
             f'<div style="min-width: 0;"><div style="font-size: 13.5px; font-weight: 600; color: {C["INK"]};">이 계획을 저장할까요?</div>'
             f'<div style="font-size: 11.5px; line-height: 1.45; color: {C["INK3"]}; margin-top: 2px;">저장해야 자산 경로와 목적지 계산에 반영됩니다.</div></div></div>'
             f'<div style="display: flex; gap: 8px; margin-top: 12px;">'
             f'{btn("가정 종료", "secondary", h=44).replace("width: 100%;", "flex: 1;")}'
             f'{btn("상환 계획 저장", "primary", h=44).replace("width: 100%;", "flex: 1.4;")}</div>'),
    ]) + bottomnav(4)), keep_all=True)
