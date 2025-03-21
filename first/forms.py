# from django import forms
# from .models import Employee

# class EmployeeForm(forms.ModelForm):
#     class Meta:
#         model = Employee
#         fields = ['first_name', 'last_name', 'job_title', 'salary', 'hire_date', 'email', 'phone', 'department']
#         widgets = {
#             'hire_date': forms.DateInput(attrs={'type': 'date'}),
#         }


from django import forms
from .models import AuditRecord

class AuditRecordForm(forms.ModelForm):
    class Meta:
        model = AuditRecord
        fields = ['order_number', 'order_date', 'audited_entity', 'start_date', 'end_date']
        widgets = {
            'order_date': forms.DateInput(attrs={'type': 'date'}),
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

