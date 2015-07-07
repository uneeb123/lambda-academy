# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_participant_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='module',
            old_name='end_date',
            new_name='registration_deadline',
        ),
        migrations.RemoveField(
            model_name='module',
            name='start_date',
        ),
        migrations.AddField(
            model_name='module',
            name='image_file',
            field=models.ImageField(default=datetime.datetime(2015, 6, 29, 22, 45, 17, 582726, tzinfo=utc), upload_to=b'/school/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='module',
            name='number_of_days',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
    ]
