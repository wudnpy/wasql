# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-13 05:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PizzaShop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('logo', models.ImageField(upload_to='pizzashop_log/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='pizzashhop', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
