# -*- coding: utf-8 -*-

from django.db.models import ForeignKey
from icontrol.models import ControlModel
from app.iform.models import IForm
from django.db import models
import django_tables2 as tables
from django_tables2.utils import A


class Inspection(ControlModel):

    class Meta:
        db_table = 'inspection'

    iform = ForeignKey(IForm, related_name='inspection_iform', on_delete=models.CASCADE, null=True, blank=True)
    parent = ForeignKey(IForm, related_name='parent_iform', on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        created_when = self.created_when
        return f'{self.iform.name} - {created_when.strftime("%Y-%m-%d %H:%M")}'

class InspectionTable(tables.Table):
    
    iform__name = tables.LinkColumn('inspection:inspection_update', args=[A('pk')]) # link for editing
    delete = tables.LinkColumn('inspection:inspection_delete', args=[A('pk')], text='delete', orderable=False) # link for deleting

    
    class Meta:
        model = Inspection
        fields = ('iform__name', 'created_by', 'created_when')
        attrs = {"class": "table-striped table-bordered"}
        empty_text = "There are no inspections matching the search criteria..."
        attrs = {"class": "table-striped table-bordered"}
        