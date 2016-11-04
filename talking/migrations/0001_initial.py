# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='talk',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('talk_tag', models.CharField(blank=True, verbose_name='归属', max_length=64)),
                ('talk_time', models.DateTimeField(verbose_name='评论时间')),
                ('talk_name', models.CharField(blank=True, verbose_name='昵称', max_length=32)),
                ('talk_email', models.EmailField(verbose_name='邮箱', max_length=254)),
                ('talk_content', models.TextField(verbose_name='评论内容')),
            ],
            options={
                'db_table': 'talking',
            },
        ),
    ]
