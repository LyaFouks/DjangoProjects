from django.http import HttpResponse
from django.shortcuts import render

def about(request):
	return HttpResponse('This is about')


def home(request):
	return HttpResponse(request, 'home.html', {'greeting':'Hello!'})