# -*- coding: utf-8 -*-
import pathlib
from gen_common import *

OUT = pathlib.Path('/home/user/ajs-bit.github.com/design/canvas')


def w(name, body):
    (OUT / f'{name}.dc.html').write_text(doc(body), encoding='utf-8')
    print('wrote', name)


def group(label, inner, meta=None):
    m = f'<span style="font-size: 11.5px; color: {C["INK3"]};">{meta}</span>' if meta else ''
    return (f'<div><div style="display: flex; align-items: baseline; justify-content: space-between; gap: 8px; margin-bottom: 9px;">'
            f'<span style="font-size: 11px; font-weight: 600; letter-spacing: 0.07em; color: {C["INK3"]};">{label}</span>{m}</div>{inner}</div>')


def foldrow(label, meta=None, open_=False):
    m = f'<span style="font-size: 12px; color: {C["INK3"]};">{meta}</span>' if meta else ''
    return (f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px; height: 48px; '
            f'padding: 0 13px; border-radius: 12px; background: {C["INSET"]};">'
            f'<span style="font-size: 13.5px; font-weight: 600; color: {C["INK"]};">{label}</span>'
            f'<div style="display: flex; align-items: center; gap: 8px;">{m}{icon("up" if open_ else "down", 16, C["INK4"], 2)}</div></div>')


def checkbox(text, on=True, tone="brand"):
    col = C["BRAND"] if tone == "brand" else C["NEG"]
    box = (f'<span style="width: 20px; height: 20px; border-radius: 6px; background: {col}; display: flex; align-items: center; '
           f'justify-content: center; flex-shrink: 0;">{icon("check", 13, "#FFFFFF", 3)}</span>') if on else (
        f'<span style="width: 20px; height: 20px; border-radius: 6px; border: 1.5px solid {C["INPUT"]}; flex-shrink: 0;"></span>')
    return (f'<div style="display: flex; align-items: flex-start; gap: 9px;">{box}'
            f'<span style="font-size: 12.5px; line-height: 1.5; color: {C["INK2"]};">{text}</span></div>')


def kv(k, v, vcol=None, h=42, last=False):
    return (f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px; min-height: {h}px; '
            f'{"" if last else "border-bottom: 1px solid " + C["LINE_ROW"] + ";"}">'
            f'<span style="font-size: 13px; color: {C["INK2"]};">{k}</span>'
            f'<span style="font-size: 13.5px; font-weight: 600; color: {vcol or C["INK"]};">{v}</span></div>')


