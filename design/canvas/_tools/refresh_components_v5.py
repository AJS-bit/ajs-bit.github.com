# -*- coding: utf-8 -*-
"""Components.dc.html 의 「08 · v5 달력과 하루 시트」 절을 지금의 v5 시안에서 다시 잘라 와 채운다.

Components 는 손으로 쓴 파일이지만 08절만은 v5 장(HomeCalendarStrip · HomeCalendar · DaySheet · DoneCard ·
ClassifySheet · HeroInsufficient · HeroFootnotes)의 조각을 그대로 옮겨 온 것이다. 그 장들을 고치면 이 절이
옛 모습으로 남으므로(2026-09-21 최신화 점검에서 실제로 걸림) gen_v5.py 뒤에 이 스크립트를 돌린다.
01~07절과 루트 크기는 건드리지 않는다 — 높이가 달라지면 직접 재서 루트 · gen_canvas.py WIDE 를 고친다.
그 뒤 darken.py 로 DarkComponents 를 다시 만든다.
"""
import pathlib, re
from nobreak import nobreak          # 파일을 쓰지 않는 모듈
from gen_calendar import cell as _cal_cell, TODAY as _TODAY      # 오늘 · 기록 0건(+) 칸 견본 — 홈 장에는 없는 상태라 같은 조각에서 만든다(파일을 쓰지 않는 모듈)

CANVAS = pathlib.Path(__file__).resolve().parent.parent


def balanced(s, a):
    """a 에서 시작하는 <div ...> 의 닫는 태그까지."""
    depth = 0
    for m in re.finditer(r'<div\b|</div>', s[a:]):
        if m.group(0) == '</div>':
            depth -= 1
            if depth == 0:
                return s[a:a + m.end()]
        else:
            depth += 1
    raise ValueError


R = lambda n: (CANVAS / (n + '.dc.html')).read_text(encoding='utf-8')
strip_s=R('HomeCalendarStrip'); month_s=R('HomeCalendar'); day_s=R('DaySheet'); done_s=R('DoneCard'); cls_s=R('ClassifySheet'); hi_s=R('HeroInsufficient'); hf_s=R('HeroFootnotes')

# ② 스트립 카드 · 월 달력 카드
i=strip_s.find('펼치기'); strip_card=balanced(strip_s, strip_s.rfind('<div style="background: #FFFFFF',0,i))
i=month_s.find('접기'); month_card=balanced(month_s, month_s.rfind('<div style="background: #FFFFFF',0,i))
# ① 칸 — 스트립 카드의 칸을 그대로
# 2026-09-26(DZ3 호환): 스트립 위 간격 10 → 8 · 칸은 카드 안쪽 7등분(flex · 최대 44 · home-17) — 견본 칸은 44 고정으로 되돌려 쓴다
cells_row=balanced(strip_card, strip_card.index('<div style="display: flex; justify-content: space-between; margin-top: 8px;">'))
CELL_FLEX='<div style="flex: 1 1 0; min-width: 0; max-width: 44px; height: 56px;'
cells=[]; pos=cells_row.index('>')+1
while True:
    k=cells_row.find(CELL_FLEX,pos)
    if k<0: break
    c=balanced(cells_row,k); pos=k+len(c); cells.append(c.replace(CELL_FLEX,'<div style="width: 44px; flex-shrink: 0; height: 56px;',1))
assert len(cells)==7
def find(txt): 
    r=[c for c in cells if txt in c]; assert r, txt; return r[0]
