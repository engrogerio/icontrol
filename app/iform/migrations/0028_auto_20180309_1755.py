# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-09 17:55
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('iform', '0027_auto_20180122_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iform',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='iform.IForm'),
        ),
    ]