# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-06 21:31
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tag', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='IForm',
            fields=[
                ('created_when', models.DateTimeField(default=datetime.datetime.now)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'iform',
            },
        ),
        migrations.CreateModel(
            name='TagOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField()),
                ('iform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iform.IForm')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tag.Tag')),
            ],
        ),
        migrations.AddField(
            model_name='iform',
            name='tag',
            field=models.ManyToManyField(related_name='iform_tags', through='iform.TagOrder', to='tag.Tag'),
        ),
    ]
