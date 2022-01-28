$('.product-item').on("click", function() {

    /**
   * Product Carousel Indicators
   */
   let productCarouselIndicators = $(this).children("#product-carousel-indicators");
   let productCarouselItems = $(this).children('.carousel-item');

   for (i in productCarouselItems) {
    if (i === 0) {
      productCarouselIndicators.html("<li data-bs-target='#productCarousel' data-bs-slide-to='" + i + "' class='active'></li>");
    } else {
      productCarouselIndicators.html("<li data-bs-target='#productCarousel' data-bs-slide-to='" + i + "'></li>");
    }
  };
});