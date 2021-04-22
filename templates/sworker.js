
// var CACHE_STATIC_NAME = 'static-v5';
// var CACHE_DYNAMIC_NAME = 'dynamic-v2';

// async function getCSRFToken() {
//   let response = await fetch("/appointment/get_csrftoken_from_cookie");
//   let decoded = await response.json();
//   return decoded.token;
// }
// async function fetcher(data) {
//   try {
//     let csrftoken = await getCSRFToken()
//     let form = new URLSearchParams(data.value.data);
//     form.set("csrfmiddlewaretoken", csrftoken);
//     const response = await fetch(data.value.url, {
//       method: "POST",
//       body: form.toString(),
//       headers: {
//         'Accept': 'application/json',
//         'X-Requested-With': 'XMLHttpRequest',
//         'X-CSRFToken': csrftoken,
//         'Content-Type': "application/x-www-form-urlencoded"
//       }
//     })
//     const result = await response.json();
//     return { success: result.success, key: data.key }
//   } catch(e) {
//     return { success: false, key: data.key }
//   }
// }


// async function sendToServer() {
//     let pending = await readDB();
//     let results = await Promise.all(pending.map(fetcher))
//     await removeFromDB(results.filter(r => r.success).map(r => r.key));
//   }
//   self.onsync = function(event) {
//     if (event.tag == 'appoint-post') {
//       event.waitUntil(sendToServer());
//     }
//   }

//   function removeFromDB(keys) {
//     return new Promise((resolve, reject) => {
//       let db = indexedDB.open("appoint");
//       db.onsuccess = e => {
//         function removeNextKey() {
//           let nextKey = keys.shift();
//           if (!nextKey) { return resolve(); }
//           let rq = store.delete(nextKey);
//           rq.onsuccess = ev => { removeNextKey(); }
//           rq.onerror = err => { console.error(err); removeNextKey(); }
//         }
//         let store = db.result.transaction("appoint", "readwrite").objectStore("appoint");
//         removeNextKey();
//       }
//     })
//   }
//   function readDB() {
//     return new Promise((resolve, reject) => {
//       let db = indexedDB.open("appoint");
//       db.onsuccess = e => {
//         let results = [];
//         let rq = db.result.transaction("appoint", 'readwrite').objectStore("appoint").openCursor();
//         rq.onsuccess = ev => {
//           let cursor = ev.target.result;
//           if (cursor) {
//             results.push({key: cursor.primaryKey, value: cursor.value});
//             cursor.continue();
//           } else {
//             resolve(results);
//           }
//         }
//       }
//       db.onerror = err => { reject(err); }
//     })
//   }

  

// self.addEventListener('install', function(event) {
//     console.log('[Service Worker] Installing Service Worker ...', event);
//     event.waitUntil(
//         caches.open(CACHE_STATIC_NAME)
//         .then(function(cache) {
//             console.log('[Service Worker] Precaching App Shell');
//             cache.addAll([
//                 '/offline.html',
           

//                 // '/home/templates/home.html',

//                 '/home/',
//                 '/cal/caltwo',


               
//                 // '/templates/basePW.html',
//                 // 'https://i-horse.s3.amazonaws.com/static/images/logo5.png',{ mode: 'no-cors'},
//                 // 'https://i-horse.s3.amazonaws.com/static/css/base.css',
//                 // 'https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/css/materialize.min.css',
//                 // // 'https://cors-anywhere.herokuapp.com/https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css',
//                 // 'https://i-horse.s3.amazonaws.com/static/images/logo/mobile_logo.png'





//             ]);
//         })
//     )
// });

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

