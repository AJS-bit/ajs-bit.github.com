# -*- coding: utf-8 -*-
"""Components.dc.html 의 「08 · v5 달력과 하루 시트」 절을 지금의 v5 시안에서 다시 잘라 와 채운다.

Components 는 손으로 쓴 파일이지만 08절만은 v5 장(HomeCalendarStrip · HomeCalendar · DaySheet · DoneCard ·
ClassifySheet · HeroInsufficient · HeroFootnotes)의 조각을 그대로 옮겨 온 것이다. 그 장들을 고치면 이 절이
옛 모습으로 남으므로(2026-09-21 최신화 점검에서 실제로 걸림) gen_v5.py 뒤에 이 스크립트를 돌린다.
01~07절과 루트 크기는 건드리지 않는다 — 높이가 달라지면 직접 재서 루트 · gen_canvas.py WIDE 를 고친다.
그 뒤 darken.py 로 DarkComponents 를 다시 만든다.
"""
import pathlib, re

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
cells_row=balanced(strip_card, strip_card.index('<div style="display: flex; justify-content: space-between; margin-top: 8px;">'))
cells=[]; pos=cells_row.index('>')+1
while True:
    k=cells_row.find('<div style="width: 44px; height: 56px;',pos)
    if k<0: break
    c=balanced(cells_row,k); cells.append(c); pos=k+len(c)
assert len(cells)==7
def find(txt): 
    r=[c for c in cells if txt in c]; assert r, txt; return r[0]
c_sum=find('>5.9만<'); c_none=find('>2</span>'); c_zero=find('>0</span>'); c_check=find('>4,500<'); c_today=find('#E9EDFD')
assert '이체' in c_zero and '—' in c_none
c_focus=c_sum.replace('background: transparent; ','background: transparent; box-shadow: inset 0 0 0 1.5px #3556E6, 0 0 0 3px rgba(53,86,230,.16);',1)
assert c_focus!=c_sum
CAP='<span style="font-size: 10.5px; line-height: 1.3; color: #626D88; text-align: center; white-space: nowrap;">%s</span>'
def cellcol(c,cap): return '<div style="display: flex; flex-direction: column; align-items: center; gap: 5px; width: 50px;">'+c+CAP%cap+'</div>'
cell_states=('<div style="background: #FFFFFF; border: 1px solid #E3E8F1; border-radius: 18px; padding: 12px 6px 10px; display: flex; justify-content: space-between;">'
  + cellcol(c_sum,'합계') + cellcol(c_none,'미입력') + cellcol(c_zero,'안 씀 · 이체') + cellcol(c_check,'다 적음') + cellcol(c_today,'오늘') + cellcol(c_focus,'포커스') + '</div>')

# ⑤ 하루 시트 — 흰 시트 부분만(키보드 · 배경 제외)
a=day_s.index('<div style="flex: 1; min-height: 0; background: #FFFFFF; border-radius: 26px 26px 0 0;')
sheet=balanced(day_s,a)
sheet=sheet.replace('<div style="flex: 1; min-height: 0; background: #FFFFFF; border-radius: 26px 26px 0 0; display: flex; flex-direction: column; overflow: hidden;">',
                    '<div style="background: #FFFFFF; border-radius: 26px 26px 0 0; display: flex; flex-direction: column; overflow: hidden; padding-bottom: 16px;">',1)
sheet=sheet.replace('<div style="flex: 1; min-height: 0; overflow: hidden; padding: 12px 18px 0; display: flex; flex-direction: column; gap: 10px;">',
                    '<div style="padding: 12px 18px 0; display: flex; flex-direction: column; gap: 10px;">',1)
assert 'min-height: 0' not in sheet
# ⑧ 완료 카드
a=done_s.index('<!--dc-keep-->'); b=done_s.index('<!--/dc-keep-->')+len('<!--/dc-keep-->')
done=done_s[a:b].replace('position: absolute; left: 14px; right: 14px; bottom: 78px; ','',1)
assert 'position: absolute' not in done
# ⑨ 분류 묶음 행 — 첫 묶음(펼침) + 둘째 묶음
a=cls_s.index('<div style="display: flex; align-items: center; gap: 10px; height: 52px; border-bottom: 1px solid #F3F5FA;">')
g1=balanced(cls_s,a); rest=cls_s[a+len(g1):]
sub=balanced(rest,rest.index('<div style="background: #F4F6FB; border-radius: 0 0 12px 12px;')); rest2=rest[rest.index(sub)+len(sub):]
g2=balanced(rest2,rest2.index('<div style="display: flex; align-items: center; gap: 10px; height: 52px;'))
classify='<div style="background: #FFFFFF; border: 1px solid #E3E8F1; border-radius: 18px; padding: 2px 16px 4px;">'+g1+sub+g2+'</div>'
# ⑩ 이력 부족 히어로 — 위쪽(큰 숫자 ~ 항로 바)만
a=hi_s.index('<div style="background: #FFFFFF; border: 1px solid #E3E8F1; border-radius: 20px; padding: 16px; box-shadow')
hero=balanced(hi_s,a)
cut=hero.index('<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 0; margin-top: 14px;')
hero_top=hero[:cut]+'</div>'
hero_top=hero_top.replace('border-radius: 20px; padding: 16px;','border-radius: 20px 20px 0 0; border-bottom: none; padding: 16px 16px 14px;',1).replace(' flex-shrink: 0;','',1)
# ⑪ 조건부 각주 — HeroFootnotes 2번 견본의 카드 아랫부분
k=hf_s.index('분류 안 한 32,000원은 적은 금액 그대로 예상에 더했어요</div><div style="display: flex; align-items: center; justify-content: center; gap: 6px; height: 46px;')
a=hf_s.rfind('<div style="background: #FFFFFF; border: 1px solid #E3E8F1; border-top: none; border-radius: 0 0 20px 20px;',0,k)
tail=balanced(hf_s,a)
assert '안내 줄</span>' not in tail

