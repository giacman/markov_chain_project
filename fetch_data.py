##
# Method to Fetch Jarvis Cocker lyrics from musixmatch API
##
# -*- coding: utf-8 -*-

import requests
import json
import pprint

apikey = "7261173ce8778dc4d9ae6de378b5dfb9"

# Get the artist_id searching for 'pulp' 
url = "http://api.musixmatch.com/ws/1.1/artist.search"
payload = {'q_artist' : 'pulp', 'page_size' : '5', 'apikey' : apikey}
r = requests.get(url, params = payload)
response_artist = r.json()
#print pprint.pprint(response_artist['message']['body']['artist_list'][0]['artist']['artist_id'])
artist_id = response_artist['message']['body']['artist_list'][0]['artist']['artist_id']

# Using the artist_id to search for tracks
f_artist_id = artist_id
url_1 = "http://api.musixmatch.com/ws/1.1/track.search?"
payload_1 = {'f_artist_id' : f_artist_id , 'apikey' : apikey}
r_1 = requests.get(url_1, params=payload_1)
response_tracks = r_1.json()
print pprint.pprint(response_tracks['message'])
# for message in response_tracks:
# 	print 1
# 	# for i in message:
# 	# 	print message[0]
