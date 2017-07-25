# -*- coding: utf-8 -*-
from django.db.models import UUIDField, CharField, ForeignKey, IntegerField, DecimalField, ManyToManyField
import uuid
from icontrol.models import ControlModel


class Tag(ControlModel):

    class Meta:
        db_table='tag'

    TEXT = 1
    INTEGER = 2
    FLOAT = 3
    REFERENCE = 4
    BOOL = 5
    DATE = 6
    TIME = 7
    DATETIME = 8
    MONEY = 9

    TYPE_CHOICES = ((TEXT, 'Text'), (INTEGER, 'Integer Number'), (FLOAT, 'Float Point Number'),
                    (REFERENCE, 'Reference'), (BOOL, 'Yes/No'), (DATE, 'Date'), (TIME, 'Time'),
                    (DATETIME, 'Date and Time')
                    )

    UNIT_CHOICES = ((1, '°C'), (2, 'Kg'), (3, 'm'), (4, 's'))

    id = UUIDField(primary_key=True, default=uuid.uuid4, )
    name = CharField(max_length=255)
    type = IntegerField('Field Type', choices=TYPE_CHOICES, blank=True, null=True)
    unit = IntegerField('Unit', choices=UNIT_CHOICES, blank=True, null=True)
    decimal_places = IntegerField(default=0)
    max_length = IntegerField(default=0) # 0 means no limit or 1000 characteres
    required = IntegerField('Required', choices=((1, 'Yes'),(0,'No')), default=1)
    #default_value = CharField(max_length=1000, null=True, blank=True)

    def __unicode__(self):
        if self.unit:
            return self.name + ' ('+self.get_unit_display()+')'
        else:
            return self.name

    def get_tag(self, id):
        return Tag