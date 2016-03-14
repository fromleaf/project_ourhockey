from __future__ import unicode_literals

import os.path

from unidecode import unidecode
from django.conf import settings
from django.db import models
from ourhockey_common.models import Person


def get_upload_to(instance, filename):
    # Dumb proxy to instance method.
    return instance.get_upload_to(filename)


class Player(Person):
    back_number = models.IntegerField(default=0)  # Player Back Number
    duty = models.CharField(max_length=255)  # Player Duty
    position = models.CharField(max_length=2)  # Player Position
    member_level = models.CharField(max_length=2, default="03")  # Player Member Level
                                                                        # 00: Member / 01: Pre Member / 02: Guest / 
                                                                        # 03: None Level(default) / 04: Officer
    state = models.CharField(max_length=2, default="00")  # 00: alive / 01: Pause / 02: Not attend
    profile_image = models.ImageField(upload_to=get_upload_to)
    attend = models.BooleanField(default=False)   
                
    def __unicode__(self):  # __str__ on Python3
        return self.name
    
    def get_upload_to(self, filename):
        folder_name = 'static/photo/ourhockey_player/profiles'
        filename = self.profile_image.field.storage.get_valid_name(filename)

        # do a unidecode in the filename and then
        # replace non-ascii characters in filename with _ , to sidestep issues with filesystem encoding
        filename = "".join((i if ord(i) < 128 else '_') for i in unidecode(filename))

        # Truncate filename so it fits in the 100 character limit
        # https://code.djangoproject.com/ticket/9893
        while len(os.path.join(folder_name, filename)) >= 95:
            prefix, dot, extension = filename.rpartition('.')
            filename = prefix[:-1] + dot + extension
        # return filename
        return os.path.join(folder_name, filename)
