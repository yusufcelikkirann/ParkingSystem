from django.db import models

class ParkingSpot(models.Model):
    spot_number = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.spot_number

from django.db import models

class Reservation(models.Model):
    spot = models.ForeignKey(ParkingSpot, on_delete=models.CASCADE)
    plate_number = models.CharField(max_length=15)
    reserved_from = models.DateTimeField()
    reserved_to = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    vehicle_image = models.ImageField(upload_to='vehicles/', blank=True, null=True)

    def __str__(self):
        return f"{self.plate_number} - {self.spot.spot_number}"
