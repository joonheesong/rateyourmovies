# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20161126_1727'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='review',
            field=models.TextField(null=True),
        ),
    ]
