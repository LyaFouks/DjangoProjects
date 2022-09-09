from django.shortcuts inport render

def home(request):
	return render(request, 'home.html')

def reverse(request):
	return render(request, 'reverse.html')