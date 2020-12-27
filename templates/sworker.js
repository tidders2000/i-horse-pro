var CACHE_STATIC_NAME = 'static-v2';
var CACHE_DYNAMIC_NAME = 'dynamic-v1';

self.addEventListener('install', function(event) {
    console.log('[Service Worker] Installing Service Worker ...', event);
    event.waitUntil(
        caches.open(CACHE_STATIC_NAME)
        .then(function(cache) {
            console.log('[Service Worker] Precaching App Shell');
            cache.addAll([
                '/accounts/error/',

                // '/home/templates/home.html',

                '/home/',
                '/static/css/base.css'

                // '/templates/base.html',
                // '/templates/basePW.html',
                // 'https://i-horse.s3.amazonaws.com/static/images/logo5.png',
                // 'https://i-horse.s3.amazonaws.com/static/css/base.css',
                // 'https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/css/materialize.min.css',
                // // 'https://cors-anywhere.herokuapp.com/https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css',
                // 'https://i-horse.s3.amazonaws.com/static/images/logo/mobile_logo.png'





            ]);
        })
    )
});

self.addEventListener('activate', function(event) {
    console.log('[Service Worker] Activating Service Worker ....', event);
    event.waitUntil(
        caches.keys()
        .then(function(keyList) {
            return Promise.all(keyList.map(function(key) {
                if (key !== CACHE_STATIC_NAME && key !== CACHE_DYNAMIC_NAME) {
                    console.log('[Service Worker] Removing old cache.', key);
                    return caches.delete(key);
                }
            }));
        })
    );
    return self.clients.claim();
});

self.addEventListener('fetch', function(event) {
    event.respondWith(
        caches.match(event.request)
        .then(function(response) {
            if (response) {
                console.log(response.status)
                return response;
            } else {
                return fetch(event.request)
                    .then(function(res) {
                        return caches.open(CACHE_DYNAMIC_NAME)
                            .then(function(cache) {
                                cache.put(event.request.url, res.clone());
                                return res;
                            })
                    })
                    .catch(function(err) {
                        return caches.open(CACHE_STATIC_NAME)
                            .then(function(cache) {
                                return cache.match('/accounts/error/');
                            });

                    });
            }
        })
    );
});