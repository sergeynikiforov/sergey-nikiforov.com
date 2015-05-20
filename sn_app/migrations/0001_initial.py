# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('college', models.CharField(max_length=500)),
                ('location', models.CharField(max_length=500)),
                ('website', models.URLField(max_length=300)),
                ('degree', models.CharField(max_length=100)),
                ('major', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
            options={
                'verbose_name': 'Education',
                'verbose_name_plural': 'Education',
            },
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=500)),
                ('location', models.CharField(max_length=500)),
                ('website', models.URLField(max_length=300)),
                ('number_of_employees', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Employer',
                'verbose_name_plural': 'Employers',
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('position', models.CharField(max_length=300)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('description_json', models.CharField(max_length=1000)),
                ('employer', models.ForeignKey(to='sn_app.Employer')),
            ],
            options={
                'verbose_name': 'Job',
                'verbose_name_plural': 'Jobs',
            },
        ),
        migrations.CreateModel(
            name='OnlineCourse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=500)),
                ('school', models.CharField(max_length=500)),
                ('date', models.DateField()),
                ('url', models.URLField(max_length=300)),
            ],
            options={
                'verbose_name': 'Online Course',
                'verbose_name_plural': 'Online Courses',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=100)),
                ('birthdate', models.DateField()),
                ('address', models.URLField(max_length=500)),
                ('email', models.EmailField(max_length=254)),
                ('telephone', models.CharField(max_length=50)),
                ('facebook_link', models.URLField(max_length=300)),
                ('linkedin_link', models.URLField(max_length=300)),
                ('instagram_link', models.URLField(max_length=300)),
                ('flickr_link', models.URLField(max_length=300)),
                ('github_link', models.URLField(max_length=300)),
                ('twitter_link', models.URLField(max_length=300)),
                ('skills_json', models.CharField(max_length=1000)),
                ('hobbies_json', models.CharField(max_length=1000)),
            ],
            options={
                'verbose_name': 'Person',
            },
        ),
        migrations.AddField(
            model_name='onlinecourse',
            name='person',
            field=models.ForeignKey(to='sn_app.Person'),
        ),
        migrations.AddField(
            model_name='job',
            name='person',
            field=models.ForeignKey(to='sn_app.Person'),
        ),
        migrations.AddField(
            model_name='education',
            name='person',
            field=models.ForeignKey(to='sn_app.Person'),
        ),
    ]
