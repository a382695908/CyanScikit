# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='example',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('ex_title', models.CharField(verbose_name='案例标题', max_length=30)),
                ('ex_id', models.CharField(unique=True, verbose_name='唯一ID', max_length=64)),
                ('ex_seenum', models.IntegerField(verbose_name='浏览次数')),
                ('ex_money', models.IntegerField(verbose_name='成交金额', blank=True)),
                ('ex_gree', models.FloatField(verbose_name='满意度', blank=True)),
                ('ex_time', models.DateTimeField(verbose_name='发表时间')),
                ('ex_content', models.TextField(verbose_name='案例描述')),
            ],
            options={
                'db_table': 'example',
            },
        ),
        migrations.CreateModel(
            name='wcate',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('wcate_name', models.CharField(verbose_name='外包类别', max_length=30)),
                ('wcate_addtime', models.DateTimeField(verbose_name='类别添加时间', blank=True)),
                ('wcate_id', models.IntegerField(unique=True, verbose_name='类别编号')),
                ('wcate_content', models.TextField(verbose_name='类别介绍')),
            ],
            options={
                'db_table': 'waibao_cate',
            },
        ),
        migrations.AddField(
            model_name='example',
            name='ex_category',
            field=models.ForeignKey(to='market.wcate', related_name='article_cate', verbose_name='类别'),
        ),
    ]
