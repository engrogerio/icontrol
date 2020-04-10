# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db.models import ForeignKey
from icontrol.models import ControlModel
from app.iform.models import IForm
from django.db import models

class Inspection(ControlModel):

    class Meta:
        db_table='inspection'

    iform = ForeignKey(IForm, related_name='inspection_iform', null=True, blank=True
                       , on_delete=models.CASCADE)

    def __str__(self):
        created_when = self.created_when
        return self.iform.name +' - '+ created_when.strftime("%Y-%m-%d %H:%M")
