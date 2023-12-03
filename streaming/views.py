from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Movie, Series, Episode
from django.views.generic import TemplateView
from django.db.models import Q



# HomeView
class HomeView(TemplateView):
    template_name = 'streaming/home.html'  # Replace with your actual template path

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_movies'] = Movie.objects.filter(is_featured=True).order_by('-release_date')[:16]
        context['featured_series'] = Series.objects.filter(is_featured=True).order_by('-release_date')[:16]
        # Add more context as needed
        return context



class MovieListView(ListView):
    model = Movie
    template_name = 'streaming/movie_list.html'  # Replace with your actual template path
    context_object_name = 'movies'
    ordering = ['-release_date']  # Order by release date, newest first
    paginate_by = 24  # Or any number you prefer



class MovieDetailView(DetailView):
    model = Movie
    template_name = 'streaming/movie_detail.html'  # Replace with your actual template path



class SeriesListView(ListView):
    model = Series
    template_name = 'streaming/series_list.html'
    context_object_name = 'series'
    ordering = ['-release_date']  # Order by release date, newest first
    paginate_by = 24  # Or any number you prefer



class SeriesDetailView(DetailView):
    model = Series
    template_name = 'streaming/series_detail.html'
    context_object_name = 'series'  # The context variable name in the template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['seasons'] = self.object.seasons.all()
        return context



class EpisodeDetailView(DetailView):
    model = Episode
    template_name = 'streaming/episode_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['series'] = self.object.season.series
        return context



class SearchResultsView(ListView):
    template_name = 'streaming/search_results.html'
    context_object_name = 'results'

    def get_queryset(self):
        query = self.request.GET.get('query', '')
        if query:
            movies = Movie.objects.filter(Q(title__icontains=query) | Q(genres__name__icontains=query)).distinct()
            series = Series.objects.filter(Q(title__icontains=query) | Q(genres__name__icontains=query)).distinct()
            return {'movies': movies, 'series': series}
        else:
            return {'movies': Movie.objects.none(), 'series': Series.objects.none()}

