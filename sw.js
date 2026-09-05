/* 오프라인 지원 — 네트워크 우선, 실패 시 캐시 */
const CACHE = 'asset-compass-v1';
const ASSETS = [
  './', './index.html', './css/style.css', './manifest.webmanifest', './assets/icon.svg',
  './js/app.js', './js/store.js', './js/finance.js', './js/coach.js', './js/charts.js',
  './js/format.js', './js/ui.js', './js/seed.js',
  './js/views/dashboard.js', './js/views/assets.js', './js/views/spending.js',
  './js/views/goals.js', './js/views/coach.js',
];

/* addAll 은 **하나라도 실패하면 통째로 실패한다.** 그러면 서비스워커가 설치되지
   않아 오프라인 캐시가 조용히 없는 상태가 된다. 안드로이드 웹뷰에서 실제로 그랬다 —
   앱 안에 담긴 파일은 디렉터리 인덱스('./')를 줄 수 없어서 그 한 항목 때문에
   나머지 17개도 캐시되지 않았다. 하나씩 담고 실패한 것만 건너뛴다. */
self.addEventListener('install', (e) => {
  e.waitUntil(
    caches.open(CACHE)
      .then((c) => Promise.all(ASSETS.map((u) => c.add(u).catch(() => {}))))
      .then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', (e) => {
  e.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(keys.filter((k) => k !== CACHE).map((k) => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (e) => {
  if (e.request.method !== 'GET') return;
  e.respondWith(
    fetch(e.request)
      .then((res) => {
        const copy = res.clone();
        caches.open(CACHE).then((c) => c.put(e.request, copy)).catch(() => {});
        return res;
      })
      .catch(() => caches.match(e.request).then((r) => r || caches.match('./index.html')))
  );
});
