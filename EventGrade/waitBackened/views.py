from django.http import HttpResponse
from django.template import Context, loader, Template
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.shortcuts import render

def wait_for_backend(request):
	if 'units_distance' in request.GET:
		latitude = request.GET['latitude']
		longtitude = request.GET['longtitude']
		covered_area = request.GET['covered_area']
		units_distance = request.GET['units_distance']
		select_category_event = request.GET['select_category_event']
	return HttpResponse(latitude)
