from django.db import models

# Create your models here.
class Clas(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    year = models.DecimalField(max_digits=10, decimal_places=2)
    hire_date = models.DateField()

    def __str__(self):
        return self.name