# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sn_app', '0021_auto_20151214_0214'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='thumbnail_url',
            field=models.URLField(default=b'http://www.example.com/thumbnailURL'),
        ),
    ]
