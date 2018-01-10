# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-09 13:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0008_auto_20180108_1141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='created_when',
        ),
        migrations.AddField(
            model_name='tag',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tag',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
