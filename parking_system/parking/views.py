from django.shortcuts import render, redirect
from django.utils import timezone
from .models import ParkingSpot, Reservation
from .forms import ReservationForm

def format_duration(duration):
    days = duration.days
    hours, remainder = divmod(duration.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{days} gün, {hours} saat, {minutes} dakika"

def index(request):
    return render(request, 'index.html')

def reserve_view(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST, request.FILES)  # request.FILES ile dosya yüklemesini alıyoruz
        if form.is_valid():
            reservation = form.save()
            return redirect('confirmation', reservation_id=reservation.id)
    else:
        form = ReservationForm()
    return render(request, 'reserve.html', {'form': form})

def check_time_view(request):
    remaining_time = None
    spot_number = None
    formatted_remaining_time = None
    if request.method == 'POST':
        plate_number = request.POST.get('plate_number')
        try:
            reservation = Reservation.objects.filter(plate_number=plate_number).latest('reserved_to')
            remaining_time = reservation.reserved_to - timezone.now()
            spot_number = reservation.spot.spot_number
            formatted_remaining_time = format_duration(remaining_time)
        except Reservation.DoesNotExist:
            remaining_time = None
    return render(request, 'check_time.html', {'remaining_time': formatted_remaining_time, 'spot_number': spot_number})

def confirmation_view(request, reservation_id):
    try:
        reservation = Reservation.objects.get(id=reservation_id)
    except Reservation.DoesNotExist:
        reservation = None
    return render(request, 'confirmation.html', {'reservation': reservation})
