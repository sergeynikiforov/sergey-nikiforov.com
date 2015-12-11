# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sn_app', '0018_remove_photoset_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='photoset',
            name='short_description',
            field=models.TextField(default=b'Vehicula sem libero per ipsum donec, ante vitae neque mauris, integer quisque et nisl, etiam veritatis pede commodo sed penatibus vel, erat ac suspendisse ipsum enim tristique orci.', max_length=1000),
        ),
    ]
