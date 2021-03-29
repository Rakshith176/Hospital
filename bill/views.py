from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from .forms import *
from .models import *
import datetime
from django.contrib.auth.decorators import login_required

@login_required
def generate_bill(request,pk):
   if request.user.is_superuser:
      report = Report.objects.get(id=pk)
      check = Bill.objects.filter(report_id = report.id).exists()
      if not check:
            if request.method == POST:
                  bill_form = Generate_Bill(request.POST)
                  if bill_form.is_valid():
                        amount = bill_form.cleaned_data['amount']
                        details = bill_form.cleaned_data['bill_details']
                        bill = Bill()
                        bill.report_id = report.id
                        bill.patient_id = report.patient_id
                        bill.amount = amount
                        bill.bill_details = details
                        bill.bill_generated_on = datetime.datetime.now()
                        bill.save()
                        messages.success(request, f'Bill generated successfully, go to admin portal to check payment status')
                        return redirect('all-reports')
            else:
                  bill_form = Generate_Bill()
            return render(request,'admin/generate_bill.html',locals())
      else: 
             messages.warning(request, f'Bill already generated for this report')
             return redirect('all-reports')
   else:
      messages.warning(request, f'Request denied')
      return redirect('home')
   return render(request,'admin/generate_bill.html',locals())
      

      
    