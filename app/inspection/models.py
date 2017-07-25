# -*- coding: utf-8 -*-

from django.db.models import ForeignKey
from icontrol.models import ControlModel
from app.iform.models import IForm


class Inspection(ControlModel):

    class Meta:
        db_table='inspection'

    iform = ForeignKey(IForm, related_name='inspection_iform', null=True, blank=True)

    def __unicode__(self):
        return self.iform.name.encode('utf-8')