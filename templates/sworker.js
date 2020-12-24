importScripts('https://storage.googleapis.com/workbox-cdn/releases/5.0.0/workbox-sw.js');

const VERSION = '1.0';

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
    console.log(VERSION)
} else {
    console.log(`Boo! Workbox didn't load 😬`);
}


const OFFLINE_URL = '/accounts/error/';
const appShell = [

    // '/static/css/base.css',
    // '/static/images/logo5.png',
    //'/home/'

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

// importScripts('https://www.gstatic.com/firebasejs/8.2.0/firebase-app.js');
// importScripts('https://www.gstatic.com/firebasejs/8.2.0/firebase-messaging.js');
// firebase.initializeApp({
//     apiKey: "AIzaSyD4p8Ud9SI8Cv_u1qxpyH7v7nP0K0S5rPU",
//     authDomain: "ihorse-8e7f4.firebaseapp.com",
//     projectId: "ihorse-8e7f4",
//     storageBucket: "ihorse-8e7f4.appspot.com",
//     messagingSenderId: "51294489856",
//     appId: "1:51294489856:web:021c3f0fd7f810c7e4f7e5",
//     measurementId: "G-QBC4KFYX42"
// });
// // Retrieve an instance of Firebase Messaging so that it can handle background
// // messages.
// const messaging = firebase.messaging();
// // IDs of divs that display registration token UI or request permission UI.
// const tokenDivId = 'token_div';
// const permissionDivId = 'permission_div';

// // [START receive_message]
// // Handle incoming messages. Called when:
// // - a message is received while the app has focus
// // - the user clicks on an app notification created by a service worker
// //   `messaging.setBackgroundMessageHandler` handler.
// messaging.onMessage((payload) => {
//     console.log('Message received. ', payload);
//     // [START_EXCLUDE]
//     // Update the UI to include the received message.
//     appendMessage(payload);
//     // [END_EXCLUDE]
// });
// // [END receive_message]

// function resetUI() {
//     clearMessages();
//     showToken('loading...');
//     // [START get_token]
//     // Get registration token. Initially this makes a network call, once retrieved
//     // subsequent calls to getToken will return from cache.
//     messaging.getToken({ vapidKey: 'BMk5wlvBQEvChiTZkVw59uy-45EUAYo_MG4d-yQ7rf_xncyDxFHtP7AosN-sKlhcY0GNFAeFEnn0uaNA4lmPkZ4' }).then((currentToken) => {
//         if (currentToken) {
//             sendTokenToServer(currentToken);
//             updateUIForPushEnabled(currentToken);
//         } else {
//             // Show permission request.
//             console.log('No registration token available. Request permission to generate one.');
//             // Show permission UI.
//             updateUIForPushPermissionRequired();
//             setTokenSentToServer(false);
//         }
//     }).catch((err) => {
//         console.log('An error occurred while retrieving token. ', err);
//         showToken('Error retrieving registration token. ', err);
//         setTokenSentToServer(false);
//     });
//     // [END get_token]
// }


// function showToken(currentToken) {
//     // Show token in console and UI.
//     const tokenElement = document.querySelector('#token');
//     tokenElement.textContent = currentToken;
// }

// // Send the registration token your application server, so that it can:
// // - send messages back to this app
// // - subscribe/unsubscribe the token from topics
// function sendTokenToServer(currentToken) {
//     if (!isTokenSentToServer()) {
//         console.log('Sending token to server...');
//         // TODO(developer): Send the current token to your server.
//         setTokenSentToServer(true);
//     } else {
//         console.log('Token already sent to server so won\'t send it again ' +
//             'unless it changes');
//     }

// }

// function isTokenSentToServer() {
//     return window.localStorage.getItem('sentToServer') === '1';
// }

// function setTokenSentToServer(sent) {
//     window.localStorage.setItem('sentToServer', sent ? '1' : '0');
// }

// function showHideDiv(divId, show) {
//     const div = document.querySelector('#' + divId);
//     if (show) {
//         div.style = 'display: visible';
//     } else {
//         div.style = 'display: none';
//     }
// }

// function requestPermission() {
//     console.log('Requesting permission...');
//     // [START request_permission]
//     Notification.requestPermission().then((permission) => {
//         if (permission === 'granted') {
//             console.log('Notification permission granted.');
//             // TODO(developer): Retrieve a registration token for use with FCM.
//             // [START_EXCLUDE]
//             // In many cases once an app has been granted notification permission,
//             // it should update its UI reflecting this.
//             resetUI();
//             // [END_EXCLUDE]
//         } else {
//             console.log('Unable to get permission to notify.');
//         }
//     });
//     // [END request_permission]
// }

// function deleteToken() {
//     // Delete registraion token.
//     // [START delete_token]
//     messaging.getToken().then((currentToken) => {
//         messaging.deleteToken(currentToken).then(() => {
//             console.log('Token deleted.');
//             setTokenSentToServer(false);
//             // [START_EXCLUDE]
//             // Once token is deleted update UI.
//             resetUI();
//             // [END_EXCLUDE]
//         }).catch((err) => {
//             console.log('Unable to delete token. ', err);
//         });
//         // [END delete_token]
//     }).catch((err) => {
//         console.log('Error retrieving registration token. ', err);
//         showToken('Error retrieving registration token. ', err);
//     });

// }

// // Add a message to the messages element.
// function appendMessage(payload) {
//     const messagesElement = document.querySelector('#messages');
//     const dataHeaderElement = document.createElement('h5');
//     const dataElement = document.createElement('pre');
//     dataElement.style = 'overflow-x:hidden;';
//     dataHeaderElement.textContent = 'Received message:';
//     dataElement.textContent = JSON.stringify(payload, null, 2);
//     messagesElement.appendChild(dataHeaderElement);
//     messagesElement.appendChild(dataElement);
// }

// // Clear the messages element of all children.
// function clearMessages() {
//     const messagesElement = document.querySelector('#messages');
//     while (messagesElement.hasChildNodes()) {
//         messagesElement.removeChild(messagesElement.lastChild);
//     }
// }

// function updateUIForPushEnabled(currentToken) {
//     showHideDiv(tokenDivId, true);
//     showHideDiv(permissionDivId, false);
//     showToken(currentToken);
// }

// function updateUIForPushPermissionRequired() {
//     showHideDiv(tokenDivId, false);
//     showHideDiv(permissionDivId, true);
// }

// resetUI();