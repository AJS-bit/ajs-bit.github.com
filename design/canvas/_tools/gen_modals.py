# -*- coding: utf-8 -*-
import pathlib
from gen_common import *

OUT = pathlib.Path(__file__).resolve().parent.parent


def w(name, body, keep_all=True):
    """모달 · 시트 장은 설명 문장이 많아 word-break: keep-all 을 기본으로 켠다(gen_common.doc 의 기본값은 그대로 False)."""
    (OUT / f'{name}.dc.html').write_text(doc(body, keep_all=keep_all), encoding='utf-8')
    print('wrote', name)


def group(label, inner, meta=None, fixed=False, mb=9):
    """fixed=True 면 본문이 넘칠 때 이 구역이 눌리지 않는다(목록 마지막 행이 상자 테두리에 닿는 것 방지)."""
    m = f'<span style="font-size: 11.5px; color: {C["INK3"]};">{meta}</span>' if meta else ''
    root = '<div style="flex-shrink: 0;">' if fixed else '<div>'
    return (f'{root}<div style="display: flex; align-items: baseline; justify-content: space-between; gap: 8px; margin-bottom: {mb}px;">'
            f'<span style="font-size: 11px; font-weight: 600; letter-spacing: 0.07em; color: {C["INK3"]};">{label}</span>{m}</div>{inner}</div>')


def foldrow(label, meta=None, open_=False):
    m = f'<span style="font-size: 12px; color: {C["INK3"]};">{meta}</span>' if meta else ''
    return (f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px; height: 48px; '
            f'padding: 0 13px; border-radius: 12px; background: {C["INSET"]}; flex-shrink: 0;">'
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
          f'<div style="display: flex; align-items: center; margin-top: 4px;">'
          f'<span style="flex: 1; font-size: 11px; color: {C["INK4"]};">0%</span>'
          f'<span style="font-size: 11.5px; font-weight: 600; color: {C["INK"]}; white-space: nowrap;">월 216만원까지</span>'
          f'<span style="flex: 1; text-align: right; font-size: 11px; color: {C["INK4"]};">100%</span></div>'
          f'<div style="margin-top: 11px;">{note("60%는 통계 평균이나 정답이 아니라 <b style=font-weight:600>바꿔도 되는 계획 시작값</b>입니다. 0%로 두어도 그대로 유지돼요.", "mute")}</div></div>') +
    group('추가 설정',
          f'<div style="display: flex; gap: 10px;">{field("부수입", "30", "만원", optional=True)}'
          f'{field("총자산", "1억 8,210", "만원", state="readonly")}</div>'
          f'<div style="display: flex; gap: 10px; margin-top: 12px;">{field("총부채", "8,860", "만원", state="readonly")}'
          f'{field("기대수익률", "2.4", "%", optional=True, w=124)}</div>'
          f'<div style="margin-top: 9px;">{note("자산 5건·부채 4건을 따로 입력해 두어서 총자산과 총부채는 그 합계로 표시됩니다. 자산·부채 화면에서 고칠 수 있어요.", "mute", "lock")}</div>'
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
    f'{solo(field("자산 이름", "ETF 계좌", required=True))}'
    f'<div style="display: flex; gap: 10px;">{select_field("유형", "투자")}{field("평가액", "4,890", "만원", required=True, w=142)}</div>'
    f'{solo(field("연 기대수익률", "6.5", "%", optional=True, helper="비워 두면 유형 기본값을 씁니다", w=None))}'
    f'{note("거래에서 <b style=font-weight:600>잔액에도 반영하기</b>를 켜면 이 계좌의 평가액이 함께 바뀝니다. 0원이어도 계좌 기록은 남습니다.", "mute")}',
    sheet_footer('취소', '자산 추가'), scrim_h=190, body_pb=14))


