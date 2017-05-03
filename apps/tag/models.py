# -*- coding: utf-8 -*-

from django.db.models import UUIDField, CharField, ForeignKey, IntegerField, DecimalField, ManyToManyField
import uuid
from apps.control.models import ControlModel
from apps.inspection.models import Inspection

# Create your models here.

#
# class FieldType(ControlModel):
#     name = CharField(max_length=20)
#
#     def __str__(self):
#         return self.name
#
#
# class Unit(ControlModel):
#     name = CharField(max_length=25)
#     symbol = CharField(max_length=10, null=True, blank=True)
#     unit_of = CharField(max_length=25, null=True, blank=True)
#
#     def __str__(self):
#         return self.name+' ( '+self.symbol+' )'


class Tag(ControlModel):

    class Meta:
        db_table='tag'

    TYPE_CHOICES = ((1, 'Text'), (2, 'Integer Number'), (3, 'Float Point Number'), (4, 'Reference'))
    UNIT_CHOICES = ((1, '°C'), (2, 'Kg'), (3, 'm'), (4, 's'))

    id = UUIDField(primary_key=True, default=uuid.uuid4, ) #editable=False)
    name = CharField(max_length=255)
    type = IntegerField('Field Type', choices=TYPE_CHOICES, blank=True, null=True)
    unit = IntegerField('Unit', choices=UNIT_CHOICES, blank=True, null=True)
    decimal_places = IntegerField(default=0)


    def __str__(self):
        # if self.unit:
        return self.name #+'('+self.get_unit_display+')'
        # else:
        # return self.name

