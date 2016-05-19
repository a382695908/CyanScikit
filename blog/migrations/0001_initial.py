# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logre', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('blog_title', models.CharField(unique=True, max_length=20, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('blog_time', models.DateTimeField(verbose_name=b'\xe5\x8f\x91\xe8\xa1\xa8\xe6\x97\xb6\xe9\x97\xb4')),
                ('blog_content', models.TextField(verbose_name=b'\xe5\x86\x85\xe5\xae\xb9')),
                ('blog_seenum', models.IntegerField(default=0, verbose_name=b'\xe6\xb5\x8f\xe8\xa7\x88\xe9\x87\x8f')),
                ('blog_id', models.CharField(unique=True, max_length=20, verbose_name=b'\xe5\x8d\x9a\xe5\xae\xa2\xe7\xbc\x96\xe5\x8f\xb7')),
                ('blog_author', models.ForeignKey(related_name='blog_author', verbose_name=b'\xe4\xbd\x9c\xe8\x80\x85', to='logre.Author')),
            ],
            options={
                'db_table': 'blog',
            },
        ),
        migrations.CreateModel(
            name='Cate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cate_name', models.CharField(max_length=20, verbose_name=b'\xe7\xb1\xbb\xe5\x88\xab')),
                ('cate_time', models.DateTimeField(verbose_name=b'\xe6\xb7\xbb\xe5\x8a\xa0\xe6\x97\xb6\xe9\x97\xb4')),
                ('cate_num', models.IntegerField(verbose_name=b'\xe7\xb1\xbb\xe5\x88\xab\xe7\xbc\x96\xe5\x8f\xb7')),
            ],
            options={
                'db_table': 'blog_cate',
            },
        ),
        migrations.AddField(
            model_name='blog',
            name='blog_cate',
            field=models.ForeignKey(related_name='blog_cate', verbose_name=b'\xe7\xb1\xbb\xe5\x88\xab', to='blog.Cate'),
        ),
    ]
