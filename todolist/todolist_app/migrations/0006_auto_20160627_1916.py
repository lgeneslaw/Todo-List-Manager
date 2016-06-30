# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-27 19:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0005_auto_20160627_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='datetime_completed',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='due',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 27, 19, 16, 44, 289610, tzinfo=utc)),
        ),
    ]
