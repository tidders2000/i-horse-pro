importScripts('https://storage.googleapis.com/workbox-cdn/releases/6.0.2/workbox-sw.js');

const VERSION = '1.9';

if (workbox) {
    console.log(`Yay! Workbox is loaded 🎉 `);

} else {
    console.log(`Boo! Workbox didn't load 😬`);
}
    // console.log(VERSION)
console.log(VERSION)

const {setCatchHandler,setDefaultHandler,registerRoute} = workbox.routing;

const {NetworkOnly,NetworkFirst,CacheFirst} = workbox.strategies;
const {StaleWhileRevalidate} = workbox.strategies;
const {CacheableResponsePlugin } = workbox.cacheableResponse;
const {ExpirationPlugin } = workbox.expiration;
const { precacheAndRoute } = workbox.precaching
const {BackgroundSyncPlugin,Queue} = workbox.backgroundSync


const {  pageCache,
    imageCache,
    staticResourceCache,
    googleFontsCache,
    offlineFallback} = workbox.recipes

 workbox.routing.registerRoute(/\/appointment\/edit\//,
  new workbox.strategies.NetworkOnly({
    plugins: [
      new workbox.backgroundSync.BackgroundSyncPlugin('po-data-queue', {
        maxRetentionTime: 2 * 24 * 60 // two days
      })
    ]
  }),
 'POST'
);

const queue = new Queue('myQueueName');

self.addEventListener('fetch', (event) => {
  // Add in your own criteria here to return early if this
  // isn't a request that should use background sync.
  if (event.request.method !== 'POST') {
    return;
  }

  const bgSyncLogic = async () => {
    try {
      const response = await fetch(event.request.clone());
      return response;
    } catch (error) {
      await queue.pushRequest({request: event.request});
      return error;
    }
  };

  event.respondWith(bgSyncLogic());
});

    
  



    precacheAndRoute([
      {url: 'https://i-horse.s3.amazonaws.com/static/manifest.json', revision: '383676' },
     ]
      // ... other entries ...
    );


setDefaultHandler(
        new NetworkOnly()
      );

//offline fallback


const pageFallback = '/offline.html';
const imageFallback = false;
const fontFallback = false;

setDefaultHandler(
  new NetworkOnly()
);

self.addEventListener('install', event => {
  const files = [pageFallback];
  if (imageFallback) {
    files.push(imageFallback);
  }
  if (fontFallback) {
    files.push(fontFallback);
  }

  event.waitUntil(self.caches.open('workbox-offline-fallbacks').then(cache => cache.addAll(files)));
});

const handler = async (options) => {
  const dest = options.request.destination;
  const cache = await self.caches.open('workbox-offline-fallbacks');

  if (dest === 'document') {
    return (await cache.match(pageFallback)) || Response.error();
  }

  if (dest === 'image' && imageFallback !== false) {
    return (await cache.match(imageFallback)) || Response.error();
  }

  if (dest === 'font' && fontFallback !== false) {
    return (await cache.match(fontFallback)) || Response.error();
  }

  return Response.error();
};

setCatchHandler(handler);





//page cacheing
pageCache();

//static cache
staticResourceCache();

//cache images
imageCache();

//cache fonts

googleFontsCache();