# ══════════════ 1. 설정 · 내 수치 ══════════════
w('ProfileDialog', sheet(
    '내 수치 입력', '급여와 소비 목표만 있으면 홈이 계산됩니다. 나머지는 언제든 채워도 돼요.',
    group('기본', f'<div style="display: flex; gap: 10px;">{field("월 실수령 급여", "360", "만원", required=True)}'
                  f'{field("나이", "28", "세", optional=True, w=104)}</div>') +
    group('소비 목표',
          f'<div style="padding: 13px; background: {C["INSET"]}; border-radius: 14px;">'
          f'<div style="display: flex; align-items: baseline; justify-content: space-between; gap: 8px;">'
          f'<span style="font-size: 13px; color: {C["INK2"]};">급여의 얼마까지 쓸까요?</span>'
          f'<span style="font-size: 22px; font-weight: 700; letter-spacing: -0.03em; color: {C["INK"]};">60<span style="font-size: 14px; font-weight: 600; color: {C["INK2"]};">%</span></span></div>'
          f'<div style="margin-top: 9px;">{slider(60)}</div>'
          f'<div style="display: flex; align-items: center; justify-content: space-between; margin-top: 4px;">'
          f'<span style="font-size: 11px; color: {C["INK4"]};">0%</span>'
          f'<span style="font-size: 11.5px; font-weight: 600; color: {C["INK"]};">월 216만원까지</span>'
          f'<span style="font-size: 11px; color: {C["INK4"]};">100%</span></div>'
          f'<div style="margin-top: 11px;">{note("60%는 통계 평균이나 정답이 아니라 <b style=font-weight:600>바꿔도 되는 계획 시작값</b>입니다. 0%로 두어도 그대로 유지돼요.", "mute")}</div></div>') +
    group('추가 설정',
          f'<div style="display: flex; gap: 10px;">{field("부수입", "30", "만원", optional=True)}'
          f'{field("총자산", "1억 8,210", "만원", state="readonly")}</div>'
          f'<div style="margin-top: 9px;">{note("자산을 5건 입력해 두어서 총자산은 합계로 고정됩니다. 개별 자산에서 수정하세요.", "mute", "lock")}</div>'
          f'<div style="display: flex; gap: 10px; margin-top: 12px;">{field("총부채", "8,860", "만원", state="readonly")}'
          f'{field("기대수익률", "2.4", "%", optional=True, w=124)}</div>'
          f'<div style="margin-top: 12px;"><div style="font-size: 12px; font-weight: 600; color: {C["INK2"]}; margin-bottom: 7px;">테마</div>'
          f'{segmented(["시스템", "라이트", "다크"], 0)}</div>') +
    group('데이터', f'<div style="display: flex; gap: 8px;">'
                    f'{btn("백업 내보내기", "secondary", "download", h=44).replace("width: 100%;", "flex: 1;")}'
                    f'{btn("불러오기", "secondary", "upload", h=44).replace("width: 100%;", "flex: 1;")}</div>'
                    f'<div style="margin-top: 8px;">{btn("모두 지우고 새로 시작", "danger", h=44)}</div>'),
    sheet_footer('취소', '저장')))


# ══════════════ 2. 자산 추가 ══════════════
w('AssetDialog', sheet(
    '자산 추가', '이름과 평가액만 있으면 저장돼요.',
    f'{field("자산 이름", "ETF 계좌", required=True)}'
    f'<div style="display: flex; gap: 10px;">{select_field("유형", "투자")}{field("평가액", "4,890", "만원", required=True, w=142)}</div>'
    f'{field("연 기대수익률", "6.5", "%", optional=True, helper="비워 두면 유형 기본값을 씁니다", w=None)}'
    f'{note("거래에서 <b style=font-weight:600>잔액에도 반영하기</b>를 켜면 이 계좌의 평가액이 함께 바뀝니다. 0원이어도 계좌 기록은 남습니다.", "mute")}',
    sheet_footer('취소', '자산 추가'), scrim_h=190))


# ══════════════ 3. 부채 수정 ══════════════
w('DebtDialog', sheet(
    '카드 할부 수정', '거래에서 대출상환으로 연결된 부채예요.',
    f'{field("부채 이름", "카드 할부", required=True)}'
    f'<div style="display: flex; gap: 10px;">{select_field("유형", "할부")}{field("남은 원금", "180", "만원", required=True, w=142)}</div>'
    f'<div style="display: flex; gap: 10px;">{field("연 금리", "14.5", "%", required=True)}{field("월 최소 상환액", "2", "만원", w=142)}</div>'
    f'{note("연 14.5%는 보유한 부채 중 가장 높아요. 고금리 우선 전략에서 1순위로 상환됩니다.", "warn", "warn")}'
    f'{note("남은 원금을 0으로 두면 완납으로 기록되고 목록에는 남습니다. 삭제하면 연결된 거래의 부채 연결이 끊깁니다.", "mute")}',
    sheet_footer('취소', '변경 저장'), scrim_h=110,
    header_right=f'<div style="display: flex; align-items: center; gap: 8px; flex-shrink: 0;">{smallbtn("삭제", "danger", "trash", h=32)}'
                 f'<div style="width: 36px; height: 36px; border-radius: 11px; background: {C["INSET"]}; display: flex; align-items: center; justify-content: center;">{icon("x", 17, C["INK2"], 2.2)}</div></div>'))


