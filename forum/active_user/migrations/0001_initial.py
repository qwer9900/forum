# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-29 09:00
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='active_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actice_str', models.CharField(max_length=100, verbose_name='激活码')),
                ('deadline', models.DateTimeField(default=datetime.datetime(2016, 12, 30, 9, 0, 48, 479268, tzinfo=utc))),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户id')),
            ],
        ),
    ]
