
from django.urls import path
from .views import Clas_list

urlpatterns = [
    path('classes/', Clas_list, name='Clas_list'),
]
