# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-21 05:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geofood', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='zoom',
            field=models.PositiveIntegerField(default=14),
        ),
    ]