# ══════════════ 4. 목적지 추가 ══════════════
types = []
TYPES = [("일반 저축", "wallet", C["BRAND"]), ("비상금", "shield", C["SKY"]), ("투자", "chart", C["VIO"]),
         ("순자산", "target", C["POS"]), ("부채 상환", "bank", C["WARN"])]
for i, (name, ic, col) in enumerate(TYPES):
    sel = i == 4
    types.append(
        f'<div style="flex: 1; min-width: 0; padding: 10px 6px; border-radius: 12px; text-align: center; '
        f'border: {"1.5px solid " + col if sel else "1px solid " + C["LINE"]}; background: {col + "14" if sel else C["SURF"]};">'
        f'<div style="display: flex; justify-content: center;">{icon(ic, 17, col if sel else C["INK3"], 1.9)}</div>'
        f'<div style="font-size: 11px; font-weight: {700 if sel else 500}; color: {col if sel else C["INK2"]}; margin-top: 5px; white-space: nowrap;">{name}</div></div>')

debtpick = []
for i, (name, bal, on) in enumerate([("카드 할부", "180만원 · 연 14.5%", True), ("신용대출", "2,200만원 · 연 6.8%", True),
                                     ("학자금대출", "280만원 · 연 2.5%", False),
                                     ("주택담보대출", "6,200만원 · 연 3.4%", False)]):
    box = (f'<span style="width: 20px; height: 20px; border-radius: 6px; background: {C["BRAND"]}; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">{icon("check", 13, "#FFFFFF", 3)}</span>'
           if on else f'<span style="width: 20px; height: 20px; border-radius: 6px; border: 1.5px solid {C["INPUT"]}; flex-shrink: 0;"></span>')
    debtpick.append(
        f'<div style="display: flex; align-items: center; gap: 10px; min-height: 46px; '
        f'{"border-bottom: 1px solid " + C["LINE_ROW"] + ";" if i < 2 else ""}">{box}'
        f'<div style="flex: 1; min-width: 0;"><div style="font-size: 13.5px; font-weight: 600; color: {C["INK"]};">{name}</div>'
        f'<div style="font-size: 11px; color: {C["INK3"]};">{bal}</div></div></div>')

w('GoalDialog', sheet(
    '목적지 추가', '유형에 따라 필요한 값이 달라져요.',
    group('유형', f'<div style="display: flex; gap: 6px;">{"".join(types)}</div>') +
    f'{field("이름", "신용대출 완제", required=True)}'
    + group('갚을 부채 선택', f'<div style="padding: 0 13px; background: {C["INSET"]}; border-radius: 14px;">{"".join(debtpick)}</div>',
            meta='2건 선택 · 2,380만원')
    + f'<div style="display: flex; gap: 10px;">{select_field("우선순위", "1순위 · 가장 먼저")}{field("목표 기한", "2029.06", optional=True, w=124)}</div>'
    + note('부채 상환 목적지는 적립 대신 <span style="font-weight:600">상환 계획</span>을 따릅니다. 목표액·적립액 입력란이 없고 홈 대표로도 지정할 수 있어요.', 'mute'),
    sheet_footer('취소', '목적지 추가'), scrim_h=40))


# ══════════════ 5. 반복 거래 관리 ══════════════
rules = []
for i, (name, meta, amt, on) in enumerate([("ETF 자동이체", "매월 5일 · 저축/투자", "30만원", True),
                                           ("휴대폰 요금", "매월 5일 · 통신", "2만원", True),
                                           ("헬스장", "일시정지됨 · 문화/여가", "5만원", False)]):
    col = C["INK"] if on else C["INK4"]
    rules.append(
        f'<div style="display: flex; align-items: center; gap: 10px; min-height: 52px; '
        f'{"border-bottom: 1px solid " + C["LINE_ROW"] + ";" if i < 2 else ""}">'
        f'<div style="flex: 1; min-width: 0;"><div style="font-size: 13.5px; font-weight: 600; color: {col};">{name}</div>'
        f'<div style="font-size: 11px; color: {C["INK4"] if not on else C["INK3"]};">{meta}</div></div>'
        f'<span style="font-size: 13.5px; font-weight: 600; color: {col};">{amt}</span>'
        f'{toggle(on)}{icon("more", 16, C["INK4"], 2.2)}</div>')

