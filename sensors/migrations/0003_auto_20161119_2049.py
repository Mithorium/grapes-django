# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-19 20:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensors', '0002_auto_20161119_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='avg_humidity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='avg_pressure',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='avg_temp',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='max_humidity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='max_pressure',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='max_temp',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='min_humidity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='min_pressure',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='min_temp',
            field=models.IntegerField(),
        ),
    ]
