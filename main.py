import SpotifyID

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
import string

scope = 'playlist-modify-public'
username = 'deangullberry42'

token = SpotifyOAuth(scope=scope, username=username)
spotifyObject = spotipy.Spotify(auth_manager=token)


playlist_name = "PizzaPlace"
playlist_description = "Test"

spotifyObject.user_playlist_create(user=username, name=playlist_name, description=playlist_description)
''''

list_of_songs = []
list_of_uris = []

for i in list_of_songs:
    result = spotifyObject.search(q=i)
    list_of_uris.append(result['tracks']['items'][0]['uri'])
'''
#Find newest playlist
playlists = spotifyObject.user_playlists(user=username)
recent_playlist = playlists['items'][0]['id']


#Add songs to playlist
#spotifyObject.user_playlist_add_tracks(user=username, playlist_id=recent_playlist, tracks=list_of_uris)


def phrase_to_playlist():
    phrase = "Hello pizza place I'd like one pizza please give me your weakest delivery boy I won't settle for less We've got a score to settle."#"hello pizza place I would like some chicken alfredo."
    list_of_words = phrase.split(" ")

    MAX_SONG_LENGTH = 6
    missed_songs = []
    count = 0

    while count < len(list_of_words):
        if count+MAX_SONG_LENGTH > len(list_of_words):
            MAX_SONG_LENGTH = len(list_of_words) - count

        song_added = False
        for i in range(0,MAX_SONG_LENGTH):
            title = (' '.join(str(list_of_words[count+j]) for j in range(MAX_SONG_LENGTH-i)))
            print(title)
            result = spotifyObject.search(q=title)

            if len(result['tracks']['items']) != 0:
                for a in range(len(result['tracks']['items'])):
                    print('test against the song:'+ result['tracks']['items'][a]['name'])
                    if result['tracks']['items'][a]['name'].lower().translate(str.maketrans('', '', string.punctuation)) == title.lower().translate(str.maketrans('', '', string.punctuation)):
                        print("added "+title+" to playlist")
                        spotifyObject.user_playlist_add_tracks(user=username, playlist_id=recent_playlist, tracks=[result['tracks']['items'][a]['uri']])
                        count += MAX_SONG_LENGTH - i
                        song_added = True
                        break
                if song_added:
                    break
        
        if not song_added:    
            missed_songs.append(list_of_words[count])
            count += 1

    return missed_songs

print(phrase_to_playlist())
#result = spotifyObject.search(q="pizza place")
#print(len(result['tracks']['items']))