$('#apply-discount-code').on('click', function() {
    var csrf = $("#payment-form").find('input[name="csrfmiddlewaretoken"]').attr("value");
    $.ajax({
        type: "POST",
        headers: {
            'X-CSRFToken': csrf,
        },
        data: $("form").serializeArray(),
        url: "/checkout/verify_discount_codes",
        contentType: "application/javascript",
        dataType: "json",
        success: function(response) {
            if (response.discount == 'False') {
                //pass
            } else {
                var grandTotal = $(".checkout-container").find("p#grand-total");
                var grandTotalLabel = $(".checkout-container").find("p#grand-total-label");
                grandTotalLabel.before('<p class="my-0">Discount:</p>');
                grandTotal.before('<p class="my-0">-' + response.percent_off + '%</p>');
                grandTotalFloat = parseFloat(grandTotal.text().replace('$', ''));
                newGrandTotal = ((1 - (response.percent_off / 100)) * grandTotalFloat).toFixed(2);
                grandTotal.text('$' + String(newGrandTotal));
                $("strong#card-charged").text('$' + String(newGrandTotal));
            }
        },
    });
});