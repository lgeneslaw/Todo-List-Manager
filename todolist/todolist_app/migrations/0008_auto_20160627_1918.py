# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-27 19:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0007_auto_20160627_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='datetime_completed',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='due',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 27, 19, 18, 38, 264187, tzinfo=utc)),
        ),
    ]
