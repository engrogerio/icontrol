# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from icontrol.models import ControlModel
from django.db.models import CharField, IntegerField

# Create your models here.
class Chart(ControlModel):
    name = CharField(max_length=255)
    type = IntegerField('Chart Type', blank=True, null=True)
