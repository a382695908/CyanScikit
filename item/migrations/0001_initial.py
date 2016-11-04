# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='item',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('item_title', models.CharField(verbose_name='文章标题', max_length=30)),
                ('item_id', models.CharField(unique=True, verbose_name='文章唯一ID', max_length=64)),
                ('item_seenum', models.IntegerField(verbose_name='浏览次数')),
                ('item_time', models.DateTimeField(verbose_name='发表时间')),
                ('item_content', models.TextField(verbose_name='文章内容')),
            ],
            options={
                'db_table': 'item',
            },
        ),
    ]
