# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-19 21:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensors', '0003_auto_20161119_2049'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='light',
            field=models.IntegerField(default=0),
        ),
    ]
