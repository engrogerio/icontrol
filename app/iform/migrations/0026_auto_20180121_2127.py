# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-21 21:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iform', '0025_auto_20180121_2115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='iformtag',
            name='level',
        ),
        migrations.RemoveField(
            model_name='iformtag',
            name='lft',
        ),
        migrations.RemoveField(
            model_name='iformtag',
            name='rght',
        ),
        migrations.RemoveField(
            model_name='iformtag',
            name='tree_id',
        ),
    ]
