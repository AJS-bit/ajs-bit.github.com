# -*- coding: utf-8 -*-
"""기기 알림 2장 — 2026-09-23 사용자 결정(「저장 순간 사건은 사용자가 이미 아는 것 · 기기 알림은 앱을 안 켜고 있을 때 시각으로 오는 것만」).
  SettingsNotify  설정 › 알림 시트(390 × 844) — 전체 스위치 · 조용한 시간 · 여섯 항목(기본 켬 3) · 테스트 · 다음 알림.
  NotifyCases     구현 참고 장 — 여섯 알림의 기기 카드 모양 · 문구 · 누르면 가는 곳 · 규칙.
회의 기록: navi-handoff/outputs/NAVI-NOTIFY-MEETING-2026-09-23.md. 다크는 darken 으로 같이 쓴다."""
import brand_mark
import pathlib
from gen_common import C, icon, sheet, sheet_footer, note, toggle, btn, doc
from gen_v5 import spec_frame, mark
from darken import darken
from nobreak import nobreak          # 낱말 중간 꺾임 묶음(D14 · 파일 이름 NAVI-NOTIFY-… 등)

OUT = pathlib.Path(__file__).resolve().parent.parent
KEEP_ALL_FROM = '-webkit-font-smoothing: antialiased; }'
KEEP_ALL_TO = '-webkit-font-smoothing: antialiased; word-break: keep-all; }'


def w(name, body):
    light = doc(body)
    assert light.count(KEEP_ALL_FROM) == 1
    light = nobreak(light.replace(KEEP_ALL_FROM, KEEP_ALL_TO))
    (OUT / f'{name}.dc.html').write_text(light, encoding='utf-8')
    (OUT / f'Dark{name}.dc.html').write_text(darken(light, name), encoding='utf-8')
    print('wrote', name, '+ Dark' + name)


# 여섯 알림 — (키, 이름, 언제, 기본 켬, 기기 문구 제목, 기기 문구 본문, 누르면)
# 앱 lib/navi-notify.ts · notify-settings.tsx(a724aac) 문구. 금액 · 이름은 문구에 넣지 않는다(반복 기록 이름만 예외 — 규칙 2).
NOTIFY = [
    ('record', '오늘 소비 기록 확인', '매일 21:00 무렵 · 안 적은 날만', True,
     '오늘 소비 기록을 확인해 주세요', '날짜를 눌러 숫자만 넣으면 돼요<br><span style="color: #626D88;">이틀째부터: 어제 것도 같이 적을 수 있어요 · 조용한 시간에 미뤄지면 제목이 「9월 7일 소비 기록을 확인해 주세요」</span>', '홈 · 오늘 하루 시트'),
    ('close', '지난달 마감', '매월 1일 10:00 · 마감할 기록이 있을 때', True,
     '지난달 기록을 확인하고 마감해 주세요', '마감한 달이 예상의 기준이 돼요<br><span style="color: #626D88;">잔액 · 백업 알림과 한 건이면: … · 자산 잔액과 백업도 확인해 주세요</span>', '소비 · 그 달 월 요약 + 「8월 마감」 창'),
    ('hygiene', '자산 잔액 · 백업 확인', '매월 1일 · 마감 알림과 한 건', True,
     '자산 잔액과 백업을 확인해 주세요', '기록한 잔액과 백업을 확인해 주세요<br><span style="color: #626D88;">백업한 적이 없으면: 이 기기의 백업 기록이 없어요</span>', '자산 · 잔액 한 번에 확인'),
    ('reclose', '미마감 재안내', '매월 8일 10:00 · 아직 안 했을 때', False,
     '지난달이 아직 마감되지 않았어요', '지난달 기록을 확인하고 마감해 주세요', '소비 · 그 달 월 요약 + 「8월 마감」 창'),      # 앱 lib/navi-notify.ts reclose 본문(2026-09-27 fix-up)
    ('mid', '월 중간 점검', '매월 15일 10:00', False,
     '이번 달 소비와 남은 한도를 확인해 주세요', '소비 화면에서 이번 달 기록을 확인할 수 있어요', '소비 · 이번 달'),
    ('recur', '반복 기록 예정일 전날', '예정일 전날 09:00', False,
     '내일은 등록한 반복 기록 예정일이에요', '휴대폰 요금 · 매월 25일<br><span style="color: #626D88;">둘 이상이면: 휴대폰 요금 외 1건 · 반복 기록을 확인해 주세요</span>', '소비 · 내역 · 반복 기록'),
]


