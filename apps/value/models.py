# -*- coding: utf-8 -*-

from django.db.models import CharField, ForeignKey, DecimalField
from apps.control.models import ControlModel
from apps.tag.models import Tag
from apps.inspection.models import Inspection

# Create your models here.


class Value(ControlModel):

    class Meta:
        db_table='value'

    tag = ForeignKey(Tag)
    numeric = DecimalField(decimal_places=10, max_digits=50, blank=True, null=True)
    text = CharField(max_length=1000, blank=True, null=True)
    inspection =  ForeignKey(Inspection, related_name='inspection_values')

    def __str__(self):
        return str(self.numeric or self.text) #+' ('+(self.tag.get_unit_display()) or '' +')'


