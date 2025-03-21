from django.urls import path
from . import views
from .views import export_employees_to_excel
from .views import upload_employees
from .views import employee_list

urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    path('add/', views.add_employee, name='add_employee'),
    path('export/', export_employees_to_excel, name='export_employees'),
    


    path('upload/', upload_employees, name='upload_employees'),
    path('', employee_list, name='employee_list'),
 


]


 

