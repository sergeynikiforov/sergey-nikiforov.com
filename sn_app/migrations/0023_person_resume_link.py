# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sn_app', '0022_photo_thumbnail_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='resume_link',
            field=models.URLField(default=b'http://www.example.com'),
        ),
    ]