c_sum=find('>5.9만<'); c_none=find('>2</span>'); c_zero=find('>0</span>'); c_check=find('>4,500<'); c_today=find('#E9EDFD')
assert '이체' in c_zero and '—' in c_none and 'inset 0 0 0 1.5px #3556E6' in c_today
c_add=_cal_cell(_TODAY, '화', state=('—', False, False, False))      # 오늘 · 아직 안 적음 — 파란 원 +
assert 'inset 0 0 0 1.5px #3556E6' in c_add and c_add.count('border-radius: 99px; background: #3556E6') == 1
c_focus=c_sum.replace('background: transparent; ','background: transparent; box-shadow: inset 0 0 0 1.5px #3556E6, 0 0 0 3px rgba(53,86,230,.16);',1)
assert c_focus!=c_sum
CAP='<span style="font-size: 10.5px; line-height: 1.3; color: #626D88; text-align: center; white-space: nowrap;">%s</span>'
# 칸 일곱 개를 4 + 3 격자로(2026-09-24 최종 점검 후속 — 50px 열에 `오늘 · 안 적음`이 넘치고 `포커스`만 둘째 줄에 떨어지던 것). 열 77.5 · 카드 높이 그대로
def cellcol(c,cap): return '<div style="display: flex; flex-direction: column; align-items: center; gap: 5px; min-width: 0;">'+c+CAP%cap+'</div>'
cell_states=('<div style="background: #FFFFFF; border: 1px solid #E3E8F1; border-radius: 18px; padding: 12px 6px 10px; display: grid; grid-template-columns: repeat(4, 1fr); row-gap: 10px;">'
  + cellcol(c_sum,'합계') + cellcol(c_none,'기록 없음') + cellcol(c_zero,'안 씀 · 이체') + cellcol(c_check,'다 적음')
  + cellcol(c_today,'오늘') + cellcol(c_add,'오늘 · 안 적음') + cellcol(c_focus,'포커스') + '</div>')

# ⑤ 하루 시트 — 흰 시트 부분만(키보드 · 배경 제외). 2026-09-27 fix-up 4: 키보드가 열린 장은 시트가 30 ~ 564 고정 높이 + 저장 바닥 띠(앱) —
#    견본은 높이를 풀고, 본문의 「오늘 기록」 목록(키보드 위에서는 바닥 띠에 가려 안 보이는 부분)을 빼 머리 · 칸 · 최근 기록 · 링크 · 바닥 띠만 남긴다.
SHEET_OPEN = '<div style="height: 534px; flex-shrink: 0; background: #FFFFFF; border: 1px solid #E3E8F1; border-bottom: 0; border-radius: 26px 26px 0 0; display: flex; flex-direction: column; overflow: hidden;">'
a=day_s.index(SHEET_OPEN)
sheet=balanced(day_s,a)
sheet=sheet.replace(SHEET_OPEN, '<div style="background: #FFFFFF; border: 1px solid #E3E8F1; border-radius: 26px; display: flex; flex-direction: column; overflow: hidden;">',1)
sheet=sheet.replace('<div style="flex: 1; min-height: 0; overflow: hidden; padding: 12px 18px 21px; display: flex; flex-direction: column; gap: 10px;">',
                    '<div style="padding: 12px 18px 16px; display: flex; flex-direction: column; gap: 10px;">',1)
_tl = sheet.index('<div style="display: flex; flex-direction: column; gap: 8px; flex-shrink: 0;"><span style="font-size: 12px; font-weight: 600; line-height: 17px; color: #475467;">오늘 기록</span>')
sheet = sheet[:_tl] + sheet[_tl + len(balanced(sheet, _tl)):]
assert 'min-height: 0' not in sheet and '오늘 기록' not in sheet and sheet.count('>저장<') == 1
# ⑧ 완료 카드
a=done_s.index('<!--dc-keep-->'); b=done_s.index('<!--/dc-keep-->')+len('<!--/dc-keep-->')
done=done_s[a:b].replace('position: absolute; left: 14px; right: 14px; bottom: 78px; ','',1)
assert 'position: absolute' not in done
# ⑨ 카테고리 고르기 줄 — 커피 묶음(펼침 · 건별 행) + 간식 줄(추천 칩 · 카테고리 고르기 ›). 2026-09-27 fix-up 4: 묶음 = 앱 .classify-group(줄 최소 52 + 아래 선 · 펼친 건별 행 포함)
GROUP = '<div style="flex-shrink: 0; '
k = cls_s.index('커피'); a = cls_s.rfind(GROUP, 0, k); g1 = balanced(cls_s, a)
k2 = cls_s.index('간식', a + len(g1)); g2 = balanced(cls_s, cls_s.rfind(GROUP, 0, k2))
assert '13,500원' in g1 and '카테고리 고르기' in g1 and '9월 4일' in g1 and '추천' in g2
classify = '<div style="background: #FFFFFF; border: 1px solid #E3E8F1; border-radius: 18px; padding: 2px 16px 4px;">' + g1 + g2 + '</div>'
# ⑩ 이력 부족 히어로 — 카드 전체(아래 칸 「월급 360만원 · 월말 예상 — · 월말 예상 여유 —」와 기준 줄까지 · 2026-09-27 fix-up — 예전엔 항로 바에서 잘라 열린 모서리로 보였다)
a=hi_s.index('<div style="background: #FFFFFF; border: 1px solid #E3E8F1; border-radius: 20px; padding: 16px; box-shadow')
hero=balanced(hi_s,a)
assert '월급 · 부수입 고치기' in hero and '월말 예상 여유' in hero
hero_top=hero.replace(' flex-shrink: 0;','',1)
# ⑪ 조건부 각주 — 캐논 홈(HomeCalendarStrip) 히어로의 아랫부분: 기준 줄 + 「월급 · 부수입 고치기 ›」 + 캐논 각주 두 줄(2026-09-27 fix-up · 앱 Components--hero 와 같은 날)
k=strip_s.index('이번 달 소비'); _h=balanced(strip_s, strip_s.rfind('<div style="background: #FFFFFF; border: 1px solid #E3E8F1; border-radius: 20px; padding: 16px;', 0, k))
_B='<div style="display: flex; align-items: center; justify-content: space-between; gap: 10px; margin-top: 12px;">'
assert _h.count(_B)==1 and '카테고리 없는 32,000원은 적은 금액 그대로 예상에 더했어요' in _h and '지난 고정비 기록을 보고' in _h
_t=_h[_h.index(_B):_h.rstrip().rindex('</div>')]
tail=('<div style="background: #FFFFFF; border: 1px solid #E3E8F1; border-top: none; border-radius: 0 0 20px 20px; padding: 4px 16px 16px; '
      'box-shadow: 0 1px 2px rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24);">'+_t.replace(_B,_B.replace('margin-top: 12px;','margin-top: 0;'),1)+'</div>')
