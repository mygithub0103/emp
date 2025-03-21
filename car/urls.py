

from django.urls import path
from .views import cars_list,input,show

urlpatterns = [
    path('car/', cars_list, name='cars_list'),
    path('input/', input, name='input'),
     path(' ', show, name='show'),
]
