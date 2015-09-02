# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sn_app', '0014_auto_20150828_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photoinphotoset',
            name='order',
            field=models.PositiveIntegerField(),
        ),
    ]
