from json import load
import os
import requests
from dotenv import load_dotenv
load_dotenv()
spotify_create_playlist_url=os.environ.get("SPOTIFY_CREATE_PLAYLIST_URL") 
access_token=os.environ.get("ACCESS_TOKEN")


def create_playlist_on_spotify(name, description, public):
    """Create a playlist for the user"""
    headers = {
        "Authorization": "Bearer " + access_token
    }
    data = {
        "name": name,
        "description": description,
        "public": public
    }
    response = requests.post(spotify_create_playlist_url.format(user_id="123456789"), json=data, headers=headers)
    response_json = response.json()
    return response_json["id"]

def main():
    playlist= create_playlist_on_spotify(name="My private Playlist",public = False, description="My private playlist description")
    print(playlist)

if __name__ == "__main__":
    main()    
