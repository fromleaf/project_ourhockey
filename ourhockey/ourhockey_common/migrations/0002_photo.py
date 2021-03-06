# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-21 08:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ourhockey_common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_file', models.ImageField(upload_to='%Y/%m/%d')),
                ('filtered_image_file', models.ImageField(upload_to='static_files/photo/uploaded/%Y/%m/%d')),
                ('description', models.TextField(blank=True, max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
