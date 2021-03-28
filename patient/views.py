from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from patient.forms import *
from .models import *
from .forms import *
from appointment.models import *
from appointment.forms import *
from report.models import *
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
import datetime,csv

def home(request):
    is_patient = Patient.objects.get(user_id = request.user.id)
    return render(request,'index.html',locals())


def register_patient(request):
    if request.method == 'POST':
        form = Patient_register(request.POST)
        profile_form = Patient_Profile(request.POST)
        if form.is_valid():
            user = form.save()
            profile = profile_form.save(commit = False)
            profile.user = user
            profile.save()
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = Patient_register()
        profile_form = Patient_Profile()
    return render(request, 'patient/register.html', locals())
     
@login_required
def book_appointment(request):
    if request.method == 'POST':
        book = Patient_Appointment(request.POST)
        check = Appointment.objects.filter(status = 'pending')
        check = check.filter(patient_id = request.user.id)
        if check:
            reason = book.cleaned_data['reason']
            new_appointment = Appointment()
            new_appointment.patient_id = request.user.id
            new_appointment.status = 'pending'
            new_appointment.reason = reason
            new_appointment.save()
            messages.success(request, f'Asked for appointment. Keep checking for your timings')
            return redirect('home')
        else:
            messages.error(request,f'Wait for your previous appointment to be confirmed')
            return redirect('home')
    else:
        book = Patient_Appointment()
    return render(request,'patient/book_appointment.html',locals())


@login_required
def my_appointments(request):
    booked_appointments = Appointment.objects.filter(status = 'booked')
    booked_appointments = booked_appointments.filter(patient_id = request.user.id)
    pending_appointments = Appointment.objects.filter(status = 'pending')
    pending_appointments =  pending_appointments.filter(patient_id = request.user.id)


@login_required
def my_reports(request):
    report = Report.objects.filter(patient_id= request.user.id)