# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-20 20:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='content',
            field=models.CharField(max_length=10, verbose_name='内容'),
        ),
    ]
