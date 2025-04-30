from django.shortcuts import render
from .models import *

def aadhar(request):
    data=Aadhar.objects.all()
    print(data.values())

# Create your views here.
