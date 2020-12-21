importScripts('https://storage.googleapis.com/workbox-cdn/releases/5.0.0/workbox-sw.js');

const VERSION = '2.6';

if (workbox) {
    console.log(`Yay! Workbox is loaded 🎉`);
} else {
    console.log(`Boo! Workbox didn't load 😬`);
}


const OFFLINE_URL = '/accounts/error/';
const appShell = [

    '/static/css/base.css',
    '/static/images/logo5.png',
    '/home/'

].map((partialUrl) => `${location.protocol}//${location.host}${partialUrl}`);

// Precache the shell.
workbox.precaching.precacheAndRoute(appShell.map(url => ({
    url,
    revision: null,
})));

// Serve the app shell from the cache.
workbox.routing.registerRoute(({ url }) => appShell.includes(url), new workbox.strategies.CacheOnly());

//Serve the other pages from the cache and make a request to update the value in the cache.
//Limit the cache to 5 entries.
workbox.routing.registerRoute(
    ({ url }) => !appShell.includes(url),
    new workbox.strategies.StaleWhileRevalidate({
        cacheName: 'dynamic-cache',
        plugins: [new workbox.expiration.ExpirationPlugin({
            maxEntries: 5,
        })],
    })
);
//cache all images
workbox.routing.registerRoute(
    ({ request }) => request.destination === 'image',
    new workbox.strategies.CacheFirst({
        cacheName: 'images',
        plugins: [
            new workbox.expiration.ExpirationPlugin({
                maxEntries: 60,

            }),
        ],
    })
);
// Handle offline.
// From https://developers.google.com/web/tools/workbox/guides/advanced-recipes#provide_a_fallback_response_to_a_route
workbox.routing.setCatchHandler(({ event }) => {
    console.log(event)
    switch (event.request.method) {
        case 'GET':
            return caches.match(OFFLINE_URL);
        default:
            return Response.error();
    }
});

// Register event listener for the 'push' event.
// self.addEventListener('push', function(event) {
//     // Retrieve the textual payload from event.data (a PushMessageData object).
//     // Other formats are supported (ArrayBuffer, Blob, JSON), check out the documentation
//     // on https://developer.mozilla.org/en-US/docs/Web/API/PushMessageData.
//     const eventInfo = event.data.text();
//     const data = JSON.parse(eventInfo);
//     const head = data.head || 'New Notification 🕺🕺';
//     const body = data.body || 'This is default content. Your notification didn\'t have one 🙄🙄';

//     // Keep the service worker alive until the notification is created.
//     event.waitUntil(
//         self.registration.showNotification(head, {
//             body: body,
//             icon: 'https://i.imgur.com/MZM3K5w.png'
//         })
//     );
// });