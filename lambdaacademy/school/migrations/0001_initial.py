# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('max_participants', models.IntegerField(null=True)),
                ('current_participants', models.IntegerField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('f_name', models.CharField(max_length=20)),
                ('l_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('contact_number', models.CharField(max_length=10)),
                ('confirmed', models.BooleanField(default=False)),
                ('best_suited_time', models.TimeField(null=True)),
                ('course_registered', models.ForeignKey(to='school.Module')),
            ],
        ),
    ]