# ══════════════ 설정 › 알림 ══════════════
def group(label, inner, top=0):
    return (f'<div style="flex-shrink: 0; margin-top: {top}px;"><div style="font-size: 11px; font-weight: 600; line-height: 16.5px; letter-spacing: 0.07em; color: {C["INK3"]}; margin-bottom: 8px;">{label}</div>{inner}</div>')


def trow(label, sub, on, last=False, chip=None):
    bb = '' if last else f'border-bottom: 1px solid {C["LINE_ROW"]};'
    ch = (f'<span style="font-size: 12px; font-weight: 600; color: {C["BRAND"]}; white-space: nowrap; margin-right: 8px;">{chip} &rsaquo;</span>' if chip else '')
    # 앱 .navi-notify-row — 위아래 8 · 제목 13.5 / 600 · 줄 19.6 · 부제 11.5 · 줄 17.25 → 55 + 줄 사이 선 1 = 56(2026-09-27 fix-up 4 · 예전 48)
    return (f'<div style="display: flex; align-items: center; gap: 10px; min-height: 55px; padding: 8px 0; {bb}">'
            f'<div style="display: flex; flex-direction: column; gap: 2px; flex: 1; min-width: 0;">'
            f'<span style="font-size: 13.5px; font-weight: 600; line-height: 19.6px; color: {C["INK"]};">{label}</span>'
            f'<span style="font-size: 11.5px; line-height: 17.25px; color: {C["INK3"]}; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">{sub}</span></div>{ch}{toggle(on)}</div>')


def inset(inner, pad='0 13px'):
    return f'<div style="background: {C["INSET"]}; border-radius: 14px; padding: {pad};">{inner}</div>'


rows = ''.join(trow(n, when, on, last=(i == len(NOTIFY) - 1), chip=('21:00' if k == 'record' else None))
               for i, (k, n, when, on, *_) in enumerate(NOTIFY))
# 세로 예산(본문 약 560px): 전체 스위치는 시트 머리 오른쪽, 항목 6행은 48px, 확인 구역은 한 행에 다음 알림을 부제로.
body = (
    group('조용한 시간', inset(
        f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px; min-height: 55px; padding: 8px 0;">'
        f'<div style="display: flex; flex-direction: column; gap: 2px;"><span style="font-size: 13.5px; font-weight: 600; line-height: 19.6px; color: {C["INK"]};">22:00 ~ 08:00</span>'
        f'<span style="font-size: 11.5px; line-height: 17.25px; color: {C["INK3"]};">이 시간의 알림은 08:00 이후로 미뤄요</span></div>'
        f'<span style="font-size: 12px; font-weight: 600; color: {C["BRAND"]}; white-space: nowrap;">바꾸기 &rsaquo;</span></div>'))
    + group('알림', inset(rows), top=3)
    + group('확인', inset(
        f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px; height: 46px;">'
        f'<div style="display: flex; flex-direction: column; gap: 2px;"><span style="font-size: 13.5px; font-weight: 600; color: {C["INK"]};">테스트 알림 보내기</span>'
        f'<span style="font-size: 11.5px; color: {C["INK3"]};">다음 알림 9월 9일 21:00 무렵 · 오늘 소비 기록 확인</span>'
        f'<span style="font-size: 11.5px; color: {C["INK3"]};">이 기기의 백업 기록이 없어요.</span></div>{icon("right", 16, C["INK4"], 2)}</div>', pad='8px 13px'), top=3)
    + f'<div style="margin-top: 3px; flex-shrink: 0;">{note("절전 상태와 기기 설정에 따라 늦거나 빠질 수 있어요. 앱을 35일 넘게 안 열면 예약이 멈춰요.", "mute", "info")}</div>'
)
MASTER = (f'<span style="display: flex; align-items: center; gap: 8px; flex-shrink: 0; letter-spacing: 0;">'
          f'<span style="font-size: 12px; font-weight: 600; color: {C["INK2"]};">기기 알림</span>{toggle(True)}</span>')
