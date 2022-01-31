function refreshPage() {
    location.reload(true);
};


$('.delete-product-button').on('click', function() {
    var productId = $(this).closest('.modal').attr('aria-labelledby').replace('Delete Product Modal ','');
    $.ajax({
        type: "GET",
        url: "/products/delete/"+ productId +"/",
        contentType: "application/javascript",
        dataType: "json",
        complete: function() {
            refreshPage();
        },
    });
});