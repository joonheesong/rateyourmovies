# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_auto_20161127_0248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='m_id',
            field=models.ForeignKey(to='webapp.Movie', db_column='m_id'),
        ),
        migrations.AlterField(
            model_name='post',
            name='username',
            field=models.ForeignKey(to='webapp.User', db_column='username'),
        ),
    ]
