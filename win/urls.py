from django.urls import path
from .views import search_employees

urlpatterns = [
    path('search/', search_employees, name='search_employees'),
]
