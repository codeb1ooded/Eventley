from django.http import HttpResponse
from plotly.graph_objs import Bar, Scatter, Figure, Layout
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
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
    	print len(li)
    	for i in range(0, len(li)):
    		idd=li[i]
    		ab = event.objects.filter(Eventid = idd).values()
    		for j in range(0, len(li)):
    			x_comm.append(ab[j]['Nocomments'])
    			x_likes.append(ab[j]['Nolikes'])
    			x_name.append(ab[j]['Eventname'])
    			x_link.append(ab[j]['NoImages'])
		fig = {
			'data': [{'x':[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
			'y': x_comm,
			'type': 'scatter',
			'mode': 'lines',
			}],
			'layout': {'title': 'Marker Size and Color'}
		}
		scatter_diag = plot(fig, filename='my-graph.html', auto_open=False, output_type='div')
		bar_diag = plot([Bar(x=[x_name[0], x_name[1], x_name[2]], y=[x_comm[0], x_comm[1], x_comm[2]])], filename='my-bar.html', auto_open=False, output_type='div')
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