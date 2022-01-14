from turtle import home
from django.shortcuts import render
from .models import HomePagePicture

# Create your views here.

def index(request):
    '''A view to return the home page'''

    home_page_pictures = HomePagePicture.objects.values()

    context = {
        'page': 'home',
        'home_page_pictures': home_page_pictures,
    }
    
    return render(request, 'home/index.html', context)