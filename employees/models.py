from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    hire_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name
    



    

