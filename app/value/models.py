# -*- coding: utf-8 -*-

from django.db.models import CharField, ForeignKey, DecimalField, CASCADE
from icontrol.models import ControlModel
from app.tag.models import Tag
from app.inspection.models import Inspection

# Create your models here.


class Value(ControlModel):

    class Meta:
        db_table='value'
    # TODO: would be better to have a field for integers separatly?
    # TODO: What would be the best aproach to save a decimal number on the db? Float, Double or Decimal?
    tag = ForeignKey(Tag, on_delete=CASCADE,)
    number = DecimalField(decimal_places=10, max_digits=50, blank=True, null=True)
    text = CharField(max_length=1000, blank=True, null=True)
    inspection =  ForeignKey(Inspection, on_delete=CASCADE, related_name='values')
    
    def __str__(self):
        return str(self.text) or str(self.number)