assert '월급 · 부수입 고치기' in tail and tail.count('<div')==tail.count('</div>')

NUM='<span style="flex-shrink: 0; width: 17px; height: 17px; border-radius: 99px; background: #101828; color: #FFFFFF; font-size: 10.5px; font-weight: 700; display: inline-flex; align-items: center; justify-content: center;">%s</span>'
D={
 1:('CalendarCell','스트립은 카드 안쪽 7등분(최대 44 · 320에서 약 39) × 56 · 월 달력은 카드 안쪽 ÷ 7 × 56, 큰 글자 × 72. 요일 10/500 · 날짜 11/500(월 달력 12, 오늘 굵게) · 합계 11/600 줄 높이 13. 수식어 줄(스트립 9 · 월 달력 12)은 비어도 자리를 둡니다. 기록 없음 —(ink-3 · 시작일 전 날도 같음) · 안 씀 0(ink-2) · ✓ · 이체(ink-2) · 오늘 brand-soft + 안쪽 테두리 1.5px brand(늘) · 오늘 기록 0건(안 썼어요 아님)이면 — 대신 파란 원 +(지름 20 · 큰 글자 24, 이체나 ✓ 와 함께면 16 · 칸 크기 불변) · aria 「오늘 · 눌러서 적기」 · 누르는 순간 테두리 2px&nbsp;· 포커스 링 3px.'),
 2:('RecentStrip · MonthCalendar · DayList','접힘은 제목 「이번 달 소비 기록」(1 ~ 6일에 지난달 날이 들어가면 「최근 7일 소비 기록」) + 「펼치기 ▾」 + 안내 한 줄 「날짜를 누르면 그날 쓴 돈을 적어요」(12 · ink-3) + 7칸(오늘이 오른쪽 끝 · 옆으로 밀지 않음 · 위 간격 8). 칸 바로 아래 범례 줄 「— 기록 없음 · 0 안 썼어요 · ✓ 다 적었어요」(11.5 · ink-3 · 항목마다 줄바꿈 없음)는 접힘 · 펼침 · 목록 어디서나 늘 있습니다. 펼침은 머리줄(‹ 월 › 32 × 32 · 「접기 ▴」) + 안내 + 요일 줄 + 7열 grid(주마다 line-soft 1px). 날짜 목록은 큰 글자에서 「목록으로 보기」를 고른 때만.'),
 3:('StatusLine · 적기 버튼','상태 문장 12.5 / 400 · ink-2 · 한 문장. 오늘 기록 0건(안 썼어요 <span style="white-space: nowrap;">아님)이면</span> 문장 대신 가득 찬 폭 버튼 「+ 오늘 쓴 돈 적기」(40 · 반경 12&nbsp;· brand-soft · brand 14 / 700 · 누르면 오늘 하루 시트). 기록이 있으면 문장 오른쪽에 알약 「+ 더 적기」(안 썼어요 표시면 「+ 적기」 · 32 · 13 / 700) — 그 줄도 높이 40이라 저장 전후 카드 높이가 같습니다. 저녁 6시 뒤 · 오늘 기록 있음 · 표시 안 함이면 「오늘 4건 37,000원 · 오늘 다 적었어요 ›」 → 누르면 「… · 다 적었어요 ✓」. 샘플은 위 줄 「샘플에서는 「다 적었어요」 표시를 쓰지 않아요 · 카테고리는 저장할 때 골라요」. 펼친 달력은 그 위에 그 달 합계 한 줄.'),
 4:('ReviewRow','높이 32 · 위 간격 6 · 위 선 line-soft · 12.5 / 600 · ink · 주황 없음. 항목이 하나면 그 항목 이름(「카테고리 없는 기록 7건 · 카테고리 고르기 ›」 · 「8월에 새 기록이 있어요 · 8월 합계 고치기 ›」)이 되고 바로 그 항목을 엽니다. 둘 이상이면 「확인할 내용 N개 ›」. 누르는 영역은 44.'),
 5:('DaySheet','위 모서리 26 · 손잡이 38 × 4 · 제목 18 / 700. 칸 이름은 칸 위(12 / 600 · ink-2) — 금액 칸 48(값 오른쪽 20 / 600 + 원 · 비면 원만) · 메모 칸 44(자리 글자 「예: 팀 점심」). 카테고리 줄 오른쪽 「나중에 고르기」 — 고르지 않은 초안이면 눌린 알약(brand-soft · brand 600 · 1px brand), 골랐으면 외곽선. 저장 52(radius 14 · 16 / 600) — 금액이 비면 회색 + 까닭 한 줄. 링크 아래 「저축·투자와 대출상환은 계좌까지 고르는 기록 창에서 남겨요 · 소비율에는 안 들어가요」. 「9월 8일 다 적었어요」 아래 효과 줄 「누르면 달력에 ✓가 남고 오늘 저녁엔 더 묻지 않아요」. 키보드가 열린 상태가 기본 — 앱 창이 키보드 위로 줄어 「저장」은 본문 밖 바닥 띠(위 선 · 12 18 12)에 붙습니다. 머리 위 20 · 본문 12 18 20 · 칸 사이 10 · 링크 줄 28.'),
 6:('ColorChipRow','칩 높이 32 · radius 8 · 색 점 8px + 이름 12.5 / 500 · 자주 쓴 3개(앱 categorySlots) + 「전체 ›」 — 펼치면 위 세 칸을 뺀 나머지가 늘 같은 순서, 고정비 넷은 선 아래. 색만으로 뜻을 전하지 않습니다.'),
 7:('RecentEntryChip','높이 32 · radius 8 · inset 배경 · 메모 + 금액(600) + 색 점 7px + 카테고리 이름 11 / 500. 카테고리가 없으면 점 없이 회색 「카테고리 없음」, 메모가 없으면 「● 식비 4,500」 · 「카테고리 없음 3,000」. 어떤 칩이 어떤 순서로 오는지는 앱 recentEntries(30일 · 메모 + 금액 + 카테고리로 묶어 잦은 순 · 최대 5).'),
 8:('DoneCard','ink 배경 · radius 16 · 제목 14 / 700 + 닫기 · 둘째 줄 13.5 — 무엇을 저장했는지(「9월 8일 · 편의점 · 카테고리 없음 12,000원 저장 · 오늘 5건 49,000원」) · 카테고리 없이 저장했으면 셋째 줄 「소비에는 이미 포함됐어요 · 지금 카테고리를 고를까요?」 + 칩 줄(32 · 13 / 600 · 색 점 · 「전체 ›」) · 버튼 36 「한 건 더」 · 「되돌리기」(aria 「방금 기록한 12,000원 되돌리기」). 6초 뒤 40px 띠 「✓ 12,000원 저장 · 되돌리기 · 닫기」, 저장 60초 뒤 사라짐 · 탭을 옮겨도 남음. 라이트 · 다크에서 같은 모양.'),
 9:('ClassifyGroupRow','줄 최소 52(위아래 6) + 아래 선 · 제목 14 / 600 + 금액 12. 모든 줄에 파란 글자 버튼 「카테고리 고르기 ›」(칩이 있어도). 묶음 금액은 묶음 전체(13,500원 — 빼도 바닥의 건수만 바뀜). 추천 = 최근 30일 같은 메모의 확정 카테고리 중 최신 — 누르기 전 「● 기타 추천」(9월 8일 샘플 · 8월 간식을 마감 뒤 기타로 고름), 누른 뒤 「● 카페/간식」 눌림. 메모 없는 기록은 묶지 않고 「9월 5일 토 메모 없음 · 3,000원」. 펼치면 건별 행 40(체크 22 · 뺀 행은 회색) · 최근 기록부터.'),
 10:('HeroInsufficient','평소 히어로와 같은 틀. 머리말 「이번 달 소비」 + 알약 「소비 목표 조정」(배지 없음) · 큰 숫자 = 지금까지 쓴 돈 ÷ 월급(0 < x < 0.05 면 0.1 + 「% 미만」 · 0건이면 「아직 기록이 없어요」) · 설명 줄 「월급 360만원 중 5,000원 썼어요」 · 오른쪽 「소비 목표까지 / 216만원 남음」(돈) · 「순자산의 0.1% 미만 ⓘ」 · 게이지 「소비 목표 60%」. 다른 점은 월말 예상과 월말 예상 여유 — · 설명 줄 아래 각주 두 줄(12 · ink-3) 「아직 기록하지 않은 소비는 포함되지 않았어요」 · 「9월을 마감하면 10월부터 월말 예상을 보여 드려요」.'),
 11:('HomeHero 조건부 각주','「월급(실수령) 기준 · 저축 이체와 대출 갚은 돈은 쓴 돈에 넣지 않아요」 + 「월급 · 부수입 고치기 ›」 줄 아래에 11 / 1.4 · ink-3 · 위 간격 10 으로 한 줄씩. 그림은 9월 8일 샘플(카테고리 없는 32,000원 · 고정비 이력 두 줄). 순서: 「8월에 새 기록이 있어요 · 8월 합계 고치기 ›」(링크 줄 · 마감한 달에 기록을 더했을 때만) → 카테고리 없는 이번 달 금액 → 카테고리 없는 지난 기록 → 고정비 이력 → 한 달치뿐. 카드 높이만 줄 수만큼 늡니다.'),
}
def note(n):
    name,desc=D[n]
    return ('<div style="display: flex; gap: 8px; padding: 0 2px;"><div style="padding-top: 1px;">'+NUM%n+'</div>'
            '<div style="min-width: 0;"><div style="font-size: 12.5px; font-weight: 600; color: #101828;">'+name+'</div>'
            '<div style="font-size: 11.5px; line-height: 1.55; color: #475467; margin-top: 2px;">'+desc+'</div></div></div>')