# ══════════════ 3. 부채 수정 ══════════════
w('DebtDialog', sheet(
    '카드 할부 수정', '거래에서 대출상환으로 연결된 부채예요.',
    f'{solo(field("부채 이름", "카드 할부", required=True))}'
    f'<div style="display: flex; gap: 10px;">{select_field("유형", "할부")}{field("남은 원금", "180", "만원", required=True, w=142)}</div>'
    f'<div style="display: flex; gap: 10px;">{field("연 금리", "14.5", "%", required=True)}{field("월 최소 상환액", "2", "만원", w=142)}</div>'
    f'{note("연 14.5%는 보유한 부채 중 가장 높아요. 고금리 우선 전략에서 1순위로 상환됩니다.", "warn", "warn")}'
    f'{note("남은 원금을 0으로 두면 완납으로 기록되고 목록에는 남습니다. 삭제하면 연결된 거래의 부채 연결이 끊깁니다.", "mute")}',
    sheet_footer('취소', '변경 저장'), scrim_h=110, body_pb=14,
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
    f'{solo(field("이름", "신용대출 완제", required=True))}'
    + group('갚을 부채 선택', f'<div style="padding: 6px 13px; background: {C["INSET"]}; border-radius: 14px; flex-shrink: 0;">{"".join(debtpick)}</div>',
            meta='2건 선택 · 2,380만원', fixed=True)
    + f'<div style="display: flex; gap: 10px;">{select_field("우선순위", "1순위 · 가장 먼저")}{field("목표 기한", "2029.06", optional=True, w=124)}</div>'
    + note('부채 상환 목적지는 적립 대신 <span style="font-weight:600">상환 계획</span>을 따릅니다. 목표액·적립액 입력란이 없고 홈 대표로도 지정할 수 있어요.', 'mute'),
    sheet_footer('취소', '목적지 추가'), scrim_h=40, body_pb=14))


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
    group('등록된 반복 거래', f'<div style="padding: 0 13px; background: {C["SURF"]}; border: 1px solid {C["LINE"]}; border-radius: 14px;">{"".join(rules)}</div>',
          meta='3건 · 활성 2건') +
    group('새 반복 거래',
          f'<div style="display: flex; gap: 10px;">{field("이름", "넷플릭스", required=True)}{field("금액", "13,500", "원", required=True, w=142)}</div>'
          f'<div style="display: flex; gap: 10px; margin-top: 12px;">{select_field("카테고리", "구독")}{field("결제일", "15", "일", w=104)}'
          f'{field("시작 월", "2026.10", w=112)}</div>'
          f'<div style="margin-top: 11px;">{note("이미 지난 달에는 만들어지지 않아요. 이미 만들어진 거래는 하나씩 고치거나 지울 수 있어요.", "mute")}</div>'),
    sheet_footer('닫기', '반복 거래 추가'), scrim_h=40))


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


# ══════════════ 6-2. 월 마감 확정 — v5-1 이후 (MonthlyCloseV5) ══════════════
# plan/v5-calendar.md §9-9 · §9-23 · §5-3: 체크박스 새 문구 + `자동으로 채워진 값` 위 분류 안 함 한 줄. v3 기준 그림 `MonthlyClose` 는 그대로 둔다.
# 한 줄이 늘어난 만큼 시트 본문이 길어져, 맨 아래 급여 안내(`급여를 비워 두면 …`)는 이 장에서 스크롤 아래로 내려간 것으로 보고 그리지 않는다.
# 8월 마감 창이므로 8월 값이다 — 8월 달력(gen_calendar.AUG)의 11일 6,700 · 24일 5,600 · 26일 8,900원 칸을 분류 안 함 3건으로 본다.
# 9월의 `분류 안 함 7건 32,000원`(내역 · 분류하기 · 소비 화면)과 같은 숫자로 읽히지 않게 달마다 다른 값을 쓴다.
from gen_calendar import AUG
UNCAT_AUG_DAYS = (11, 24, 26)
UNCAT_AUG_SUM = sum(AUG[d] for d in UNCAT_AUG_DAYS)
assert UNCAT_AUG_SUM == 21_200
UNCAT_LINE = (
    f'<div style="flex-shrink: 0; padding: 10px 12px; border: 1px solid {C["LINE"]}; border-radius: 12px; font-size: 12px; line-height: 1.5; color: {C["INK2"]};">'
    f'<span style="font-weight: 600; color: {C["INK"]};">분류 안 함 {len(UNCAT_AUG_DAYS)}건 · {UNCAT_AUG_SUM:,}원이 기타로 들어가요</span> · 다음 달 한도 배분에도 기타로 들어가요 · '
    f'<span style="font-weight: 600; color: {C["BRAND"]}; white-space: nowrap;">지금 분류 &rsaquo;</span></div>')