w('RecurringDialog', sheet(
    '반복 거래', '매달 자동으로 만들어지는 거래예요. 끄면 다음 달부터 생성되지 않습니다.',
    group('등록된 규칙', f'<div style="padding: 0 13px; background: {C["SURF"]}; border: 1px solid {C["LINE"]}; border-radius: 14px;">{"".join(rules)}</div>',
          meta='3건 · 활성 2건') +
    group('새 규칙',
          f'<div style="display: flex; gap: 10px;">{field("이름", "넷플릭스", required=True)}{field("금액", "13,500", "원", required=True, w=142)}</div>'
          f'<div style="display: flex; gap: 10px; margin-top: 12px;">{select_field("카테고리", "구독")}{field("결제일", "15", "일", w=104)}'
          f'{field("시작 월", "2026.10", w=112)}</div>'
          f'<div style="margin-top: 11px;">{note("이미 지난 달에는 만들어지지 않아요. 생성된 거래는 개별로 수정·삭제할 수 있습니다.", "mute")}</div>'),
    sheet_footer('닫기', '규칙 추가'), scrim_h=40))


# ══════════════ 6. 월 마감 확정 ══════════════
w('MonthlyClose', sheet(
    '2026년 8월 마감', '그 달의 실제 수치를 확정합니다. 저장한 값으로만 과거 소비율을 계산해요.',
    note('이미 <span style="font-weight:600">2026년 9월 2일</span>에 마감한 달입니다. 다시 저장하면 기존 마감값을 덮어씁니다.', 'warn', 'warn') +
    group('그 달의 실제 수치', f'<div style="display: flex; gap: 10px;">{field("총수입", "3,900,000", "원", required=True)}'
                                f'{field("그중 실수령 급여", "3,600,000", "원", required=True)}</div>'
                                f'<div style="display: flex; gap: 10px; margin-top: 12px;">{field("대출상환", "920,000", "원")}'
                                f'{field("저축·투자 이체", "630,000", "원")}</div>', meta='원 단위') +
    group('자동으로 채워진 값',
          f'<div style="padding: 2px 13px; background: {C["INSET"]}; border-radius: 14px;">'
          f'{kv("일반 소비 합계", "2,043,800원")}{kv("급여 대비 소비율", "56.8%", C["POS"])}'
          f'{kv("월말 자산 총액", "180,400,000원")}{kv("월말 부채 총액", "89,200,000원", last=True)}</div>') +
    note('급여를 비워 두면 그 달은 <span style="font-weight:600">—</span>로 남습니다. 지금 급여로 과거를 채우지 않아요.', 'mute'),
    sheet_footer('취소', '마감 저장'),
    sticky=f'<div style="padding: 12px 18px; background: {C["INSET"]}; border-top: 1px solid {C["LINE"]}; flex-shrink: 0;">'
           f'{checkbox("위 수치가 실제와 같음을 확인했습니다.", True)}</div>', scrim_h=40))


# ══════════════ 7. 백업 가져오기 미리보기 ══════════════
def diffrow(label, count, tone, desc, last=False):
    m = {"new": (C["POS"], C["POS_SOFT"]), "dup": (C["TAB_INK"], C["LINE_SOFT"]),
         "conf": (C["WARN"], C["WARN_SOFT"]), "chk": (C["SKY"], C["SKY_SOFT"])}
    col, bg = m[tone]
    return (f'<div style="display: flex; align-items: center; gap: 10px; min-height: 48px; '
            f'{"" if last else "border-bottom: 1px solid " + C["LINE_ROW"] + ";"}">'
            f'<span style="min-width: 34px; height: 24px; border-radius: 7px; background: {bg}; color: {col}; font-size: 12px; '
            f'font-weight: 700; display: flex; align-items: center; justify-content: center; padding: 0 7px;">{count}</span>'
            f'<div style="flex: 1; min-width: 0;"><div style="font-size: 13px; font-weight: 600; color: {C["INK"]};">{label}</div>'
            f'<div style="font-size: 11px; color: {C["INK3"]};">{desc}</div></div>'
            f'{icon("right", 15, C["INK4"], 2)}</div>')

