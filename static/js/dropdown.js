function dropdown(el) {
    $(el).toggleClass("visible");
};

$(".dropdown").on("click", function() {
    dropdown($(this).children('ul'));
});