# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_auto_20150629_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='contact_number',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
