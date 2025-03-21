from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Player

class PlayerListView(ListView):
    model = Player
    template_name = 'players/player_list.html'
    context_object_name = 'players'

class PlayerCreateView(CreateView):
    model = Player
    template_name = 'players/player_form.html'
    fields = ['first_name', 'last_name', 'age', 'team', 'position']
    success_url = reverse_lazy('player_list')