w('MonthlyCloseV5', sheet(
    '2026년 8월 마감', '그 달의 실제 수치를 확정합니다. 저장한 값으로만 과거 소비율을 계산해요.',
    note('이미 <span style="font-weight:600">2026년 9월 2일</span>에 마감한 달입니다. 다시 저장하면 기존 마감값을 덮어씁니다.', 'warn', 'warn') +
    group('그 달의 실제 수치', f'<div style="display: flex; gap: 10px;">{field("총수입", "3,900,000", "원", required=True)}'
                                f'{field("그중 실수령 급여", "3,600,000", "원", required=True)}</div>'
                                f'<div style="display: flex; gap: 10px; margin-top: 12px;">{field("대출상환", "920,000", "원")}'
                                f'{field("저축·투자 이체", "630,000", "원")}</div>', meta='원 단위') +
    UNCAT_LINE +
    group('자동으로 채워진 값',
          f'<div style="padding: 2px 13px; background: {C["INSET"]}; border-radius: 14px;">'
          f'{kv("일반 소비 합계", "2,043,800원")}{kv("급여 대비 소비율", "56.8%", C["POS"])}'
          f'{kv("월말 자산 총액", "180,400,000원")}{kv("월말 부채 총액", "89,200,000원", last=True)}</div>'),
    sheet_footer('취소', '마감 저장'),
    sticky=f'<div style="padding: 12px 18px; background: {C["INSET"]}; border-top: 1px solid {C["LINE"]}; flex-shrink: 0;">'
           f'{checkbox("이 달의 수입·상환·잔액을 확인했고, 빠진 소비 기록이 없는지 살펴봤어요", True)}</div>', scrim_h=40,
    # 급여 안내를 뺀 뒤 `자동으로 채워진 값` 회색 상자가 같은 회색의 확인 줄에 3.75px 로 붙었다 — 구역 간격 15 → 12(3곳 = 9px)로 상자 아래 약 12.75px 를 낸다.
    # body_pb 는 글꼴 차이로 본문이 조금 길어져도 상자가 확인 줄에 닿지 않게 하는 아래 여백. v3 `MonthlyClose` 는 기본값 그대로.
    body_gap=12, body_pb=12))


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
    '백업 불러오기', 'navi-backup-2026-09-01.json · 기록 35건<br>적용하기 전에 무엇이 바뀌는지 먼저 확인하세요.',
    group('적용 방식', segmented(['기존에 추가', '전체 교체'], 0) +
          f'<div style="margin-top: 9px;">{note("추가는 겹치지 않는 기록만 넣습니다. 전체 교체를 고르면 현재 기록이 모두 사라져요.", "mute")}</div>') +
    group('불러올 항목', f'<div style="padding: 0 13px; background: {C["SURF"]}; border: 1px solid {C["LINE"]}; border-radius: 14px;">'
                          f'{diffrow("새로 추가", 24, "new", "거래 21 · 자산 2 · 목적지 1")}'
                          f'{diffrow("이미 있는 기록", 8, "dup", "같은 거래라 건너뜁니다")}'
                          f'{diffrow("값이 다른 기록", 2, "conf", "자산 평가액 2건 · 백업 파일 값으로 바뀝니다")}'
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
            f'<div style="font-size: 12.5px; font-weight: 600; color: {C["BRAND"]}; margin-top: 6px;">{action} &rsaquo;</div></div></div>')

