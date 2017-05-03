# -*- coding: utf-8 -*-

from django.db.models import UUIDField, CharField, ForeignKey, IntegerField, DecimalField, ManyToManyField
import uuid
from django.db import models
from django.contrib.auth.models import User
import datetime

class ControlModel(models.Model):

    class Meta:
        abstract = True
    created_by = models.ForeignKey(User, null=True, blank=True)
    created_when = models.DateTimeField(default=datetime.datetime.now)

