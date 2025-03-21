from django.db import models

# Create your models here.
 

class Student(models.Model):
    name = models.CharField(max_length=255, verbose_name="الاسم الكامل")
    student_id = models.CharField(max_length=50, unique=True, verbose_name="رقم الطالب")
    major = models.CharField(max_length=100, verbose_name="التخصص")

    def __str__(self):
        return f"{self.name} - {self.student_id}"

