from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy as r
from django.views.generic import CreateView, ListView, DetailView
from django.db.models import Max
from .models import Movie


def home(request):
    return render(request, 'index.html')


# def movie_list(request):
#     movies = Movie.objects.all()
#     context = {'movies': movies}
#     return render(request, 'core/movie_list.html', context)

class MovieList(ListView):
    template_name = 'core/movie_list.html'
    model = Movie
    context_object_name = 'movies'

    def get_queryset(self):
        m = Movie.objects.all()
        # Filme de maior bilheteria
        if self.request.GET.get('great_movie', False):
            q = Movie.objects.all().aggregate(Max('raised'))
            m = Movie.objects.filter(raised=q['raised__max'])
        return m


# def movie_detail(request, pk):
#     movie = get_object_or_404(Movie, pk=pk)
#     context = {'movie': movie}
#     return render(request, 'core/movie_detail.html', context)

class MovieDetail(DetailView):
    template_name = 'core/movie_detail.html'
    model = Movie


class MovieCreate(CreateView):
    template_name = 'core/movie_form.html'
    model = Movie
    fields = '__all__'
    success_url = r('core:movie_list')
