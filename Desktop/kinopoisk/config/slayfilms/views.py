from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'slayfilms/home.html')


def movies_list(request):
    return render(request, 'slayfilms/list/movies_list.html')

def actors_list(request):
    return render(request, 'slayfilms/list/actors_list.html')

def directors_list(request):
    return render(request, 'slayfilms/list/directors_list.html')

def genres_list(request):
    return render(request, 'slayfilms/list/genres_list.html')


def movie_detail(request, movie_id):
    return render(request, 'slayfilms/detail/movie_detail.html')

def actor_detail(request, actor_id):
    return render(request, 'slayfilms/detail/actor_detail.html')

def director_detail(request, director_id):
    return render(request, 'slayfilms/detail/director_detail.html')

def genre_detail(request, genre_id):
    return render(request, 'slayfilms/detail/genre_detail.html')