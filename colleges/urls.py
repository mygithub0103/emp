
from django.urls import path
from .views import colleges_list

urlpatterns = [
    path('colleges/', colleges_list, name='colleges_list'),
]
