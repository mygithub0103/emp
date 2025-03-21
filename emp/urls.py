"""
URL configuration for emp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
   path('second/', include('second.urls')),
    #path('nodody/', include('nodody.urls')),

    

    


   # path('first/', include('first.urls')),  # ربط التطبيق
#path('first/second/', include('first.urls')),  # ربط التطبيق


    
#     path('', include('employees.urls')),
#     path('', include('classes.urls')),
    
#     path('', include('employees/add.urls'))
#    # path('', include('people.urls')),
#     # path('', include('car.urls')),
#     # path(' ',include('show.urls')),

#     # path('win/', include('win.urls')),
#     # path('', include('amjed.urls')),
#     #  path('wen/', include('wen.urls')),
#     # path('student/', include('student.urls')),
#     # path('app/', include('app.urls')),  # إضافة مسار التطبيق

  
    
#     path('play/', include('play.urls')),  # إضافة التطبيق play
]



