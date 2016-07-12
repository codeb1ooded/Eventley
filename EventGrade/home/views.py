from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader, Template
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.shortcuts import render
 

def my_homepage_view(request):
	return render(request, 'homepage.html', Context())

# Create your views here.
