import requests
import os

def get_videos():
    key = os.environ.get("YOUTUBE_FEED_API_KEY")
    channel = os.environ.get("YOUTUBE_CHANNEL_ID")
    url = f'https://youtube.googleapis.com/youtube/v3/search?part=snippet&channelId={channel}&order=date&key={key}'
    response = requests.get(url)
    return response.json()
