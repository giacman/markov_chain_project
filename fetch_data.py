##
# Method to Fetch Jarvis Cocker lyrics from musixmatch API
##
# -*- coding: utf-8 -*-

import requests
import json
import pprint

apikey = "7261173ce8778dc4d9ae6de378b5dfb9"

# Getting the artist_id from band name search 
url = "http://api.musixmatch.com/ws/1.1/artist.search"
payload = {'q_artist' : 'pulp', 'page_size' : '5', 'apikey' : apikey}
# need to implement a loop up to catch IndexError: list index out of range at 'page': 11
r = requests.get(url, params = payload)
response_artist = r.json()
artist_id = response_artist['message']['body']['artist_list'][0]['artist']['artist_id']

# Getting track_ids from artist_id
tracks = []
f_artist_id = artist_id
url_1 = "http://api.musixmatch.com/ws/1.1/track.search?"
payload_1 = {'f_artist_id' : f_artist_id , 'apikey' : apikey}
r_1 = requests.get(url_1, params=payload_1)
response_tracks = r_1.json()

for item in response_tracks['message']['body']['track_list']:
 	for i in item:
 		track_id = item[i]["track_id"]
 		tracks.append(track_id)

#print tracks

# Getting lytics from track_ids

url_2 = "http://api.musixmatch.com/ws/1.1/track.lyrics.get?"
for track_id in tracks:
	data = []
	payload_2 = {'track_id' : int(track_id) , 'apikey' : apikey}
	r_2 = requests.get(url_2, params=payload_2)
	response_lyric = r_2.json()
	print response_lyric['message']['header']["status_code"]
	if response_lyric['message']['header']["status_code"] == 200:
		response_lyric = response_lyric['message']['body']['lyrics']
		lyric_text = response_lyric['lyrics_body']
		data.append(lyric_text)
		#print lyric_text

print data

#[9611472, 2206785, 13980697, 1948865, 1745355, 47891068, 17486978, 1646148, 33211787, 17898713]


