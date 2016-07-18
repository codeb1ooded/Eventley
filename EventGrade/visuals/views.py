from django.shortcuts import render
from plotly.graph_objs import Bar, Scatter, Figure, Layout
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from django.http import HttpResponse
from django.template import Context, loader, Template
from django.template.loader import get_template
from django.shortcuts import render

def plot_p(request):
	plot([Scatter(x=[1, 2, 3], y=[3, 1, 6])])
	return render(request, 'temp-plot.html', Context())