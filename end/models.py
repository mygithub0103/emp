from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gpa = models.FloatField()

    def is_eligible(self):
        return self.age >= 18 and self.gpa >= 2.5

    def __str__(self):
        return self.name
