from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Content, Product, Category
from django.db.models import Q
from django.contrib.auth.decorators import login_required

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


@login_required
def delete_product(request, product_id):
    if not request.user.is_superuser:
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    return redirect(reverse('products'))