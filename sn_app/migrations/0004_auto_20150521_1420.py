# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sn_app', '0003_auto_20150520_1625'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='description_json',
            new_name='achievements_json',
        ),
    ]
