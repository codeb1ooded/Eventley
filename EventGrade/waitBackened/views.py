from django.http import HttpResponse
from django.template import Context, loader, Template
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.shortcuts import render
from waitBackened.collect_events import *
from django.http import HttpResponseRedirect

def wait_for_backend(request):
	if 'units_distance' in request.GET:
		latitude = request.GET['latitude']
		longtitude = request.GET['longtitude']
		covered_area = request.GET['covered_area']
		units_distance = request.GET['units_distance']
		select_category_event = request.GET['select_category_event']
		li=event_collection(latitude, longtitude, covered_area, units_distance, select_category_event)
		#j=len(li)
		i=0
		x_comm = []
		x_likes = []
		x_name = []
		x_link = []
		#Database starts now!!!
    	event.objects.order_by('-Date','-score')
    	for idd in li:
    		ab = event.objects.filter(Eventid = idd).values()
    		print ab[0]['Nocomments']
    		print type(ab)
    		print type(x_comm)
    		x_comm.append(ab[0]['Nocomments'])
    		x_likes.append(ab[0]['Nolikes'])
    		x_name.append(ab[0]['Eventname'])
    		x_link.append(ab[0]['NoImages'])
    		
   		
		scatter_diag = plot([Scatter(x=[1, 2, 3], y=[3, 1, 6])], filename='my-graph.html', auto_open=False, output_type='div')
		bar_diag = plot([Bar(x=['1', '2', '3'], y=[13, 10, 50])], filename='my-bar.html', auto_open=False, output_type='div')
		fig = {
			'data': [{'labels': ['Residential', 'Non-Residential', 'Utility'],
			'values': [19, 26, 55],
			'type': 'pie',
			'name': 'Event Comparison',
			'text': 'likes',
			'textposition': 'inside',
			'hoverinfo': 'label+percent+name',
			'hole': .4,}],
			'layout': {'title': 'Event Comparison',
			'annotations': [{'showarrow': 'False', 'text': 'likes'}]}
			}
		pie_chart = plot(fig, filename='my-pie.html', auto_open=False, output_type='div')
		fig = {
			'data': [{'x':[1, 2, 3, 4],
			'y': [10, 11, 12, 13],
			'mode': 'markers',
			'marker': { 'color': ['rgb(93, 164, 214)', 'rgb(255, 144, 14)',  'rgb(44, 160, 101)', 'rgb(255, 65, 54)'],
			'opacity': [1, 0.8, 0.6, 0.4],
			'size': [40, 60, 80, 100]
			 }
			}],
			'layout': {'title': 'Marker Size and Color'}
		}
		bubble_diag = plot(fig, filename='my-bubble.html', auto_open=False, output_type='div')
		utf8 = [scatter_diag, u'<br>', bar_diag, u'<br>', pie_chart, u'<br>', bubble_diag]
		html = ''.join(utf8) #str(scatter_diag) + u'<br>' + str(bar_diag) + u'<br>' + str(pie_chart)
		return HttpResponse(html)