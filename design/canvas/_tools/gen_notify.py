# -*- coding: utf-8 -*-
"""기기 알림 2장 — 2026-09-23 사용자 결정(「저장 순간 사건은 사용자가 이미 아는 것 · 기기 알림은 앱을 안 켜고 있을 때 시각으로 오는 것만」).
  SettingsNotify  설정 › 알림 시트(390 × 844) — 전체 스위치 · 조용한 시간 · 여섯 항목(기본 켬 3) · 테스트 · 다음 알림.
  NotifyCases     구현 참고 장 — 여섯 알림의 기기 카드 모양 · 문구 · 누르면 가는 곳 · 규칙.
회의 기록: navi-handoff/outputs/NAVI-NOTIFY-MEETING-2026-09-23.md. 다크는 darken 으로 같이 쓴다."""
import pathlib
from gen_common import C, icon, sheet, sheet_footer, note, toggle, btn, doc
from gen_v5 import spec_frame, mark
from darken import darken

OUT = pathlib.Path(__file__).resolve().parent.parent
KEEP_ALL_FROM = '-webkit-font-smoothing: antialiased; }'
KEEP_ALL_TO = '-webkit-font-smoothing: antialiased; word-break: keep-all; }'


def w(name, body):
    light = doc(body)
    assert light.count(KEEP_ALL_FROM) == 1
    light = light.replace(KEEP_ALL_FROM, KEEP_ALL_TO)
    (OUT / f'{name}.dc.html').write_text(light, encoding='utf-8')
    (OUT / f'Dark{name}.dc.html').write_text(darken(light, name), encoding='utf-8')
    print('wrote', name, '+ Dark' + name)


# 여섯 알림 — (키, 이름, 언제, 기본 켬, 기기 문구 제목, 기기 문구 본문, 누르면)
NOTIFY = [
    ('record', '오늘 소비 기록 확인', '매일 21:00 · 안 적은 날만', True,
     '오늘 소비 기록을 확인해 주세요', '날짜를 눌러 숫자만 넣으면 돼요', '홈 · 오늘 하루 시트'),
    ('close', '지난달 마감', '매월 1일 10:00 · 마감할 기록이 있을 때', True,
     '지난달 기록을 확인하고 마감해 주세요', '마감한 달이 예상의 기준이 돼요', '소비 · 지난달 마감'),
    ('hygiene', '자산 잔액 · 백업 확인', '매월 1일 · 마감 알림과 한 건', True,
     '자산 잔액과 백업을 확인해 주세요', '오래된 잔액은 순자산과 미래 예측에 영향을 줘요', '자산 · 구성'),
    ('reclose', '미마감 재안내', '매월 8일 10:00 · 아직 안 했을 때', False,
     '지난달이 아직 마감되지 않았어요', '기록을 확인하고 마감해 주세요', '소비 · 지난달 마감'),
    ('mid', '월 중간 점검', '매월 15일 10:00', False,
     '이번 달 소비와 남은 한도를 확인해 주세요', '지금 속도로 월말까지 괜찮은지 봐요', '소비 · 이번 달'),
    ('recur', '반복 거래 예정일 전날', '예정일 전날 09:00', False,
     '내일은 등록한 반복 거래 예정일이에요', '휴대폰 요금 · 매월 25일', '소비 · 내역 · 반복 거래'),
]


# ══════════════ 설정 › 알림 ══════════════
def group(label, inner, top=0):
    return (f'<div style="flex-shrink: 0; margin-top: {top}px;"><div style="font-size: 11px; font-weight: 600; letter-spacing: 0.07em; color: {C["INK3"]}; margin-bottom: 8px;">{label}</div>{inner}</div>')


def trow(label, sub, on, last=False, chip=None):
    bb = '' if last else f'border-bottom: 1px solid {C["LINE_ROW"]};'
    ch = (f'<span style="font-size: 12px; font-weight: 600; color: {C["BRAND"]}; white-space: nowrap; margin-right: 8px;">{chip} &rsaquo;</span>' if chip else '')
    return (f'<div style="display: flex; align-items: center; gap: 10px; height: 48px; {bb}">'
            f'<div style="display: flex; flex-direction: column; gap: 2px; flex: 1; min-width: 0;">'
            f'<span style="font-size: 13.5px; font-weight: 600; color: {C["INK"]};">{label}</span>'
            f'<span style="font-size: 11.5px; color: {C["INK3"]}; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">{sub}</span></div>{ch}{toggle(on)}</div>')


