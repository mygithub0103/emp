from django.urls import path
from .views import PlayerListView, PlayerCreateView

urlpatterns = [
    path('', PlayerListView.as_view(), name='player_list'),
    path('add/', PlayerCreateView.as_view(), name='player_add'),
]
