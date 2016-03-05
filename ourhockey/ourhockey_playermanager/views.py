from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView

from ourhockey_playermanager.models import Player
from ourhockey_playermanager.forms import AttendCheckForm

# Add logging
import logging
from rest_framework.urls import template_name
logger = logging.getLogger(__name__)


class PlayerModelView(TemplateView):
    template_name = 'ourhockey_playermanager/index.html'
    
    def get_context_data(self, **kwargs):
        context = super(PlayerModelView, self).get_context_data(**kwargs)
        context['object_list'] = ['player_list']
        return context


class PlayerListView(ListView):
    template_name = 'ourhockey_playermanager/player_list.html'
    context_object_name = 'player_list'
    
    def get_queryset(self):
        return Player.objects.order_by('-birthday')[:5]
    
class PlayerDetailView(DetailView):
    model = Player
    
    
#-- Function-based View
def update_attend(request):
    player_attend_list = []
    
    if request.POST:
        form = AttendCheckForm(request.POST)   
        if form.is_valid():
            for attend in request.POST.getlist('attend'):
               attend_player = get_object_or_404(Player, pk=int(attend))
               attend_player.attend = True
               attend_player.save()
               player_attend_list.append(attend_player)
                
        else:
            logger.debug("update_attend() not form.is_valid()")
            return render(request, 'ourhockey_playermanager/player_list.html', {
                            'error_message': "What's wrong with you!!!!",
    })
    else:
        return HttpResponseRedirect('')

    return render(request, 'ourhockey_playermanager/player_attend_list.html', {
        'player_attend_list': player_attend_list,
    })