def col(w,*parts):
    return '<div style="width: %dpx; flex-shrink: 0; display: flex; flex-direction: column; gap: 9px;">'%w+''.join(parts)+'</div>'
GAP='<div style="height: 8px;"></div>'
col1=col(362,note(2),note(3),note(4),strip_card,month_card,GAP,note(11),tail)
col2=col(362,note(5),note(6),note(7),sheet,GAP,note(10),hero_top)
col3=col(324,note(1),cell_states,GAP,note(8),done,GAP,note(9),classify)

SECTION=('  <div>\n    <div style="font-size: 12px; font-weight: 600; letter-spacing: 0.1em; color: #626D88;">08 · v5 달력과 하루 시트 — 새 컴포넌트 11종</div>\n'
  '    <p style="margin: 6px 0 0; font-size: 12.5px; line-height: 1.55; color: #475467;">조각은 v5 시안(홈 달력 · 하루 시트 · 완료 카드 · 카테고리 고르기)에서 그대로 가져왔습니다. 새 색은 없습니다 — 달력 칸은 brand-soft · brand · ink · ink-2 · ink-3 · ink-4 만 씁니다(그날 합계 · 오늘 날짜는 ink · 날짜 · 0 · ✓ · 이체는 ink-2 · 기록 없음 —은 ink-3 · 미래 · 이웃 달 날짜는 ink-4 · 이웃 달은 70% · 오늘 테두리와 + 원만 brand · 앱 v5-calendar.css).</p>\n'
  '    <div style="display: flex; align-items: flex-start; justify-content: space-between; gap: 18px; margin-top: 14px; background: #EDF0F7; border-radius: 18px; padding: 16px 14px 18px;">\n'+col1+'\n'+col2+'\n'+col3+'\n    </div>\n  </div>\n\n')

