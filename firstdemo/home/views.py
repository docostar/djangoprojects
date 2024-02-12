from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def display(request):
    return HttpResponse("<h1>This is Django ITI App.</h1>")


def displayDateTime(request):
    dt=datetime.datetime.now()
    s="<b>Curren time is:</b>"+ str(dt)
    return HttpResponse(s)