# -*- coding: utf-8 -*-

from django.db.models import ForeignKey
from icontrol.models import ControlModel
from app.iform.models import IForm
from django.db import models


class Inspection(ControlModel):

    class Meta:
        db_table='inspection'

    iform = ForeignKey(IForm, related_name='inspection_iform', on_delete = models.CASCADE, null=True, blank=True)

    def __str__(self):
        created_when = self.created_when
        return self.iform.name +' - '+ '{:%Y-%m-%d %H:%M}'.format(created_when)
