from django.db import models

#
# Create your models here.
class workshops(models.Model):
    holle = models.CharField(max_length=100)
    employees= models.CharField(max_length=100)
    day = models.DecimalField(max_digits=10, decimal_places=2)
    

    def __str__(self):
        return self.holle