def inset(inner, pad='0 13px'):
    return f'<div style="background: {C["INSET"]}; border-radius: 14px; padding: {pad};">{inner}</div>'


rows = ''.join(trow(n, when, on, last=(i == len(NOTIFY) - 1), chip=('21:00' if k == 'record' else None))
               for i, (k, n, when, on, *_) in enumerate(NOTIFY))
# 세로 예산(본문 약 560px): 전체 스위치는 시트 머리 오른쪽, 항목 6행은 48px, 확인 구역은 한 행에 다음 알림을 부제로.
body = (
    group('조용한 시간', inset(
        f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px; height: 46px;">'
        f'<div style="display: flex; flex-direction: column; gap: 2px;"><span style="font-size: 13.5px; font-weight: 600; color: {C["INK"]};">22:00 ~ 08:00</span>'
        f'<span style="font-size: 11.5px; color: {C["INK3"]};">이 시간의 알림은 아침 8시 이후로 미뤄요</span></div>'
        f'<span style="font-size: 12px; font-weight: 600; color: {C["BRAND"]}; white-space: nowrap;">바꾸기 &rsaquo;</span></div>'))
    + group('알림', inset(rows), top=8)
    + group('확인', inset(
        f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px; height: 46px;">'
        f'<div style="display: flex; flex-direction: column; gap: 2px;"><span style="font-size: 13.5px; font-weight: 600; color: {C["INK"]};">테스트 알림 보내기</span>'
        f'<span style="font-size: 11.5px; color: {C["INK3"]};">다음 알림 오늘 21:00 · 오늘 소비 기록 확인</span></div>{icon("right", 16, C["INK4"], 2)}</div>'), top=8)
    + f'<div style="margin-top: 8px; flex-shrink: 0;">{note("절전 중이면 몇 분 늦을 수 있어요. 앱을 35일 넘게 안 열면 예약이 멈춰요.", "mute", "info")}</div>'
)
HEADER_RIGHT = (f'<div style="display: flex; align-items: center; gap: 8px; flex-shrink: 0; padding-top: 4px;">'
                f'<span style="font-size: 12px; font-weight: 600; color: {C["INK2"]};">기기 알림</span>{toggle(True)}</div>')
w('SettingsNotify', sheet('알림', '앱 안의 알림 창(종)과는 별개예요. 앱을 안 켜고 있을 때만 기기로 알려 드려요.', body, sheet_footer('닫기', '저장'), body_pb=14, header_right=HEADER_RIGHT))


# ══════════════ 구현 참고 장 — 여섯 알림 카드 ══════════════
def phone_notice(title, body_text, when):
    """안드로이드 알림 카드 모양(앱 아이콘 · 앱 이름 · 시각 · 제목 · 본문). 금액 · 이름은 기본 숨김이라 본문에 숫자가 없다."""
    return (f'<div style="width: 362px; background: {C["SURF"]}; border: 1px solid {C["LINE"]}; border-radius: 16px; padding: 12px 14px; '
            f'box-shadow: 0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24);">'
            f'<div style="display: flex; align-items: center; gap: 7px;"><div style="width: 16px; height: 16px; border-radius: 5px; background: linear-gradient(140deg, #3556E6 0%, #7A3FE4 100%);"></div>'
            f'<span style="font-size: 11.5px; font-weight: 600; color: {C["INK2"]};">NAVI</span><span style="font-size: 11.5px; color: {C["INK4"]};">· {when}</span></div>'
            f'<div style="font-size: 14px; font-weight: 700; letter-spacing: -0.01em; color: {C["INK"]}; margin-top: 7px;">{title}</div>'
            f'<div style="font-size: 12.5px; line-height: 1.45; color: {C["INK2"]}; margin-top: 2px;">{body_text}</div></div>')


