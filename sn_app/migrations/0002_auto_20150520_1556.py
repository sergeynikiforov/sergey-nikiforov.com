# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sn_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='description_json',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='person',
            name='hobbies_json',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='person',
            name='skills_json',
            field=models.TextField(max_length=1000),
        ),
    ]
