# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-21 21:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('block', '0002_auto_20161121_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='status',
            field=models.IntegerField(choices=[(0, '正常'), (-1, '关闭')], verbose_name='状态'),
        ),
    ]
