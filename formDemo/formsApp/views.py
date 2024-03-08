from django.shortcuts import render
from . import forms

# Create your views here.
def UserRegistrationView(request):
    form=forms.UserRegistrationForm()
    return render(request,'formsApp/userRegistration.html',{'form':form})

