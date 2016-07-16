import requests
import json
import time
from array import *

def Weather(lat, lng, cnt):
	lat = str(lat)
	lng = str(lng)
	cnt = str(cnt)
	base_url='http://api.openweathermap.org/data/2.5/forecast/daily?lat='+lat+'&lon='+lng+'&cnt='+cnt+'&mode=json&appid=47ad83e3abd72657b4946a3dfc63e49b&units=metric'
	results = requests.get(base_url)
	results_text = results.text
	results_json = json.loads(results_text)
	for item in results_json['list']:
		maxtmp= item['temp']['min']
		mintmp= item['temp']['max']
		if bool(maxtmp > 35) | bool(mintmp < 25) :
			return "1"
	return	"2"

def calculateDays(datestr):
	daysInMonth = array('i',[31,28,31,30,31,30,31,31,30,31,30,31])
	month = int(datestr[5]) * 10 + int(datestr[6])
	date = int(datestr[8]) *10 + int(datestr[9])
	curDate = int(time.strftime("%d"))
	curMonth = int(time.strftime("%m"))
	if(month == curMonth):
		if(curDate <= date):
			return date - curDate
		else:
			return -1;
	if(month == curMonth + 1):
		return daysInMonth[curMonth]-curDate + date
	return -1