from django.urls import path

from . views import MovieList, MovieDetail
from . import views



urlpatterns = [

    path('', MovieList.as_view(), name="movie"),
    path('<int:pk>/', MovieDetail.as_view(), name="moviebyid"),
    path('filter/', views.filter_movie, name="filtermovie"),
    path('search/<str:key>/', views.movie_search, name="search"),

]