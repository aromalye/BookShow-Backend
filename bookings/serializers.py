from rest_framework import serializers

from .models import AddTickets, Payment, Booking
from user.serializers import AccountSerializer
from shows.serializers import ShowSerializer, ShowSeatSearializer


class AddTicketSerializer(serializers.ModelSerializer):
    user = AccountSerializer(many=False)
    show = ShowSerializer(many=False)
    seat = ShowSeatSearializer(many=False)
    class Meta:
        model = AddTickets
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    user = AccountSerializer(many=False)
    class Meta:
        model = Payment
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    user = AccountSerializer(many=False)
    show = ShowSerializer(many=False)
    seat = AddTicketSerializer(many=False)
    payment = PaymentSerializer(many=False)
    class Meta:
        model = Booking
        fields = '__all__'