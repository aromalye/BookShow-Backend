# Generated by Django 4.1.5 on 2023-02-08 03:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0004_alter_booking_seat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='seat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bookings.addtickets'),
        ),
    ]
