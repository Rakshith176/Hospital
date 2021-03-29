from django.forms import ModelForm
from report.models import Report

# Create the form class.
class Create_Report(ModelForm):
    class Meta:
        model = Report
        fields = ['description']