// self.addEventListener('fetch', function(event) {
//     event.respondWith(
//         caches.match(event.request)
//         .then(function(response) {
//             if (response) {
//                 console.log(response.status)
//                 return response;
//             } else {
//                 return fetch(event.request)
//                     .then(function(res) {
//                         return caches.open(CACHE_DYNAMIC_NAME)
//                             .then(function(cache) {
//                                 cache.put(event.request.url, res.clone());
//                                 return res;
//                             })
//                     })
//                     .catch(function(err) {
//                         return caches.open(CACHE_STATIC_NAME)
//                             .then(function(cache) {
//                                 return cache.match('/offline.html');
//                             });

//                     });
//             }
//         })
//     );
// });






// // importScripts('https://storage.googleapis.com/workbox-cdn/releases/6.1.1/workbox-sw.js');

// // const VERSION = '5.0';
// // console.log('Hello from service-worker.js');

// // const {registerRoute} = workbox.routing;
// // const {CacheFirst} = workbox.strategies;
// // const {NetworkFirst} = workbox.strategies;
// // const {CacheableResponse} = workbox.cacheableResponse;
// // const {StaleWhileRevalidate} = workbox.strategies;
// // const {CacheableResponsePlugin} = workbox.cacheableResponse;
// // const {ExpirationPlugin} = workbox.expiration;
// // const {precacheAndRoute} =workbox.precaching
// // const {getCacheKeyForUR} = workbox.precaching

// // const {setCatchHandler} = workbox.routing
// // const {BackgroundSyncPlugin} = workbox.backgroundSync
// // const {NetworkOnly} = workbox.strategies

// // precacheAndRoute([
// //    {url: '/offline.html', revision: '00001' },
   
// //     // ... other entries ...
// //   ]);


// //   const bgSyncPlugin = new BackgroundSyncPlugin('queue', {
// //     maxRetentionTime: 24 * 60 // Retry for max of 24 Hours
// // });


// // registerRoute(
// //     'http://127.0.0.1:8000/appointment/edit/',
// //     new NetworkOnly({
// //         plugins: [bgSyncPlugin]
// //       }),
// //       'POST'
// //     );

// // // Cache page navigations (html) with a Network First strategy
// // registerRoute(
// //   // Check to see if the request is a navigation to a new page
// //   ({ request }) => request.mode === 'navigate',
// //   // Use a Network First caching strategy
// //   new NetworkFirst({
// //     // Put all cached files in a cache named 'pages'
// //     cacheName: 'pages',
// //     plugins: [
// //       // Ensure that only requests that result in a 200 status are cached
// //       new CacheableResponsePlugin({
// //         statuses: [200],
// //       }),
// //     ],
// //   }),
// // );

// // // Cache CSS, JS, and Web Worker requests with a Stale While Revalidate strategy
// // registerRoute(
// //   // Check to see if the request's destination is style for stylesheets, script for JavaScript, or worker for web worker
// //   ({ request }) =>
// //     request.destination === 'style' ||
// //     request.destination === 'script' ||
// //     request.destination === 'worker',
// //   // Use a Stale While Revalidate caching strategy
// //   new StaleWhileRevalidate({
// //     // Put all cached files in a cache named 'assets'
// //     cacheName: 'assets',
// //     plugins: [
// //       // Ensure that only requests that result in a 200 status are cached
// //       new CacheableResponsePlugin({
// //         statuses: [200],
// //       }),
// //     ],
// //   }),
// // );

// // // Cache images with a Cache First strategy
// // registerRoute(
// //   // Check to see if the request's destination is style for an image
// //   ({ request }) => request.destination === 'image',
// //   // Use a Cache First caching strategy
// //   new CacheFirst({
// //     // Put all cached files in a cache named 'images'
// //     cacheName: 'images',
// //     plugins: [
// //       // Ensure that only requests that result in a 200 status are cached
// //       new CacheableResponsePlugin({
// //         statuses: [200],
// //       }),
// //       // Don't cache more than 50 items, and expire them after 30 days
// //       new ExpirationPlugin({
// //         maxEntries: 50,
// //         maxAgeSeconds: 60 * 60 * 24 * 30, // 30 Days
// //       }),
// //     ],
// //   }),
// // );