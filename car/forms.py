from django import forms
from .models import Cars

class CarsForm(forms.ModelForm):
    class Meta:
        model = Cars
        fields = ['name', 'color', 'year', 'hire_date']