/* 오프라인 지원 — 네트워크 우선, 실패 시 캐시 */
const CACHE = 'asset-compass-v1';
const ASSETS = [
  './', './index.html', './css/style.css', './manifest.webmanifest', './assets/icon.svg',
  './js/app.js', './js/store.js', './js/finance.js', './js/coach.js', './js/charts.js',
  './js/format.js', './js/ui.js', './js/seed.js',
  './js/views/dashboard.js', './js/views/assets.js', './js/views/spending.js',
  './js/views/goals.js', './js/views/coach.js',
];

self.addEventListener('install', (e) => {
  e.waitUntil(caches.open(CACHE).then((c) => c.addAll(ASSETS)).then(() => self.skipWaiting()));
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
