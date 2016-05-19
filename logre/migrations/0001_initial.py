# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author_name', models.CharField(max_length=15, verbose_name=b'\xe5\xa7\x93\xe5\x90\x8d')),
                ('author_eamil', models.EmailField(max_length=254, verbose_name=b'\xe9\x82\xae\xe7\xae\xb1')),
                ('author_phone', models.CharField(max_length=11, verbose_name=b'\xe7\x94\xb5\xe8\xaf\x9d', blank=True)),
                ('author_qq', models.CharField(max_length=10, verbose_name=b'QQ', blank=True)),
                ('author_pwd', models.CharField(max_length=50, verbose_name=b'\xe5\xaf\x86\xe7\xa0\x81')),
                ('author_time', models.DateTimeField(verbose_name=b'\xe6\xb3\xa8\xe5\x86\x8c\xe6\x97\xb6\xe9\x97\xb4')),
                ('author_xingqu', models.CharField(max_length=50, verbose_name=b'\xe6\x88\x91\xe7\x9a\x84\xe5\x85\xb4\xe8\xb6\xa3', blank=True)),
            ],
            options={
                'db_table': 'author',
            },
        ),
    ]
