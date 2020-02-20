from django.shortcuts import render
from .models import *

def Index(requrest):
    qs = WorldBorder.objects.all()
    return render(requrest,'home/index.html',context={'world':qs})