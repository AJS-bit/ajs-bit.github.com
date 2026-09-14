"""plan/v4-stocks.md → 검토용 HTML 한 장. NAVI v3 토큰을 그대로 쓴다."""
import re, html, pathlib, sys

SRC = pathlib.Path(__file__).resolve().parent.parent / 'v4-stocks.md'
OUT = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else SRC.parent / 'v4-stocks.html'

def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
    s = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'\[ \]', '<span class="box"></span>', s)
    return s

lines = SRC.read_text().split('\n')
out, i, in_list = [], 0, False
first_h1 = True

def close_list():
    global in_list
    if in_list:
        out.append('</ul>' if in_list == 'ul' else '</ol>'); in_list = False

while i < len(lines):
    ln = lines[i]
    if ln.startswith('```'):
        close_list()
        buf = []; i += 1
        while i < len(lines) and not lines[i].startswith('```'):
            buf.append(lines[i]); i += 1
        out.append('<pre>' + html.escape('\n'.join(buf)) + '</pre>'); i += 1; continue
    if ln.startswith('|'):
        close_list()
        rows = []
        while i < len(lines) and lines[i].startswith('|'):
            rows.append(lines[i]); i += 1
        cells = lambda r: [c.strip() for c in r.strip().strip('|').split('|')]
        head = cells(rows[0]); body = [cells(r) for r in rows[2:]]
        t = ['<div class="tw"><table><thead><tr>' + ''.join(f'<th>{inline(c)}</th>' for c in head) + '</tr></thead><tbody>']
        for r in body:
            t.append('<tr>' + ''.join(f'<td>{inline(c)}</td>' for c in r) + '</tr>')
        t.append('</tbody></table></div>')
        out.append(''.join(t)); continue
    if ln.startswith('# '):
        close_list()
        out.append(f'<h1>{inline(ln[2:])}</h1>'); i += 1; continue
    if ln.startswith('## '):
        close_list()
        m = re.match(r'(\d+)\.\s+(.*)', ln[3:])
        if m:
            out.append(f'<h2 id="s{m.group(1)}"><span class="num">§{m.group(1)}</span>{inline(m.group(2))}</h2>')
        else:
            out.append(f'<h2>{inline(ln[3:])}</h2>')
        i += 1; continue
    if ln.startswith('### '):
        close_list()
        out.append(f'<h3>{inline(ln[4:])}</h3>'); i += 1; continue
    if ln.strip() == '---':
        close_list(); out.append('<hr>'); i += 1; continue
    if ln.startswith('- '):
        if in_list != 'ul':
            close_list(); out.append('<ul>'); in_list = 'ul'
        out.append(f'<li>{inline(ln[2:])}</li>'); i += 1; continue
    m = re.match(r'^(\d+)\.\s+(.*)', ln)
    if m:
        if in_list != 'ol':
            close_list(); out.append('<ol>'); in_list = 'ol'
        out.append(f'<li>{inline(m.group(2))}</li>'); i += 1; continue
    if ln.strip() == '':
        close_list(); i += 1; continue
    # 문단 — 이어지는 줄을 합친다
    buf = [ln]; i += 1
    while i < len(lines) and lines[i].strip() and not re.match(r'^(#|\||```|- |---|\d+\.\s)', lines[i]):
        buf.append(lines[i]); i += 1
    close_list()
    txt = ' '.join(buf)
    if txt.startswith('작성 '):
        out.append(f'<p class="meta">{inline(txt)}</p>')
    else:
        out.append(f'<p>{inline(txt)}</p>')
close_list()
body = '\n'.join(out)