NUM='<span style="flex-shrink: 0; width: 17px; height: 17px; border-radius: 99px; background: #101828; color: #FFFFFF; font-size: 10.5px; font-weight: 700; display: inline-flex; align-items: center; justify-content: center;">%s</span>'
D={
 1:('CalendarCell','스트립 44 × 56 · 월 달력은 카드 안쪽 ÷ 7(390 = 47.7 · 360 = 44.6 · 320 = 39.4) × 56, 큰 글자 × 72. 요일 10/500 · 날짜 11/500(월 달력 12, 오늘 굵게) · 합계 11/600 줄 높이 13. 수식어 줄 12px 은 비어도 자리를 둡니다. 미입력 —(ink-3) · 안 씀 0(ink-2) · ✓ · 이체(ink-2) · 오늘 brand-soft · 포커스 링 3px.'),
 2:('RecentStrip · MonthCalendar · DayList','접힘은 7칸(간격 0 · 오늘이 오른쪽 끝) + 제목 오른쪽 「펼치기 ▾」. 펼침은 머리줄(‹ 월 › 32 × 32 · 「접기 ▴」) + 요일 줄 약 21 + 7열 grid, 주마다 line-soft 1px. 날짜 목록은 큰 글자에서 「목록으로 보기」를 고른 때만.'),
 3:('StatusLine','meta 11 / 400 · ink-2 · 위 간격 8 · 한 문장.'),
 4:('ReviewRow','높이 32(= 24 + 간격 8) · 위 선 line-soft · 12.5 / 600 · ink · 주황 없음. 누르는 영역은 44.'),
 5:('DaySheet','위 모서리 26 · 손잡이 38 × 4 · 제목 18 / 700 · 금액 칸 48 · 메모 칸 44 · 저장 버튼 52(radius 14 · 16 / 600). 키보드가 열린 상태가 기본.'),
 6:('ColorChipRow','칩 높이 32 · radius 8 · 색 점 8px + 이름 12.5 / 500 · 자주 쓴 3개 + 「전체 ›」. 색만으로 뜻을 전하지 않습니다.'),
 7:('RecentEntryChip','높이 32 · radius 8 · inset 배경 · 메모 + 금액(600) + 색 점 7px + 카테고리 이름 11 / 500(분류가 없으면 점 없이 「분류 안 함」 11px). 색만으로 뜻을 전하지 않습니다.'),
 8:('DoneCard','ink 배경 · radius 16 · 제목 14 / 700 + 닫기 · 둘째 줄 13.5 · 버튼 높이 36(주 행동 + 방금 기록 취소). 라이트 · 다크에서 같은 모양.'),
 9:('ClassifyGroupRow','묶음 행 높이 52 · 제목 14 / 600 + 건수 12 · 오른쪽 추천 칩 30 · 펼치면 건별 행 40(체크 22 · 제외는 disabled 색).'),
 10:('HeroInsufficient','히어로의 자리 · 모양 그대로. 큰 숫자 = 이번 달 기록한 소비(0건이면 「아직 기록이 없어요」) · 보조 = 월급의 N%(월급이 없으면 없음) · 항로 바는 목표 눈금만 · 월말 예상과 여유는 — · 순항 배지 없음.'),
 11:('HomeHero 조건부 각주','기준 조정 줄 아래에 meta 11 / 1.4 · ink-3 · 위 간격 4 로 한 줄씩. 기존 요소 치수는 그대로이고 카드 높이만 줄 수만큼 늡니다.'),
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
  '    <p style="margin: 6px 0 0; font-size: 12.5px; line-height: 1.55; color: #475467;">조각은 v5 시안(홈 달력 · 하루 시트 · 완료 카드 · 분류하기)에서 그대로 가져왔습니다. 새 색은 없습니다 — 달력 칸은 brand-soft · ink-2 · ink-3 · disabled 만 씁니다.</p>\n'
  '    <div style="display: flex; align-items: flex-start; justify-content: space-between; gap: 18px; margin-top: 14px; background: #EDF0F7; border-radius: 18px; padding: 16px 14px 18px;">\n'+col1+'\n'+col2+'\n'+col3+'\n    </div>\n  </div>\n\n')

p = CANVAS / 'Components.dc.html'; s = p.read_text(encoding='utf-8')
START = '  <div>\n    <div style="font-size: 12px; font-weight: 600; letter-spacing: 0.1em; color: #626D88;">08 · v5'
end = s.rindex('</div>\n</x-dc>')
if START in s:                      # 있던 08절을 걷어 내고 다시 채운다
    s = s[:s.index(START)] + s[end:]
    end = s.rindex('</div>\n</x-dc>')
s = s[:end] + SECTION + s[end:]
assert s.count('08 · v5') == 1
p.write_text(s, encoding='utf-8')
print('Components 08절 다시 채움 · div', s.count('<div'), '/', s.count('</div>'))
