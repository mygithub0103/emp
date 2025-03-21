

from django.urls import path
from .views import Amjed_list


urlpatterns = [
    path('amjed/', Amjed_list, name='Amjed_list'),
   
]
