import os
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import pprint

load_dotenv()

URL = 'https://www.billboard.com/charts/hot-100'

date = input('Which year would youl like to travel to? Type date in this format YYYY-MM-DD \n>')

###########Getting songs titles... ##############

response = requests.get(f'{URL}/{date}')

soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
pprint.pp(song_names)

######## Spotify Authenticationn ###############
# print(os.getenv('SPORTIFY_CLIENT_ID'), os.getenv('SPORTIFY_SECRET_KEY'))
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=os.getenv('SPORTIFY_CLIENT_ID'),
        client_secret=os.getenv('SPORTIFY_SECRET_KEY'),
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
#print(user_id)


######## Searching sportify for songs by title.. ########

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    pprint.pp(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

###### Creating new private playlist in spotify.. ###

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

# Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

