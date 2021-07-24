importScripts('https://storage.googleapis.com/workbox-cdn/releases/6.0.2/workbox-sw.js');
// const VERSION = '1.0';
// const CACHE_STATIC_NAME='1.0'

// self.addEventListener('activate', function(event) {
//     console.log('[Service Worker] Activating Service Worker ....', event);
//     event.waitUntil(
//         caches.keys()
//         .then(function(keyList) {
//             return Promise.all(keyList.map(function(key) {
//                 if (key !== CACHE_STATIC_NAME && key !== CACHE_DYNAMIC_NAME) {
//                     console.log('[Service Worker] Removing old cache.', key);
//                     return caches.delete(key);
//                 }
//             }));
//         })
//     );
//     return self.clients.claim();
// });



if (workbox) {
    console.log(`Yay! Workbox is loaded 🎉 `);
    // console.log(VERSION)
} else {
    console.log(`Boo! Workbox didn't load 😬`);
}

const {registerRoute} = workbox.routing;
const {CacheFirst} = workbox.strategies;
const {NetworkFirst} = workbox.strategies;
const {StaleWhileRevalidate} = workbox.strategies
const {CacheableResponsePlugin } = workbox.cacheableResponse;
const {ExpirationPlugin } = workbox.expiration



// Cache page navigations (html) with a Network First strategy
registerRoute(
  // Check to see if the request is a navigation to a new page
  ({ request }) => request.mode === 'navigate',
  // Use a Network First caching strategy
  new NetworkFirst({
    // Put all cached files in a cache named 'pages'
    cacheName: 'pages',
    plugins: [
      // Ensure that only requests that result in a 200 status are cached
      new CacheableResponsePlugin({
        statuses: [200],
      }),
    ],
  }),
);

// Cache CSS, JS, and Web Worker requests with a Stale While Revalidate strategy
registerRoute(
  // Check to see if the request's destination is style for stylesheets, script for JavaScript, or worker for web worker
  ({ request }) =>
    request.destination === 'style' ||
    request.destination === 'script' ||
    request.destination === 'worker',
  // Use a Stale While Revalidate caching strategy
  new StaleWhileRevalidate({
    // Put all cached files in a cache named 'assets'
    cacheName: 'assets',
    plugins: [
      // Ensure that only requests that result in a 200 status are cached
      new CacheableResponsePlugin({
        statuses: [200],
      }),
    ],
  }),
);

// Cache images with a Cache First strategy
registerRoute(
  // Check to see if the request's destination is style for an image
  ({ request }) => request.destination === 'image',
  // Use a Cache First caching strategy
  new CacheFirst({
    // Put all cached files in a cache named 'images'
    cacheName: 'images',
    plugins: [
      // Ensure that only requests that result in a 200 status are cached
      new CacheableResponsePlugin({
        statuses: [200],
      }),
      // Don't cache more than 50 items, and expire them after 30 days
      new ExpirationPlugin({
        maxEntries: 50,
        maxAgeSeconds: 60 * 60 * 24 * 30, // 30 Days
      }),
    ],
  }),
);