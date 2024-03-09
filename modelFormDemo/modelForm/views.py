from django.shortcuts import render
from modelForm.models import Project
from  modelForm.forms import ProjectForm
# Create your views here.

def index(request):
    return render(request,'modelForm/index.html')

def listProject(request):
    projectlist = Project.objects.all()
    return render(request, 'modelForm/listproject.html',{'projects':projectlist})

def addProject(request):
    form = ProjectForm
    if request.method=='POST':
        form=ProjectForm(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    return render(request, 'modelForm/addproject.html',{'form':form})