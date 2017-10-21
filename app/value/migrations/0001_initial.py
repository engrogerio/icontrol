# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-19 20:03
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inspection', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tag', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Value',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_when', models.DateTimeField(default=datetime.datetime.now)),
                ('number', models.DecimalField(blank=True, decimal_places=10, max_digits=50, null=True)),
                ('text', models.CharField(blank=True, max_length=1000, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('inspection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='values', to='inspection.Inspection')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tag.Tag')),
            ],
            options={
                'db_table': 'value',
            },
        ),
    ]