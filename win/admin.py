 
 

from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'salary')

admin.site.register(Employee, EmployeeAdmin)
