# Generated by Django 5.0.2 on 2024-09-17 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0002_reservation_vehicle_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parkingspot',
            name='spot_number',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
