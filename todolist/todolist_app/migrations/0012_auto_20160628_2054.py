# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-28 20:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0011_auto_20160627_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 28, 20, 54, 50, 419536, tzinfo=utc)),
        ),
    ]
