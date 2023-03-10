# Generated by Django 4.1.5 on 2023-02-04 08:08

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_title', models.CharField(max_length=150, unique=True)),
                ('main_image', models.ImageField(upload_to='photos/main')),
                ('cover_pic', models.ImageField(upload_to='photos/cover')),
                ('description', models.TextField(max_length=500)),
                ('movie_format', models.CharField(choices=[('2D', '2D'), ('3D', '3D')], max_length=2)),
                ('language', models.CharField(choices=[('Malayalam', 'Malayalam'), ('Tamil', 'Tamil'), ('English', 'English'), ('Hindi', 'Hindi')], max_length=10)),
                ('journer', multiselectfield.db.fields.MultiSelectField(choices=[('Action', 'Action'), ('Drama', 'Drama'), ('Comedy', 'Comedy'), ('Romance', 'Romance'), ('Horror', 'Horror'), ('Fiction', 'Fiction'), ('Thriller', 'Thriller')], max_length=100)),
                ('movie_certificate', models.CharField(choices=[('U', 'U'), ('U/A', 'U/A'), ('A', 'A')], max_length=3)),
                ('is_running', models.BooleanField(default=True)),
                ('rating', models.FloatField(null=True)),
                ('releasing_date', models.DateField(null=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('trailer_url', models.URLField(null=True)),
            ],
        ),
    ]
