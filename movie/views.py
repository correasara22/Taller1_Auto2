from django.shortcuts import render
from django.http import HttpResponse

from .models import Movie

# Create your views here.

def home(request):
    #return render(request, 'movie/home.html', {'name': 'Sara Correa'})
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movies = Movie.objects.filter(title__icotains=searchTerm)
    else:
        movies = Movie.objects.all()
    return render(request, 'movie/home.html', {'searchTerm': searchTerm, 'movies': movies})

def about(request):
    return render(request, 'movie/about.html')