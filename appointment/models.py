from django.db import models
from patient.models import Patient
from doctor.models import Doctor


application_status=(
  ('none','NONE'),
  ('pending','PENDING'),
  ('booked','BOOKED'),
  ('cancelled','CANCELLED'),
)
class Appointment(models.Model):
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    reason = models.CharField(max_length=200)
    status =  models.CharField(choices =application_status,default = 'none',max_length = 10)
    time= models.DateTimeField(unique=True)

    def __str__(self):
        return '{} at {}'.format(self.patient_id,self.time)
    
