from django.shortcuts import render

# Create your views here.
def renderfirst(request):
    return render(request,"Home/first.html")