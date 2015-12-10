# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sn_app', '0017_photoset_cover_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photoset',
            name='cover',
        ),
    ]
