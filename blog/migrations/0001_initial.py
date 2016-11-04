# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('blog_title', models.CharField(verbose_name='文章标题', max_length=30)),
                ('blog_id', models.CharField(unique=True, verbose_name='文章唯一ID', max_length=64)),
                ('blog_seenum', models.IntegerField(verbose_name='浏览次数')),
                ('blog_time', models.DateTimeField(verbose_name='发表时间')),
                ('blog_content', models.TextField(verbose_name='文章内容')),
            ],
            options={
                'db_table': 'blog',
            },
        ),
        migrations.CreateModel(
            name='cate',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('cate_name', models.CharField(verbose_name='美文类别', max_length=30)),
                ('cate_addtime', models.DateTimeField(verbose_name='类别添加时间', blank=True)),
                ('cate_id', models.IntegerField(unique=True, verbose_name='类别编号')),
            ],
            options={
                'db_table': 'blog_cate',
            },
        ),
        migrations.AddField(
            model_name='blog',
            name='blog_category',
            field=models.ForeignKey(to='blog.cate', related_name='article_cate', verbose_name='类别'),
        ),
    ]
