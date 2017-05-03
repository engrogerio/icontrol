# -*- coding: utf-8 -*-

from django.db.models import ForeignKey, UUIDField
import uuid
from apps.control.models import ControlModel
from apps.iform.models import IForm


class Inspection(ControlModel):

    class Meta:
        db_table='inspection'

    iform = ForeignKey(IForm, related_name='inspection_iform', null=True, blank=True)
