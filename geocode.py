import requests
import json

def geoCode(user_input):
	base_url='https://maps.googleapis.com/maps/api/geocode/json?address='+user_input+'&key=AIzaSyCz-F0VhJAlR6HY0oHs7G1NWF2rJPRnStM'
	results = requests.get(base_url)
	results_text = results.text
	results_json = json.loads(results_text)
	for item in results_json['results']:
		Vlat=item['geometry']['location']['lat']
		Vlng=item['geometry']['location']['lng']
		print Vlng
		print Vlat

geoCode('Sahibabad,Uttar pradesh')