from django.shortcuts import render

# Create your views here.

  
from .models import Peop

def People_list(request):
    peoples = Peop.objects.all()
    return render(request, 'people/people_list.html', {'people': peoples})

