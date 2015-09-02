# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sn_app', '0013_photoset_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photoset',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