NOTIFY_DESC = '앱 안의 알림 창(종)과는 별개예요. 앱을 안 켜고 있을 때 기기로 알려 드려요.'
NOTIFY_HEAD = (f'<span style="display: flex; align-items: center; justify-content: space-between; gap: 8px; min-height: 27px; width: 354px;">'
               f'<span style="line-height: 24.3px;">알림</span>{MASTER}</span>'
               f'<span style="display: block; margin-top: 8px; font-size: 12.5px; font-weight: 400; line-height: 18.75px; letter-spacing: 0; color: {C["INK3"]};">{NOTIFY_DESC}</span>')
SN_H = 903      # 2026-09-27 fix-up 4 자연 879 + 24(알림 줄 56 · 머리 설명 온 폭) · 예전 자연 871 + 24(테스트 줄 아래 백업 줄)
w('SettingsNotify', sheet(NOTIFY_HEAD, None, body, sheet_footer('닫기', '저장'), body_pb=14, header_right='', h=SN_H, backdrop='light', scrim_h=24))      # 앱: 밝게 흐린 겉 · 닫기 안내 없음(2026-09-27 fix-up)


# ══════════════ 구현 참고 장 — 여섯 알림 카드 ══════════════
def phone_notice(title, body_text, when):
    """안드로이드 알림 카드 모양(앱 아이콘 · 앱 이름 · 시각 · 제목 · 본문). 금액 · 이름은 기본 숨김이라 본문에 숫자가 없다."""
    return (f'<div style="width: 362px; background: {C["SURF"]}; border: 1px solid {C["LINE"]}; border-radius: 16px; padding: 12px 14px; '
            f'box-shadow: 0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24);">'
            f'<div style="display: flex; align-items: center; gap: 7px;">{brand_mark.tile(16, 5)}'
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
    '기기 알림은 <b style="font-weight: 600;">앱을 안 켜고 있을 때 시각으로 오는 것</b>뿐입니다. 한도 넘음 · 목적지 도착 · 다 갚음 · 합계 고치기 · 자동 기록처럼 저장 순간 생기는 일은 사용자가 이미 아는 것이라 앱 안(완료 카드 · 알림 창 · 종 배지)에만 둡니다. 마감한 뒤 기록이 바뀐 달(합계 고치기)도 기기 알림을 보내지 않습니다.',
    '문구에 금액 · 목표 이름을 넣지 않습니다 — 예약 시점 값이라 틀릴 수 있고, 알림 내용은 앱의 암호화 저장 밖에 놓입니다. 상세는 앱에서 봅니다.',
    '같은 종류는 하루 1번. 기록 알림은 이틀째부터 「어제 것도 같이 적을 수 있어요」, 일주일째부터는 주 1회로 줄입니다. 조용한 시간(22:00 ~ 08:00)의 알림은 아침 8시 이후로 미룹니다.',
    '누르면 그 화면 · 그 날짜로 갑니다. 알림으로 들어온 동안은 첫 실행 안내를 띄우지 않되, 본 것으로 저장하지는 않습니다.',
    '권한(안드로이드 13+)은 홈 안내가 끝난 뒤 개인 데이터일 때, 설명 카드에서 「켜기」를 누를 때 묻습니다. 샘플 모드에는 기기 알림이 없습니다. 정확 알람 권한은 쓰지 않습니다(「21시 무렵」).',
    '앱이 열릴 때마다 앞으로 35일치를 다시 예약하고 지난 예약은 지웁니다. 설정 화면의 안내 줄 그대로 — 「절전 상태와 기기 설정에 따라 늦거나 빠질 수 있어요. 앱을 35일 넘게 안 열면 예약이 멈춰요.」',
    '샘플 모드에는 기기 알림이 없어요(「샘플 모드에는 기기 알림이 없어요. 여기서 고른 설정은 내 데이터로 시작할 때 유지돼요.」 · 테스트 알림 꺼짐). 웹에서는 「기기 알림은 안드로이드 앱에서 사용할 수 있어요. 이 화면에서는 알림 취향을 저장할 수 있어요.」 권한이 꺼져 있으면 「기기 알림을 받으려면 권한을 켜 주세요. · 알림 권한 켜기 ›」.',
]
# 기기 알림이 꺼져 있을 때(tasks-12) — 항목 스위치가 모두 꺼진 모양 + 한 줄. 켜면 고른 것이 돌아온다.
off_rows = ''.join(trow(n, when, False, last=(i == len(NOTIFY) - 1), chip=('21:00' if k == 'record' else None)) for i, (k, n, when, on, *_) in enumerate(NOTIFY))
off_panel = (f'<div style="width: 362px; display: flex; flex-direction: column; gap: 8px;">'
             f'<div style="display: flex; align-items: center; gap: 7px;">{mark(7, pos="flex-shrink: 0;")}<span style="font-size: 14px; font-weight: 700; color: {C["INK"]};">기기 알림이 꺼져 있을 때</span></div>'
             f'<div style="font-size: 12px; color: {C["INK3"]}; margin-top: -4px;">설정 › 알림 · 맨 위 스위치 끔</div>'
             f'<div style="background: {C["SURF"]}; border: 1px solid {C["LINE"]}; border-radius: 16px; padding: 12px 14px;">'
             f'<div style="font-size: 12.5px; color: {C["INK2"]}; margin-bottom: 8px;">기기 알림을 켜면 고를 수 있어요</div>{inset(off_rows)}</div>'
             # 패널 밖 설명(앱 화면에 없는 문장 · notify-settings.tsx 의 주석 내용 — 2026-09-27 fix-up)
             f'<div style="font-size: 11.5px; line-height: 1.5; color: {C["INK3"]}; padding: 0 2px;">다시 켜면 전에 고른 항목이 그대로 돌아온다(앱 동작 · 화면 문구는 없음).</div></div>')
