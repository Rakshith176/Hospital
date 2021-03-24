from django.forms import ModelForm
from bill.models import Appointment

# Create the form class.
class Generate_Bill(ModelForm):
    class Meta:
       model = Bill
        fields = ['reason']