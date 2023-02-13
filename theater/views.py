from django.shortcuts import render
from django.http import Http404


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from . models import Theaters, TheaterSeat
from . serializers import TheaterSerializer, TheaterSeatSearializer

# Create your views here.


class TheaterList(APIView):
    def get(self, request, format=None):
        theaters = Theaters.objects.all()
        serializer = TheaterSerializer(theaters, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request, format=None):
        serializer = TheaterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TheaterDetail(APIView):
    def get_object(self, pk):
        try:
            return Theaters.objects.get(pk=pk)
        except Theaters.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        theater = self.get_object(pk)
        serializer = TheaterSerializer(theater)
        return Response(serializer.data)


    def delete(self, request, pk, format=None):
        theater = self.get_object(pk)
        theater.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TheaterSeatList(APIView):
    def get(self, request, format=None):
        theaterseats = TheaterSeat.objects.all()
        serializer = TheaterSeatSearializer(theaterseats, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request, format=None):
        serializer = TheaterSeatSearializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TheaterSeatDetail(APIView):
    def get_object(self, pk):
        try:
            return TheaterSeat.objects.get(pk=pk)
        except TheaterSeat.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        theaterseat = self.get_object(pk)
        serializer = TheaterSeatSearializer(theaterseat)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        theaterseat = self.get_object(pk)
        serializer = TheaterSeatSearializer(theaterseat, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        TheaterSeat = self.get_object(pk)
        TheaterSeat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#create all theaterseats for theaters
@api_view(['POST'])
def add_theater_seats(request, pk):
    theater = Theaters.objects.get(id=pk)
    row = 10
    col = ['A', 'B', 'C', 'D', 'E']
    for x in col:
        for y in range(1, row+1):
            theater_seat = TheaterSeat.objects.create(
                theater=theater,
                seatnum=y,
                seatalp=x,
            )
            theater_seat.save()
    response = Response()
    response.data = {
        'message': 'theater seats created successfully'
    }
    return response