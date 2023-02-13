from django.db import models

# Create your models here.


class Theaters(models.Model):

    district_choices = (
        ('TVM', 'Trivandrum'),
        ('EKM', 'Eranakulam'),
        ('kZH', 'Kozhikode'),
    )

    theater_name = models.CharField(max_length=50)
    about_theater = models.TextField(max_length=350, blank=True)
    landmark_1 = models.CharField(max_length=50)
    landmark_2 = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=25)
    district = models.CharField(max_length=50, choices=district_choices)
    state = models.CharField(max_length=25)
    postal_code = models.CharField(max_length=6)
    country = models.CharField(max_length=25)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.theater_name


class TheaterSeat(models.Model):
    SEAT_ALPH = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
    )
    

    STATUS = (
        ('sold', 'sold'),
        ('available', 'available'),
        ('selected', 'selected'),
    )

    SEAT_NO= (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10),
    )
    theater = models.ForeignKey(Theaters, on_delete=models.CASCADE)
    seatnum = models.IntegerField(choices=SEAT_NO, null=True)
    seatalp = models.CharField(choices=SEAT_ALPH, max_length=1, null=True)
    status = models.CharField(choices=STATUS, max_length=10, default='available')

    def seatname(self):
        return self.seatalp + str(self.seatnum)

    def __str__(self):
        return self.seatalp + str(self.seatnum)