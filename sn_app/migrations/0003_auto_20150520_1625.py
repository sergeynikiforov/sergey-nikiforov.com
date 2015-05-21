# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sn_app', '0002_auto_20150520_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='address',
            field=models.CharField(max_length=500),
        ),
    ]