def case(i, k, name, when, on, title, body_text, dest):
    dflt = (f'<span style="font-size: 10.5px; font-weight: 700; padding: 2px 7px; border-radius: 99px; background: {C["BRAND_SOFT"]}; color: {C["BRAND"]};">기본 켬</span>' if on
            else f'<span style="font-size: 10.5px; font-weight: 700; padding: 2px 7px; border-radius: 99px; background: {C["INSET"]}; color: {C["INK3"]};">설정에서 켬</span>')
    return (f'<div style="display: flex; flex-direction: column; gap: 8px; width: 362px;">'
            f'<div style="display: flex; align-items: center; gap: 7px;">{mark(i, pos="flex-shrink: 0;")}'
            f'<span style="font-size: 14px; font-weight: 700; color: {C["INK"]};">{name}</span>{dflt}</div>'
            f'<div style="font-size: 12px; color: {C["INK3"]}; margin-top: -4px;">{when}</div>'
            f'{phone_notice(title, body_text, when.split(" · ")[0].replace("매일 ", "").replace("매월 ", ""))}'
            f'<div style="font-size: 12px; color: {C["INK3"]};">누르면 → <b style="font-weight: 600; color: {C["INK2"]};">{dest}</b></div></div>')


cases = ''.join(case(i + 1, *row) for i, row in enumerate(NOTIFY))
RULES = [
    '기기 알림은 <b style="font-weight: 600;">앱을 안 켜고 있을 때 시각으로 오는 것</b>뿐입니다. 한도 초과 · 목적지 도착 · 부채 완제 · 다시 마감 · 자동 기록처럼 저장 순간 생기는 일은 사용자가 이미 아는 것이라 앱 안(완료 카드 · 알림 창 · 종 배지)에만 둡니다.',
    '문구에 금액 · 목표 이름을 넣지 않습니다 — 예약 시점 값이라 틀릴 수 있고, 알림 내용은 앱의 암호화 저장 밖에 놓입니다. 상세는 앱에서 봅니다.',
    '같은 종류는 하루 1번. 기록 알림은 이틀째부터 「어제 것도 같이 적을 수 있어요」, 일주일째부터는 주 1회로 줄입니다. 조용한 시간(22:00 ~ 08:00)의 알림은 아침 8시 이후로 미룹니다.',
    '누르면 그 화면 · 그 날짜로 갑니다. 알림으로 들어온 동안은 첫 실행 안내를 띄우지 않되, 본 것으로 저장하지는 않습니다.',
    '권한(안드로이드 13+)은 홈 안내가 끝난 뒤 개인 데이터일 때, 설명 카드에서 「켜기」를 누를 때 묻습니다. 샘플 모드에는 기기 알림이 없습니다. 정확 알람 권한은 쓰지 않습니다(「21시 무렵」).',
    '앱이 열릴 때마다 앞으로 35일치를 다시 예약하고 지난 예약은 지웁니다. 35일 넘게 안 열면 알림이 멈추고, 재부팅 · 강제 종료 뒤에는 늦거나 빠질 수 있습니다 — 설정 화면의 안내 줄이 이것을 말합니다.',
]
rules = ''.join(f'<li style="margin: 0 0 6px;">{r}</li>' for r in RULES)
body2 = (f'<div style="display: grid; grid-template-columns: repeat(3, 362px); gap: 26px 28px; align-items: start;">{cases}</div>'
         f'<div style="margin-top: 22px; padding: 16px 18px; background: {C["SURF"]}; border: 1px solid {C["LINE"]}; border-radius: 16px; max-width: 1140px;">'
         f'<div style="font-size: 13px; font-weight: 700; color: {C["INK"]}; margin-bottom: 8px;">규칙</div>'
         f'<ol style="margin: 0; padding-left: 18px; font-size: 12.5px; line-height: 1.55; color: {C["INK2"]};">{rules}</ol></div>')
NOTIFY_CASES_H = 830   # 실측: 마지막 요소 아래 792 + 여백
w('NotifyCases', spec_frame(1200, NOTIFY_CASES_H, '기기 알림 — 여섯 가지와 규칙',
                            '앱 안 알림 창과 별개로, 앱을 안 켜고 있을 때 시각으로 오는 안드로이드 로컬 알림입니다. 기본 켬 셋 · 설정에서 켜는 것 셋. 회의 기록은 NAVI-NOTIFY-MEETING-2026-09-23.md.',
                            body2, sub_w=760))