w('CoachPanel', sheet(
    '코칭', '저장된 기록을 보고 중요한 순서로 알려드려요.',
    f'<div style="display: flex; flex-direction: column; gap: 8px; flex-shrink: 0;">'
    f'{advice("neg", "카드 할부 금리 14.5%를 먼저 정리하세요", "잔액은 전체의 2%뿐이지만 금리가 신용대출의 2.1배예요. 고금리 우선 전략에서 1순위입니다.", "상환 전략 열기", 1)}'
    f'{advice("warn", "주거/관리가 한도의 94%예요", "9월 8일인데 벌써 47만원을 썼어요. 관리비 결제일이 지난 뒤라면 정상 속도입니다.", "카테고리 한도 보기", 2)}'
    f'{advice("pos", "비상금이 목표의 68%까지 왔어요", "목표 1,500만원까지 480만원 남았습니다. 월 35만원이면 2027년 11월에 닿아요.", "목적지 배분 조정", 3)}</div>'
    f'{foldrow("다른 안내 4개 더 보기", "낮은 우선순위")}'
    + group('카테고리 절감 가정',
            f'<div style="padding: 11px 13px; background: {C["VIO_SOFT"]}; border-radius: 14px; border: 1px dashed {C["VIO_LINE"]};">'
            f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px;">'
            f'{badge("저장되지 않는 가정", "vio", "spark")}'
            f'<span style="font-size: 12.5px; font-weight: 600; color: {C["VIO_STRONG"]};">−15%</span></div>'
            f'<div style="margin-top: 8px;">{slider(37, C["VIO"])}</div>'
            f'<div style="display: flex; align-items: center; margin-top: 4px;">'
            f'<span style="flex: 1; font-size: 11px; color: {C["INK4"]};">0%</span>'
            f'<span style="font-size: 11.5px; font-weight: 600; color: {C["VIO_STRONG"]}; white-space: nowrap;">월 31만원 절감 가정</span>'
            f'<span style="flex: 1; text-align: right; font-size: 11px; color: {C["INK4"]};">40%</span></div>'
            f'<div style="display: flex; gap: 8px; margin-top: 9px;">'
            f'<div style="flex: 1; padding: 8px 11px; background: {C["SURF"]}; border-radius: 11px;">'
            f'<div style="font-size: 11.5px; color: {C["INK3"]};">비상금 도착</div>'
            f'<div style="font-size: 15px; font-weight: 600; color: {C["VIO_STRONG"]}; margin-top: 2px;">6개월 빨라짐</div></div>'
            f'<div style="flex: 1; padding: 8px 11px; background: {C["SURF"]}; border-radius: 11px;">'
            f'<div style="font-size: 11.5px; color: {C["INK3"]};">10년 적립 효과</div>'
            f'<div style="font-size: 15px; font-weight: 600; color: {C["VIO_STRONG"]}; margin-top: 2px;">+4,227만원</div></div></div></div>', mb=7),
    btn('닫기', 'secondary', h=48), scrim_h=40, body_gap=12), keep_all=True)


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

ALERTS_DESC = '저장된 기록을 기준으로 만든 알림이에요. 읽어도 기록은 바뀌지 않아요.'
STALE_NOTE = note("자산을 <b style=font-weight:600>3개월</b> 넘게 갱신하지 않으면 여기에 알려드려요. 지금은 갱신이 필요한 자산이 없습니다.", "mute")

w('AlertsPanel', sheet(
    '알림 3건', ALERTS_DESC,
    f'<div style="display: flex; flex-direction: column;">'
    f'{alert("warn", "warn", "주거/관리 한도의 94%를 썼어요", "47만원 / 50만원 · 이번 달 22일 남음", "카테고리 한도")}'
    f'{alert("neg", "bank", "카드 할부 금리가 14.5%예요", "보유 부채 중 가장 높습니다", "상환 전략")}'
    f'{alert("sky", "shield", "비상금이 목표의 68%예요", "1,020 / 1,500만원 · 480만원 남음", "목적지 배분")}</div>'
    f'{STALE_NOTE}',
    btn('닫기', 'secondary', h=48), scrim_h=40))

# 알림이 하나도 없을 때 — 예전에는 AlertsPanel 안에 '알림이 없을 때'라는 설계자용 소제목과 함께 끼어 있었다
w('AlertsEmpty', sheet(
    '알림', ALERTS_DESC,
    f'<div style="display: flex; flex-direction: column; align-items: center; text-align: center; padding: 20px 10px; '
    f'background: {C["INSET"]}; border-radius: 14px;">'
    f'<div style="width: 40px; height: 40px; border-radius: 13px; background: {C["POS_SOFT"]}; display: flex; align-items: center; justify-content: center;">{icon("check", 20, C["POS"], 2.4)}</div>'
    f'<div style="font-size: 13.5px; font-weight: 600; color: {C["INK"]}; margin-top: 10px;">지금 조치할 것이 없어요</div>'
    f'<div style="font-size: 12px; color: {C["INK3"]}; margin-top: 4px;">한도·부채·비상금 모두 정상 범위입니다</div></div>'
    f'{STALE_NOTE}',
    btn('닫기', 'secondary', h=48), scrim_h=40))


