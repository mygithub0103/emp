from django.db import models

# Create your models here.

 
from datetime import date

class AuditRecord(models.Model):
    order_number = models.CharField(max_length=50, unique=True)  # رقم الأمر الإداري
    order_date = models.DateField()  # تاريخ الأمر الإداري
    audited_entity = models.CharField(max_length=255)  # الجهة الخاضعة للتدقيق
    start_date = models.DateField()  # بداية التدقيق
    end_date = models.DateField()  # نهاية التدقيق

    def is_expired(self):
        return date.today() > self.end_date  # يتحقق إذا انتهت فترة التدقيق

    def __str__(self):
        return f"أمر {self.order_number} - {self.audited_entity}"






class Employee(models.Model):
    first_name = models.CharField(max_length=50)  # الاسم الأول
    last_name = models.CharField(max_length=50)   # الاسم الأخير
    job_title = models.CharField(max_length=100)  # المسمى الوظيفي
    salary = models.DecimalField(max_digits=10, decimal_places=2)  # الراتب
    hire_date = models.DateField()  # تاريخ التعيين
    email = models.EmailField(unique=True)  # البريد الإلكتروني (فريد لكل موظف)
    phone = models.CharField(max_length=15, unique=True)  # رقم الهاتف (فريد)
    department = models.CharField(max_length=100)  # القسم

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.job_title}"

