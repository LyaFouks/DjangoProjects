from django.http import HttpResponse


def about(request):
	return HttpResponse('This is about')


def home(request):
	return HttpResponse('<h1>This is home</h1>')