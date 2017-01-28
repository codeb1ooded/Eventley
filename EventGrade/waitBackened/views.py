from django.http import HttpResponse
from plotly.graph_objs import Bar, Scatter, Figure, Layout
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from django.template import Context, loader, Template
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.shortcuts import render
import csv
from django.http import HttpResponseRedirect
from waitBackened.eventful import *
import codecs
import random
from math import radians, cos, sin, asin, sqrt
from waitBackened.models import event 
from waitBackened.weather import *
import datetime
from array import *

api = API('WC9TDF3TpJzXXztH')
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

def wait_for_backend(request):
	if 'units_distance' in request.GET:
		latitude = request.GET['latitude']
		longtitude = request.GET['longtitude']
		covered_area = request.GET['covered_area']
		units_distance = request.GET['units_distance']
		select_category_event = request.GET['select_category_event']
		file_name = "csv/"+select_category_event + '.csv'
		count=0
		links=0 
		li=[]
		j=0
		x_comm = []
		x_likes = [] #array(1000)
		x_name = [] #array(1000)
		x_link = [] #array(1000)
		x_score = [] #array(1000)
		with open(file_name,'rb') as csvfile:
			with open('csv/datafile.csv','a+') as csvfile1:
				data = csv.reader(csvfile)
				for row in data:
					key=''.join(row)
					i=0
       		
					events_1 = api.call('/events/search', q=key, l=latitude+", "+longtitude, within=covered_area+"", units=units_distance+"")
					if 'page_count' in events_1:
						num_of_pages = int(events_1['page_count'])
					else:
						num_of_pages = 1
					print num_of_pages
					distanceKm = inKilometeres(float(covered_area), units_distance)
					try:
					  for i in range(0, num_of_pages):
						events = api.call('/events/search', q=key, l=latitude+", "+longtitude, within=covered_area+"", units=units_distance+"", 	page_number=i)
						for Event in events['events']['event']:
							comm = random.randint(10, 50) 
							likes = random.randint(500, 1000)
							calculateKm = haversine(float(longtitude), float(latitude), float(Event['longitude']), float(Event['latitude']))
							distanceScore = (float(distanceKm) - float(calculateKm)) * 100
							distanceScore = distanceScore / distanceKm
							#list for event-id
							print Event['id']
							######
							eventobj = event()
							eventobj.Eventid = Event['id']
							eventobj.Eventname = Event['title']
							eventobj.Venuename = Event['venue_name']
							eventobj.Nolikes = likes
							eventobj.Category = key
							eventobj.Nocomments = comm
							eventCall = api.call('/events/get',id = Event['id'], image_sizes="block16")
							print eventobj.Eventname
							images = 0
							if eventCall['images']:
								for image in eventCall['images']:
									images = images + 1
							eventobj.NoImages = images
							if eventCall['links']:
								for image in eventCall['links']:
									links = links + 1
							eventobj.Nolinks = links
							eventobj.Date = eventCall['start_time']
							days = int(calculateDays(eventCall['start_time']))
							weatherScore = int(Weather(Event['latitude'], Event['longitude'], days))
							eventobj.Score = (0.25 * distanceScore + 0.75 * eventobj.Nolikes + eventobj.Nocomments + 2 * images + 1.5 * links) * weatherScore / 2 

    							ab = event.objects.filter(Eventid = Event['id']).values()
    							x_comm.append(eventobj.Nocomments)
    							x_likes.append(eventobj.Nolikes)
				    			x_name.append(eventobj.Eventname)
				    			x_link.append(images)
				    			x_score.append(eventobj.Score)
							eventobj.save()
							count=count+1
							print count
					except:
						print 'key error'
		#j=len(li)
		#Database starts now!!!
    #	event.objects.order_by('-Date','-score')
    #	print len(li)

		if len(x_name) >= 10 : 
			fig = {
				'data': [{'x': x_name[:10],
				'y': x_likes[:10],
				'type': 'scatter',
				'mode': 'lines',
				}],
				'layout': {'title': 'Number of likes'}
			}
			scatter_diag = plot(fig, filename='my-graph.html', auto_open=False, output_type='div')
			fig = {
				'data': [{'x': x_name[:10],
				'y': x_comm[:10],
				'type': 'bar'
				}],
				'layout': {'title': 'Number of comments'}
			}
			bar_diag = plot(fig, filename='my-bar.html', auto_open=False, output_type='div')
			fig = {
			'data': [{'labels': x_name[:10],
				'values': x_score[:10],
				'type': 'pie',
				'name': 'Score',
				'text': 'score',
				'textposition': 'inside',
				'hoverinfo': 'label+percent+name',
				'hole': .4,}],
				'layout': {'title': 'Score',
				'annotations': [{'showarrow': 'False', 'text': 'score'}]}
				}
			pie_chart = plot(fig, filename='my-pie.html', auto_open=False, output_type='div')
			fig = {
				'data': [{'x': x_name[:10],
				'y': x_link[:10],
					'mode': 'markers',
				'marker': { 'color': ['rgb(255,0,0)', 'rgb(0,255,0)', 'rgb(0,0,255)', 'rgb(255,255,0)', 'rgb(0,255,255)', 'rgb(255,0,255)', 'rgb(192,192,192)', 'rgb(128,0,0)', 'rgb(128,128,0)', 'rgb(128,0,128)'],
				'opacity': [1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1],
				'size': [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
				 }
				}],
				'layout': {'title': 'Images'}
			}
			bubble_diag = plot(fig, filename='my-bubble.html', auto_open=False, output_type='div')
		else:
			arr = []
			op = []
			sz = []
			clr = []
			for i in range(0, len(x_name)):
				arr.append(i)
				op.append((10-i)*0.1)
				sz.append(100)
				if i == 0:
					clr.append('rgb(255,0,0)')
				elif i == 1:
					clr.append('rgb(0,255,0)')
				elif i == 2:
					clr.append('rgb(0,0,255)')
				elif i == 3:
					clr.append('rgb(255,255,0)')
				elif i == 4:
					clr.append('rgb(0,255,255)')
				elif i == 5:
					clr.append('rgb(255,0,255)')
				elif i == 6:
					clr.append('rgb(192,192,192)')
				elif i == 7:
					clr.append('rgb(128,0,0)')
				elif i == 8:
					clr.append('rgb(128,128,0)')
				elif i == 9:
					clr.append('rgb(128,0,128)')
			fig = {
				'data': [{'x': x_name,
				'y': x_likes,
				'type': 'scatter',
				'mode': 'lines',
				}],
				'layout': {'title': 'Number of likes'}
			}
			scatter_diag = plot(fig, filename='my-graph.html', auto_open=False, output_type='div')
			fig = {
				'data': [{'x': x_name,
				'y': x_comm,
				'type': 'bar'
				}],
				'layout': {'title': 'Number of comments'}
			}
			bar_diag = plot(fig, filename='my-bar.html', auto_open=False, output_type='div')
			fig = {
			'data': [{'labels': x_name,
				'values': x_score,
				'type': 'pie',
				'name': 'Score',
				'text': 'score',
				'textposition': 'inside',
				'hoverinfo': 'label+percent+name',
				'hole': .4,}],
				'layout': {'title': 'Score',
				'annotations': [{'showarrow': 'False', 'text': 'score'}]}
				}
			pie_chart = plot(fig, filename='my-pie.html', auto_open=False, output_type='div')
			fig = {
				'data': [{'x': x_name,
				'y': x_link,
					'mode': 'markers',
				'marker': { 'color': clr,
				'opacity': op,
				'size': sz
				 }
				}],
				'layout': {'title': 'Marker Size and Color'}
			}
			bubble_diag = plot(fig, filename='my-bubble.html', auto_open=False, output_type='div')
		utf8 = [scatter_diag, u'<br><br><br><br><br>', bar_diag, u'<br><br><br><br><br>', pie_chart, u'<br><br><br><br><br>', bubble_diag]
		html = ''.join(utf8) #str(scatter_diag) + u'<br>' + str(bar_diag) + u'<br>' + str(pie_chart)
		return HttpResponse(html)