w('ImportReview', sheet(
    '백업 불러오기', 'navi-backup-2026-09-01.json · 3만 4천 건 · 저장 전에 무엇이 바뀌는지 먼저 봅니다.',
    group('적용 방식', segmented(['기존에 추가', '전체 교체'], 0) +
          f'<div style="margin-top: 9px;">{note("추가는 겹치지 않는 기록만 넣습니다. 전체 교체를 고르면 현재 기록이 모두 사라져요.", "mute")}</div>') +
    group('불러올 항목', f'<div style="padding: 0 13px; background: {C["SURF"]}; border: 1px solid {C["LINE"]}; border-radius: 14px;">'
                          f'{diffrow("새로 추가", 24, "new", "거래 21 · 자산 2 · 목적지 1")}'
                          f'{diffrow("이미 있음 · 건너뜀", 8, "dup", "같은 거래 ID")}'
                          f'{diffrow("값이 다름 · 백업 우선", 2, "conf", "자산 평가액 2건")}'
                          f'{diffrow("검토 필요", 1, "chk", "연결된 계좌가 없는 거래 1건", last=True)}</div>') +
    group('적용 후', f'<div style="display: flex; gap: 8px;">'
                      f'<div style="flex: 1; padding: 12px; background: {C["INSET"]}; border-radius: 13px;">'
                      f'<div style="font-size: 11.5px; color: {C["INK3"]};">지금</div>'
                      f'<div style="font-size: 18px; font-weight: 600; color: {C["INK"]}; margin-top: 3px;">거래 132건</div>'
                      f'<div style="font-size: 11.5px; color: {C["INK3"]}; margin-top: 2px;">순자산 9,350만원</div></div>'
                      f'<div style="display: flex; align-items: center;">{icon("arrowr", 16, C["INK4"], 2.2)}</div>'
                      f'<div style="flex: 1; padding: 12px; background: {C["BRAND_SOFT"]}; border-radius: 13px;">'
                      f'<div style="font-size: 11.5px; color: {C["BRAND"]};">적용 후</div>'
                      f'<div style="font-size: 18px; font-weight: 600; color: {C["INK"]}; margin-top: 3px;">거래 153건</div>'
                      f'<div style="font-size: 11.5px; color: {C["INK3"]}; margin-top: 2px;">순자산 9,410만원</div></div></div>'),
    sheet_footer('취소', '이 내용으로 적용'),
    sticky=f'<div style="padding: 12px 18px; background: {C["INSET"]}; border-top: 1px solid {C["LINE"]}; flex-shrink: 0;">'
           f'{checkbox("바뀌는 내용을 확인했습니다.", True)}</div>', scrim_h=40))


# ══════════════ 8. 코칭 패널 ══════════════
def advice(tone, title, body, action, num):
    m = {"neg": (C["NEG"], C["NEG_SOFT"]), "warn": (C["WARN"], C["WARN_SOFT"]), "pos": (C["POS"], C["POS_SOFT"])}
    col, bg = m[tone]
    return (f'<div style="display: flex; gap: 11px; padding: 13px; border-radius: 14px; background: {C["SURF"]}; '
            f'border: 1px solid {C["LINE"]}; border-left: 3px solid {col};">'
            f'<span style="width: 22px; height: 22px; border-radius: 99px; background: {bg}; color: {col}; font-size: 11.5px; '
            f'font-weight: 700; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">{num}</span>'
            f'<div style="min-width: 0;"><div style="font-size: 14px; font-weight: 600; letter-spacing: -0.015em; color: {C["INK"]};">{title}</div>'
            f'<div style="font-size: 12.5px; line-height: 1.5; color: {C["INK2"]}; margin-top: 4px;">{body}</div>'
            f'<div style="font-size: 12.5px; font-weight: 600; color: {C["BRAND"]}; margin-top: 8px;">{action} &rsaquo;</div></div></div>')

