# Generated by Django 4.1.5 on 2023-02-08 00:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shows', '0001_initial'),
        ('bookings', '0002_payment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_booked', models.BooleanField(default=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('payment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookings.payment')),
                ('seat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shows.showseat')),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shows.movieshow')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
