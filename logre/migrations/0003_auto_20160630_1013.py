# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logre', '0002_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='wechat',
        ),
        migrations.AddField(
            model_name='user',
            name='eamil',
            field=models.EmailField(max_length=254, verbose_name=b'\xe9\x82\xae\xe7\xae\xb1', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='desc',
            field=models.TextField(verbose_name=b'\xe4\xb8\xaa\xe4\xba\xba\xe6\x8f\x8f\xe8\xbf\xb0', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=11, verbose_name=b'\xe7\x94\xb5\xe8\xaf\x9d', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='qq',
            field=models.CharField(max_length=10, verbose_name=b'QQ', blank=True),
        ),
    ]
