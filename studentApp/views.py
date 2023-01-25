from django.shortcuts import render

from .models import Student 
from  .forms import StudentForm 
from django.contrib import messages

# from django.views.generic import ListView, CreateView, UpdateView,DeleteView, TemplateView,DetailView
from django.views.generic import *

from django.urls import reverse,reverse_lazy
from django.conf import settings 


# Create your views here.
class StudentListView(ListView):
    model= Student
    # context_object_name='students'

    template_name="studentApp/listStudent.html"
    queryset= Student.objects.all()

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context["title"]='Student List'
        return context

class StudentCreateView(CreateView):
    model= Student
    form_class = StudentForm
    template_name = "studentApp/studentForm.html"

    def get_success_url(self):
        messages.add_message(self.request, messages.INFO,'New Student Saved')
        return reverse("list_student")

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context["title"]='Student List'
        context["heading"] = 'Create New Student'
        return context
    

class StudentUpdateView(UpdateView):
    model= Student
    form_class = StudentForm
    template_name = "studentApp/studentForm.html"

    def get_success_url(self):
        messages.success(self.request,'Student has been updated')
        return reverse("list_student")

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context["title"]='Edit Student'
        context["heading"] = 'Update Student'
        return context

class StudentDeleteView(DeleteView):
    model= Student
    # form_class = StudentForm
    template_name = "studentApp/deleteStudent.html"
    # success_url = reverse_lazy('list_student')

    def get_success_url(self):
        messages.success(self.request,'Student has been deleted')
        return reverse("list_student")

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context["title"]='Delete Student'
        context["heading"] = 'Delete Student'
        return context


class StudentDetailView(DetailView):
    model = Student
   
    template_name = "studentApp/detailStudent.html"


    