# ══════════════ 09 · 탭 머리줄 · 10 · 판정 줄과 참고 줄 (2026-09-26 DZ4 · D14 · D1 · D3 · D7 · D15) ══════════════
from gen_common import screen_header as _screen_header, C as _C      # gen_common 은 파일을 쓰지 않는다
hs_s = R('HomeCalendarStrip'); sp_s = R('Spending'); lm_s = R('Limits'); hi2 = hi_s
home_head = balanced(hs_s, hs_s.index('<div style="display: flex; flex-direction: column; gap: 6px; padding: 12px 16px 10px; flex-shrink: 0;">'))
spend_head = balanced(sp_s, sp_s.index('<div style="display: flex; flex-direction: column; gap: 10px; padding: 14px 16px 12px; flex-shrink: 0;">'))
asset_head = _screen_header('자산', tabs=['자산 구성', '부채', '상환 계획'], active=0)
STRIP = ('<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px; height: 32px; padding: 0 14px; background: #E9EDFD;">'      # 앱 샘플 띠 32 · #3B4E8F(fix-up 3)
         '<span style="font-size: 12px; font-weight: 500; color: #3B4E8F; white-space: nowrap;">샘플 데이터로 둘러보는 중</span>'
         '<span style="font-size: 12px; font-weight: 600; color: #3556E6; white-space: nowrap;">내 데이터로 시작 &rsaquo;</span></div>')
