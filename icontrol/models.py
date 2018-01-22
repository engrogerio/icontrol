# -*- coding: utf-8 -*-

from django.db.models import ForeignKey, DateTimeField
from django.db import models
from django.contrib.auth.models import User
import datetime

class ControlModel(models.Model):

    class Meta:
        abstract = True

    @staticmethod
    def get_related_name():
        return '%(app_label)s_%(class)s'

    created_by = ForeignKey(User, null=True, blank=True,related_name="created"+get_related_name.__func__())
    updated_by = ForeignKey(User, null=True, blank=True, related_name="updated"+get_related_name.__func__())
    created_when = DateTimeField(auto_now_add=True)
    updated_when = DateTimeField(auto_now=True)

     