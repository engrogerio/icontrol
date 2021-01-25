# -*- coding: utf-8 -*-

from django.db.models import ForeignKey, DateTimeField, BooleanField
from django.db import models
from django.contrib.auth.models import User
import datetime

class ControlModel(models.Model):

    class Meta:
        abstract = True
    # thanks to https://stackoverflow.com/questions/42899817
    @staticmethod
    def get_related_name():
        return '%(app_label)s_%(class)s'

    created_by = ForeignKey(User, null=True, blank=True,related_name="created"+get_related_name.__func__()
                            , on_delete=models.CASCADE)
    updated_by = ForeignKey(User, null=True, blank=True, related_name="updated"+get_related_name.__func__()
                            , on_delete=models.CASCADE)
    created_when = DateTimeField(auto_now_add=True)
    updated_when = DateTimeField(auto_now=True)
    is_active = BooleanField(default=True)