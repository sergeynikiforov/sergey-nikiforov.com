# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sn_app', '0010_auto_20150825_1515'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='albums',
            new_name='photosets',
        ),
    ]
