# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_auto_20161128_0106'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.FloatField()),
                ('review', models.TextField(null=True)),
                ('m_id', models.ForeignKey(to='webapp.Movie', db_column='m_id')),
                ('username', models.ForeignKey(to='webapp.User', db_column='username')),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='m_id',
        ),
        migrations.RemoveField(
            model_name='post',
            name='username',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
