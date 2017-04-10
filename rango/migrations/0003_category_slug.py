# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20170410_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2017, 4, 10, 14, 54, 25, 97000, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
