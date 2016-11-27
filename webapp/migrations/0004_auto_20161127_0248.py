# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_post_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='director',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='genre',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='published_year',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='runtime',
        ),
        migrations.AddField(
            model_name='movie',
            name='release_date',
            field=models.CharField(null=True, max_length=10),
        ),
    ]
