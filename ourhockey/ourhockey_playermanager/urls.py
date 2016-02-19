from django.conf.urls import patterns, url
from ourhockey_playermanager import views

urlpatterns = [
    url(r'^$', views.PlayerListView.as_view(), name='players_list'),
    url(r'^players/(?P<pk>\d+)/$', views.PlayerDetailView.as_view(), name='players_detail'),
]