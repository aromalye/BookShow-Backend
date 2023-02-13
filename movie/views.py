from django.shortcuts import render
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from rest_framework import status

from . models import Movies
from . serializers import MovieSerializer


# Create your views here.


# to get all movie deatails
@api_view(['GET'])
def movie_list(request):
    movies = Movies.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


#to get movie by id
@api_view(['GET'])
def movie_by_id(request, pk):
    movie = Movies.objects.get(id=pk)
    serializer = MovieSerializer(movie, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)



class MovieList(APIView):
    def get(self, request, format=None):
        movies = Movies.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
   

class MovieDetail(APIView):
    def get_object(self, pk):
        try:
            return Movies.objects.get(pk=pk)
        except Movies.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        movie = self.get_object(pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        movie = self.get_object(pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#search movies with its title
@api_view(['GET'])
def movie_search(request, key):
    movies = Movies.objects.filter(movie_title__icontains=key)
    print(movies, "dd")
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


#filter movie by journer,certificate,language,format
@api_view(['POST'])
def filter_movie(request):
    data = request.data
    lang = data['language']
    m_format = data['movie_format']
    journer = data['journer']
    m_cert = data['movie_certificate']

    if m_cert and journer and m_format and lang:
        movies = Movies.objects.filter(
            movie_certificate__icontains=m_cert,
            journer__icontains=journer,
            movie_format__icontains=m_format,
            language__icontains=lang
            )
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif journer and m_format and lang:
        movies = Movies.objects.filter(
            journer__icontains=journer,
            movie_format__icontains=m_format,
            language__icontains=lang
            )
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif m_format and journer:
        movies = Movies.objects.filter(
            movie_format__icontains=m_format,
            journer__icontains=journer
            )
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif journer and lang:
        movies = Movies.objects.filter(
            journer__icontains=journer,
            language__icontains=lang
            )
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    elif m_format and lang:
        movies = Movies.objects.filter(
            movie_format__icontains=m_format,
            language__icontains=lang
            )
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif lang:
        movies = Movies.objects.filter(
            language__icontains=lang
            )
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif m_format:
        movies = Movies.objects.filter(
            movie_format__icontains=m_format,
            )
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif journer:
        movies = Movies.objects.filter(
            journer__icontains=journer
            )
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif m_cert:
        movies = Movies.objects.filter(
            movie_certificate__icontains=m_cert,
            )
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        movies = Movies.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



    def post(self, request):
        data = request.data
        # director = data["director"]
        movie_title = data["movie_title"]
        print("dd")

        # if title is not None and director is not None:
        #     movies = Movies.objects.filter(movie_title__icontains=title, language__icontains=director)
        if movie_title is not None:
            movies = Movies.objects.filter(movie_title__icontains=movie_title)
        # elif director is not None:
        #     movies = Movies.objects.filter(language__icontains=director)

        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)