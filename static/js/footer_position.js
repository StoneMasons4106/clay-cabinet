function footerPosition() {
    var windowHeight = $(window).height();
    var documentHeight = $(document).height();
    var headerMainHeight = $('.navbar').height() + $('#main').height();
    var difference = (documentHeight - 136) - headerMainHeight;
    var sectionPaddingBottom = difference + 112;
        
    if (documentHeight == windowHeight) {
        $("#footer").css({'position': 'fixed', 'bottom': '0px', 'width': '100%'});
        $('section').css({'padding-bottom': sectionPaddingBottom + 'px' });
    } else {
        $("#footer").css({'position': '', 'bottom': '', 'width': ''});
        $('section').css({'padding-bottom': ''});
    }
}

$(document).ready(function() {
    footerPosition();
})

$(window).resize(function() {
    footerPosition();
})