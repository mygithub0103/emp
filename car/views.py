from django.shortcuts import render
from . import views

#Create your views here.
from .models import Cars
def cars_list(request):
   car = Cars.objects.all()
   return render(request, 'car/car_list.html', {'car': car})



from django.shortcuts import render, redirect
from .forms import CarsForm

def input(request):
    if request.method == "POST":
        form = CarsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('input')  # يمكنك تغييره لصفحة تأكيد أو قائمة السيارات
    else:
        form = CarsForm()
    
    return render(request, 'car/input.html', {'form': form})



from django.shortcuts import render
from .models import Cars

def show(request):
   car = Cars.objects.filter(year=2020)  # جلب السيارات الأحدث من 2020
   return render(request, 'car/show.html', {'show': show})



from django.shortcuts import render
from .models import Cars

def list(request):
   num = Cars.objects.count()  # حساب عدد السيارات المدخلة
   return render(request, 'car/list.html', {'عدد_السيارات': عدد_السيارات})


