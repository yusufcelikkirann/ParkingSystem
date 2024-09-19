from django.contrib import admin
from .models import ParkingSpot, Reservation

@admin.register(ParkingSpot)
class ParkingSpotAdmin(admin.ModelAdmin):
    list_display = ['spot_number']  # Park yeri numarasını liste içinde gösterir
    search_fields = ['spot_number']  # Arama yapılacak alanları liste içinde belirtir

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ['plate_number', 'spot', 'reserved_from', 'reserved_to', 'created_at', ]  # Liste görünümünde gösterilecek alanlar
    list_filter = ['spot', 'reserved_from', 'reserved_to']  # Filtreleme seçenekleri
    search_fields = ['plate_number']  # Arama yapılacak alanlar