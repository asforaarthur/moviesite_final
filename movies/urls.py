from django.urls import path

from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.MovieListView.as_view(), name='index'), # edite esta linha
    path('search/', views.search_movies, name='search'),
    path('create/', views.create_movie, name='create'),
    path('<int:pk>/', views.MovieDetailView.as_view(), name='detail'), # edite esta linha
]