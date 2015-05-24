# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sn_app', '0006_auto_20150523_1419'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='education',
            options={'verbose_name': 'Education entry', 'verbose_name_plural': 'Education entries'},
        ),
        migrations.RenameField(
            model_name='contactme',
            old_name='sender_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='contactme',
            old_name='sender_name',
            new_name='name',
        ),
    ]
