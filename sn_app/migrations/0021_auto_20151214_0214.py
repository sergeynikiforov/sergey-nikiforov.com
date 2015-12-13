# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sn_app', '0020_photo_date_taken'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photoinphotoset',
            name='order',
            field=models.FloatField(),
        ),
    ]
