from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    grade = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


 

class Student(models.Model):
    name = models.CharField(max_length=100)  # اسم الطالب
    student_id = models.CharField(max_length=20, unique=True)  # رقم الطالب
    major = models.CharField(max_length=100)  # التخصص

    def __str__(self):
        return self.name