# ══════════════ 10. 또래 기준 등록 ══════════════
w('PeerDialog', sheet(
    '20대 후반 비교 기준', '만 27~29세 구간에 쓸 기준을 직접 등록해요. 앱이 만든 값이 아니에요.',
    note('NAVI에는 세부 연령별 통계가 <span style="font-weight:600">들어 있지 않습니다.</span> 여기 넣은 값은 화면에서 항상 “내가 등록한 기준”으로 표시되고, 순위나 상위 %로 바뀌지 않습니다.', 'warn', 'warn') +
    f'<div style="display: flex; gap: 10px;">{field("연령 구간", "20대 후반 · 만 27~29세", state="readonly")}</div>'
    f'<div style="display: flex; gap: 10px;">{field("평균 소비율", "62.0", "%", required=True)}{field("조사 인원", "1,200", "명", w=132)}</div>'
    f'<div style="display: flex; gap: 10px;">{field("기준 연도", "2025", "년", required=True, w=132)}{field("소비율 계산 기준", "실수령 급여", state="readonly")}</div>'
    f'{solo(field("자료 출처", "직접 입력한 예시 기준", required=True, helper="화면에 그대로 표시됩니다"))}'
    f'{note("실수령 급여가 아닌 다른 소득을 기준으로 한 통계라면 내 소비율과 바로 비교할 수 없어요. 출처의 기준을 꼭 확인하세요.", "mute")}',
    sheet_footer('취소', '기준 저장'), scrim_h=40, body_pb=14,
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
    '지우기 전에 한 번 더 묻는 창 다섯 가지입니다.',
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
     ('D · 반복 거래 삭제',
      confirm('trash', 'warn', 'ETF 자동이체 반복 거래를 삭제할까요?',
              '앞으로는 자동으로 만들어지지 않아요. 이미 만들어진 거래 8건은 남아요.',
              '취소', '반복만 삭제', 'primary')),
     ('E · 전체 초기화',
      confirm('warn', 'neg', '모두 지우고 새로 시작할까요?',
              '거래 132건 · 자산 5건 · 부채 4건 · 목적지 4건 · 월 마감 6건이 <span style="font-weight:600">되돌릴 수 없이</span> 사라집니다.',
              '취소', '모두 삭제',
              extra=f'<div style="margin-top: 12px;">{note("먼저 백업을 내보내면 나중에 그대로 복구할 수 있어요.", "warn", "download")}</div>'
                    f'<div style="margin-top: 9px;">{checkbox("백업을 내보냈거나, 지워도 괜찮습니다.", False)}</div>'))],
    h=1245, pill='구현 참고 · 앱 화면이 아닙니다'), keep_all=True)


# ══════════════ 12. 구현 참고 장 틀 — gen_v5.spec_frame 과 같은 모양 ══════════════
# gen_v5 를 import 하면 v4 · v5 장 전체를 다시 쓰는 부작용이 있어, 승인된 틀(알약 · 제목 · 부제 · 번호 mark · 번호별 설명 줄)만 같은 값으로 옮겨 둔다.
def spec_frame(w_, h_, title, sub, body, sub_w=640):
    chip = (f'<span style="align-self: flex-start; font-size: 11px; font-weight: 600; letter-spacing: 0.02em; color: {C["INK2"]}; '
            f'border: 1px solid {C["LINE"]}; background: {C["SURF"]}; border-radius: 99px; padding: 4px 10px; white-space: nowrap;">구현 참고 · 앱 화면이 아닙니다</span>')
    return (f'<div style="width: {w_}px; height: {h_}px; background: {C["BG"]}; color: {C["INK"]}; padding: 28px 30px 30px; display: flex; '
            f'flex-direction: column; gap: 10px; overflow: hidden; font-variant-numeric: tabular-nums;">{chip}'
            f'<h2 style="margin: 2px 0 0; font-size: 20px; font-weight: 700; letter-spacing: -0.025em; color: {C["INK"]};">{title}</h2>'
            f'<p style="margin: 0 0 8px; font-size: 13px; line-height: 1.55; color: {C["INK3"]}; max-width: {sub_w}px;">{sub}</p>{body}</div>')


