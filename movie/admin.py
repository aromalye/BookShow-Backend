from django.contrib import admin

from . models import Movies

# Register your models here.


class MovieAdmin(admin.ModelAdmin):
    list_display = ["id", "movie_title"]


admin.site.register(Movies, MovieAdmin)