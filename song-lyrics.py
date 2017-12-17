# just gets lyrics from Musicmatch api

import sys
from musixmatch import Musixmatch

API_KEY = sys.argv[1]

musixmatch = Musixmatch(API_KEY)

with open("songs.txt") as f:
    songs = f.readlines()
    songs = [x.strip() for x in songs]
	
for song in songs:

    data = song.split("–")
    title =  data[0]
    artist = data[1]
        
    r = musixmatch.matcher_lyrics_get(title,artist)
    
    if r["message"]["body"] == []:
        print ("***missing***")
    else:
        print(r["message"]["body"]["lyrics"]["lyrics_body"])
