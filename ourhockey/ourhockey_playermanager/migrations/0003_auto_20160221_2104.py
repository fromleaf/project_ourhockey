# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-21 12:04
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import ourhockey_playermanager.models


class Migration(migrations.Migration):

    dependencies = [
        ('ourhockey_playermanager', '0002_player_player_profile_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='player_level',
            new_name='member_level',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='player_state',
            new_name='state',
        ),
        migrations.RemoveField(
            model_name='player',
            name='player_profile_photo',
        ),
        migrations.AddField(
            model_name='player',
            name='profile_image',
            field=models.ImageField(default=datetime.datetime(2016, 2, 21, 12, 4, 59, 800873, tzinfo=utc), upload_to=ourhockey_playermanager.models.get_upload_to),
            preserve_default=False,
        ),
    ]
