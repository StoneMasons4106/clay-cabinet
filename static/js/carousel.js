$('.product-item').on("click", function() {

    /**
   * Product Carousel Indicators
   */
   let productCarouselIndicatorsValue = $(this).children(".fancybox").attr('data-bs-target');
   let productCarouselIndicators = $(productCarouselIndicatorsValue).children('.carousel-indicators')
   let productCarouselItems = $(productCarouselIndicatorsValue).children('.carousel-item');

   for (i in productCarouselItems) {
    if (i === 0) {
      productCarouselIndicators.html("<li data-bs-target='#productCarousel' data-bs-slide-to='" + i + "' class='active'></li>");
    } else {
      productCarouselIndicators.html("<li data-bs-target='#productCarousel' data-bs-slide-to='" + i + "'></li>");
    }
  };
});