from django.db import models
from patient.models import Patient
from doctor.models import Doctor

class Appointment(models.Model):
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    reason = models.CharField()
    time= models.DateTimeField()

    def __str__(self):
        return self.patient.username + "at" + self.time
    
