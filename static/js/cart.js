// Update quantity on click
$('.update-link').click(function(e) {
    var form = $(this).prev('.update-form');
    form.submit();
})

// Remove item and reload on click
$('.remove-item').click(function(e) {
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').attr("value");
    var itemId = $(this).attr('id').split('remove_')[1];
    var url = `/cart/remove/${itemId}/`;
    var data = {'csrfmiddlewaretoken': csrfToken};

    $.post(url, data)
     .done(function() {
         location.reload();
    });
})

$('.btt-link').click(function(e) {
    window.scrollTo(0,0)
})