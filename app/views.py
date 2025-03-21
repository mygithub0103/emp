
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Customer, Driver, Student2, Worker,Player
from django.views.generic import DetailView, ListView

class CustomerListView(View):
    def get(self, request):
        customers = Customer.objects.all()  # استرجاع جميع الزبائن
        drivers = Driver.objects.all()
        student2s=Student2.objects.all
        workers=Worker.objects.all()
        players = Player.object.all()
        return render(request, 'app/customer_list.html', {'customers': customers,
                                                          'drivers':drivers, student2s:student2s, 'workers':workers})

class CustomerDetailView(View):
    def get(self, request, pk):
        customer = get_object_or_404(Customer, pk=pk)  # الحصول على زبون حسب الـ id
        return render(request, 'app/customer_detail.html', {'customer': customer})
    


from django.views.generic import DeleteView
from django.urls import reverse_lazy
from .models import Worker

class WorkerDeleteView(DeleteView):
    model = Worker
    template_name = 'worker_confirm_delete.html'  # صفحة التأكيد
    success_url = reverse_lazy('worker_list')  # بعد الحذف يعود إلى قائمة الموظفين

    
class DriverDetailview(DetailView):
    model= Driver
    template_name="app/driver_detail.html"

 

class StudentListView(ListView):
    model = Student2
    template_name = 'student_list.html'  # ملف القالب لعرض البيانات
    #context_object_name = 'students'

    

  
    

# class DriverListView(View):
#     def get(self, request):
#         drivers = Driver.objects.all()  # استرجاع جميع الزبائن
#         return render(request, 'app/customer_detail.html', {'Drivers': Driver})


