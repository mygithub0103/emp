from django.urls import path
from .views import People_list 

urlpatterns = [
    path('people/', People_list, name='People_list'),
]
