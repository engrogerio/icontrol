# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-08 11:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iform', '0019_iformtag_help_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='iformtag',
            name='help_text',
        ),
        migrations.AddField(
            model_name='iformtag',
            name='width',
            field=models.IntegerField(default=100),
        ),
    ]
