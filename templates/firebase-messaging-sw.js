console.log('firestore sw')



// [START initialize_firebase_in_sw]
// Give the service worker access to Firebase Messaging.
// Note that you can only use Firebase Messaging here. Other Firebase libraries
// are not available in the service worker.
importScripts('https://www.gstatic.com/firebasejs/8.2.1/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/8.2.1/firebase-messaging.js');
// Initialize the Firebase app in the service worker by passing in
// your app's Firebase config object.
// https://firebase.google.com/docs/web/setup#config-object
firebase.initializeApp({
    apiKey: "AIzaSyD4p8Ud9SI8Cv_u1qxpyH7v7nP0K0S5rPU",
    authDomain: "ihorse-8e7f4.firebaseapp.com",
    projectId: "ihorse-8e7f4",
    storageBucket: "ihorse-8e7f4.appspot.com",
    messagingSenderId: "51294489856",
    appId: "1:51294489856:web:021c3f0fd7f810c7e4f7e5",
    measurementId: "G-QBC4KFYX42"
});
// Retrieve an instance of Firebase Messaging so that it can handle background
// messages.
const messaging = firebase.messaging();
//

messaging.onBackgroundMessage(function(payload) {
    console.log('[firebase-messaging-sw.js] Received background message ', payload);
    // Customize notification here
    const notificationTitle = payload.notification.title;
    const notificationOptions = {
        body: payload.notification.body,
        icon: 'mobile_logo.png'
    };

    self.registration.showNotification(notificationTitle,
        notificationOptions);
    console.log(payload)
});