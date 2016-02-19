from __future__ import unicode_literals

from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=200)         # Name
    birthday = models.DateField()                   # Birthday 
    gender = models.CharField(max_length=10)        # Gender: male or female
    adult = models.BooleanField(default=True)       # Adult: True - Adult, False - Junior

    def __unicode__(self):      # __str__ on Python3
        return self.name