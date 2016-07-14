import eventful
import unicodecsv as csv
import codecs
import random
api = eventful.API('mhRcqWrPnjbF86T2')
img=1

def event_collection(latitude, longtitude, covered_area, units_distance, select_category_event):
	file_name = "csv/"+select_category_event + '.csv'
	count=0
	with open(file_name,'rb') as csvfile:
		with open('csv/datafile.csv','a+') as csvfile1:
			fieldnames = ['id', 'title', 'venue_name', 'number_of_likes', 'number_of_comments', 'key']
			datawriter = csv.DictWriter(csvfile1, fieldnames=fieldnames)
			data = csv.reader(csvfile)
			for row in data:
				key=''.join(row)
				i=0
       
				events = api.call('/events/search', q=key, l=latitude+", "+longtitude, within=covered_area+"", units=units_distance+"")
				num_of_pages = int(events['page_count'])
			#	try: 
				for i in range(0, num_of_pages):
					events = api.call('/events/search', q=key, l=latitude+", "+longtitude, within=covered_area+"", units=units_distance+"", page_number=i)
					for event in events['events']['event']:
						print "%s at %s of %s" % (event['title'], event['venue_name'],key)
						comm = random.randint(10, 50) 
						likes = random.randint(500, 1000) 
						count=count+1
						print count
    						datawriter.writerow({'id': event['id'], 'title': event['title'], 'venue_name': event['venue_name'], 'number_of_likes':likes, 'number_of_comments':comm, 'key': key})
				#except:
				#	print 'exception'


