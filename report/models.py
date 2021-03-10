from django.db import models
from patient.models import Patient

class Report(models.Model):
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    description = models.TextField()
    opened_on = models.DateField()
    closed_on = models.DateField()

    def __str__(self):
        return self.patient.username + "report:" + self.description
    