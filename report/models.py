from django.db import models
from patient.models import Patient
from django.contrib.auth.models import User

class Report(models.Model):
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    description = models.TextField()
    opened_on = models.DateField()
    closed_on = models.DateField(blank=True,null=True)

    def __str__(self):
        return 'Report of {} opened on {}'.format(self.patient_id,self.opened_on)
    