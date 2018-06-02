# -*- coding: utf-8 -*-

from django.db.models import ForeignKey
from icontrol.models import ControlModel
from app.iform.models import IForm


class Inspection(ControlModel):

    class Meta:
        db_table='inspection'

    iform = ForeignKey(IForm, related_name='inspection_iform', null=True, blank=True)

    def __unicode__(self):
        created_when = self.created_when
        return self.iform.name +' - '+ created_when.strftime("%Y-%m-%d %H:%M")