PHONE = lambda inner: f'<div style="width: 356px; background: #EDF0F7; border: 1px solid #E3E8F1; border-radius: 18px; overflow: hidden;"><div style="width: 390px; transform: scale(0.91); transform-origin: top left;">{inner}</div></div>'
CAPN = lambda t, d: f'<div><div style="font-size: 12.5px; font-weight: 600; color: #101828;">{t}</div><div style="font-size: 11.5px; line-height: 1.55; color: #475467; margin-top: 2px;">{d}</div></div>'
sec09 = ('  <div>\n    <div style="font-size: 12px; font-weight: 600; letter-spacing: 0.1em; color: #626D88;">09 · 탭 머리줄 — 모든 탭이 같은 틀(AppTopbar)</div>\n'
         '    <div style="display: grid; grid-template-columns: repeat(3, 356px); justify-content: space-between; gap: 18px 8px; margin-top: 14px; background: #EDF0F7; border-radius: 18px; padding: 16px 14px 18px;">'
         + '<div style="display: flex; flex-direction: column; gap: 9px;">' + CAPN('홈', '앱마크 + NAVI · 「오늘의 내비게이션」 + 날짜 줄 「9월 8일 · 오늘 포함 23일 남음」(마지막 날 「이번 달 마지막 날」). 홈에는 「?」 없음.') + PHONE(home_head)
         + CAPN('샘플 모드', '머리줄 위에 띠 하나 「샘플 데이터로 둘러보는 중 · 내 데이터로 시작 ›」 — 모든 탭.') + PHONE(STRIP + home_head) + '</div>'
         + '<div style="display: flex; flex-direction: column; gap: 9px;">' + CAPN('자산 · 목적지 · 미래', '제목 h1 바로 뒤 「?」(보이는 28 · 누르는 영역 44 · aria 「{화면} 안내 보기」 · 빈 화면에서는 숨김) + 세그먼트.') + PHONE(asset_head) + '</div>'
         + '<div style="display: flex; flex-direction: column; gap: 9px;">' + CAPN('소비', '둘째 줄 왼쪽 「‹ 2026년 9월 ›」 · 오른쪽 채운 「+ 기록」 + 세그먼트.') + PHONE(spend_head)
         + CAPN('오른쪽 묶음', '설정 · 코칭 · 알림 — 아이콘 36 + 글자 10.5px · 칸마다 44. 종 배지 = 중요 알림 수(시안 사용자 1). 알림이 없으면 배지 없음. 누를 수 있는 것은 모두 44 × 44.') + '</div>'
         + '</div>\n  </div>\n\n')

