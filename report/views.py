from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from .forms import *
from .models import *
from appointment.models import *
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

@login_required
def create_report(request)
    form = new_report(request.post)
    if request.method = 'POST':


def close_report(request,pk)
    report = Report.objects.get(id= pk)
    if request.user.is_superuser:
        if report.closed_on = NULL
            report.closed_on = datetime.datetime.now()
            report.save()
            messages.success(request, f'Report closed, Generate bill if needed')
            return redirect('')
        else:
            messages.warning(request, f'Report already closed')
            return redirect('')
    else:
        messages.warning(request, f'Request denied')
        return redirect('')


