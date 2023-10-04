from django.http import HttpResponse
from .models import Movie
from django.shortcuts import render, get_object_or_404
from .temp_data import movie_data
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .forms import MovieForm

class MovieListView(generic.ListView):
    model = Movie
    template_name = 'movies/index.html'

class MovieDetailView(generic.DetailView):
    model = Movie
    template_name = 'movies/detail.html'

def search_movies(request):
    context = {}
    if request.GET.get('query', False):
        context = {
            "movie_list": [
                m for m in movie_data
                if request.GET['query'].lower() in m['name'].lower()
            ]
        }
    return render(request, 'movies/search.html', context) # modifique esta linha


def create_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie_name = form.cleaned_data['name']
            movie_release_year = form.cleaned_data['release_year']
            movie_poster_url = form.cleaned_data['poster_url']
            movie = Movie(name=movie_name,
                          release_year=movie_release_year,
                          poster_url=movie_poster_url)
            movie.save()
            return HttpResponseRedirect(
                reverse('movies:detail', args=(movie.id, )))
    else:
        form = MovieForm()
    context = {'form': form}
    return render(request, 'movies/create.html', context)
