from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def displayquote(request):
    return HttpResponse("The best Investment we can make is in ourself.")