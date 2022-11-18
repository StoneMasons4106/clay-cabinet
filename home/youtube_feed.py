import requests
import os
from .models import Content
from django.shortcuts import get_object_or_404

def get_videos():
    key = os.environ.get("YOUTUBE_FEED_API_KEY")
    channel = os.environ.get("YOUTUBE_CHANNEL_ID")
    url = f'https://youtube.googleapis.com/youtube/v3/search?part=snippet&channelId={channel}&maxResults=4&order=date&key={key}'
    response = requests.get(url).json()

    return response
