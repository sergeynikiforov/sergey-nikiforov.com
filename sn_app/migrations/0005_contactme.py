# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sn_app', '0004_auto_20150521_1420'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sender_name', models.CharField(max_length=100)),
                ('sender_email', models.EmailField(max_length=254)),
                ('message', models.TextField(max_length=2000)),
                ('time_sent', models.TimeField()),
            ],
            options={
                'verbose_name': 'ContactMe message',
                'verbose_name_plural': 'ContactMe messages',
            },
        ),
    ]
