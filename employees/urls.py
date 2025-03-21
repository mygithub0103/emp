#from django.urls import path
#from .views import employee_list

#urlpatterns = [
  #  path('employees/', employee_list, name='employee_list'),
#]



from django.urls import path
from .views import employee_create, employee_list

urlpatterns = [
    path('employees/add/', employee_create, name='employee_create'),
    path('employees/', employee_list, name='employee_list'),
]
