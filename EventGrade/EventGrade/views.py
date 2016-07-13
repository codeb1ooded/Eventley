from django.http import HttpResponse
from django.template import Context, loader, Template
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.shortcuts import render
 
def hello(request):
	latitude = request.GET['latitude']
	longtitude = request.GET['longtitude']
	return render(request, 'fromuser.html', {'latitude': latitude, 'longtitude': longtitude})

def my_homepage_view(request):
	return render(request, 'homepage.html', Context())
