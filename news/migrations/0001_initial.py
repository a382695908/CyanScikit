# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('news_title', models.CharField(verbose_name='新闻标题', max_length=30)),
                ('news_id', models.CharField(unique=True, verbose_name='唯一ID', max_length=64)),
                ('news_seenum', models.IntegerField(verbose_name='浏览次数')),
                ('news_time', models.DateTimeField(verbose_name='发表时间')),
                ('news_content', models.TextField(verbose_name='新闻内容')),
            ],
            options={
                'db_table': 'news',
            },
        ),
    ]
