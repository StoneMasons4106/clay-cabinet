from django.shortcuts import render, redirect, reverse
from .models import Content, Product, Category
from django.db.models import Q

# Create your views here.

def all_products(request):

    content = Content.objects.values()[0]
    products = Product.objects.all()
    categories = Category.objects.values()
    query = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'query' in request.GET:
            query = request.GET['query']
            if not query:
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'page': 'products',
        'content': content,
        'products': products,
        'current_categories': categories,
        'search_term': query,
    }

    return render(request, 'products/products.html', context)