from django.shortcuts import render, redirect
from .models import *
# Create your views here.
def add_movie_review(request):
    if not request.user.is_authenticated:
        return redirect('signin')
    if request.method == 'POST':
        movie_id = request.POST.get('movie_id')
        MovieReview.objects.create(
            author = request.user,
            movie = Movie.objects.get(id=movie_id),
            text = request.POST.get('review_text'),
        )
        return redirect('movie_detail', movie_id=movie_id)

def home(request):
    movies = Movie.objects.all()

    context = {
        'movies':movies,
    }

    return render(request, 'slayfilms/home.html', context)


def movies_list(request):
    movies = Movie.objects.all()
    return render(request, 'slayfilms/list/movies_list.html',{
        'movies': movies
        })

def persons_list(request, person_role):
    persons = MoviePerson.objects.filter(role = person_role).order_by('-id')
    if person_role == MoviePerson.RoleType.ACTOR:
        title = 'Актёры'
    else:
        title = 'Режиссёры'
    return render(request, 'slayfilms/list/actors_list.html',{
        'persons': persons, 'title': title
    })

def genres_list(request):
    genres = Genre.objects.all()
    return render(request, 'slayfilms/list/genres_list.html',{
        'genres': genres
    })


def movie_detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    # reviews = MovieReview.objects.filter(movie=movie)
    return render(request, 'slayfilms/detail/movie_detail.html',{
        'movie': movie,
        # 'reviews': reviews
    })

def person_detail(request, person_id):
    person = MoviePerson.objects.get(id=person_id)
    if person.role == MoviePerson.RoleType.ACTOR:
        movies = person.acted_in_movies.all()
    else:
        movies = person.directed_movies.all()

    return render(request, 'slayfilms/detail/actor_detail.html',{
        'person': person,
        'movies': movies
    })

def genre_detail(request, genre_id):
    genre = Genre.objects.get(id=genre_id)
    return render(request, 'slayfilms/detail/genre_detail.html',{
        'genre': genre
    })