w('CoachPanel', sheet(
    '코칭', '저장된 기록만 보고 드리는 조언이에요. 우선순위가 높은 순서입니다.',
    f'<div style="display: flex; flex-direction: column; gap: 9px;">'
    f'{advice("neg", "카드 할부 금리 14.5%를 먼저 정리하세요", "잔액은 전체의 2%뿐이지만 금리가 신용대출의 2.1배예요. 고금리 우선 전략에서 1순위입니다.", "상환 전략 열기", 1)}'
    f'{advice("warn", "주거/관리가 한도의 94%예요", "9월 8일인데 벌써 47만원을 썼어요. 관리비 결제일이 지난 뒤라면 정상 속도입니다.", "카테고리 한도 보기", 2)}'
    f'{advice("pos", "비상금이 생활비 5.8개월치까지 왔어요", "목표 6개월(1,500만원)까지 40만원 남았습니다. 월 35만원이면 다음 달에 닿아요.", "목적지 배분 조정", 3)}</div>'
    f'{foldrow("다른 안내 4개 더 보기", "낮은 우선순위")}'
    + group('카테고리 절감 가정',
            f'<div style="padding: 13px; background: {C["VIO_SOFT"]}; border-radius: 14px; border: 1px dashed {C["VIO_LINE"]};">'
            f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px;">'
            f'{badge("저장되지 않는 가정", "vio", "spark")}'
            f'<span style="font-size: 12.5px; font-weight: 600; color: {C["VIO_STRONG"]};">−15%</span></div>'
            f'<div style="margin-top: 10px;">{slider(37, C["VIO"])}</div>'
            f'<div style="display: flex; align-items: center; justify-content: space-between; margin-top: 4px;">'
            f'<span style="font-size: 11px; color: {C["INK4"]};">0%</span>'
            f'<span style="font-size: 11.5px; font-weight: 600; color: {C["VIO_STRONG"]};">월 31만원 절감 가정</span>'
            f'<span style="font-size: 11px; color: {C["INK4"]};">40%</span></div>'
            f'<div style="display: flex; gap: 8px; margin-top: 11px;">'
            f'<div style="flex: 1; padding: 10px 11px; background: {C["SURF"]}; border-radius: 11px;">'
            f'<div style="font-size: 11.5px; color: {C["INK3"]};">비상금 도착</div>'
            f'<div style="font-size: 15px; font-weight: 600; color: {C["VIO_STRONG"]}; margin-top: 2px;">7개월 빨라짐</div></div>'
            f'<div style="flex: 1; padding: 10px 11px; background: {C["SURF"]}; border-radius: 11px;">'
            f'<div style="font-size: 11.5px; color: {C["INK3"]};">10년 적립 효과</div>'
            f'<div style="font-size: 15px; font-weight: 600; color: {C["VIO_STRONG"]}; margin-top: 2px;">+4,227만원</div></div></div></div>'),
    btn('닫기', 'secondary', h=48), scrim_h=40))


