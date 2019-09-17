import json
import requests

#Request URL, headers and params
u = 'https://api.spotify.com/v1/me/player/currently-playing'
h = {'Authorization': 'Bearer <insert authorization token here>'}
p = {'market': 'FI'}

#Make the request
request = requests.get(url=u, headers=h, params=p)

#Get the JSON from the request
response = request.json()

#Get the values we want
song = response['item']['name']
album = response['item']['album']['name']

#We need to get all the artists since there can be multiple artists for a song
artists = []

#Go through the artists
for x in response['item']['artists']:
    artists.append(x['name'])

#For debugging purposes so we can see the request, comment out or remove the following line when not needed anymore
#print(json.dumps(response,indent=4))

#Print the song details
print(song)
print(album)

#Artists need to be printed individually
artists_string = ""

#Loop through the artists and add commas between the artists but not before or after them
for artist in artists:
    if len(artists) == artists.index(artist) + 1 and artists.index(artist) != 0:
        artists_string = artists_string + ", "
    artists_string = artists_string + artist

#Print the artists
print(artists_string)