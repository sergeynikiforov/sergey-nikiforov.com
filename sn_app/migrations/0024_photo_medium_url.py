# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sn_app', '0023_person_resume_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='medium_url',
            field=models.URLField(default=b'http://www.example.com/mediumURL'),
        ),
    ]
