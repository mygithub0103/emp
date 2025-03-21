from django.shortcuts import render


# Create your views here.

from .models import Clas
def Clas_list(request):
    classes = Clas.objects.all()
    return render(request, 'classes/classes_list.html', {'classes': classes})