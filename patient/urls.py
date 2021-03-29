from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/',views.register_patient,name='register-patient'),
    path('book_appointment/',views.book_appointment,name='book-appointment'),
    path('my_appointments/',views.my_appointments,name='patient-appointment'),
    path('my_reports/',views.my_reports,name='patient-report'),
    path('my_bill/<int:pk>',views.my_bill,name='patient-bill'),
]