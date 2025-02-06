from django.shortcuts import render, redirect
from .models import Movie
from django.http import Http404, HttpResponseServerError
from django.http import HttpResponse

# Create your views here.
def index(request):
    newest_movies = Movie.objects.order_by('-release_date')[:15]
    context = {'newest_movies': newest_movies}
    return render(request, 'movies/index.html', context)
    # return HttpResponse("You're at the movies index.")

def show(request, movie_id):
    try:
        movie = Movie.objects.get(pk=movie_id)
    except Movie.DoesNotExist:
        raise Http404("Movie does not exist")
    return render(request, 'movies/show.html', {'movie': movie})

def delete(request, movie_id):
    if request.method == "GET":
        try:
            Movie.objects.filter(pk=movie_id).delete()
        except:
            raise HttpResponseServerError("Delete movie was fail")
        return redirect("/movies")