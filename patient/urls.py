from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/',views.register_patient,name='register-patient'),
    path('book_appointment',views.book_appointment,name='book-appointment'),
]