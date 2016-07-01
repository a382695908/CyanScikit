# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logre', '0003_auto_20160630_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(unique=True, max_length=11, verbose_name=b'\xe7\x94\xb5\xe8\xaf\x9d', blank=True),
        ),
    ]
