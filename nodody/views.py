from django.shortcuts import render

# Create your views here.

from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Student

class StudentCreateView(CreateView):
    model = Student
    fields = ['name', 'student_id', 'major']
    template_name = 'student_form.html'  # يجب إنشاء هذا القالب
    success_url = reverse_lazy('student_list')  # يعيد التوجيه بعد الإدخال الناجح

