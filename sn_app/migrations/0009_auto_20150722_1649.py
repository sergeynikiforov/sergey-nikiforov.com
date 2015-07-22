# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sn_app', '0008_job_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='description',
        ),
        migrations.AddField(
            model_name='employer',
            name='description',
            field=models.TextField(default='descr', max_length=1000),
            preserve_default=False,
        ),
    ]
