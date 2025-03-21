from django.urls import path
from .views import Wensdey_list 

urlpatterns = [
    path(' ', Wensdey_list, name='Wensdey_list'),
]
