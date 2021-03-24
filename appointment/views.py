from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from .forms import *
from .models import *
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
import datetime,csv


@login_required
def appointments(request,pk)
    obj = Appointment.objects.get(id= pk)
    if request.user.is_superuser:
        form = Add_appointment(instance = obj)
         if request.method == 'POST':
              form = Add_appointment(data = request.POST, instance = obj)
            if form.is_valid():
                obj = form.save(commit = False)
                obj.status = 'booked'
                
                obj.save()
                messages.success(request, f'Book has been updated')
                return redirect('all_books')
                

