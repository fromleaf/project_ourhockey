from __future__ import unicode_literals

from django.db import models
from ourhockey_common.models import Person


class Player(Person):
    back_number = models.IntegerField(default=0)                        # Player Back Number
    duty = models.CharField(max_length=255)                             # Player Duty
    position = models.CharField(max_length=2)                           # Player Position
    player_level = models.CharField(max_length=2, default="03")         # Player Member Level
                                                                        # 00: Member / 01: Pre Member / 02: Guest / 
                                                                        # 03: None Level(default) / 04: Officer
    player_state = models.CharField(max_length=2, default="00")         # 00: alive / 01: Pause / 02: Not attend

    def __unicode__(self):      # __str__ on Python3
        return self.name
    