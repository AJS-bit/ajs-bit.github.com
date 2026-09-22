# -*- coding: utf-8 -*-
"""캔버스 페이지(navi-redesign.html)의 내용 블록을 디스크의 아트보드로 다시 채운다.

design 스킬의 seed-canvas.mjs 없이도 캔버스를 갱신하기 위한 도구입니다. 캔버스의 편집 가능한 내용은
페이지 안 <script type="application/json" id="appifact-doc"> 한 블록에 있습니다 —
{"title", "content": {"files": {"<이름>.dc.html": "<원문>", ..., "canvas.json": "<원문>"}}, "comments": []}.
직렬화 규칙은 json(ensure_ascii=False, 구분자 ',' ':') + '<' → '\\u003c', 앞뒤 개행 하나. 편집기 코드는 건드리지 않습니다.

    python3 gen_canvas.py && python3 seed_doc.py      # canvas.json을 먼저 만든 뒤
    # 그다음 Artifact publish: file_path=navi-redesign.html, url=<캔버스 URL>, contract="0.1.31"

게시 전에 Artifact read(url)로 게시본을 한 번 열람해야 하며(안 하면 publish가 거절됨), 게시본의 files·comments가
로컬과 같은지 확인한 뒤 올리세요. 캔버스에서 직접 고친 내용이 있으면 그것부터 .dc.html로 가져와야 합니다.
"""
import json, pathlib, re, sys

CANVAS = pathlib.Path(__file__).resolve().parent.parent
PAGE = CANVAS / 'navi-redesign.html'
OPEN = '<script type="application/json" id="appifact-doc">'


def ser(obj):
    return '\n' + json.dumps(obj, ensure_ascii=False, separators=(',', ':')).replace('<', '\\u003c') + '\n'


def main():
    s = PAGE.read_text(encoding='utf-8')
    st = s.index(OPEN) + len(OPEN)
    en = s.index('</script>', st)
    raw = s[st:en]
    doc = json.loads(raw)
    if ser(doc) != raw:
        sys.exit('직렬화 규칙이 바뀌었습니다 — 변경 없이 다시 써도 원문과 달라집니다. 편집기 판이 바뀌었는지 확인하세요.')
    old = doc['content']['files']
    new = {}
    # canvas.json 을 맨 앞에 — 문서가 7MB 를 넘은 2026-09-22 판에서 canvas.json 이 마지막 키이면 에디터가 배치를 읽지 못해
    # 모든 장을 한 열로 늘어놓았다(헤드리스로 이분 탐색해 확인 · 맨 앞이면 정상). 원인은 에디터 안이라 순서로 피한다.
    new['canvas.json'] = (CANVAS / 'canvas.json').read_text(encoding='utf-8')
    for name in old:                                  # 기존 순서 유지, 디스크에서 사라진 아트보드는 뺀다
        if name.endswith('.dc.html'):
            f = CANVAS / name
            if f.exists():
                new[name] = f.read_text(encoding='utf-8')
        elif name != 'canvas.json':
            new[name] = old[name]
    for f in sorted(CANVAS.glob('*.dc.html')):
        new.setdefault(f.name, f.read_text(encoding='utf-8'))
    layout = json.loads(new['canvas.json'])
    missing = [a['file'] for a in layout['artboards'] if a['file'] not in new]
    if missing:
        sys.exit(f'canvas.json에 있으나 파일이 없는 아트보드: {missing}')
    added = [n for n in new if n not in old]
    changed = [n for n in new if n in old and new[n] != old[n]]
    removed = [n for n in old if n not in new]
    doc['content']['files'] = new
    PAGE.write_text(s[:st] + ser(doc) + s[en:], encoding='utf-8')
    print(f'files {len(old)} → {len(new)} · 추가 {len(added)} · 변경 {len(changed)} · 삭제 {len(removed)} · 아트보드 {len(layout["artboards"])} · 페이지 {len(layout["pages"])}')


if __name__ == '__main__':
    main()
