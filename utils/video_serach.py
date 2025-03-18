import requests
import webbrowser
from config.settings import YOUTUBE_API_KEY

def search_youtube_video(query):
    """Searches YouTube for a video related to the query and plays it."""
    search_url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "q": query,
        "key": YOUTUBE_API_KEY,
        "maxResults": 1,
        "type": "video"
    }
    
    response = requests.get(search_url, params=params)
    if response.status_code == 200:
        results = response.json().get("items", [])
        if results:
            video_id = results[0]["id"]["videoId"]
            video_url = f"https://www.youtube.com/watch?v={video_id}"
            print(f"Playing video: {video_url}")
            webbrowser.open(video_url)  # Open video in web browser
        else:
            print("No video found for this query.")
    else:
        print("YouTube API request failed.")