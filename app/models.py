from django.db import models

# Create your models here.


class Customer(models.Model):
    first_name = models.CharField(max_length=50)  # الاسم الأول
    last_name = models.CharField(max_length=50)   # الاسم الأخير
    email = models.EmailField(unique=True)        # البريد الإلكتروني
    phone = models.CharField(max_length=15)       # رقم الهاتف
    address = models.TextField()                  # العنوان
    created_at = models.DateTimeField(auto_now_add=True)  # تاريخ الإضافة

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Driver(models.Model):
    first_name = models.CharField(max_length=50)  # الاسم الأول
    last_name = models.CharField(max_length=50)   # الاسم الأخير
    car = models.CharField(max_length=50) 
    phone = models.CharField(max_length=15)       # رقم الهاتف
    address = models.TextField()                  # العنوان
    created_at = models.DateTimeField(auto_now_add=True)  # تاريخ الإضافة

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.car}"

class Worker(models.Model):
    first_name = models.CharField(max_length=50)  # الاسم الأول
    last_name = models.CharField(max_length=50)   # الاسم الأخير
    email = models.EmailField(unique=True)        # البريد الإلكتروني
    phone = models.CharField(max_length=15)       # رقم الهاتف
    address = models.TextField()                  # العنوان
    created_at = models.DateTimeField(auto_now_add=True)  # تاريخ الإضافة

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


    
class Student2(models.Model):
    first_name = models.CharField(max_length=50)  # الاسم الأول
    last_name = models.CharField(max_length=50)   # الاسم الأخير
    email = models.CharField(max_length=50) 
    phone = models.CharField(max_length=15)       # رقم الهاتف
    address = models.TextField()                  # العنوان
    created_at = models.DateTimeField(auto_now_add=True)  # تاريخ الإضافة

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Player(models.Model):
    first_name = models.CharField(max_length=50)  # الاسم الأول
    last_name = models.CharField(max_length=50)   # الاسم الأخير
    email = models.EmailField(unique=True)        # البريد الإلكتروني
    phone = models.CharField(max_length=15)       # رقم الهاتف
    address = models.TextField()                  # العنوان
    created_at = models.DateTimeField(auto_now_add=True)  # تاريخ الإضافة

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
