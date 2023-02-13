from django.urls import path

from . views import *
from . import views



urlpatterns = [
    path('', ShowList.as_view(), name="shows"),
    path('<int:pk>/', ShowDetail.as_view(), name="showsbyid"),
    path('movies/<int:pk>/', ShowByMovie.as_view(), name="showsbymovie"),  

    path('showseats/', ShowSeatList.as_view(), name="showseats"),
    path('showseats/create/<int:pk>/', views.add_show_seats, name="add_show_seats"),
    path('showseats/<int:pk>/', ShowDetail.as_view(), name="showseatsbyid"),
    path('showseatsbyshow/<int:pk>/', SeatByShow.as_view(), name="showseatsbyshow"),

    path('seatstatus/<int:pk>/', views.seatstatus, name="seatstatus"),
    path('sel_seat/', views.sel_seat, name="sel_seat_count"),


]