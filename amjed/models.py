from django.db import models

# Create your models here.
class Husband(models.Model):
    wife = models.CharField(max_length=100)
    son= models.CharField(max_length=100)
    year = models.DecimalField(max_digits=10, decimal_places=2)
    

    def __str__(self):
        return self.wife