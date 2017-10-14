# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-13 18:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0002_query_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='query',
            options={'ordering': ['number'], 'verbose_name': 'Запрос', 'verbose_name_plural': 'Запросы'},
        ),
        migrations.AddField(
            model_name='query',
            name='q_type',
            field=models.IntegerField(default=0),
        ),
    ]
