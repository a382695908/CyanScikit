# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-12 18:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_seenum',
            field=models.IntegerField(blank=True, verbose_name='浏览次数'),
        ),
        migrations.AlterField(
            model_name='cate',
            name='cate_name',
            field=models.CharField(max_length=30, verbose_name='文章类别'),
        ),
    ]
