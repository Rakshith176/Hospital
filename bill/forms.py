from django.forms import ModelForm
from bill.models import Bill

# Create the form class.
class Generate_Bill(ModelForm):
    class Meta:
       model = Bill
       fields = ['amount','bill_details']