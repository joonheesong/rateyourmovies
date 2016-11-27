# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('m_id', models.PositiveIntegerField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('director', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=50)),
                ('runtime', models.PositiveIntegerField()),
                ('poster_path', models.CharField(max_length=100)),
                ('published_year', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('rating', models.FloatField()),
                ('m_id', models.ForeignKey(unique=True, db_column='m_id', to='webapp.Movie')),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(unique=True, max_length=254),
        ),
        migrations.AddField(
            model_name='post',
            name='username',
            field=models.ForeignKey(unique=True, db_column='username', to='webapp.User'),
        ),
    ]
