$("#login-form").on("submit", function (e) {
    e.preventDefault();
    var username = $("#email").val();
    var password = $("#pwd").val();

    $.ajax({
        url: 'functions.php',
        type: 'POST',
        data: {
            username: username,
            password: password,
            function: "login"
        },
        dataType: 'json',
        success: function (data) {
            if (data.status == "success") {
                if (data.auth_type == 0) {
                    window.location = 'dashboard.php';
                } else {
                    window.location = 'dashboard.php';
                }
            } else {
                // 🚨 VULNERABILITY HERE! 🚨
                // 'data.message' tells us EXACTLY what went wrong (e.g. "User not found" vs "Wrong password").
                // This lets hackers know if an email exists without knowing the password! 🕵️‍♂️
                $("#messagess").html('<p class="errr">' + data.message + '</p>');
            }
        }
    });
});