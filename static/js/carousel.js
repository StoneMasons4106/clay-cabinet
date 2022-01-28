$('.product-item').on("click", function() {
    let productCarouselIndicatorsValue = $(this).children('#product').attr('data-bs-target');
    let productCarouselIndicators = $(productCarouselIndicatorsValue).children('#product-carousel-indicators');
    let productCarouselItems = $(productCarouselIndicatorsValue).children('.carousel-item');
    
    for (index in productCarouselItems) {
        productCarouselIndicators.html("<li data-bs-target='#productCarousel' data-bs-slide-to='" + index + "' class='active'></li>");
        productCarouselIndicators.html("<li data-bs-target='#productCarousel' data-bs-slide-to='" + index + "'></li>");
    };
});