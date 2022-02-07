$('.edit-product-button').on('click', function() {
    count = 0;
    var csrf = $(this).closest('.product-details-container').find('input[name="csrfmiddlewaretoken"]').attr("value");
    var productId = $(this).closest('.modal').attr('aria-labelledby').replace('Product Modal ','');
    var productName = $(this).closest('.product-details-container').find('.product-name-secondary');
    var productPrice = $(this).closest('.product-details-container').find('.product-price');
    var productInventoryField = $(this).closest('.product-details-container').find('.product-inventory');
    if (productInventoryField.text() == "We're sorry, this product is currently unavailable for order.") {
        var productInventory = 0;
    } else {
        var productInventory = productInventoryField.text().replace('Pieces Available: ', '');
    }
    var productCategories = $('.products-menu-large');
    var productCategory = $(this).closest('.product-details-container').find('.product-category-name').text();
    var productDescription = $(this).closest('.product-details-container').find('.product-description');
    var productContainer = $(this).closest('.product-details-container');
    productContainer.empty();
    $('<form method="POST" action="/products/edit/'+ productId +'/" enctype="multipart/form-data"><input type="hidden" name="csrfmiddlewaretoken" value="' + csrf + '"><div class="wrapper"><input type="text" id="id_name" name="product-name" class="mb-0 form-control product-name-secondary edit-product-field" value="'+ productName.text() +'" required><div class="validation">*</div></div><div class="wrapper"><input id="id_price" type="number" step="0.01" name="price" class="mb-0 form-control product-price edit-product-field" value="'+ parseInt(productPrice.text().replace('$', '')) +'" required><div class="validation">*</div></div><div class="wrapper"><select id="id_category" name="category" class="form-control dropdown edit-product-field category-edit-product-field"></select></div><div class="wrapper"><input type="number" name="inventory" min="0" class="form-control edit-product-field" value="'+ productInventory +'" id="id_inventory" required><div class="validation"></div></div><div class="wrapper"><textarea id="id_description" cols="40" rows="4" name="product-description" class="mb-0 form-control product-description edit-product-field" required>'+productDescription.text()+'</textarea><div class="validation">*</div></div><button type="button" class="btn btn-secondary edit-products-button cancel-edit-product">Cancel</button><button class="btn btn-primary edit-products-button" type="submit">Save Changes</button></form>').appendTo(productContainer);
    categoryEditProductField = productContainer.find('.category-edit-product-field');
    productCategories.children('li').each(function() {
        if ($(this).children('a').text() == 'Add Product') {
            //pass
        } else if ($(this).children('a').text() == 'View All Products') {
            //pass
        } else if ($(this).children('a').text() == productCategory) {
            count = count + 1;
            $('<option value="'+ count +'" selected>' + $(this).children('a').text() + '</option>').appendTo(categoryEditProductField);
        } else {
            count = count + 1;
            $('<option value="'+ count +'">' + $(this).children('a').text() + '</option>').appendTo(categoryEditProductField);
        }
    });
    $('.cancel-edit-product').on('click', function() {
        location.reload(true);
    });
});