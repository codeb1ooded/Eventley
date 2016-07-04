import requests
import json

def Weather(lat,lng,cnt):
	base_url='http://api.openweathermap.org/data/2.5/forecast/daily?lat='+lat+'&lon='+lng+'&cnt='+cnt+'&mode=json&appid=47ad83e3abd72657b4946a3dfc63e49b'
	results = requests.get(base_url)
	results_text = results.text
	results_json = json.loads(results_text)
	for item in results_json['list']:
		maxtmp= item['temp']['min']
		mintmp= item['temp']['max']
		print maxtmp
		print mintmp
		
Weather('28','77','1')		
#pass the lat , long and count of the number of days u want to see temperature of!