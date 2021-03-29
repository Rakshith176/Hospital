from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('<int:pk>/',views.generate_bill,name='create-bill'),
]