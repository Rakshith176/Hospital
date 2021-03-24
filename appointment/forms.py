from django.forms import ModelForm
from appointment.models import Appointment

# Create the form class.
class Patient_Appointment(ModelForm):
    class Meta:
       model = Appointment
        fields = ['reason']

class Confirm_Appointment(ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient_id','doctor_id','reason','status','time']