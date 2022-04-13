from django.shortcuts import render
from .models import HomePagePicture, Testimonial, Content
from .youtube_feed import get_videos
import os

# Create your views here.

def index(request):
    '''A view to return the home page'''

    home_page_pictures = HomePagePicture.objects.values()
    testimonials = Testimonial.objects.values()
    content = Content.objects.values()[0]

    youtube_videos = get_videos()

    context = {
        'page': 'home',
        'home_page_pictures': home_page_pictures,
        'youtube_feed': youtube_videos,
        'testimonials': testimonials,
        'content': content,
    }

    return render(request, 'home/index.html', context)