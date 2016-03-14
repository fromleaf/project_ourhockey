from django.test import TestCase
from django.contrib.auth import get_user_model

from ourhockey_playermanager.models import Player
from ourhockey_playermanager.forms import AttendCheckForm

"""
def test_valid_form(self):
    w = Whatever.objects.create(title='Foo', body='Bar')
    data = {'title': w.title, 'body': w.body,}
    form = WhateverForm(data=data)
    self.assertTrue(form.is_valid())

def test_invalid_form(self):
    w = Whatever.objects.create(title='Foo', body='')
    data = {'title': w.title, 'body': w.body,}
    form = WhateverForm(data=data)
    self.assertFalse(form.is_valid())
    
"""


class SimpleViewTest(TestCase):
    def setUp(self):
        Player.objects.create(name="test1", birthday="1984-08-06",
                              gender="male", back_number=10,
                              duty="member", position="C",
                              attend=True,                              
                            )
    
    def test_valid_form(self):
        print 'start test_valid_form()'
        player = Player.objects.get(name="test1")
        data = {'attend': player.attend}
        form = AttendCheckForm(data=data)
        self.assertTrue(form.is_valid())