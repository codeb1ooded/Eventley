import eventful
import unicodecsv as csv
import codecs
import random
from math import radians, cos, sin, asin, sqrt
from waitBackened.models import event 
api = eventful.API('mhRcqWrPnjbF86T2')
img=1

def haversine(lon1, lat1, lon2, lat2):
	lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
	dlon = lon2 - lon1 
	dlat = lat2 - lat1
	a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
	c = 2 * asin(sqrt(a)) 
	km = 6367 * c
	return km

def inKilometeres(distance, units):
	abc = distance
	if units == 'miles':
		abc = distance * 1.60934
	elif units == 'km':
		abc = distance
	else:
		abc = 0.001 * distance
	return abc


def event_collection(latitude, longtitude, covered_area, units_distance, select_category_event):
	file_name = "csv/"+select_category_event + '.csv'
	count=0
	links=0 
	with open(file_name,'rb') as csvfile:
		with open('csv/datafile.csv','a+') as csvfile1:
			#fieldnames = ['id', 'title', 'venue_name', 'number_of_likes', 'number_of_comments', 'key']
			#datawriter = csv.DictWriter(csvfile1, fieldnames=fieldnames)
			data = csv.reader(csvfile)
			for row in data:
				key=''.join(row)
				i=0
       			
				events = api.call('/events/search', q=key, l=latitude+", "+longtitude, within=covered_area+"", units=units_distance+"")
				num_of_pages = int(events['page_count'])
				distanceKm = inKilometeres(float(covered_area), units_distance)
				try: 
					for i in range(0, num_of_pages):
						events = api.call('/events/search', q=key, l=latitude+", "+longtitude, within=covered_area+"", units=units_distance+"", page_number=i)
						for Event in events['events']['event']:
							comm = random.randint(10, 50) 
							likes = random.randint(500, 1000)
							calculateKm = haversine(float(longtitude), float(latitude), float(Event['longitude']), float(Event['latitude']))
							distanceScore = (float(distanceKm) - float(calculateKm)) * 100
							distanceScore = distanceScore / distanceKm
							eventobj = event()
							eventobj.Eventid = Event['id']
							eventobj.Eventname = Event['title']
							eventobj.Venuename = Event['venue_name']
							eventobj.Nolikes = likes
							eventobj.Category = key
							eventobj.Nocomments = comm
							eventCall = api.call('/events/get',id = Event['id'], image_sizes="block16")
							images = 0
							if eventCall['images']:
								for image in eventCall['images']:
									images = images + 1
							eventobj.NoImages = images
							if eventCall['links']:
								for image in eventCall['links']:
									images = images + 1
							eventobj.Nolinks = links
							eventobj.Date = eventCall['start_time']
							eventobj.Score = 0.25 * distanceScore + 0.75 * eventobj.Nolikes + eventobj.Nocomments + 2 * images + 1.5 * links;
							eventobj.save()
							count=count+1
							print count
				except:
					print 'exception'