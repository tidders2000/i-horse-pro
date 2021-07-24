importScripts('https://storage.googleapis.com/workbox-cdn/releases/6.0.2/workbox-sw.js');

const VERSION = '2.0';

if (workbox) {
    console.log(`Yay! Workbox is loaded 🎉 `);
    // console.log(VERSION)
} else {
    console.log(`Boo! Workbox didn't load 😬`);
}

console.log(VERSION)

const {setCatchHandler,setDefaultHandler,registerRoute} = workbox.routing;

const {NetworkOnly,NetworkFirst,CacheFirst} = workbox.strategies;
const {StaleWhileRevalidate} = workbox.strategies;
const {CacheableResponsePlugin } = workbox.cacheableResponse;
const {ExpirationPlugin } = workbox.expiration;

const {  pageCache,
    imageCache,
    staticResourceCache,
    googleFontsCache,
    offlineFallback,} = workbox.recipes




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

//warm the cache



//page cacheing
pageCache();

//static cache
staticResourceCache();

//cache images
imageCache();

//cache fonts

googleFontsCache();