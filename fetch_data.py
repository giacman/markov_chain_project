##
# Method to Fetch Jarvis Cocker lyrics from musixmatch API
##
# -*- coding: utf-8 -*-

import requests
import json
import pprint

apikey = "7261173ce8778dc4d9ae6de378b5dfb9"

# Getting the artist_id from band name search 
url_artist = "http://api.musixmatch.com/ws/1.1/artist.search"
payload_artist = {'q_artist' : 'pulp', 'apikey' : apikey}
response_artist = requests.get(url_artist, params = payload_artist)
response_artist = response_artist.json()
artist_id = response_artist['message']['body']['artist_list'][0]['artist']['artist_id']
print artist_id

# Getting track_ids from artist_id

# need to implement a loop up to catch IndexError: list index out of range at 'page': 11
tracks = []
url_tracks = "http://api.musixmatch.com/ws/1.1/track.search?"
payload_tracks = {'f_artist_id' : artist_id , 'apikey' : apikey}
response_tracks = requests.get(url_tracks, params=payload_tracks)
response_tracks = response_tracks.json()

for item in response_tracks['message']['body']['track_list']:
 	for i in item:
 		track_id = item[i]["track_id"]
 		tracks.append(track_id)


# Getting lyrics from track_ids

url_lyrics = "http://api.musixmatch.com/ws/1.1/track.lyrics.get?"
for track_id in tracks:
	data = []
	payload_lyrics = {'track_id' : int(track_id) , 'apikey' : apikey}
	response_lyric = requests.get(url_lyrics, params=payload_lyrics)
	response_lyric = response_lyric.json()
	print response_lyric['message']['header']["status_code"]
	if response_lyric['message']['header']["status_code"] == 200:
		response_lyric = response_lyric['message']['body']['lyrics']
		lyric_text = response_lyric['lyrics_body']
		data.append(lyric_text)
		#print lyric_text

print data

# two issues: if workign only at the end ot the loop
# most of the calls return 404
#[9611472, 2206785, 13980697, 1948865, 1745355, 47891068, 17486978, 1646148, 33211787, 17898713]


