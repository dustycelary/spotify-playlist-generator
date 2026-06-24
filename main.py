import datetime
import json
import os
import pprint
import random

import dotenv
import spotipy

dotenv.load_dotenv()
CLIENT_ID = os.environ.get("client_id")
CLIENT_SECRET = os.environ.get("client_secret")
REDIRECT_URI = os.environ.get("redirect_uri")
spotify_authorisation = spotipy.oauth2.SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope="user-library-read user-library-modify playlist-read-private playlist-read-collaborative playlist-modify-public",
)
sp = spotipy.Spotify(auth_manager=spotify_authorisation)

with open("band_info.json") as file:
    playlist_dictionary = json.load(file)


all_ids = []
for i in playlist_dictionary.keys():
    print(f"this has been accepted : {i}")
    playlist_sugar = playlist_dictionary[i]
    pprint.pprint(f"Playlist sugar: {playlist_sugar}")
    playlist_all_info = sp.playlist_tracks(
        playlist_id=playlist_sugar, fields="items(track(album,id,name))"
    )
    # with open("test.json", "a") as file:
    #     json.dump(playlist_all_info, file, indent=2)

    for item_index in range(len(playlist_all_info["items"])):
        all_ids.append(playlist_all_info["items"][item_index]["track"]["id"])

# sys.exit()


playlist_ids = []
for i in range(40):
    current_track = random.choice(all_ids)
    all_ids.remove(current_track)
    playlist_ids.append(current_track)


today_date_element = datetime.datetime.now()
today_date = today_date_element.strftime("%d/%m/%Y  %H-%M")

playlist_information = sp.user_playlist_create(
    user="fergussharp2", name=f"{today_date}"
)
adding_items = sp.playlist_add_items(
    items=playlist_ids, playlist_id=playlist_information["id"]
)
