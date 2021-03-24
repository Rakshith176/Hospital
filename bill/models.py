from django.db import models
from patient.models import Patient
from report.models import Report

class Bill(models.Model):
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    amount = models.IntegerField()
    report_id = models.ForeignKey(Report, on_delete=models.CASCADE)
    bill_generated_on = models.DateField()
    bill_details = models.CharField(max_length=200)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return '{} -> {} on {}'.format(self.patient_id,self.amount,self.bill_date)
    
