from django.contrib import admin
from . models import Theaters, TheaterSeat

# Register your models here.


class TheaterAdmin(admin.ModelAdmin):
    list_display = ['theater_name', 'district', 'id']


class TheaterSeatAdmin(admin.ModelAdmin):
    list_display = ['theater','seatname', 'id']
    list_filter = ['theater']



admin.site.register(Theaters, TheaterAdmin)
admin.site.register(TheaterSeat, TheaterSeatAdmin)