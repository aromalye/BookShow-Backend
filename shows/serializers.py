from rest_framework import serializers

from .models import MovieShow, ShowSeat
from movie.serializers import MovieSerializer
from theater.serializers import TheaterSerializer, TheaterSeatSearializer


class ShowSerializer(serializers.ModelSerializer):
    movie=MovieSerializer(many=False)
    theater=TheaterSerializer(many=False)
    class Meta:
        model = MovieShow
        fields = '__all__'


class ShowSeatSearializer(serializers.ModelSerializer):
    theater_seat = TheaterSeatSearializer(many=False)
    show = ShowSerializer(many=False)
    class Meta:
        model = ShowSeat
        fields = '__all__'