optin = (f'<div style="width: 362px; display: flex; flex-direction: column; gap: 8px;">'
         f'<div style="display: flex; align-items: center; gap: 7px;">{mark(8, pos="flex-shrink: 0;")}<span style="font-size: 14px; font-weight: 700; color: {C["INK"]};">처음 묻는 카드</span></div>'
         f'<div style="font-size: 12px; color: {C["INK3"]}; margin-top: -4px;">홈 안내가 끝난 뒤 · 내 데이터일 때 한 번(규칙 5)</div>'
         f'<div style="background: {C["SURF"]}; border: 1px solid {C["LINE"]}; border-radius: 16px; padding: 14px;">'
         f'<div style="display: flex; gap: 10px;"><div style="width: 34px; height: 34px; border-radius: 11px; background: {C["BRAND_SOFT"]}; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">{icon("bell", 18, C["BRAND"], 2)}</div>'
         f'<div><div style="font-size: 14px; font-weight: 700; color: {C["INK"]};">앱을 안 켜고 있을 때 기록 · 마감을 알려 드릴까요?</div>'
         f'<div style="font-size: 12px; line-height: 1.5; color: {C["INK2"]}; margin-top: 4px;">정한 시각 무렵에 이 기기로 알려 드려요. 나중에 설정 › 기기 알림에서 바꿀 수 있어요.</div></div></div>'
         f'<div style="display: flex; gap: 8px; margin-top: 12px;">{btn("나중에", "secondary", h=40).replace("width: 100%;", "flex: 1;")}{btn("켜기", "primary", h=40).replace("width: 100%;", "flex: 1;")}</div></div></div>')
rules = ''.join(f'<li style="margin: 0 0 6px;">{r}</li>' for r in RULES)
body2 = (f'<div style="display: grid; grid-template-columns: repeat(3, 362px); gap: 26px 28px; align-items: start;">{cases}{off_panel}{optin}</div>'
         f'<div style="margin-top: 22px; padding: 16px 18px; background: {C["SURF"]}; border: 1px solid {C["LINE"]}; border-radius: 16px; max-width: 1140px;">'
         f'<div style="font-size: 13px; font-weight: 700; color: {C["INK"]}; margin-bottom: 8px;">규칙</div>'
         f'<ol style="margin: 0; padding-left: 18px; font-size: 12.5px; line-height: 1.55; color: {C["INK2"]};">{rules}</ol></div>')
NOTIFY_CASES_H = 1435      # 2026-09-27 fix-up 4 자연 1411 + 24(알림 줄 56) ·     # 자연 1365 + 24(꺼져 있을 때 · 처음 묻는 카드)
w('NotifyCases', spec_frame(1200, NOTIFY_CASES_H, '기기 알림 — 여섯 가지와 규칙',
                            '앱 안 알림 창과 별개로, 앱을 안 켜고 있을 때 시각으로 오는 안드로이드 로컬 알림입니다. 기본 켬 셋 · 설정에서 켜는 것 셋. 회의 기록은 NAVI-NOTIFY-MEETING-2026-09-23.md.',
                            body2, sub_w=760))
