# 브라우저 검증 스크립트

앱은 빌드 도구가 없으므로 유닛 테스트 대신 **실제 브라우저에서 화면을 띄워** 확인한다.

## 준비

```bash
npm init -y && npm i -D playwright
npx playwright install chromium     # 시스템에 크로미움이 이미 있으면 CHROMIUM 환경변수로 지정
python3 -m http.server 8000         # 별도 터미널에서 계속 띄워둔다
```

## 실행

```bash
node test/screens.mjs    # 13개 화면이 콘솔 에러 없이 렌더되는지 + 스크린샷
node test/flows.mjs      # 자산/지출/목표 입력, 설정, 영속화, 단축키
node test/home.mjs       # 홈 화면 — 알림, 테마, 슬라이더 동기화, 목표 전환
node test/sliders.mjs    # 슬라이더 5종이 드래그 중 실시간으로 반응하는지
node test/regions.mjs    # 부분 갱신한 자리의 버튼·라벨·저장값이 멀쩡한지
```

환경변수: `URL`(기본 http://localhost:8000), `OUT`(스크린샷 폴더, 기본 ./test/out),
`CHROMIUM`(크로미움 실행 파일 경로).

## 왜 이렇게 검증하나

계산 로직은 순수 함수라 node 로도 확인할 수 있지만, 이 앱에서 실제로 깨진 것들은
**브라우저에서만 드러나는 문제**였다.

- 이벤트 리스너가 중복 등록돼 모달이 두 개 뜨던 것
- 라디오 묶음에서 선택값 대신 첫 옵션이 저장되던 것
- SVG 원호가 viewBox 를 벗어나 아래 텍스트와 겹치던 것
- 슬라이더를 끄는 도중 리렌더가 노드를 지워 드래그가 끊기던 것

특히 `sliders.mjs` 는 `page.mouse.down()` → 여러 번 `move` → `up` 으로 **진짜 드래그를
흉내내고, 아직 놓지 않은 상태에서** 화면 숫자를 읽는다. `fill()` 이나 `dispatchEvent`
로는 이 부류의 버그가 잡히지 않는다.

`regions.mjs` 는 반대쪽을 본다. 드래그 중에는 화면 전체가 아니라 출력 영역만
`innerHTML` 로 갈아끼우는데, 그 자리에 있던 버튼(목표 금액 프리셋, 전략 선택,
'필요액으로 맞추기')이 갈아끼운 뒤에도 동작하는지, 라벨과 실제 저장값이 어긋나지
않는지 확인한다. 값이 따라오는 것과 자리가 멀쩡한 것은 별개 문제다.
