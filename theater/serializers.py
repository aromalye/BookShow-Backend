from rest_framework import serializers
from . models import Theaters, TheaterSeat


class TheaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theaters
        fields = '__all__'


class TheaterSeatSearializer(serializers.ModelSerializer):
    class Meta:
        model = TheaterSeat
        fields = '__all__'