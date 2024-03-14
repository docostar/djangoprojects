from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from cbvApp.models import Student
from django.urls import reverse_lazy
# Create your views here.

class StudentListView(ListView):
    model = Student
    #default template name is 'student_list.html'
    #default context_objectname is 'student_list'

class StudentDetailView(DetailView):
    model = Student
    #default template name is 'student_detail.html'
    #default context_objectname is 'student'

class StudentCreateView(CreateView):
    model = Student
    fields = ['firstName','lastName','testScore']
    #default template name is 'student_form.html'

class StudentUpdateView(UpdateView):
    model = Student
    fields = ['testScore']

class StudentDeleteView(DeleteView):
    model = Student
    success_url=reverse_lazy('students')
    #default template name is 'student_confirm_delete.html'