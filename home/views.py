from django.shortcuts import render, get_object_or_404
from .models import HomePagePicture, Testimonial, Content
import ast
from .youtube_feed import get_videos

# Create your views here.

def index(request):
    '''A view to return the home page'''

    home_page_pictures = HomePagePicture.objects.values()
    testimonials = Testimonial.objects.values()
    content = get_object_or_404(Content, name="Homepage Content")

    youtube_videos = ast.literal_eval(content.video_content)

    context = {
        'page': 'home',
        'home_page_pictures': home_page_pictures,
        'youtube_feed': youtube_videos,
        'testimonials': testimonials,
        'content': content,
    }

    return render(request, 'home/index.html', context)


def privacy_policy(request):
    '''A view to return the privacy policy page'''

    content = get_object_or_404(Content, name="Homepage Content")

    context = {
        'page': 'home',
        'content': content,
    }

    return render(request, 'home/privacypolicy.html', context)