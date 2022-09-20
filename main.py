import SpotifyID

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

scope = 'playlist-modify-public'
username = 'deangullberry42'

token = SpotifyOAuth(scope=scope, username=username)
spotifyObject = spotipy.Spotify(auth_manager=token)

playlist_name = "AngryBirds"
playlist_description = "Test"

spotifyObject.user_playlist_create(user=username, name=playlist_name, description=playlist_description)


list_of_songs = []
list_of_uris = []

for i in list_of_songs:
    result = spotifyObject.search(q=i)
    list_of_uris.append(result['tracks']['items'][0]['uri'])

#Find newest playlist
playlists = spotifyObject.user_playlists(user=username)
recent_playlist = playlists['items'][0]['id']

#Add songs to playlist
spotifyObject.user_playlist_add_tracks(user=username, playlist_id=recent_playlist, tracks=list_of_uris)