from django.contrib import admin

from . models import MovieShow, ShowSeat

# Register your models here.


class ShowAdmin(admin.ModelAdmin):
    list_display = ['movie', 'id', 'theater', 'time']
    list_filter = ['movie', 'theater','time']


class ShowSeatAdmin(admin.ModelAdmin):
    list_display = ['status', 'id', 'theater_seat', 'show']
    list_filter = ['show']


admin.site.register(MovieShow, ShowAdmin)
admin.site.register(ShowSeat, ShowSeatAdmin)