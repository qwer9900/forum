# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-22 11:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20161122_0318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.CharField(max_length=10000, verbose_name='文章内容'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=10, verbose_name='文章标题'),
        ),
    ]
