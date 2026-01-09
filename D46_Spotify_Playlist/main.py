import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

from D19_high_order_function_and_turtle_race.high_order_function.hof import result

URL='https://www.billboard.com/charts/hot-100/'
HEADER={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
REDIRECT_URI="http://example.com"
CLIENT_ID="client_id"
CLIENT_SECRET="client_secret"

time = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
print(time)
music_res=requests.get(f'{URL}{time}',headers=HEADER)
# SCRAPING BILLBOARD TOP 100 CHARTS WITH BEAUTIFUL SOUP
music_soup=BeautifulSoup(music_res.text,'html.parser')
song_names_span=music_soup.select("li ul li h3")
# strip: remove the leading and trailing whitespace
song_names=[song.getText().strip() for song in song_names_span]
print(song_names)
# Authenticating Spotify client
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=REDIRECT_URI,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
    )
)
user_id = sp.current_user()["id"]

song_uris=[]
for song in song_names:
    result=sp.search(q=song,type="track")
    if result["tracks"]["items"]:
        song_uri=result["tracks"]["items"][0]["uri"]
        song_uris.append(song_uri)
    else:
        print(f"Song {song} not found on Spotify")

# Creating a new playlist on Spotify
playlist_name = f"Billboard Hot 100 - {time}"
description = "Top 100 songs on Billboard charts for the specified year."

playlist=sp.user_playlist_create(user=user_id, name=playlist_name,description=description,public=True)
# Adding songs to playlist
sp.playlist_add_items(playlist_id=playlist["id"],items=song_uris)
