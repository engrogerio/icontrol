# -*- coding: utf-8 -*-

from django.db.models import UUIDField, CharField, ForeignKey, IntegerField, FloatField, ManyToManyField
import uuid
from icontrol.models import ControlModel
import django_tables2 as tables
from django_tables2.utils import A
import django_filters
from app.iform.models import IFormTag
import pint
from mptt.models import MPTTModel, TreeForeignKey

class Tag( MPTTModel, ControlModel):

    class Meta:
        db_table='tag'

    class MPTTMeta:
        order_insertion_by = ['name']


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
    

    TYPE_CHOICES = ((TEXT, 'Text'), (INTEGER, 'Integer Number'), (FLOAT, 'Float Point Number'),
                    (CHOICES, 'Choices'), (BOOL, 'Yes/No'), (DATE, 'Date'), (TIME, 'Time'),
                    (DATETIME, 'Date and Time'), # (MONEY, 'Money'), 
                    (FILE, 'File'), (SECTION, 'Section'),
                    (LARGE_TEXT, 'Large Text'), (RADIO, 'Radio Button'),
                    )

    UNIT_CHOICES = [(units, units) for units in dir(pint.UnitRegistry())]

    id = UUIDField(primary_key=True, default=uuid.uuid4, )
    name = CharField(max_length=255)
    type = IntegerField('Field Type', choices=TYPE_CHOICES, blank=True, null=True)
    unit = CharField('Unit', choices=UNIT_CHOICES, blank=True, null=True, max_length=40)
    decimal_places = IntegerField(default=0)
    usl = FloatField('USL', blank=True, null=True)
    lsl = FloatField('LSL', blank=True, null=True)
    upl = FloatField('UPL', blank=True, null=True)
    lpl = FloatField('LPL', blank=True, null=True)
    max_length = IntegerField(default=0) # 0 means no limit or 1000 characteres
    choices_source = ForeignKey('Tag', blank=True, null=True )
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', db_index=True)
    help_text = CharField('Help Text', blank=True, null=True, max_length=255)

    def __unicode__(self):
        if self.unit:
            return self.name + ' ('+self.get_unit_display()+')'
        else:
            return self.name

    #@property
    def form(self):    
        return self.iformtag_tag__iform__name

    # TODO: fix to show trees on the dropdowns for tag
    # https://djangopy.org/package-of-week/categories-with-django-mptt/
    # this currently has no functionality and its here just for reference.
    def get_slug_list(self):
    		try:
			ancestors = self.get_ancestors(include_self=True)
		except:
			ancestors = []
		else:
			ancestors = [ i.slug for i in ancestors]
		slugs = []
		for i in range(len(ancestors)):
			slugs.append('/'.join(ancestors[:i+1]))
		return slugs


class TagTable(tables.Table):

    name = tables.LinkColumn('tag:tag_update', args=[A('pk')]) # link for editing
    delete = tables.LinkColumn('tag:tag_delete', args=[A('pk')],text='delete',orderable=False) # link for deleting

    
    class Meta:
        model = Tag
        fields = ('parent', 'name', 'unit', 'type', 'created_when' )
        attrs = {"class": "table-striped table-bordered"}
        empty_text = "There are no tags matching the search criteria..."

