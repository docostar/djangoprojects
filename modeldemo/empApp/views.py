from django.shortcuts import render
from empApp.models import Employee

# Create your views here.
def employeeData(request):
    empls=Employee.objects.all()
    empDict={"employees":empls}
    return render(request,"empApp/employee.html",empDict)
