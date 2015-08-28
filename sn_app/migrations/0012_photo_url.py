# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sn_app', '0011_auto_20150827_2101'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='url',
            field=models.URLField(default=b'http://www.example.com'),
        ),
    ]
