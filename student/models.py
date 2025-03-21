from django.db import models

#Create your models here.
from django.db import models

class Student(models.Model):
    full_name = models.CharField(max_length=100)
    college_name = models.CharField(max_length=100)
    average = models.FloatField()
    department=models.CharField(max_length=100, blank=True, null=True)
    branch = models.CharField(max_length=100 , blank=True, null=True)

    def __str__(self):
        return self.full_name

    def is_admitted(self):
        if self.college_name == "الطب" and self.average > 95 and self.branch =="العلمي":
            return True
        elif self.college_name == "الهندسة" and self.average > 85   and self.branch =="العلمي":
            return True
        elif self.college_name == "القانون" and self.average > 80 and self.branch=="الادبي":
            return True
        return False
    def smart(self):
        if self.average== 100:
            return "smart"
        elif self.average==50:
            return "stupid student"
     
        elif self.average <80: 
            return "no college excepted"

        return ''
    def dep(self):
        if self.college_name=="القانون" or self.college_name=="الهندسة" or self.college_name=="الطب":
            return  "عليك  بتقديم طلب  لاختيار القسم المطلوب "

class  Animals(models.Model):
    name = models.CharField(max_length=100)
    food=models.CharField(max_length=100)
    legs = models.FloatField()
   
    def __str__(self):
        return self.name
    

    def choose(self):
        if self.name == "اسد":  
            return "حيوان قوي  جدا"
            
        elif self.name == "كلب":
            return  "pet animals"
           
        return False