def mark(n, pos='flex-shrink: 0; margin-top: 1px;'):
    return (f'<span style="{pos} width: 17px; height: 17px; border-radius: 99px; background: {C["INK"]}; color: #FFFFFF; '
            f'font-size: 10.5px; font-weight: 700; display: inline-flex; align-items: center; justify-content: center; '
            f'box-shadow: 0 0 0 2px {C["SURF"]};">{n}</span>')


def guide_row(n, name, meaning, second, last=False):
    border = '' if last else f'border-bottom: 1px solid {C["LINE_ROW"]};'
    lead = mark(n) if n is not None else '<span style="width: 17px; flex-shrink: 0;"></span>'      # n=None: 번호 없는 딸린 줄(들여쓰기만)
    return (f'<div style="display: flex; gap: 11px; padding: 10px 0; {border}">{lead}'
            f'<div style="display: flex; flex-direction: column; gap: 2px; min-width: 0;">'
            f'<div style="font-size: 13.5px; line-height: 1.4; color: {C["INK2"]};"><b style="font-weight: 600; color: {C["INK"]};">{name}</b>&nbsp;&nbsp;{meaning}</div>'
            f'<div style="font-size: 12px; line-height: 1.45; color: {C["INK3"]};">{second}</div></div></div>')


def case_cap(n, title, desc):
    return (f'<div><div style="display: flex; align-items: center; gap: 7px;">{mark(n, pos="flex-shrink: 0;")}'
            f'<span style="font-size: 14px; font-weight: 700; letter-spacing: -0.01em; color: {C["INK"]};">{title}</span></div>'
            f'<div style="font-size: 12px; line-height: 1.5; color: {C["INK3"]}; margin-top: 3px;">{desc}</div></div>')


# ══════════════ 13. 거래 추가 — 하루 시트에서 넘어온 초안 (TransactionAddFromDaySheet) ══════════════
# plan/v5-calendar.md §4-2 · §9-5 · §12-28 · §12-29: 하루 시트의 `저축·투자로 기록 ›`가 그 종류를 미리 고르고 날짜 · 금액 · 메모를 채운 채
# 소비 탭 `거래 추가`를 연다. 필드 순서는 그대로. 손으로 쓴 TransactionAdd.dc.html 을 읽어 값만 바꾼다(그 파일은 고치지 않는다).
def _swap(src, old, new, count=1):
    assert src.count(old) == count, (old[:60], src.count(old))
    return src.replace(old, new)


