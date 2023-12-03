from django.urls import path
from .views import MovieListView, MovieDetailView, SeriesListView, SeriesDetailView, HomeView, EpisodeDetailView, \
     SearchResultsView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),  # Home page
    path('movies/', MovieListView.as_view(), name='movie_list'),  # List of movies
    path('movies/<int:pk>/', MovieDetailView.as_view(), name='movie_detail'),  # Detail view for a specific movie

    # URL for listing all series
    path('series/', SeriesListView.as_view(), name='series_list'),

    # URL for series details
    path('series/<int:pk>/', SeriesDetailView.as_view(), name='series_detail'),

    # URL for episode details
    path('episodes/<int:pk>/', EpisodeDetailView.as_view(), name='episode_detail'),

    # URL for search
    path('search/', SearchResultsView.as_view(), name='search_results'),

    # Add other URL patterns as needed
]