CSS = """
:root{
  --canvas:#EDF0F7;--surface:#FFFFFF;--inset:#F4F6FB;--line:#E3E8F1;--line-soft:#EFF2F8;
  --ink:#101828;--ink2:#475467;--ink3:#626D88;--ink4:#697182;
  --brand:#3556E6;--brand-soft:#E9EDFD;--violet:#7A3FE4;--violet-soft:#F1EAFD;
  --pos:#0F7B47;--warn:#B45309;--warn-soft:#FDF1E0;
  --shadow:0 1px 2px rgba(16,24,40,.04),0 6px 20px -14px rgba(16,24,40,.24);
  color-scheme:light;
}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){
  --canvas:#080C16;--surface:#121A2B;--inset:#1A2337;--line:#232D45;--line-soft:#1E2739;
  --ink:#EAEFF8;--ink2:#A5B2C9;--ink3:#8595AE;--ink4:#7E8AA2;
  --brand:#7FA0FF;--brand-soft:#1B2748;--violet:#B79BFF;--violet-soft:#241D3D;
  --pos:#3DD489;--warn:#F5B544;--warn-soft:#2E2617;
  --shadow:0 1px 2px rgba(0,0,0,.3),0 6px 20px -14px rgba(0,0,0,.6);color-scheme:dark}}
:root[data-theme="dark"]{
  --canvas:#080C16;--surface:#121A2B;--inset:#1A2337;--line:#232D45;--line-soft:#1E2739;
  --ink:#EAEFF8;--ink2:#A5B2C9;--ink3:#8595AE;--ink4:#7E8AA2;
  --brand:#7FA0FF;--brand-soft:#1B2748;--violet:#B79BFF;--violet-soft:#241D3D;
  --pos:#3DD489;--warn:#F5B544;--warn-soft:#2E2617;
  --shadow:0 1px 2px rgba(0,0,0,.3),0 6px 20px -14px rgba(0,0,0,.6);color-scheme:dark}
*{box-sizing:border-box}
body{margin:0;background:var(--canvas);color:var(--ink);
  font-family:'IBM Plex Sans KR','Apple SD Gothic Neo','Noto Sans KR',system-ui,sans-serif;
  font-size:14.5px;line-height:1.7;-webkit-font-smoothing:antialiased;
  font-variant-numeric:tabular-nums;padding:0 16px}
main{max-width:720px;margin:0 auto;padding-block:40px 96px}
.mark{display:inline-flex;align-items:center;gap:8px;margin-bottom:22px}
.mark i{width:26px;height:26px;border-radius:8px;display:inline-flex;align-items:center;justify-content:center;
  background:linear-gradient(140deg,#3556E6 0%,#7A3FE4 100%)}
.mark span{font-size:13px;font-weight:700;letter-spacing:.06em;color:var(--ink)}
.mark em{font-style:normal;font-size:12px;color:var(--ink3);font-weight:500}
h1{font-size:28px;font-weight:700;letter-spacing:-.03em;line-height:1.25;margin:0 0 6px;text-wrap:balance}
.meta{font-size:12.5px;color:var(--ink3);margin:0 0 8px}
h2{font-size:19px;font-weight:700;letter-spacing:-.025em;line-height:1.3;margin:44px 0 12px;
  display:flex;align-items:baseline;gap:10px;text-wrap:balance}
h2 .num{font-size:11px;font-weight:600;letter-spacing:.07em;color:var(--brand);
  background:var(--brand-soft);border-radius:99px;padding:3px 9px;flex-shrink:0;transform:translateY(-3px)}
h3{font-size:15px;font-weight:600;letter-spacing:-.015em;margin:26px 0 8px;color:var(--ink)}
p{margin:0 0 12px;color:var(--ink2);max-width:66ch}
p strong{color:var(--ink);font-weight:600}
ul,ol{margin:0 0 14px;padding-left:18px;color:var(--ink2)}
ol li::marker{color:var(--brand);font-weight:600}
li{margin:3px 0}
li strong{color:var(--ink);font-weight:600}
code{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:12.5px;
  background:var(--inset);border-radius:5px;padding:1px 5px;color:var(--ink)}
pre{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:12.5px;line-height:1.6;
  background:var(--inset);border:1px solid var(--line);border-radius:12px;padding:12px 14px;
  margin:10px 0 16px;overflow-x:auto;color:var(--ink)}
hr{border:0;border-top:1px solid var(--line);margin:36px 0 0}
.tw{overflow-x:auto;margin:10px 0 18px;border:1px solid var(--line);border-radius:12px;background:var(--surface)}
table{border-collapse:collapse;width:100%;font-size:13px}
th{text-align:left;font-size:11px;font-weight:600;letter-spacing:.06em;color:var(--ink3);
  padding:9px 12px;border-bottom:1px solid var(--line);white-space:nowrap}
td{padding:9px 12px;border-bottom:1px solid var(--line-soft);vertical-align:top;color:var(--ink2);line-height:1.55}
tr:last-child td{border-bottom:0}
td:first-child{color:var(--ink);font-weight:500;white-space:nowrap}
td strong{color:var(--ink);font-weight:600}
.box{display:inline-block;width:13px;height:13px;border:1.5px solid var(--ink4);border-radius:4px;
  vertical-align:-2px;margin-right:6px}
/* 결정 절만 띄운다 */
#s9{margin-top:52px}
#s9 + p, #s9 ~ .decide{}
.decide{background:var(--surface);border:1px solid var(--line);border-radius:18px;padding:6px 16px 4px;
  box-shadow:var(--shadow);margin:12px 0 18px}
.decide .tw{border:0;margin:0;background:transparent}
.decide td:first-child{color:var(--brand);font-weight:700}
.decide td:nth-child(3){color:var(--ink);font-weight:500}
.foot{margin-top:56px;padding-top:16px;border-top:1px solid var(--line);font-size:12px;color:var(--ink3)}
.foot a{color:var(--brand);text-decoration:none}
@media (max-width:480px){h1{font-size:24px}h2{font-size:17px}td:first-child{white-space:normal}}
"""

# 결정 표만 카드로 감싼다 (§9 바로 뒤의 첫 표)
body = re.sub(r'(<h2 id="s9">.*?</h2>\s*)(<div class="tw">.*?</table></div>)',
              r'\1<div class="decide">\2</div>', body, count=1, flags=re.S)

page = f'''<title>NAVI v4 계획</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+KR:wght@400;500;600;700&display=swap">
<style>{CSS}</style>
<main>
<div class="mark"><i><svg width="14" height="14" viewBox="0 0 24 24" fill="#FFFFFF"><path d="M20.28 2.32 2.88 9.62c-.9.4-.8 1.7.1 2l6.6 2.2c.3.1.5.3.6.6l2.2 6.6c.3.9 1.6 1 2 .1L21.68 3.72c.3-.8-.6-1.7-1.4-1.4Z"/></svg></i><span>NAVI</span><em>· v4 계획 초안</em></div>
{body}
<div class="foot">원본 <a href="https://github.com/AJS-bit/ajs-bit.github.com/blob/claude/navi-ui-ux-redesign-nzxoxz/plan/v4-stocks.md">plan/v4-stocks.md</a> · 커밋 e190fd9 · 이 페이지는 그 파일을 그대로 옮긴 것이라 두 곳이 다르면 파일이 기준입니다.</div>
</main>'''
OUT.write_text(page)
print('wrote', OUT, len(page), 'bytes')
