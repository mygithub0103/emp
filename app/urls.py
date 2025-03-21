from django.urls import path
from .views import CustomerListView, CustomerDetailView, DriverDetailview,StudentListView, Workerو WorkerDeleteView

urlpatterns = [
    path('', CustomerListView.as_view(), name='customer_list'),  # قائمة الزبائن
    path('customer/', CustomerListView.as_view(), name='customer_list'),  # قائمة الزبائن
    path('customer/<int:pk>/', CustomerDetailView.as_view(), name='customer_detail'),  # تفاصيل الزبون

    path('driver/<int:pk>/', DriverDetailview.as_view(), name='driver_detail'),  # قائمة السواق

    path('student2/', StudentListView.as_view(), name='student_list'),  # قائمة الطلاب

    path('players/', PlayerListView.as_view(), name='palyer_list'),  # قائمة الطلاب



 

# urlpatterns = [
#     path('worker/delete/<int:pk>/', WorkerDeleteView.as_view(), name='worker_delete'),
# ]


    
]
