from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView

from ourhockey_playermanager.models import Player

# Add logging
import logging
from rest_framework.urls import template_name
logger = logging.getLogger(__name__)

class PlayerListView(ListView):
    template_name = 'players/player_list.html'
    context_object_name = 'players_list'
    
    def get_queryset(self):
        return Player.objects.order_by('-birthday')[:5]
    
class PlayerDetailView(DetailView):
    model = Player