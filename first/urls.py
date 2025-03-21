from django.urls import path
from . import views    
from .views import audit_list, employee_list


 
from .views import employee_list, audit_list
# from .views import EmployeeListView, EmployeeDetailView, EmployeeCreateView, EmployeeUpdateView, EmployeeDeleteView

urlpatterns = [
    path('', views.index, name='index'),
    path('second/', views.index2, name='index2'),
    path('third/', views.index3, name='index3'),
    path('fourth/', views.index4, name='index4'),
    path('fifth/',views.index5, name='inedex5'),
    # path('add/<int:a>/<int:b>/', views.add_numbers, name='add_numbers'),
    #path('add/<str:a>/<str:b>/', views.add_numbers, name='add_numbers'),
    path('six/',views.index6, name='inedex6'),
    path('seven/',views.index7, name='index7'),
     #path('firstemployee/', employ_list, name='employ_lis'),

 
  # تأكد من أن audit_list موجود

 
    path('audits/', audit_list, name='audit_list'),
    path('employees/', employee_list, name='employee_list'),
 


 

 
   # path('employees/', employee_list, name='employee_list'),


    



    #path('sum/', views.sum_two_numbers, name='sum_two_numbers'),



    

    # path('employees/', EmployeeListView.as_view(), name='employee_list'),           # عرض قائمة الموظفين
    # path('employees/<int:pk>/', EmployeeDetailView.as_view(), name='employee_detail'),  # عرض موظف معين
    # path('employees/add/', EmployeeCreateView.as_view(), name='employee_add'),       # إضافة موظف جديد
    # path('employees/<int:pk>/edit/', EmployeeUpdateView.as_view(), name='employee_edit'),  # تعديل بيانات موظف
    # path('employees/<int:pk>/delete/', EmployeeDeleteView.as_view(), name='employee_delete'),  # حذف موظف
]

    
 
