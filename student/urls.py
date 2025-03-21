from django.urls import path
from .views import  register_animals, CreateAnimal

urlpatterns = [
    # path('register/', register_animals, name='register_animals'),
    path('register/', CreateAnimal.as_view(), name='register_animals'),
]
