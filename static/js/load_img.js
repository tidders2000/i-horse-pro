$("#post-form").submit(function (event) {
    event.preventDefault();

    var formData = new FormData($('#post-form')[0]);
    formData.append('csrfmiddlewaretoken', $.cookie("csrftoken"));

    var progress_bar = new ldBar("#progressBar");

    $.ajax({
        // xhr method is for Progress bar
        xhr: function () {
            var xhr = new window.XMLHttpRequest();
            xhr.upload.addEventListener("progress", function (evt) {
                var percent = Math.round(evt.loaded / evt.total * 100)
                if (percent < 100) {
                    progress_bar.set(Math.round(percent));
                } else {
                    document.getElementById("progressBar").innerHTML = "<i>loading...</i>";
                }
            });
            return xhr;
        },
        url: POST_URL,
        headers: {
            'Conten-Type': 'application/json',
            'X-CSRFToken': $.cookie("csrftoken")
        },
        type: "POST",
        data: formData,
        cache: false,
        processData: false,
        contentType: false,
        beforeSend: function () {
            $('#formSubmitBTN').prop('disabled', true);
            $('.uploading').css("display", "block");
            console.log('saving...')
        },
        success: function (data) {
            console.log('success', data);
        },
        error: function (rs, e) {
            $("#error").html(rs.responseText);
            $("#error").css('display', 'block');
            console.error(rs.status);
        },
        complete: function () {
            $('#formSubmitBTN').prop('disabled', false);
            $('.uploading').css("display", "none");
            $('.upload-successfully').css("display", "block");
            console.log('request completed')
        }
    }); // end ajax
});