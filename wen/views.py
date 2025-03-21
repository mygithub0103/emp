from django.shortcuts import render

# Create your views here.
from .models import Wensdey
def Wensdey_list(request):
    information= Wensdey.objects.all()
    return render(request, 'wen/wensdey_list.html', {'wen': information})