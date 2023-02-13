from django.contrib import admin
from .models import AddTickets, Payment, Booking


# Register your models here.


class AddTicketAdmin(admin.ModelAdmin):
    list_display = ['id', 'seat', 'show', 'user']


class PaymentAdmin(admin.ModelAdmin):
    list_display = ['payment_id', 'id']


class BookingAdmin(admin.ModelAdmin):
    list_display = ['user', 'seat', 'id']


admin.site.register(AddTickets, AddTicketAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Booking, BookingAdmin)
