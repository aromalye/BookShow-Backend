from django.urls import path

from .import views



urlpatterns = [
    path('run_command/', views.run_command, name="run_command"),

    path('', views.add_tickets, name="add_tickets"),
    path('ticket/user', views.get_added_tickets, name="get_tickets_byuser"),
    path('payment/', views.create_payment, name="create_payment"),
    path('bookticket/', views.bookticket, name="bookticket"),
    path('bookingdetails/<int:pk>/', views.booking_details, name="bookingdetails"),
    path('bookedtickets/<int:pk>/', views.booked_tickets, name="booked_tickets"),

]