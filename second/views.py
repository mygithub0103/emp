from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm

import pandas as pd
from django.http import HttpResponse
from .models import Employee,Student


def employee_list(request):
    employees = Employee.objects.all().order_by('-id')[:10]
    return render(request, 'second/employee_list.html', {'employees': employees})

def add_employee(request):
    form = EmployeeForm()
    success_message = None

    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            success_message = "   تمت الاضافة بنجاح   " 
            form = EmployeeForm()  # إعادة تعيين الحقول إلى فارغة

    return render(request, 'second/add_employee.html', {'form': form, 'success_message': success_message})






def upload_employees(request):
    if request.method == "POST" and request.FILES.get("excel_file"):
        excel_file = request.FILES["excel_file"]
        try:
            # قراءة ملف الإكسل وتحويله إلى DataFrame
            df = pd.read_excel(excel_file)

            # التحقق من الأعمدة المطلوبة
            required_columns = {"name", "job_title", "grade", "salary"}
            if not required_columns.issubset(df.columns):
                return HttpResponse("ملف الإكسل غير متوافق! يجب أن يحتوي على الأعمدة: name, job_title, grade, salary")

            # إدخال البيانات في قاعدة البيانات
            for _, row in df.iterrows():
                Employee.objects.create(
                    name=row["name"],
                    job_title=row["job_title"],
                    grade=row["grade"],
                    salary=row["salary"]
                )

            return redirect("employee_list")

        except Exception as e:
            return HttpResponse(f"حدث خطأ أثناء رفع الملف: {e}")

    return redirect("employee_list")


def export_employees_to_excel(request):
    # جلب جميع بيانات الموظفين
    employees = Employee.objects.all().values('name', 'job_title', 'grade', 'salary')

    # تحويل البيانات إلى DataFrame
    df = pd.DataFrame(list(employees))

    # إنشاء ملف إكسل في الذاكرة
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=employees.xlsx'

    # حفظ البيانات في ملف Excel
    with pd.ExcelWriter(response, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Employees')

    return response

def employee_list(request):
    query = request.GET.get('q', '')  # الحصول على قيمة البحث

    if query:
        employees = Employee.objects.filter(name__icontains=query).order_by('-id')[:10]
    else:
        employees = Employee.objects.all().order_by('-id')[:10]

    return render(request, 'second/employee_list.html', {'employees': employees, 'query': query})


def student_list(request):
    students = Student.objects.all().order_by('-id')[:10]
    return render(request, 'second/student_list.html', {'students': students})

def upload_student(request):
    if request.method == "POST" and request.FILES.get("excel_file"):
        excel_file = request.FILES["excel_file"]
        try:
            # قراءة ملف الإكسل وتحويله إلى DataFrame
            df = pd.read_excel(excel_file)

            # التحقق من الأعمدة المطلوبة
            required_columns = {"name", " student_id", "major"}
            if not required_columns.issubset(df.columns):
                return HttpResponse("ملف الإكسل غير متوافق! يجب أن يحتوي على الأعمدة: name, job_title, grade, salary")

            # إدخال البيانات في قاعدة البيانات
            for _, row in df.iterrows():
                student_list.objects.create(
                    name=row["name"],
                    student_id=row["student_id"],
                    major=row["major"],
                    
                )

            return redirect("employee_list")

        except Exception as e:
            return HttpResponse(f"حدث خطأ أثناء رفع الملف: {e}")
