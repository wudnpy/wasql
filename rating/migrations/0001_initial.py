# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-19 13:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Indicators',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=255)),
                ('indicator', models.TextField()),
                ('calculation', models.CharField(max_length=255)),
            ],
        ),
    ]
