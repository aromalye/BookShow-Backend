from django.urls import path
from . views import *
from . import views



urlpatterns = [
    path('', TheaterList.as_view(), name="theater"),
    path('<int:pk>/', TheaterDetail.as_view(), name="theaterbyid"),

    path('theaterseats/', TheaterSeatList.as_view(), name="theaterseats"),
    path('theaterseats/<int:pk>', TheaterSeatList.as_view(), name="theaterseatsbyid"),
    path('theaterseats/create/<int:pk>/', views.add_theater_seats, name="add_theater_seats"),

]