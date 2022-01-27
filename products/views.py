from django.shortcuts import render
from .models import Content, Product, Category

# Create your views here.

def all_products(request):

    content = Content.objects.values()[0]
    products = Product.objects.all()
    categories = Category.objects.values()

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    context = {
        'page': 'products',
        'content': content,
        'products': products,
        'current_categories': categories,
    }

    return render(request, 'products/products.html', context)