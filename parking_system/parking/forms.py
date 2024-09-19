from django import forms
from .models import ParkingSpot, Reservation

class ReservationForm(forms.ModelForm):
    spot = forms.ModelChoiceField(queryset=ParkingSpot.objects.all(), label='Spot Number')
    plate_number = forms.CharField(max_length=15, label='Plate Number')
    reserved_from = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}), label='Start Time')
    reserved_to = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}), label='End Time')
    vehicle_image = forms.ImageField(required=False, label='Upload Vehicle Image')  # Araç görseli

    class Meta:
        model = Reservation
        fields = ['spot', 'plate_number', 'reserved_from', 'reserved_to', 'vehicle_image']
