# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sn_app', '0019_photoset_short_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='date_taken',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
