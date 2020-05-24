# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from django.db.models import UUIDField, CharField, ForeignKey, IntegerField, FloatField, ManyToManyField
import uuid
from icontrol.models import ControlModel
import django_tables2 as tables
from django_tables2.utils import A
from app.iform.models import IFormTag
import pint
from fontawesome_5.fields import IconField


class Tag(ControlModel):

    class Meta:
        db_table='tag'

    icon = IconField()
      
    TEXT = 1
    INTEGER = 2
    FLOAT = 3
    CHOICES = 4
    BOOL = 5
    DATE = 6
    TIME = 7
    DATETIME = 8
    MONEY = 9
    FILE = 10
    SECTION = 11
    LARGE_TEXT = 12
    RADIO = 13
    

    JSGRID_TYPE = ((TEXT, 'text'), (INTEGER, 'number'), (FLOAT, 'number'),
                    (CHOICES, 'select'), (BOOL, 'checkbox'), (DATE, 'date'), (TIME, 'time'),
                    (DATETIME, 'datetime'), 
                    (FILE, 'File'), (SECTION, 'section'),
                    (LARGE_TEXT, 'textarea'), (RADIO, 'radiobutton'),
                    )

    TYPE_CHOICES = ((TEXT, 'Text'), (INTEGER, 'Integer Number'), (FLOAT, 'Float Point Number'),
                    (CHOICES, 'Choices'), (BOOL, 'Yes/No'), (DATE, 'Date'), (TIME, 'Time'),
                    (DATETIME, 'Date and Time'), # (MONEY, 'Money'), 
                    (FILE, 'File'), (SECTION, 'Section'),
                    (LARGE_TEXT, 'Text Area'), (RADIO, 'Radio Button'),
                    )

    UNIT_CHOICES = [(units, units) for units in dir(pint.UnitRegistry())]

    id = UUIDField(primary_key=True, default=uuid.uuid4, )
    name = CharField(max_length=255)
    type = IntegerField('Field Type', choices=TYPE_CHOICES, blank=True, null=True)
    unit = CharField('Unit', choices=UNIT_CHOICES, blank=True, null=True, max_length=100)
    decimal_places = IntegerField(default=0)
 
    max_length = IntegerField(default=100) # 0 means no limit or 1000 characteres
    choices_source = ForeignKey('Tag', blank=True, null=True,
                                on_delete=models.CASCADE)
    parent = ForeignKey('self', blank=True, null=True, related_name='children', 
                        db_index=True, on_delete=models.CASCADE)
    help_text = CharField('Help Text', blank=True, null=True, max_length=255)

    def __str__(self):
        if self.unit:
            return self.name + ' ('+self.get_unit_display()+')'
        else:
            return self.name

    #@property
    def form(self):    
        return self.iformtag_tag__iform__name

    #@property
    def jsgrid_type(self): 
        type_dic = dict(self.JSGRID_TYPE) 
        return type_dic[self.type]
        
class TagTable(tables.Table):

    name = tables.LinkColumn('tag:tag_update', args=[A('pk')]) # link for editing
    delete = tables.LinkColumn('tag:tag_delete', args=[A('pk')],text='delete',orderable=False) # link for deleting

    
    class Meta:
        model = Tag
        fields = ('parent', 'name', 'unit', 'type', 'created_when' )
        attrs = {"class": "table-striped table-bordered"}
        empty_text = "There are no tags matching the search criteria..."
        attrs = {"class": "table-striped table-bordered"}
        


