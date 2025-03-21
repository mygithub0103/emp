from django.db import models
from django.db.models import Q

class Employee(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return self.name

    def similar_names(self, search_term):
        return Employee.objects.filter(Q(name__icontains=search_term))
