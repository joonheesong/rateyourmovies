# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_auto_20161129_0207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posting',
            name='rating',
            field=models.IntegerField(null=True),
        ),
    ]
