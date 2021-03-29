from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('create/<int:pk>',views.create_report,name='create-report'),
    path('all',views.all_reports,name='all-reports'),
    path('close/<int:pk>',views.close_report,name='close-report'),
]