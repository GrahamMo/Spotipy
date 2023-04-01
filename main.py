import SpotifyID

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
import re
import string

scope = 'playlist-modify-public'
username = 'deangullberry42'

token = SpotifyOAuth(scope=scope, username=username)
spotifyObject = spotipy.Spotify(auth_manager=token)


playlist_name = "The Entire Bee Movie Script"
playlist_description = "Test"

#spotifyObject.user_playlist_create(user=username, name=playlist_name, description=playlist_description)
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
#so aevery when we hanging out?

def phrase_to_playlist():
    phrase = """initial that.
Thank you.
OK.
You got a rain advisory today, and as you all know, bees cannot fly in rain.
So be careful. As always, watch your brooms, hockey sticks, dogs, birds, bears and bats.
Also, I got a couple of reports of root beer being poured on us.
Murphy's in a home because of it, babbling like a cicada!
That's awful.
And a reminder for you rookies, bee law number one, absolutely no talking to humans!
 All right, launch positions!
Buzz, buzz, buzz, buzz! Buzz, buzz, buzz, buzz! Buzz, buzz, buzz, buzz!
Black and yellow!
Hello!
You ready for this, hot shot?
Yeah. Yeah, bring it on.
Wind, check.
Antennae, check.
Nectar pack, check.
Wings, check.
Stinger, check.
Scared out of my shorts, check.
OK, ladies,
let's move it out!
Pound those petunias, you striped stem-suckers!
All of you, drain those flowers!
Wow! I'm out!
I can't believe I'm out!
So blue.
I feel so fast and free!
Box kite!
Wow!
Flowers!
This is Blue Leader, We have roses visual.
Bring it around 30 degrees and hold.
Roses!
30 degrees, roger. Bringing it around.
Stand to the side, kid.
It's got a bit of a kick.
That is one nectar collector!
Ever see pollination up close?
No, sir."""
    #NO SIR
    phrase = phrase.replace("-", " ")
    #phrase = phrase.replace("'re", " are")
    #phrase = phrase.replace("'ll", " will")
    list_of_words = re.split(",| |\n", phrase.translate(str.maketrans('', '', string.punctuation)))
    print(list_of_words)

    MAX_SONG_LENGTH = 6
    MAX_ITEMS_SEARCHED = 150
    PAGE_LIMIT = 50
    missed_songs = []
    count = 0
    current_playlist_length = 161
    song_number = 1 + current_playlist_length

    while count < len(list_of_words):
        song_added = False
    
        if count+MAX_SONG_LENGTH > len(list_of_words):
            MAX_SONG_LENGTH = len(list_of_words) - count

        for i in range(0,MAX_SONG_LENGTH):
            items_searched = 0
            while items_searched <= MAX_ITEMS_SEARCHED:    
                title = (' '.join(str(list_of_words[count+j]) for j in range(MAX_SONG_LENGTH-i)))
                print(title)
                result = spotifyObject.search(q=title, offset=items_searched, limit=PAGE_LIMIT)

                if len(result['tracks']['items']) != 0:
                    for a in range(len(result['tracks']['items'])):
                        print('test against the song:'+ result['tracks']['items'][a]['name'])
                        if result['tracks']['items'][a]['name'].lower().translate(str.maketrans('', '', string.punctuation)) == title.lower().translate(str.maketrans('', '', string.punctuation)):
                            print("-----------------added "+title+" to playlist-----------------------------------------")
                            spotifyObject.user_playlist_add_tracks(user=username, playlist_id=recent_playlist, tracks=[result['tracks']['items'][a]['uri']])
                            count += MAX_SONG_LENGTH - i
                            song_number += 1
                            song_added = True
                            break
                    if song_added:
                        break
                else:
                    break

                items_searched += PAGE_LIMIT
                print(items_searched)  
                
            if song_added:
                break
        if not song_added:
            print('################################# MISSING SONG #########################################')
            print(list_of_words[count])
            input("Make an input to continue:")
            count += 1

        '''
        if not song_added:    
            missed_songs.append([list_of_words[count], song_number])
            count += 1
        '''
    return missed_songs

print(phrase_to_playlist())
#result = spotifyObject.search(q="pizza place")
#print(len(result['tracks']['items']))