import tmdbsimple as tmdb
from datetime import datetime


MY_API_KEY = '666038f66859e2a1a566d589b3fe1e34'
IMG_SRC = 'http://image.tmdb.org/t/p/w185/'

tmdb.API_KEY = MY_API_KEY

current_time = datetime.now()
released_before = '-'.join([str(current_time.year), str(current_time.month), str(current_time.day)])


search = tmdb.Search()
response = search.movie(query="hi")

for result in response['results']:
	print("************************************************************************")
	print(result['id'])
	print(result['original_title'])
	print(result['poster_path'])
	print(result['release_date'])
	print("************************************************************************")

#print(beast.credits()['crew'])
'''
print (type(response['results'][0]['release_date']))

for result in response['results']:
	if result['release_date']:
		if result['release_date'] < released_before:
			print(result)
'''
#conf = tmdb.Configuration()
#beast = tmdb.Movies(response['results'][0]['id'])
'''
attrs=['account_states', 'alternative_titles', 'base_uri', 'changes', 'credits', 'headers', 'id', 'images', 'info', 'keywords', 'latest', 'lists', 'now_playing', 'popular', 'rating', 'releases', 'reviews', 'similar_movies', 'top_rated', 'translations', 'upcoming', 'videos']

for attr in attrs:
	print(attr, ": ", getattr(beast, attr))
'''
#print(beast.images()['posters'])

#for d in beast.images()['posters']:
	#print(d)#print (d['width'], d['file_path'])
'''

import requests

url = "https://api.themoviedb.org/3/configuration?api_key="+MY_API_KEY

payload = "{}"
response = requests.request("GET", url, data=payload)

print(response.text)'''