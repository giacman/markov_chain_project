##
# Method to Fetch Jarvis Cocker lyrics from musixmatch API
##
# -*- coding: utf-8 -*-

import requests

apikey = "7261173ce8778dc4d9ae6de378b5dfb9"

# Getting the artist_id from band name search
url_artist = "http://api.musixmatch.com/ws/1.1/artist.search"
payload_artist = {'q_artist': 'pulp', 'apikey': apikey}
response_artist = requests.get(url_artist, params=payload_artist)
response_artist = response_artist.json()
artist_id = response_artist['message']['body']['artist_list'][0]['artist']['artist_id']


# Getting all track_ids available for the artist
tracks = []
url_tracks = "http://api.musixmatch.com/ws/1.1/track.search?"

for page in range(1, 15):
    payload_tracks = {'f_artist_id': artist_id,'page_size': 100, 'page': 3, 'f_has_lyrics': 1, 'apikey': apikey}
    response_tracks = requests.get(url_tracks, params=payload_tracks)
    response_tracks = response_tracks.json()
    for item in response_tracks['message']['body']['track_list']:
        for i in item:
            track_id = item[i]["track_id"]
            tracks.append(track_id)
    print page
    print len(tracks)

# Getting lyrics from track_ids
data = []
url_lyrics = "http://api.musixmatch.com/ws/1.1/track.lyrics.get?"
for track_id in tracks:
    payload_lyrics = {'track_id' : int(track_id), 'apikey': apikey}
    response_lyric = requests.get(url_lyrics, params=payload_lyrics)
    response_lyric = response_lyric.json()
    response_lyric = response_lyric['message']['body']['lyrics']
    lyric_text = response_lyric['lyrics_body']
    # Cleaning the Data
    bad_string = '''******* This Lyrics is NOT for Commercial use *******'''
    lyric_text = lyric_text.replace(bad_string, '')
    another_bad_string = '''...'''
    lyric_text = lyric_text.replace(another_bad_string, '')
    data.append(lyric_text)

print 'Saved a total of %s tracks' % len(tracks)

# Save data in a file
string = ''
for lyric in data:
    string += lyric.encode('ascii', 'ignore')

# Open a file
f = open("lyrics.txt", "wb")

f.write(string)

# Close opend file
f.close()


# main problem is that songs returned by this API are truncated.
# I will try to train the model with this data and see results, but I will have to find a better solution moving forwad.
