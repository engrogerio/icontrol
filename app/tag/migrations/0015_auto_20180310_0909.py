# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-10 09:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0014_auto_20180122_1806'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='lpl',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='lsl',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='upl',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='usl',
        ),
    ]