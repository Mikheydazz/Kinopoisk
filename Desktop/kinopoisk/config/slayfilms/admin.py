from django.contrib import admin
from slayfilms.models import *

# Register your models here.

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'rating',
        'budget',
        'release_date'
    )

    list_editable = (
        'budget',
    )

@admin.register(Genre)
class GenerAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

@admin.register(MoviePerson)
class MoviePersonAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'role',
    )

@admin.register(MovieReview)
class MovieReviewAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'created_at',
    )