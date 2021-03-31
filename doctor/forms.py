from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class Doctor_register(UserCreationForm):
    email = models.EmailField(null=False,unique=True)

    class Meta:
        model = User
        fields = ('username','email','password1','password2',)
        
    def save(self,commit=True):
        user = super().save(commit = False)

        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user       


class Doctor_Profile(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ('age','specification','contact','is_doctor')
