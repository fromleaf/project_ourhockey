from django.conf.urls import patterns, url
from ourhockey_playermanager import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.PlayerModelView.as_view(), name='index'),
    url(r'^player_list/$', views.PlayerListView.as_view(), name='player_list'),
    url(r'^player_detail/(?P<pk>\d+)/$', views.PlayerDetailView.as_view(), name='player_detail'),
    url(r'^player_attend_list/$', views.update_attend, name='player_attend_list'),
]
