from django.urls import path
from slayfilms.views import *

urlpatterns = [
    path('', home, name='home'),
    path('actors_list/', actors_list, name='actors_list'),
    path('directors_list/', directors_list, name='directors_list'),
    path('genres_list/', genres_list, name='genres_list'),
    path('movies_list/', movies_list, name='movies_list'),
    path('actor_detail/<int:actor_id>/', actor_detail, name='actor_detail'),
    path('director_detail/<int:director_id>/', director_detail, name='director_detail'),
    path('genre_detail/<int:genre_id>/', genre_detail, name='genre_detail'),
    path('movie_detail/<int:movie_id>/', movie_detail, name='movie_detail'),
]