LM_TOP_ = '<div style="background: #FFFFFF; border: 1px solid #E3E8F1; border-radius: 20px; padding: 16px; box-shadow'
limit_top = balanced(lm_s, lm_s.index(LM_TOP_))
k = hi2.index('9월 5일부터 기록'); limit_mid = balanced(hi2, hi2.rfind('<div style="background: #FFFFFF; border: 1px solid #E3E8F1; border-radius: 18px; padding: 12px 14px;', 0, k))
over_card = ('<div style="background: #FFFFFF; border: 1px solid #E3E8F1; border-radius: 18px; padding: 12px 14px;">'
             '<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px;"><span style="font-size: 13.5px; font-weight: 600; color: #101828;">이번 달 한도</span>'
             '<span style="font-size: 13.5px; font-weight: 600; color: #C0342F; white-space: nowrap;">3만원 넘음 &rsaquo;</span></div>'
             '<div style="font-size: 13px; line-height: 1.45; color: #475467; margin-top: 4px;">이번 달 한도는 이미 넘었어요 · 216만원 중 219만원 썼어요</div>'
             '<div style="position: relative; height: 8px; border-radius: 99px; background: #E8ECF5; margin-top: 9px; overflow: hidden;"><div style="position: absolute; inset: 0; border-radius: 99px; background: #C0342F;"></div></div></div>')
CMP = lambda col, t, w=600: f'<div style="font-size: 12.5px; font-weight: {w}; color: {col}; padding: 7px 0; border-top: 1px solid #F3F5FA;">{t}</div>'
compare_card = ('<div style="background: #FFFFFF; border: 1px solid #E3E8F1; border-radius: 18px; padding: 8px 14px 6px;">'
                '<div style="font-size: 12px; font-weight: 600; color: #475467; padding: 2px 0 6px;">상환 방식 비교 한 줄</div>'
                + CMP('#626D88', '어느 방식이든 결과가 같아요', 500) + CMP('#0F7B47', '소액 우선보다 이자 30만원 덜 내요 · 1개월 먼저 끝나요')
                + CMP('#B45309', '고금리 우선보다 이자 30만원 더 내요 · 1개월 늦게 끝나요') + CMP('#98A2B3', '— · 매달 이자가 약 300,000원이에요. 이보다 많이 갚아야 잔액이 줄어요.', 500) + '</div>')
# 앱 부채 줄 모양(debt-fidelity): 「카드/리볼빙 · 월 최소 —」 + 「입력 필요」(2026-09-27 fix-up — 예전 「월 최소 상환 — 입력 필요」는 앱에 없는 상태)
# 2026-09-27 fix-up 2: 캐논 카드 할부는 가장 높은 금리(14.5%)라 앱처럼 이름 옆 빨간 「최고 금리」 칩 · 금액 아래 빨간 「연 14.5%」 · 줄 끝 ⋯(Debts 장과 같은 줄)
missing_card = ('<div style="background: #FFFFFF; border: 1px solid #E3E8F1; border-radius: 18px; padding: 12px 14px; display: flex; align-items: center; gap: 10px;">'
                '<div style="flex: 1; display: flex; flex-direction: column; gap: 3px; min-width: 0;"><div style="display: flex; align-items: center; gap: 6px;"><span style="font-size: 14px; font-weight: 600; color: #101828;">카드 할부</span>'
                '<span style="display: inline-flex; align-items: center; background: #FCEBEA; color: #C0342F; font-size: 11.5px; font-weight: 600; border-radius: 99px; padding: 4px 9px; white-space: nowrap;">최고 금리</span></div>'
                '<span style="display: inline-flex; align-items: center; gap: 6px; font-size: 12px; color: #626D88;"><span>카드/리볼빙 · 월 최소 <span style="color: #98A2B3; font-weight: 600;">—</span></span>'
                '<span style="font-size: 10.5px; font-weight: 600; color: #475467; background: #F4F6FB; border-radius: 99px; padding: 2px 7px; white-space: nowrap;">입력 필요</span></span></div>'
                '<div style="text-align: right; flex-shrink: 0;"><span style="font-size: 15px; font-weight: 600; letter-spacing: -0.02em; color: #101828; white-space: nowrap;">180<span style="font-size: 11.5px; font-weight: 500; color: #626D88;">만원</span></span>'
                '<div style="font-size: 11.5px; font-weight: 600; color: #C0342F; white-space: nowrap;">연 14.5%</div></div>'
                '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#697182" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink: 0;"><circle cx="5" cy="12" r="1"/><circle cx="12" cy="12" r="1"/><circle cx="19" cy="12" r="1"/></svg></div>')