def tx_add_from_day_sheet():
    src = (OUT / 'TransactionAdd.dc.html').read_text(encoding='utf-8')
    start = src.index('  <div style="flex: 1; min-height: 0; background: #FFFFFF; border-radius: 26px 26px 0 0;')
    end = src.index('</x-dc>')
    sheet_html = src[start:end].rstrip()
    assert sheet_html.endswith('</div>')
    sheet_html = sheet_html[:-len('</div>')].rstrip()            # 바깥 390 × 844 틀의 닫는 태그는 뺀다
    # 폰 틀 없이 창만 — 높이는 내용만큼(가운데 본문의 flex: 1 을 푼다)
    sheet_html = _swap(sheet_html, 'flex: 1; min-height: 0; background: #FFFFFF; border-radius: 26px 26px 0 0;',
                       f'background: #FFFFFF; border: 1px solid {C["LINE"]}; border-radius: 26px 26px 18px 18px;')
    sheet_html = _swap(sheet_html, 'flex: 1; min-height: 0; overflow: hidden; padding: 14px 18px 0;', 'padding: 14px 18px 14px;')
    m = lambda n: mark(n, pos='margin-left: 6px; vertical-align: -3px; flex-shrink: 0;')       # 버튼 안(이미 flex 가운데 맞춤)

    # 라벨 옆 번호: 17px inline-flex 배지를 글줄에 그대로 넣으면 그 라벨 줄만 18 → 21px 로 커져 옆 칸(날짜 ↔ 금액)과 3px 어긋난다.
    # 라벨을 flex 가운데 맞춤으로 바꾸고 배지의 위아래 margin 을 -2px 로 눌러(차지하는 높이 13px < 글줄 18px) 줄 높이는 글자가 정하게 한다.
    # 원래 글자는 <span> 하나로 감싼다 — flex 안에서 `메모 ` 뒤 빈칸이 사라지지 않게.
    def label_mark(html, inner, n):
        old = f'margin-bottom: 7px;">{inner}</div>'
        new = (f'margin-bottom: 7px; display: flex; align-items: center;"><span>{inner}</span>'
               f'{mark(n, pos="margin: -2px 0 -2px 6px; flex-shrink: 0;")}</div>')
        return _swap(html, old, new)
    # ① 거래 종류 — 저축·투자가 미리 선택됨
    on = 'background: #FFFFFF; display: flex; align-items: center; justify-content: center; font-size: 13px; font-weight: 600; color: #101828; box-shadow: 0 1px 2px rgba(16,24,40,.08);">'
    off = 'display: flex; align-items: center; justify-content: center; font-size: 13px; font-weight: 500; color: #5B6880;">'
    sheet_html = _swap(sheet_html, on + '일반 소비', off + '일반 소비')
    sheet_html = _swap(sheet_html, off + '저축·투자', on + '저축·투자')
    sheet_html = label_mark(sheet_html, '거래 종류', 1)
    # ② 날짜 9월 8일 · 금액 12,000
    assert sheet_html.count('2026. 09. 08') == 1
    sheet_html = label_mark(sheet_html, '날짜', 2)
    sheet_html = _swap(sheet_html, '>32,000</span>', '>12,000</span>')
    # 카테고리 — 저축·투자는 종류가 곧 카테고리라 고르는 칩 대신 잠긴 칸
    c0 = sheet_html.index('<div style="display: flex; gap: 7px; overflow: hidden;">')
    c1 = sheet_html.index('더보기</div>', c0) + len('더보기</div>')
    c1 = sheet_html.index('</div>', c1) + len('</div>')
    locked = (f'<div style="display: flex; align-items: center; gap: 8px; height: 46px; padding: 0 12px; border-radius: 11px; border: 1px solid {C["LINE"]}; background: {C["INSET"]};">'
              f'{catdot("저축/투자", 8)}<span style="flex: 1; font-size: 15px; font-weight: 500; color: {C["INK2"]};">저축/투자</span>{icon("lock", 15, C["INK4"], 1.9)}</div>')
    sheet_html = sheet_html[:c0] + locked + sheet_html[c1:]
    sheet_html = _swap(sheet_html, '카테고리 <span style="color: #C0342F;">*</span></span>', '카테고리</span>')
    sheet_html = _swap(sheet_html, '13개 중 선택', '거래 종류에 따라 정해져요')
    # ③ 메모
    sheet_html = _swap(sheet_html, '점심 · 팀 회식', '적금 추가 납입')
    sheet_html = label_mark(sheet_html, '메모 <span style="font-weight: 500; color: #697182;">선택 사항</span>', 3)
    # 잔액 반영 — 하루 시트는 계좌를 넘기지 않으므로 꺼진 채, 계좌 고르는 줄은 없다
    sheet_html = _swap(sheet_html, 'background: #3556E6; padding: 3px; display: flex; justify-content: flex-end; flex-shrink: 0;">',
                       f'background: {C["LINE"]}; padding: 3px; display: flex; justify-content: flex-start; flex-shrink: 0;">')
    a0 = sheet_html.index('<div style="display: flex; align-items: center; justify-content: space-between; gap: 10px; height: 44px; margin-top: 10px;')
    a1 = sheet_html.index('</svg>', a0)
    a1 = sheet_html.index('</div>', a1) + len('</div>')
    a1 = sheet_html.index('</div>', a1) + len('</div>')
    sheet_html = sheet_html[:a0].rstrip() + '\n' + sheet_html[a1:]
    # 맨 아래 안내 — 창에 1px 테두리가 생겨 안쪽 폭이 2px 줄면서 `저축` / `·투자 이체와…`로 꺾였다. 한 용어는 한 줄에 묶는다(원본 파일은 그대로)
    sheet_html = _swap(sheet_html, '저축·투자 이체와 대출상환은', '<span style="white-space: nowrap;">저축·투자</span> 이체와 대출상환은')
    # ④ 거래 저장
    sheet_html = _swap(sheet_html, 'font-weight: 600; color: #FFFFFF;">거래 저장</div>',
                       f'font-weight: 600; color: #FFFFFF;">거래 저장{m(4)}</div>')
    return sheet_html


