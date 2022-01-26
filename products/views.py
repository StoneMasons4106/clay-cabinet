from django.shortcuts import render
from .models import Content

# Create your views here.

def all_products(request):

    content = Content.objects.values()[0]

    context = {
        'page': 'products',
        'content': content,
    }

    return render(request, 'products/products.html', context)