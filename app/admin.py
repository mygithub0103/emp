# from django.contrib import admin

# # Register your models here.

# from .models import Customer

# admin.site.register(Customer)


from django.contrib import admin
from .models import Customer, Driver,Student2,Worker,Player

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'address', 'created_at')  # عرض الحقول في قائمة الزبائن
    search_fields = ('first_name', 'last_name', 'email')  # إمكانية البحث عن الزبائن

admin.site.register(Customer, CustomerAdmin)  # تسجيل النموذج

class DriverAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'car', 'phone','address', 'created_at')  # عرض الحقول في قائمة الزبائن
    search_fields = ('first_name', 'last_name', 'car')  # إمكانية البحث عن الزبائن

admin.site.register(Driver, DriverAdmin)  # تسجيل النموذج


class Student2Admin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'address', 'created_at')  # عرض الحقول في قائمة الزبائن
    search_fields = ('first_name', 'last_name', 'email')  #  
admin.site.register(Student2, Student2Admin)  # تسجيل النموذج





from django.contrib import admin
from .models import Worker

class WorkerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'created_at')  # عرض الأعمدة في لوحة الإدارة
    search_fields = ('first_name', 'last_name', 'email')  # إضافة البحث
    list_filter = ('created_at',)  # إضافة فلتر حسب تاريخ الإضافة
    ordering = ('-created_at',)  # ترتيب تنازلي حسب الأحدث

admin.site.register(Worker, WorkerAdmin)  # تسجيل النموذج



class PlayerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'created_at')  # عرض الأعمدة في لوحة الإدارة
    search_fields = ('first_name', 'last_name', 'email')  # إضافة البحث
    list_filter = ('created_at',)  # إضافة فلتر حسب تاريخ الإضافة
    ordering = ('-created_at',)  # ترتيب تنازلي حسب الأحدث

admin.site.register(Player, PlayerAdmin)  # تسجيل النموذج

