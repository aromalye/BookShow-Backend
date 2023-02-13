from django.shortcuts import render
from django.http import Http404
from django.http import JsonResponse
from django.core.management import call_command


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response

from . models import AddTickets, Payment, Booking
from . serializers import AddTicketSerializer, PaymentSerializer, BookingSerializer
from user.models import Account
from shows.models import MovieShow, ShowSeat
from user. authentication import *


# Create your views here.


@api_view(['POST'])
def add_tickets(request):
    data = request.data
    userid = data['userid']
    showid = data['showid']
    seatid = data['seatid']
    print("00", userid, showid, seatid)

    ticket_exist = AddTickets.objects.filter(user__id=userid, show__id=showid,seat__id=seatid)
    print("0012", ticket_exist)

    if ticket_exist:
        print("yy")
        ticket = AddTickets.objects.filter(user__id=userid, show__id=showid,seat__id=seatid)
        ticket.delete()
        response = Response()
        response.data = {
            'message':'seat removed'
        }
        return response
    print("00kk", ticket_exist)
    if not ticket_exist:
        print("012120")
        user = Account.objects.get(id=userid)
        show = MovieShow.objects.get(id=showid)
        seat = ShowSeat.objects.get(id=seatid)

        AddTickets.objects.create(
            user=user,
            show=show,
            seat=seat
        )
        response = Response()
        response.data = {
            'message':'seat selected'
        }
        return response


@api_view(['POST'])
@authentication_classes([JWTAuthentications])
def get_added_tickets(request):
    data = request.data
    userid = data['userid']
    showid = data['showid']
    ticket = AddTickets.objects.filter(user__id=userid, show__id=showid)
    print(userid, showid, ticket)
    serializer = AddTicketSerializer(ticket, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_payment(request):
    data = request.data
    userid = data['userid']
    payment_id = data['payment_id']
    payment_method = data['payment_method']
    amount_paid = data['amount_paid']
    status = data['status']

    user = Account.objects.get(id=userid)

    payment = Payment.objects.create(
                user=user,
                payment_id=payment_id,
                payment_method=payment_method,
                amount_paid=amount_paid,
                status=status
            )

    serializer = PaymentSerializer(payment, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def bookticket(request):
    data = request.data
    userid = data['userid']
    showid = data['showid']
    paymentid = data['paymentid']

    user = Account.objects.get(id=userid)
    show = MovieShow.objects.get(id=showid)
    seats = AddTickets.objects.filter(user__id=userid, show__id=showid) #3addtickets
    seat_count = seats.count()
    payment = Payment.objects.get(id=paymentid)
    is_paymentid_used = Booking.objects.filter(payment__id=paymentid).exists()
    print(seats, seat_count, "ss")
    print(is_paymentid_used)
    if is_paymentid_used:
        bookings = Booking.objects.filter(payment__id=paymentid)
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)
    else:
        if seat_count == 1:
            seat = AddTickets.objects.get(user__id=userid, show__id=showid)
            Booking.objects.create(
                user=user,
                show=show,
                seat=seat,
                payment=payment
            )
            show_seat = ShowSeat.objects.get(id=seat.seat.id)
            print(show_seat, "shoewee")
            show_seat.status = "sold"
            show_seat.save()
            bookings = Booking.objects.filter(payment__id=paymentid)
            serializer = BookingSerializer(bookings, many=True)
            return Response(serializer.data)

        else:
            for seat in seats:
                print(seat.id, "GG")
                seat = AddTickets.objects.get(id=seat.id)
                Booking.objects.create(
                    user=user,
                    show=show,
                    seat=seat,
                    payment=payment
                )
                show_seat = ShowSeat.objects.get(id=seat.seat.id)
                print(show_seat, "shoewee")
                show_seat.status = "sold"
                show_seat.save()
        
            bookings = Booking.objects.filter(payment__id=paymentid)
            serializer = BookingSerializer(bookings, many=True)
            return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([JWTAuthentications])
def booking_details(request, pk):
    booking = Booking.objects.filter(payment__id=pk)
    serializer = BookingSerializer(booking, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def booked_tickets(request, pk):
    booking = Booking.objects.filter(user__id=pk)
    serializer = BookingSerializer(booking, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def run_command(request):
    call_command('reset_seats')
    return JsonResponse({'status': 'success'})


