$('.product-item').on("click", function() {
  
   var productCarouselIndicatorsValue = $(this).children(".fancybox").attr('data-bs-target').replace('#','');
   var productCarouselIndicators = $("#" + productCarouselIndicatorsValue).find('#product-carousel-indicators');
   var productCarouselItems = $("#" + productCarouselIndicatorsValue).find('.carousel-item');

   for (i in productCarouselItems) {
      if (i == 0) {
        $("<li data-bs-target='#productCarousel' data-bs-slide-to='" + i + "' class='active'></li>").appendTo(productCarouselIndicators);
      } else if (parseInt(i)) {
        $("<li data-bs-target='#productCarousel' data-bs-slide-to='" + i + "'></li>").appendTo(productCarouselIndicators);
      } else {
      //pass
    };
  };
});