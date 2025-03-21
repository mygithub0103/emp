from django.shortcuts import render
from django.views.generic import CreateView
# Create your views here.
from django.shortcuts import render, redirect
from .models import Student, Animals

# def register_student(request):
#     if request.method == 'POST':
#         full_name = request.POST['full_name']
#         college_name = request.POST['college_name']
#         average = float(request.POST['average'])
#         department = request.POST['department']
#         branch = request.POST['branch']

#         student = Student(full_name=full_name, college_name=college_name, average=average,department=department, branch=branch)
#         print(student)
#         if student.is_admitted():
#             student.save()
#             message = "تم تسجيل الطالب بنجاح."  #+student.smart()+student.dep()
#         else:
#             message = "غير مسموح لك التسجيل." #+student.smart()

#         return render(request, 'student/register.html', {'message': message})

#    return render(request, 'student/register.html')



class CreateAnimal(CreateView):
    model = Animals
    template_name = "student/register.html"
    fields = '__all__'

def register_animals(request):
    if request.method == 'POST':
        name = request.POST['name']
        food = request.POST['food']
        legs = float(request.POST['legs'])
        animals = Animals(name=name, food=food, legs=legs)
        print(animals)
        res = animals.choose()
        if res:
            animals.save()
            message = res  
        else:
            message = "غير مسموح لك التسجيل." 

        return render(request, 'student/register.html', {'message': res})

    return render(request, 'student/register.html')

