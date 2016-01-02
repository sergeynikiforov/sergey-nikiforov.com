# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sn_app', '0024_photo_medium_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='large_url',
            field=models.URLField(default=b'http://www.example.com/largeURL'),
        ),
    ]
