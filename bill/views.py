from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from .forms import *
from .models import *
from appointment.models import *
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

def generate_bill(request)
    