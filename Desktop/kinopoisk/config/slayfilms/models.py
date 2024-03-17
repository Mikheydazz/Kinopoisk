from django.db import models
from core.models import User

# Create your models here.
class Gener(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()


class MoviePerson(models.Model):
    class RoleType(models.TextChoices):
        ACTOR = 'actor', 'Actor'
        DIRECTOR = 'director', 'Director'
    
    name = models.CharField(max_length=255)
    birthdate = models.DateField()
    photo = models.ImageField(
        upload_to='slayfilms/images/movies/photos/',
        blank=True, null=True
    )
    biography = models.TextField()
    role = models.CharField(
        max_length=25,
        choices=RoleType.choices,
        blank = True, null = True
        )

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    poster = models.ImageField(
        upload_to='slayfilms/images/movies/posters/',
        blank=True, null=True
        )
    embed = models.TextField()
    rating = models.FloatField(blank=True, null=True)
    release_date = models.DateField()
    duration = models.PositiveSmallIntegerField()
    geners = models.ManyToManyField(Gener, related_name='movies')
    age_limit = models.PositiveSmallIntegerField()
    actor = models.ManyToManyField(MoviePerson, related_name='acted_in_movie')
    director = models.ManyToManyField(MoviePerson, related_name='directed_movie')
    budget = models.PositiveIntegerField()

class MovieReview(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL,
                                null=True, related_name='reviews')
    movie = models.ForeignKey(Movie, on_delete=models.SET_NULL,
                                null=True, related_name='reviews')
    text = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    author_advice = models.BooleanField(default=True, null=True, blank=True)