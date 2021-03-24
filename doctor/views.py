from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from .forms import *
from .models import *
from appointment.models import *
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
import datetime

@login_required
def my_appointment(request)
    my_appoints = Appointment.objects.filter(doctor_id = request.user.id)
    coming_appointments = my_appoints.filter(time > datetime.datetime.now())
    completed = my_appoints.filter(time < datetime.datetime.now())



