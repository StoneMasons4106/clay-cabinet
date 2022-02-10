$(window).scroll(function() {
    if ($(window).scrollTop() == 0) {
        $('.back-to-top').removeClass('d-flex');
    } else {
        $('.back-to-top').addClass('d-flex');
    }
});