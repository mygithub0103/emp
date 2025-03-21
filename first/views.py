from django.shortcuts import render
from .models import Employee

# # Create your views here.
# from django.http import HttpResponse

# def index(request):
#     return HttpResponse("welcome to  the first application   >>>>>>  مرحبًا بك في التطبيق الأول!")
   

# def index2(request):
#     return HttpResponse("welcome to  the second application   >>>>>>  مرحبًا بك في التطبيق الثاني!")
   
# def index3(request):
#     return HttpResponse("welcome to  the third application   >>>>>>  مرحبًا بك في التطبيق االثالث!")
# def index4(request):
#     return HttpResponse("welcome to the fourth application")

# def index5(request):
#     return HttpResponse("welcome to fifth application")
# def index6(request):
#     return HttpResponse ("welcome  haider to  six application")

# def index7(request):
#     return HttpResponse("welcome to sever  application")
    

# from django.shortcuts import render
# from .models import Employee

# # def employee_list(request):
# #     employees = Employee.objects.all()  # جلب جميع الموظفين
# #     return render(request, 'employee_list.html', {'employees': employees})

# from django.shortcuts import render, redirect
# from .models import Employee
# from .forms import EmployeeForm

def employee_list(request):
    employees = Employee.objects.all()
    
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')  # إعادة تحميل الصفحة بعد الحفظ
    
    else:
        form = EmployeeForm()

    return render(request, 'employee_list.html', {'employees': employees, 'form': form})









   

# # def add_numbers(request, a, b):
# #     result = a + b
# #     return HttpResponse(f"المجموع: {result}")

# # def add_numbers(request, a, b):
# #     try:
# #         # تحويل النصوص إلى أرقام لإجراء عملية الجمع
# #         num1 = float(a)
# #         num2 = float(b)
# #         result = num1 + num2
# #         return HttpResponse(f"المجموع: {result}")
# #     except ValueError:
# #         return HttpResponse("الرجاء إدخال أرقام صحيحة في الرابط.")

# # from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# # from django.urls import reverse_lazy
# # from .models import Employee

# # # عرض قائمة الموظفين
# # class EmployeeListView(ListView):
# #     model = Employee
# #     template_name = 'employees/employee_list.html'
# #     context_object_name = 'employees'  # المتغير الذي سيتم تمريره للقالب

# # # عرض تفاصيل موظف واحد
# # class EmployeeDetailView(DetailView):
# #     model = Employee
# #     template_name = 'employees/employee_detail.html'
# #     context_object_name = 'employee'

# # # إضافة موظف جديد
# # class EmployeeCreateView(CreateView):
# #     model = Employee
# #     fields = ['first_name', 'last_name', 'job_title', 'salary', 'hire_date', 'email', 'phone', 'department']
# #     template_name = 'employees/employee_form.html'
# #     success_url = reverse_lazy('employee_list')  # يعيد التوجيه لقائمة الموظفين بعد الإضافة

# # # تعديل بيانات موظف
# # class EmployeeUpdateView(UpdateView):
# #     model = Employee
# #     fields = ['first_name', 'last_name', 'job_title', 'salary', 'hire_date', 'email', 'phone', 'department']
# #     template_name = 'employees/employee_form.html'
# #     success_url = reverse_lazy('employee_list')

# # # حذف موظف
# # class EmployeeDeleteView(DeleteView):
# #     model = Employee
# #     template_name = 'employees/employee_confirm_delete.html'
# #     success_url = reverse_lazy('employee_list')



from django.shortcuts import render, redirect
from .models import AuditRecord
from .forms import AuditRecordForm

def audit_list(request):
    audits = AuditRecord.objects.all()
    expired_audits = [audit for audit in audits if audit.is_expired()]  # التحقق من التدقيقات المنتهية

    if request.method == "POST":
        form = AuditRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('audit_list')

    else:
        form = AuditRecordForm()

    return render(request, 'audit_list.html', {'audits': audits, 'form': form, 'expired_audits': expired_audits})



