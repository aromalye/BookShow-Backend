from django.db import models

from multiselectfield import MultiSelectField

# Create your models here.


class Movies(models.Model):

    format_choice = (
        ('2D', '2D'),
        ('3D', '3D'),
    )

    language_choice = (
        ('Malayalam', 'Malayalam'),
        ('Tamil', 'Tamil'),
        ('English', 'English'),
        ('Hindi', 'Hindi'),
    )

    certificate_choice = (
        ('U', 'U'),
        ('U/A', 'U/A'),
        ('A', 'A'),
    )

    genre_choice = (
        ('Action', 'Action'),
        ('Drama', 'Drama'),
        ('Comedy', 'Comedy'),
        ('Romance', 'Romance'),
        ('Horror', 'Horror'),
        ('Fiction', 'Fiction'),
        ('Thriller', 'Thriller'),
    )



    movie_title = models.CharField(max_length=150, unique=True)
    main_image = models.ImageField(upload_to='photos/main')
    cover_pic = models.ImageField(upload_to='photos/cover')
    description = models.TextField(max_length=500)
    movie_format = models.CharField(max_length=2, choices=format_choice)
    language =  models.CharField(max_length=10, choices=language_choice)
    journer = MultiSelectField(choices=genre_choice, max_length=100)
    movie_certificate = models.CharField(max_length=3, choices=certificate_choice)
    is_running = models.BooleanField(default=True)
    rating = models.FloatField(null=True)
    releasing_date = models.DateField(null=True)
    created_date = models.DateField(auto_now_add=True)
    trailer_url = models.URLField(max_length=200, null=True)

    def __str__(self):
        return self.movie_title