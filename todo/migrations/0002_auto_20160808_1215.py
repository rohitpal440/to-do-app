# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-08 12:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='assigned_at',
            field=models.DateField(default=datetime.datetime(2016, 8, 8, 12, 15, 9, 834639, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='todoitem',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 8, 8, 12, 15, 24, 253672, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='todoitem',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 8, 8, 12, 15, 31, 960568, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
