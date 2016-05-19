# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logre', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResCate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('resc_title', models.CharField(unique=True, max_length=50, verbose_name=b'\xe7\xb1\xbb\xe5\x88\xab\xe5\x90\x8d\xe7\xa7\xb0')),
                ('resc_time', models.DateTimeField(verbose_name=b'\xe4\xb8\x8a\xe4\xbc\xa0\xe6\x97\xb6\xe9\x97\xb4')),
                ('resc_num', models.IntegerField(verbose_name=b'\xe7\xb1\xbb\xe5\x88\xab\xe7\xbc\x96\xe5\x8f\xb7')),
            ],
            options={
                'db_table': 'resource_cate',
            },
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('res_title', models.CharField(max_length=30, verbose_name=b'\xe8\xb5\x84\xe6\xba\x90\xe5\x90\x8d\xe7\xa7\xb0')),
                ('res_time', models.DateTimeField(verbose_name=b'\xe4\xb8\x8a\xe4\xbc\xa0\xe6\x97\xb6\xe9\x97\xb4')),
                ('res_url', models.URLField(verbose_name=b'\xe8\xb5\x84\xe6\xba\x90URL')),
                ('res_seenum', models.IntegerField(default=0, verbose_name=b'\xe6\xb5\x8f\xe8\xa7\x88\xe9\x87\x8f')),
                ('res_downnum', models.IntegerField(default=0, verbose_name=b'\xe4\xb8\x8b\xe8\xbd\xbd\xe9\x87\x8f')),
                ('res_author', models.ForeignKey(related_name='res_author', verbose_name=b'\xe4\xb8\x8a\xe4\xbc\xa0\xe4\xba\xba', to='logre.Author')),
                ('res_cate', models.ForeignKey(related_name='res_cate', verbose_name=b'\xe8\xb5\x84\xe6\xba\x90\xe7\xb1\xbb\xe5\x88\xab', to='download.ResCate')),
            ],
            options={
                'db_table': 'resource',
            },
        ),
    ]