COL = lambda *parts: '<div style="display: flex; flex-direction: column; gap: 9px;">' + ''.join(parts) + '</div>'
sec10 = ('  <div>\n    <div style="font-size: 12px; font-weight: 600; letter-spacing: 0.1em; color: #626D88;">10 · 판정 줄 · 참고 줄 · 비어 있는 값</div>\n'
         '    <div style="display: grid; grid-template-columns: repeat(3, 356px); justify-content: space-between; gap: 18px 8px; margin-top: 14px; background: #EDF0F7; border-radius: 18px; padding: 16px 14px 18px;">'
         + COL(CAPN('참고 줄', '「저축 · 상환 계획까지 지키려면 152만원 안에서 쓰면 돼요」 — ink-3 12px · 빨강 없음 · planCapInfo 가 있을 때만. 풀이에는 「이 금액은 참고예요. 한도를 넘었는지는 소비 목표로만 판단해요.」'), limit_top)
         + COL(CAPN('달 중간에 시작한 달', '남은 한도는 초록 대신 기본 글자색 + 「9월 5일부터 기록 · 그 전 소비는 빠져 있어요」.'), limit_mid,
               CAPN('넘었을 때', '카드 · 줄은 「{n} 넘음」(빨강), 한도 탭은 「한도를 {n} 넘었어요」 + 「남은 한도 없음」 · 빨간 막대. 「하루 0원」이라고 쓰지 않습니다.'), over_card)
         + COL(CAPN('상환 방식 비교', '같으면 회색, 나으면 초록, 못하면 주황(--warning), 계산할 수 없으면 「—」 + 까닭. 「추천」은 고금리 우선이 확실히 나을 때만.'), compare_card,
               CAPN('비어 있는 값', '한 번도 넣지 않은 값은 0원 · 0% · 좋은 결과가 아니라 회색 「—」 + 「입력 필요」.'), missing_card)
         + '</div>\n  </div>\n\n')
SECTION = SECTION + sec09 + sec10

p = CANVAS / 'Components.dc.html'; s = p.read_text(encoding='utf-8')
START = '  <div>\n    <div style="font-size: 12px; font-weight: 600; letter-spacing: 0.1em; color: #626D88;">08 · v5'
end = s.rindex('</div>\n</x-dc>')
if START in s:                      # 있던 08절을 걷어 내고 다시 채운다
    s = s[:s.index(START)] + s[end:]
    end = s.rindex('</div>\n</x-dc>')
s = s[:end] + SECTION + s[end:]
assert s.count('08 · v5') == 1 and s.count('09 · 탭 머리줄') == 1 and s.count('10 · 판정 줄') == 1
# 루트 높이 — 01~07(손편집 · DZ4 make_components.py) + 08 ~ 10 의 자연 높이 + 24. gen_canvas.py WIDE · screens.json 과 같아야 한다.
COMP_H = 4773      # 2026-09-27 fix-up 5 자연 4749 + 24(04 잠긴 칸 안내 상자 · 확인 창 앱 AlertDialog 치수) · fix-up 3 자연 4732 + 24(04 원 단위 확인 창 띠) · 2026-09-27 fix-up 2 자연 4729 + 24(01 저장 중 두 가지 · 10 부채 줄 최고 금리) · fix-up 1(⑩ 히어로 카드 전체 · ⑪ 캐논 각주 · 04 확인 창 세로 버튼 · 10 부채 줄) — 자연 4725 + 24 · 2026-09-26 DZ4 4598
s, n_ = re.subn(r'(<div style="width: 1200px; height: )\d+(px; background: #FFFFFF;)', lambda m_: f'{m_.group(1)}{COMP_H}{m_.group(2)}', s, count=1)
assert n_ == 1
s = nobreak(s)       # 낱말 중간 꺾임 묶음(D14) — 01~10 모든 절의 글자(flex 상자 바로 안 · svg 는 그대로 · 멱등)
p.write_text(s, encoding='utf-8')
print('Components 08절 다시 채움 · div', s.count('<div'), '/', s.count('</div>'))
