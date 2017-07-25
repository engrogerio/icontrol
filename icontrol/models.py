# -*- coding: utf-8 -*-

from django.db.models import ForeignKey, DateTimeField
from django.db import models
from django.contrib.auth.models import User
import datetime

class ControlModel(models.Model):

    class Meta:
        abstract = True
    created_by = ForeignKey(User, null=True, blank=True)
    created_when = DateTimeField(default=datetime.datetime.now)

