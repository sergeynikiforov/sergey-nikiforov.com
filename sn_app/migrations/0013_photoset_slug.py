# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sn_app', '0012_photo_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='photoset',
            name='slug',
            field=models.SlugField(default=True, unique=True),
        ),
    ]
