# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-28 08:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_gallery_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='desc',
            field=models.TextField(default='description goes here'),
            preserve_default=False,
        ),
    ]
