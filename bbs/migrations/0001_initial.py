# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logre', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='bbs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bbs_title', models.CharField(unique=True, max_length=20, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('bbs_time', models.DateTimeField(verbose_name=b'\xe5\x8f\x91\xe8\xa1\xa8\xe6\x97\xb6\xe9\x97\xb4')),
                ('bbs_content', models.TextField(verbose_name=b'\xe5\x86\x85\xe5\xae\xb9')),
                ('bbs_seenum', models.IntegerField(default=0, verbose_name=b'\xe6\xb5\x8f\xe8\xa7\x88\xe9\x87\x8f')),
                ('bbs_num', models.CharField(default=0, max_length=40, verbose_name=b'\xe7\xbc\x96\xe5\x8f\xb7')),
                ('bbs_author', models.ForeignKey(related_name='bbs_author', verbose_name=b'\xe5\x8f\x91\xe8\xa1\xa8\xe4\xba\xba', to='logre.Author')),
            ],
            options={
                'db_table': 'bbs',
            },
        ),
        migrations.CreateModel(
            name='bbsCate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bc_title', models.CharField(unique=True, max_length=20, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('bc_time', models.DateTimeField(verbose_name=b'\xe5\x8f\x91\xe8\xa1\xa8\xe6\x97\xb6\xe9\x97\xb4')),
                ('bc_num', models.IntegerField(default=0, verbose_name=b'\xe7\xbc\x96\xe5\x8f\xb7')),
            ],
            options={
                'db_table': 'bbscate',
            },
        ),
        migrations.AddField(
            model_name='bbs',
            name='bbs_cate',
            field=models.ForeignKey(related_name='bbs_cate', verbose_name=b'\xe7\xb1\xbb\xe5\x88\xab', to='bbs.bbsCate'),
        ),
    ]
