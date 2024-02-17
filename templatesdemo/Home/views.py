from django.shortcuts import render

# Create your views here.
def renderfirst(request):
    mydict={"name":"Rahul"}
    return render(request,"Home/first.html",context=mydict)

def renderEmployee(request):
    arg={"name":"Rahul","post":"SI","salary":40800}
    return render(request,"Home/employee.html",arg)