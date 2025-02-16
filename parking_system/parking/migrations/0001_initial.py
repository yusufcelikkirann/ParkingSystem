# Generated by Django 5.0.2 on 2024-09-17 08:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ParkingSpot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spot_number', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plate_number', models.CharField(max_length=15)),
                ('reserved_from', models.DateTimeField()),
                ('reserved_to', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('spot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parking.parkingspot')),
            ],
        ),
    ]
