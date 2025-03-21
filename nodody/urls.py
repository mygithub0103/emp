from django.urls import path
from .views import StudentCreateView
from . import views

urlpatterns = [
  path('add/', StudentCreateView.as_view(), name='student_add'),

 
]


