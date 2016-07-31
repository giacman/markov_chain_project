##
# Method to Fetch Jarvis Cocker lyrics from musixmatch API
##
# -*- coding: utf-8 -*-

import requests
import json
import pprint
import ast

apikey = "7261173ce8778dc4d9ae6de378b5dfb9"

# Getting the artist_id from band name search 
url = "http://api.musixmatch.com/ws/1.1/artist.search"

payload = {'q_artist' : 'pulp', 'page_size' : '5', 'apikey' : apikey}

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

print tracks

