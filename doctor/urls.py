from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/',views.doctor_register,name='register-doctor'),
    path('my_appointments/',views.my_appointment,name='doctor-appointments'),
]