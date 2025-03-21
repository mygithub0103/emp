from django.db import models

# Create your models here.
from django.db import models

class Player(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="الاسم الأول")
    last_name = models.CharField(max_length=50, verbose_name="الاسم الأخير")
    age = models.PositiveIntegerField(verbose_name="العمر")
    team = models.CharField(max_length=100, verbose_name="الفريق")
    position = models.CharField(max_length=50, verbose_name="المركز")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإضافة")

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "لاعب"
        verbose_name_plural = "اللاعبون"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
