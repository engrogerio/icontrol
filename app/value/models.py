# -*- coding: utf-8 -*-
from django.db import models
# from __future__ import unicode_literals
from django.db.models import CharField, ForeignKey, DecimalField
from icontrol.models import ControlModel
from app.tag.models import Tag
from app.inspection.models import Inspection
from django.db import models


class Value(ControlModel):

    class Meta:
        db_table='value'
    # TODO: would be better to have a field for integers separatly?
    # TODO: What would be the best aproach to save a decimal number on the db? Float, Double or Decimal?
    tag = ForeignKey(Tag, on_delete=models.CASCADE)
    number = DecimalField(decimal_places=10, max_digits=50, blank=True, null=True)
    text = CharField(max_length=1000, blank=True, null=True)
<<<<<<< HEAD
    inspection = ForeignKey(Inspection, related_name='values', on_delete=models.CASCADE)
=======
    inspection =  ForeignKey(Inspection, related_name='values', on_delete=models.CASCADE)
>>>>>>> 0128cebd3a705f885946dadfc854e54c4cf9443b
    
    def __str__(self):
        return self.text or str(self.number)
