# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logre', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='bigCate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bcate_name', models.CharField(max_length=30, verbose_name=b'\xe5\xa4\xa7\xe7\xb1\xbb\xe5\x88\xab\xe6\xa0\x87\xe9\xa2\x98')),
                ('bcate_time', models.DateTimeField(verbose_name=b'\xe6\xb7\xbb\xe5\x8a\xa0\xe6\x97\xb6\xe9\x97\xb4')),
                ('bcate_num', models.IntegerField(unique=True, verbose_name=b'\xe5\xa4\xa7\xe7\xb1\xbb\xe5\x88\xab\xe7\xbc\x96\xe5\x8f\xb7')),
            ],
            options={
                'db_table': 'bigcate',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('m_num', models.CharField(unique=True, max_length=40, verbose_name=b'\xe4\xbf\xa1\xe6\x81\xaf\xe7\xbc\x96\xe5\x8f\xb7')),
                ('m_name', models.CharField(max_length=40, verbose_name=b'\xe4\xbf\xa1\xe6\x81\xaf\xe6\xa0\x87\xe9\xa2\x98')),
                ('m_content', models.TextField(default=b'\xe6\xad\xa4\xe4\xbf\xa1\xe6\x81\xaf\xe6\x97\xa0\xe5\x85\xb7\xe4\xbd\x93\xe5\x86\x85\xe5\xae\xb9', max_length=250, verbose_name=b'\xe4\xbf\xa1\xe6\x81\xaf\xe5\x86\x85\xe5\xae\xb9')),
                ('m_price', models.FloatField(default=b'', verbose_name=b'\xe4\xbb\xb7\xe6\xa0\xbc')),
                ('m_from', models.CharField(max_length=30, verbose_name=b'\xe5\x8f\x91\xe5\xb8\x83\xe6\x96\xb9')),
                ('m_cate_xuorfu', models.CharField(default=b'\xe9\x9c\x80\xe6\xb1\x82', max_length=20, verbose_name=b'\xe9\x9c\x80\xe6\xb1\x82or\xe6\x9c\x8d\xe5\x8a\xa1')),
                ('m_tuoing', models.CharField(default=b'\xe5\x90\xa6', max_length=15, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe6\x89\x98\xe7\xae\xa1')),
                ('m_result', models.CharField(default=b'\xe5\x90\xa6', max_length=20, verbose_name=b'\xe4\xba\xa4\xe6\x98\x93\xe6\x98\xaf\xe5\x90\xa6\xe6\x88\x90\xe5\x8a\x9f')),
                ('m_time', models.DateTimeField(verbose_name=b'\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xb6\xe9\x97\xb4')),
                ('m_seenum', models.IntegerField(default=0, verbose_name=b'\xe6\xb5\x8f\xe8\xa7\x88\xe6\xac\xa1\xe6\x95\xb0')),
                ('m_bigcate', models.ForeignKey(verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe5\xa4\xa7\xe7\xb1\xbb\xe5\x88\xab', to='csMarket.bigCate')),
            ],
            options={
                'db_table': 'message',
            },
        ),
        migrations.CreateModel(
            name='smallCate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('scate_name', models.CharField(max_length=30, verbose_name=b'\xe5\xb0\x8f\xe7\xb1\xbb\xe5\x88\xab\xe6\xa0\x87\xe9\xa2\x98')),
                ('scate_time', models.DateTimeField(verbose_name=b'\xe6\xb7\xbb\xe5\x8a\xa0\xe6\x97\xb6\xe9\x97\xb4')),
                ('scate_num', models.IntegerField(unique=True, verbose_name=b'\xe5\xb0\x8f\xe7\xb1\xbb\xe5\x88\xab\xe7\xbc\x96\xe5\x8f\xb7')),
                ('scate_bcate', models.ForeignKey(verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe5\xa4\xa7\xe7\xb1\xbb\xe5\x88\xab', to='csMarket.bigCate')),
            ],
            options={
                'db_table': 'smallcate',
            },
        ),
        migrations.AddField(
            model_name='message',
            name='m_smallcate',
            field=models.ForeignKey(verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe5\xb0\x8f\xe7\xb1\xbb\xe5\x88\xab', to='csMarket.smallCate'),
        ),
        migrations.AddField(
            model_name='message',
            name='m_to',
            field=models.ForeignKey(verbose_name=b'\xe6\x89\x98\xe7\xae\xa1\xe6\x96\xb9', blank=True, to='logre.Author'),
        ),
    ]
