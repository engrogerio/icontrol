# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-18 20:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('value', '0002_auto_20180109_1305'),
    ]

    operations = [
        migrations.RenameField(
            model_name='value',
            old_name='date_created',
            new_name='created_when',
        ),
        migrations.RenameField(
            model_name='value',
            old_name='date_updated',
            new_name='updated_when',
        ),
    ]
