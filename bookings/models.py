from django.db import models

from user.models import Account
from shows.models import MovieShow, ShowSeat

# Create your models here.


class AddTickets(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    show = models.ForeignKey(MovieShow, on_delete=models.CASCADE)
    seat = models.ForeignKey(ShowSeat, on_delete=models.CASCADE)
    is_added = models.BooleanField(default=True)

    def __str__(self):
        return str(self.show) + str(self.seat)


class Payment(models.Model):

    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    payment_id = models.CharField(max_length=200)
    payment_method = models.CharField(max_length=50)
    amount_paid = models.FloatField()
    status = models.CharField(max_length=150)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.payment_id


class Booking(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    show = models.ForeignKey(MovieShow, on_delete=models.CASCADE)
    seat = models.ForeignKey(AddTickets, null=True, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    is_booked = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.user)