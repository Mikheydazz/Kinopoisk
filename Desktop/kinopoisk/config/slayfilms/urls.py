from django.urls import path
from slayfilms.views import *

urlpatterns = [
    path('', home, name='home'),
    path('persons_list/<str:person_role>', persons_list, name='persons_list'),
    path('genres_list/', genres_list, name='genres_list'),
    path('movies_list/', movies_list, name='movies_list'),
    path('person/<int:person_id>/', person_detail, name='person_detail'),
    path('genre_detail/<int:genre_id>/', genre_detail, name='genre_detail'),
    path('movie_detail/<int:movie_id>/', movie_detail, name='movie_detail'),
    path('add_movie_review/', add_movie_review, name='add_movie_review'),
]