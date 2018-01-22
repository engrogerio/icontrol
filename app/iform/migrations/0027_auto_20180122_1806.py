# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-22 18:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('iform', '0026_auto_20180121_2127'),
    ]

    operations = [
        migrations.AddField(
            model_name='iform',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updatediform_iform', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='iform',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='creatediform_iform', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='iform',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='get_related_name', to='iform.IForm'),
        ),
    ]
