from dotenv import load_dotenv
import os
from spotipy.oauth2 import SpotifyOAuth
import spotipy

load_dotenv()
IDprint = os.getenv("CLIENTID")
SecretPrint = os.getenv("CLIENTSECRET")
URLink = os.getenv("URLREDIRECT")
if IDprint is not None:
    print("ID Success")
else:
    print("Error on ID")
if SecretPrint is not None:
    print("Client Secret Success")
else:
    print("Error on Client Secret")
if URLink is not None:
    print("URL Success")
else:
    print("Error on URL")

key_values = SpotifyOAuth(
    client_id=IDprint,
    client_secret=SecretPrint,
    redirect_uri=URLink,
    scope="user-read-playback-state user-modify-playback-state"
)

main_spotify=spotipy.Spotify(auth_manager=key_values)
infouser = main_spotify.current_user()
print(infouser["display_name"])

request_song = input("What song are you searching for? ")
song = main_spotify.search(q=request_song, type="track", limit=3)


songs = song["artists"]["name"]["tracks"]["items"][0]
print(songs)

