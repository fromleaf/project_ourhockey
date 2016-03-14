from django.test import TestCase
from ourhockey_playermanager.models import Player

"""
class AnimalTestCase(TestCase):
    def setUp(self):
        Animal.objects.create(name="lion", sound="roar")
        Animal.objects.create(name="cat", sound="meow")

    def test_animals_can_speak(self):
        # Animals that can speak are correctly identified
        lion = Animal.objects.get(name="lion")
        cat = Animal.objects.get(name="cat")
        self.assertEqual(lion.speak(), 'The lion says "roar"')
        self.assertEqual(cat.speak(), 'The cat says "meow"')
"""      
        
class PlayerTestCase(TestCase):
    def setUp(self):
        Player.objects.create(name="test1", birthday="1984-08-06",
                                  gender="male", back_number=10,
                                  duty="member", position="C",
                                )
        Player.objects.create(name="test2", birthday="1994-08-06",
                              gender="female", back_number=13,
                              duty="boss", position="RF",
                            ) 
        
    def test_get_player_info(self):
         test1 = Player.objects.get(name="test1")
         test2 = Player.objects.get(name="test2")
         self.assertEqual(test1.pk, 1)
         self.assertEqual(test2.pk, 2)
         print "test1: ", test1
         print "test2: ", test2  
