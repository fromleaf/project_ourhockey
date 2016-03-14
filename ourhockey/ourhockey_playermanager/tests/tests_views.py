from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, RequestFactory

from ourhockey_playermanager.models import Player
from ourhockey_playermanager import views

class SimpleViewTest(TestCase):
        def setUp(self):
            # Every test needs access to the request factory.
            self.factory = RequestFactory()
            self.player1 = Player.objects.create(name="test1", birthday="1984-08-06",
                                  gender="male", back_number=10,
                                  duty="member", position="C",
                                )
            self.player2 = Player.objects.create(name="test2", birthday="1994-08-06",
                                  gender="female", back_number=13,
                                  duty="boss", position="RF",
                                )
            
        def test_detail(self):
            request = self.factory.get('/player_detail/(?P<pk>\d+)/')
            request.player = self.player1
            request.pk = self.player1.id
             
            response = views.PlayerDetailView.as_view()(request, pk=request.pk)
            self.assertEqual(response.status_code,200)