# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sn_app', '0010_auto_20150825_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photoset',
            name='title',
            field=models.CharField(unique=True, max_length=200),
        ),
    ]