TXADD_GUIDE = [
    (1, '거래 종류', '<b style="font-weight: 600;">저축·투자</b>가 미리 선택된 채 열립니다.',
     '하루 시트의 <b style="font-weight: 600;">저축·투자로 기록 &rsaquo;</b>를 눌렀을 때입니다. <b style="font-weight: 600;">대출상환으로 기록 &rsaquo;</b>를 눌렀으면 대출상환이 선택됩니다.'),
    (2, '날짜 · 금액', '하루 시트에 적어 둔 값 그대로 채워집니다.', '9월 8일 시트에서 12,000원을 적고 넘어온 그림입니다. 여기서 고칠 수 있습니다.'),
    (3, '메모', '하루 시트에 적은 메모도 함께 넘어옵니다.', '칸 순서는 기존 거래 추가와 같습니다(거래 종류 → 날짜 · 금액 → 카테고리 → 메모 → 잔액 반영). 순서를 바꾸지 않습니다.'),
    (4, '거래 저장', '저장하면 소비 탭에 머물지 않고 <b style="font-weight: 600;">홈으로 돌아와 완료 카드</b>가 뜹니다.',
     '저장에 성공하면 출발한 하루 시트의 9월 8일 초안을 비웁니다. 취소하거나 저장에 실패하면 초안은 남습니다.'),
]


def flow_step(text, strong=False):
    return (f'<span style="display: inline-flex; align-items: center; height: 32px; padding: 0 12px; border-radius: 10px; white-space: nowrap; flex-shrink: 0; '
            f'font-size: 12.5px; font-weight: 600; ' +
            (f'background: {C["BRAND_SOFT"]}; color: {C["BRAND"]};' if strong else f'background: {C["INSET"]}; color: {C["INK2"]};') + f'">{text}</span>')


txadd_flow = card(
    f'<div style="font-size: 12px; font-weight: 700; color: {C["INK"]};">어디서 와서 어디로 가나</div>'
    f'<div style="display: flex; align-items: center; flex-wrap: wrap; gap: 6px; margin-top: 9px;">'
    + flow_step('홈 · 하루 시트') + icon("arrowr", 14, C["INK4"], 2.2)
    + flow_step('저축·투자로 기록 &rsaquo;') + icon("arrowr", 14, C["INK4"], 2.2)
    + flow_step('소비 탭 · 거래 추가', strong=True) + icon("arrowr", 14, C["INK4"], 2.2)
    + flow_step('거래 저장') + icon("arrowr", 14, C["INK4"], 2.2)
    + flow_step('홈 · 완료 카드') + '</div>'
    f'<p style="margin: 10px 0 0; font-size: 12px; line-height: 1.55; color: {C["INK3"]};">하루 시트에는 거래 종류 · 잔액 반영 · 계좌 선택이 없어서, 저축·투자와 대출상환은 이 창에서 남깁니다. '
    f'소비율에는 들어가지 않습니다. 수입 · 환불은 어디에서도 안내하지 않습니다.</p>', pad='13px 16px')

txadd_guide = card(''.join(guide_row(*r, last=(i == len(TXADD_GUIDE) - 1)) for i, r in enumerate(TXADD_GUIDE)), pad='4px 16px')

w('TransactionAddFromDaySheet', spec_frame(
    960, 850, '거래 추가 — 하루 시트에서 넘어왔을 때',
    '하루 시트 아래의 링크 「저축·투자로 기록 ›」를 누르면 소비 탭의 거래 추가 창이 이 모습으로 열립니다. 왼쪽 창의 번호를 오른쪽에서 찾으세요.',
    f'<div style="display: flex; gap: 28px; align-items: flex-start;">'
    f'<div style="width: 390px; flex-shrink: 0;">{tx_add_from_day_sheet()}</div>'
    f'<div style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 12px;">{txadd_guide}{txadd_flow}</div></div>', sub_w=760))
