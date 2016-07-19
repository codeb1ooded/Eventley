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
		x_score = []
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
    			x_score.append(int(ab[j]['Score']))

		if len(ab) >= 10 : 
			fig = {
				'data': [{'x':[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
				'y': x_likes[:10],
				'type': 'scatter',
				'mode': 'lines',
				}],
				'layout': {'title': 'Number of likes'}
			}
			scatter_diag = plot(fig, filename='my-graph.html', auto_open=False, output_type='div')
			fig = {
				'data': [{'x':[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
				'y': x_comm[:10],
				'type': 'bar'
				}],
				'layout': {'title': 'Number of comments'}
			}
			bar_diag = plot(fig, filename='my-bar.html', auto_open=False, output_type='div')
			fig = {
			'data': [{'labels': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
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
				'data': [{'x':[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
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
			for i in range(0, len(ab)):
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
				'data': [{'x':arr,
				'y': x_likes,
				'type': 'scatter',
				'mode': 'lines',
				}],
				'layout': {'title': 'Number of likes'}
			}
			scatter_diag = plot(fig, filename='my-graph.html', auto_open=False, output_type='div')
			fig = {
				'data': [{'x':arr,
				'y': x_comm,
				'type': 'bar'
				}],
				'layout': {'title': 'Number of comments'}
			}
			bar_diag = plot(fig, filename='my-bar.html', auto_open=False, output_type='div')
			fig = {
			'data': [{'labels': arr,
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
				'data': [{'x':[1, 2, 3, 4],
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
		utf8 = [scatter_diag, u'<br>', bar_diag, u'<br>', pie_chart, u'<br>', bubble_diag]
		html = ''.join(utf8) #str(scatter_diag) + u'<br>' + str(bar_diag) + u'<br>' + str(pie_chart)
		return HttpResponse(html)