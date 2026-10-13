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
song = main_spotify.search(q=request_song, type="track", limit=5)

for i in range(len(song["tracks"]["items"])):
    track = song["tracks"]["items"][i]
    nameart = track["name"]
    artists = track["artists"][0]["name"]
    print(f"{i+1}. name: {nameart}, artist: {artists}")

position = input("What number do you want? ")
position = int(position)-1

if position in range(len(song["tracks"]["items"])):
    selected_song = song["tracks"]["items"][position]
    song_title = selected_song["name"]
    uri_song = selected_song["uri"]
    print(f"song: {song_title}, uri: {uri_song}")

    device_save = main_spotify.devices()
    if len(device_save["devices"]) > 0:
        id_device = device_save["devices"][0]["id"]
        main_spotify.start_playback(device_id=id_device,uris=[uri_song])
    else:
        print("Please reproduce something on your device for 3 seconds")
else:
    print("Number doesn't exist")


    