# ══════════════ 9. 알림 패널 ══════════════
def alert(tone, ic, title, body, action, muted=False):
    m = {"neg": (C["NEG"], C["NEG_SOFT"]), "warn": (C["WARN"], C["WARN_SOFT"]),
         "sky": (C["SKY"], C["SKY_SOFT"]), "pos": (C["POS"], C["POS_SOFT"]), "mute": (C["INK3"], C["INSET"])}
    col, bg = m[tone]
    a = f'<div style="font-size: 12.5px; font-weight: 600; color: {C["BRAND"]}; margin-top: 7px;">{action} &rsaquo;</div>' if action else ''
    return (f'<div style="display: flex; gap: 11px; min-height: 60px; padding: 13px 0; border-bottom: 1px solid {C["LINE_ROW"]};">'
            f'<div style="width: 32px; height: 32px; border-radius: 10px; background: {bg}; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">{icon(ic, 16, col, 2)}</div>'
            f'<div style="min-width: 0;"><div style="font-size: 13.5px; font-weight: 600; color: {C["INK"]};">{title}</div>'
            f'<div style="font-size: 12px; line-height: 1.5; color: {C["INK3"]}; margin-top: 3px;">{body}</div>{a}</div></div>')

w('AlertsPanel', sheet(
    '알림 3건', '저장된 기록을 기준으로 만든 알림이에요. 읽어도 기록은 바뀌지 않습니다.',
    f'<div style="display: flex; flex-direction: column;">'
    f'{alert("warn", "warn", "주거/관리 한도의 94%를 썼어요", "47만원 / 50만원 · 이번 달 22일 남음", "카테고리 한도")}'
    f'{alert("neg", "bank", "카드 할부 금리가 14.5%예요", "보유 부채 중 가장 높습니다", "상환 전략")}'
    f'{alert("sky", "shield", "비상금이 목표까지 40만원 남았어요", "현재 5.8개월 · 1,460만원", "목적지 배분")}</div>'
    f'{note("자산을 <b style=font-weight:600>3개월</b> 넘게 갱신하지 않으면 여기에 알려드려요. 지금은 갱신이 필요한 자산이 없습니다.", "mute")}'
    + group('알림이 없을 때',
            f'<div style="display: flex; flex-direction: column; align-items: center; text-align: center; padding: 20px 10px; '
            f'background: {C["INSET"]}; border-radius: 14px;">'
            f'<div style="width: 40px; height: 40px; border-radius: 13px; background: {C["POS_SOFT"]}; display: flex; align-items: center; justify-content: center;">{icon("check", 20, C["POS"], 2.4)}</div>'
            f'<div style="font-size: 13.5px; font-weight: 600; color: {C["INK"]}; margin-top: 10px;">지금 조치할 것이 없어요</div>'
            f'<div style="font-size: 12px; color: {C["INK3"]}; margin-top: 4px;">한도·부채·비상금 모두 정상 범위입니다</div></div>'),
    btn('닫기', 'secondary', h=48), scrim_h=40))


# ══════════════ 10. 또래 기준 등록 ══════════════
w('PeerDialog', sheet(
    '20대 후반 비교 기준', '만 27~29세 구간에 쓸 기준을 직접 등록합니다. 앱이 만들어 주는 값이 아니에요.',
    note('NAVI에는 세부 연령별 통계가 <span style="font-weight:600">들어 있지 않습니다.</span> 여기 넣은 값은 화면에서 항상 “내가 등록한 기준”으로 표시되고, 순위나 상위 %로 바뀌지 않습니다.', 'warn', 'warn') +
    f'<div style="display: flex; gap: 10px;">{field("연령 구간", "20대 후반 · 만 27~29세", state="readonly")}</div>'
    f'<div style="display: flex; gap: 10px;">{field("평균 소비율", "62.0", "%", required=True)}{field("조사 인원", "1,200", "명", w=132)}</div>'
    f'<div style="display: flex; gap: 10px;">{field("기준 연도", "2025", "년", required=True, w=132)}{field("소비율 분모", "실수령 급여", state="readonly")}</div>'
    f'{field("자료 출처", "디자인 검증용 가상 기준", required=True, helper="화면에 그대로 표시됩니다")}'
    f'{note("분모가 실수령 급여가 아닌 통계라면 내 소비율과 직접 비교할 수 없어요. 출처의 기준을 꼭 확인하세요.", "mute")}',
    sheet_footer('취소', '기준 저장'), scrim_h=40,
    header_right=f'<div style="display: flex; align-items: center; gap: 8px; flex-shrink: 0;">{smallbtn("기준 삭제", "danger", "trash", h=32)}'
                 f'<div style="width: 36px; height: 36px; border-radius: 11px; background: {C["INSET"]}; display: flex; align-items: center; justify-content: center;">{icon("x", 17, C["INK2"], 2.2)}</div></div>'))


