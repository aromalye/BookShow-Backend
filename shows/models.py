from django.db import models

from theater.models import Theaters, TheaterSeat
from movie.models import Movies

# Create your models here.


class MovieShow(models.Model):

    TIME = (
        ('6:30 AM', '6:30 AM'),
        ('10:30 AM', '10:30 AM'),
        ('2:30 PM', '2:30 PM'),
        ('6:30 PM', '6:30 PM'),
        ('10:30 PM', '10:30 PM'),
    )

    theater = models.ForeignKey(Theaters, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    time = models.CharField(choices=TIME, max_length=100)
    date = models.DateField()
    total_tickets = models.IntegerField(default=50)
    is_tick_avail = models.BooleanField(default=True)

    def __str__(self):
        slug = self.movie.movie_title[:4] + self.theater.theater_name[:4] + str(self.time)
        return str(slug)


class ShowSeat(models.Model):

    STATUS = (
        ('sold', 'sold'),
        ('available', 'available'),
        ('selected', 'selected'),
    )

    show = models.ForeignKey(MovieShow, on_delete=models.CASCADE)
    theater_seat  = models.ForeignKey(TheaterSeat, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS, max_length=50, default='available')
    price = models.FloatField(default=150)
    # bookingID = models.ForeignKey(ShowBooking, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return str(self.theater_seat)