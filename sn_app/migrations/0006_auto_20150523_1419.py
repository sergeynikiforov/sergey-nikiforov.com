# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sn_app', '0005_contactme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactme',
            name='time_sent',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
