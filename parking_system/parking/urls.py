from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('reserve/', views.reserve_view, name='reserve'),
    path('check_time/', views.check_time_view, name='check_time'),
    path('confirmation/<int:reservation_id>/', views.confirmation_view, name='confirmation'),  # Rezervasyon ID'si ile URL
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
