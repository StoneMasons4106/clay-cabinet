from turtle import home
from django.shortcuts import render
from django.test import TestCase
from .models import HomePagePicture, Testimonial
from .youtube_feed import get_videos

# Create your views here.

def index(request):
    '''A view to return the home page'''

    home_page_pictures = HomePagePicture.objects.values()
    testimonials = Testimonial.objects.values()

    youtube_videos = get_videos()

    context = {
        'page': 'home',
        'home_page_pictures': home_page_pictures,
        'youtube_feed': youtube_videos,
        'testimonials': testimonials,
    }

    return render(request, 'home/index.html', context)