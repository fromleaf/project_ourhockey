# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-21 12:26
from __future__ import unicode_literals

from django.db import migrations, models
import ourhockey_playermanager.models


class Migration(migrations.Migration):

    dependencies = [
        ('ourhockey_playermanager', '0004_auto_20160221_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='profile_image',
            field=models.ImageField(upload_to=ourhockey_playermanager.models.get_upload_to, verbose_name='profile_image'),
        ),
    ]
