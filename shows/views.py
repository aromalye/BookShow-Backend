import datetime

from django.shortcuts import render
from django.http import Http404


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes


from . models import MovieShow, ShowSeat
from . serializers import ShowSerializer, ShowSeatSearializer
from theater.models import Theaters, TheaterSeat

# Create your views here.


class ShowList(APIView):
    def get(self, request, format=None):
        shows = MovieShow.objects.all()
        serializer = ShowSerializer(shows, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request, format=None):
        serializer = ShowSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ShowDetail(APIView):
    def get_object(self, pk):
        try:
            return MovieShow.objects.get(pk=pk)
        except MovieShow.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        show = self.get_object(pk)
        serializer = ShowSerializer(show)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        show = self.get_object(pk)
        serializer = ShowSerializer(show, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        show = self.get_object(pk)
        show.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ShowByMovie(APIView):
    def post(self, request, pk):
        data = request.data
        date = data['date']
        shows = MovieShow.objects.filter(movie__id=pk, date=date)

        currentdate = datetime.datetime.today().strftime('%Y-%m-%d')

        if date == currentdate:
            for show in shows:
                time = show.time
                showid = show.id
                check_show_time = check_show_status(time)
                if check_show_time:
                    print("x")
                    pass
                else:
                    print("y")
                    movie_show = MovieShow.objects.get(id=showid)
                    movie_show.is_tick_avail = False
                    movie_show.save()
            updatedshows = MovieShow.objects.filter(movie__id=pk, date=date).order_by('id')
            serializer = ShowSerializer(updatedshows, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            shows = MovieShow.objects.filter(movie__id=pk, date=date)
            serializer = ShowSerializer(shows, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)


        


class ShowSeatList(APIView):
    def get(self, request, format=None):
        showseat = ShowSeat.objects.all()
        serializer = ShowSeatSearializer(showseat, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request, format=None):
        serializer = ShowSeatSearializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ShowSeatDetail(APIView):
    def get_object(self, pk):
        try:
            return ShowSeat.objects.get(pk=pk)
        except MovieShow.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        showseat = self.get_object(pk)
        serializer = ShowSeatSearializer(showseat)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        showseat = self.get_object(pk)
        data = request.data
        status = data['status']
        print(showseat)
        showseat.status = status
        showseat.save()
        serializer = ShowSeatSearializer(showseat, many=False)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        showseat = self.get_object(pk)
        showseat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SeatByShow(APIView):
    def get(self, request, pk):
        showseat = ShowSeat.objects.filter(show__id=pk)
        serializer = ShowSeatSearializer(showseat, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


def check_show_status(time):
    print(time)
    timex = time
    timey = datetime.datetime.now().strftime("%I:%M %p")
    # show = MovieShow.objects.filter(time__gt=current_time)
    timex_obj = datetime.datetime.strptime(timex, "%I:%M %p")
    timey_obj = datetime.datetime.strptime(timey, "%I:%M %p")
    if timex_obj > timey_obj:
        return True
    else:
        return False




#create all showseats for individual show
@api_view(['POST'])
def add_show_seats(request, pk):
    show = MovieShow.objects.get(id=pk)
    theater = Theaters.objects.get(id=show.theater.id)
    theater_seats = TheaterSeat.objects.filter(theater=theater)
    countx = theater_seats.count() #50
    row = 10
    col = ['A', 'B', 'C', 'D', 'E']
    for x in col:
        for y in range(1, row+1):
            theater_seats = TheaterSeat.objects.get(seatalp=x, seatnum=y, theater=theater)
            show_seat = ShowSeat.objects.create(
                show=show,
                theater_seat=theater_seats
            )
            show_seat.save()
    response = Response()
    response.data = {
        'message': f'{countx} tickets/seats created for show'
    }
    return response


@api_view(['GET'])
def seatstatus(request, pk):
    showseat = ShowSeat.objects.get(id=pk)
    if showseat.status == "available":
        showseat.status = "selected"
        showseat.save()
        sel_count = ShowSeat.objects.filter(status="selected")
        # count = sel_count.count()
        response = Response()
        response.data = {
            'message' : "success"
        }
        return response
        
    if showseat.status == "selected":
        showseat.status = "available"
        showseat.save()
        
        # count = sel_count.count()
        response = Response()
        response.data = {
            'message' : "success"
        }
        return response


@api_view(['GET'])
def sel_seat(request):
    showseat = ShowSeat.objects.filter(status="selected")
    sel_count = showseat.count()
    print(sel_count)
    response = Response()
    response.data = {
        "sel_count" : sel_count
    }
    return response

