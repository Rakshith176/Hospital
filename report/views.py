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
def create_report(request,pk):
    if request.user.is_superuser:
        patient_id = Patient.objects.get(user_id = pk)
        check = Report.objects.filter(patient_id=patient_id).exists()
        if not check:
            if request.method == 'POST':
                form = Create_Report(request.POST)
                if form.is_valid():
                    new_report = Report()
                    new_report.patient_id = patient_id
                    new_report.description = form.cleaned_data['description']
                    new_report.opened_on = datetime.datetime.now()
                    new_report.save()
                    messages.success(request, f'Report created')
                    return redirect('patient-list')          
            else:
                form = Create_Report()
            return render(request,'admin/create_report.html',locals())
        else:
            messages.warning(request, f'There is already a open report for this patient')
            return redirect('patient-list')
    else:
        messages.warning(request, f'Request denied')
        return redirect('home')
    return render(request,'admin/create_report.html',locals())


def close_report(request,pk):
    report = Report.objects.get(id= pk)
    if request.user.is_superuser:
        if report.closed_on == None:
            report.closed_on = datetime.datetime.now()
            report.save()
            messages.success(request, f'Report closed, Generate bill if needed')
            return redirect('all-reports')
        else:
            messages.warning(request, f'Report already closed')
            return redirect('all-reports')
    else:
        messages.warning(request, f'Request denied')
        return redirect('home')

def all_reports(request):
    reports = Report.objects.all()
    return render(request,'admin/all_reports.html',locals())