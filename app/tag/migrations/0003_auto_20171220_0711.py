# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-20 07:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0002_auto_20171014_1422'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='default_value',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='required',
        ),
    ]
