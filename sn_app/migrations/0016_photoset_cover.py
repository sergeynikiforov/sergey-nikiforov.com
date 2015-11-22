# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sn_app', '0015_auto_20150902_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='photoset',
            name='cover',
            field=models.CharField(default=b'choose_coverID_plz', max_length=200),
        ),
    ]
