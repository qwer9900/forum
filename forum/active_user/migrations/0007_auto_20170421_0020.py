# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-20 16:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('active_user', '0006_auto_20170421_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='active_user',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 21, 16, 20, 14, 949892, tzinfo=utc)),
        ),
    ]
