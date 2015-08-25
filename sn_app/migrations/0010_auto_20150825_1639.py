# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sn_app', '0009_auto_20150722_1649'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('publicID', models.CharField(max_length=200)),
                ('title', models.CharField(default=b'Untitled', max_length=200)),
                ('description', models.TextField(default=b'No description', max_length=2000)),
                ('num_views', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='PhotoInPhotoset',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.PositiveIntegerField(unique=True)),
                ('photo', models.ForeignKey(to='sn_app.Photo')),
            ],
        ),
        migrations.CreateModel(
            name='Photoset',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=2000)),
                ('num_views', models.PositiveIntegerField(default=0)),
                ('num_photos', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='photoinphotoset',
            name='photoset',
            field=models.ForeignKey(to='sn_app.Photoset'),
        ),
        migrations.AddField(
            model_name='photo',
            name='photosets',
            field=models.ManyToManyField(to='sn_app.Photoset', through='sn_app.PhotoInPhotoset'),
        ),
    ]
