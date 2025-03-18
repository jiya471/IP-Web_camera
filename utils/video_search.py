



import requests
import webbrowser

def search_youtube_video(query, api_key):
    """Searches YouTube for a video related to the query and plays it."""
    search_url = "https://youtube138.p.rapidapi.com/search/"
    headers = {
        "X-RapidAPI-Key": "8fd3d69fbdmsh91400bc8e41583ap1fbfcajsnaaf910b35543",
        "X-RapidAPI-Host": "youtube138.p.rapidapi.com"
    }
    params = {"q": query, "hl": "en", "gl": "US"}

    response = requests.get(search_url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        if "contents" in data:
            for content in data["contents"]:
                if "video" in content and "videoId" in content["video"]:
                    video_id = content["video"]["videoId"]
                    video_url = f"https://www.youtube.com/watch?v={video_id}"
                    print(f"Playing video: {video_url}")
                    webbrowser.open(video_url)
                    return
            print("No video found for this query.")
        else:
            print("No video found for this query.")
    else:
        print("YouTube API request failed. Please check your API key and request limits.")