# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-28 20:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0013_auto_20160628_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 28, 20, 59, 9, 278466, tzinfo=utc)),
        ),
    ]