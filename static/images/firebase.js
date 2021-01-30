< script >
    // Your web app's Firebase configuration
    // For Firebase JS SDK v7.20.0 and later, measurementId is optional
    var firebaseConfig = {
        apiKey: "AIzaSyD4p8Ud9SI8Cv_u1qxpyH7v7nP0K0S5rPU",
        authDomain: "ihorse-8e7f4.firebaseapp.com",
        projectId: "ihorse-8e7f4",
        storageBucket: "ihorse-8e7f4.appspot.com",
        messagingSenderId: "51294489856",
        appId: "1:51294489856:web:021c3f0fd7f810c7e4f7e5",
        measurementId: "G-QBC4KFYX42",
    };
// Initialize Firebase
firebase.initializeApp(firebaseConfig);
firebase.analytics(); <
/script>

<
script >
    const messaging = firebase.messaging();

function resetUI() {
    console.log("loading...");

    messaging
        .getToken({
            vapidKey: "BMk5wlvBQEvChiTZkVw59uy-45EUAYo_MG4d-yQ7rf_xncyDxFHtP7AosN-sKlhcY0GNFAeFEnn0uaNA4lmPkZ4",
        })
        .then((currentToken) => {
            if (currentToken) {
                console.log(currentToken); //save token and check for duplicates
            } else {
                // Show permission request.
                console.log(
                    "No registration token available. Request permission to generate one."
                );
                // Show permission UI.
            }
        })
        .catch((err) => {
            console.log("An error occurred while retrieving token. ", err);
        });
    // [END get_token]
}

function requestPermission() {
    console.log("Requesting permission...");
    // [START request_permission]
    Notification.requestPermission().then((permission) => {
        if (permission === "granted") {
            console.log("Notification permission granted.");
            // TODO(developer): Retrieve a registration token for use with FCM.
            // [START_EXCLUDE]
            // In many cases once an app has been granted notification permission,
            // it should update its UI reflecting this.
            resetUI();
            // [END_EXCLUDE]
        } else {
            console.log("Unable to get permission to notify.");
        }
    });
    // [END request_permission]
}
resetUI(); <
/script>