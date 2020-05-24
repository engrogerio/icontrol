# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db.models import ForeignKey
from icontrol.models import ControlModel
from app.iform.models import IForm
from django.db import models

@python_2_unicode_compatible
class Inspection(ControlModel):

    class Meta:
        db_table='inspection'

    iform = ForeignKey(IForm, related_name='inspection_iform', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        created_when = self.created_when
        return self.iform.name +' - '+ created_when.strftime("%Y-%m-%d %H:%M")
