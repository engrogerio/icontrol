# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-20 13:37
from __future__ import unicode_literals

import app.iform.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iform', '0003_auto_20170519_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iformtag',
            name='order',
            field=models.IntegerField(),
        ),
    ]