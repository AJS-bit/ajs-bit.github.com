# -*- coding: utf-8 -*-
"""라이트 아트보드를 다크 토큰으로 변환한다. 데이터 팔레트와 브랜드 그라디언트는 유지."""
import re
import pathlib

SRC = pathlib.Path('/home/user/ajs-bit.github.com/design/canvas')

MAP = {
    '#EDF0F7': '#080C16',   # canvas
    '#FFFFFF': '#121A2B',   # surface
    '#F8FAFD': '#151D30',
    '#E3E8F1': '#232D45',   # line
    '#EFF2F8': '#1E2739',   # line-soft
    '#F3F5FA': '#1E2739',   # line-row
    '#E8ECF5': '#232D45',   # track
    '#F4F6FB': '#1A2337',   # inset
    '#F0F2F7': '#1E2739',   # mute badge bg
    '#101828': '#EAEFF8',   # ink
    '#475467': '#A5B2C9',   # ink-2
    '#5B6880': '#8494AD',
    '#6B7794': '#8494AD',   # ink-3
    '#98A4BC': '#6E7C96',   # ink-4
    '#8593AD': '#7A879F',
    '#B4BECD': '#5D6B85',   # disabled
    '#C4CCDA': '#46536E',
    '#D7DEEA': '#2E3A54',
    '#CFD7E6': '#39455F',   # input line
    '#B9C3D6': '#4E5B76',
    '#D6DDE9': '#2E3A54',
    '#DCE2EC': '#263049',
    '#3556E6': '#7FA0FF',   # brand
    '#2743C4': '#A8BCF5',
    '#E9EDFD': '#1B2748',   # brand soft
    '#3B4E8F': '#A8BCF5',
    '#6B85EC': '#5E7DDA',   # saving
    '#8FA6F2': '#6C86D8',
    '#4B6BDE': '#8FA6F2',
    '#0F7B47': '#3DD489',   # positive
    '#E4F4EA': '#0F2C22',
    '#9CCDB2': '#2A6B4A',
    '#C9E5D5': '#1E4534',
    '#14603D': '#8FD9B4',
    '#6FBE94': '#2A6B4A',
    '#B45309': '#F5B544',   # warning
    '#FDF1E0': '#2E2617',
    '#DE8A2A': '#A9772C',
    '#7A3E0A': '#F0C88A',
    '#C0342F': '#E8635F',   # negative
    '#FCEBEA': '#331C1F',
    '#D9827E': '#8E4C49',
    '#7C221E': '#FFB3B0',
    '#7A3FE4': '#B79BFF',   # violet
    '#6E6BEE': '#9AA0FF',
    '#F1EAFD': '#241D3D',
    '#6B32D6': '#C4A9FF',
    '#4E2496': '#C9B4FF',
    '#F7F4FE': '#1E1B33',
    '#B79BFF': '#B79BFF',
    '#0B7FBF': '#5CC3F5',   # sky
    '#E4F2FB': '#12293C',
    '#0A5F8F': '#9CD8F5',
    '#7EC4E8': '#2A5A78',
    '#2A3245': '#04070E',   # modal scrim
}
KEYS = sorted(MAP, key=len, reverse=True)
PAT = re.compile('|'.join(re.escape(k) for k in KEYS), re.IGNORECASE)

BRAND_GRAD_DARK = 'linear-gradient(140deg, #7FA0FF 0%, #B79BFF 100%)'
BRAND_GRAD = 'linear-gradient(140deg, #3556E6 0%, #7A3FE4 100%)'
ARROW = 'M21.3 3.1 3.9 10.4c-.9.4-.8 1.7.1 2l6.6 2.2c.3.1.5.3.6.6l2.2 6.6c.3.9 1.6 1 2 .1L22.7 4.5c.3-.8-.6-1.7-1.4-1.4Z'


def darken(text):
    out = PAT.sub(lambda m: MAP[m.group(0).upper()], text)
    out = out.replace('rgba(16,24,40,.04), 0 6px 20px -14px rgba(16,24,40,.24)',
                      'rgba(0,0,0,.3), 0 10px 28px -16px rgba(0,0,0,.7)')
    out = out.replace('rgba(16,24,40,.04), 0 8px 24px -16px rgba(16,24,40,.28)',
                      'rgba(0,0,0,.3), 0 12px 32px -18px rgba(0,0,0,.75)')
    out = out.replace('rgba(16,24,40,.06)', 'rgba(0,0,0,.45)')
    out = out.replace('rgba(16,24,40,.08)', 'rgba(0,0,0,.5)')
    out = out.replace('rgba(16,24,40,.2)', 'rgba(0,0,0,.6)')
    out = out.replace('rgba(16,24,40,.5)', 'rgba(0,0,0,.8)')
    # 브랜드 그라디언트와 마크 화살표는 라이트/다크 동일
    out = out.replace(BRAND_GRAD_DARK, BRAND_GRAD)
    out = re.sub(r'fill="#121A2B"(\s*><path d="' + re.escape(ARROW) + r')', r'fill="#FFFFFF"\1', out)
    # 부채 해치 패턴
    out = out.replace('#E0908C 0 4px, #F0BFBD 4px 8px', '#8E4C49 0 4px, #B36F6C 4px 8px')
    return out


SCREENS = ['Main', 'HomeScroll', 'Assets', 'Debts', 'Strategy', 'Spending', 'Ledger',
           'Limits', 'Goals', 'GoalDesign', 'Future', 'Payoff', 'Onboarding']
MODALS = ['LimitEditor', 'TransactionAdd', 'ProfileDialog', 'AssetDialog', 'DebtDialog',
          'GoalDialog', 'RecurringDialog', 'MonthlyClose', 'ImportReview', 'CoachPanel',
          'AlertsPanel', 'PeerDialog']
DESKTOP = ['DesktopHome']

if __name__ == '__main__':
    n = 0
    for name in SCREENS + MODALS + DESKTOP:
        src = SRC / f'{name}.dc.html'
        dst = SRC / ('DarkHome.dc.html' if name == 'Main' else f'Dark{name}.dc.html')
        dst.write_text(darken(src.read_text(encoding='utf-8')), encoding='utf-8')
        n += 1
    print(f'{n} dark artboards written')
