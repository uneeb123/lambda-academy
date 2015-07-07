# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_auto_20150629_2245'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='short_description',
            field=models.TextField(default='adas'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='module',
            name='image_file',
            field=models.ImageField(upload_to=b'school/'),
        ),
    ]
