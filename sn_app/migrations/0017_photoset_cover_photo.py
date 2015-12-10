# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sn_app', '0016_photoset_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='photoset',
            name='cover_photo',
            field=models.OneToOneField(null=True, to='sn_app.Photo'),
        ),
    ]
