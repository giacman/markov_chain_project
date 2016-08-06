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

# Getting all track_ids avilable for the artist_id
tracks = []
url_tracks = "http://api.musixmatch.com/ws/1.1/track.search?"
for page in range(1,3):
	payload_tracks = {'f_artist_id' : artist_id ,'page_size' : 100, 'page' : 1, 'apikey' : apikey}
	response_tracks = requests.get(url_tracks, params=payload_tracks)
	response_tracks = response_tracks.json()
	for item in response_tracks['message']['body']['track_list']:
	 	for i in item:
	 		track_id = item[i]["track_id"]
	 		tracks.append(track_id)

# Getting lyrics from track_ids
data = []
no_lyrics_count = 0
url_lyrics = "http://api.musixmatch.com/ws/1.1/track.lyrics.get?"
url_track_id = "http://api.musixmatch.com/ws/1.1/track.get?"
for track_id in tracks:
	payload_lyrics = {'track_id' : int(track_id) ,'f_has_lyrics' : 1, 'apikey' : apikey}
	response_track_id = requests.get(url_track_id, params=payload_lyrics)
	response_track_id = response_track_id.json()
	if response_track_id['message']['body']['track']['has_lyrics'] == 1:
		#print 'lyrics available for track %s :' % response_track_id['message']['body']['track']['track_name'] 
		response_lyric = requests.get(url_lyrics, params=payload_lyrics)
		response_lyric = response_lyric.json()
		response_lyric = response_lyric['message']['body']['lyrics']
		lyric_text = response_lyric['lyrics_body']
		bad_string = '''******* This Lyrics is NOT for Commercial use *******'''
		string = string.replace(bad_string,'')
		data.append(lyric_text)
	else:
		no_lyrics_count += 1

print 'On a total of %s tracks, %s has no lyrics and %s has' % (len(tracks), no_lyrics_count, len(tracks) - no_lyrics_count)

# main problem is that songs returned by this API are truncated. 
# I will try to train the model with this data and see results, but I will have to find a better solution moving forwad.


# Cleaning the Data: a method to clean the data


# Save data in a file
string = ''
for lyric in data:
	string += str(lyric)

# Open a file
f = open("lyrics.txt", "wb")
f.write(string)

# Close opend file
f.close()









