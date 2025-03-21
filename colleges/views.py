from django.shortcuts import render

# Create your views here.

from .models import College
def colleges_list(request):
    colleges = College.objects.all()
    return render(request, 'colleges/colleges_list.html', {'colleges': colleges})