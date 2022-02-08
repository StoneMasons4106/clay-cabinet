$(".fa-eye-slash").on("click", function () {
    if ($("#id_password").get(0).type == "password") {
        $("#id_password").get(0).type = "text";
        $(this).removeClass("fa-eye-slash");
        $(this).addClass("fa-eye");
    } else {
        $("#id_password").get(0).type = "password";
        $(this).removeClass("fa-eye");
        $(this).addClass("fa-eye-slash");
    }
});