# ══════════════ 11. 확인 다이얼로그 모음 ══════════════
def confirm(ic, tone, title, body, cancel, ok, ok_kind="danger", extra=""):
    col, bg = (C["NEG"], C["NEG_SOFT"]) if tone == "neg" else (C["WARN"], C["WARN_SOFT"])
    return card(
        f'<div style="display: flex; gap: 12px;">'
        f'<div style="width: 38px; height: 38px; border-radius: 12px; background: {bg}; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">{icon(ic, 19, col, 2)}</div>'
        f'<div style="min-width: 0;"><div style="font-size: 15.5px; font-weight: 700; letter-spacing: -0.02em; color: {C["INK"]};">{title}</div>'
        f'<div style="font-size: 12.5px; line-height: 1.55; color: {C["INK2"]}; margin-top: 5px;">{body}</div></div></div>'
        f'{extra}<div style="display: flex; gap: 8px; margin-top: 14px;">'
        f'{btn(cancel, "secondary", h=44).replace("width: 100%;", "flex: 1;")}'
        f'{btn(ok, ok_kind, h=44).replace("width: 100%;", "flex: 1;")}</div>', pad="16px", radius=20)

w('Confirmations', state_sheet(
    '삭제 · 초기화 확인',
    '무엇이 함께 사라지는지 대상 이름과 영향을 항상 적습니다. 파괴적인 행동은 오른쪽, 취소는 왼쪽입니다.',
    [('A · 자산 삭제',
      confirm('trash', 'neg', 'ETF 계좌를 삭제할까요?',
              '평가액 4,890만원이 총자산에서 빠지고 순자산이 4,460만원이 됩니다. 이 계좌에 연결된 거래 12건은 <span style="font-weight:600">연결만 끊기고 남습니다.</span>',
              '취소', '삭제')),
     ('B · 거래 삭제 · 잔액 반영됨',
      confirm('trash', 'neg', '이 거래를 삭제할까요?',
              '9월 5일 · ETF 자동이체 300,000원. 생활비 통장 잔액이 <span style="font-weight:600">+30만원</span>, ETF 계좌가 <span style="font-weight:600">−30만원</span>으로 되돌아갑니다.',
              '취소', '삭제')),
     ('C · 목적지 삭제',
      confirm('trash', 'neg', '비상금 6개월을 삭제할까요?',
              '적립한 1,020만원 기록은 자산에 그대로 남습니다. 홈 대표 목적지가 <span style="font-weight:600">투자 계좌 5,000만원</span>으로 바뀝니다.',
              '취소', '삭제')),
     ('D · 반복 규칙 삭제',
      confirm('trash', 'warn', 'ETF 자동이체 규칙을 삭제할까요?',
              '앞으로 자동 생성되지 않습니다. 이미 만들어진 거래 8건은 남아요.',
              '취소', '규칙만 삭제', 'primary')),
     ('E · 전체 초기화',
      confirm('warn', 'neg', '모두 지우고 새로 시작할까요?',
              '거래 132건 · 자산 5건 · 부채 4건 · 목적지 4건 · 월 마감 6건이 <span style="font-weight:600">되돌릴 수 없이</span> 사라집니다.',
              '취소', '모두 삭제',
              extra=f'<div style="margin-top: 12px;">{note("먼저 백업을 내보내면 나중에 그대로 복구할 수 있어요.", "warn", "download")}</div>'
                    f'<div style="margin-top: 9px;">{checkbox("백업을 내보냈거나, 지워도 괜찮습니다.", False)}</div>'))],
    h=1300))
