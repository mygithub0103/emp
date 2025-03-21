from django.shortcuts import render

 


# Create your views here.

from .models import Husband
def Amjed_list(request):
    amjed = Husband.objects.all()
    return render(request, 'amjed/amjed_list.html', {'amjed': amjed})