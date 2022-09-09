from django.shortcuts inport render

def home(request):
	return render(request, 'home.html')