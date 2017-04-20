# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-20 07:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('article', '0005_article_owner'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=10000, verbose_name='评论内容')),
                ('status', models.IntegerField(choices=[(0, '正常'), (-1, '关闭')], verbose_name='状态')),
                ('create_timestamp', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('last_timestamp', models.DateTimeField(auto_now=True, verbose_name='最后更新时间')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.Article', verbose_name='文章ID')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
            options={
                'verbose_name_plural': '评论',
                'verbose_name': '评论',
            },
        ),
    ]
