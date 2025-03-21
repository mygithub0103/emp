from django.shortcuts import render

# Create your views here.
 
from .models import Employee

def employee_list(request):
   employees = Employee.objects.all()
   return render(request, 'employees/employee_list.html', {'employees': employees})




from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm

def employee_create(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')  # يعيد التوجيه إلى صفحة عرض الموظفين
    else:
        form = EmployeeForm()
    
    return render(request, 'employees/employee_form.html', {'form': form})
