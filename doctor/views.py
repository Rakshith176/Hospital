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
def my_appointment(request):
    my_appoints = Appointment.objects.filter(doctor_id = request.user.id)
    coming_appointments = my_appoints.filter( time__lte= datetime.datetime.now() )
    completed = my_appoints.filter(time__gte = datetime.datetime.now())
    return render(request,'doctor/appointments.html',locals())

def doctor_register(request):
    if request.method == 'POST':
        form = Doctor_register(request.POST)
        profile_form = Doctor_Profile(request.POST)
        check_key = check_doctor(request.POST)
        if form.is_valid() and profile_form.is_valid():
            if check_key.cleaned_data['special_key'] == 'Special-Key':
                user = form.save()
                profile = profile_form.save(commit = False)
                profile.user = user
                profile.save()
                messages.success(request, f'Your account has been created! You are now able to log in')
                return redirect('register-doctor')
            else:
                messages.error(request, f'You have not verified special key correctly')
                return redirect('register-doctor') #doctor-register page
    else:
        form = Doctor_register()
        profile_form = Doctor_Profile()
    return render(request, 'doctor/register.html', locals()) #template name doctor/register.html

